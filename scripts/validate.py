#!/usr/bin/env python3
"""Fail-closed publication checks; contains no credentials or source-host defaults."""
import collections,hashlib,ipaddress,json,pathlib,re,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
ROOT_FILES={'README.md','LICENSE','CITATION.cff','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','.gitignore','mkdocs.yml','requirements-docs.txt'}
DATA={'benchmark-register.json','configuration-history.json','comparison.json','research-issues.json','snapshot.json','factors.json','experiments.json','audit-excerpts.json','signed-windows.json','history.json','references.json','profiles.json','models.json','model-benchmarks.json','sources.json','research-subcases.json','publication-manifest.json'}
SCRIPTS={'leaderboard.py','test_leaderboard.py','comparison.py','test_comparison.py','export.py','render.py','validate.py','test_publication.py'}
SCRIPTS.update({'test_master_table.cjs','test_master_browser.cjs'})
SCRIPTS.update({'derivatives.py','test_derivatives.py','test_native_tools.py','test_native_tool_prefix.py'})
SECRET=re.compile(r'(?i)(?:gh[pousr]_[A-Za-z0-9]{12,}|github_pat_[A-Za-z0-9_]{12,}|sk-[A-Za-z0-9]{16,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:password|passwd|api[_-]?key|access[_-]?token|authorization)\s*[:=]\s*[\x22\x27]?[A-Za-z0-9/+_=.-]{12,})')
PRIVATE=re.compile(r'(?i)(?:\bGPU-[a-f0-9-]{16,}|\b[a-z0-9-]+\.(?:lan|local|internal)\b|\b(?:sensor|switch|light|climate|automation|person|device_tracker|input_boolean)\.[a-z0-9_]+|\b(?:pve|proxmox)-[a-z0-9-]+\b|(?:/opt|/root|/home|/run|/var)/(?!\[)[A-Za-z0-9_.-]+/)')
def allowed(p):
 s=p.as_posix();parts=p.parts
 if len(parts)==1:return s in ROOT_FILES
 if parts[0]=='data':return len(parts)==2 and p.name in DATA
 if parts[0]=='scripts':return len(parts)==2 and p.name in SCRIPTS
 if parts[:2]==('.github','workflows'):return len(parts)==3 and p.name in {'pages.yml','security.yml'}
 if parts[:2]==('.github','ISSUE_TEMPLATE'):return len(parts)==3 and p.suffix in {'.md','.yml'}
 if parts[0]=='docs':return p.suffix in {'.md','.css','.js','.svg'} and all(re.fullmatch('[A-Za-z0-9_.-]+',x) for x in parts)
 return False
def validation_event_matches(event,audit):
 if audit.get('original_sha256')!=event.get('audit_sha256'):return False
 aggregate=audit.get('aggregate_metrics',{})
 if event.get('kind')=='BFCL_FULL400_CATEGORY_DEFINITION_ADMISSION':
  return all(type(event.get(k)) is int and event[k]==0 for k in ('GPU_runs','model_results_admitted')) and aggregate.get('new_GPU_runs')==0 and aggregate.get('model_results_admitted')==0
 if event.get('experiment_id') and all(k in event for k in ('tasks','solved','changed_judgements')):
  metrics=aggregate.get('models',{}).get(event['experiment_id'],{})
  return all(metrics.get(k)==event[k] for k in ('tasks','solved','changed_judgements'))
 return False

def content_errors(s):
 issues=[]
 if SECRET.search(s):issues.append('secret-like material')
 if PRIVATE.search(s):issues.append('private infrastructure identifier')
 for match in re.findall(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])',s):
  try:
   addr=ipaddress.ip_address(match)
   if not addr.is_global:issues.append('nonpublic network address')
  except ValueError:pass
 for candidate in re.findall(r'(?<![A-Za-z0-9])(?:[A-Fa-f0-9]{0,4}:){2,}[A-Fa-f0-9:]{0,39}',s):
  try:
   if not ipaddress.ip_address(candidate).is_global:issues.append('nonpublic IPv6 address')
  except ValueError:pass
 # URLs must never contain credentials or link to an internal endpoint.
 for u in re.findall(r'https?://[^\s<>"\x27)]+',s):
  if re.match(r'https?://[^/\s]+@',u):issues.append('credential-bearing URL')
 return sorted(set(issues))
