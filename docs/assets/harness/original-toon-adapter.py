"""Reviewed adapter to the original upstream stateless TOON codec.

No model/tool execution or GPU admission. Only tool-result representation changes;
unsupported/ambiguous/non-roundtripping content stays byte-identical JSON.
Native-token benefit and actual model quality remain separate experimental gates.
"""
import copy
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import time

ARMS=('reference','upstream-tool-toon-v1')
CODEC='/harness/caveman-engine'
CODEC_SHA256='80189ce6b009ea9fba762cdef88d568f20a8640fde4302f50a2cfcb36ab1d754'
_CODEC_INSTANCE=None  # Identity validation once per immutable worker, not output caching.


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def strict_json(value):
    def pairs(items):
        result={}
        for key,item in items:
            if key in result:raise ValueError('Duplicate JSON key')
            result[key]=item
        return result
    def reject(value):raise ValueError('Nonstandard JSON constant')
    return json.loads(value,object_pairs_hook=pairs,parse_constant=reject,
                      parse_int=lambda x:('integer-lexeme',x),
                      parse_float=lambda x:('float-lexeme',x))


class OriginalCodec:
    def __init__(self):
        if os.geteuid()!=65534:raise PermissionError('Upstream binary execution requires UID65534')
        binary=Path(CODEC)
        if binary.is_symlink() or binary.stat().st_uid!=0 or binary.stat().st_mode&0o222:
            raise ValueError('Immutable root-owned codec required')
        if hashlib.sha256(binary.read_bytes()).hexdigest()!=CODEC_SHA256:raise ValueError('Unreviewed codec binary')

    def invoke(self,operation,value):
        if os.geteuid()!=65534 or operation not in ('encode','decode'):raise PermissionError('Closed unprivileged codec operation')
        encoded=value.encode()
        if len(encoded)>64*1024**2:raise ValueError('Upstream input bound exceeded')
        result=subprocess.run([CODEC,'toon',operation],input=encoded,capture_output=True,timeout=4,
                              env={'PATH':'/usr/bin:/bin','HOME':'/work','GOMAXPROCS':'2'},check=False)
        if result.returncode:
            if operation=='encode' and result.returncode==1 and b'not losslessly TOON-encodable'in result.stderr:return None
            raise RuntimeError('Original codec execution failed: '+str(result.returncode))
        if len(result.stdout)>64*1024**2:raise ValueError('Codec response bound exceeded')
        return result.stdout.decode('utf-8')


def transform(body,variant,codec=None):
    global _CODEC_INSTANCE
    if variant not in ARMS or type(body)is not dict or type(body.get('messages'))is not list:
        raise ValueError('Closed request/variant required')
    result=copy.deepcopy(body);receipts=[];changed=[]
    if variant!='reference':
        for index,message in enumerate(result['messages']):
            if message.get('role')!='tool':continue
            original=message.get('content');row={'message_index':index,'status':'UNCHANGED'}
            if not isinstance(original,str):
                row['status']='NON_TEXT_UNCHANGED';receipts.append(row);continue
            try:
                original.encode('utf-8')
                before=strict_json(original)
            except ValueError:
                row['status']='AMBIGUOUS_OR_NON_JSON_UNCHANGED';receipts.append(row);continue
            if codec is None:
                if _CODEC_INSTANCE is None:_CODEC_INSTANCE=OriginalCodec()
                codec=_CODEC_INSTANCE
            cpu=time.process_time_ns();wall=time.perf_counter_ns();children=resource.getrusage(resource.RUSAGE_CHILDREN)
            # Never swallow a TASK/case deadline. A subprocess timeout propagates.
            candidate=codec.invoke('encode',original)
            decoded=codec.invoke('decode',candidate) if candidate is not None else None
            used=resource.getrusage(resource.RUSAGE_CHILDREN)
            row.update(codec_wall_ns=time.perf_counter_ns()-wall,codec_parent_cpu_ns=time.process_time_ns()-cpu,
                       codec_children_cpu_ns=round(1e9*((used.ru_utime+used.ru_stime)-(children.ru_utime+children.ru_stime))),
                       original_content=original,original_content_sha256=hashlib.sha256(original.encode()).hexdigest())
            try:matches=decoded is not None and strict_json(decoded)==before
            except ValueError:matches=False
            if candidate is None:row['status']='UNSUPPORTED_UNCHANGED'
            elif not matches:row['status']='ROUNDTRIP_MISMATCH_UNCHANGED'
            elif candidate==original:row['status']='BYTE_IDENTICAL_UNCHANGED'
            else:
                message['content']=candidate;changed.append(index);row.update(status='ROUNDTRIP_PRESERVED',encoded_content=candidate,
                    encoded_content_sha256=hashlib.sha256(candidate.encode()).hexdigest(),decoded_content_sha256=hashlib.sha256(decoded.encode()).hexdigest())
            receipts.append(row)
    protected=copy.deepcopy(result)
    for index in changed:protected['messages'][index]['content']=body['messages'][index]['content']
    if protected!=body:raise ValueError('Protected request fields changed')
    return result,{'variant':variant,'codec_sha256':CODEC_SHA256,'changed_message_indices':changed,
                   'request_before_sha256':digest(body),'request_after_sha256':digest(result),
                   'protected_fields_sha256':digest(protected),'tool_results':receipts,
                   'local_model_requests':0,'GPU_runs':0,'native_token_savings':'NOT MEASURED',
                   'quality_nonregression':'NOT TESTED'}


def wrap_adapter(adapter,variant,sink):
    if variant not in ARMS or not callable(sink):raise ValueError('Reviewed variant/sink required')
    original=adapter._make_body
    def make_body(task,history):
        before=original(task,history);cpu=time.process_time_ns();wall=time.perf_counter_ns()
        body,receipt=transform(before,variant)
        receipt.update(transform_wall_ns=time.perf_counter_ns()-wall,transform_cpu_ns=time.process_time_ns()-cpu,transform_cpu_scope='PARENT_PYTHON_ONLY_CODEC_CHILD_CPU_RECORDED_SEPARATELY')
        sink(receipt);return body
    adapter._make_body=make_body
    return adapter


def receipt_identity(receipt):
    value=copy.deepcopy(receipt)
    for key in ('transform_wall_ns','transform_cpu_ns'):
        duration=value.pop(key,None)
        if type(duration)is not int or duration<0:raise ValueError('Measured transform duration missing')
    for item in value['tool_results']:
        for key in ('codec_wall_ns','codec_parent_cpu_ns','codec_children_cpu_ns'):
            if key in item:
                if type(item.pop(key))is not int:raise ValueError('Invalid codec duration')
    return value
