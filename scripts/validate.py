#!/usr/bin/env python3
"""Fail-closed publication checks; contains no credentials or source-host defaults."""
import collections,hashlib,ipaddress,json,pathlib,re,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
ROOT_FILES={'README.md','LICENSE','CITATION.cff','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','.gitignore','mkdocs.yml','requirements-docs.txt'}
DATA={'snapshot.json','factors.json','experiments.json','audit-excerpts.json','signed-windows.json','history.json','references.json','profiles.json','models.json','model-benchmarks.json','sources.json','research-subcases.json','publication-manifest.json'}
SCRIPTS={'export.py','render.py','validate.py','test_publication.py'}
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
def content_errors(s):
 issues=[]
 if SECRET.search(s):issues.append('secret-like material')
 if PRIVATE.search(s):issues.append('private infrastructure identifier')
 for match in re.findall(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])',s):
  try:
   addr=ipaddress.ip_address(match)
   if not addr.is_global:issues.append('nonpublic network address')
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
