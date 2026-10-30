"""Verify aggregate reproducibility evidence without exporting private requests."""
import collections,hashlib,json,math,re
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

def omni_cache_aa_repeatability(root, expected_prompt_ids):
 """Verify the exact R616 divergent prompt's two-session R620 A/A/A/B pilot."""
 root=Path(root);stage=root/'staging/r620';review=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())
 audit=json.loads((stage/'AUDIT.json').read_text());assert review['source_audit_sha256']==digest(stage/'AUDIT.json')
 assert review['status']=='INDEPENDENT_CPU_TOKEN_RECOMPUTATION_COMPLETE'
 raw_parent=root.parent/'research/mcp-workspace/r620-omni-aa-abba-token-pilot'
 raw_dirs=[p for p in raw_parent.glob('host-*') if (p/'HTTP_RESULTS.jsonl').is_file()]
 assert len(raw_dirs)==1
 raw=raw_dirs[0];pins=json.loads((raw/'RAW_HASHES.json').read_text())
 assert digest(raw/'HTTP_RESULTS.jsonl')==pins['HTTP_RESULTS.jsonl']==review['raw_responses_sha256']
 rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line]
 inputs={x['id']:x for x in rows if x.get('kind')=='r620_input'}
 requests={x['id']:x for x in rows if x.get('kind')=='r620_request'}
 assert len(requests)==24 and len(inputs)==24 and requests.keys()==inputs.keys()
 selected=[requests[f's{s}-a{a}-t3'] for s,a in ((1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4))]
 for record in selected:
  identity=inputs[record['id']]
  assert identity['prompt_token_ids']==expected_prompt_ids
  assert identity['prompt_token_ids_sha256']==hashlib.sha256(json.dumps(expected_prompt_ids,separators=(',',':')).encode()).hexdigest()
  assert record['request']['seed']==1001 and record['request']['temperature']==0
  assert {k:v for k,v in record['request'].items() if k!='cache_prompt'}=={k:v for k,v in selected[0]['request'].items() if k!='cache_prompt'}
 def seq(row):return row['reply']['__verbose']['tokens']
 baseline=[r for r in selected if r['request']['cache_prompt'] is False]
 candidate=[r for r in selected if r['request']['cache_prompt'] is True]
 assert len(baseline)==len(candidate)==4
 base_sequences=[seq(r) for r in baseline];candidate_sequences=[seq(r) for r in candidate]
 assert all(x==base_sequences[0] for x in base_sequences) and len(base_sequences[0])==558
 assert all(next((i for i,(x,y) in enumerate(zip(base_sequences[0],seq(r))) if x!=y),None)==0 for r in candidate)
 assert [len(x) for x in candidate_sequences]==[164,166,166,164]
 unique_candidate=len({tuple(x) for x in candidate_sequences})
 assert unique_candidate==2
 assert all(r['reply']['__verbose']['timings']['cache_n']==1675 for r in candidate)
 assert review['turns'][2]['no_cache_all_four_equal'] is True
 assert review['turns'][2]['cache_all_four_equal'] is False
 return {'experiment_id':'R620','same_exposed_prompt_token_ids_verified':True,
         'request_seed':1001,'temperature':0,'sessions':2,'repetitions_per_cache_setting':4,
         'no_cache_repeats_identical':4,'no_cache_output_tokens':[558,558,558,558],
         'cache_on_distinct_sequences':unique_candidate,'cache_on_repeats':4,
         'cache_on_output_tokens':[len(x) for x in candidate_sequences],
         'cache_on_repeats_identical_to_baseline':0,'cache_hit_tokens_each':1675,
         'first_output_difference_position_zero_based':0,
         'classification':'BASELINE_VARIABILITY_NOT_OBSERVED; CANDIDATE_VARIABILITY_OBSERVED_ON_ONE_EXPOSED_PROMPT',
         'limits':'Two sessions, one previously exposed request, fixed seed and temperature. No task replay, logits, RNG internals or recurrent-state values; this does not establish whole-task or policy causality.'}

def summarize_nexus_policy_case(baseline_case,candidate_case,baseline_request, candidate_request,
                                baseline_reply,candidate_reply,pilot_replies,input_tokens,
                                pilot_seed_checks):
 """Verify a cache-linked token path co-located with one policy loss, without task data."""
 assert baseline_case['task_success'] is False and candidate_case['task_success'] is False
 assert baseline_case['policy_gate_pass'] is True and candidate_case['policy_gate_pass'] is False
 assert baseline_case['policy_violations']==0 and candidate_case['policy_violations']==1
 assert baseline_case['rejected_calls']==0 and candidate_case['rejected_calls']==1
 assert baseline_case.get('all_tools_simulated') is True and candidate_case.get('all_tools_simulated') is True
 assert baseline_case.get('production_tools_connected') is False and candidate_case.get('production_tools_connected') is False
 assert sum(bool(x.get('policy_rejected')) for x in candidate_case.get('trace',[]) if x.get('kind')=='tool_response')==1
 assert sum(bool(x.get('policy_rejected')) for x in baseline_case.get('trace',[]) if x.get('kind')=='tool_response')==0
 assert {k:v for k,v in baseline_request.items() if k!='cache_prompt'}=={k:v for k,v in candidate_request.items() if k!='cache_prompt'}
 assert baseline_request['cache_prompt'] is False and candidate_request['cache_prompt'] is True
 assert baseline_request.get('seed')==candidate_request.get('seed')==1001
 assert baseline_request.get('temperature')==candidate_request.get('temperature')==0
 assert baseline_request.get('max_tokens')==candidate_request.get('max_tokens')==4096
 a=baseline_reply['__verbose']['tokens'];b=candidate_reply['__verbose']['tokens']
 first=next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y),None)
 assert a!=b and first==0 and (len(a),len(b))==(368,65)
 assert len(input_tokens)==1785
 assert len(pilot_replies)==8 and len(pilot_seed_checks)==8
 no_cache=[x for x in pilot_replies if x['request'].get('cache_prompt') is False]
 cached=[x for x in pilot_replies if x['request'].get('cache_prompt') is True]
 assert len(no_cache)==len(cached)==4
 assert all(x['reply']['__verbose']['tokens']==a for x in no_cache)
 assert all(x['reply']['__verbose']['tokens']==b for x in cached)
 assert all(x['reply']['__verbose']['timings']['cache_n']==0 for x in no_cache)
 assert all(x['reply']['__verbose']['timings']['cache_n']==1711 for x in cached)
 assert all(x['reply']['__verbose']['generation_settings']['seed']==1001 for x in pilot_seed_checks)
 assert all(x['reply']['__verbose']['generation_settings']['temperature']==0 for x in pilot_seed_checks)
 return {'baseline_run':531,'candidate_run':614,'repeatability_run':621,
         'policy_changed_cases':1,'task_success_changed_cases':0,
         'baseline_policy_pass':True,'candidate_policy_pass':False,
         'baseline_policy_violations':0,'candidate_policy_violations':1,
         'baseline_rejected_calls':0,'candidate_rejected_calls':1,
         'production_tool_actions':0,
         'matched_turn':4,'context_tokens':len(input_tokens),
         'identity_match':True,'request_match_except_cache_flag':True,
         'seed':1001,'temperature':0,'max_tokens':4096,
         'pilot_sessions':2,'no_cache_repeats':4,'no_cache_matches_baseline':4,
         'cache_hit_repeats':4,'cache_repeats_match_candidate':4,
         'cache_tokens_reused':1711,'baseline_generated_tokens':len(a),
         'candidate_generated_tokens':len(b),'first_difference_index':first,
         'classification':'REPRODUCIBLE_CACHE_ASSOCIATED_DIVERGENCE; ONE_POLICY_LOSS_OBSERVED; WHOLE_TASK_CAUSALITY_NOT_ESTABLISHED',
         'interpretation':'The only case whose policy gate changed between R531 and R614 failed task success in both arms. Its fourth-turn request has identical 1,785 input token IDs and request fields other than cache_prompt. R621 repeated that exact request in two ABBA sessions: all four no-cache outputs matched R531, and all four cache-hit outputs matched R614, with divergence at output token 0. The R614 task trace records one additional policy violation/rejected call in that same case. This establishes a reproducible cache-associated output path and localizes the observed policy loss to the same case, but R621 did not rerun the agent/policy evaluator; the exact causal link from that response to the policy event, general task-quality effect, and internal numerical/state mechanism remain unproven. The R614 failed safety gate remains in force; no promotion.'}