def files():
 result=[]
 for p in ROOT.rglob('*'):
  rel=p.relative_to(ROOT)
  if any(x in {'.git','site','__pycache__','.venv'} for x in rel.parts):continue
  if p.is_symlink():raise ValueError('Symlink forbidden: '+str(rel))
  if p.is_file():
   if not allowed(rel):raise ValueError('File not on public allowlist: '+str(rel))
   result.append(p)
 return sorted(result)
def manifest():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files() if p.name!='publication-manifest.json'}
def validate(check_manifest=True):
 errors=[]
 if sum(p.stat().st_size for p in files())>64*1024**2:errors.append('Public metadata tree exceeds 64 MiB budget')
 for p in files():
  rel=str(p.relative_to(ROOT))
  limit=12*1024**2 if rel=='data/audit-excerpts.json' else 3*1024**2
  if p.stat().st_size>limit:errors.append(rel+': exceeds per-file export limit')
  try:s=p.read_text()
  except UnicodeError:errors.append(rel+': non-text file');continue
  errors.extend(rel+': '+x for x in content_errors(s))
  if p.suffix=='.md':
   for link in re.findall(r'\]\(([^\s)]+)',s):
    if '://' in link or link.startswith('#') or link.startswith('mailto:'):continue
    q=(p.parent/link.split('#')[0]).resolve()
    if not q.is_relative_to(ROOT) or not q.is_file():errors.append(rel+': broken local link '+link)
 def read(n):return json.loads((ROOT/'data'/n).read_text())
 s=read('snapshot.json');fs=read('factors.json');es=read('experiments.json');au=read('audit-excerpts.json');refs=read('references.json');profiles=read('profiles.json');counts=s['counts'];ids={x['id'] for x in fs};aids={x['id'] for x in au};rids={x['id'] for x in refs};eids={x['id'] for x in es}
 if len(fs)!=162 or len(ids)!=162:errors.append('162 unique factors required')
 if sum(x['kind']=='original' for x in fs)!=130 or sum(x['kind']=='additional' for x in fs)!=32:errors.append('Original/additional inventory changed')
 if dict(collections.Counter(x['status'] for x in fs))!=counts['scientific_status']:errors.append('Status counters disagree')
 if sum(x['experimentally_covered'] for x in fs)!=counts['experimentally_covered']:errors.append('Experimental count disagrees')
 if len(read('models.json'))!=11:errors.append('Challenger count changed')
 for f in fs:
  if not set(f['evidence_ids'])<=aids:errors.append(f['id']+': missing evidence')
  if not set(f['experiment_ids'])<=eids:errors.append(f['id']+': missing sprint')
  if not (ROOT/'docs'/'factors'/(f['id']+'.md')).is_file():errors.append(f['id']+': missing detail page')
 for x in es:
  if x.get('audit_id') and x['audit_id'] not in aids:errors.append(x['id']+': missing audit')
 for x in profiles:
  if x['A0'] not in rids or x['C'] and x['C'] not in rids:errors.append('Invalid reference pointer')
 for a in au:
  if not re.fullmatch('[a-f0-9]{64}',a['original_sha256']):errors.append('Invalid original audit hash')
 from comparison import check as check_comparison
 comparison=read('comparison.json');check_comparison(comparison)
 for row in comparison['records']+comparison['historical_native']:
  if not set(row['audit_ids'])<=aids:errors.append('Comparison links missing audit')
  pins={x['id']:x['original_sha256'] for x in au}
  if len(row['audit_ids'])!=len(row['audit_sha256']) or any(pins.get(k)!=v for k,v in zip(row['audit_ids'],row['audit_sha256'])):errors.append('Comparison audit reference/hash pairing mismatch')
  if not set(row['audit_sha256'])<={x['original_sha256'] for x in au}:errors.append('Comparison original audit hash missing')
 from leaderboard import validate_history
 history=read('configuration-history.json');register=read('benchmark-register.json')
 validate_history(history,{d['benchmark_id']:d for d in register['definitions']})
 for review in register.get('same_quantizer_weight_reviews',[]):
  if not set(review.get('evidence_audit_ids',[]))<=aids:errors.append('Same-quantizer review missing evidence')
  result=review['result'];rows=result['tensor_results']
  if len(rows)!=result['compared_tensors'] or len({r['name'] for r in rows})!=len(rows) or sum(r['parameters'] for r in rows)!=result['compared_parameters']:errors.append('Incomplete payload census')
  if result['represented_weight_verdict']=='IDENTICAL_MODEL_WEIGHTS_PROVEN_FOR_ALL_STORED_GGUF_TENSORS' and any(not r['byte_identical'] or r['payload_sha256_V1']!=r['payload_sha256_V2'] for r in rows):errors.append('False identical-payload claim')
  if result['new_GPU_runs']!=0 or any(k.endswith('_path') for k in review):errors.append('Unsafe same-quantizer review projection')
 for label in register.get('model_label_annotations',[]):
  sources=[r for r in register.get('same_quantizer_weight_reviews',[]) if r['review_id']==label['review_id'] and r['rename_sha256']==label['audit_sha256']]
  if len(sources)!=1 or sources[0]['result']['rename_and_dedup']['retained_main_sha256']!=label['artifact_sha256'] or sources[0]['result']['rename_and_dedup']['display_name']!=label['display_name']:errors.append('Unproven model identity label')
 for review in register.get('artifact_weight_reviews',[]):
  if not set(review.get('evidence_audit_ids',[]))<=aids:errors.append('Weight review missing original evidence')
  result=review['result'];rows=result['tensor_results']
  if len(rows)!=result['compared_tensors'] or len({r['name'] for r in rows})!=len(rows):errors.append('Weight review incomplete tensor coverage')
  if sum(r['parameters'] for r in rows)!=result['compared_parameters'] or sum(r['changed_values_exact'] for r in rows)!=result['changed_values_exact']:errors.append('Weight review aggregate mismatch')
  if result.get('new_GPU_runs')!=0 or result['underlying_checkpoint_verdict']!='NOT_UNAMBIGUOUSLY_DETERMINABLE':errors.append('Unsupported weight-review conclusion')
  if any(k.endswith('_path') for k in review):errors.append('Private weight-review source path exported')
 for r in history['runs']:
  if not set(r['audit_ids'])<=aids:errors.append('Configuration result missing original audit')
  if r['official_eligible'] and r.get('qualification_audit_id') not in aids:errors.append('Official result missing independent qualification audit')
 for event in register.get('local_validation_events',[]):
  audit=next((a for a in au if a['id']==event.get('audit_id')),{})
  if not validation_event_matches(event,audit):errors.append('Validation event disagrees with its pinned audit or event type')
 import xml.etree.ElementTree as ET
 for svg in (ROOT/'docs/assets/benchmarks').glob('*.svg'):
  tree=ET.fromstring(svg.read_text())
  for node in tree.iter():
   if node.tag.split('}')[-1] in {'script','foreignObject'} or any(k.lower().startswith('on') or k.split('}')[-1]=='href' for k in node.attrib):errors.append('Active/external SVG content')
 if check_manifest and read('publication-manifest.json')!=manifest():errors.append('Publication byte manifest mismatch')
 if (ROOT/'.git').exists():
  tracked=subprocess.run(['git','-C',str(ROOT),'ls-files','-z'],capture_output=True,text=True,check=True).stdout.split('\0')
  for p in tracked:
   if p and not allowed(pathlib.Path(p)):errors.append('Tracked file outside allowlist: '+p)
 if errors:raise ValueError('\n'.join(errors[:40]))
 print('PASS: public allowlist, confidentiality, links, 162 factors, references and manifest')
if __name__=='__main__':
 if '--write-manifest' in sys.argv:(ROOT/'data'/'publication-manifest.json').write_text(json.dumps(manifest(),indent=2,sort_keys=True)+'\n')
 validate()
