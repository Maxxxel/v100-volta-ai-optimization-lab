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

def reviewed_dispositions(experiments):
 """Specific reviewed profiles, not blanket decisions for an optimization family."""
 rows=[
  ('R22','OmniCoder','PARTIAL','R616','R620','Historical quality and policy gate failed; cache-associated token divergence reproduced, but whole-task causality remains unresolved.'),
  ('R22','Nexus','PARTIAL','R614','R621','Historical policy gate failed; cache-associated token divergence reproduced, but whole-task causality remains unresolved.'),
  ('R22','Gemma 4','PARTIAL','R617','R624','Historical policy gate failed; cache-associated token divergence reproduced at original seed and temperature; whole-task causality remains unresolved.'),
  ('HBM07','OmniCoder','TESTED_NEGATIVE','R611',None,'One exposed Agent33 conversion-cache screen found no practical gain; other workloads and implementations remain open.'),
  ('R04','Gemma 4','TESTED_NEGATIVE','R612',None,'Microbatch 256 lost to historical 512 in one screen; output lengths and stochastic results differ, so causation remains unconfirmed.'),
  ('S01','Nexus','TESTED_NEGATIVE','R604',None,'A 32-task exposed n-gram screen showed no practical gain versus a historical interleaved control; energy was not fully measured and causation remains uncertain.'),
  ('K02','Gemma 4','PARTIAL','R606','R608','Q8 value cache looked promising in a paired development screen; the later full coding score fell against a historical control. No promotion; causal quality loss is unconfirmed.'),
  ('S03','Qwen3.8','PARTIAL','R551','R548','Integrated MTP improved a fresh development comparison and passed a scoped coding gate; task-level safety and broad equivalence remain unqualified.'),
  ('HBM07','OmniCoder','TESTED_NEGATIVE','R603',None,'A 4 GiB conversion-cache development screen showed no practical latency benefit; this is limited to the measured workload and profile.')]
 byid={e['id']:e for e in experiments if e.get('audit_id')}
 for factor,model,status,primary,followup,reason in rows:
  for ident in (primary,followup):
   if ident is None:continue
   e=byid.get(ident); normalized=re.sub(r'[^a-z0-9]','',(e.get('model') or '').lower()) if e else ''
   token=dict(PATTERNS)[model]
   if not e or factor not in (e.get('factor_ids') or ()) or token not in normalized:raise ValueError('Missing model-specific disposition evidence: '+ident)
 on=byid.get('R618');off=byid.get('R625')
 if on and off:
  paired=(off.get('aggregate_metrics') or {}).get('mtp_paired_comparison') or {}
  if ('qwen38' not in re.sub(r'[^a-z0-9]','',(on.get('model') or '').lower()) or
      'qwen38' not in re.sub(r'[^a-z0-9]','',(off.get('model') or '').lower()) or
      on['audit_id']!='audit-'+paired.get('candidate_on_audit_sha256','')[:20] or
      off['audit_id']!='audit-'+paired.get('reference_off_audit_sha256','')[:20] or
      paired.get('tasks')!=33 or paired.get('winner_qualified') is not False):
   raise ValueError('Invalid Qwen3.8 MTP paired evidence')
  rows.append(('S03','Qwen3.8','PARTIAL','R618','R625','MTP ON/OFF compared on 33 exposed agent tasks: 27/33 successes and 31/33 policy gates in each; 8/150 matched outputs differed. Separate sessions, no independent quality or safety equivalence; no Champion promotion.'))
 return rows