def summarize_server_prompt_path(rows,server_log,selected_request_id):
 """Pair server task timing rows with captured requests by order and exact token counts."""
 turns=sorted((x for x in rows if x.get('kind')=='agent_turn'),key=lambda x:x['start_ns'])
 warmups=sorted((x for x in rows if x.get('kind')=='warmup'),key=lambda x:x['start_ns'])
 assert len(warmups)>=1
 task_order=[]; task_data={}
 for line in Path(server_log).read_text(errors='replace').splitlines():
  m=re.search(r'task\s+(\d+)\s+\|\s+processing task, is_child = 0',line)
  if m:
   tid=m.group(1);assert tid not in task_data
   task_data[tid]={'lines':[]};task_order.append(tid)
  m=re.search(r'task\s+(\d+)\s+\|',line)
  if m and m.group(1) in task_data:task_data[m.group(1)]['lines'].append(line)
 assert len(task_order)==len(turns)+len(warmups)
 def parse_task(tid):
  out={}
  for line in task_data[tid]['lines']:
   m=re.search(r'task\.n_tokens\s*=\s*(\d+)',line)
   if m:out['prompt_tokens']=int(m.group(1))
   m=re.search(r'prompt eval time\s*=\s*([0-9.]+)\s*ms\s*/\s*(\d+)\s+tokens',line)
   if m:out.update(prompt_eval_ms=float(m.group(1)),prompt_eval_tokens=int(m.group(2)))
   m=re.search(r'eval time\s*=\s*([0-9.]+)\s*ms\s*/\s*(\d+)\s+tokens',line)
   if m:out.update(decode_ms=float(m.group(1)),completion_tokens=int(m.group(2)))
   m=re.search(r'cached n_tokens\s*=\s*(\d+)',line)
   if m and 'initial_context_cached_tokens' not in out:out['initial_context_cached_tokens']=int(m.group(1))
   if 'restored context checkpoint' in line:out['checkpoint_restore_logged']=True
   if 'forcing full prompt re-processing due to lack of cache data' in line:out['full_reprocess_fallback_logged']=True
  return out
 tasks=[parse_task(tid) for tid in task_order[len(warmups):]] # warmups precede scored turns
 assert len(tasks)==len(turns)
 for turn,task in zip(turns,tasks):
  usage=turn['reply']['usage']
  assert task.get('prompt_tokens')==usage['prompt_tokens']
  assert task.get('completion_tokens')==usage['completion_tokens']
  assert 'prompt_eval_tokens' in task and 'decode_ms' in task
 selected=[(turn,task) for turn,task in zip(turns,tasks) if turn['id']==selected_request_id]
 assert len(selected)==1
 turn,task=selected[0];usage=turn['reply']['usage'];timing=turn['reply']['__verbose']['timings']
 return {'requests':len(turns),'server_tasks':len(tasks),'exact_input_and_completion_token_matches':len(turns),
         'input_tokens':usage['prompt_tokens'],'completion_tokens':usage['completion_tokens'],
         'server_input_eval_tokens':task['prompt_eval_tokens'],
         'server_input_eval_ms':task['prompt_eval_ms'],
         'initial_context_cached_tokens':task.get('initial_context_cached_tokens'),
         'checkpoint_restore_logged':bool(task.get('checkpoint_restore_logged',False)),
         'full_reprocess_fallback_logged':bool(task.get('full_reprocess_fallback_logged',False)),
         'selected_reported_cached_tokens':usage.get('prompt_tokens_details',{}).get('cached_tokens'),
         'selected_engine_cache_n':timing.get('cache_n'),
         'selected_cache_flag':turn['request'].get('cache_prompt')}

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
   'task_level_repeatability':'NOT_ESTIMATED_FROM_THIS_AB_PAIR',
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
 commit='097cf33d9499b1eade67d51e16d7c75427e7b267';source_sha256_expected='6b5fdf2b246017b074c239e8f0b93f9d6952b4715501269627fec7a11b00bab7'
 assert digest(src)==source_sha256_expected
 hybrid=root/'staging/r31/extra/source/src/llama-memory-hybrid.cpp'
 recurrent=root/'staging/r31/extra/source/src/llama-memory-recurrent.cpp'
 hybrid_sha256='907b769206d9b29b8ee2dd0f04ead29e99810843edaecb722ddbbac852d0bf1e'
 recurrent_sha256='51172be188d0eece2267c9105dc5a8d2c3ef7ebd58e88a6f562ac6ee36326f98'
 assert digest(hybrid)==hybrid_sha256 and digest(recurrent)==recurrent_sha256
 lines=src.read_text(errors='replace').splitlines()
 hybrid_lines=hybrid.read_text(errors='replace').splitlines()
 recurrent_lines=recurrent.read_text(errors='replace').splitlines()
 common=root/'staging/r31/extra/source/common/common.h'
 common_sha256_expected='2a2d084f28932b04ca0a26687bd4c4744bd68e504956d50f8f5719cbbecca4cd'
 assert digest(common)==common_sha256_expected
 common_lines=common.read_text(errors='replace').splitlines()
 cache_reuse_default=next((i for i,line in enumerate(common_lines,1) if 'int32_t n_cache_reuse       = 0;' in line),None)
 assert cache_reuse_default==634
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
 assert all(source_lines.values()) and digest(src)==source_sha256_expected
 hybrid_recurrent=hybrid_recurrent_state_semantics(hybrid_lines,recurrent_lines)
 runs={};profiles={}
 for rid in ('r614','r616'):
  audit_path=root/'staging'/rid/'AUDIT.json';audit=json.loads(audit_path.read_text());raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());log=raw/'server.log';rows=[json.loads(x) for x in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if x];turns=[x for x in rows if x.get('kind')=='agent_turn']
  assert digest(log)==pins['server.log'] and digest(raw/'HTTP_RESULTS.jsonl')==pins['HTTP_RESULTS.jsonl'] and digest(raw/'profile.json')==pins['profile.json'] and digest(raw/'LAUNCH.json')==pins['LAUNCH.json']
  cache_flags=collections.Counter(str(x.get('request',{}).get('cache_prompt','MISSING')) for x in turns)
  assert cache_flags=={'True':len(turns)}
  launch=json.loads((raw/'LAUNCH.json').read_text())
  argv=launch.get('argv',[])
  cache_reuse_option_present=any(str(arg)=='--cache-reuse' for arg in argv)
  if rid=='r616':assert not cache_reuse_option_present and launch.get('native_request_options',{}).get('cache_prompt') is True
  text=log.read_text(errors='replace')
  runs[rid.upper()]={
   'audit_sha256':digest(audit_path),'server_log_sha256':pins['server.log'],'profile_sha256':pins['profile.json'],'requests_with_cache_prompt_true':len(turns),
   'cache_reuse_option_present':cache_reuse_option_present,
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
 lost_case=next(x['id'] for x in base['checks'] if x['task_success'] and not next(y for y in candidate['checks'] if y['id']==x['id'])['task_success'])
 baseline_identity=next(x for x in base['rows'] if x.get('kind')=='input_identity' and x.get('case_id')==lost_case and x.get('turn')==2)
 candidate_identity=next(x for x in candidate['rows'] if x.get('kind')=='input_identity' and x.get('case_id')==lost_case and x.get('turn')==2)
 baseline_server_path=summarize_server_prompt_path(base['rows'],Path(base['audit']['raw_root'])/'server.log',baseline_identity['id'])
 candidate_server_path=summarize_server_prompt_path(candidate['rows'],Path(candidate['audit']['raw_root'])/'server.log',candidate_identity['id'])
 assert baseline_server_path['server_input_eval_tokens']==1790 and baseline_server_path['selected_engine_cache_n']==0 and baseline_server_path['initial_context_cached_tokens']==0
 assert candidate_server_path['server_input_eval_tokens']==115 and candidate_server_path['selected_engine_cache_n']==1675 and candidate_server_path['initial_context_cached_tokens']==1675
 assert not baseline_server_path['checkpoint_restore_logged'] and not candidate_server_path['checkpoint_restore_logged']
 assert not baseline_server_path['full_reprocess_fallback_logged'] and not candidate_server_path['full_reprocess_fallback_logged']
 assert baseline_server_path['requests']==154 and candidate_server_path['requests']==156
 task_divergence['server_execution_path']={'baseline':baseline_server_path,'candidate':candidate_server_path,
  'interpretation':'Server task logs align one-to-one with every captured scored request by exact input and completion token counts. On the lost task’s divergent third turn, baseline began with no reusable context and evaluated all 1,790 input tokens; candidate began with 1,675 reusable prefix tokens and evaluated 115. Neither selected server task logged checkpoint restore or full-prompt fallback. This verifies the common-prefix compute path, not whole-task cache causality or an internal state/numerical mechanism.'}
 # R620 subsequently repeated this exact exposed prompt in two sessions.
 # Preserve the task-level causal limit, but replace the now-stale claim that
 # no no-cache A/A existed for the prompt.
 exact_prompt_ids=next(x for x in base['rows'] if x.get('kind')=='input_identity' and x.get('case_id')==lost_case and x.get('turn')==2)['prompt_token_ids']
 followup=omni_cache_aa_repeatability(root,exact_prompt_ids)
 task_divergence['repeatability_followup']=followup
 task_divergence['interpretation']='The sole R536-success/R616-failure case had two identical earlier replies; the first divergent response was turn 3, where the candidate reported reusing 1,675 prefix tokens and diverged at output token 0. R620 later repeated this exact exposed prompt: no-cache outputs were identical in 4/4 trials, while cache-on produced two distinct sequences across 4/4 trials (164/166 tokens), each differing from the no-cache output at token 0. This shows baseline variability was not observed but candidate variability was observed for this one prompt. It narrows the repeatability concern; it does not prove that cache behavior caused the complete-task or policy outcome, identify a numerical/GDN mechanism, or qualify the cache.'
 # The R614 policy-pass loss is independently tied to a repeated request-level
 # cache divergence by the balanced, two-session R621 diagnostic.
 baseline_audit=json.loads((root/'staging/r531/AUDIT.json').read_text())
 candidate_audit=json.loads((root/'staging/r614/AUDIT.json').read_text())
 baseline_raw=Path(baseline_audit['raw_root']);candidate_raw=Path(candidate_audit['raw_root'])
 for raw in (baseline_raw,candidate_raw):
  pins=json.loads((raw/'RAW_HASHES.json').read_text())
  for filename in ('HTTP_RESULTS.jsonl','profile.json','LAUNCH.json','server.log'):
   assert digest(raw/filename)==pins[filename]
 baseline_profile=json.loads((baseline_raw/'profile.json').read_text())
 candidate_profile=json.loads((candidate_raw/'profile.json').read_text())
 baseline_launch=json.loads((baseline_raw/'LAUNCH.json').read_text())
 candidate_launch=json.loads((candidate_raw/'LAUNCH.json').read_text())
 assert baseline_profile['model_sha256']==candidate_profile['model_sha256']==baseline_audit['model_sha256']==candidate_audit['model_sha256']
 assert baseline_profile['runtime']==candidate_profile['runtime']
 assert baseline_profile['chat_template']==candidate_profile['chat_template']
 assert baseline_launch['argv']==candidate_launch['argv']
 assert {k:v for k,v in baseline_launch['environment'].items() if k!='O2_GPU_BUILD_LEASE'}=={k:v for k,v in candidate_launch['environment'].items() if k!='O2_GPU_BUILD_LEASE'}
 baseline_rows=[json.loads(x) for x in (baseline_raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if x]
 candidate_rows=[json.loads(x) for x in (candidate_raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if x]
 baseline_cases={x['id']:x['reported_result'] for x in baseline_rows if x.get('kind')=='agent_case'}
 candidate_cases={x['id']:x['reported_result'] for x in candidate_rows if x.get('kind')=='agent_case'}
 assert baseline_cases.keys()==candidate_cases.keys() and len(baseline_cases)==33
 policy_lost=[key for key in baseline_cases if baseline_cases[key]['policy_gate_pass'] and not candidate_cases[key]['policy_gate_pass']]
 assert len(policy_lost)==1
 case_id=policy_lost[0]
 def case_turn(rows):
  identity=next(x for x in rows if x.get('kind')=='input_identity' and x.get('case_id')==case_id and x.get('turn')==3)
  response=next(x for x in rows if x.get('kind')=='agent_turn' and x.get('id')==identity['id'])
  return identity,response
 baseline_identity,baseline_response=case_turn(baseline_rows)
 candidate_identity,candidate_response=case_turn(candidate_rows)
 assert baseline_identity['prompt_token_ids']==candidate_identity['prompt_token_ids']
 assert baseline_identity['prompt_token_ids_sha256']==candidate_identity['prompt_token_ids_sha256']
 assert baseline_identity['prompt_token_count']==candidate_identity['prompt_token_count']==1785
 r621_stage=root/'staging/r621';r621_audit=json.loads((r621_stage/'AUDIT.json').read_text())
 r621_review=json.loads((r621_stage/'INDEPENDENT_REVIEW.json').read_text())
 r621_plan=json.loads((r621_stage/'PLAN.json').read_text())
 assert r621_audit['reference_audit_sha256']==digest(root/'staging/r531/AUDIT.json')
 assert r621_audit['source_screen_audit_sha256']==digest(root/'staging/r614/AUDIT.json')
 assert r621_plan['reference_audit_sha256']==r621_audit['reference_audit_sha256']
 assert r621_plan['candidate_audit_sha256']==r621_audit['source_screen_audit_sha256']
 assert r621_plan['model_sha256']==baseline_audit['model_sha256']
 r621_raw=root.parent/'research/mcp-workspace/r621-nexus-aa-abba-token-pilot/host-20261029T080641Z'
 r621_http=r621_raw/'HTTP_RESULTS.jsonl'
 assert digest(r621_http)==r621_audit['raw_responses_sha256']==r621_review['raw_responses_sha256']
 r621_rows=[json.loads(x) for x in r621_http.read_text().splitlines() if x]
 input_rows={x['id']:x for x in r621_rows if x.get('kind')=='r621_input'}
 expected_cases=json.loads((r621_stage/'CPU_PILOT_INPUT.json').read_text())['cases']
 pilot_expected=[x for x in expected_cases if x['turn']==4]
 assert len(pilot_expected)==1
 expected_hash=baseline_identity['prompt_token_ids_sha256']
 assert all(x['expected_prompt_token_ids_sha256']==expected_hash and x['expected_prompt_token_ids']==baseline_identity['prompt_token_ids'] for x in pilot_expected)
 template_review=json.loads((r621_stage/'CPU_TEMPLATE_REVIEW.json').read_text())
 rendered=next(x for x in template_review['records'] if x['turn']==4)
 assert rendered['equal'] and rendered['actual_ids_sha256']==rendered['expected_ids_sha256']==expected_hash
 pilot_replies=[];pilot_seed_checks=[]
 for row in r621_rows:
  if row.get('kind')!='r621_request' or row['id'] not in input_rows:continue
  ir=input_rows[row['id']]
  if ir['prompt_token_ids_sha256']!=expected_hash:continue
  assert ir['prompt_token_ids']==baseline_identity['prompt_token_ids']
  pilot_replies.append(row);pilot_seed_checks.append(row)
 assert len(pilot_replies)==8
 assert all(x['reply']['__verbose']['generation_settings']['seed']==x['request']['seed']==1001 for x in pilot_replies)
 assert all(x['reply']['__verbose']['generation_settings']['temperature']==x['request']['temperature']==0 for x in pilot_replies)
 nexus_policy_mapping=summarize_nexus_policy_case(
  baseline_cases[case_id],candidate_cases[case_id],baseline_response['request'],candidate_response['request'],
  baseline_response['reply'],candidate_response['reply'],pilot_replies,
  baseline_identity['prompt_token_ids'],pilot_seed_checks)
 baseline_server_path=summarize_server_prompt_path(baseline_rows,baseline_raw/'server.log',baseline_response['id'])
 candidate_server_path=summarize_server_prompt_path(candidate_rows,candidate_raw/'server.log',candidate_response['id'])
 assert baseline_server_path['server_input_eval_tokens']==1785
 assert baseline_server_path['selected_engine_cache_n']==0
 assert baseline_server_path['initial_context_cached_tokens']==0
 assert candidate_server_path['server_input_eval_tokens']==74
 assert candidate_server_path['selected_engine_cache_n']==1711
 assert candidate_server_path['initial_context_cached_tokens']==1711
 assert not baseline_server_path['checkpoint_restore_logged'] and not candidate_server_path['checkpoint_restore_logged']
 assert not baseline_server_path['full_reprocess_fallback_logged'] and not candidate_server_path['full_reprocess_fallback_logged']
 assert candidate_server_path['selected_reported_cached_tokens']==1711
 assert baseline_server_path['selected_cache_flag'] is False
 assert candidate_server_path['selected_cache_flag'] is True
 assert baseline_server_path['requests']==153 and candidate_server_path['requests']==155
 nexus_policy_mapping['server_execution_path']={
  'baseline':baseline_server_path,'candidate':candidate_server_path,
  'interpretation':'Server task records align one-to-one with every captured agent request by exact input and completion token counts. For the matched request, baseline began with no reusable context and evaluated all 1,785 input tokens; candidate began with 1,711 reusable prefix tokens and evaluated 74. Neither selected server task logged checkpoint restore or full-prompt fallback. This confirms the common-prefix compute path for this request, not why its first generated token changed or whether caching caused the complete-task policy outcome.'}
 nexus_policy_mapping.update({'baseline_audit_sha256':digest(root/'staging/r531/AUDIT.json'),
                              'candidate_audit_sha256':digest(root/'staging/r614/AUDIT.json'),
                              'repeatability_audit_sha256':digest(r621_stage/'AUDIT.json'),
                              'repeatability_capture_sha256':digest(r621_http)})
 source_lines['cache_reuse_default']=cache_reuse_default
 return {
  'kind':'PINNED_SOURCE_AND_HASHED_LOG_RECONCILIATION','source_commit':commit,'source_file_sha256':source_sha256_expected,'source_lines':source_lines,'runs':runs,
  'common_header_sha256':common_sha256_expected,
  'R616_prefix_execution':{'cache_prompt':True,'cache_reuse_option_present':runs['R616']['cache_reuse_option_present'],'effective_n_cache_reuse':0,'basis':'Pinned common.h default; R616 launch does not pass --cache-reuse.'},
  'external_issue':{
   'url':'https://github.com/ggml-org/llama.cpp/issues/22940',
   'status':'CLOSED_NOT_PLANNED',
   'claim':'FULL-only memory backends always fall back because the checkpoint restore path is not consulted when pos_min == -1.',
   'local_applicability':'NOT_ESTABLISHED; pinned source explicitly selects checkpoint state for FULL-only rollback and contains an explicit pos_min == -1 abort guard. R614/R616 logs contain checkpoint-restore events, so the issue’s blanket permanent-disablement claim does not describe every request in these runs.',
  'remaining_limit':'Per-request input-compute counts are mapped for the R614 policy case; checkpoint restore/fallback event attribution and internal recurrent-state/numerical mechanism remain unresolved, as does whole-task policy causality.'
  },
  'source_interpretation':[
   'The request-level cache_prompt path finds a matching prompt prefix; the server can reuse cached chunks.',
   'Context checkpoints save target state (and the source also saves draft/speculative state); the source comment says recurrent state cannot be rewound from only the final state.',
   'In the pinned hybrid-memory implementation, PARTIAL_ONLY omits attention-memory serialization/restoration but still serializes/restores recurrent memory; the recurrent implementation writes cell metadata and tensor state. Missing recurrent checkpoint serialization is therefore not supported by this code path.',
   'The source TODO about checkpoint position coverage is explicitly scoped to SWA. Both R614 and R616 logs report n_swa=0; the divergent R616 request has no checkpoint restore or full-prompt fallback. That TODO is not an evidenced explanation for this divergence.',
   'When a usable checkpoint is unavailable for a hybrid/recurrent context, this code path forces full prompt re-processing.',
   'The log message that the host RAM prompt cache is disabled is a separate cache layer; it does not mean the per-request cache_prompt flag was off.',
  ],
  'causal_disposition':'OBSERVED_CACHE_ASSOCIATED_TOKEN_DIVERGENCE; INTERNAL_STATE_OR_NUMERICAL_CAUSE_UNRESOLVED',
  'case_level_divergence':task_divergence,
  'nexus_policy_case_mapping':nexus_policy_mapping,
  'limits':'R616’s one lost task is mapped to an exact matching 1,790-token prompt and first changed token. R620 repeats the exact prompt in two sessions: selected no-cache outputs are stable in 4/4 trials, while cache-on outputs vary across two sequences in 4/4 trials. These are exposed request-level observations only; no logits, per-layer state, or request-to-checkpoint restore/fallback mapping was captured. The evidence does not prove task/policy causality or identify a numerical/GDN state mechanism.',
  'hybrid_recurrent_state':{'source_commit':commit,'hybrid_source_sha256':hybrid_sha256,'recurrent_source_sha256':recurrent_sha256,**hybrid_recurrent,'partial_only_semantics':'attention memory excluded; recurrent memory serialized/restored','R614_n_swa_values':[0],'R616_n_swa_values':[0],'SWA_checkpoint_position_TODO_applies':False,'divergent_R616_checkpoint_restore_logged':False,'divergent_R616_full_prompt_fallback_logged':False,'interpretation':'Does not identify the cause of token divergence. Actual recurrent-state values, logits and intermediate numerics were not captured.'},
  'GPU_runs':0,'model_requests':0,
 }

def hybrid_recurrent_state_semantics(hybrid_lines,recurrent_lines):
 """Summarize the pinned hybrid PARTIAL_ONLY checkpoint serialization path."""
 def find(lines,needle):return next((i for i,line in enumerate(lines,1) if needle in line),None)
 write_cond=find(hybrid_lines,'if ((flags & LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY) == 0) {')
 write_attn=find(hybrid_lines,'mem_attn->state_write(io, seq_id, flags);')
 write_recr=find(hybrid_lines,'mem_recr->state_write(io, seq_id, flags);')
 read_cond=find(hybrid_lines,'const bool read_attn = (flags & LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY) == 0;')
 read_attn_call=find(hybrid_lines,'mem_attn->state_read(io, seq_id, flags);')
 read_recr=find(hybrid_lines,'mem_recr->state_read(io, seq_id, flags);')
 write_close=next((i for i in range(write_attn+1,len(hybrid_lines)+1) if hybrid_lines[i-1].strip()=='}'),None) if write_attn else None
 assert write_cond and write_attn and write_recr and write_close and write_recr>write_close
 read_close=next((i for i in range(read_attn_call+1,len(hybrid_lines)+1) if hybrid_lines[i-1].strip()=='}'),None) if read_attn_call else None
 assert read_cond and read_attn_call and read_recr and read_close and read_recr>read_close
 recurrent_write=find(recurrent_lines,'void llama_memory_recurrent::state_write(')
 recurrent_data=find(recurrent_lines,'state_write_data(io, cell_ranges_data);')
 recurrent_read=find(recurrent_lines,'void llama_memory_recurrent::state_read(')
 assert recurrent_write and recurrent_data and recurrent_read
 return {'hybrid_source_lines':{'partial_write_attention_guard':write_cond,'attention_write':write_attn,'recurrent_write_after_guard':write_recr,'partial_read_attention_guard':read_cond,'attention_read':read_attn_call,'recurrent_read_after_guard':read_recr},'recurrent_source_lines':{'state_write':recurrent_write,'state_write_data':recurrent_data,'state_read':recurrent_read}}

def seed_execution_path(data, captures, root):
 """Reconcile archived seed fields with the pinned per-request sampler path."""
 commit='097cf33d9499b1eade67d51e16d7c75427e7b267'
 if data['build_source']['commit']!=commit:return None
 checks=data['build_source'].get('checks',{})
 expected={
  'tools/server/server-schema.cpp':'1f9d7b73b4363b90b08de0360b0a5ce0b3d152750bfb8d587a367e90c7904050',
  'tools/server/server-context.cpp':'6b5fdf2b246017b074c239e8f0b93f9d6952b4715501269627fec7a11b00bab7',
  'common/sampling.cpp':'b6a1f963fd75fd17d12bafb59351a1009d2358dd789dba7ed10943340f8e5553',
 }
 assert all(checks[k]['actual']==checks[k]['proof']==v for k,v in expected.items())
 profiles={}
 for key,(turns,_) in captures.items():
  configured=data['profiles'][key]['configured_seed']
  req=collections.Counter(str(r['request'].get('seed','MISSING')) for r in turns.values())
  server=collections.Counter(str(r['reply'].get('__verbose',{}).get('generation_settings',{}).get('seed','MISSING')) for r in turns.values())
  assert dict(req)==data['profiles'][key]['request_seeds']
  assert dict(server)==data['profiles'][key]['server_reported_seeds']
  assert len(req)==len(server)==1 and next(iter(req))==next(iter(server))==str(configured)
  settings=collections.Counter()
  for r in turns.values():
   g=r['reply'].get('__verbose',{}).get('generation_settings',{})
   settings[(g.get('temperature'),g.get('n_probs'),g.get('backend_sampling'),
             tuple(g.get('samplers',[])[-1:]),g.get('dynatemp_range'))]+=1
  temp0_greedy=sum(n for (temp,n_probs,backend,last,dynatemp),n in settings.items()
                   if temp==0 and n_probs==0 and backend is False and last==('temperature',)
                   and dynatemp==0)
  profiles[key]={
   'request_count':len(turns),'configured_seed':configured,
   'request_seed_counts':dict(req),'server_reported_seed_counts':dict(server),
   'all_request_and_reported_seeds_match':True,
   'observed_sampling_settings':[{'temperature':k[0],'n_probs':k[1],
      'backend_sampling':k[2],'final_sampler':list(k[3]),'dynatemp_range':k[4],
      'requests':n} for k,n in sorted(settings.items(),key=lambda x:str(x[0]))],
   'source_greedy_condition_requests':temp0_greedy,
  }
 qwen35=qwen35_seed_profile(root)
 if qwen35:profiles['r535']=qwen35
 return {
  'engine_commit':commit,
  'source_sha256':expected,
  'source_locations':{
   'request_seed_field':'tools/server/server-schema.cpp:175',
   'global_defaults_then_request_overrides':'tools/server/server-schema.cpp:470-495',
   'per-task_sampler_initialization':'tools/server/server-context.cpp:1925',
   'greedy_sampler_selection':'common/sampling.cpp:403-406',
   'temperature_zero_argmax':'src/llama-sampler.cpp:265-280',
   'multi-choice_child_seed_offset':'tools/server/server-task.h:287-291',
  },
  'profiles':profiles,
  'interpretation':'The archived requests and server-reported settings carry the configured seed in every reviewed request. The pinned server overlays request fields on global defaults and initializes a sampler for each task; multi-choice child tasks intentionally offset seeds. For R614/R616, temperature=0, n_probs=0, backend sampling=false, final sampler=temperature, and dynatemp_range=0 satisfy the pinned greedy-sampler branch, so RNG seed variation is not a sufficient explanation for their token divergence. This does not establish deterministic GPU logits or identify a cache/kernel/state cause. Gemma temperature=1 remains stochastic even with a fixed per-request seed.'
 }

def qwen35_seed_profile(root):
 """Verify seed propagation in Qwen3.5 R535 without treating unique tasks as A/A."""
 root=Path(root);stage=root/'staging/r535';audit_path=stage/'AUDIT.json'
 if not audit_path.is_file():return None
 audit=json.loads(audit_path.read_text());raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text())
 for name in ('profile.json','LAUNCH.json','HTTP_RESULTS.jsonl','server.log'):
  assert name in pins and digest(raw/name)==pins[name]
  assert audit['original_raw_files_sha256'][name]==pins[name]
 profile=json.loads((raw/'profile.json').read_text())
 assert digest(raw/'profile.json')==audit['profile_sha256']
 assert profile['model_sha256']==audit['model_sha256']=='02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d'
 argv=profile['native_recipe']['argv_tail'];seed=next((int(argv[i+1]) for i,x in enumerate(argv[:-1]) if x=='--seed'),None)
 assert seed==1001
 rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line]
 turns={x['id']:x for x in rows if x.get('kind')=='agent_turn'}
 identities={x['id']:x for x in rows if x.get('kind')=='input_identity'}
 assert len(turns)==162 and turns.keys()==identities.keys()
 req=collections.Counter(str(x['request'].get('seed','MISSING')) for x in turns.values())
 server=collections.Counter(str(x['reply'].get('__verbose',{}).get('generation_settings',{}).get('seed','MISSING')) for x in turns.values())
 assert dict(req)==dict(server)=={str(seed):len(turns)}
 settings=collections.Counter()
 for x in turns.values():
  g=x['reply'].get('__verbose',{}).get('generation_settings',{})
  settings[(g.get('temperature'),g.get('n_probs'),g.get('backend_sampling'),tuple(g.get('samplers',[])[-1:]),g.get('dynatemp_range'))]+=1
 assert len(settings)==1
 (temperature,n_probs,backend,last_sampler,dynatemp),setting_count=next(iter(settings.items()))
 hashes=[]
 for identity in identities.values():
  ids=identity['prompt_token_ids'];token_hash=hashlib.sha256(json.dumps(ids,separators=(',',':')).encode()).hexdigest()
  assert token_hash==identity['prompt_token_ids_sha256'] and len(ids)==identity['prompt_token_count']
  hashes.append(token_hash)
 repeated=sum(n>1 for n in collections.Counter(hashes).values())
 assert repeated==0
 warmup=qwen35_warmup_repeatability(root)
 return {'experiment_id':'R535','model':'Qwen3.5-9B','model_sha256':profile['model_sha256'],
  'audit_sha256':digest(audit_path),'profile_sha256':digest(raw/'profile.json'),
  'request_count':len(turns),'configured_seed':seed,'configured_temperature':temperature,
  'request_seed_counts':dict(req),
  'server_reported_seed_counts':dict(server),'all_request_and_reported_seeds_match':True,
  'unique_tokenized_prompts':len(set(hashes)),'repeated_tokenized_prompts':repeated,
  'observed_sampling_settings':[{'temperature':temperature,'n_probs':n_probs,'backend_sampling':backend,
   'final_sampler':list(last_sampler),'dynatemp_range':dynatemp,'requests':setting_count}],
  'source_greedy_condition_requests':setting_count if temperature==0 and n_probs==0 and backend is False and last_sampler==('temperature',) and dynatemp==0 else 0,
  'same_prompt_AA_repeats':'NOT_MEASURED','warmup_repeatability':warmup,
  'disposition':'SEED_PROPAGATION_VERIFIED; SYNTHETIC_WARMUP_TEXT_REPEATABILITY_OBSERVED; TASK_LEVEL_AA_NOT_MEASURED'}

def qwen35_warmup_repeatability(root):
 """Compare exact synthetic warmup requests and output text across archived Qwen3.5 runs."""
 root=Path(root);phase=root if (root/'staging').is_dir() else root/'phase_o2_restart_20261015_2245';experiment_ids=('r501','r509','r519','r535');runs=[]
 expected_model='02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d'
 for ident in experiment_ids:
  audit_path=phase/f'staging/{ident}/AUDIT.json'
  if not audit_path.is_file():return None
  audit=json.loads(audit_path.read_text());raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text())
  for name in ('profile.json','LAUNCH.json','HTTP_RESULTS.jsonl','server.log'):
   assert name in pins and digest(raw/name)==pins[name]
   assert audit['original_raw_files_sha256'][name]==pins[name]
  profile=json.loads((raw/'profile.json').read_text())
  assert profile['model_sha256']==expected_model
  recipe=profile['native_recipe']
  argv=recipe['argv_tail'];seed=next((int(argv[i+1]) for i,x in enumerate(argv[:-1]) if x=='--seed'),None)
  runtime={k:v for k,v in profile['assets'].items() if '/runtime/' in k}
  template_sha=profile['assets'].get(profile['chat_template'])
  assert seed==1001 and recipe['context']==8192 and runtime and template_sha
  rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line]
  warmups={x['id']:x for x in rows if x.get('kind')=='warmup'}
  assert set(warmups)=={'warmup-0','warmup-1'}
  runs.append({'experiment_id':ident,'audit_sha256':digest(audit_path),
   'profile_sha256':digest(raw/'profile.json'),'model_sha256':profile['model_sha256'],
   'argv_sha256':hashlib.sha256(json.dumps(argv,separators=(',',':')).encode()).hexdigest(),
   'runtime_assets_sha256':hashlib.sha256(json.dumps(runtime,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
   'request_options_sha256':hashlib.sha256(json.dumps(recipe['request_options'],sort_keys=True,separators=(',',':')).encode()).hexdigest(),
   'template_sha256':template_sha,
   'environment':recipe['environment'],'context':recipe['context'],'warmups':warmups})
 assert len({x['model_sha256'] for x in runs})==1
 assert len({x['argv_sha256'] for x in runs})==1
 assert len({x['runtime_assets_sha256'] for x in runs})==1
 assert len({x['request_options_sha256'] for x in runs})==1
 assert len({x['template_sha256'] for x in runs})==1
 assert len({json.dumps(x['environment'],sort_keys=True) for x in runs})==1
 assert len({x['context'] for x in runs})==1
 evidence=[]
 for warm_id in ('warmup-0','warmup-1'):
  observations=[]
  for run in runs:
   item=run['warmups'][warm_id];request=item['request'];reply=item['reply'];settings=reply['generation_settings']
   request_settings={k:request.get(k) for k in ('seed','temperature','n_predict','cache_prompt','ignore_eos','stream')}
   assert request_settings=={'seed':1001,'temperature':0,'n_predict':(1 if warm_id=='warmup-0' else 128),'cache_prompt':False,'ignore_eos':True,'stream':False}
   assert settings.get('seed')==1001 and settings.get('temperature')==0 and settings.get('backend_sampling') is False
   observations.append({'prompt_sha256':hashlib.sha256(request['prompt'].encode()).hexdigest(),
    'request_settings':request_settings,
    'output_text_sha256':hashlib.sha256(reply['content'].encode()).hexdigest(),
    'output_characters':len(reply['content']),'tokens_predicted':reply['tokens_predicted'],
    'stop_type':reply.get('stop_type'),'returned_token_ids':len(reply.get('tokens',[]))})
  assert len({x['prompt_sha256'] for x in observations})==1
  assert len({json.dumps(x['request_settings'],sort_keys=True) for x in observations})==1
  assert len({x['output_text_sha256'] for x in observations})==1
  assert len({x['tokens_predicted'] for x in observations})==1
  evidence.append({'warmup_id':warm_id,'independent_profiles':len(observations),
   'prompt_sha256':observations[0]['prompt_sha256'],'request_settings':observations[0]['request_settings'],
   'output_text_sha256':observations[0]['output_text_sha256'],
   'output_characters':observations[0]['output_characters'],
   'tokens_predicted':observations[0]['tokens_predicted'],
   'sampling_and_prompt_text_match_across_profiles':True,
   'token_ids':'NOT_CAPTURED','logits':'NOT_CAPTURED'})
 return {'experiment_ids':list(experiment_ids),'audit_sha256':{x['experiment_id']:x['audit_sha256'] for x in runs},
  'profile_sha256':{x['experiment_id']:x['profile_sha256'] for x in runs},
  'distinct_gpu_experiments':len(runs),'model_sha256':expected_model,
  'argv_sha256':runs[0]['argv_sha256'],'runtime_assets_sha256':runs[0]['runtime_assets_sha256'],
  'request_options_sha256':runs[0]['request_options_sha256'],'template_sha256':runs[0]['template_sha256'],
  'same_model_engine_runtime_argv_template_and_context_verified':True,'warmups':evidence,
  'interpretation':'Identical synthetic warmup prompt bytes and output text hashes were observed across four separately audited GPU experiments. This is narrow warmup text-repeatability evidence only; it does not characterize task-level quality variability. API token IDs and logits were not captured. The 128-token warmup is an output-limit path, not a scored complete task.'}

def logprobs_diagnostic_path(data, captures):
 """Check whether the pinned non-stream API can expose bounded token probabilities."""
 commit='097cf33d9499b1eade67d51e16d7c75427e7b267'
 if data['build_source']['commit']!=commit:return None
 checks=data['build_source'].get('checks',{})
 expected='c4d53b4c72ca825434a035a4b632c8bc71e709d22fe33ca149fde95cee8460a1'
 assert checks['tools/server/server-common.cpp']['actual']==checks['tools/server/server-common.cpp']['proof']==expected
 sampling_sha='b6a1f963fd75fd17d12bafb59351a1009d2358dd789dba7ed10943340f8e5553'
 assert checks['common/sampling.cpp']['actual']==checks['common/sampling.cpp']['proof']==sampling_sha
 turns=captures['r616'][0]
 shape=collections.Counter((r['request'].get('stream'), 'tools' in r['request'],
                            'logprobs' in r['request'], 'top_logprobs' in r['request'])
                           for r in turns.values())
 count=data['profiles']['r616']['request_count']
 assert sum(shape.values())==count and shape=={(False,True,False,False):count}
 return {
  'source_file_sha256':expected,
  'source_locations':{'logprobs_parse_and_stream_guard':'tools/server/server-common.cpp:1455-1463',
                      'pre_sampling_logits_collection':'tools/server/server-context.cpp:1932',
                      'probability_output':'tools/server/server-task.cpp:256-289'},
  'r616_requests':len(turns),'non_stream_with_tools':count,
  'logprobs_requested':0,'top_logprobs_requested':0,
  'pinned_api_support':'SUPPORTED_FOR_NON_STREAM_TOOL_REQUESTS',
  'default_top_logprobs':20,
  'sampler_effect':'Requesting probabilities disables the n_probs==0 greedy fast-path and selects the distribution sampler in this pinned build; temperature zero remains in the chain. Identical output versus the original uninstrumented profile is not established.',
  'sampling_source_sha256':sampling_sha,
  'limit':'Top-20 probability/logprob view only; not a full raw-logit vector. Enabling it changes the sampler chain as well as instrumentation; match both arms and compare separately against the original uninstrumented profile.',
  'decision':'R616 frozen profile remains unchanged. Any token-probability diagnosis requires a separate reviewed broker profile; no GPU request or run was made.'
 }

def r630_native_aa(root):
 """Verify and safely summarize the R536/R630 same-profile replay and counter bounds."""
 root=Path(root);stage=root/'staging/r630';addendum=stage/'COUNTER_ENERGY_BOUNDS.json'
 if not addendum.is_file():return None
 raw_dirs={
  'R536':root.parent/'research/mcp-workspace/r536-native-validation33/host-20261025T092944Z',
  'R630':root.parent/'research/mcp-workspace/r630-native-validation33/host-20261029T163436Z',
 }
 comparison=json.loads((stage/'AA_COMPARISON.json').read_text())
 replay=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())
 receipt=json.loads((stage/'CPU_REPLAY_RECEIPT.json').read_text())
 energy=json.loads(addendum.read_text())
 assert comparison['experiment_id']=='R630' and comparison['official_benchmark'] is False
 assert replay['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and replay['result']['cases']==33
 assert receipt['systemd_result']=='success' and receipt['result']['GPU_runs']==0
 runs={};profiles={}
 captures={}
 for ident,raw in raw_dirs.items():
  audit=json.loads((raw/'AUDIT.json').read_text());pins=json.loads((raw/'RAW_HASHES.json').read_text())
  for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json'):
   assert name in pins and digest(raw/name)==pins[name]
  rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line]
  by_kind={kind:{x['id']:x for x in rows if x.get('kind')==kind and x.get('id')}
           for kind in ('input_identity','agent_turn','agent_case')}
  assert len(by_kind['input_identity'])==len(by_kind['agent_turn'])==154
  assert len(by_kind['agent_case'])==33 and audit['measurement_valid'] is True
  profiles[ident]=json.loads((raw/'profile.json').read_text())
  captures[ident]=by_kind
  cases=list(by_kind['agent_case'].values())
  runs[ident]={'experiment_id':ident,'audit_sha256':pins['AUDIT.json'],'raw_capture_sha256':pins['HTTP_RESULTS.jsonl'],
               'tasks':33,'solved':sum(bool(x['reported_result']['task_success']) for x in cases),
               'policy_gate_pass':sum(bool(x['reported_result']['policy_gate_pass']) for x in cases),
               'task_scope_pass':sum(bool(x['reported_result']['task_scope_pass']) for x in cases),
               'task_phase_s':audit['case_inference_wall_s'],'peak_vram_mib':audit['peak_device_vram_mib']}
 a,b=profiles['R536'],profiles['R630']
 for profile in (a,b):profile.pop('execution_review',None);profile.pop('review',None)
 assert a==b
 left,right=captures['R536'],captures['R630']
 input_match=request_match=token_match=case_match=0
 for ident,x in left['input_identity'].items():
  y=right['input_identity'].get(ident)
  if y and x.get('prompt_token_ids_sha256')==y.get('prompt_token_ids_sha256'):input_match+=1
 for ident,x in left['agent_turn'].items():
  y=right['agent_turn'].get(ident)
  if not y:continue
  request_match+=x.get('request_sha256')==y.get('request_sha256')
  token_match+=x['reply']['__verbose']['tokens']==y['reply']['__verbose']['tokens']
 stable=('case_id','domain','task_success','policy_gate_pass','task_scope_pass','failure_reasons',
         'total_model_rounds','all_tools_simulated','production_tools_connected','actual','expected')
 for ident,x in left['agent_case'].items():
  y=right['agent_case'].get(ident)
  if y and all(x['reported_result'].get(k)==y['reported_result'].get(k) for k in stable):case_match+=1
 assert (input_match,request_match,token_match,case_match)==(154,154,154,33)
 assert runs['R536']['solved']==runs['R630']['solved']==28
 assert energy['baseline']['raw_capture_sha256']==runs['R536']['raw_capture_sha256']
 assert energy['candidate']['raw_capture_sha256']==runs['R630']['raw_capture_sha256']
 e0=energy['baseline']['whole_gpu_task_phase_energy_bounds_j'];e1=energy['candidate']['whole_gpu_task_phase_energy_bounds_j']
 overlap=max(e0['lower'],e1['lower'])<=min(e0['upper'],e1['upper'])
 assert overlap==energy['comparison']['energy_bounds_overlap'] is True
 return {'status':'A_A_REPRODUCED_ON_EXPOSED_FROZEN33', 'baseline':runs['R536'],'candidate':runs['R630'],
         'identical_prompts':input_match,'identical_requests':request_match,
         'identical_generated_token_sequences':token_match,'identical_task_outcomes':case_match,
         'gpu_energy_counter_bounds_j':{'R536':e0,'R630':e1},
         'gross_gpu_j_per_success_bounds':{'R536':energy['baseline']['gross_GPU_J_per_success_bounds'],
                                           'R630':energy['candidate']['gross_GPU_J_per_success_bounds']},
         'energy_bounds_overlap':True,'energy_scope':'Whole task-phase GPU-board counter bounds; per-case power integration incomplete; excludes CPU/system energy.',
         'limits':'Same exposed validation tasks, not an unseen holdout or official benchmark. One A/A pair only; no speed or energy winner, no Champion qualification.',
         'evidence':{'R536_audit_sha256':runs['R536']['audit_sha256'],'R536_capture_sha256':runs['R536']['raw_capture_sha256'],
                     'R630_audit_sha256':runs['R630']['audit_sha256'],'R630_capture_sha256':runs['R630']['raw_capture_sha256'],
                     'counter_addendum_sha256':digest(addendum),'CPU_replay_sha256':digest(stage/'INDEPENDENT_REVIEW.json')}}

def r631_native_aa(root):
 """Verify and publish only aggregate evidence for the R531/R631 Nexus A/A replay."""
 root=Path(root);stage=root/'staging/r631';result_path=stage/'AA_RESULT.json'
 if not result_path.is_file():return None
 result=json.loads(result_path.read_text());receipt=json.loads((stage/'CPU_REPLAY_RECEIPT.json').read_text())
 admission=json.loads((stage/'BROKER_ADMISSION.json').read_text())
 assert result['experiment_id']=='R631' and result['baseline_experiment_id']=='R531'
 assert result['status']=='COMPLETE_CPU_REPLAYED_NOT_QUALIFICATION'
 assert admission['broker_registration']=='REGISTERED_AND_PRECHECK_PASSED' and admission['GPU_started'] is True
 assert admission['single_start'] is True and admission['task_budget_seconds']==1200
 assert receipt['status']=='SUCCESS' and receipt['result']['GPU_runs']==0 and receipt['result']['model_requests']==0
 assert receipt['result']['scored_tasks']==33 and receipt['result']['solved']==25
 runs={};captures={}
 raw_dirs={
  'R531':root.parent/'research/mcp-workspace/r531-native-validation33/host-20261025T081403Z',
  'R631':root.parent/'research/mcp-workspace/r631-native-validation33/host-20261029T181806Z',
 }
 for ident,raw in raw_dirs.items():
  pins=json.loads((raw/'RAW_HASHES.json').read_text());audit=json.loads((raw/'AUDIT.json').read_text())
  for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json'):
   assert digest(raw/name)==pins[name]
  assert audit['experiment_id'].startswith(ident.lower()) and audit['measurement_valid'] is True and audit['GPU_execution_observed'] is True
  profile=json.loads((raw/'profile.json').read_text())
  assert profile['model_sha256']==result['configuration_identity']['model_sha256']
  rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line]
  indexed={kind:{x['id']:x for x in rows if x.get('kind')==kind and x.get('id')}
           for kind in ('input_identity','agent_turn','agent_case')}
  expected=153 if ident=='R531' else 153
  assert len(indexed['input_identity'])==len(indexed['agent_turn'])==expected
  assert len(indexed['agent_case'])==33
  cases=list(indexed['agent_case'].values())
  runs[ident]={'experiment_id':ident,'tasks':33,
    'solved':sum(bool(x['reported_result']['task_success']) for x in cases),
    'policy_pass':sum(bool(x['reported_result']['policy_gate_pass']) for x in cases),
    'audit_sha256':pins['AUDIT.json'],'capture_sha256':pins['HTTP_RESULTS.jsonl'],
    'profile_sha256':pins['profile.json'],'telemetry_sha256':pins['GPU_TELEMETRY.jsonl']}
  captures[ident]=indexed
 assert runs['R531']['solved']==runs['R631']['solved']==25
 assert runs['R531']['policy_pass']==runs['R631']['policy_pass']==29
 assert receipt['scorer_sha256']==result['independent_cpu_replay']['scorer_sha256']
 assert receipt['stdout_sha256']==result['independent_cpu_replay']['stdout_sha256']
 left,right=captures['R531'],captures['R631'];prompt_match=token_match=visible_match=0
 for key,x in left['input_identity'].items():
  y=right['input_identity'].get(key)
  if y and x['prompt_token_ids_sha256']==y['prompt_token_ids_sha256']:prompt_match+=1
 for key,x in left['agent_turn'].items():
  y=right['agent_turn'].get(key)
  if not y:continue
  ar,br=x['reply']['__verbose'],y['reply']['__verbose']
  token_match+=ar['tokens']==br['tokens']
  visible_match+=(x['reply'].get('content')==y['reply'].get('content') and
                  x['reply'].get('tool_calls',[])==y['reply'].get('tool_calls',[]))
 cases_match=0
 stable=('task_success','policy_gate_pass','task_scope_pass','failure_reasons','total_model_rounds')
 for key,x in left['agent_case'].items():
  y=right['agent_case'].get(key)
  if y and all(x['reported_result'].get(k)==y['reported_result'].get(k) for k in stable):cases_match+=1
 assert (prompt_match,token_match,visible_match,cases_match)==(153,153,153,33)
 m=result['metrics'];a=m['r531'];b=m['r631']
 assert (a['task_wall_s'],b['task_wall_s'])==(319.983392506,320.859687076)
 assert b['energy_complete_case_count']==0 and b['peak_vram_mib']==7356.5
 return {'status':'A_A_REPRODUCED_ON_EXPOSED_FROZEN33','baseline':runs['R531'],'candidate':runs['R631'],
  'identical_prompt_token_sequences':prompt_match,'identical_generated_token_sequences':token_match,
  'identical_visible_replies':visible_match,'identical_task_outcomes':cases_match,
  'metrics':{'R531':{k:a[k] for k in ('task_wall_s','decode_tps','prefill_tps','e2e_median_s','peak_vram_mib','energy_task_phase_j','joules_per_success','energy_complete_case_count','telemetry')},
             'R631':{k:b[k] for k in ('task_wall_s','decode_tps','prefill_tps','e2e_median_s','peak_vram_mib','energy_task_phase_j','joules_per_success','energy_complete_case_count','telemetry')}},
  'cpu_replay':{'status':'PASS','cases':33,'solved':25,'model_requests':0,'gpu_runs':0,
                'receipt_sha256':digest(stage/'CPU_REPLAY_RECEIPT.json'),'scorer_sha256':receipt['scorer_sha256']},
  'interpretation':'One matched pair showed no observed task, policy, prompt-token or generated-token divergence. It does not prove global determinism or equivalence. Timing and aggregate energy are descriptive only; no winner or Champion change.',
  'limits':'Exposed internal validation set, not holdout or official benchmark. Per-case energy is unavailable for R631 (0/33); whole-task-phase NVML board-counter bounds are not per-task energy and exclude CPU/system energy. R614/R621 cache-associated cause remains unresolved.',
  'evidence':{'R531_audit_sha256':runs['R531']['audit_sha256'],'R531_capture_sha256':runs['R531']['capture_sha256'],
              'R631_audit_sha256':runs['R631']['audit_sha256'],'R631_capture_sha256':runs['R631']['capture_sha256'],
              'R631_admission_sha256':digest(stage/'BROKER_ADMISSION.json'),'R631_result_sha256':digest(result_path)}}

