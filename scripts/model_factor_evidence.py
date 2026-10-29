"""Conservative model/factor audit index; associations are not GPU or qualification claims."""
import re
MODELS=('OmniCoder','Nexus','Gemma 4','Qwen3.5','Qwen3.8')
PATTERNS=(('OmniCoder','omnicoder'),('Nexus','nexus'),('Gemma 4','gemma4'),('Qwen3.5','qwen35'),('Qwen3.8','qwen38'))
def build(factors,experiments):
 ids={f['id'] for f in factors};out={f:{m:[] for m in MODELS} for f in ids}
 for e in experiments:
  if not e.get('audit_id') or not re.fullmatch(r'R[1-9][0-9]*',e.get('id','')):continue
  name=re.sub(r'[^a-z0-9]','',(e.get('model') or '').lower())
  matches=[model for model,token in PATTERNS if token in name]
  if len(matches)!=1:continue
  for factor in set(e.get('factor_ids') or ()) & ids:
   if e['id'] not in out[factor][matches[0]]:out[factor][matches[0]].append(e['id'])
 for models in out.values():
  for links in models.values():links.sort(key=lambda x:int(x[1:]),reverse=True)
 return out
