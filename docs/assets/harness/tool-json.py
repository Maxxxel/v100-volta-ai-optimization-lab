"""Lossless lexical JSON whitespace reduction; no tool execution or GPU admission.

Only insignificant ASCII JSON whitespace outside strings is removed. String
escapes, numeric lexemes, object order and duplicate keys stay byte-exact.
Original tool outputs remain in the unmodified capture. Invalid JSON fails closed.
"""
import copy,json,hashlib,time

def compact_json(value):
    if type(value) is not str:raise ValueError('Tool payload must be text')
    def reject(_):raise ValueError('Nonstandard JSON numeric constant')
    json.loads(value,parse_constant=reject)
    out=[];quoted=False;escaped=False
    for c in value:
        if quoted:
            out.append(c)
            if escaped:escaped=False
            elif c=='\\':escaped=True
            elif c=='"':quoted=False
        elif c=='"':quoted=True;out.append(c)
        elif c not in ' \t\r\n':out.append(c)
    result=''.join(out)
    json.loads(result,parse_constant=reject)
    return result

def transform(body,variant):
    if variant not in ('reference','compact-tool-json-v1'):raise ValueError('Unknown variant')
    if type(body) is not dict or type(body.get('messages')) is not list:raise ValueError('Missing messages')
    result=copy.deepcopy(body);changed=[]
    for i,m in enumerate(result['messages']):
        if m.get('role')!='tool':continue
        original=m.get('content');compact=compact_json(original)
        if variant!='reference':m['content']=compact
        if m['content']!=original:changed.append(i)
    # Protect all other request fields, tool IDs, arguments, prompts and schemas.
    protected=copy.deepcopy(result)
    for i in changed:protected['messages'][i]['content']=body['messages'][i]['content']
    if protected!=body:raise ValueError('Protected request field changed')
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return result,{'variant':variant,'changed_message_indices':changed,'request_before_sha256':digest(body),'request_after_sha256':digest(result),'GPU_admitted':False}

def wrap_adapter(adapter,variant,sink):
    """Intercept only the reviewed request builder inside the unprivileged worker.

    The caller retains the existing adapter, model transport, simulator,
    permissions, task deadline and scoring. No role/reviewer/model call added.
    """
    if variant not in ARMS or not callable(sink):raise ValueError('Reviewed variant and audit sink required')
    original=adapter._make_body
    def make_body(task,history):
        original_body=original(task,history)
        cpu_begin=time.process_time_ns();wall_begin=time.perf_counter_ns()
        body,receipt=transform(original_body,variant)
        receipt['transform_wall_ns']=time.perf_counter_ns()-wall_begin
        receipt['transform_cpu_ns']=time.process_time_ns()-cpu_begin
        sink(receipt)
        return body
    adapter._make_body=make_body
    return adapter


def receipt_identity(receipt):
    """Replay semantic evidence exactly; measured CPU/wall durations vary per run."""
    value=copy.deepcopy(receipt)
    for key in ('transform_wall_ns','transform_cpu_ns'):
        duration=value.pop(key,None)
        if type(duration) is not int or duration<0:raise ValueError('Missing or invalid measured transform duration')
    return value


ARMS=('reference','compact-tool-json-v1')