def verify_aa_runtime_identity(profiles,launches):
 """Exclude only administrative review and per-run lease identifiers."""
 def profile(p):return {k:v for k,v in p.items() if k not in ('review','execution_review')}
 def launch(p):
  p=dict(p);p['environment']={k:v for k,v in p['environment'].items() if k!='O2_GPU_BUILD_LEASE'};return p
 assert profile(profiles[0])==profile(profiles[1])
 assert launch(launches[0])==launch(launches[1])

def r633_native_aa(root):
 """Verify the Gemma R534/R633 A/A pair without exporting private traces."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r633';result_path=stage/'AA_RESULT.json'
 if not result_path.is_file():return None
 result=json.loads(result_path.read_text());receipt=json.loads((stage/'CPU_REPLAY_RECEIPT.json').read_text())
 assert result['experiment_id']=='R633' and result['baseline']=='R534' and result['winner_qualified'] is False
 assert receipt['status']=='SUCCESS' and receipt['cases']==33 and receipt['solved']==17 and receipt['GPU_runs']==receipt['model_requests']==0
 assert digest(stage/'CPU_REPLAY_RECEIPT.json')==result['cpu_replay_sha256']
 assert digest(stage/'cpu-replay.stdout')==receipt['stdout_sha256'] and digest(stage/'CPU_INPUTS/quality_eval.py')==receipt['scorer_sha256']=='92e123a86cd8624f0ba68ca6d0ffcb5bd641f5565b55377f52f31e73835d22af'
 replay=json.loads(next(line for line in (stage/'cpu-replay.stdout').read_text().splitlines() if line.startswith('AGENT18_REPLAY_JSON ')).split(' ',1)[1])
 assert replay['cases']==33 and replay['solved']==17 and replay['all_scores_and_effects_reproduced'] is True and replay['GPU_runs']==replay['model_requests']==0 and replay['real_evaluator_uid']!=0
 raw0=Path(json.loads((root/'staging/r534/AUDIT.json').read_text())['raw_root'])
 raw1=root.parent/'research/mcp-workspace/r633-native-validation33/host-20261029T215000Z'
 captures={};metrics={};profiles=[];launches=[]
 for ident,raw in (('R534',raw0),('R633',raw1)):
  pins=json.loads((raw/'RAW_HASHES.json').read_text());audit=json.loads((raw/'AUDIT.json').read_text())
  for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
  assert pins['AUDIT.json']==result['audit_sha256'][ident] and pins['HTTP_RESULTS.jsonl']==result['raw_capture_sha256'][ident]
  assert audit['measurement_valid'] is True and audit['GPU_execution_observed'] is True
  profile=json.loads((raw/'profile.json').read_text());options=profile['native_recipe']['request_options']
  profiles.append(profile);launches.append(json.loads((raw/'LAUNCH.json').read_text()))
  assert profile['model_sha256']=='93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b' and options['seed']==1001 and options['temperature']==1.0 and options['cache_prompt'] is False
  rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines() if line];index={kind:{x['id']:x for x in rows if x.get('kind')==kind} for kind in ('agent_case','agent_turn','input_identity')}
  assert len(index['agent_case'])==33 and len(index['agent_turn'])==len(index['input_identity'])==177
  telemetry=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];cases=list(index['agent_case'].values());bounds=counter_energy_bounds(telemetry,cases,[x['id'] for x in cases]);record=result['metrics'][ident]
  assert bounds['group_window_s']==record['case_window_s'] and [bounds['lower_j'],bounds['upper_j']]==record['gpu_case_window_j_bounds']
  assert record['gpu_j_per_success_bounds']==[bounds['lower_j']/17,bounds['upper_j']/17]
  assert record['peak_vram_mib']==audit['peak_device_vram_mib'] and record['energy_complete_cases']==audit['energy_complete_cases']
  assert record['max_temperature_c']==max(z['temperature_c'] for z in telemetry if isinstance(z.get('temperature_c'),(int,float)))
  assert record['uncorrected_ecc_observed']==any(z.get('ecc_uncorrected',0)>0 for z in telemetry)
  assert record['throttle_masks']==sorted({z['clock_throttle_event_mask'] for z in telemetry if z.get('clock_throttle_event_mask') is not None})
  captures[ident]=index;metrics[ident]=record
 verify_aa_runtime_identity(profiles,launches)
 a,b=captures['R534'],captures['R633'];assert all(a[k].keys()==b[k].keys() for k in a)
 for key in a['agent_turn']:
  assert a['input_identity'][key]['prompt_token_ids']==b['input_identity'][key]['prompt_token_ids']
  assert a['agent_turn'][key]['request']==b['agent_turn'][key]['request']
  assert a['agent_turn'][key]['reply']['__verbose']['tokens']==b['agent_turn'][key]['reply']['__verbose']['tokens']
 for key in a['agent_case']:
  x=a['agent_case'][key]['reported_result'];y=b['agent_case'][key]['reported_result']
  assert all(x[k]==y[k] for k in ('task_success','policy_gate_pass','task_scope_pass'))
 assert sum(x['reported_result']['task_success'] for x in a['agent_case'].values())==17
 assert sum(x['reported_result']['policy_gate_pass'] for x in a['agent_case'].values())==29
 assert result['outcomes']=={'R534_solved':17,'R633_solved':17,'R534_policy_pass':29,'R633_policy_pass':29,'identical_task_outcomes':33,'identical_policy_outcomes':33,'identical_input_token_sequences':177,'identical_request_bodies':177,'identical_generated_token_sequences':177,'first_divergence':'NONE_OBSERVED'}
 return {'status':result['status'],'scope':result['scope'],'outcomes':result['outcomes'],'metrics':metrics,'energy_scope':result['energy_scope'],'audit_sha256':result['audit_sha256'],'raw_capture_sha256':result['raw_capture_sha256'],'result_sha256':digest(result_path),'cpu_replay_sha256':result['cpu_replay_sha256'],'winner_qualified':False}

def validate_r635_pair(a,b):
 assert all(a[k].keys()==b[k].keys() for k in a)
 for k in a['agent_turn']:
  assert a['agent_turn'][k]['request']==b['agent_turn'][k]['request'] and a['input_identity'][k]['prompt_token_ids']==b['input_identity'][k]['prompt_token_ids'] and a['agent_turn'][k]['reply']['__verbose']['tokens']==b['agent_turn'][k]['reply']['__verbose']['tokens']
 for k in a['agent_case']:
  x=a['agent_case'][k]['reported_result'];y=b['agent_case'][k]['reported_result'];assert all(x[v]==y[v] for v in ('task_success','policy_gate_pass'))
 assert len(a['agent_case'])==33 and len(a['agent_turn'])==150
 assert sum(x['reported_result']['task_success'] for x in a['agent_case'].values())==27 and sum(x['reported_result']['policy_gate_pass'] for x in a['agent_case'].values())==31

def qwen_native_aa(root,baseline_id,trial_id):
 """Recompute a Qwen A/A pair from pinned raw evidence."""
 from leaderboard import counter_energy_bounds
 assert (baseline_id,trial_id) in (('R618','R635'),('R625','R636'))
 root=Path(root);stage=root/'staging'/trial_id.lower();path=stage/'AA_RESULT.json'
 if not path.is_file():return None
 result=json.loads(path.read_text());receipt=json.loads((stage/'CPU_REPLAY_RECEIPT.json').read_text())
 assert result['experiment_id']==trial_id and result['baseline']==baseline_id and result['status']=='GPU_COMPLETE_INDEPENDENT_CPU_REPLAYED' and result['winner_qualified'] is False
 assert digest(stage/'CPU_REPLAY_RECEIPT.json')==result['cpu_replay_sha256']
 assert receipt['status']=='SUCCESS' and receipt['cases']==33 and receipt['solved']==27 and receipt['GPU_runs']==receipt['model_requests']==0
 assert digest(stage/'cpu-replay.stdout')==receipt['stdout_sha256'] and digest(stage/'CPU_INPUTS/quality_eval.py')==receipt['scorer_sha256']=='e18c5e03b37e31ae55092e22f18209970a5b7b318371fd8710a48a764923d43c'
 replay=json.loads(next(line for line in (stage/'cpu-replay.stdout').read_text().splitlines() if line.startswith('AGENT18_REPLAY_JSON ')).split(' ',1)[1])
 assert replay['cases']==33 and replay['solved']==27 and replay['all_scores_and_effects_reproduced'] is True and replay['real_evaluator_uid']!=0 and replay['GPU_runs']==replay['model_requests']==0
 baseline=Path(json.loads((root/'staging'/baseline_id.lower()/'AUDIT.json').read_text())['raw_root']);captures=list((root.parent/'research/mcp-workspace'/(trial_id.lower()+'-lean-final-validation33')).glob('host-*'));assert len(captures)==1
 indexed={};profiles=[];launches=[];metrics={}
 for ident,raw in ((baseline_id,baseline),(trial_id,captures[0])):
  pins=json.loads((raw/'RAW_HASHES.json').read_text());audit=json.loads((raw/'AUDIT.json').read_text())
  for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
  assert pins['AUDIT.json']==result['raw_comparison']['audit_sha256'][ident] and audit['measurement_valid'] is True and audit['GPU_execution_observed'] is True
  p=json.loads((raw/'profile.json').read_text());assert p['model_sha256']=='58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f';profiles.append(p);launches.append(json.loads((raw/'LAUNCH.json').read_text()))
  rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];idx={kind:{x['id']:x for x in rows if x.get('kind')==kind} for kind in ('agent_case','agent_turn','input_identity')}
  assert len(idx['agent_case'])==33 and len(idx['agent_turn'])==len(idx['input_identity'])==150
  tele=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];cases=list(idx['agent_case'].values());bounds=counter_energy_bounds(tele,cases,[x['id'] for x in cases]);m=result['metrics'][ident]
  assert m['case_window_s']==bounds['group_window_s'] and m['gpu_case_window_j_bounds']==[bounds['lower_j'],bounds['upper_j']] and m['gpu_j_per_success_bounds']==[bounds['lower_j']/27,bounds['upper_j']/27]
  assert m['peak_vram_mib']==audit['peak_device_vram_mib'] and m['energy_complete_cases']==audit['energy_complete_cases']
  indexed[ident]=idx;metrics[ident]=m
 verify_aa_runtime_identity(profiles,launches);validate_r635_pair(indexed[baseline_id],indexed[trial_id])
 assert result['raw_comparison']['turn_comparison']=={'identical_output_tokens':150}
 assert result['raw_comparison']['paired_outcomes']=={'task_success_both_pass':27,'task_success_both_fail':6,'task_success_gained':0,'task_success_lost':0,'policy_gate_pass_both_pass':31,'policy_gate_pass_both_fail':2,'policy_gate_pass_gained':0,'policy_gate_pass_lost':0}
 return {'status':result['status'],'scope':result['scope'],'paired_outcomes':result['raw_comparison']['paired_outcomes'],'turn_comparison':result['raw_comparison']['turn_comparison'],'metrics':metrics,'energy_scope':result['energy_scope'],'audit_sha256':result['raw_comparison']['audit_sha256'],'result_sha256':digest(path),'cpu_replay_sha256':result['cpu_replay_sha256'],'winner_qualified':False}

def r637_balanced_mtp(root):
 """Validate the two selected ABBA comparisons without exporting requests."""
 root=Path(root);stage=root/'staging/r637';audit=stage/'AUDIT.json';review=stage/'INDEPENDENT_REVIEW.json'
 if not audit.is_file() or not review.is_file():return None
 a=json.loads(audit.read_text());v=json.loads(review.read_text())
 assert a['status']=='FOUR_SESSION_ABBA_REQUEST_DIAGNOSTIC_COMPLETE' and a['winner_qualified'] is False and a['official_benchmark'] is False
 assert v['status']=='INDEPENDENT_CPU_RAW_TOKEN_REVIEW_PASSED' and v['audit_sha256']==digest(audit) and v['raw_sha256']==a['raw_responses_sha256']
 dirs=list((root.parent/'research/mcp-workspace/r637-qwen38-mtp-abba-token-pilot').glob('host-*'));assert len(dirs)==1
 raw=dirs[0];assert digest(raw/'HTTP_RESULTS.jsonl')==a['raw_responses_sha256'] and digest(raw/'AUDIT.json')==a['broker_audit_sha256']
 rows=[json.loads(l) for l in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];seq={x['id']:x['reply']['__verbose']['tokens'] for x in rows if x.get('kind')=='r637_request'}
 assert set(seq)=={f's{s}-t{t}' for s in range(1,5) for t in (1,2)}
 for t in (1,2):
  a0,b1,b2,a1=(seq[f's{s}-t{t}'] for s in range(1,5));first=next((i for i,(x,y) in enumerate(zip(a0,b1)) if x!=y),min(len(a0),len(b1)) if len(a0)!=len(b1) else None)
  c=v['checks'][t-1];assert c['request']==t and c['off_repeat_equal']==(a0==a1) and c['on_repeat_equal']==(b1==b2) and c['first_off_on_divergence']==first
  assert a['turns'][t-1]['first_divergence_positions'][0]==first
 argument_path=stage/'ARGUMENT_REVIEW.json';arg_result=None
 if argument_path.is_file():
  ar=json.loads(argument_path.read_text());assert ar['status']=='CPU_SEMANTIC_ARGUMENT_COMPARISON' and ar['raw_responses_sha256']==digest(raw/'HTTP_RESULTS.jsonl') and ar['GPU_runs']==ar['model_requests']==0
  by_id={x['id']:x for x in rows if x.get('kind')=='r637_request'}
  for t in (1,2):
   messages=[by_id[f's{i}-t{t}']['reply']['choices'][0]['message'] for i in range(1,5)];assert all(len(m['tool_calls'])==1 for m in messages)
   f=[m['tool_calls'][0]['function'] for m in messages];args=[json.loads(x['arguments']) for x in f];assert all(type(x) is dict for x in args)
   c=ar['checks'][t-1];expected={'request':t,'tool_call_count_each':1,'same_tool_name':len({x['name'] for x in f})==1,'same_argument_keys':all(set(x)==set(args[0]) for x in args),'same_arguments_within_off':args[0]==args[3],'same_arguments_within_on':args[1]==args[2],'same_arguments_off_vs_on':args[0]==args[1],'same_content':all(x.get('content')==messages[0].get('content') for x in messages)};assert c==expected
  arg_result={'checks':ar['checks'],'review_sha256':digest(argument_path),'scope':ar['scope']}
 return {'experiment_id':'R637','argument_review':arg_result,'task_phase_s':a['task_phase_s'],'peak_device_vram_mib':a['peak_device_vram_mib'],'turns':a['turns'],'audit_sha256':digest(audit),'review_sha256':digest(review),'broker_audit_sha256':a['broker_audit_sha256'],'raw_responses_sha256':a['raw_responses_sha256'],'scope':a['scope'],'winner_qualified':False}

def qwen_mtp_cross_review(root,on_aa,off_aa):
 """Validate observed ON/OFF differences without treating them as causal."""
 root=Path(root);file=root/'staging/r636/MTP_CROSS_REVIEW.json'
 if not file.is_file():return None
 assert on_aa is not None and off_aa is not None
 review=json.loads(file.read_text());assert review['status']=='FOUR_CAPTURE_CROSS_REVIEW_COMPLETE' and review['GPU_runs']==review['model_requests']==0
 for ident,aa in (('R618',on_aa),('R635',on_aa),('R625',off_aa),('R636',off_aa)):
  assert review['captures'][ident]['audit']==aa['audit_sha256'][ident]
 captures={}
 for ident in ('R635','R636'):
  dirs=list((root.parent/'research/mcp-workspace'/(ident.lower()+'-lean-final-validation33')).glob('host-*'));assert len(dirs)==1;path=dirs[0]/'HTTP_RESULTS.jsonl'
  assert digest(path)==review['captures'][ident]['responses']
  rows=[json.loads(line) for line in path.read_text().splitlines()];captures[ident]={kind:{x['id']:x for x in rows if x.get('kind')==kind} for kind in ('agent_turn','input_identity','agent_case')}
 x,y=captures['R635'],captures['R636'];assert all(x[k].keys()==y[k].keys() for k in x)
 equal=0;positions=[];cases=set();tokens=[0,0];wall=[0.0,0.0]
 for key in sorted(x['agent_turn']):
  a,b=x['agent_turn'][key],y['agent_turn'][key];assert a['request']==b['request'] and x['input_identity'][key]['prompt_token_ids']==y['input_identity'][key]['prompt_token_ids']
  u,v=a['reply']['__verbose']['tokens'],b['reply']['__verbose']['tokens'];tokens[0]+=len(u);tokens[1]+=len(v);wall[0]+=a['e2e_s'];wall[1]+=b['e2e_s']
  if u==v:equal+=1
  else:cases.add(key.rsplit('--turn',1)[0]);positions.append(next((i for i,(p,q) in enumerate(zip(u,v)) if p!=q),min(len(u),len(v))))
 assert len(x['agent_turn'])==review['matching_request_and_input_tokens']==150 and equal==review['identical_output_turns'] and len(positions)==review['different_output_turns'] and len(cases)==review['affected_cases']
 assert sorted(positions)==review['first_divergence_indices_sorted'] and tokens==review['generated_tokens_mtp_on_off'] and wall==review['summed_request_wall_s_mtp_on_off']
 assert all(x['agent_case'][k]['reported_result'][z]==y['agent_case'][k]['reported_result'][z] for k in x['agent_case'] for z in ('task_success','policy_gate_pass'))
 return {**review,'review_sha256':digest(file)}

def summarize_r634_sequences(groups,baseline):
 """Return aggregates only; input prompts and output tokens stay private."""
 assert len(groups)==len(baseline)==3
 result=[]
 for group,ref in zip(groups,baseline):
  assert len(group)==12 and [x[0] for x in group]==[1001,1002,1003,1003,1002,1001]*2
  sequences={seed:[tokens for actual,tokens in group if actual==seed] for seed in (1001,1002,1003)}
  assert all(len(v)==4 and all(x==v[0] for x in v) for v in sequences.values())
  pairs=[]
  for a,b in ((1001,1002),(1001,1003),(1002,1003)):
   x,y=sequences[a][0],sequences[b][0];first=next((i for i,(u,v) in enumerate(zip(x,y)) if u!=v),min(len(x),len(y)))
   pairs.append({'seeds':[a,b],'equal':x==y,'first_divergence':None if x==y else first})
  result.append({'request':len(result)+1,'baseline_seed_matches_r633':sequences[1001][0]==ref,'seed_pairs':pairs,'all_fixed_seed_repeats_equal':True})
 return result

def r634_seed_pilot(root):
 """Validate R634's frozen input, GPU audit, seed outputs and CPU review."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r634';file=stage/'AUDIT.json'
 if not file.is_file():return None
 audit=json.loads(file.read_text());review=json.loads((stage/'INDEPENDENT_TOKEN_REVIEW.json').read_text());plan=json.loads((stage/'PREREGISTRATION.json').read_text())
 assert audit['experiment_id']=='R634' and audit['winner_qualified'] is False and audit['official_benchmark'] is False and audit['tool_executions']==0
 assert digest(file)==review['local_audit_sha256'] and review['status']=='COMPLETE_INDEPENDENT_TOKEN_REVIEW' and review['GPU_runs']==0
 assert digest(stage/'PRIVATE_FROZEN_INPUTS.json')==plan['frozen_inputs_sha256'] and digest(root/'staging/r633/AA_RESULT.json')==audit['baseline_aa_result_sha256']
 captures=list((root.parent/'research/mcp-workspace/r634-gemma-long-seed-token-pilot').glob('host-*'));assert len(captures)==1;raw=captures[0];pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','LAUNCH.json','CONTRACT.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==audit['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==audit['raw_responses_sha256'] and pins['GPU_TELEMETRY.jsonl']==audit['raw_telemetry_sha256']
 assert gpu['measurement_valid'] is True and gpu['GPU_execution_observed'] is True and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==audit['peak_device_vram_mib']
 rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];turns=[x for x in rows if x.get('kind')=='r634_request'];inputs=[x for x in rows if x.get('kind')=='r634_input'];frozen=json.loads((stage/'PRIVATE_REQUESTS.json').read_text())['cases'];assert len(turns)==len(inputs)==len(frozen)==36
 for t,i,c in zip(turns,inputs,frozen):
  assert t['id']==i['id']==c['id'] and json.dumps(t['request'],ensure_ascii=True,allow_nan=False)==c['request_json'] and i['prompt_token_ids']==c['expected_prompt_token_ids']
  assert t['reply']['__verbose']['generation_settings']['temperature']==1.0
 source=list((root.parent/'research/mcp-workspace/r633-native-validation33').glob('host-*'));assert len(source)==1
 source_pins=json.loads((source[0]/'RAW_HASHES.json').read_text());assert digest(source[0]/'HTTP_RESULTS.jsonl')==source_pins['HTTP_RESULTS.jsonl']
 orig={x['id']:x for x in (json.loads(line) for line in (source[0]/'HTTP_RESULTS.jsonl').read_text().splitlines()) if x.get('kind')=='agent_turn'}
 chosen=json.loads((stage/'PRIVATE_FROZEN_INPUTS.json').read_text())['cases'];baseline=[orig[x['id']]['reply']['__verbose']['tokens'] for x in chosen]
 groups=[[(x['reply']['__verbose']['generation_settings']['seed'],x['reply']['__verbose']['tokens']) for x in [turns[i+3*j] for j in range(12)]] for i in range(3)]
 result=summarize_r634_sequences(groups,baseline);assert result==review['results']
 telemetry=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];energy=counter_energy_bounds(telemetry,turns,[x['id'] for x in turns]);assert energy==audit['energy_counter']
 return {'status':audit['status'],'scope':audit['scope'],'results':result,'task_phase_s':audit['task_phase_s'],'peak_vram_mib':audit['peak_device_vram_mib'],'energy_counter':energy,'audit_sha256':digest(file),'broker_audit_sha256':audit['broker_audit_sha256'],'raw_responses_sha256':audit['raw_responses_sha256'],'review_sha256':digest(stage/'INDEPENDENT_TOKEN_REVIEW.json'),'winner_qualified':False}

