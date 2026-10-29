"""Verify aggregate reproducibility evidence without exporting private requests."""
import collections,hashlib,json,math
from pathlib import Path

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def agent_task_pairs(root):
 root=Path(root);out={}
 for label,baseline,candidate in (('Nexus_prefix_cache','r531','r614'),('OmniCoder_prefix_cache','r536','r616')):
  paths={name:root/'staging'/name for name in (baseline,candidate)}
  required=('AUDIT.json','INDEPENDENT_REVIEW.json','QUALITY_REVIEW.json')
  if not all((paths[name]/file).is_file() for name in (baseline,candidate) for file in required) or not (paths[candidate]/'SINGLE_FACTOR_REVIEW.json').is_file():continue
  items={name:{file:json.loads((paths[name]/file).read_text()) for file in ('AUDIT.json','INDEPENDENT_REVIEW.json','QUALITY_REVIEW.json')} for name in (baseline,candidate)}
  a,b=items[baseline],items[candidate]
  assert a['AUDIT.json']['dataset_id']==b['AUDIT.json']['dataset_id']=='jarvis-agent-validation-20261025-v1'
  assert a['AUDIT.json']['tasks']==b['AUDIT.json']['tasks']==33
  assert a['AUDIT.json']['model_sha256']==b['AUDIT.json']['model_sha256']
  checks={name:review['result']['checks'] for name,review in ((baseline,a['INDEPENDENT_REVIEW.json']),(candidate,b['INDEPENDENT_REVIEW.json']))}
  assert a['INDEPENDENT_REVIEW.json']['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and a['INDEPENDENT_REVIEW.json']['result']['complete']
  assert b['INDEPENDENT_REVIEW.json']['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and b['INDEPENDENT_REVIEW.json']['result']['complete']
  left={row['id']:bool(row['task_success']) for row in checks[baseline]};right={row['id']:bool(row['task_success']) for row in checks[candidate]}
  assert len(left)==len(right)==33 and left.keys()==right.keys()
  a_only=sum(left[k] and not right[k] for k in left);b_only=sum(right[k] and not left[k] for k in left)
  both=sum(left[k] and right[k] for k in left);neither=sum(not left[k] and not right[k] for k in left)
  # Exact two-sided McNemar test. For zero or one discordance it is necessarily 1.0;
  # this does not establish equivalence or noninferiority.
  n=a_only+b_only
  tail=sum(math.comb(n,k) for k in range(min(a_only,b_only)+1))/(2**n) if n else 0.5
  p=min(1.0,2*tail)
  assert a['INDEPENDENT_REVIEW.json']['result']['solved']==sum(left.values())
  assert b['INDEPENDENT_REVIEW.json']['result']['solved']==sum(right.values())
  assert a['QUALITY_REVIEW.json']['tasks']==b['QUALITY_REVIEW.json']['tasks']==33
  sf=json.loads((paths[candidate]/'SINGLE_FACTOR_REVIEW.json').read_text());comparison=sf['comparison']
  assert sf['reference_audit_sha256']==digest(paths[baseline]/'AUDIT.json')
  assert sf['candidate_audit_sha256']==digest(paths[candidate]/'AUDIT.json')
  assert sf['factor']=='R22' and sf['winner_qualified'] is False and sf['status']=='NOT_QUALIFIED_SCREEN_GATE_NOT_MET'
  assert comparison['quality']['task_success']['reference_passed']==sum(left.values())
  assert comparison['quality']['task_success']['candidate_passed']==sum(right.values())
  assert comparison['quality']['task_success']['lost']==a_only and comparison['quality']['task_success']['gained']==b_only
  assert comparison['quality']['policy_gate_pass']['reference_passed']==a['QUALITY_REVIEW.json']['quality']['policy_gate_passes']
  assert comparison['quality']['policy_gate_pass']['candidate_passed']==b['QUALITY_REVIEW.json']['quality']['policy_gate_passes']
  out[label]={
   'baseline_experiment':baseline.upper(),'candidate_experiment':candidate.upper(),
   'baseline_audit_sha256':digest(paths[baseline]/'AUDIT.json'),'candidate_audit_sha256':digest(paths[candidate]/'AUDIT.json'),
   'baseline_independent_review_sha256':digest(paths[baseline]/'INDEPENDENT_REVIEW.json'),'candidate_independent_review_sha256':digest(paths[candidate]/'INDEPENDENT_REVIEW.json'),
   'dataset_id':'jarvis-agent-validation-20261025-v1','tasks':33,'task_outcomes':{'baseline_only_success':a_only,'candidate_only_success':b_only,'both_success':both,'both_failed':neither,'exact_mcnemar_two_sided_p':p},
   'policy_gate_passes':{'baseline':a['QUALITY_REVIEW.json']['quality']['policy_gate_passes'],'candidate':b['QUALITY_REVIEW.json']['quality']['policy_gate_passes']},
   'case_wall_seconds':{'baseline':comparison['reference_case_wall_s'],'candidate':comparison['candidate_case_wall_s'],'observed_reduction_percent':comparison['case_wall_reduction_percent']},
   'completion_tokens':{'baseline':comparison['reference_cache']['completion_tokens'],'candidate':comparison['candidate_cache']['completion_tokens']},
   'gpu_energy_j_bounds':{'baseline':[comparison['reference_gpu_j_lower'],comparison['reference_gpu_j_upper']],'candidate':[comparison['candidate_gpu_j_lower'],comparison['candidate_gpu_j_upper']]},
   'peak_vram_mib':{'baseline':comparison['reference_peak_vram_mib'],'candidate':comparison['candidate_peak_vram_mib']},
   'cache_observation':{'candidate_cache_hit_turns':comparison['candidate_cache']['cache_hit_turns'],'candidate_cached_tokens':comparison['candidate_cache']['cached_tokens']},
   'task_level_repeatability':'NOT_MEASURED',
   'causal_disposition':'OBSERVED_REGRESSION_CAUSE_UNCONFIRMED',
   'performance_disposition':'OBSERVED_SPEED_DIFFERENCE_CAUSAL_GAIN_UNCONFIRMED',
   'qualification':'NOT_QUALIFIED',
   'winner_qualified':False,
   'interpretation':'One complete response per arm on 33 exposed fixed tasks. Exact paired test is descriptive and underpowered with 0/1 discordant task; no equivalence or noninferiority claim. Task-level A/A repeatability is not estimated. Cache-on request-level divergence is separately documented; whole-task causality remains unresolved.'
  }
 return out

def build(root):
 root=Path(root);report=root/'staging/reproducibility-20261029/REPRODUCIBILITY_REVIEW.json'
 if not report.is_file():return None
 data=json.loads(report.read_text());captures={}
 for ident,v in data['profiles'].items():
  audit=root/'staging'/ident/'AUDIT.json';assert digest(audit)==v['audit_sha256'];a=json.loads(audit.read_text());raw=Path(a['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());assert digest(raw/'profile.json')==pins['profile.json']==v['profile_sha256'] and digest(raw/'HTTP_RESULTS.jsonl')==pins['HTTP_RESULTS.jsonl']==v['raw_responses_sha256'];p=json.loads((raw/'profile.json').read_text());assert p['model_sha256']==v['model_sha256'];rows=[json.loads(s) for s in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if s];turns={r['id']:r for r in rows if r.get('kind')=='agent_turn'};inputs={r['id']:r for r in rows if r.get('kind')=='input_identity'};assert turns.keys()==inputs.keys() and len(turns)==v['request_count'];req=collections.Counter(str(x['request'].get('seed','MISSING')) for x in turns.values());srv=collections.Counter(str(x['reply'].get('__verbose',{}).get('generation_settings',{}).get('seed','MISSING')) for x in turns.values());assert dict(req)==v['request_seeds'] and dict(srv)==v['server_reported_seeds'];captures[ident]=(turns,inputs)
 pairs={}
 for label,review in data['paired_historical'].items():
  a,b=label.split('_');lt,li=captures[a];rt,ri=captures[b];same=changed=equal=different=0
  for key in lt.keys()&rt.keys():
   x,y=lt[key],rt[key]
   if {k:v for k,v in x['request'].items() if k!='cache_prompt'}!={k:v for k,v in y['request'].items() if k!='cache_prompt'}:continue
   same+=1
   if li[key]['prompt_token_ids']!=ri[key]['prompt_token_ids']:changed+=1;continue
   if x['reply']['__verbose']['tokens']==y['reply']['__verbose']['tokens']:equal+=1
   else:different+=1
  assert (same,changed,equal,different)==tuple(review[k] for k in ('same_request_except_cache_flag','different_prompt_token_sequences','same_prompt_and_same_output_tokens','same_prompt_and_different_output_tokens'))
  pairs[label]={'matching_requests':same,'different_input_tokens':changed,'equal_outputs':equal,'different_outputs':different}
 fixed=root/'staging/reproducibility-20261029/FIXED_OUTPUT_TIMING_REVIEW.json';timings={}
 if fixed.exists():
  fd=json.loads(fixed.read_text());assert fd['GPU_runs']==0
  for label,review in fd['pairs'].items():
   a,b=label.split('_');lt,li=captures[a];rt,ri=captures[b];selected=[]
   for key in sorted(lt.keys()&rt.keys()):
    x,y=lt[key],rt[key]
    if {k:v for k,v in x['request'].items() if k!='cache_prompt'}!={k:v for k,v in y['request'].items() if k!='cache_prompt'} or li[key]['prompt_token_ids']!=ri[key]['prompt_token_ids'] or x['reply']['__verbose']['tokens']!=y['reply']['__verbose']['tokens']:continue
    xx=x['reply']['__verbose']['timings'];yy=y['reply']['__verbose']['timings']
    if any(type(z.get(k)) not in (int,float) or not math.isfinite(z[k]) or z[k]<0 for z in (xx,yy) for k in ('prompt_n','prompt_ms','predicted_n','predicted_ms')):continue
    if xx['predicted_n']!=yy['predicted_n'] or xx['predicted_n']<=0:continue
    selected.append((x,y,xx,yy))
   def stats(i):
    z=[x[i] for x in selected];t=[x[i+2] for x in selected]
    return {'request_wall_s':sum(r['e2e_s'] for r in z),'prefill_ms':sum(r['prompt_ms'] for r in t),'prefill_processed_tokens':sum(r['prompt_n'] for r in t),'decode_ms':sum(r['predicted_ms'] for r in t),'decode_tokens':sum(r['predicted_n'] for r in t),'reported_cached_tokens':sum(r['reply']['usage']['prompt_tokens_details']['cached_tokens'] for r in z)}
   assert review['matched_requests']==len(selected) and review['reference_audit_sha256']==data['profiles'][a]['audit_sha256'] and review['candidate_audit_sha256']==data['profiles'][b]['audit_sha256'] and review['reference']==stats(0) and review['candidate']==stats(1)
   timings[label]={k:review[k] for k in ('matched_requests','reference','candidate')}
 profiles={k:{x:v[x] for x in ('audit_sha256','model_sha256','profile_sha256','configured_seed','configured_temperature','request_count','server_reported_seeds','input_token_ids_recorded','output_token_ids_recorded')} for k,v in data['profiles'].items()}
 return {'source_review_sha256':digest(report),'timing_review_sha256':digest(fixed) if fixed.exists() else None,'source_commit':data['build_source']['commit'],'profiles':profiles,'paired_historical':pairs,'agent_task_pairs':agent_task_pairs(root),'fixed_output_timings':timings,'scope':'Different sessions; observed divergence cannot establish causation or equivalence. Archived request and server-reported settings are not direct internal RNG-state observations. No new GPU run.'}
