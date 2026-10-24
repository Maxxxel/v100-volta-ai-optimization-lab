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

def build(root):
 root=Path(root);base=root/'staging/model-comparison-preparation/model-screening';holdout=read(base/'VALIDATION_FROZEN_MANIFEST.json')
 assert all(H(base/k)==v for k,v in holdout['files'].items())
 inventory=read(base/'MODEL_INVENTORY.json');protocol=read(base/'PROTOCOL.json');rows=[]
 history=read(Path(__file__).resolve().parents[1]/'data/configuration-history.json');profiles={p['runtime_configuration_id']:p for p in history['profiles']}
 for entry in inventory['models']:
  profile=read(Path(entry['parent_capture'])/'profile.json');recipe=profile['native_recipe'];sha=profile.get('model_sha256') or profile['assets'][profile['model']]
  assert sha==entry['model_sha256']
  cfg={'parent_profile_id':entry['parent_profile'],'model_sha256':sha,'request_options':{k:v for k,v in recipe['request_options'].items() if k in ('chat_template_kwargs','temperature','seed','max_tokens','top_p','top_k','min_p','repeat_penalty','presence_penalty','reasoning_effort','cache_prompt')},'context':recipe['context'],'engine':'llama.cpp native','engine_version':None,'binary_identities':{Path(k).name:v for k,v in profile['assets'].items() if Path(k).name in ('llama-server','libggml-cuda.so','libggml-cuda.so.0','libggml-cuda.so.0.21.0')},'warmup_requests':len(recipe['warmups']),'task_time_policy':profile.get('task_time_policy'),'hardware':'Tesla V100 SXM2 16 GB','power_w':300}
  matches=[r for r in history['runs'] if r['experiment_id']==entry['parent_experiment_id']]
  if matches:
   recorded=profiles[matches[0]['runtime_configuration_id']]
   assert recorded['model']['artifact_sha256']==sha
   cfg['recorded_parent_profile']=recorded
   cfg['quantization']=recorded['model']['quantization']
  identity={k:v for k,v in cfg.items() if k!='recorded_parent_profile'}
  cfg['screening_configuration_id']='screening-config-'+hashlib.sha256(json.dumps(identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  row={'model':entry['model'],'configuration':cfg,'status':entry['status'],'local_artifact_available':entry['local_artifact_available'],'parent_experiment_id':entry['parent_experiment_id'],'results':None,'audit_sha256':None,'experiment_id':None,'conditions':'Single native-profile session; frozen base-task order','decision':'No quality exclusion from16 tasks; retain for review.','independent_review_sha256':None}
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
  rows.append(row)
 output={'schema':1,'official_benchmark':False,'dataset_id':protocol['dataset_id'],'tasks_per_category':16,'source_tasks_sha256':protocol['source_tasks_sha256'],'source_oracles_sha256':protocol['source_oracles_sha256'],'protocol_sha256':H(base/'PROTOCOL.json'),'data_role':'DEVELOPMENT_ALREADY_USED_FOR_NEXUS_VARIANT_SELECTION','holdout':{'status':read(base/'VALIDATION_FROZEN_MANIFEST.json')['status'],'coding':8,'mock_tools':8,'manifest_sha256':H(base/'VALIDATION_FROZEN_MANIFEST.json'),'scope':'Reserved unexecuted authored tasks, not broker-admitted. No independent-population guarantee; no official benchmark claim.'},'selection':'No automatic quality rejection. Small differences retain both candidates; technical failures require diagnosis. Reuse matching full benchmarks.','rows':rows}
 extras=[]
 for x in inventory.get('other_local_artifacts',[]):
  assert re.fullmatch(r'[A-Za-z0-9_.-]{1,120}\.gguf',x['artifact'])
  extras.append({k:x[k] for k in ('artifact','status','reason')})
 output['other_local_artifacts']=extras
 plan=read(base/'QUALIFICATION_SELECTION_PLAN.json')
 output['qualification_plan']={k:plan[k] for k in ('rule','priorities','agents','holdout')}
 output['qualification_plan_sha256']=H(base/'QUALIFICATION_SELECTION_PLAN.json')
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
  cells=[e(row['model']),e(row['status']),score(groups.get('coding')) if groups else 'NOT MEASURED',score(groups.get('tools')) if groups else 'NOT MEASURED',fmt(wall),fmt(tokens/wall if tokens is not None and wall else None),fmt(joules),fmt(row.get('peak_vram_mib'))]
  content=('<a href="../experiments/'+e(row['experiment_id'])+'/">Screening '+e(row['experiment_id'])+'</a> · ' if row.get('experiment_id') else '')+'<details><summary>Profile & evidence</summary><pre>'+e(json.dumps(detail,indent=2))+'</pre></details>'
  parent=row['parent_experiment_id'];cells.append(f'<a href="../experiments/{parent}/">{parent} archive</a> · <a href="../configuration-comparison/">Official comparison</a>')
  rows.append('<tr>'+''.join('<td>'+v+'</td>' for v in cells)+'<td>'+content+'</td></tr>')
 headers=['Model','Status','Coding /16','Mock tools /16','Request time s','Output tok/s¹','GPU J/success ≥²','VRAM MiB','Existing benchmarks','Details']
 html='<div class="screening-wrap"><table id="screening-table"><thead><tr>'+''.join('<th>'+e(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
 extras='\n\n<details><summary>Other local artifacts pending standalone-profile review</summary>\n\n'+''.join('- **'+e(x['artifact'])+'** — '+e(x['status'])+': '+e(x['reason'])+'\n' for x in data.get('other_local_artifacts',[]))+'\n</details>\n'
 plan=data.get('qualification_plan',{})
 if plan:
  extras+='\n<details><summary>Conservative qualification shortlist & next decisions</summary>\n\n'+''.join('- **'+e(x['priority'])+' · '+e(', '.join(x['models']))+'**: '+e(x['action'])+'\n' for x in plan['priorities'])+'\n'+e(plan['agents'])+'\n\n</details>\n'
 measured=sum(r['results'] is not None for r in data['rows']);return '# Model screening\n\n'+f'**{measured}/{len(data["rows"])} profiles measured** · 16 coding + 16 mock-tool development tasks.\n\nScreening → full qualification → targeted optimization → independent confirmation.\n\n'+'<input id="screening-search" type="search" placeholder="Filter models or status" aria-label="Filter screening models">\n\n'+html+'\n\nDevelopment evidence, not an official benchmark or unseen validation set. These tasks were previously used for Nexus A/B/C tuning. No automatic exclusion from small score differences. Wilson intervals, native sampling, hashes, missing answers and audit references are in **Details**. A separate8coding+8mock-tool validation set is frozen and reserved; no model has answered it. Native templates and settings remain unchanged.\n\n¹ Completion tokens / completed-request wall time, including reasoning when reported; not pure decode speed. ² Counter-bracketed lower bound; upper bounds remain in Details. Failed completed requests count toward costs. Historical Nexus A timings used an interleaved ABC schedule. Missing values stay unknown.\n'+extras