def r639_policy_replay(root):
 """Verify the scoped R639 replay from hash-pinned captures; export aggregates only."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r639';file=stage/'AUDIT.json'
 if not file.is_file():return None
 audit=json.loads(file.read_text());review=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text());plan=json.loads((stage/'PREREGISTRATION.json').read_text())
 assert audit['experiment_id']=='R639' and audit['winner_qualified'] is False and audit['official_benchmark'] is False and audit['tool_executions']==0
 assert digest(file)==review['audit_sha256'] and review['status']=='INDEPENDENT_CPU_CAPTURE_REVIEW' and review['gpu_runs']==0
 assert digest(stage/'PRIVATE_FROZEN_INPUTS.json')==plan['frozen_inputs_sha256'] and digest(root/'staging/r638/AUDIT.json')==audit['reference_audit_sha256']
 captures=list((root.parent/'research/mcp-workspace/r639-gemma-policy-repeat-token-pilot').glob('host-*'));assert len(captures)==1;raw=captures[0];pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','LAUNCH.json','CONTRACT.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==audit['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==audit['raw_responses_sha256'] and pins['GPU_TELEMETRY.jsonl']==audit['raw_telemetry_sha256']
 assert gpu['measurement_valid'] is True and gpu['GPU_execution_observed'] is True and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==audit['peak_device_vram_mib']
 original=json.loads((stage/'PRIVATE_FROZEN_INPUTS.json').read_text())['cases'];frozen=json.loads((stage/'PRIVATE_REQUESTS.json').read_text())['cases']
 baseline=json.loads((root/'staging/r638/AUDIT.json').read_text());source=Path(baseline['raw_root']);source_pins=json.loads((source/'RAW_HASHES.json').read_text());assert digest(source/'HTTP_RESULTS.jsonl')==source_pins['HTTP_RESULTS.jsonl']==plan['source_r638_responses_sha256']
 source_turns={x['request_sha256']:x for x in (json.loads(line) for line in (source/'HTTP_RESULTS.jsonl').read_text().splitlines()) if x.get('kind')=='agent_turn'}
 for item in original:
  row=source_turns[item['source_request_sha256']];assert row['request']==item['request'] and row['reply']['__verbose']['tokens']==item['recorded_output_tokens']
 rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];turns=[x for x in rows if x.get('kind')=='r639_request'];inputs=[x for x in rows if x.get('kind')=='r639_input'];assert len(turns)==len(inputs)==len(frozen)==8
 for t,i,c in zip(turns,inputs,frozen):
  assert t['id']==i['id']==c['id'] and json.dumps(t['request'],ensure_ascii=True,allow_nan=False)==c['request_json'] and i['prompt_token_ids']==c['expected_prompt_token_ids']
  settings=t['reply']['__verbose']['generation_settings'];assert settings['temperature']==0 and settings['seed']==1001
 results=[]
 for index in range(2):
  group=turns[index::2];seq=[x['reply']['__verbose']['tokens'] for x in group];results.append({'repetitions':len(group),'identical_to_r638':sum(x==original[index]['recorded_output_tokens'] for x in seq),'all_four_equal':all(x==seq[0] for x in seq),'output_tokens':len(seq[0])})
 assert results==review['cases']
 telemetry=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];energy=counter_energy_bounds(telemetry,turns,[x['id'] for x in turns]);assert energy==review['energy']
 return {'status':audit['status'],'scope':audit['scope'],'cases':results,'task_phase_s':audit['task_phase_s'],'peak_vram_mib':audit['peak_device_vram_mib'],'energy_counter':energy,'audit_sha256':digest(file),'review_sha256':digest(stage/'INDEPENDENT_REVIEW.json'),'broker_audit_sha256':audit['broker_audit_sha256'],'winner_qualified':False}

def r640_policy_abba(root):
 """Verify four original captures and isolated CPU replay before public export."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r640';file=stage/'AUDIT.json'
 if not file.is_file():return None
 audit=json.loads(file.read_text());review=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())
 assert audit['experiment_id']=='R640' and not audit['winner_qualified'] and not audit['official_benchmark'] and audit['tool_executions']==0
 assert review['status']=='INDEPENDENT_CPU_REPLAY_PASSED' and review['audit_sha256']==digest(file)
 assert review['replay_sha256']==digest(stage/'independent_replay.py') and review['adapter_sha256']==digest(stage/'task_adapter_candidate.py')
 assert review['result']['gpu_runs']==0 and review['result']['model_requests']==0 and not review['result']['production_tools_connected']
 assert digest(root/'staging/r638/AUDIT.json')==audit['reference_audit_sha256']
 raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','CONTRACT.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==audit['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==audit['raw_response_sha256'] and pins['GPU_TELEMETRY.jsonl']==audit['raw_telemetry_sha256']
 assert gpu['measurement_valid'] and gpu['GPU_execution_observed'] and gpu['model_starts']==4 and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==audit['peak_device_vram_mib']
 assert review['input_sha256']['captured-profile.json']==pins['profile.json']
 labels=('A1','B1','B2','A2');cases_all=[];computed=[]
 for label,check in zip(labels,review['result']['arms']):
  name='r640-'+label+'-HTTP_RESULTS.jsonl';assert digest(raw/name)==pins[name]==review['input_sha256'][label+'.jsonl']
  assert check['arm']==label and check['cases']==2 and check['complete'] and check['all_scores_and_effects_reproduced']
  rows=[json.loads(x) for x in (raw/name).read_text().splitlines() if x];cases=[x for x in rows if x.get('kind')=='agent_case'];turns=[x for x in rows if x.get('kind')=='agent_turn'];assert len(cases)==2
  for t in turns:
   settings=t['reply']['__verbose']['generation_settings'];assert settings['seed']==1001 and settings['temperature']==(1.0 if label.startswith('A') else 0.0)
  for c in cases:
   entry=dict(c);entry['id']=label+'-'+c['id'];cases_all.append(entry)
  computed.append({'arm':label,'task_successes':sum(x['reported_result']['task_success'] for x in cases),'policy_passes':sum(x['reported_result']['policy_gate_pass'] for x in cases),'denied_calls':sum(x['reported_result']['rejected_calls'] for x in cases),'model_requests':len(turns),'completion_tokens':sum(x['reply']['usage']['completion_tokens'] for x in turns),'case_wall_s':sum(x['e2e_s'] for x in cases)})
 assert computed==audit['arms']
 telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];assert counter_energy_bounds(telemetry,cases_all,[x['id'] for x in cases_all])==audit['energy_counter']
 return {'arms':computed,'task_phase_s':audit['task_phase_s'],'peak_vram_mib':audit['peak_device_vram_mib'],'energy_counter':audit['energy_counter'],'audit_sha256':digest(file),'review_sha256':digest(stage/'INDEPENDENT_REVIEW.json'),'broker_audit_sha256':audit['broker_audit_sha256'],'scope':audit['scope'],'winner_qualified':False}

