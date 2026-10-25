"""Positive-list projection of frozen development screening; never leaderboard runs."""
import hashlib,json,math,re
from pathlib import Path
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def wilson(k,n):
 if not n:return None
 z=1.959963984540054;d=1+z*z/n;c=(k/n+z*z/(2*n))/d;r=z*math.sqrt(k/n*(1-k/n)/n+z*z/(4*n*n))/d
 return [max(0,c-r),min(1,c+r)]
def project_group(g):
 fields=('completed','successes','final_text_present','valid_terminal_output','length_stops','completed_request_wall_s','completion_tokens','tokens_s_completed_requests','successful_tasks_s_completed_requests','GPU_j_per_success_lower','GPU_j_per_success_upper')
 result={k:g.get(k) for k in fields};result['wilson95']=wilson(g['successes'],g['completed']);counter=g.get('GPU_counter') or {};result['gpu_energy_j_lower']=counter.get('lower_j');result['gpu_energy_j_upper']=counter.get('upper_j');return result

def captured_screen_profile(profile,entry,package):
 """Project actual first-screen launch without creating any official history run."""
 import leaderboard
 from export import text as sanitize
 raw=Path(entry['parent_capture']);launch=read(raw/'LAUNCH.json');identity=package['identity'];assets=dict(profile['assets']);options=profile['native_recipe']['request_options']
 assets['/models/target.gguf']=profile['model_sha256'];assets['/engine/llama-server']=assets[profile['runtime']+'/llama-server'];assets['/harness/chat_template.jinja']=assets[profile['chat_template']]
 for path,h in profile['assets'].items():
  if path.startswith(profile['runtime']+'/'):assets['/engine/'+Path(path).name]=h
 pseudo={'runtime_identities':assets,'model_profile':identity['name'],'maximum_output_tokens':options['max_tokens'],'maximum_device_vram_mib':14336,'maximum_model_seconds':1200,'power_limit_w':300}
 metadata={'model_sha256':profile['model_sha256'],'engine_binary_sha256':assets['/engine/llama-server'],'output_cap':options['max_tokens'],'sampling':{k:v for k,v in options.items() if k in ('temperature','top_p','top_k','min_p','presence_penalty','repeat_penalty','seed')},'chat_template_kwargs':options.get('chat_template_kwargs'),'template_sha256':assets[profile['chat_template']],'power_limit_w':300}
 cfg=leaderboard.profile(pseudo,launch,identity['family_id'],identity['name'],identity['quantization'],entry['parent_experiment_id'],H(raw/'CONTRACT.json'),sanitize,metadata,origin={'repository':identity['hf_repository'],'revision':identity['hf_revision']})
 cfg['model'].update(architecture=identity['architecture'],parameters_in_GGUF=identity['parameters_in_GGUF']);cfg['model_artifact_id']='artifact-'+leaderboard.H(cfg['model']);cfg['engine']['build_id']=Path(profile['runtime']).parent.name
 cfg['runtime'].update(benchmark_task_limit_s=1200,timing_scope='DEVELOPMENT_SCREEN_TASK_PHASE_ONLY',startup_limit_s=180,GPU_wrapper_limit_s=1440,CPU_scoring_limit_s=120,native_HTTP_timeout_policy=profile['native_recipe']['http_timeout_policy'])
 cfg['source_provenance']={'kind':'BROKER_NATIVE_CAPTURED_CONFIGURATION','evidence_scope':'FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY','frozen_model_profile_sha256':leaderboard.H({k:v for k,v in profile.items() if k!='selected_task_inputs'}),'model_source_package_sha256':entry['first_model_source_review']['sha256'],'actual_profile_sha256':H(raw/'profile.json'),'actual_launch_sha256':H(raw/'LAUNCH.json')};cfg['runtime_configuration_id']='cfg-'+leaderboard.H({k:v for k,v in cfg.items() if k!='runtime_configuration_id'})
 leaderboard.verify_broker_capture(cfg,profile,launch);leaderboard.validate_history({'profiles':[cfg],'runs':[],'attempts':[]},{})
 return cfg

def same_validation_inference(actual,parent):
 """Only validation collection size/preflight may differ from the executed parent."""
 if any(actual.get(k)!=parent.get(k) for k in ('assets','model','runtime','chat_template','adapter')):return False
 ignored={'maximum_tasks','maximum_generation_requests','preflight_all_inputs'}
 recipe=lambda p:{k:v for k,v in p['native_recipe'].items() if k not in ignored}
 return recipe(actual)==recipe(parent)

def same_native_inference(actual,screen,discipline):
 """Only the reviewed native auto/parallel tool envelope is category-specific."""
 if actual['assets']!=screen['assets']:return False
 keys=('argv_tail','context','environment','http_timeout_policy','warmups')
 if any(actual['native_recipe'].get(k)!=screen['native_recipe'].get(k) for k in keys):return False
 observed=dict(actual['native_recipe']['request_options']);expected=dict(screen['native_recipe']['request_options'])
 if discipline=='tools' and actual.get('adapter')=='llama-native-tools':
  if observed.pop('tool_choice',None)!='auto' or observed.pop('parallel_tool_calls',None) is not True:return False
  # A screening parent may itself already be a native-tools profile.
  if 'tool_choice' in expected or 'parallel_tool_calls' in expected:
   if expected.pop('tool_choice',None)!='auto' or expected.pop('parallel_tool_calls',None) is not True:return False
 return observed==expected

def matching_full_runs(root,history,profiles,profile,sha):
 """Link only full local runs with the same captured artifact and native options."""
 matches=[]
 for run in history['runs']:
  cfg=profiles[run['runtime_configuration_id']]
  if not run.get('official_eligible') or cfg['model']['artifact_sha256']!=sha or cfg['runtime'].get('power_limit_w')!=300:continue
  audit=Path(root)/'staging'/run['experiment_id'].lower()/'AUDIT.json'
  if not audit.exists() or H(audit)!=run['audit_hash']:continue
  original=read(audit)
  for part in original.get('parts',[]):
   path=Path(part['audit_path'])
   assert H(path)==part['audit_sha256']
   actual=read(path.parent/'profile.json')
   if same_native_inference(actual,profile,run['discipline']):
    matches.append({k:run[k] for k in ('experiment_id','benchmark_identity_id','runtime_configuration_id','audit_hash','official_eligible')});break
 return matches

