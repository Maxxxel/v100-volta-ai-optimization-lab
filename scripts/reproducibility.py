"""Verify aggregate reproducibility evidence without exporting private requests."""
import collections,hashlib,json,math
from pathlib import Path

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def lost_task_first_divergence(baseline_checks,candidate_checks,baseline_rows,candidate_rows):
 """Return a prompt-free summary of the one R536->R616 lost task, if provable."""
 left={x['id']:bool(x['task_success']) for x in baseline_checks}
 right={x['id']:bool(x['task_success']) for x in candidate_checks}
 assert left.keys()==right.keys() and len(left)>0
 lost=[key for key in left if left[key] and not right[key]]
 assert len(lost)==1
 case=lost[0]
 def indexed(rows,kind):return {x['id']:x for x in rows if x.get('kind')==kind}
 aturns, bturns=indexed(baseline_rows,'agent_turn'),indexed(candidate_rows,'agent_turn')
 ainputs, binputs=indexed(baseline_rows,'input_identity'),indexed(candidate_rows,'input_identity')
 ids=sorted((key for key in aturns.keys()&bturns.keys() if key.startswith(case+'--turn')),
            key=lambda key:int(key.rsplit('turn',1)[1]))
 assert len(ids)>=3
 turns=[]
 for key in ids:
  a,b=aturns[key],bturns[key]
  assert key in ainputs and key in binputs
  ai,bi=ainputs[key],binputs[key]
  assert ai['prompt_token_ids']==bi['prompt_token_ids']
  assert ai['prompt_token_ids_sha256']==bi['prompt_token_ids_sha256']
  ar,br=a['request'],b['request']
  assert {k:v for k,v in ar.items() if k!='cache_prompt'}=={k:v for k,v in br.items() if k!='cache_prompt'}
  assert ar.get('cache_prompt') is False and br.get('cache_prompt') is True
  at=a['reply']['__verbose']['tokens'];bt=b['reply']['__verbose']['tokens']
  first=next((i for i,(x,y) in enumerate(zip(at,bt)) if x!=y),None)
  identical=len(at)==len(bt) and first is None
  av=a['reply']['__verbose']['timings'];bv=b['reply']['__verbose']['timings']
  turns.append({'context_tokens':ai['prompt_token_count'],'identity_match':True,
                'same_tokens':identical,'baseline_generated_tokens':len(at),
                'candidate_generated_tokens':len(bt),'first_difference_index':first,
                'baseline_cached_tokens':av['cache_n'],'candidate_cached_tokens':bv['cache_n']})
 # Validate the observed pattern rather than turning any arbitrary comparison into a claim.
 assert turns[0]['same_tokens'] and turns[1]['same_tokens']
 assert not turns[2]['same_tokens'] and turns[2]['first_difference_index']==0
 assert turns[2]['context_tokens']==1790 and turns[2]['baseline_cached_tokens']==0
 assert turns[1]['candidate_cached_tokens']==1543 and turns[2]['candidate_cached_tokens']==1675
 assert turns[2]['baseline_generated_tokens']==558 and turns[2]['candidate_generated_tokens']==166
 base_case_turns=[x for x in aturns.values() if x['id'].startswith(case+'--turn')]
 candidate_case_turns=[x for x in bturns.values() if x['id'].startswith(case+'--turn')]
 base_total=sum(len(x['reply']['__verbose']['tokens']) for x in base_case_turns)
 candidate_total=sum(len(x['reply']['__verbose']['tokens']) for x in candidate_case_turns)
 assert len(base_case_turns)==3 and len(candidate_case_turns)==5
 assert (base_total,candidate_total)==(636,744)
 return {'source_experiments':['R536','R616'],'lost_task_count':1,
         'task_identifier_withheld':True,'turns':turns,
         'agent_trajectory':{'baseline_turns':len(base_case_turns),'candidate_turns':len(candidate_case_turns),'extra_candidate_turns':len(candidate_case_turns)-len(base_case_turns),'baseline_generated_tokens':base_total,'candidate_generated_tokens':candidate_total},
         'interpretation':'The sole R536-success/R616-failure case had two identical earlier replies. On turn 3, exact prompt token IDs and request fields (except cache_prompt) matched; the baseline processed all 1790 prompt tokens while the candidate reported reusing 1675 and diverged at output token 0. The candidate then used two additional turns: total captured output was 744 tokens versus 636 in the baseline. This directly maps cache-enabled execution to the observed first divergence in this case, but the historical sessions were not contemporaneous and no no-cache A/A repeat exists for this exact prompt. It does not prove the cache caused the task or policy outcome, identify a numerical/GDN state mechanism, or qualify the cache.'}

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