def r641_policy_abba(root):
 """Verify four original captures and isolated CPU replay before public export."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r641';file=stage/'AUDIT.json'
 if not file.is_file():return None
 audit=json.loads(file.read_text());review=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())
 assert audit['experiment_id']=='R641' and not audit['winner_qualified'] and not audit['official_benchmark'] and audit['tool_executions']==0
 assert review['status']=='INDEPENDENT_CPU_REPLAY_PASSED' and review['audit_sha256']==digest(file)
 assert review['replay_sha256']==digest(stage/'independent_replay.py') and review['adapter_sha256']==digest(stage/'task_adapter_candidate.py')
 assert review['result']['gpu_runs']==0 and review['result']['model_requests']==0 and not review['result']['production_tools_connected']
 assert digest(root/'staging/r614/AUDIT.json')==audit['reference_audit_sha256']
 raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','CONTRACT.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==audit['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==audit['raw_response_sha256'] and pins['GPU_TELEMETRY.jsonl']==audit['raw_telemetry_sha256']
 assert gpu['measurement_valid'] and gpu['GPU_execution_observed'] and gpu['model_starts']==4 and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==audit['peak_device_vram_mib']
 assert review['input_sha256']['captured-profile.json']==pins['profile.json']
 labels=('A1','B1','B2','A2');cases_all=[];computed=[]
 for label,check in zip(labels,review['result']['arms']):
  name='r641-'+label+'-HTTP_RESULTS.jsonl';assert digest(raw/name)==pins[name]==review['input_sha256'][label+'.jsonl']
  assert check['arm']==label and check['cases']==1 and check['complete'] and check['all_scores_and_effects_reproduced']
  rows=[json.loads(x) for x in (raw/name).read_text().splitlines() if x];cases=[x for x in rows if x.get('kind')=='agent_case'];turns=[x for x in rows if x.get('kind')=='agent_turn'];assert len(cases)==1
  for t in turns:
   settings=t['reply']['__verbose']['generation_settings'];assert settings['seed']==1001 and settings['temperature']==0.0 and t['request']['cache_prompt']==label.startswith('B')
  for c in cases:
   entry=dict(c);entry['id']=label+'-'+c['id'];cases_all.append(entry)
  computed.append({'arm':label,'task_successes':sum(x['reported_result']['task_success'] for x in cases),'policy_passes':sum(x['reported_result']['policy_gate_pass'] for x in cases),'denied_calls':sum(x['reported_result']['rejected_calls'] for x in cases),'model_requests':len(turns),'completion_tokens':sum(x['reply']['usage']['completion_tokens'] for x in turns),'case_wall_s':sum(x['e2e_s'] for x in cases)})
 assert computed==audit['arms']
 token=json.loads((stage/'TOKEN_REVIEW.json').read_text());assert token['audit_sha256']==digest(file) and token['independent_review_sha256']==digest(stage/'INDEPENDENT_REVIEW.json')
 for label in labels:assert token['raw_input_sha256'][label]==review['input_sha256'][label+'.jsonl']
 inputs={}
 for label in labels:
  rows=[json.loads(x) for x in (raw/('r641-'+label+'-HTTP_RESULTS.jsonl')).read_text().splitlines() if x]
  inputs[label]=([x for x in rows if x.get('kind')=='agent_turn'],[x for x in rows if x.get('kind')=='input_identity'])
  assert token['cached_prompt_tokens'][label]==[x['reply']['usage']['prompt_tokens_details']['cached_tokens'] for x in inputs[label][0]]
 for pair in token['comparisons']:
  (ta,ia),(tb,ib)=[inputs[x] for x in pair['arms']]
  assert pair['total_turns']==[len(ta),len(tb)] and len(pair['turns'])==min(len(ta),len(tb))
  for n,turn in enumerate(pair['turns']):
   a,b=ta[n],tb[n];same={k:v for k,v in a['request'].items() if k!='cache_prompt'}=={k:v for k,v in b['request'].items() if k!='cache_prompt'}
   same_ids=ia[n]['prompt_token_ids']==ib[n]['prompt_token_ids'];x=a['reply']['__verbose']['tokens'];y=b['reply']['__verbose']['tokens']
   first=next((i for i,(u,v) in enumerate(zip(x,y)) if u!=v),None)
   if first is None and len(x)!=len(y):first=min(len(x),len(y))
   assert turn=={'turn_1based':n+1,'request_equal_except_cache_flag':same,'prompt_token_ids_equal':same_ids,'first_output_token_difference_0based':first,'output_lengths':[len(x),len(y)]}
 assert all(x['first_output_token_difference_0based']==0 for pair in token['comparisons'][2:] for x in pair['turns'] if x['turn_1based']==4)
 telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];assert counter_energy_bounds(telemetry,cases_all,[x['id'] for x in cases_all])==audit['energy_counter']
 return {'arms':computed,'task_phase_s':audit['task_phase_s'],'peak_vram_mib':audit['peak_device_vram_mib'],'energy_counter':audit['energy_counter'],'audit_sha256':digest(file),'review_sha256':digest(stage/'INDEPENDENT_REVIEW.json'),'broker_audit_sha256':audit['broker_audit_sha256'],'scope':audit['scope'],'winner_qualified':False,'token_review_sha256':digest(stage/'TOKEN_REVIEW.json'),'cached_prompt_tokens':token['cached_prompt_tokens'],'comparisons':token['comparisons']}

def r642_policy_abba(root):
 """Verify four original captures and isolated CPU replay before public export."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r642';file=stage/'AUDIT.json'
 if not file.is_file():return None
 audit=json.loads(file.read_text());review=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text())
 assert audit['experiment_id']=='R642' and not audit['winner_qualified'] and not audit['official_benchmark'] and audit['tool_executions']==0
 assert review['status']=='INDEPENDENT_CPU_REPLAY_PASSED' and review['audit_sha256']==digest(file)
 assert review['replay_sha256']==digest(stage/'independent_replay.py') and review['adapter_sha256']==digest(stage/'task_adapter_candidate.py')
 assert review['result']['gpu_runs']==0 and review['result']['model_requests']==0 and not review['result']['production_tools_connected']
 assert digest(root/'staging/r616/AUDIT.json')==audit['reference_audit_sha256']
 raw=Path(audit['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','CONTRACT.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==audit['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==audit['raw_response_sha256'] and pins['GPU_TELEMETRY.jsonl']==audit['raw_telemetry_sha256']
 assert gpu['measurement_valid'] and gpu['GPU_execution_observed'] and gpu['model_starts']==4 and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==audit['peak_device_vram_mib']
 assert review['input_sha256']['captured-profile.json']==pins['profile.json']
 labels=('A1','B1','B2','A2');cases_all=[];computed=[]
 for label,check in zip(labels,review['result']['arms']):
  name='r642-'+label+'-HTTP_RESULTS.jsonl';assert digest(raw/name)==pins[name]==review['input_sha256'][label+'.jsonl']
  assert check['arm']==label and check['cases']==1 and check['complete'] and check['all_scores_and_effects_reproduced']
  rows=[json.loads(x) for x in (raw/name).read_text().splitlines() if x];cases=[x for x in rows if x.get('kind')=='agent_case'];turns=[x for x in rows if x.get('kind')=='agent_turn'];assert len(cases)==1
  for t in turns:
   settings=t['reply']['__verbose']['generation_settings'];assert settings['seed']==1001 and settings['temperature']==0.0 and t['request']['cache_prompt']==label.startswith('B')
  for c in cases:
   entry=dict(c);entry['id']=label+'-'+c['id'];cases_all.append(entry)
  computed.append({'arm':label,'task_successes':sum(x['reported_result']['task_success'] for x in cases),'policy_passes':sum(x['reported_result']['policy_gate_pass'] for x in cases),'denied_calls':sum(x['reported_result']['rejected_calls'] for x in cases),'model_requests':len(turns),'completion_tokens':sum(x['reply']['usage']['completion_tokens'] for x in turns),'case_wall_s':sum(x['e2e_s'] for x in cases)})
 assert computed==audit['arms']
 token=json.loads((stage/'TOKEN_REVIEW.json').read_text());assert token['audit_sha256']==digest(file) and token['independent_review_sha256']==digest(stage/'INDEPENDENT_REVIEW.json')
 for label in labels:assert token['raw_input_sha256'][label]==review['input_sha256'][label+'.jsonl']
 inputs={}
 for label in labels:
  rows=[json.loads(x) for x in (raw/('r642-'+label+'-HTTP_RESULTS.jsonl')).read_text().splitlines() if x]
  inputs[label]=([x for x in rows if x.get('kind')=='agent_turn'],[x for x in rows if x.get('kind')=='input_identity'])
  assert token['cached_prompt_tokens'][label]==[x['reply']['usage']['prompt_tokens_details']['cached_tokens'] for x in inputs[label][0]]
 for pair in token['comparisons']:
  (ta,ia),(tb,ib)=[inputs[x] for x in pair['arms']]
  assert pair['total_turns']==[len(ta),len(tb)] and len(pair['turns'])==min(len(ta),len(tb))
  for n,turn in enumerate(pair['turns']):
   a,b=ta[n],tb[n];same={k:v for k,v in a['request'].items() if k!='cache_prompt'}=={k:v for k,v in b['request'].items() if k!='cache_prompt'}
   same_ids=ia[n]['prompt_token_ids']==ib[n]['prompt_token_ids'];x=a['reply']['__verbose']['tokens'];y=b['reply']['__verbose']['tokens']
   first=next((i for i,(u,v) in enumerate(zip(x,y)) if u!=v),None)
   if first is None and len(x)!=len(y):first=min(len(x),len(y))
   assert turn=={'turn_1based':n+1,'request_equal_except_cache_flag':same,'prompt_token_ids_equal':same_ids,'first_output_token_difference_0based':first,'output_lengths':[len(x),len(y)]}
 assert all(x['first_output_token_difference_0based']==0 for pair in token['comparisons'][2:] for x in pair['turns'] if x['turn_1based']==3)
 telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];assert counter_energy_bounds(telemetry,cases_all,[x['id'] for x in cases_all])==audit['energy_counter']
 return {'arms':computed,'task_phase_s':audit['task_phase_s'],'peak_vram_mib':audit['peak_device_vram_mib'],'energy_counter':audit['energy_counter'],'audit_sha256':digest(file),'review_sha256':digest(stage/'INDEPENDENT_REVIEW.json'),'broker_audit_sha256':audit['broker_audit_sha256'],'scope':audit['scope'],'winner_qualified':False,'token_review_sha256':digest(stage/'TOKEN_REVIEW.json'),'cached_prompt_tokens':token['cached_prompt_tokens'],'comparisons':token['comparisons']}

def r643_mtp_agent_abba(root):
 """Recompute the eight-case ABBA metrics from immutable captures and replay."""
 import re
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r643';file=stage/'AUDIT.json'
 if not file.exists():return None
 a=json.loads(file.read_text());r=json.loads((stage/'INDEPENDENT_REVIEW.json').read_text());analysis=json.loads((stage/'ANALYSIS.json').read_text())
 assert a['experiment_id']=='R643' and not a['winner_qualified'] and not a['official_benchmark'] and a['tool_executions']==0
 assert r['status']=='INDEPENDENT_CPU_REPLAY_PASSED' and r['audit_sha256']==digest(file) and analysis['audit_sha256']==digest(file) and analysis['independent_review_sha256']==digest(stage/'INDEPENDENT_REVIEW.json')
 assert r['replay_sha256']==digest(stage/'independent_replay.py') and r['adapter_sha256']==digest(stage/'task_adapter_candidate.py') and r['result']['gpu_runs']==0 and r['result']['model_requests']==0 and not r['result']['production_tools_connected']
 assert digest(root/'staging/r618/AUDIT.json')==a['reference_audit_sha256']
 raw=Path(a['raw_root']);pins=json.loads((raw/'RAW_HASHES.json').read_text());gpu=json.loads((raw/'AUDIT.json').read_text())
 for name in ('AUDIT.json','HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl','profile.json','CONTRACT.json','LAUNCH.json'):assert digest(raw/name)==pins[name]
 assert pins['AUDIT.json']==a['broker_audit_sha256'] and pins['HTTP_RESULTS.jsonl']==a['raw_response_sha256'] and pins['GPU_TELEMETRY.jsonl']==a['raw_telemetry_sha256']
 assert gpu['measurement_valid'] and gpu['GPU_execution_observed'] and gpu['model_starts']==4 and gpu['tool_executions']==0 and gpu['peak_device_vram_mib']==a['peak_device_vram_mib'] and r['input_sha256']['captured-profile.json']==pins['profile.json']
 labels=('A1','B1','B2','A2');data={};allcases=[];computed=[]
 pattern=re.compile(r'spec common_specu:\s+statistics\s+draft-mtp:.*?#gen drafts\s*=\s*(\d+),\s*#acc drafts\s*=\s*(\d+),\s*#gen tokens\s*=\s*(\d+),\s*#acc tokens\s*=\s*(\d+),\s*#mean acc len\s*=\s*([\d.]+)')
 for label,check in zip(labels,r['result']['arms']):
  name='r643-'+label+'-HTTP_RESULTS.jsonl';assert digest(raw/name)==pins[name]==r['input_sha256'][label+'.jsonl'] and check['arm']==label and check['cases']==8 and check['complete'] and check['all_scores_and_effects_reproduced']
  launch='r643-'+label+'-LAUNCH.json';log='r643-'+label+'-server.log';assert digest(raw/launch)==pins[launch] and digest(raw/log)==pins[log];argv=json.loads((raw/launch).read_text())['argv'];assert argv[argv.index('--spec-type')+1]==('none' if label.startswith('A') else 'draft-mtp')
  rows=[json.loads(x) for x in (raw/name).read_text().splitlines() if x];cases=[x for x in rows if x.get('kind')=='agent_case'];turns={x['id']:x for x in rows if x.get('kind')=='agent_turn'};inputs={x['id']:x for x in rows if x.get('kind')=='input_identity'};assert len(cases)==8 and turns.keys()==inputs.keys()
  for t in turns.values():
   settings=t['reply']['__verbose']['generation_settings'];assert settings['seed']==1001 and settings['temperature']==0 and t['request']['cache_prompt'] is False
  for case in cases:entry=dict(case);entry['id']=label+'-'+case['id'];allcases.append(entry)
  data[label]=(cases,turns,inputs)
  computed.append({'arm':label,'task_successes':sum(x['reported_result']['task_success'] for x in cases),'policy_passes':sum(x['reported_result']['policy_gate_pass'] for x in cases),'denied_calls':sum(x['reported_result']['rejected_calls'] for x in cases),'model_requests':len(turns),'completion_tokens':sum(x['reply']['usage']['completion_tokens'] for x in turns.values()),'case_wall_s':sum(x['e2e_s'] for x in cases)})
  matches=list(pattern.finditer((raw/log).read_text(errors='replace')));observed=analysis['server_reported_mtp_counters'][label]
  if label.startswith('A'):assert not matches and observed['status']=='NOT_MEASURED'
  else:
   assert matches and observed['status']=='OBSERVED_SERVER_COUNTERS' and observed['log_records']==len(matches)
   counts=matches[-1].groups();assert tuple(int(x) for x in counts[:4])==tuple(observed[k] for k in ('generated_drafts','accepted_drafts','generated_draft_tokens','accepted_draft_tokens')) and float(counts[4])==observed['mean_accepted_length_reported']
   assert observed['accepted_draft_token_fraction']==int(counts[3])/int(counts[2])
 assert computed==a['arms']
 telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];assert counter_energy_bounds(telemetry,allcases,[x['id'] for x in allcases])==a['energy_counter']
 for arm in computed:
  label=arm['arm'];e=counter_energy_bounds(telemetry,allcases,[x['id'] for x in allcases if x['id'].startswith(label+'-')]);success=arm['task_successes'];e['gpu_j_per_success_lower']=e['lower_j']/success if success else None;e['gpu_j_per_success_upper']=e['upper_j']/success if success else None;assert e==analysis['per_arm_energy'][label]
 assert [(x['left'],x['right']) for x in analysis['paired']]==[('A1','A2'),('B1','B2'),('A1','B1'),('A2','B2')]
 for pair in analysis['paired']:
  ac,at,ai=data[pair['left']];bc,bt,bi=data[pair['right']];assert [x['id'] for x in ac]==[x['id'] for x in bc];loss=gain=ploss=pgain=0
  for x,y in zip(ac,bc):
   u,v=x['reported_result'],y['reported_result'];loss+=u['task_success'] and not v['task_success'];gain+=v['task_success'] and not u['task_success'];ploss+=u['policy_gate_pass'] and not v['policy_gate_pass'];pgain+=v['policy_gate_pass'] and not u['policy_gate_pass']
  matched=equal=0;first=[]
  for k in sorted(at.keys() & bt.keys()):
   x,y=at[k],bt[k]
   if x['request']!=y['request'] or ai[k]['prompt_token_ids']!=bi[k]['prompt_token_ids']:continue
   matched+=1;xx=x['reply']['__verbose']['tokens'];yy=y['reply']['__verbose']['tokens'];d=next((i for i,(u,v) in enumerate(zip(xx,yy)) if u!=v),None)
   if d is None and len(xx)!=len(yy):d=min(len(xx),len(yy))
   if d is None:equal+=1
   else:first.append(d)
  assert (loss,gain,ploss,pgain,matched,equal,sorted(first))==tuple(pair[k] for k in ('task_losses','task_gains','policy_losses','policy_gains','matched_requests_and_prompt_ids','identical_output_sequences','first_differences_0based'))
 tool=json.loads((stage/'TOOL_DELTA_REVIEW.json').read_text());timing=json.loads((stage/'CASE_TIMING_REVIEW.json').read_text());assert tool['audit_sha256']==timing['audit_sha256']==digest(file) and tool['replay_sha256']==timing['replay_sha256']==digest(stage/'INDEPENDENT_REVIEW.json')
 detailed=[]
 for left,right in (('A1','B1'),('A2','B2')):
  ac,at,ai=data[left];bc,bt,bi=data[right];ac={v['id']:v for v in ac};bc={v['id']:v for v in bc};changes=[]
  for k in sorted(at.keys() & bt.keys()):
   a1,b1=at[k],bt[k]
   if a1['request']!=b1['request'] or ai[k]['prompt_token_ids']!=bi[k]['prompt_token_ids'] or a1['reply']['__verbose']['tokens']==b1['reply']['__verbose']['tokens']:continue
   x,y=[v['reply']['choices'][0] for v in (a1,b1)];xm,ym=x['message'],y['message'];xc=xm.get('tool_calls') or [];yc=ym.get('tool_calls') or [];names=len(xc)==len(yc) and [z['function']['name'] for z in xc]==[z['function']['name'] for z in yc]
   try:arguments=len(xc)==len(yc) and [json.loads(z['function']['arguments']) for z in xc]==[json.loads(z['function']['arguments']) for z in yc]
   except (KeyError,TypeError,ValueError):arguments=None
   key=k.rsplit('--turn',1)[0];changes.append({'call_counts':[len(xc),len(yc)],'function_names_equal':names,'parsed_arguments_equal':arguments,'response_content_equal':xm.get('content')==ym.get('content'),'finish_reason_equal':x.get('finish_reason')==y.get('finish_reason'),'task_successes':[ac[key]['reported_result']['task_success'],bc[key]['reported_result']['task_success']],'policy_passes':[ac[key]['reported_result']['policy_gate_pass'],bc[key]['reported_result']['policy_gate_pass']]})
  detailed.append(changes)
 assert detailed[0]==detailed[1]==tool['results'] and len(detailed[0])==tool['matched_divergent_turns_per_pair']
 import statistics
 maps={k:{x['id']:x for x in data[k][0]} for k in labels};assert all(maps[k].keys()==maps['A1'].keys() for k in labels);delta=[]
 for key in maps['A1']:
  off=(maps['A1'][key]['e2e_s']+maps['A2'][key]['e2e_s'])/2;on=(maps['B1'][key]['e2e_s']+maps['B2'][key]['e2e_s'])/2;assert off>0 and on>0;delta.append((off-on,100*(off-on)/off))
 assert len(delta)==timing['cases']==8 and len({k.rsplit('-',1)[0] for k in maps['A1']})==timing['families']==8
 assert (sum(x>0 for x,y in delta),sum(x<0 for x,y in delta),sum(x==0 for x,y in delta))==(timing['mtp_faster_cases'],timing['mtp_slower_cases'],timing['ties'])
 assert (min(y for x,y in delta),statistics.median(y for x,y in delta),max(y for x,y in delta))==(timing['min_case_reduction_percent'],timing['median_case_reduction_percent'],timing['max_case_reduction_percent'])
 exact_path=stage/'EXACT_TRAJECTORY_REVIEW.json';exact=json.loads(exact_path.read_text())
 assert exact['status']=='EXACT_TRAJECTORY_POSTSELECTED_DIAGNOSTIC' and exact['audit_sha256']==digest(file) and exact['independent_review_sha256']==digest(stage/'INDEPENDENT_REVIEW.json') and exact['gpu_runs']==0
 matched=[]
 for case in maps['A1']:
  turns={k for k,v in data['A1'][2].items() if v['case_id']==case}
  same=bool(turns) and all({k for k,v in data[l][2].items() if v['case_id']==case}==turns for l in labels)
  for k in turns:
   if not same:break
   base=data['A1'][1][k];identity=data['A1'][2][k]
   same=all(data[l][1][k]['request']==base['request'] and data[l][2][k]['prompt_token_ids']==identity['prompt_token_ids'] and data[l][1][k]['reply']['__verbose']['tokens']==base['reply']['__verbose']['tokens'] for l in labels)
  if same:matched.append(case)
 assert len(matched)==exact['selected_cases']==7 and exact['excluded_cases']==1
 for label in labels:
  cases=[maps[label][k] for k in matched];e=counter_energy_bounds(telemetry,allcases,[label+'-'+k for k in matched]);x=exact['arms'][label]
  assert sum(c['reported_result']['task_success'] for c in cases)==x['successes']==5
  assert sum(c['reported_result']['policy_gate_pass'] for c in cases)==x['policy_passes']==7 and x['cases']==7
  assert sum(c['e2e_s'] for c in cases)==x['task_wall_s'] and e['groups']==x['counter_groups']
  assert e['lower_j']==x['gpu_energy_lower_j'] and e['upper_j']==x['gpu_energy_upper_j']
  assert e['lower_j']/5==x['gpu_j_per_success_lower'] and e['upper_j']/5==x['gpu_j_per_success_upper']
 assert exact['off_combined_s']==exact['arms']['A1']['task_wall_s']+exact['arms']['A2']['task_wall_s']
 assert exact['on_combined_s']==exact['arms']['B1']['task_wall_s']+exact['arms']['B2']['task_wall_s']
 assert exact['observed_reduction_pct']==100*(exact['off_combined_s']-exact['on_combined_s'])/exact['off_combined_s']
 off=computed[0]['case_wall_s']+computed[3]['case_wall_s'];on=computed[1]['case_wall_s']+computed[2]['case_wall_s']
 return {'exact_trajectory':{k:v for k,v in exact.items() if k not in ('audit_sha256','independent_review_sha256')},'exact_trajectory_review_sha256':digest(exact_path),'tool_delta':tool['results'],'tool_delta_review_sha256':digest(stage/'TOOL_DELTA_REVIEW.json'),'case_timing':{k:v for k,v in timing.items() if k not in ('audit_sha256','replay_sha256')},'case_timing_review_sha256':digest(stage/'CASE_TIMING_REVIEW.json'),'arms':computed,'pairs':analysis['paired'],'per_arm_energy':analysis['per_arm_energy'],'mtp_counters':analysis['server_reported_mtp_counters'],'off_total_case_s':off,'on_total_case_s':on,'observed_case_reduction_pct':(off-on)/off*100,'task_phase_s':a['task_phase_s'],'peak_vram_mib':a['peak_device_vram_mib'],'audit_sha256':digest(file),'review_sha256':digest(stage/'INDEPENDENT_REVIEW.json'),'analysis_sha256':digest(stage/'ANALYSIS.json'),'scope':analysis['scope'],'winner_qualified':False}