def qualification_decisions(root,phase,measured):
 """Project an audit-bound research decision, never a new benchmark result."""
 descriptor=phase.get('decision_review')
 if not descriptor:return None
 path=Path(descriptor['path']);assert H(path)==descriptor['sha256'];review=read(path)
 assert review['schema']==1 and review['official_benchmark'] is False and review['winner_qualified'] is False and review['population_ranking'] is False
 assert review['dataset_id']=='jarvis-agent-validation-20261025-v1'
 assert review['dataset_sha256']==phase['frozen_agent_validation']['private_dataset_sha256']
 assert review['authored_groups']==11 and review['cases_per_profile']==33 and review['new_GPU_runs']==0
 actual={r['experiment_id']:r for r in measured};rows=review['profiles']
 assert len(actual)==len(measured)==review['model_profiles']==len(rows)
 assert {r['experiment_id'] for r in rows}==set(actual)
 projected=[]
 for r in rows:
  eid=r['experiment_id'];assert re.fullmatch(r'R[1-9][0-9]*',eid)
  observed=actual[eid];m=observed['metrics']
  assert r['model']==observed['model'] and r['audit_sha256']==observed['audit_sha256']
  for key in ('solved','tasks','task_phase_s','peak_device_vram_mib','gpu_j_per_success_lower','gpu_j_per_success_upper'):assert r[key]==m[key]
  folder=Path(root)/'staging'/eid.lower();quality=folder/'QUALITY_REVIEW.json';independent=folder/'INDEPENDENT_REVIEW.json'
  assert H(quality)==r['quality_review_sha256'] and H(independent)==r['independent_review_sha256']
  q=read(quality);i=read(independent)
  assert q['source_audit_sha256']==r['audit_sha256'] and q['tasks']==33 and q['solved']==r['solved']
  assert i['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and i['result']['all_scores_and_effects_reproduced'] is True
  for key in ('policy_gate_passes','task_scope_passes'):
   assert type(r[key]) is int and 0<=r[key]<=33 and r[key]==q['quality'][key]
  assert r['decision'].startswith(('RETAIN_','PRIORITIZE_'))
  projected.append({k:r[k] for k in ('experiment_id','model','decision','reason','optimization_after_qualification','policy_gate_passes','task_scope_passes')})
 return {'review_sha256':descriptor['sha256'],'profiles':projected,'scope':review['review_scope'],'next_decisions':review['next_decisions'],'official_benchmark':False,'winner_qualified':False}

def qualification_phase(root,history):
 """Allowlisted current qualification evidence; never a new benchmark score."""
 phase=read(root/'BENCHMARK_REFERENCES.json')['summary'].get('jarvis_qualification_phase')
 if not phase:return None
 candidates=[]
 for c in phase['candidates']:
  recorded=[{k:r[k] for k in ('experiment_id','discipline','benchmark_id','benchmark_identity_id','runtime_configuration_id','solved','tasks','official_eligible','status','audit_hash')} for r in history['runs'] if r['experiment_id'] in c['source_experiments']]
  assert recorded==c['full_benchmark_records']
  candidates.append({k:c[k] for k in ('profile','source_experiments','full_benchmark_records','agent_development_experiment','reserved_validation_experiment','qualification_status','official_agents','optimization_after_qualification')})
 frozen=phase['frozen_agent_validation']
 for path,key in [('plan_path','plan_sha256'),('private_dataset_path','private_dataset_sha256'),('CPU_QA_path','CPU_QA_sha256')]:assert H(frozen[path])==frozen[key]
 qa=read(frozen['CPU_QA_path']);folder=Path(frozen['CPU_QA_path']).parent
 receipt=folder/'jarvis-validation33-freeze.receipt.json';assert H(receipt)==qa['CPU_receipt_sha256']
 control=read(receipt);assert control['returncode']==0 and 'Result=success\n' in control['properties'] and 'ExecMainStatus=0\n' in control['properties']
 observed=[json.loads(l.split(' ',1)[1]) for l in (folder/'jarvis-validation33-freeze.stdout').read_text().splitlines() if l.startswith('FROZEN_VALIDATION_QA_JSON ')]
 assert len(observed)==1 and all(qa[k]==v for k,v in observed[0].items())
 assert qa['passed'] and qa['real_uid']!=0 and qa['model_requests']==qa['GPU_calls']==qa['production_tool_actions']==0 and not qa['models_released']
 assert qa['cases']==qa['golden_passed']==qa['wrong_final_rejected']==qa['forbidden_action_rejected']==frozen['cases']
 assert qa['groups']==frozen['generalization_groups'] and qa['private_dataset_file_sha256']==frozen['private_dataset_sha256']
 assert H(folder/'generate_validation.py')==qa['generator_source_sha256']
 assert control['input_sha256'][str(folder/'generate_validation.py')]==qa['generator_source_sha256']
 tf=phase['terminal_bench_feasibility'];assert H(tf['path'])==tf['sha256'];tb=read(tf['path'])
 assert tb['model_requests']==tb['GPU_runs']==0 and tb['official_scorer_admitted'] is False
 ctx=phase['gemma_context_failure'];ap=root/'staging'/ctx['experiment_id'].lower()/'AUDIT.json';assert H(ap)==ctx['audit_sha256'];a=read(ap)
 assert not a['measurement_valid'] and a['actual_generation_requests']==a['tasks']==0 and a['solved'] is None
 assert H(ctx['CPU_candidate_fix_path'])==ctx['CPU_candidate_fix_sha256'];fix=read(ctx['CPU_candidate_fix_path']);assert fix['GPU_calls']==fix['model_requests']==0
 sl=phase['slopus_diagnosis'];assert H(sl['quality_review_path'])==sl['quality_review_sha256'];sq=read(sl['quality_review_path'])
 assert sl['recorded_policy_violations']==sq['failure_reasons']['policy_violations'] and sl['length_stopped_responses']==sq['quality']['length_stopped_responses']
 correction=None
 if ctx.get('corrective_experiment'):
  ca=root/'staging'/ctx['corrective_experiment'].lower()/'AUDIT.json';assert H(ca)==ctx['corrective_audit_sha256'];actual=read(ca)
  cr=Path(ctx['corrective_context_review_path']);assert H(cr)==ctx['corrective_context_review_sha256'];review=read(cr)
  assert review['source_audit_sha256']==H(ca) and actual['measurement_valid'] and actual['tasks']==18
  comparison=read(ca.parent/'COMPARISON_REVIEW.json');assert comparison['candidate_audit_sha256']==H(ca)
  correction={'experiment_id':ctx['corrective_experiment'],'tasks':actual['tasks'],'solved':actual['solved'],'reference_solved':review['quality']['reference_solved'],'context_preflight_errors':actual['technical_preflight_cases'],'HTTP_errors':actual['technical_request_errors'],'task_phase_s':actual['task_phase_s'],'task_phase_change_percent':comparison['comparison']['task_phase_change_percent'],'peak_vram_change_mib':comparison['comparison']['peak_vram_change_mib'],'identical_first_turn_prompt_hashes':review['identical_first_turn_prompt_token_hashes'],'official_benchmark':False,'winner_qualified':False}
  reference_path=root/'staging'/review['reference_experiment_id'].lower()/'AUDIT.json';assert H(reference_path)==review['reference_audit_sha256'];reference=read(reference_path)
  correction.update(model_requests=actual['actual_generation_requests'],reference_model_requests=reference['actual_generation_requests'])
 model_validation=[]
 from export import verified_native_agent_development
 for key,summary in read(root/'BENCHMARK_REFERENCES.json')['summary'].items():
  if not isinstance(summary,dict) or summary.get('status')!='VALIDATION33_COMPLETE':continue
  ap=Path(summary['audit_path']);assert H(ap)==summary['audit_sha256'];actual=read(ap)
  assert actual['dataset_id']=='jarvis-agent-validation-20261025-v1' and actual['tasks']==33 and actual['measurement_valid']
  metric=verified_native_agent_development(root,summary,lambda path,expected:'audit-'+expected[:20])
  model_validation.append({'experiment_id':actual['experiment_id'],'model':actual['model'],'audit_sha256':H(ap),'metrics':metric})
 multi=phase['multi_agent_plan'];assert multi['total_task_budget_s']==1200 and multi['per_arm_task_budget_s']*len(multi['arms'])==1200 and multi['GPU_concurrency']==1
 return {'status':phase['status'],'selection_scope':phase['selection_scope'],'candidates':candidates,'model_validation':model_validation,'decision_review':qualification_decisions(root,phase,model_validation),'validation_execution':({k:frozen['current_execution'][k] for k in ('experiment_id','status')} if frozen.get('current_execution') else None),
  'validation':{'status':'FROZEN_NOT_RELEASED_NO_MODEL_RESULTS','cases':qa['cases'],'generalization_groups':qa['groups'],'golden_QA_passed':qa['golden_passed'],'wrong_final_QA_rejected':qa['wrong_final_rejected'],'forbidden_action_QA_rejected':qa['forbidden_action_rejected'],'model_requests':0,'CPU_QA_sha256':frozen['CPU_QA_sha256'],'private_dataset_sha256':frozen['private_dataset_sha256'],'scope':frozen['scope']},
  'terminal_bench':{'status':tb['status'],'tasks':tb['task_count'],'revision':tb['dataset_revision'],'evaluator_version':tb['candidate_evaluator']['version'],'official_complete_local_result':'NOT MEASURED','sources':tb['sources'],'blockers':['Reviewed local container backend and Harbor are not installed.','Task environments, evaluator dependencies and shared1200s broker route are not admitted.']},
  'slopus_diagnosis':{k:sl[k] for k in ('experiment_id','recorded_policy_violations','length_stopped_responses','actual_effect_scope_passes','scope')},
  'gemma_context':{'experiment_id':ctx['experiment_id'],'status':a['status'],'model_requests':0,'quality_score':None,'CPU_fix_tests':fix['tests'],'GPU_retry_admitted':ctx['new_transport_GPU_admitted'],'corrective_result':correction},
  'multi_agent_plan':{k:multi[k] for k in ('status','arms','total_task_budget_s','per_arm_task_budget_s','GPU_concurrency','task_coverage')}}

def build(root):
 root=Path(root);base=root/'staging/model-comparison-preparation/model-screening';holdout=read(base/'VALIDATION_FROZEN_MANIFEST.json')
 assert all(H(base/k)==v for k,v in holdout['files'].items())
 inventory=read(base/'MODEL_INVENTORY.json');protocol=read(base/'PROTOCOL.json');rows=[]
 history=read(Path(__file__).resolve().parents[1]/'data/configuration-history.json');profiles={p['runtime_configuration_id']:p for p in history['profiles']}
 for entry in inventory['models']:
  package=None
  if entry.get('first_model_source_review'):
   descriptor=entry['first_model_source_review'];assert H(descriptor['file'])==descriptor['sha256'];package=read(descriptor['file'])
  profile=package['profile'] if package and not entry.get('screening_results') else read(Path(entry['parent_capture'])/'profile.json');recipe=profile['native_recipe'];sha=profile.get('model_sha256') or profile['assets'][profile['model']]
  assert sha==entry['model_sha256']
  cfg={'parent_profile_id':entry['parent_profile'],'model_sha256':sha,'request_options':{k:v for k,v in recipe['request_options'].items() if k in ('chat_template_kwargs','temperature','seed','max_tokens','top_p','top_k','min_p','repeat_penalty','presence_penalty','reasoning_effort','cache_prompt')},'context':recipe['context'],'engine':'llama.cpp native','engine_version':None,'binary_identities':{Path(k).name:v for k,v in profile['assets'].items() if Path(k).name in ('llama-server','libggml-cuda.so','libggml-cuda.so.0','libggml-cuda.so.0.21.0')},'warmup_requests':len(recipe['warmups']),'task_time_policy':profile.get('task_time_policy'),'hardware':'Tesla V100 SXM2 16 GB','power_w':300}
  matches=[] if package else [r for r in history['runs'] if r['experiment_id']==entry['parent_experiment_id']]
  if matches:
   recorded=profiles[matches[0]['runtime_configuration_id']]
   assert recorded['model']['artifact_sha256']==sha
   cfg['recorded_parent_profile']=recorded
   cfg['quantization']=recorded['model']['quantization']
  if package:
   cfg['quantization']=package['identity']['quantization'];cfg['model_source']={k:package['identity'][k] for k in ('hf_repository','hf_revision','base_repository','base_revision','license','quantizer','parameters_in_GGUF')}
   cfg['binary_identities'].update({Path(k).name:v for k,v in profile['assets'].items() if Path(k).name.startswith('libggml-cuda.so')})
   if entry.get('screening_results'):cfg['recorded_native_profile']=captured_screen_profile(profile,entry,package)
  identity={k:v for k,v in cfg.items() if k not in ('recorded_parent_profile','recorded_native_profile')}
  cfg['screening_configuration_id']='screening-config-'+hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  row={'model':entry['model'],'configuration':cfg,'status':entry['status'],'local_artifact_available':entry['local_artifact_available'],'parent_experiment_id':entry['parent_experiment_id'],'results':None,'audit_sha256':None,'experiment_id':None,'conditions':'Single native-profile session; frozen base-task order','decision':'No quality exclusion from16 tasks; retain for review.','independent_review_sha256':None}
  if package:row['full_benchmark_status']='NOT MEASURED';row['decision']='First native source-reviewed screening only. No full result inherited from the engine reference; retain without small-sample quality rejection.'
  if package and package['source_review'].get('provenance_limits'):row['source_provenance_limits']=package['source_review']['provenance_limits']
  results=entry.get('screening_results',[])
  if results:
   item=results[-1];a=read(item['audit_path']);review=read(item['independent_review_path'])
   assert H(item['audit_path'])==item['audit_sha256'] and H(item['independent_review_path'])==item['independent_review_sha256']
   assert review['audit_sha256']==item['audit_sha256'] and review['changed_judgments']==[] and review['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL'
   assert a['measurement_valid'] and a['GPU_execution_observed'] and a['official_benchmark'] is False
   assert len(review['replay'])==a['completed_requests']==len(a['scored_tasks'])
   assert [(x['id'],x['success']) for x in review['replay']]==[(x['id'],x['success']) for x in a['scored_tasks']]
   assert len({x['id'] for x in a['scored_tasks']})==len(a['scored_tasks'])
   for cat in ('coding','tools'):
    tasks=[x for x in a['scored_tasks'] if x['category']==cat];g=a['groups'][cat]
    assert len(tasks)==g['completed'] and sum(x['success'] for x in tasks)==g['successes']
   raw=Path(a['raw_root']);assert all(H(raw/k)==v for k,v in a['original_raw_files_sha256'].items())
   actual=read(raw/'profile.json');assert (actual.get('model_sha256') or actual['assets'][actual['model']])==sha
   assert actual['native_recipe']['request_options']==recipe['request_options']
   row.update(results={k:project_group(v) for k,v in a['groups'].items()},audit_sha256=item['audit_sha256'],independent_review_sha256=item['independent_review_sha256'],experiment_id=item['experiment_id'],task_phase_s=a['task_phase_s'],peak_vram_mib=a['peak_device_vram_mib'],date=a['at_utc'],timeouts=a['timeouts'])
  elif entry['model']=='Nexus-9B':
   ap=root/'staging/r487/AUDIT.json';rp=root/'staging/r487/INDEPENDENT_REVIEW.json';a=read(ap);r=read(rp)
   assert r['audit_sha256']==H(ap) and not r['changed_judgments'] and a['complete_ABC_task_triples']==32
   assert all(a['matched_arms_by_category']['A'][cat]['completed']==16 for cat in ('coding','tools'))
   row.update(status='SCREENING VOLLSTÄNDIG',experiment_id='R487',audit_sha256=H(ap),independent_review_sha256=H(rp),results={k:project_group(v) for k,v in a['matched_arms_by_category']['A'].items()},peak_vram_mib=a['peak_device_vram_mib'],date=a['at_utc'],task_phase_s=None,timeouts=0,conditions='Reused native A arm; interleaved ABC schedule. Same tasks/scorer and native sampler; timing is historical, not matched standalone performance evidence.')
  if package and results:
   source=read(root/'BENCHMARK_REFERENCES.json')['summary'][row['experiment_id'].lower()]
   if source.get('comparison_review_path'):
    assert H(source['comparison_review_path'])==source['comparison_review_sha256'];review=read(source['comparison_review_path']);assert review['candidate_audit_sha256']==row['audit_sha256'] and review['all32_actual_requests_identical'] is True and review['winner_qualified'] is False and review['official_benchmark'] is False
    row.update(selection_status='VERTIEFUNG EMPFOHLEN',decision=review['decision'],comparison_audit_sha256=source['comparison_review_sha256'],comparison_summary=review['metrics'])
   if source.get('cpu_diagnosis_path'):
    assert H(source['cpu_diagnosis_path'])==source['cpu_diagnosis_sha256'];diagnosis=read(source['cpu_diagnosis_path']);assert diagnosis['source_audit_sha256']==row['audit_sha256'] and diagnosis['GPU_runs']==0
    row.update(selection_status='WEITERE DIAGNOSE',decision=diagnosis['decision'],diagnostic_audit_sha256=source['cpu_diagnosis_sha256'],diagnostic_summary=diagnosis['coding'])
  full=matching_full_runs(root,history,profiles,profile,sha)
  row['full_benchmark_runs']=full
  row['full_benchmark_status']='MATCHED_FULL_LOCAL_RESULTS' if full else 'NOT MEASURED'
  rows.append(row)
 output={'schema':1,'official_benchmark':False,'dataset_id':protocol['dataset_id'],'tasks_per_category':16,'source_tasks_sha256':protocol['source_tasks_sha256'],'source_oracles_sha256':protocol['source_oracles_sha256'],'protocol_sha256':H(base/'PROTOCOL.json'),'data_role':'DEVELOPMENT_ALREADY_USED_FOR_NEXUS_VARIANT_SELECTION','holdout':{'status':read(base/'VALIDATION_FROZEN_MANIFEST.json')['status'],'coding':8,'mock_tools':8,'manifest_sha256':H(base/'VALIDATION_FROZEN_MANIFEST.json'),'scope':'Reserved unexecuted authored tasks, not broker-admitted. No independent-population guarantee; no official benchmark claim.'},'selection':'No automatic quality rejection. Small differences retain both candidates; technical failures require diagnosis. Reuse matching full benchmarks.','rows':rows}
 extras=[]
 for x in inventory.get('other_local_artifacts',[]):
  assert re.fullmatch(r'[A-Za-z0-9_.-]{1,120}\.gguf',x['artifact'])
  item={k:x[k] for k in ('artifact','status','reason')}
  if x.get('audit_sha256'):
   assert H(x['audit_path'])==x['audit_sha256'] and re.fullmatch('[a-f0-9]{64}',x['audit_sha256']);item.update(audit_sha256=x['audit_sha256'],audit_id='audit-'+x['audit_sha256'][:20],experimentally_screened=x['experimentally_screened'])
  extras.append(item)
 output['other_local_artifacts']=extras
 plan=read(base/'QUALIFICATION_SELECTION_PLAN.json')
 output['qualification_plan']={k:plan[k] for k in ('rule','priorities','agents')}
 output['qualification_plan']['holdout_at_plan_creation']=plan['holdout']
 output['qualification_plan']['created_at_utc']=plan['at_utc']
 output['qualification_plan_sha256']=H(base/'QUALIFICATION_SELECTION_PLAN.json')
 validation_dir=base.parent/'independent-validation16'
 if (validation_dir/'PLAN.json').exists():
  vp=read(validation_dir/'PLAN.json');vr=[];specs=list(vp['profiles'])
  extra_path=validation_dir/'ADDITIONAL_PROFILES_PLAN.json'
  if extra_path.exists():
   extra=read(extra_path)
   assert extra['original_plan_sha256']==H(validation_dir/'PLAN.json')
   assert extra['original_cohort_sha256']==H(validation_dir/'COHORT_REVIEW.json')
   assert extra['frozen_validation_manifest_sha256']==H(base/'VALIDATION_FROZEN_MANIFEST.json')
   assert extra['no_parameter_changes'] is True and extra['official_scores_reused_not_repeated'] is True
   assert len({x['experiment'] for x in specs+extra['profiles']})==len(specs)+len(extra['profiles'])
   specs+=extra['profiles']
  for spec in specs:
   experiment=spec['experiment'];folder=root/'staging'/experiment.lower();item={'model':spec['model'],'experiment_id':experiment,'status':'NOT MEASURED','groups':None}
   if (folder/'AUDIT.json').exists() and (folder/'INDEPENDENT_REVIEW.json').exists():
    a=read(folder/'AUDIT.json');r=read(folder/'INDEPENDENT_REVIEW.json')
    assert a['official_benchmark'] is False and r['audit_sha256']==H(folder/'AUDIT.json') and r['changed_judgments']==[]
    assert a['planned_requests']==16 and a['completed_requests']==len(a['scored_tasks'])==r['replayed_requests']
    for category in ('coding','tools'):
     subset=[t for t in a['scored_tasks'] if t['category']==category]
     assert len(subset)==a['groups'][category]['completed'] and sum(t['success'] for t in subset)==a['groups'][category]['successes']
    raw=Path(a['raw_root']);assert all(H(raw/name)==h for name,h in a['original_raw_files_sha256'].items())
    actual=read(raw/'profile.json');original=next(x for x in inventory['models'] if x['model']==spec['model'].removesuffix(' · OFF/T0'))
    parent_capture=Path(original['parent_capture'])
    if spec in specs[len(vp['profiles']):]:
     selection=read(folder/'PARENT_SELECTION.json');assert selection['additional_plan_sha256']==H(extra_path)
     assert selection['model']==spec['model']
     evidence=selection['evidence'][-1];assert evidence['experiment_id']==spec['parent_experiment']
     assert evidence['model_sha256']==original['model_sha256']
     parent_audit=Path(evidence['audit_path']);assert H(parent_audit)==evidence['audit_sha256']
     qualified=Path(evidence['qualification_path']);assert H(qualified)==evidence['qualification_sha256']
     qualification=read(qualified);assert qualification['tasks']==200 and len(set(qualification['task_ids']))==200
     assert qualification['qualification_kind']=='FULL_OFFICIAL_BFCL_CATEGORY_LOCAL_PROTOCOL_VERIFIED'
     assert qualification['audit_hash']==H(parent_audit)
     audited=read(parent_audit);assert audited['measurement_valid'] and audited['GPU_execution_observed']
     assert len(audited['parts'])==1
     part=audited['parts'][0];gpu=Path(part['audit_path']);assert H(gpu)==part['audit_sha256']
     parent_capture=gpu.parent
     campaign=read(folder/'CAMPAIGN_PLAN.json');assert campaign['protocol_sha256']==H(extra_path)
     assert a['validation_exposure']==extra['exposure']
     item.update(additional_plan_sha256=H(extra_path),validation_exposure=extra['exposure'])
    parent=read(parent_capture/'profile.json')
    assert (actual.get('model_sha256') or actual['assets'][actual['model']])==original['model_sha256']
    assert same_validation_inference(actual,parent),'Validation inference differs from the executed qualified parent'
    parent_runs=[r for r in history['runs'] if r['experiment_id']==spec['parent_experiment']]
    assert parent_runs and len({r['runtime_configuration_id'] for r in parent_runs})==1
    parent_id=parent_runs[0]['runtime_configuration_id'];recorded=profiles[parent_id]
    assert recorded['model']['artifact_sha256']==original['model_sha256']
    item.update(runtime_configuration_id=parent_id,recorded_parent_profile=recorded,captured_validation_profile_sha256=H(raw/'profile.json'),parent_experiment_id=spec['parent_experiment'])

    item.update(status=a['status'],groups={k:project_group(g) for k,g in a['groups'].items()},audit_sha256=H(folder/'AUDIT.json'),independent_review_sha256=H(folder/'INDEPENDENT_REVIEW.json'),peak_vram_mib=a['peak_device_vram_mib'],task_phase_s=a['task_phase_s'])
   vr.append(item)
  output['independent_validation16']={'official_benchmark':False,'scope':'Frozen8coding+8mock-tool reserved tasks, no parameter tuning. Tasks were already exposed on the original three profiles; additional fixed-profile measurements are not a globally unseen holdout. Small descriptive validation, not an official benchmark or model-superiority proof.','plan_sha256':H(validation_dir/'PLAN.json'),'rows':vr}
  if (validation_dir/'COHORT_REVIEW.json').exists():
   review=read(validation_dir/'COHORT_REVIEW.json');assert review['plan_sha256']==H(validation_dir/'PLAN.json')
   assert H(validation_dir/'COHORT_REVIEW.json')==read(root/'BENCHMARK_REFERENCES.json')['summary']['independent_validation16']['cohort_review_sha256']
   for result in review['rows']:
    projected=next(x for x in vr if x['experiment_id']==result['experiment_id']);assert projected['audit_sha256']==result['audit_sha256'] and projected['independent_review_sha256']==result['independent_review_sha256']
   output['independent_validation16']['cohort_review_sha256']=H(validation_dir/'COHORT_REVIEW.json')
   output['independent_validation16']['decision']=review['decision']
   output['independent_validation16']['failure_classes']=[{'model':r['model'],'experiment_id':r['experiment_id'],'classes':[f['classification'] for f in r['failures']],'actual_tool_executions':0} for r in review['rows']]
  additional_review=validation_dir/'ADDITIONAL_PROFILES_REVIEW.json'
  if additional_review.exists():
   review=read(additional_review)
   pin=read(root/'BENCHMARK_REFERENCES.json')['summary']['independent_validation16_additional']
   assert H(additional_review)==pin['review_sha256'] and review['additional_plan_sha256']==H(extra_path)
   assert review['original_plan_sha256']==H(validation_dir/'PLAN.json') and review['original_cohort_sha256']==H(validation_dir/'COHORT_REVIEW.json')
   assert review['official_benchmark'] is False and review['winner_qualified'] is False
   assert {r['experiment_id'] for r in review['rows']}=={r['experiment'] for r in extra['profiles']}
   for result in review['rows']:
    projected=next(x for x in vr if x['experiment_id']==result['experiment_id'])
    assert projected['audit_sha256']==result['audit_sha256'] and projected['independent_review_sha256']==result['independent_review_sha256']
    for category in ('coding','tools'):assert projected['groups'][category]['successes']==result[category+'_successes']
   output['independent_validation16'].update(additional_review_sha256=H(additional_review),additional_decision=review['decision'])
  output['holdout']['status_at_freeze']=output['holdout']['status'];output['holdout']['status']='SEPARATE_PREDECLARED_VALIDATION_PHASE'
  output['holdout']['scope_at_freeze']=output['holdout']['scope']
  exposed=sum(r['groups'] is not None for r in vr)
  output['holdout']['evaluated_profiles']=exposed
  output['holdout']['scope']=('Previously reserved8+8 tasks; evaluated on '+str(exposed)+' frozen profiles. They are no longer untouched for these profiles. No parameter tuning or official benchmark claim.' if exposed else 'Reserved8+8 tasks remain unexecuted on models; no official benchmark claim.')
  output['holdout']['current_scope']=output['holdout']['scope']
 output['qualification_phase']=qualification_phase(root,history)
 validate(output);return output

def validate(data):
 assert data['official_benchmark'] is False and data['tasks_per_category']==16
 assert len({json.dumps(r['configuration'],sort_keys=True,separators=(',',':')) for r in data['rows']})==len(data['rows'])
 for row in data['rows']:
  assert re.fullmatch('[a-f0-9]{64}',row['configuration']['model_sha256'])
  assert row['status'] in ('SCREENING OFFEN','SCREENING VOLLSTÄNDIG','VERTIEFUNG EMPFOHLEN','WEITERE DIAGNOSE','TECHNISCH BLOCKIERT')
  if row['results'] is None:continue
  assert re.fullmatch('[a-f0-9]{64}',row['audit_sha256']) and re.fullmatch('[a-f0-9]{64}',row['independent_review_sha256'])
  for g in row['results'].values():
   assert type(g['completed']) is int and type(g['successes']) is int and 0<=g['successes']<=g['completed']<=16
   assert g['wilson95']==wilson(g['successes'],g['completed'])

 v=data.get('independent_validation16')
 if v:
  assert v['official_benchmark'] is False and len(v['rows'])>0
  assert len({r['experiment_id'] for r in v['rows']})==len(v['rows'])
  for row in v['rows']:
   if row['groups'] is None:
    assert row['status']=='NOT MEASURED'
    continue
   assert re.fullmatch('[a-f0-9]{64}',row['audit_sha256']) and re.fullmatch('[a-f0-9]{64}',row['independent_review_sha256'])
   assert set(row['groups'])=={'coding','tools'}
   for g in row['groups'].values():
    assert type(g['completed']) is int and type(g['successes']) is int and 0<=g['successes']<=g['completed']<=8
    assert g['wilson95']==wilson(g['successes'],g['completed'])

 q=data.get('qualification_phase')
 if q:
  assert q['validation']['model_requests']==0 and q['validation']['status']=='FROZEN_NOT_RELEASED_NO_MODEL_RESULTS'
  assert q['gemma_context']['quality_score'] is None and q['gemma_context']['model_requests']==0
  assert all(c['official_agents']=='NOT MEASURED' for c in q['candidates'])
  m=q['multi_agent_plan'];assert m['total_task_budget_s']==1200 and m['per_arm_task_budget_s']*len(m['arms'])==1200 and m['GPU_concurrency']==1
  ids=[]
  for row in q.get('model_validation',[]):
   metric=row['metrics'];ids.append(row['experiment_id'])
   assert metric['tasks']==metric['planned_tasks']==33 and 0<=metric['solved']<=33
   assert metric['official_benchmark'] is False and metric['winner_qualified'] is False
   assert metric['data_role']=='FROZEN33_VALIDATION_AUTHORED_FAMILIES_NOT_OFFICIAL'
  assert len(ids)==len(set(ids))
  review=q.get('decision_review')
  if review:
   assert review['official_benchmark'] is False and review['winner_qualified'] is False
   assert len(review['profiles'])==len(ids) and {r['experiment_id'] for r in review['profiles']}==set(ids)
   assert re.fullmatch('[a-f0-9]{64}',review['review_sha256'])

def render(data):
 from html import escape as e
 def fmt(v,digits=1):return 'NOT MEASURED' if v is None else f'{v:,.{digits}f}'
 def score(g):
  if g is None:return 'NOT MEASURED'
  return (("PARTIAL · " if g['completed']<16 else "")+f"{g['successes']}/{g['completed']} · {100*g['successes']/g['completed']:.1f}%") if g['completed'] else 'NOT MEASURED'
 rows=[]
 for row in data['rows']:
  groups=row['results'];values=list(groups.values()) if groups else [];wall=sum(g['completed_request_wall_s'] for g in values) if values else None;tokens=sum(g['completion_tokens'] for g in values) if values and all(g['completion_tokens'] is not None for g in values) else None
  energy=[g.get('gpu_energy_j_lower') for g in values];solved=sum(g['successes'] for g in values)
  joules=sum(energy)/solved if energy and all(x is not None for x in energy) and solved else None
  detail={k:v for k,v in row.items() if k!='results'};detail['category_results']=groups
  cells=[e(row['model']),e(row['status']+(' · '+row['selection_status'] if row.get('selection_status') else '')),score(groups.get('coding')) if groups else 'NOT MEASURED',score(groups.get('tools')) if groups else 'NOT MEASURED',fmt(wall),fmt(tokens/wall if tokens is not None and wall else None),fmt(joules),fmt(row.get('peak_vram_mib'))]
  content=('<a href="../experiments/'+e(row['experiment_id'])+'/">Screening '+e(row['experiment_id'])+'</a> · ' if row.get('experiment_id') else '')+'<details><summary>Profile & evidence</summary><pre>'+e(json.dumps(detail,indent=2))+'</pre></details>'
  parent=row['parent_experiment_id']
  if row.get('full_benchmark_runs'):
   cells.append(' · '.join('<a href="../experiments/'+e(r['experiment_id'])+'/">'+e(r['experiment_id'])+'</a>' for r in row['full_benchmark_runs'])+' · <a href="../configuration-comparison/">Official comparison</a>')
  else:cells.append('NOT MEASURED' if row.get('full_benchmark_status')=='NOT MEASURED' else f'<a href="../experiments/{parent}/">{parent} archive</a> · <a href="../configuration-comparison/">Official comparison</a>')
  rows.append('<tr>'+''.join('<td>'+v+'</td>' for v in cells)+'<td>'+content+'</td></tr>')
 headers=['Model','Status','Coding /16','Mock tools /16','Request time s','Output tok/s¹','GPU J/success ≥²','VRAM MiB','Existing benchmarks','Details']
 html='<div class="screening-wrap"><table id="screening-table"><thead><tr>'+''.join('<th>'+e(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
 extra_items=[]
 for x in data.get('other_local_artifacts',[]):
  link=(' <a href="../audits/'+e(x['audit_id'])+'/">CPU review</a> · GPU screen: NOT MEASURED') if x.get('audit_id') else ''
  extra_items.append('<li><strong>'+e(x['artifact'])+'</strong> — '+e(x['status'])+': '+e(x['reason'])+link+'</li>')
 extras='\n\n<details><summary>Other local artifacts: technical disposition</summary><ul>'+''.join(extra_items)+'</ul></details>\n'
 plan=data.get('qualification_plan',{})
 if plan:
  extra_items=['<li><strong>'+e(x['priority'])+' · '+e(', '.join(x['models']))+'</strong>: '+e(x['action'])+'</li>' for x in plan['priorities']]
  extras+='\n<details><summary>Conservative qualification shortlist & next decisions</summary><ul>'+''.join(extra_items)+'</ul><p>'+e(plan['agents'])+'</p></details>\n'
 if data.get('independent_validation16'):
  extras+='\n[Reserved independent validation: status and evidence](pipeline-methods.md#independent-native-profile-validation).\n'
 measured=sum(r['results'] is not None for r in data['rows']);return '# Model screening\n\n'+f'**{measured}/{len(data["rows"])} profiles measured** · 16 coding + 16 mock-tool development tasks.\n\nScreening → full qualification → targeted optimization → independent confirmation.\n\n'+('[Current Jarvis qualification shortlist](pipeline-methods.md#jarvis-qualification) · screening complete; no repeat planned.\n\n' if data.get('qualification_phase') else '')+'<input id="screening-search" type="search" placeholder="Filter models or status" aria-label="Filter screening models">\n\n'+html+'\n\nDevelopment evidence, not an official benchmark or unseen validation set. These tasks were previously used for Nexus A/B/C tuning. No automatic exclusion from small score differences. Wilson intervals, native sampling, hashes, missing answers and audit references are in **Details**. Native templates and settings remain unchanged. Reserved8+8 validation status and evidence are recorded separately in the methods archive.\n\n¹ Completion tokens / completed-request wall time, including reasoning when reported; not pure decode speed. ² Counter-bracketed lower bound; upper bounds remain in Details. Failed completed requests count toward costs. Historical Nexus A timings used an interleaved ABC schedule. Missing values stay unknown.\n'+extras


def render_validation(data):
 from html import escape as e
 v=data.get('independent_validation16')
 if not v:return ''
 rows=[]
 for r in v['rows']:
  g=r['groups'];score=lambda c:'NOT MEASURED' if g is None else str(g[c]['successes'])+'/'+str(g[c]['completed'])
  evidence='['+r['experiment_id']+'](experiments/'+r['experiment_id']+'.md)' if g is not None else 'NOT MEASURED'
  if g is not None and r.get('runtime_configuration_id'):evidence+=' · [Exact inference profile](configuration-profiles/'+r['runtime_configuration_id']+'.md)'
  rows.append('| '+e(r['model'])+' | '+score('coding')+' | '+score('tools')+' | '+evidence+' |')
 return '\n## Independent native-profile validation\n\n'+v['scope']+'\n\n| Profile | Coding /8 | Mock tools /8 | Evidence |\n|---|---|---|---|\n'+'\n'.join(rows)+'\n\nFull official coding/tools qualifications were reused. No original benchmark score changed.\n'+('\nOriginal three-profile cohort: all three profiles proposed a simulated tool call despite explicit denial in one frozen case. No tool was executed. Qwen3.5 and OmniCoder also refused an unsupported request without the required status JSON; Gemma failed one coding task. These are profile-specific observations, not population safety rates. Keep permission enforcement outside model responses.\n' if v.get('cohort_review_sha256') else '')+('\nAdditional fixed-profile validation: '+e(v['additional_decision'])+'\n' if v.get('additional_decision') else '')


def render_native_agent_development(experiments):
 """Isolated workflow evidence, deliberately outside official agent rankings."""
 from html import escape
 selected=[e for e in experiments if e.get('aggregate_metrics',{}).get('native_agent18_development')]
 if not selected:return ''
 rows=[];group_note=''
 grouped=[e for e in selected if e.get('native_agent_grouped_review')]
 if grouped:
  last=grouped[-1];g=last['native_agent_grouped_review']['aggregate_metrics']['quality'];group_note='\n\nThe '+str(g['frozen_tasks_per_model'])+' tasks share '+str(g['frozen_generalization_groups'])+' original generalization groups. [Group-aware sensitivity review](experiments/'+last['id']+'.md) preserves the original case-wise statistics and independently verifies group-level sign flips. All p-values are exploratory and unadjusted across model comparisons; no population-superiority or independent-task claim follows.\n'
 def value(n):return 'NOT MEASURED' if n is None else format(n,'.2f')
 for e in selected:
  m=e['aggregate_metrics']['native_agent18_development']
  assert m['official_benchmark'] is False and m['winner_qualified'] is False
  energy='NOT MEASURED' if m.get('gpu_j_per_success_lower') is None or m.get('gpu_j_per_success_upper') is None else value(m['gpu_j_per_success_lower'])+'–'+value(m['gpu_j_per_success_upper'])
  model=escape(str(e.get('model','NOT RECORDED'))).replace('|','\\|')
  rows.append('| ['+e['id']+'](experiments/'+e['id']+'.md) | '+model+' | '+str(m['solved'])+'/'+str(m['tasks'])+' | '+value(m.get('task_phase_s'))+' | '+energy+' | '+value(m.get('peak_device_vram_mib'))+' | '+str(m.get('technical_preflight_cases','NOT MEASURED'))+' / '+str(m.get('technical_request_errors','NOT MEASURED'))+' |')
 return '\n## Native Agent18 development evidence\n\nPreviously used frozen simulated coding, automation and read workflows. **Not Terminal-Bench, unseen validation, a production safety certificate or a Champion qualification.** Native model profiles are preserved; the required/single-tool-call envelope is explicit.\n\n| Experiment | Native model profile | Solved / completed | Task phase s | GPU J/success bounds | Peak VRAM MiB | Preflight / HTTP failures |\n|---|---|---|---|---|---|---|\n'+'\n'.join(rows)+group_note+'\n\nQuality is independently replayed from the actual retained replies in a non-root CPU jail using the original simulator and oracle. No productive tools execute. Technical context/transport failures remain separate in the linked audit; incomplete captures remain partial. Energy covers the measured case window, including failed tasks and setup between cases, excluding load/warmup and CPU/system energy. Nonstream output-token rate is not pure decode speed or TTFT. No scores are added to the official model table or its mean.\n\nAdmission retains the trusted broker, immutable source/execution review, exact asset hashes, one GPU lease and all power, VRAM, temperature, ECC and throttling guards. A source hash alone grants no trust. The development runner and independent CPU replay were checked with original simulator controls before actual inference.\n'


def render_qualification(data):
 from html import escape
 q=data.get('qualification_phase')
 if not q:return ''
 out='\n## Jarvis qualification\n\nScreening is complete. This is a provisional shortlist, **not a new ranking**. [Existing complete benchmark results](configuration-comparison.md) remain unchanged.\n\n'
 for c in q['candidates']:
  refs=', '.join('['+e+'](experiments/'+e+'.md)' for e in c['source_experiments'])
  note='; incomplete evidence remains PARTIAL' if any(not r['official_eligible'] for r in c['full_benchmark_records']) else ''
  out+='- **'+escape(c['profile'])+'**: '+refs+note+'. Official agent qualification: NOT MEASURED.\n'
 v=q['validation'];t=q['terminal_bench'];g=q['gemma_context'];m=q['multi_agent_plan']
 results=q.get('model_validation',[])
 if results:
  out+='\n### Frozen agent validation\n\n33 frozen cases / 11 related-task groups; all tools simulated. Native profiles may differ. This is separate validation evidence, **not Terminal-Bench or an official Agents score**.\n\n'
  out+='| Profile | Success | Task time | Completion tok/s¹ | GPU J/success² | Peak VRAM MiB | Evidence |\n|---|---:|---:|---:|---:|---:|---|\n'
  for row in results:
   metric=row['metrics'];value=lambda key:format(metric[key],'.2f') if metric.get(key) is not None else 'NOT MEASURED'
   out+='| '+escape(row['model'])+' | '+str(metric['solved'])+'/'+str(metric['tasks'])+' | '+value('task_phase_s')+'s | '+value('tokens_s_completed_requests')+' | '+value('gpu_j_per_success_lower')+'–'+value('gpu_j_per_success_upper')+' | '+value('peak_device_vram_mib')+' | ['+row['experiment_id']+'](experiments/'+row['experiment_id']+'.md) |\n'
  out+='\n¹ Includes reasoning where reported; not pure decode. ² Counter-bracketed GPU energy. One pass over11 authored families does not establish population superiority. Private fixtures/oracles are not exported.\n'
  for row in results:
   correction=row['metrics'].get('evaluation_correction_audit_id')
   if correction:out+='\nEvaluator correction: replay preserves the exact captured fixture mapping order after checking equality with the frozen archive. Original replies and scoring rules are unchanged; no additional GPU run. [Correction evidence](audits/'+correction+'.md).\n'
 elif q.get('validation_execution'):
  out+='\n**Frozen agent validation:** model execution started on33cases/11groups. No audited model result yet; CPU controls remain harness evidence only.\n'
 else:
  out+='\n**Reserved agent validation:** '+str(v['cases'])+' frozen cases / '+str(v['generalization_groups'])+' related-task groups; zero model responses. CPU-only controls: '+str(v['golden_QA_passed'])+' golden passes, '+str(v['wrong_final_QA_rejected'])+' incorrect-final rejections and '+str(v['forbidden_action_QA_rejected'])+' forbidden-action rejections. Fixtures/oracles remain private and unreleased. These are harness checks, not model scores.\n'

 out+='\n**Terminal-Bench 2.1:** '+str(t['tasks'])+' tasks verified at revision `'+t['revision']+'`; Harbor '+t['evaluator_version']+' source inspected. [Official dataset]('+t['sources'][0]+'). No local official score; isolated container/evaluator/broker execution remains unadmitted.\n'
 out+='\n**Gemma context:** ['+g['experiment_id']+'](experiments/'+g['experiment_id']+'.md) failed during startup, before any task. The bridge fix passed '+str(g['CPU_fix_tests'])+' direct transport controls. This is not a negative model-quality result.\n'
 if g.get('corrective_result'):
  c=g['corrective_result'];out+='\nCorrected GPU run ['+c['experiment_id']+'](experiments/'+c['experiment_id']+'.md): '+str(c['tasks'])+' cases completed, '+str(c['context_preflight_errors'])+' context-preflight errors and '+str(c['HTTP_errors'])+' request errors; '+str(c['solved'])+'/'+str(c['tasks'])+' solved versus '+str(c['reference_solved'])+'/'+str(c['tasks'])+' at8K. Task time changed by '+format(c['task_phase_change_percent'],'+.2f')+'%, peak VRAM by '+format(c['peak_vram_change_mib'],'+.0f')+'MiB. Technical fix confirmed; no task-success gain or Champion claim.\n'
  out+='\nThe corrected run made '+str(c['model_requests'])+' model requests versus '+str(c['reference_model_requests'])+' before. The task-time difference includes those additional turns; it is not an isolated decode-speed comparison.\n'
 else:out+='\nNew bridge GPU execution remains unadmitted.\n'
 if q.get('slopus_diagnosis'):
  sl=q['slopus_diagnosis'];out+='\n**Slopus diagnosis:** ['+sl['experiment_id']+'](experiments/'+sl['experiment_id']+'.md) recorded '+str(sl['recorded_policy_violations'])+' rejected simulated policy proposals and '+str(sl['length_stopped_responses'])+' length-stopped response. Complete coding/tools results remain valid; no global model exclusion.\n'
 out+='\n**Orchestration:** Single-Agent, Planner + Worker, and Planner + Worker + Reviewer are planned with one shared '+str(m['total_task_budget_s'])+'s task allowance ('+str(m['per_arm_task_budget_s'])+'s per arm), identical model/tasks and one GPU job. Recovery/delegation controls remain pending; no orchestration result is claimed. Keep deterministic permissions outside all model roles.\n'
 review=q.get('decision_review')
 if review:
  out+='\n### Decisions after native-profile validation\n\nProvisional role selection; **not a winner qualification**. Policy checks count cases with no prohibited proposal; permissions stay outside every model.\n\n'
  out+='<div class="screening-wrap"><table id="qualification-decisions"><thead><tr><th>Profile</th><th>Policy checks</th><th>Next decision</th><th>Evidence</th></tr></thead><tbody>'
  for row in review['profiles']:
   out+='<tr><td>'+escape(row['model'])+'</td><td>'+str(row['policy_gate_passes'])+'/33</td><td>'+escape(row['reason'])+'</td><td><a href="../experiments/'+row['experiment_id']+'/">Evidence '+row['experiment_id']+'</a></td></tr>'
  out+='</tbody></table></div>\n\n<details><summary>Confirmation and optimization gates</summary>\n\n'
  for step in review['next_decisions']:out+='- '+escape(step)+'\n'
  out+='\nDecision review SHA256: `'+review['review_sha256']+'`. Other models and all negative results remain in the archive.\n\n</details>\n'
 elif results:
  out+='\nNext: finish the remaining native-profile validation, review context/wrapper diagnostics, then select confirmation candidates. Other models and all negative results remain in the archive.\n'
 else:
  out+='\nNext: source-admit the existing runner for the reserved validation, finish context/wrapper diagnostics, then select optimization candidates. Other models and all negative results remain in the archive.\n'
 return out
