"""Versioned benchmark/configuration projection. No GPU calls or source mutations."""
import copy,hashlib,html,json,math,pathlib,re
from comparison import extract_tuning
SCHEMA=1
H=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,allow_nan=False,separators=(',',':')).encode()).hexdigest()
def digest(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(pathlib.Path(p).read_text())
def finite(v):return type(v) in (int,float) and math.isfinite(v)
def verify_broker_capture(cfg,native,launch):
 if cfg['source_provenance']['kind']!='BROKER_NATIVE_CAPTURED_CONFIGURATION' or cfg['start_parameters']['exact_private_launch_sha256']!=H(launch):raise ValueError('Broker launch identity mismatch')
 if cfg['source_provenance']['frozen_model_profile_sha256']!=H({k:v for k,v in native.items() if k!='selected_task_inputs'}):raise ValueError('Broker native profile changed')
 assets=native['assets'];options=native['native_recipe']['request_options']
 if cfg['model']['artifact_sha256']!=assets[native['model']] or cfg['engine']['binary_sha256']!=assets[native['runtime']+'/llama-server']:raise ValueError('Broker model/engine identity mismatch')
 if launch['uid']!=65534 or launch['native_request_options']!=options:raise ValueError('Unverified native request recipe')
 sampling={k:v for k,v in options.items() if k in ('temperature','top_p','top_k','min_p','presence_penalty','repeat_penalty','seed')}
 if cfg['runtime']['sampling']!=sampling or cfg['runtime']['native_template_controls']!=options.get('chat_template_kwargs') or cfg['runtime']['max_output']!=options['max_tokens']:raise ValueError('Broker sampler/template/output mismatch')
 if cfg['runtime']['chat_template_sha256']!=assets[native['chat_template']]:raise ValueError('Broker template identity mismatch')
 argv=launch['argv'];flag=lambda key:argv[argv.index(key)+1] if key in argv and argv.index(key)+1<len(argv) else None
 for field,key in [('context','--ctx-size'),('batch','--batch-size'),('microbatch','--ubatch-size'),('CPU_threads','--threads'),('GPU_offload','--n-gpu-layers'),('thinking_reasoning_requested','--reasoning')]:
  if cfg['runtime'][field]!=flag(key):raise ValueError('Broker runtime flags mismatch')
 for field,key in [('speculation_type','--spec-type'),('flash_attention_requested','--flash-attn')]:
  if cfg['optimizations'][field]!=flag(key):raise ValueError('Broker optimization flags mismatch')
 if cfg['optimizations']['KV_precision']!={'k':flag('--cache-type-k'),'v':flag('--cache-type-v')}:raise ValueError('Broker KV precision mismatch')
 if cfg['engine']['build_id']!=pathlib.Path(native['runtime']).parent.name:raise ValueError('Broker build identity mismatch')
 kernel=cfg['engine'].get('kernel_library_file')
 if not kernel or cfg['engine']['kernel_library_sha256']!=assets.get(native['runtime']+'/'+kernel):raise ValueError('Broker kernel identity mismatch')
 return True
def definition_identity(d):
 keys=['benchmark_id','benchmark_revision','version','dataset_split','dataset_split_hash','scorer_version','required_task_count','expected_task_ids_hash','required_evaluation_settings','metric']
 return 'bench-'+H({k:d.get(k) for k in keys})
def official_gate(record,definition,proof):
 if not definition.get('official_definition_verified') or not isinstance(proof,dict):return False
 if not all(definition.get(k) for k in ('benchmark_revision','dataset_split_hash','scorer_version','expected_task_ids_hash')):return False
 required=['complete_task_set','official_scorer_verified','no_task_exclusions','prompt_protocol_verified','unique_task_ids_verified','metrics_verified','independent_audit_verified']
 if not all(proof.get(k) is True for k in required):return False
 if record.get('benchmark_id')!=definition['benchmark_id'] or record.get('benchmark_identity_id')!=definition_identity(definition):return False
 if record.get('dataset_split_hash')!=definition.get('dataset_split_hash') or record.get('scorer_version')!=definition.get('scorer_version'):return False
 if proof.get('all_canonical_controls_passed') is not True:
  # An unchanged, verified upstream oracle anomaly is not a custom scorer.
  # It can be admitted only when explicitly pinned in this benchmark protocol,
  # all tasks stay in the denominator, and every other control is validated.
  x=proof.get('canonical_reference_exception',{});allowed=definition.get('canonical_reference_exceptions')
  if not allowed or x.get('task_ids')!=allowed:return False
  if x.get('control_task_count')!=definition.get('required_task_count') or x.get('other_canonical_tasks_passed')!=definition['required_task_count']-len(allowed):return False
  if not all(x.get(k) is True for k in ('all_negative_controls_rejected','unchanged_official_oracle_and_dataset','full_task_set_independently_replayed')):return False
  if x.get('official_oracle_source_sha256')!=definition.get('scorer_version',{}).get('source_sha256'):return False
  if not all(re.fullmatch('[a-f0-9]{64}',str(x.get(k,''))) for k in ('calibration_sha256','source_review_sha256')):return False
 if proof.get('benchmark_identity_id')!=definition_identity(definition) or proof.get('dataset_split_hash')!=definition.get('dataset_split_hash'):return False
 if proof.get('scorer_version')!=definition.get('scorer_version') or proof.get('audit_hash')!=record['audit_hash']:return False
 if proof.get('runtime_configuration_id')!=record.get('runtime_configuration_id'):return False
 if proof.get('solved')!=record.get('solved') or proof.get('tasks')!=record.get('tasks'):return False
 metric=definition.get('metric')
 if metric=='pass_at_1_percent':
  fraction=proof.get('official_pass_at_1')
 elif metric=='bfcl_simple_python_ast_accuracy_percent':
  # This is one complete official category, never BFCL's overall aggregation.
  if definition.get('benchmark_id')!='bfcl-v4-simple-python-full400' or definition.get('required_task_count')!=400:return False
  if proof.get('official_category')!='simple_python' or proof.get('category_only') is not True:return False
  if type(proof.get('official_correct_count')) is not int or proof['official_correct_count']!=record.get('solved'):return False
  fraction=proof.get('official_category_accuracy')
 else:return False
 if not finite(fraction) or not 0<=fraction<=1:return False
 if type(record.get('tasks')) is not int or record['tasks']<=0 or type(record.get('solved')) is not int or not 0<=record['solved']<=record['tasks']:return False
 if not math.isclose(fraction,record['solved']/record['tasks'],rel_tol=1e-12,abs_tol=1e-12):return False
 if not math.isclose(100*fraction,record.get('score_percent',-1),rel_tol=1e-12,abs_tol=1e-12):return False
 count=definition.get('required_task_count')
 ids=proof.get('task_ids')
 if type(count) is not int or type(ids) is not list or len(ids)!=count or len(set(ids))!=count or record['tasks']!=count:return False
 if definition.get('expected_task_ids_hash') and H(sorted(ids))!=definition['expected_task_ids_hash']:return False
 return True

def frozen_merge(previous,incoming,key):
 result={x[key]:copy.deepcopy(x) for x in previous}
 for x in incoming:
  ident=x[key]
  if ident in result and result[ident]!=x:raise ValueError('Immutable public history changed: '+ident+'; add explicit versioned correction instead')
  result[ident]=copy.deepcopy(x)
 return list(result.values())

def safe_launch(launch,identities,sanitize):
 argv=launch.get('argv',[]);out=[];redacted=[];previous=None
 for i,arg in enumerate(argv):
  arg=str(arg)
  if arg.startswith('/'):
   value='[artifact:'+str(identities.get(arg) or hashlib.sha256(arg.encode()).hexdigest())+']';redacted.append(i)
   if i==0:value=pathlib.PurePosixPath(arg).name
  elif previous in ('--host','--port','--alias'):
   value='[session-local value]';redacted.append(i)
  else:value=sanitize(arg)
  out.append(value);previous=arg
 env=launch.get('environment',{})
 safe={}
 for k,v in env.items():
  if k in ('GGML_CUDA_GRAPH_OPT','GGML_CUDA_DISABLE_GRAPHS','GGML_CUDA_O2_WEIGHT_CACHE_MIB','GGML_CUDA_FORCE_MMQ','GGML_CUDA_FORCE_CUBLAS','OMP_NUM_THREADS') and re.fullmatch('[A-Za-z0-9_.+-]{1,50}',str(v)):safe[k]=v
 return {'argv':out,'environment':safe,'redacted_argument_positions':redacted,'exact_private_launch_sha256':H(launch),'note':'All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.'}

def profile(plan,launch,model,name,quantization,experiment,plan_sha,sanitize,metadata=None,origin=None):
 metadata=metadata or {};ident=plan.get('runtime_identities',plan.get('identities',{}));t=extract_tuning(plan,launch,ident)
 model_sha=t['executed_model_sha256'] or metadata.get('model_sha256') or plan.get('model_sha256')
 if not isinstance(model_sha,str) or not re.fullmatch('[a-f0-9]{64}',model_sha):model_sha=None
 artifact={'name':sanitize(name),'family_id':sanitize(model),'architecture':None,'variant':sanitize(plan.get('model_profile')),'hf_repository':(origin or {}).get('repository'),'hf_revision':(origin or {}).get('revision'),'artifact_sha256':model_sha,'quantization':sanitize(quantization),'tensor_precision_map':None,'weight_transformations':{'description':sanitize(t.get('artifact_state')),'proof':None,'caution':'Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.'}}
 artifact_id='artifact-'+H(artifact if model_sha else {**artifact,'unknown_identity_run':experiment})
 argv=launch.get('argv',[]);exe=next((pathlib.PurePosixPath(x).name for x in argv if pathlib.PurePosixPath(x).name in ['llama-server','llama-bench','ollama','qengine']),None)
 engine='Ollama' if exe=='ollama' else 'qengine' if exe=='qengine' else 'llama.cpp-compatible' if exe in ('llama-server','llama-bench') else None
 engine_sha=next((ident[x] for x in argv if x in ident and pathlib.PurePosixPath(x).name==exe),metadata.get('engine_binary_sha256'))
 flags=t['runtime_flags'];env=t['environment_knobs'];kwargs=metadata.get('chat_template_kwargs') or plan.get('chat_template_kwargs')
 launch_data=safe_launch(launch,ident,sanitize)
 cfg={'schema_version':SCHEMA,'model_artifact_id':artifact_id,'model':artifact,'engine':{'name':engine,'version':None,'git_commit':t['engine_source_commit'],'fork_repository':None,'build_id':t['engine_build_id'],'patches':None,'binary_sha256':engine_sha,'cuda_version':plan.get('cuda_version'),'driver_version':plan.get('driver_version'),'ggml_backend_version':None,'kernel_library_file':t['kernel_library'],'kernel_library_sha256':t['kernel_library_sha256'],'executed_kernel_backend_path':None},'optimizations':{'speculation_type':flags.get('--spec-type'),'draft_head_or_model':t.get('draft_artifact'),'draft_sha256':t.get('draft_model_sha256'),'draft_parameters':{k:v for k,v in flags.items() if k.startswith('--spec-')},'flash_attention_requested':flags.get('--flash-attn'),'cuda_graphs':{'optimization_knob':env.get('GGML_CUDA_GRAPH_OPT'),'disable_knob':env.get('GGML_CUDA_DISABLE_GRAPHS'),'actual_capture_replay':None},'KV_precision':{'k':flags.get('--cache-type-k'),'v':flags.get('--cache-type-v')},'GDN_state_changes':None,'HBM_conversion_weight_cache_limit_mib':env.get('GGML_CUDA_O2_WEIGHT_CACHE_MIB'),'prefix_reuse':metadata.get('context_and_runtime',{}).get('retain_prefix',plan.get('agent_workload',{}).get('retain_prefix')),'quantization_calibration':None,'other_explicit_knobs':env},'runtime':{'context':flags.get('--ctx-size',plan.get('fixed',{}).get('ctx')),'max_output':metadata.get('output_cap') or plan.get('maximum_output_tokens'),'thinking_reasoning_requested':flags.get('--reasoning'),'native_template_controls':kwargs,'sampling':metadata.get('sampling') or plan.get('source_sampling') or plan.get('coding_sampling') or None,'batch':flags.get('--batch-size'),'microbatch':flags.get('--ubatch-size'),'CPU_threads':flags.get('--threads'),'GPU_offload':flags.get('--n-gpu-layers'),'chat_template_sha256':metadata.get('template_sha256') or plan.get('template_sha256'),'tokenizer_identity':None,'power_limit_w':metadata.get('power_limit_w',plan.get('power_limit_w')),'CPU_budget':None,'RAM_budget':None,'VRAM_budget_mib':plan.get('maximum_device_vram_mib'),'execution_deadline_s':plan.get('maximum_model_seconds')},'start_parameters':launch_data,'source_plan_sha256':plan_sha,'provenance_status':'KNOWN_FIELDS_ONLY; null means NOT MEASURED','evaluation_exposure':'Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.'}
 # Never merge two unknown identities just because both use null placeholders.
 cfg['incomplete_identity_run']=experiment if not (model_sha and engine_sha) else None
 cfg['runtime_configuration_id']='cfg-'+H(cfg)
 return cfg

def native_coverage(parts,scores,expected):
 if len(expected)!=164 or len(set(expected))!=164 or len(parts)!=len(scores):raise ValueError('Incomplete native coding coverage')
 ids=[];solved=0
 for part,score in zip(parts,scores):
  if type(part['part']) is not int or type(score['tasks']) is not int or part['part']!=score['part'] or score['tasks']!=len(part['task_ids']) or type(score['solved']) is not int or not 0<=score['solved']<=score['tasks']:raise ValueError('Native part/score mismatch')
  ids.extend(part['task_ids']);solved+=score['solved']
 if ids!=expected or len(set(ids))!=164:raise ValueError('Native task set/order mismatch')
 return solved

def native_complete_run(root,source,cfg,bench,receipt):
 """Full broker coding results only. No code execution or implicit qualification."""
 if source.get('full_benchmark_score_claimed') is not True:return None
 root=pathlib.Path(root);path=pathlib.Path(source['audit_path']);path=path if path.is_absolute() else root/path
 if digest(path)!=source['audit_sha256']:raise ValueError('Native final audit changed')
 a=read(path);stage=root/'staging'/a['experiment_id'].lower();campaign=read(stage/'CAMPAIGN_PLAN.json')
 if a.get('full_benchmark_score_claimed') is not True or a['collected_tasks']!=164 or a['scored_tasks']!=164 or digest(stage/'CAMPAIGN_PLAN.json')!=a['campaign_plan_sha256']:raise ValueError('Native campaign not complete')
 if len(a['parts'])!=len(campaign['parts']) or len(a['parts'])!=campaign['part_count']:raise ValueError('Native partition manifest incomplete')
 expected=campaign['expected_task_ids'];solved=native_coverage(a['parts'],a['scoring'],expected)
 if bench.get('required_task_count')!=164 or H(sorted(expected))!=bench.get('expected_task_ids_hash') or solved!=a['scopes']['standard_full164']['solved']:raise ValueError('Native benchmark definition/count mismatch')
 if cfg['source_plan_sha256']!=a['campaign_plan_sha256'] or campaign['immutable_profile_identity_sha256']!=cfg['source_provenance']['frozen_model_profile_sha256']:raise ValueError('Native configuration lineage mismatch')
 audits=[receipt(path,source['audit_sha256'])];hashes=[source['audit_sha256']];wall=0;energies=[];peaks=[];first_launch=None;first_contract=None;helper=None
 for part,score,planned in zip(a['parts'],a['scoring'],campaign['parts']):
  if part['part']!=planned['index'] or part['job_id']!=planned['id'] or part['task_ids']!=planned['task_ids']:raise ValueError('Native campaign partition changed')
  ap=pathlib.Path(part['audit_path']);sp=pathlib.Path(score['audit_path'])
  if digest(ap)!=part['audit_sha256'] or digest(sp)!=score['audit_sha256']:raise ValueError('Native child audit changed')
  scored=read(sp)
  if scored['tasks']!=score['tasks'] or scored['solved']!=score['solved'] or scored['task_ids']!=part['task_ids']:raise ValueError('Native scoring summary changed')
  folder=ap.parent;observed=read(ap);pins=read(folder/'RAW_HASHES.json');launch=read(folder/'LAUNCH.json');native=read(folder/'profile.json');contract=read(folder/'CONTRACT.json')
  completed=read(folder/'HOST_COMPLETION.json')
  if completed.get('status')!='GPU_COMPLETE_AUDITED' or completed.get('starts')!=1 or completed.get('audit_sha256')!=part['audit_sha256']:raise ValueError('Native broker completion missing or changed')
  if observed.get('recovered_after_controller_exit_race'):
   if completed.get('recovered_after_controller_exit_race') is not True or digest(folder/'RECOVERY_REVIEW.json')!=completed.get('recovery_review_sha256') or observed.get('recovery_review_sha256')!=completed.get('recovery_review_sha256'):raise ValueError('Native recovered data review changed')
  for name,key in [('HTTP_RESULTS.jsonl','raw_answers_sha256'),('LAUNCH.json','launch_sha256'),('profile.json','profile_snapshot_sha256'),('CONTRACT.json','contract_sha256')]:
   if digest(folder/name)!=part[key] or pins[name]!=part[key]:raise ValueError('Native raw/source identity changed')
  if H({k:v for k,v in native.items() if k!='selected_task_inputs'})!=campaign['immutable_profile_identity_sha256'] or native.get('adapter')!='llama-native-coding':raise ValueError('Native model/profile drift')
  if launch['native_request_options']!=native['native_recipe']['request_options'] or launch['uid']!=65534 or observed.get('measurement_valid') is not True or observed.get('GPU_execution_observed') is not True:raise ValueError('Native execution not verified')
  stable_launch={'argv':launch['argv'],'environment':{k:v for k,v in launch['environment'].items() if k!='O2_GPU_BUILD_LEASE'}};stable_contract={k:v for k,v in contract.items() if k not in ('id','parameters')}
  if first_launch is None:first_launch=stable_launch;first_contract=stable_contract
  if stable_launch!=first_launch or stable_contract!=first_contract or contract['id']!=part['job_id'] or contract['parameters']['task_ids']!=part['task_ids'] or observed['case_ids']!=part['task_ids']:raise ValueError('Native launch/contract drift')
  judge=sp.parent/f"{a['experiment_id'].lower()}-judge-part{part['part']:02d}.stdout";plan=read(sp.parent/'SCORING_PLAN.json')
  if digest(judge)!=score['judge_stdout_sha256'] or digest(sp.parent/'JUDGE_SAMPLES.jsonl')!=score['judge_samples_sha256'] or digest(sp.parent/f"{a['experiment_id'].lower()}-judge-part{part['part']:02d}.receipt.json")!=score['judge_receipt_sha256']:raise ValueError('Native scorer output changed')
  if plan['raw_answers_sha256']!=part['raw_answers_sha256'] or plan['judge_samples_sha256']!=score['judge_samples_sha256']:raise ValueError('Native scorer input binding changed')
  if helper is None:helper=plan['helper_sha256']
  if plan['helper_sha256']!=helper:raise ValueError('Native scorer changed across parts')
  if not finite(observed['case_inference_wall_s']) or observed['case_inference_wall_s']<=0 or observed['case_gpu_energy_j'] is not None and (not finite(observed['case_gpu_energy_j']) or observed['case_gpu_energy_j']<0):raise ValueError('Native cost measurement invalid')
  decisions=[json.loads(line) for line in judge.read_text().splitlines()]
  if [d['task_id'] for d in decisions]!=part['task_ids'] or sum(d['checks']['base']['status']==d['checks']['plus']['status']=='pass' for d in decisions)!=score['solved']:raise ValueError('Native judgments/count mismatch')
  wall+=observed['case_inference_wall_s'];energies.append(observed['case_gpu_energy_j']);peaks.append(observed['peak_device_vram_mib'])
  for p,h in [(ap,part['audit_sha256']),(sp,score['audit_sha256'])]:audits.append(receipt(p,h));hashes.append(h)
 if not all(audits):raise ValueError('Native public audit reference missing')
 energy=sum(energies) if all(v is not None for v in energies) else None;scope=a['scopes']['standard_full164']
 if scope['tasks']!=164 or not math.isclose(scope['wall_s'],wall,rel_tol=1e-10) or (scope['gpu_energy_j'] is None)!=(energy is None) or energy is not None and not math.isclose(scope['gpu_energy_j'],energy,rel_tol=1e-10):raise ValueError('Native aggregate costs mismatch')
 return {'record_schema_version':SCHEMA,'benchmark_id':bench['benchmark_id'],'benchmark_identity_id':definition_identity(bench),'benchmark_revision':bench['benchmark_revision'],'dataset_split_hash':bench['dataset_split_hash'],'evaluated_task_set_hash':campaign['source_workload_sha256'],'scorer_version':{'adapter_sha256':helper},'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':a['experiment_id'],'audit_hash':source['audit_sha256'],'audit_ids':audits,'source_audit_hashes':hashes,'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'discipline':'coding','tasks':164,'solved':solved,'score_percent':100*solved/164,'metric':'observed_success_percent','wall_s':wall,'gpu_j':energy,'gpu_j_per_success':energy/solved if energy is not None and solved else None,'peak_vram_mib':max(peaks),'repeat_range':None,'date':a['at_utc'][:10],'status':'FULL_NATIVE_CODING_OFFICIAL_API_PENDING','status_reason':'All164 original answers and per-part scoring/costs verified; independent official API qualification is separate.','official_eligible':False,'qualification_audit':None,'warning':'Declared native template/sampling and local output/context limits apply. No publisher-protocol equivalence, model superiority or causal optimization benefit is implied. Monitoring corrections and data recovery remain in original audit lineage.','causal_optimization_proof':None,'measurement_conditions':{'hardware':'Tesla V100-SXM2 16 GB HBM2','cache_condition':'Completion HTTP intervals; startup, warmups and CPU evaluation excluded; see original per-request cache setting.','date':a['at_utc'][:10],'output_cap':cfg['runtime']['max_output'],'sampling':cfg['runtime']['sampling'],'power_limit_w':cfg['runtime']['power_limit_w']}}

def build(root,db,comparison,experiments,receipt,sanitize,previous):
 root=pathlib.Path(root);reg=read(root/'BENCHMARK_REGISTER.json');profiles=[];runs=[];defs={d['benchmark_id']:d for d in reg['definitions']}
 for event in reg.get('local_validation_events',[]):
  if event.get('kind')=='BFCL_FULL400_CATEGORY_DEFINITION_ADMISSION':
   path=root/event['audit_path']
   event['audit_id']=receipt(path,event['audit_sha256'])
   if not event['audit_id']:raise ValueError('Benchmark definition source audit unavailable')
   event.pop('audit_path')
 for audit in db['summary'].get('official_api_replay_verification',{}).get('audits',[]):
  ident=receipt(audit['path'],audit['sha256'])
  if not ident:raise ValueError('Official API replay audit unavailable')
 origins={}
 for path in (root/'staging/model-comparison-preparation').glob('*/MODEL_FILE_PROVENANCE.json'):
  a=read(path);h=a.get('actual_sha256') or a.get('sha256');u=a.get('source_url') or a.get('url');m=re.match(r'https://huggingface.co/([^/]+/[^/]+)/resolve/([a-f0-9]{40})/',str(u))
  if h and m:origins[h]={'repository':m[1],'revision':m[2]}
 def get_launch(plan,path,expected_audit):
  launch=plan.get('launch',{});candidate=path.parent/'LAUNCH.json';pins=read(path.parent/'RAW_HASHES.json') if (path.parent/'RAW_HASHES.json').is_file() else {}
  if candidate.is_file() and pins.get('LAUNCH.json')==digest(candidate):launch=read(candidate)
  return launch
 def add_profile(p,l,model,name,quant,exp,psha,m=None):
  ids=p.get('runtime_identities',p.get('identities',{}));t=extract_tuning(p,l,ids);orig=origins.get(t.get('executed_model_sha256'))
  cfg=profile(p,l,model,name,quant,exp,psha,sanitize,m,orig);profiles.append(cfg);return cfg
 def qualify(run,bench):
  for admission in reg.get('official_qualifications',[]):
   if admission.get('source_audit_hash')==run['audit_hash'] and admission.get('evaluated_task_set_hash')==run['evaluated_task_set_hash']:
    proof_file=root/admission['proof_path']
    if digest(proof_file)!=admission['proof_sha256']:raise ValueError('Official qualification proof modified')
    proof=read(proof_file)
    candidate={**run,'scorer_version':bench.get('scorer_version'),'metric':bench.get('metric')} if bench else run
    if not bench or not official_gate(candidate,bench,proof):raise ValueError('Invalid official qualification')
    run.update(scorer_version=bench['scorer_version'],metric=bench['metric'],official_eligible=True,qualification_audit=proof,qualification_audit_id=receipt(proof_file,admission['proof_sha256']),status='FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED',status_reason='Full official scorer/API task set independently verified; declared local evaluation limits and any pinned upstream reference anomaly remain visible.',scorer_execution_limits=proof.get('scorer_execution_limits'),warning=' '.join(x for x in [run['warning'],proof.get('disclosure')] if x) or None)
 for row in comparison['records']:
  pn=int(row['id'].rsplit('-',1)[-1]);pfile=root/f'staging/r{pn}/PLAN.json';p=read(pfile)
  source=db['summary'].get(row['experiment'].lower(),{});afile=pathlib.Path(source.get('audit_path',''));afile=afile if afile.is_absolute() else root/afile
  launch=get_launch(p,afile,row['audit_sha256'][0])
  for file,h in (read(afile).get('evidence',{}) if afile.is_file() else {}).items():
   if file.startswith(f'staging/r{pn}/measurements/') and file.endswith('/launch.json'):
    file=root/file
    if digest(file)!=h:raise ValueError('Historical launch modified')
    launch=read(file);break
  cfg=add_profile(p,launch,row['model'],row['name'],row['quantization'],row['experiment'],digest(pfile),row['metadata'])
  classification=reg['local_cohort_classification'].get(row['discipline'],{'benchmark_id':'local-'+row['discipline'],'status':'LOCAL_LAB_ONLY','reason':'Not an official benchmark definition.'})
  bench=defs.get(classification['benchmark_id']);bid=definition_identity(bench) if bench else 'local-'+row['task_sha256']
  scorer={'official_evalplus_provenance_sha256':row['metadata'].get('official_evalplus_provenance_sha256'),'adapter_sha256':row['metadata'].get('scorer_adapter_sha256')}
  run={'record_schema_version':SCHEMA,'benchmark_id':classification['benchmark_id'],'benchmark_identity_id':bid,'benchmark_revision':bench.get('benchmark_revision') if bench else None,'dataset_split_hash':bench.get('dataset_split_hash') if bench else None,'evaluated_task_set_hash':row['task_sha256'],'scorer_version':scorer,'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':row['experiment'],'audit_hash':row['audit_sha256'][0],'audit_ids':row['audit_ids'],'source_audit_hashes':row['audit_sha256'],'model_family_id':row['model'],'model_name':row['name'],'discipline':row['discipline'],'tasks':row['tasks'],'solved':row['solved'],'score_percent':100*row['solved']/row['tasks'],'metric':'observed_success_percent','wall_s':row['wall_s'],'gpu_j':row['gpu_j'],'gpu_j_per_success':row['gpu_j']/row['solved'] if row['gpu_j'] is not None and row['solved'] else None,'peak_vram_mib':row['peak_vram_mib'],'repeat_range':row['repeat_range'],'date':row['metadata']['date'],'status':classification['status'],'status_reason':classification['reason'],'official_eligible':False,'qualification_audit':None,'warning':row['warning'],'causal_optimization_proof':None}
  run['measurement_conditions']={k:row['metadata'].get(k) for k in ('hardware','cache_condition','date','output_cap','sampling','power_limit_w')}
  qualify(run,bench)
  run['run_id']='run-'+H(run);runs.append(run)
 # Preserve additional executed/failed configurations, not only chart-selected winners.
 byexp={e['id']:e for e in experiments};history_attempts=[];gaps=[]
 for key,a in db['summary'].items():
  if not re.fullmatch('r[0-9]+',key) or not isinstance(a,dict) or not a.get('audit_path') or not a.get('audit_sha256'):continue
  exp=key.upper();pfile=root/f'staging/{key}/PLAN.json'
  if not pfile.is_file():continue
  p=read(pfile);path=pathlib.Path(a['audit_path']);path=path if path.is_absolute() else root/path
  if not path.is_file() or digest(path)!=a['audit_sha256']:raise ValueError('Configuration history audit changed')
  raw=read(path);e=byexp.get(exp,{})
  hp=path.parent/'HOST_PRECHECK.json'
  plan_pin=(read(hp).get('plan_sha256') if hp.is_file() else None) or raw.get('evidence',{}).get(str(pfile.relative_to(root)))
  if plan_pin and digest(pfile)!=plan_pin:
   gap={'experiment_id':exp,'reason':'Current historical plan differs from its original precheck pin; configuration not reconstructed from mismatched bytes. Original audit remains preserved.','expected_plan_sha256':plan_pin,'observed_plan_sha256':digest(pfile),'original_audit_sha256':a['audit_sha256'],'audit_id':receipt(path,a['audit_sha256'])}
   gap['gap_id']='gap-'+H(gap);gaps.append(gap);continue
  observed=any(type(raw.get(k)) is int and raw[k]>0 for k in ['model_starts','model_inference_starts','actual_generation_requests','coding_requests'])
  if not observed and not p.get('launch',{}).get('argv'):continue
  launches=[];pins=read(path.parent/'RAW_HASHES.json') if (path.parent/'RAW_HASHES.json').is_file() else {}
  direct=path.parent/'LAUNCH.json'
  if direct.is_file() and pins.get('LAUNCH.json')==digest(direct):launches.append(read(direct))
  for rel,h in raw.get('evidence',{}).items():
   if rel.startswith('staging/'+key+'/measurements/') and rel.endswith('/launch.json'):
    lp=root/rel
    if digest(lp)!=h:raise ValueError('History arm launch pin mismatch')
    launches.append(read(lp))
  if not launches:launches=[p.get('launch',{})]
  for index,l in enumerate(launches):
   ident=p.get('runtime_identities',p.get('identities',{}));t=extract_tuning(p,l,ident);matches=[r for r in comparison['records'] if r['metadata']['model_sha256']==t.get('executed_model_sha256') and t.get('executed_model_sha256')]
   first=matches[0] if matches else None;model=first['model'] if first else str(e.get('model') or p.get('model') or 'UNKNOWN');name=first['name'] if first else str(e.get('model') or p.get('model') or 'NOT MEASURED');quant=first['quantization'] if first else 'NOT MEASURED'
   if not t.get('weight_artifact') and not p.get('model_sha256'):continue
   cfg=add_profile(p,l,model,name,quant,exp,digest(pfile))
   attempt={'experiment_id':exp,'arm_index':index,'runtime_configuration_id':cfg['runtime_configuration_id'],'model_family_id':model,'model_name':sanitize(name),'audit_hash':a['audit_sha256'],'audit_id':receipt(path,a['audit_sha256']),'execution_status':'INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED' if observed else 'ATTEMPT_OR_DECLARED_PLAN_NOT_PROVEN_EXECUTED','scientific_status':sanitize(a.get('decision')),'lab_metrics':e.get('aggregate_metrics',{}),'official_eligible':False}
   attempt['attempt_id']='attempt-'+H(attempt);history_attempts.append(attempt)
 # Broker-native campaigns have captured contracts/launches rather than a
 # retrospective PLAN.json. Record their actual profile without a full score.
 for key,a in db['summary'].items():
  if not re.fullmatch('r[0-9]+',key) or not isinstance(a,dict) or not a.get('runtime_configuration_profile_path'):continue
  cp=pathlib.Path(a['runtime_configuration_profile_path']);cp=cp if cp.is_absolute() else root/cp
  if not cp.resolve().is_relative_to(root.resolve()) or digest(cp)!=a['runtime_configuration_profile_sha256']:raise ValueError('Broker configuration receipt changed')
  cfg=read(cp);first=a['parts'][0];ap=pathlib.Path(first['audit_path']);ap=ap if ap.is_absolute() else root/ap
  if digest(ap)!=first['audit_sha256'] or cfg['source_provenance']['first_part_collection_audit_sha256']!=first['audit_sha256']:raise ValueError('Broker first collection audit changed')
  pins=read(ap.parent/'RAW_HASHES.json');lp=ap.parent/'LAUNCH.json';np=ap.parent/'profile.json'
  if digest(lp)!=pins['LAUNCH.json'] or digest(np)!=pins['profile.json']:raise ValueError('Broker captured source changed')
  contract=ap.parent/'CONTRACT.json'
  if digest(contract)!=cfg['source_provenance']['first_part_contract_sha256']:raise ValueError('Broker contract changed')
  limits=read(contract)
  if cfg['runtime']['power_limit_w']!=limits['power_w'] or cfg['runtime']['VRAM_budget_mib']!=limits['vram_mib'] or cfg['runtime']['execution_deadline_s']!=limits['runtime_seconds']:raise ValueError('Broker configuration limits mismatch')
  verify_broker_capture(cfg,read(np),read(lp));validate_history({'profiles':[cfg],'runs':[],'attempts':[]},{})
  audit=read(ap)
  if audit.get('measurement_valid') is not True or audit.get('GPU_execution_observed') is not True:raise ValueError('Broker GPU execution not proven')
  profiles.append(cfg)
  attempt={'experiment_id':key.upper(),'arm_index':0,'runtime_configuration_id':cfg['runtime_configuration_id'],'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'audit_hash':first['audit_sha256'],'audit_id':receipt(ap,first['audit_sha256']),'execution_status':'INFERENCE_OBSERVED_IN_BROKER_CAMPAIGN; FULL_BENCHMARK_NOT_IMPLIED','scientific_status':'BOUNDED_NATIVE_EXECUTION_OBSERVED','lab_metrics':{},'official_eligible':False}
  if not attempt['audit_id']:raise ValueError('Broker source audit unavailable for public export')
  attempt['attempt_id']='attempt-'+H(attempt);history_attempts.append(attempt)
  bench=defs[reg['local_cohort_classification']['coding']['benchmark_id']]
  complete=native_complete_run(root,a,cfg,bench,receipt)
  if complete:
   qualify(complete,bench);complete['run_id']='run-'+H(complete);runs.append(complete)
 prior=previous or {'profiles':[],'runs':[],'attempts':[]}
 result={'schema_version':SCHEMA,'profiles':frozen_merge(prior['profiles'],profiles,'runtime_configuration_id'),'runs':frozen_merge(prior['runs'],runs,'run_id'),'attempts':frozen_merge(prior['attempts'],history_attempts,'attempt_id'),'provenance_gaps':frozen_merge(prior.get('provenance_gaps',[]),gaps,'gap_id')}
 validate_history(result,defs)
 return reg,result

def validate_history(data,defs):
 profiles={p['runtime_configuration_id']:p for p in data['profiles']};seen=set()
 if len(profiles)!=len(data['profiles']):raise ValueError('Duplicate immutable configuration')
 for r in data['runs']:
  if r['run_id'] in seen:raise ValueError('Duplicate benchmark run')
  seen.add(r['run_id'])
  if r['run_id']!='run-'+H({k:v for k,v in r.items() if k!='run_id'}):raise ValueError('Run content identity mismatch')
  if r['runtime_configuration_id'] not in profiles:raise ValueError('Missing immutable configuration')
  if type(r['tasks']) is not int or type(r['solved']) is not int or not 0<=r['solved']<=r['tasks'] or r['tasks']==0:raise ValueError('Invalid observed counts')
  if r['model_artifact_id']!=profiles[r['runtime_configuration_id']]['model_artifact_id']:raise ValueError('Model artifact/profile mismatch')
  if not math.isclose(r['score_percent'],100*r['solved']/r['tasks'],rel_tol=1e-12):raise ValueError('Unauthorized score conversion')
  if not re.fullmatch('[a-f0-9]{64}',r['audit_hash']):raise ValueError('Missing original audit identity')
  if r['official_eligible']:
   d=defs.get(r['benchmark_id'])
   if not d or not official_gate(r,d,r.get('qualification_audit')):raise ValueError('Unqualified official highscore')
   p=profiles[r['runtime_configuration_id']]
   if not all(re.fullmatch('[a-f0-9]{64}',str(v or '')) for v in (p['model']['artifact_sha256'],p['engine']['binary_sha256'])):raise ValueError('Official run missing exact model/engine identity')
 for p in profiles.values():
  if not p.get('model_artifact_id') or not p.get('source_plan_sha256'):raise ValueError('Configuration identity incomplete')
  if p['runtime_configuration_id']!='cfg-'+H({k:v for k,v in p.items() if k!='runtime_configuration_id'}):raise ValueError('Configuration content identity mismatch')
 for a in data['attempts']:
  if a['runtime_configuration_id'] not in profiles:raise ValueError('Orphan configuration attempt')
  if a['attempt_id']!='attempt-'+H({k:v for k,v in a.items() if k!='attempt_id'}):raise ValueError('Attempt identity mismatch')
 return True

def pair_delta(a,b):
 keys=['benchmark_identity_id','evaluated_task_set_hash','scorer_version','tasks']
 if any(a[k]!=b[k] for k in keys):return {'comparable':False,'reason':'Different benchmark/task set/scorer/count; no delta calculated.'}
 def percent(x,y):return (y/x-1)*100 if finite(x) and finite(y) and x>0 else None
 return {'comparable':True,'quality_delta_pp':b['score_percent']-a['score_percent'],'latency_delta_percent':percent(a.get('wall_s'),b.get('wall_s')),'energy_per_success_delta_percent':percent(a.get('gpu_j_per_success'),b.get('gpu_j_per_success')),'interpretation':'Whole-profile comparison. No causal optimization claim without a dedicated independent audit.'}

def render(register,history,comparison,docs,model_registry=None):
 """Offline pages and immutable profile detail routes, independent of matrix revision."""
 docs=pathlib.Path(docs);assets=docs/'assets/benchmarks';assets.mkdir(parents=True,exist_ok=True)
 def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
 def pretty(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2).replace('</','<\\/')
 def table(headers,rows):
  def cell(x):return str(x if x is not None else 'NOT MEASURED').replace('|','&#124;').replace('\n',' ')
  return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(cell(c) for c in row)+' |\n' for row in rows)+'\n'
 def audit_links(ids,prefix=''):return ', '.join('['+i+']('+prefix+'audits/'+i+'.md)' for i in ids if i)
 # Retain the existing figures/observations, but remove the mixed partial-suite mean.
 legacy=(docs/'benchmarks.md').read_text()
 start=legacy.find('## Official benchmark results and overall mean');end=legacy.find('## Configuration parameters and ranked benchmark results')
 if start>=0 and end>start:legacy=legacy[:start]+legacy[end:]
 legacy=legacy.replace('# Model Comparison & Benchmarks','# Supplemental model comparisons',1).replace('Official benchmark categories, exact tuning profiles and an explicitly defined percentage mean on one V100.','Historical local cohorts and exact tuning profiles; these are not official highscores.').replace('Each row is one audited official-benchmark discipline/profile.','Each row is one audited supplemental discipline/profile.').replace('They are excluded from the overall mean.','No combined score is calculated.').replace('- The overall mean is user-defined; complete selected-set coverage is required. No automatic deployment winner.','- No cross-benchmark mean: subsets and scorer exceptions cannot form an official ranking.')
 notice='\n> **SUPPLEMENTAL / HISTORICAL EVIDENCE.** BFCL static100 and MBPP+223 are frozen subsets. Original HumanEval+ records retain their historical scope here; independently verified full164 API admissions appear in [official local highscores](benchmarks.md), with the unchanged upstream reference anomaly and local evaluation limits disclosed. No combined percentage mean is calculated.\n\n'
 legacy=legacy.replace('- The user-defined mean uses the same complete selected benchmark set for every ranked row; it is not an official combined leaderboard score.','- No mean is calculated across subsets or incompatible protocols.')
 legacy=legacy.replace('\n\n','\n\n'+notice,1)
 write(docs/'supplemental-comparison.md',legacy)
 local=docs/'local-benchmarks.md';text=local.read_text().replace('do not contribute to the official-category percentage mean','are excluded from official highscores; no combined mean is calculated');write(local,text)
 page='# Model Comparison & Benchmarks\n\n<div class="hero"><strong>One result. One exact configuration. One verified protocol.</strong><p>Local official highscores, with full provenance. Publisher claims and laboratory subsets stay separate.</p></div>\n\n'
 page+='Only complete runs passing the task-set, official-scorer, canonical-control and independent-audit gates enter these rankings. **NOT MEASURED** means no eligible result, not zero ability. Different benchmark versions never share a ranking. No cross-discipline overall score is calculated.\n\n'
 page+='**Local official-benchmark API track.** This is an independent project ranking, not an entry on the benchmark authors’ leaderboard. Full164 HumanEval+ admissions preserve the exact official checker and pass@1 estimator through a streaming API adapter. The unchanged upstream HumanEval/32 canonical-reference residual anomaly is explicitly accounted for, with no dropped tasks or relaxed tolerance. Local scorer limits are 1GiB cgroup memory,805306368-byte per-process guard,one CPU,minimum1s/case and GT factor4. Publisher-protocol equivalence is not established. Scores are fixed-suite observations, not proof of overall model superiority.\n\n'
 page+='**[All results & tuning configurations — searchable, sortable table](configuration-comparison.md#all-measured-results)** · [Historical detailed cohort table](supplemental-comparison.md#configuration-parameters-and-ranked-benchmark-results)\n\n'
 page+='<div id="official-leaderboard" aria-live="polite"></div>\n\n'
 eligible=[r for r in history['runs'] if r['official_eligible']]
 page+='## Current admission status\n\n'+str(len(eligible))+' eligible official runs under the declared local protocol. '+str(len(history['runs']))+' versioned result records remain available in the [configuration comparison](configuration-comparison.md); these include preserved historical admission/protocol revisions of the same physical measurements. '+str(len(history['profiles']))+' content-addressed profiles and '+str(len(history['attempts']))+' additional audited configuration attempts are preserved; these are **not** counts of qualified optimizations or distinct GPU jobs. [Historical and subset comparisons](supplemental-comparison.md) remain accessible.\n\n'
 page+=table(['Original local cohort classification','Historical scope','Reason before separate admission'],[[k,v['status'],v['reason']] for k,v in register['local_cohort_classification'].items()])
 page+='## Next evidence gaps\n\n'+table(['Priority','Technical decision / next step','GPU initially required'],[[x['priority'],x['action'],x.get('GPU_required_initially')] for x in register['next_test_priorities']])
 page+='[Benchmark definitions and publisher evidence](benchmark-register.md) · [Local agent and synthetic tests](local-benchmarks.md) · [Reproduction](reproduce.md)\n\nEach profile records unknown fields as null (**NOT MEASURED**). An absent MTP/graph/cache setting is never assumed off. No-MTP execution does not establish that weights are original. Actual kernel execution is distinct from a requested backend. Historical development suites were reused; no unseen-holdout or absence-of-overfitting claim is made.\n'
 write(docs/'benchmarks.md',page)
 page='# All Results & Configurations\n\n## All measured results\n\nOne row per measured configuration. Tuning parameters are on the left; HumanEval+, BFCL and MBPP+ results are on the right. **Asterisk: subset. Dagger: historical scorer protocol.** Unmarked values passed the declared local official-benchmark admission. Click a model for full parameters, metrics and audits. Additional tuning columns are optional. No combined score. Unknown values remain **NOT MEASURED**.\n\n<div id="all-measured-results" aria-live="polite"></div>\n\n## Compare selected configurations\n\nSelect two or more **measured result profiles**, including weaker configurations. Differences describe complete tested profiles. A causal claim about MTP, quantization or another factor requires a dedicated isolated experiment.\n\n<div id="configuration-comparison" aria-live="polite"></div>\n\n## Full configuration history\n\nThe searchable history also contains failed or declared attempts, clearly distinguished from observed inference. An attempt without benchmark output is not a scored run. Missing fields remain **NOT MEASURED**.\n\n<div id="configuration-history"></div>\n\n'
 page+='Machine-readable [configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) is append-only. Changed metadata require a new profile identity; old results and original audit hashes remain retained.\n'
 page+='\n## Provenance gaps — excluded from reconstructed profiles\n\n'+table(['Experiment','Reason','Original audit'],[[g['experiment_id'],g['reason'],audit_links([g['audit_id']])] for g in history.get('provenance_gaps',[])])
 write(docs/'configuration-comparison.md',page)
 profiles={p['runtime_configuration_id']:p for p in history['profiles']}
 # Remove only stale generated previews; append-only ledger profiles remain retained.
 for stale in (docs/'configuration-profiles').glob('cfg-*.md'):
  if re.fullmatch(r'cfg-[a-f0-9]{64}',stale.stem) and stale.stem not in profiles:stale.unlink()
 for ident,p in profiles.items():
  runs=[r for r in history['runs'] if r['runtime_configuration_id']==ident];attempts=[a for a in history['attempts'] if a['runtime_configuration_id']==ident]
  s='# '+str(p['model']['name'])+' · '+ident[:16]+'\n\n[Back to configuration comparison](../configuration-comparison.md)\n\nProfile ID: `'+ident+'`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.\n\n'
  for title,key in [('Model and weights','model'),('Engine and backend','engine'),('Optimizations','optimizations'),('Runtime and sampler','runtime'),('Ordered startup parameters','start_parameters')]:
   s+='## '+title+'\n\n```json\n'+pretty(p[key])+'\n```\n\n'
  s+='## Results and original audits\n\n'+table(['Experiment','Benchmark / scope','Success','Wall s','GPU J / success','Peak VRAM MiB','Original audits'],[[r['experiment_id'],r['benchmark_id']+' / '+r['status'],str(r['solved'])+'/'+str(r['tasks']),r['wall_s'],r['gpu_j_per_success'],r['peak_vram_mib'],audit_links(r['audit_ids'],'../')] for r in runs])
  s+='Separate benchmark qualification audits: '+audit_links([r.get('qualification_audit_id') for r in runs],'../')+'\n\n'
  s+=table(['Experiment / arm','Execution evidence','Scientific decision','Original audit'],[[a['experiment_id']+' / '+str(a['arm_index']),a['execution_status'],a['scientific_status'],audit_links([a['audit_id']],'../')] for a in attempts])
  s+='## Immutable full profile and measurements\n\n```json\n'+pretty({'profile':p,'runs':runs,'attempts':attempts})+'\n```\n'
  write(docs/'configuration-profiles'/(ident+'.md'),s)
 page='# Benchmark register and publisher evidence\n\n**EXTERNAL PUBLISHER SELF-REPORTS are not local measurements.** A mention on a model card does not establish the dataset version, scorer, scaffold or hardware equivalence. HumanEval is distinct from HumanEval+; BFCL v3 is distinct from v4.\n\n'
 for d in register['definitions']:
  page+='## '+d['name']+'\n\n'+table(['Field','Pinned definition'],[[k,json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v] for k,v in d.items() if k not in ('expected_task_ids','model_card_references')])
  page+='Model-card sources: '+', '.join('['+m['model_repository']+']('+m['url']+')' for m in d.get('model_card_references',[]))+'\n\n'
 page+='## Verified cached model cards\n\n'+table(['Model','Revision / source SHA256','Reported benchmark families','Architecture declared by source','Card'],[[m['model_repository'],str(m.get('revision'))+' / '+m['source_sha256'],', '.join(m['benchmark_mentions']),json.dumps(m.get('architecture')),'[source]('+m['url']+')'] for m in register['model_card_evidence']])
 page+='## Publisher numeric claims — never local highscores\n\nReported numeric cells retain the publisher’s scale. Protocol matching and local reproducibility remain unverified; no conversion to local percentage or cross-model ranking is performed.\n\n'+table(['Model / publisher column','Reported label','Reported value','Scale / comparability','Source'],[[c['model_repository']+' / '+c['column_label'],c['benchmark_label'],c['reported_score'],c['score_unit']+' / '+c['benchmark_definition_match'],'[card]('+c['source_url']+')'] for c in register['publisher_claims']])
 page+='## Independent CPU replay of archived model answers\n\nThese are verification events for existing measurements, **not new GPU runs**. Official scoring functions and pass@1 aggregation were replayed through a streaming API adapter, preserving all164 tasks and the known upstream canonical-reference exception. The full optional CLI was not used; evaluation memory limits remain explicitly local. This verifies archived judgments without implying publisher-protocol equivalence or automatic official highscore qualification.\n\n'+table(['Original experiment','Full task coverage','Confirmed successes','Changed judgments','Verification audit'],[[x['experiment_id'],x['tasks'],x['solved'],x.get('changed_judgements'),audit_links([x['audit_id']])] for x in register.get('local_validation_events',[]) if x.get('experiment_id') and x.get('tasks')==164])
 page+='## Unreachable / unresolved model-card identities\n\n```json\n'+pretty(register['unreachable_model_cards'])+'\n```\n\n## Source retrieval receipts\n\n```json\n'+pretty(register['source_checks'])+'\n```\n'
 page+='\n## Transparent admission-policy corrections\n\n'+table(['Previous definition identity','Correction / preserved boundaries'],[[x.get('previous_identity') or (definition_identity(x['previous_definition']) if x.get('previous_definition') else 'NOT RECORDED'),x.get('correction') or x.get('reason') or 'NOT RECORDED'] for x in register.get('definition_history',[])])
 definitions=[x for x in register.get('local_validation_events',[]) if x.get('kind')=='BFCL_FULL400_CATEGORY_DEFINITION_ADMISSION']
 if definitions:page+='## Source and definition checks — no model results\n\n'+table(['Verification','Date','New GPU runs','Model results admitted','Source audit'],[[x['kind'],x.get('at_utc'),x.get('GPU_runs'),x.get('model_results_admitted'),audit_links([x['audit_id']]) if x.get('audit_id') else 'Audit link pending export'] for x in definitions])
 write(docs/'benchmark-register.md',page)
 reproduce=docs/'reproduce.md'
 if reproduce.is_file():
  write(reproduce,reproduce.read_text()+'\n## Official benchmark admission and immutable profiles\n\n`data/benchmark-register.json` pins benchmark definitions, task manifests where verified, scorer identities, primary-source receipts and separate publisher claims. `data/configuration-history.json` retains content-addressed profiles, measured groups, failed/declared attempts and explicit provenance gaps. Null fields mean **NOT MEASURED**.\n\nOfficial admission requires an independently audited full task manifest, exact dataset/scorer/configuration/audit identities and validated protocol/controls. Unsupported official metric aggregations require their own adapter. Subsets, canonical-reference exceptions and local tests remain supplemental until resolved through a separate qualification audit. Corrections append a new result/profile; original audits and earlier scores remain preserved.\n\nThe existing documentation publisher fingerprints the canonical benchmark register as well as the research matrix/reference ledger. It regenerates offline views, checks immutable history, task counts, hashes, links and public confidentiality before committing/pushing. Bounded publication retries do not block research; neither export nor GitHub Actions launches GPU jobs. Historical task exposure is disclosed, and parameter tuning belongs on development data.\n\nUse the existing export → render → unit tests → public validation → strict MkDocs sequence. Charts and profile comparisons use only bundled JSON/JavaScript/SVG; no external chart service is required. Whole-profile deltas are descriptive and do not establish the causal effect of an individual optimization.\n')
 models=list(comparison['models']);aliases={'ornith':'BMC01','bonsai':'BMC04','oxcoder':'BMC02','lfm':'BMC06','gemma4':'BMC07'};covered={aliases[x['id']] for x in models if x['id'] in aliases}
 models += [{'id':m['id'],'name':m['name'],'quantization':'NOT MEASURED'} for m in (model_registry or []) if m['id'] not in covered]
 payload={'register':register,'history':history,'models':models}
 write(assets/'leaderboard-data.js','window.V100Leaderboard='+json.dumps(payload,ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')+';\n')