def r646_fresh_comparison(root):
 """Recompute two historical profiles on the same exposed 16 tasks."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r646';comparison_path=stage/'CROSS_MODEL_REVIEW.json'
 if not comparison_path.exists():return None
 review=json.loads(comparison_path.read_text());assert review['status']=='SAME_CASE_CROSS_MODEL_DIAGNOSTIC_ONLY' and review['gpu_runs']==0 and review['matched_tasks']==16
 data={}
 for n in (599,646):
  folder=root/f'staging/r{n}';audit_path=folder/'AUDIT.json';replay_path=folder/'INDEPENDENT_REVIEW.json';audit=json.loads(audit_path.read_text());replay=json.loads(replay_path.read_text());assert digest(audit_path)==review['audit_sha256'][f'R{n}'] and digest(replay_path)==review['independent_review_sha256'][f'R{n}'] and replay['audit_sha256']==digest(audit_path) and replay['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and not replay['changed_judgments'] and audit['measurement_valid'] and audit['GPU_execution_observed'] and not audit['official_benchmark'] and not audit['winner_qualified']
  raw=Path(audit['raw_root'])
  for name in ('HTTP_RESULTS.jsonl','GPU_TELEMETRY.jsonl'):assert digest(raw/name)==audit['original_raw_files_sha256'][name]
  rows=[json.loads(x) for x in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];rows=[x for x in rows if 'reply' in x and x.get('id','').startswith('lean-fresh-')];scores={x['id']:x for x in audit['scored_tasks']};telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];data[n]=(rows,scores,telemetry)
 ar,ascores,_=data[599];br,bscores,_=data[646];left={x['id'][:-3]:x for x in ar if x['id'].endswith('--A')};right={x['id']:x for x in br};assert len(left)==len(right)==16 and left.keys()==right.keys()
 assert all(left[k]['request']['messages']==right[k]['request']['messages'] and left[k]['request'].get('tools')==right[k]['request'].get('tools') for k in left)
 categories=[]
 for cat in ('coding','tools'):
  ids=[k for k in left if k.startswith('lean-fresh-'+('code' if cat=='coding' else 'tools')+'-')];assert len(ids)==8;qa=[ascores[k+'--A'] for k in ids];qb=[bscores[k] for k in ids];both=sum(x['success'] and y['success'] for x,y in zip(qa,qb));alone_a=sum(x['success'] and not y['success'] for x,y in zip(qa,qb));alone_b=sum(y['success'] and not x['success'] for x,y in zip(qa,qb));row={'category':cat,'both_pass':both,'omni_only_pass':alone_a,'qwen_only_pass':alone_b,'both_fail':8-both-alone_a-alone_b}
  for n,selected,scored in ((599,[k+'--A' for k in ids],qa),(646,ids,qb)):
   records,_,telemetry=data[n];e=counter_energy_bounds(telemetry,records,selected);success=sum(x['success'] for x in scored);row[f'R{n}']={'successes':success,'total':8,'request_wall_s':sum(x['e2e_s'] for x in scored),'completion_tokens':sum(x['completion_tokens'] for x in scored),'gpu_energy_lower_j':e['lower_j'],'gpu_energy_upper_j':e['upper_j'],'gpu_j_per_success_lower':e['lower_j']/success,'gpu_j_per_success_upper':e['upper_j']/success,'counter_groups':e['groups']}
  categories.append(row)
 assert categories==review['categories']
 return {'experiment_id':'R646','reference_experiment_id':'R599','matched_tasks':16,'categories':categories,'audit_sha256':review['audit_sha256'],'independent_review_sha256':review['independent_review_sha256'],'comparison_sha256':digest(comparison_path),'official_benchmark':False,'scope':review['scope']}

def r647_gemma_fresh_comparison(root):
 """Validate Gemma against the already audited R599/R646 task identities."""
 from leaderboard import counter_energy_bounds
 root=Path(root);stage=root/'staging/r647';path=stage/'CROSS_MODEL_REVIEW.json'
 if not path.exists():return None
 comparison=json.loads(path.read_text());assert comparison['status']=='SAME_TASK_EXPOSED_SUPPLEMENTAL_ONLY' and comparison['new_gpu_runs']==0 and comparison['matched_tasks']==16
 original=r646_fresh_comparison(root);assert original and original['matched_tasks']==16
 audits={};raws={};scores={}
 for ident in ('r599','r646','r647'):
  folder=root/'staging'/ident;ap=folder/'AUDIT.json';rp=folder/'INDEPENDENT_REVIEW.json';a=json.loads(ap.read_text());r=json.loads(rp.read_text())
  assert digest(ap)==comparison['audit_sha256'][ident] and digest(rp)==comparison['independent_review_sha256'][ident] and r['audit_sha256']==digest(ap) and r['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and not r['changed_judgments']
  assert a['measurement_valid'] and a['GPU_execution_observed'] and not a['official_benchmark'] and not a['winner_qualified']
  raw=Path(a['raw_root']);assert digest(raw/'HTTP_RESULTS.jsonl')==a['original_raw_files_sha256']['HTTP_RESULTS.jsonl'] and digest(raw/'GPU_TELEMETRY.jsonl')==a['original_raw_files_sha256']['GPU_TELEMETRY.jsonl']
  rows=[json.loads(x) for x in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];rows=[x for x in rows if 'reply' in x and x.get('id','').startswith('lean-fresh-')];rows=[x for x in rows if x['id'].endswith('--A')] if ident=='r599' else rows
  raws[ident]={x['id'].removesuffix('--A'):x for x in rows};ss=[x for x in a['scored_tasks'] if x['arm']=='A'] if ident=='r599' else a['scored_tasks'];scores[ident]={x['id'].removesuffix('--A'):x for x in ss};audits[ident]=a
  assert len(raws[ident])==len(scores[ident])==16
 assert raws['r599'].keys()==raws['r646'].keys()==raws['r647'].keys()
 for k in raws['r647']:
  assert all(raws[n][k]['request']['messages']==raws['r647'][k]['request']['messages'] and raws[n][k]['request'].get('tools')==raws['r647'][k]['request'].get('tools') for n in ('r599','r646'))
 categories={}
 for cat in ('coding','tools'):
  ids=[k for k,v in scores['r647'].items() if v['category']==cat];assert len(ids)==8
  categories[cat]={n:{'successes':sum(scores[n][k]['success'] for k in ids),'total':8} for n in scores}
  categories[cat]['paired_qwen_gemma']={'both_pass':sum(scores['r646'][k]['success'] and scores['r647'][k]['success'] for k in ids),'qwen_only':sum(scores['r646'][k]['success'] and not scores['r647'][k]['success'] for k in ids),'gemma_only':sum(not scores['r646'][k]['success'] and scores['r647'][k]['success'] for k in ids),'both_fail':sum(not scores['r646'][k]['success'] and not scores['r647'][k]['success'] for k in ids)}
 assert categories==comparison['categories']
 a=audits['r647'];raw=Path(a['raw_root']);telemetry=[json.loads(x) for x in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()];records=list(raws['r647'].values());groups={}
 for cat in ('coding','tools'):
  selected=[x for x in a['scored_tasks'] if x['category']==cat];ids=[x['id'] for x in selected];energy=counter_energy_bounds(telemetry,records,ids);success=sum(x['success'] for x in selected)
  assert energy==a['groups'][cat]['GPU_counter'] and success==a['groups'][cat]['successes']
  groups[cat]={'successes':success,'total':len(ids),'request_wall_s':sum(x['e2e_s'] for x in selected),'completion_tokens':sum(x['completion_tokens'] for x in selected),'gpu_j_per_success_lower':energy['lower_j']/success if success else None,'gpu_j_per_success_upper':energy['upper_j']/success if success else None}
 return {'experiment_id':'R647','matched_tasks':16,'categories':categories,'groups':groups,'task_phase_s':a['task_phase_s'],'peak_vram_mib':a['peak_device_vram_mib'],'audit_sha256':comparison['audit_sha256'],'comparison_sha256':digest(path),'official_benchmark':False,'scope':comparison['scope']}

def reserved_family_sign_flip(group_differences):
 """Exact paired family sign enumeration; not an independence/equivalence claim."""
 import itertools
 if not group_differences:raise ValueError('No paired families')
 observed=abs(sum(group_differences)); totals=[abs(sum(sign*value for sign,value in zip(signs,group_differences))) for signs in itertools.product((-1,1),repeat=len(group_differences))]
 return sum(v>=observed for v in totals)/len(totals)

def reserved_agent_comparison(root):
 """Replay-bound pairs of original reserved agent results, grouped by task family."""
 root=Path(root); ids=('r589','r590','r591','r618','r625');data={};scorers=set()
 if not all((root/'staging'/i/'AUDIT.json').is_file() for i in ids):return None
 for ident in ids:
  stage=root/'staging'/ident;file=stage/'AUDIT.json';a=json.loads(file.read_text());reviewfile=stage/'INDEPENDENT_REVIEW.json';r=json.loads(reviewfile.read_text())
  assert a['measurement_valid'] and a['GPU_execution_observed'] and a['tasks']==33 and a['dataset_id']=='jarvis-lean-holdout-20261027-v1' and not a['official_benchmark']
  assert a['independent_review_sha256']==digest(reviewfile) and r['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and r['result']['cases']==33 and r['result']['complete'] and r['result']['all_scores_and_effects_reproduced'] and r['GPU_runs']==0 and r['model_requests']==0
  scorers.add(r['scorer_sha256']);raw=Path(a['raw_root']);source=raw/'HTTP_RESULTS.jsonl';assert digest(source)==a['original_raw_files_sha256']['HTTP_RESULTS.jsonl']
  profile=raw/'profile.json';assert digest(profile)==a['profile_sha256']==a['original_raw_files_sha256']['profile.json'] and json.loads(profile.read_text())['model_sha256']==a['model_sha256']
  rows=[json.loads(line) for line in source.read_text().splitlines() if line];cases=[x for x in rows if x.get('kind')=='agent_case'];assert len(cases)==33
  byid={x['id']:x['reported_result'] for x in cases};assert len(byid)==33 and sum(x['task_success'] for x in byid.values())==a['solved']
  checks=r['result']['checks'];assert len(checks)==33 and {x['id'] for x in checks}==set(byid) and all(x['score_and_effects_reproduced'] and x['task_success']==byid[x['id']]['task_success'] for x in checks)
  data[ident]={'audit':a,'cases':byid,'audit_sha256':digest(file),'replay_sha256':digest(reviewfile),'raw_sha256':digest(source)}
 assert len(scorers)==1 and all(set(x['cases'])==set(data['r589']['cases']) for x in data.values())
 families={k:k.rsplit('-',1)[0] for k in data['r589']['cases']};assert len(set(families.values()))==11 and all(list(families.values()).count(f)==3 for f in set(families.values()))
 profiles=[]
 for ident in ids:
  x=data[ident];a=x['audit'];energy=a.get('GPU_counter',{});profiles.append({'experiment_id':ident.upper(),'model':a['model'],'model_sha256':a['model_sha256'],'solved':a['solved'],'policy_passes':sum(v['policy_gate_pass'] for v in x['cases'].values()),'task_phase_s':a['task_phase_s'],'peak_vram_mib':a['peak_device_vram_mib'],'gpu_energy_lower_j':energy.get('lower_j'),'gpu_energy_upper_j':energy.get('upper_j'),'audit_sha256':x['audit_sha256'],'replay_sha256':x['replay_sha256'],'raw_sha256':x['raw_sha256']})
 pairs=[]
 for left,right in (('r589','r590'),('r589','r591'),('r589','r618'),('r618','r625')):
  a,b=data[left]['cases'],data[right]['cases'];metrics={}
  for key in ('task_success','policy_gate_pass'):
   diffs={f:sum(int(a[k][key])-int(b[k][key]) for k in a if families[k]==f) for f in set(families.values())};ao=sum(a[k][key] and not b[k][key] for k in a);bo=sum(b[k][key] and not a[k][key] for k in a)
   metrics[key]={'left_only':ao,'right_only':bo,'net_left_minus_right':ao-bo,'families_left_ahead':sum(v>0 for v in diffs.values()),'families_right_ahead':sum(v<0 for v in diffs.values()),'families_tied':sum(v==0 for v in diffs.values()),'family_sign_flip_two_sided_p':reserved_family_sign_flip(list(diffs.values()))}
  pairs.append({'left':left.upper(),'right':right.upper(),'metrics':metrics})
 return {'dataset_id':'jarvis-lean-holdout-20261027-v1','tasks':33,'families':11,'scorer_sha256':next(iter(scorers)),'profiles':profiles,'pairs':pairs,'official_benchmark':False,'scope':'Previously reserved instances from 11 authored related families, historical non-concurrent whole-profile comparisons, one generation per model. Exact family sign-flip is exploratory and assumes exchangeable/symmetric paired family effects; no population independence, causality, equivalence, official benchmark, seed variability or Champion qualification. Shared GPU energy includes group idle; not CPU/system energy.'}

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
 on_aa=qwen_native_aa(root,'R618','R635');off_aa=qwen_native_aa(root,'R625','R636')
 return {'source_review_sha256':digest(report),'timing_review_sha256':digest(fixed) if fixed.exists() else None,'source_commit':data['build_source']['commit'],'profiles':profiles,'paired_historical':pairs,'agent_task_pairs':agent_task_pairs(root),'fixed_output_timings':timings,'seed_execution_path':seed_execution_path(data,captures,root),'logprobs_diagnostic_path':logprobs_diagnostic_path(data,captures),'cache_state_source_path':cache_state_source_path(root),'r630_native_aa':r630_native_aa(root),'r631_native_aa':r631_native_aa(root),'r633_native_aa':r633_native_aa(root),'r635_native_aa':on_aa,'r636_native_aa':off_aa,'qwen_mtp_cross_review':qwen_mtp_cross_review(root,on_aa,off_aa),'r634_seed_pilot':r634_seed_pilot(root),'r637_balanced_mtp':r637_balanced_mtp(root),'r639_policy_replay':r639_policy_replay(root),'r640_policy_abba':r640_policy_abba(root),'r641_policy_abba':r641_policy_abba(root),'r642_policy_abba':r642_policy_abba(root),'reserved_agent_comparison':reserved_agent_comparison(root),'r643_mtp_agent_abba':r643_mtp_agent_abba(root),'r646_fresh_comparison':r646_fresh_comparison(root),'r647_gemma_fresh_comparison':r647_gemma_fresh_comparison(root),'scope':'Different sessions; observed divergence cannot establish causation or equivalence. Archived request and server-reported settings are not direct internal RNG-state observations. No new GPU run during export.'}