def cache_state_source_path(root):
 root=Path(root);src=root/'staging/r31/extra/source/tools/server/server-context.cpp'
 if not src.is_file():return None
 commit='097cf33d9499b1eade67d51e16d7c75427e7b267';expected='6b5fdf2b246017b074c239e8f0b93f9d6952b4715501269627fec7a11b00bab7'
 assert digest(src)==expected
 lines=src.read_text(errors='replace').splitlines()
 needles={
  'common_prefix':'n_past = slot.prompt.tokens.get_common_prefix(input_tokens);',
  'prefix_chunk_reuse':'reusing chunk with size',
  'checkpoint_target_state':'cur.update_tgt(ctx_tgt, slot.id, LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY);',
  'checkpoint_draft_state':'cur.update_dft(ctx_dft, slot.id, LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY);',
  'checkpoint_speculative_state':'common_speculative_get_state(spec.get(), slot.id, cur.data_spec);',
  'recurrent_state_rewind_limit':'a recurrent state cannot be rewound',
  'checkpoint_restore':'it->load_tgt(ctx_tgt, slot.id, LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY)',
  'checkpoint_restore_draft':'it->load_dft(ctx_dft, slot.id, LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY)',
  'full_only_checkpoint_path':'ctx_tgt_seq_rm_type == COMMON_CONTEXT_SEQ_RM_TYPE_FULL;',
  'pos_min_empty_guard':'if (pos_min == -1) {',
  'full_prompt_fallback':'forcing full prompt re-processing due to lack of cache data',
 }
 source_lines={key:next((i for i,line in enumerate(lines,1) if token in line),None) for key,token in needles.items()}
 assert all(source_lines.values()) and digest(src)==expected
 runs={}
 for rid in ('r614','r616'):
  audit_path=root/'staging'/rid/'AUDIT.json';audit=json.loads(audit_path.read_text());raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());log=raw/'server.log';rows=[json.loads(x) for x in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if x];turns=[x for x in rows if x.get('kind')=='agent_turn']
  assert digest(log)==pins['server.log'] and digest(raw/'HTTP_RESULTS.jsonl')==pins['HTTP_RESULTS.jsonl'] and digest(raw/'profile.json')==pins['profile.json']
  cache_flags=collections.Counter(str(x.get('request',{}).get('cache_prompt','MISSING')) for x in turns)
  assert cache_flags=={'True':len(turns)}
  text=log.read_text(errors='replace')
  runs[rid.upper()]={
   'audit_sha256':digest(audit_path),'server_log_sha256':pins['server.log'],'profile_sha256':pins['profile.json'],'requests_with_cache_prompt_true':len(turns),
   'log_counts':{
    'restored_context_checkpoint':text.count('restored context checkpoint'),
    'forced_full_prompt_reprocessing':text.count('forcing full prompt re-processing due to lack of cache data'),
    'partial_sequence_removal_unsupported':text.count('context does not support partial sequence removal'),
    'host_ram_prompt_cache_disabled':text.count('prompt cache is disabled'),
   },
  }
 # Map the only OmniCoder task lost after R616 to its first changed response.
 # The two independent sessions and all private task text stay local.
 divergence_inputs={}
 for rid in ('r536','r616'):
  stage=root/'staging'/rid
  audit=json.loads((stage/'AUDIT.json').read_text());raw=Path(audit['raw_root'])
  pins=json.loads((raw/'RAW_HASHES.json').read_text())
  for name in ('HTTP_RESULTS.jsonl','profile.json','LAUNCH.json','server.log'):
   assert digest(raw/name)==pins[name]
  divergence_inputs[rid]={
   'audit':audit,
   'checks':json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())['result']['checks'],
   'rows':[json.loads(x) for x in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if x],
   'profile':json.loads((raw/'profile.json').read_text()),
   'launch':json.loads((raw/'LAUNCH.json').read_text()),
  }
 base,candidate=divergence_inputs['r536'],divergence_inputs['r616']
 assert base['profile']['model_sha256']==candidate['profile']['model_sha256']=='a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052'
 assert base['profile']['chat_template']==candidate['profile']['chat_template']
 assert base['profile']['runtime']==candidate['profile']['runtime']
 assert base['launch']['argv']==candidate['launch']['argv']
 assert {k:v for k,v in base['launch']['environment'].items() if k!='O2_GPU_BUILD_LEASE'}=={k:v for k,v in candidate['launch']['environment'].items() if k!='O2_GPU_BUILD_LEASE'}
 assert {k:v for k,v in base['launch']['native_request_options'].items() if k!='cache_prompt'}=={k:v for k,v in candidate['launch']['native_request_options'].items() if k!='cache_prompt'}
 assert base['launch']['native_request_options']['cache_prompt'] is False
 assert candidate['launch']['native_request_options']['cache_prompt'] is True
 task_divergence=lost_task_first_divergence(base['checks'],candidate['checks'],base['rows'],candidate['rows'])
 return {
  'kind':'PINNED_SOURCE_AND_HASHED_LOG_RECONCILIATION','source_commit':commit,'source_file_sha256':expected,'source_lines':source_lines,'runs':runs,
  'external_issue':{
   'url':'https://github.com/ggml-org/llama.cpp/issues/22940',
   'status':'CLOSED_NOT_PLANNED',
   'claim':'FULL-only memory backends always fall back because the checkpoint restore path is not consulted when pos_min == -1.',
   'local_applicability':'NOT_ESTABLISHED; pinned source explicitly selects checkpoint state for FULL-only rollback and contains an explicit pos_min == -1 abort guard. R614/R616 logs contain checkpoint-restore events, so the issue’s blanket permanent-disablement claim does not describe every request in these runs.',
   'remaining_limit':'The restore/fallback events are not mapped to each divergent request; this does not identify why a specific checkpoint was unavailable or explain token/policy divergence.'
  },
  'source_interpretation':[
   'The request-level cache_prompt path finds a matching prompt prefix; the server can reuse cached chunks.',
   'Context checkpoints save target state (and the source also saves draft/speculative state); the source comment says recurrent state cannot be rewound from only the final state.',
   'When a usable checkpoint is unavailable for a hybrid/recurrent context, this code path forces full prompt re-processing.',
   'The log message that the host RAM prompt cache is disabled is a separate cache layer; it does not mean the per-request cache_prompt flag was off.',
  ],
  'causal_disposition':'OBSERVED_CACHE_ASSOCIATED_TOKEN_DIVERGENCE; INTERNAL_STATE_OR_NUMERICAL_CAUSE_UNRESOLVED',
  'case_level_divergence':task_divergence,
  'limits':'R616’s one lost task is now mapped to an exact matching 1,790-token prompt and its first changed token: two preceding turns were identical; the candidate reported reusing 1,675 tokens and diverged at output token zero. The historical sessions were not contemporaneous and this exact prompt lacks no-cache A/A repetition. No logits, per-layer state, or request-to-checkpoint restore/fallback mapping was captured. The source and token evidence do not identify a numerical/GDN state mechanism or prove task/policy causality.',
  'GPU_runs':0,'model_requests':0,
 }

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
 return {'source_review_sha256':digest(report),'timing_review_sha256':digest(fixed) if fixed.exists() else None,'source_commit':data['build_source']['commit'],'profiles':profiles,'paired_historical':pairs,'agent_task_pairs':agent_task_pairs(root),'fixed_output_timings':timings,'cache_state_source_path':cache_state_source_path(root),'scope':'Different sessions; observed divergence cannot establish causation or equivalence. Archived request and server-reported settings are not direct internal RNG-state observations. No new GPU run.'}
