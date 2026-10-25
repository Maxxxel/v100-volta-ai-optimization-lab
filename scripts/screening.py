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
  matches=[r for r in history['runs'] if r['experiment_id']==entry['parent_experiment_id']]
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
   if source.get('cpu_diagnosis_path'):
    assert H(source['cpu_diagnosis_path'])==source['cpu_diagnosis_sha256'];diagnosis=read(source['cpu_diagnosis_path']);assert diagnosis['source_audit_sha256']==row['audit_sha256'] and diagnosis['GPU_runs']==0
    row.update(selection_status='WEITERE DIAGNOSE',decision=diagnosis['decision'],diagnostic_audit_sha256=source['cpu_diagnosis_sha256'],diagnostic_summary=diagnosis['coding'])
  rows.append(row)
 output={'schema':1,'official_benchmark':False,'dataset_id':protocol['dataset_id'],'tasks_per_category':16,'source_tasks_sha256':protocol['source_tasks_sha256'],'source_oracles_sha256':protocol['source_oracles_sha256'],'protocol_sha256':H(base/'PROTOCOL.json'),'data_role':'DEVELOPMENT_ALREADY_USED_FOR_NEXUS_VARIANT_SELECTION','holdout':{'status':read(base/'VALIDATION_FROZEN_MANIFEST.json')['status'],'coding':8,'mock_tools':8,'manifest_sha256':H(base/'VALIDATION_FROZEN_MANIFEST.json'),'scope':'Reserved unexecuted authored tasks, not broker-admitted. No independent-population guarantee; no official benchmark claim.'},'selection':'No automatic quality rejection. Small differences retain both candidates; technical failures require diagnosis. Reuse matching full benchmarks.','rows':rows}
 extras=[]
 for x in inventory.get('other_local_artifacts',[]):
  assert re.fullmatch(r'[A-Za-z0-9_.-]{1,120}\.gguf',x['artifact'])
  extras.append({k:x[k] for k in ('artifact','status','reason')})
 output['other_local_artifacts']=extras
 plan=read(base/'QUALIFICATION_SELECTION_PLAN.json')
 output['qualification_plan']={k:plan[k] for k in ('rule','priorities','agents')}
 output['qualification_plan']['holdout_at_plan_creation']=plan['holdout']
 output['qualification_plan']['created_at_utc']=plan['at_utc']
 output['qualification_plan_sha256']=H(base/'QUALIFICATION_SELECTION_PLAN.json')
 validation_dir=base.parent/'independent-validation16'
 if (validation_dir/'PLAN.json').exists():
  vp=read(validation_dir/'PLAN.json');vr=[]
  for spec in vp['profiles']:
   experiment=spec['experiment'];folder=root/'staging'/experiment.lower();item={'model':spec['model'],'experiment_id':experiment,'status':'NOT MEASURED','groups':None}
   if (folder/'AUDIT.json').exists() and (folder/'INDEPENDENT_REVIEW.json').exists():
    a=read(folder/'AUDIT.json');r=read(folder/'INDEPENDENT_REVIEW.json')
    assert a['official_benchmark'] is False and r['audit_sha256']==H(folder/'AUDIT.json') and r['changed_judgments']==[]
    assert a['planned_requests']==16 and a['completed_requests']==len(a['scored_tasks'])==r['replayed_requests']
    for category in ('coding','tools'):
     subset=[t for t in a['scored_tasks'] if t['category']==category]
     assert len(subset)==a['groups'][category]['completed'] and sum(t['success'] for t in subset)==a['groups'][category]['successes']
    raw=Path(a['raw_root']);assert all(H(raw/name)==h for name,h in a['original_raw_files_sha256'].items())
    actual=read(raw/'profile.json');original=next(x for x in inventory['models'] if x['model']==spec['model']);parent=read(Path(original['parent_capture'])/'profile.json')
    assert (actual.get('model_sha256') or actual['assets'][actual['model']])==original['model_sha256']
    assert actual['native_recipe']['request_options']==parent['native_recipe']['request_options']
    assert actual['assets']==parent['assets'] and actual['native_recipe']['argv_tail']==parent['native_recipe']['argv_tail']
    item.update(status=a['status'],groups={k:project_group(g) for k,g in a['groups'].items()},audit_sha256=H(folder/'AUDIT.json'),independent_review_sha256=H(folder/'INDEPENDENT_REVIEW.json'),peak_vram_mib=a['peak_device_vram_mib'],task_phase_s=a['task_phase_s'])
   vr.append(item)
  output['independent_validation16']={'official_benchmark':False,'scope':'Frozen8coding+8mock-tool reserved tasks, no parameter tuning. Small descriptive validation, not an official benchmark or model-superiority proof.','plan_sha256':H(validation_dir/'PLAN.json'),'rows':vr}
  if (validation_dir/'COHORT_REVIEW.json').exists():
   review=read(validation_dir/'COHORT_REVIEW.json');assert review['plan_sha256']==H(validation_dir/'PLAN.json')
   assert H(validation_dir/'COHORT_REVIEW.json')==read(root/'BENCHMARK_REFERENCES.json')['summary']['independent_validation16']['cohort_review_sha256']
   for result in review['rows']:
    projected=next(x for x in vr if x['experiment_id']==result['experiment_id']);assert projected['audit_sha256']==result['audit_sha256'] and projected['independent_review_sha256']==result['independent_review_sha256']
   output['independent_validation16']['cohort_review_sha256']=H(validation_dir/'COHORT_REVIEW.json')
   output['independent_validation16']['decision']=review['decision']
   output['independent_validation16']['failure_classes']=[{'model':r['model'],'experiment_id':r['experiment_id'],'classes':[f['classification'] for f in r['failures']],'actual_tool_executions':0} for r in review['rows']]
  output['holdout']['status_at_freeze']=output['holdout']['status'];output['holdout']['status']='SEPARATE_PREDECLARED_VALIDATION_PHASE'
  output['holdout']['current_scope']='The reserved8+8 tasks are now evaluated in a frozen three-profile cohort; these responses are not used to tune parameters.'
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
  assert v['official_benchmark'] is False and len(v['rows'])==3
  assert len({r['experiment_id'] for r in v['rows']})==3
  for row in v['rows']:
   if row['groups'] is None:
    assert row['status']=='NOT MEASURED'
    continue
   assert re.fullmatch('[a-f0-9]{64}',row['audit_sha256']) and re.fullmatch('[a-f0-9]{64}',row['independent_review_sha256'])
   assert set(row['groups'])=={'coding','tools'}
   for g in row['groups'].values():
    assert type(g['completed']) is int and type(g['successes']) is int and 0<=g['successes']<=g['completed']<=8
    assert g['wilson95']==wilson(g['successes'],g['completed'])

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
  parent=row['parent_experiment_id'];cells.append('NOT MEASURED' if row.get('full_benchmark_status')=='NOT MEASURED' else f'<a href="../experiments/{parent}/">{parent} archive</a> · <a href="../configuration-comparison/">Official comparison</a>')
  rows.append('<tr>'+''.join('<td>'+v+'</td>' for v in cells)+'<td>'+content+'</td></tr>')
 headers=['Model','Status','Coding /16','Mock tools /16','Request time s','Output tok/s¹','GPU J/success ≥²','VRAM MiB','Existing benchmarks','Details']
 html='<div class="screening-wrap"><table id="screening-table"><thead><tr>'+''.join('<th>'+e(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
 extras='\n\n<details><summary>Other local artifacts pending standalone-profile review</summary>\n\n'+''.join('- **'+e(x['artifact'])+'** — '+e(x['status'])+': '+e(x['reason'])+'\n' for x in data.get('other_local_artifacts',[]))+'\n</details>\n'
 plan=data.get('qualification_plan',{})
 if plan:
  extras+='\n<details><summary>Conservative qualification shortlist & next decisions</summary>\n\n'+''.join('- **'+e(x['priority'])+' · '+e(', '.join(x['models']))+'**: '+e(x['action'])+'\n' for x in plan['priorities'])+'\n'+e(plan['agents'])+'\n\n</details>\n'
 if data.get('independent_validation16'):
  extras+='\n[Reserved independent validation: status and evidence](pipeline-methods.md#independent-native-profile-validation).\n'
 measured=sum(r['results'] is not None for r in data['rows']);return '# Model screening\n\n'+f'**{measured}/{len(data["rows"])} profiles measured** · 16 coding + 16 mock-tool development tasks.\n\nScreening → full qualification → targeted optimization → independent confirmation.\n\n'+'<input id="screening-search" type="search" placeholder="Filter models or status" aria-label="Filter screening models">\n\n'+html+'\n\nDevelopment evidence, not an official benchmark or unseen validation set. These tasks were previously used for Nexus A/B/C tuning. No automatic exclusion from small score differences. Wilson intervals, native sampling, hashes, missing answers and audit references are in **Details**. Native templates and settings remain unchanged. Reserved8+8 validation status and evidence are recorded separately in the methods archive.\n\n¹ Completion tokens / completed-request wall time, including reasoning when reported; not pure decode speed. ² Counter-bracketed lower bound; upper bounds remain in Details. Failed completed requests count toward costs. Historical Nexus A timings used an interleaved ABC schedule. Missing values stay unknown.\n'+extras


def render_validation(data):
 from html import escape as e
 v=data.get('independent_validation16')
 if not v:return ''
 rows=[]
 for r in v['rows']:
  g=r['groups'];score=lambda c:'NOT MEASURED' if g is None else str(g[c]['successes'])+'/'+str(g[c]['completed'])
  evidence='['+r['experiment_id']+'](experiments/'+r['experiment_id']+'.md)' if g is not None else 'NOT MEASURED'
  rows.append('| '+e(r['model'])+' | '+score('coding')+' | '+score('tools')+' | '+evidence+' |')
 return '\n## Independent native-profile validation\n\n'+v['scope']+'\n\n| Profile | Coding /8 | Mock tools /8 | Evidence |\n|---|---|---|---|\n'+'\n'.join(rows)+'\n\nFull official coding/tools qualifications were reused. No original benchmark score changed.\n'+('\nObserved: all three profiles proposed a simulated tool call despite explicit denial in one frozen case. No tool was executed. Qwen3.5 and OmniCoder also refused an unsupported request without the required status JSON; Gemma failed one coding task. These are profile-specific observations, not population safety rates. Keep permission enforcement outside model responses.\n' if v.get('cohort_review_sha256') else '')
