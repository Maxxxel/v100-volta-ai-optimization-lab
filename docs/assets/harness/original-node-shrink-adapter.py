"""Closed adapter to original Node Caveman shrink; no GPU admission.

Only the ten actually reviewed catalogs are eligible. Unknown catalogs and the
reference arm remain unchanged. Original model messages/tool values never change.
"""
import copy,hashlib,json,os,resource,subprocess,time
from pathlib import Path
ARMS=('reference','upstream-node-shrink-v1')
NODE='/harness/caveman-node'
MODULE='/harness/caveman-shrink.cjs'
WRAPPER='/harness/caveman-shrink-request.cjs'
NODE_SHA='67ca5783febb8bf85736c79fcdd92c8d6d465a0eb2a082672bcdfa76a506751c'
MODULE_SHA='87b89523c9466f7634b2f70dbaaa483648756e927127a4d11ba95f64003fde7f'
WRAPPER_SHA='cb547fe1f29b5e3d7d6ef1e9b658c07d03519ae2c27c3050a74e9d6c489038b8'
REVIEWED_CATALOGS={'e59731e03131624b639ae6a15fad06e014ac190910d8223fd07e7cf080c9282d': 'ec5ddd930b310f3f477e0b251f5aff5a01834fb905573181968cfc9d07bfbb2f', 'c46985bdea388cf1f7dbc1ad139b33d20da007ca7f19c8371470842adc691cdc': 'd8e111ddf7e57ba61ef6d6a251be4007b123b5953d22300b4c345f30a04e8dee', '81b4911ae55b715485abd898ec762d8c19316bf56726515ae5a52db5f2c3d9d4': '303bfde8511b4a895ddf19150fe552bea1194aceb959333a187b7eed31d87ccc', '67fddd9b84848196fec27f028f5666ad25f80b436fbedcd2238e14674f0c97ec': 'b9fc69d144d09903f3f14235840ae61981d0b05bb8096a529c2589b0a0a8a403', '444f206cbf0296c02271a25d91e1448f1e181ec6f8e2dc0920fab51ef441a0be': 'dc245b1cbeb9d35d4a99f132ee0e64d7ad1d6c65ee0be74dda2c54dc1d07d0b0', '5d6e09090e19fe97efb60172a2934baa345228a9f1775a7f017e020bbc4ceb6b': '2600fe4817bd100fb3621675a2dc8e91abbd2f3a8578de12e060eeafc797a84f', '8a1637028652c89a7bce14d9978df9b79d31e3549f3e4a84eceb7fea4889d9aa': '6d7edc01b718411d99877fe0cebbab0d9d42576c1740498aaff76be336843a67', '2d1e537fb39ba2170551e87df1fa642c203dbc840a1ed489f9eb1aedd543afd4': '5d7cfdd139eea99929b0d2c351b594e156be7891005c55a260a1564371ed3906', '6a35805a9835630b69fc04ec75c0c683b27cae4e89f751ade8b14100cd7a4d26': '766a9ca656145a7e0b87eb7d4854f16b36bfc81560d357bf005b2bcda656ee84', '59fe276142717037a396f6b346af0670e405904b561d55c0d788e6dd24163ccf': 'c79b0069739f9357d5ca5b74779e6277bcd65cd4c76012ebd01eb4ed4a5e7fce'}
_CODEC=None

def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

class OriginalCodec:
 def __init__(self):
  if os.geteuid()!=65534:raise PermissionError('Original source only after UID drop')
  for file,expected in [(NODE,NODE_SHA),(MODULE,MODULE_SHA),(WRAPPER,WRAPPER_SHA)]:
   p=Path(file)
   if p.is_symlink()or p.stat().st_uid!=0 or p.stat().st_mode&0o222 or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise ValueError('Immutable reviewed Node/module identity required')
 def invoke(self,catalog):
  if os.geteuid()!=65534:raise PermissionError('Unprivileged original codec only')
  data=json.dumps(catalog,separators=(',',':'),allow_nan=False).encode()
  if len(data)>1024**2:raise ValueError('Catalog size limit')
  result=subprocess.run([NODE,'--max-old-space-size=128',WRAPPER],input=data,capture_output=True,check=True,timeout=4,env={'PATH':'/usr/bin:/bin','HOME':'/work'})
  if len(result.stdout)>1024**2:raise ValueError('Codec output size limit')
  return json.loads(result.stdout)

def transform(body,variant,codec=None):
 global _CODEC
 if variant not in ARMS or type(body)is not dict or type(body.get('messages'))is not list:raise ValueError('Closed request and arm required')
 result=copy.deepcopy(body);receipt={'variant':variant,'module_sha256':MODULE_SHA,'request_before_sha256':digest(body),'status':'REFERENCE_UNCHANGED','local_model_requests':0,'GPU_runs':0}
 if variant!='reference':
  catalog={'tools':copy.deepcopy(body.get('tools'))};identity=digest(catalog)
  if identity not in REVIEWED_CATALOGS:receipt['status']='UNKNOWN_CATALOG_UNCHANGED'
  else:
   if codec is None:
    if _CODEC is None:_CODEC=OriginalCodec()
    codec=_CODEC
   wall=time.perf_counter_ns();cpu=time.process_time_ns();children=resource.getrusage(resource.RUSAGE_CHILDREN)
   output=codec.invoke(catalog);used=resource.getrusage(resource.RUSAGE_CHILDREN)
   if digest(output)!=REVIEWED_CATALOGS[identity]:raise ValueError('Original output differs from reviewed catalog')
   result['tools']=output['tools'];receipt.update(status='REVIEWED_ORIGINAL_NODE_TRANSFORM',catalog_before_sha256=identity,catalog_after_sha256=digest(output),codec_wall_ns=time.perf_counter_ns()-wall,codec_parent_cpu_ns=time.process_time_ns()-cpu,codec_children_cpu_ns=round(1e9*((used.ru_utime+used.ru_stime)-(children.ru_utime+children.ru_stime))))
 protected=copy.deepcopy(result)
 if 'tools'in body:protected['tools']=copy.deepcopy(body['tools'])
 if protected!=body:raise ValueError('Non-schema request fields changed')
 receipt.update(request_after_sha256=digest(result),protected_request_sha256=digest(protected))
 return result,receipt

def wrap_adapter(adapter,variant,sink):
 if variant not in ARMS or not callable(sink):raise ValueError('Closed adapter scope')
 original=adapter._make_body
 def make_body(task,history):
  before=original(task,history);cpu=time.process_time_ns();wall=time.perf_counter_ns();body,receipt=transform(before,variant)
  receipt.update(transform_wall_ns=time.perf_counter_ns()-wall,transform_cpu_ns=time.process_time_ns()-cpu);sink(receipt);return body
 adapter._make_body=make_body
 return adapter

def receipt_identity(receipt):
 value=copy.deepcopy(receipt)
 for key in ('codec_wall_ns','codec_parent_cpu_ns','codec_children_cpu_ns','transform_wall_ns','transform_cpu_ns'):
  if key in value:
   if type(value.pop(key))is not int:raise ValueError('Invalid timing field')
 return value
