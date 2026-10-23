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
 cfg={'schema_version':SCHEMA,'model_artifact_id':artifact_id,'model':artifact,'engine':{'name':engine,'version':plan.get('engine_version'),'git_commit':t['engine_source_commit'],'fork_repository':None,'build_id':t['engine_build_id'],'patches':None,'binary_sha256':engine_sha,'cuda_version':plan.get('cuda_version'),'driver_version':plan.get('driver_version'),'ggml_backend_version':None,'kernel_library_file':t['kernel_library'],'kernel_library_sha256':t['kernel_library_sha256'],'executed_kernel_backend_path':None},'optimizations':{'speculation_type':flags.get('--spec-type'),'draft_head_or_model':t.get('draft_artifact'),'draft_sha256':t.get('draft_model_sha256'),'draft_parameters':{k:v for k,v in flags.items() if k.startswith('--spec-')},'flash_attention_requested':flags.get('--flash-attn'),'cuda_graphs':{'optimization_knob':env.get('GGML_CUDA_GRAPH_OPT'),'disable_knob':env.get('GGML_CUDA_DISABLE_GRAPHS'),'actual_capture_replay':None},'KV_precision':{'k':flags.get('--cache-type-k'),'v':flags.get('--cache-type-v')},'GDN_state_changes':None,'HBM_conversion_weight_cache_limit_mib':env.get('GGML_CUDA_O2_WEIGHT_CACHE_MIB'),'prefix_reuse':metadata.get('context_and_runtime',{}).get('retain_prefix',plan.get('agent_workload',{}).get('retain_prefix')),'quantization_calibration':None,'other_explicit_knobs':env},'runtime':{'context':flags.get('--ctx-size',plan.get('fixed',{}).get('ctx')),'max_output':metadata.get('output_cap') or plan.get('maximum_output_tokens'),'thinking_reasoning_requested':flags.get('--reasoning'),'native_template_controls':kwargs,'sampling':metadata.get('sampling') or plan.get('source_sampling') or plan.get('coding_sampling') or None,'batch':flags.get('--batch-size'),'microbatch':flags.get('--ubatch-size'),'CPU_threads':flags.get('--threads'),'GPU_offload':flags.get('--n-gpu-layers'),'chat_template_sha256':metadata.get('template_sha256') or plan.get('template_sha256'),'tokenizer_identity':None,'power_limit_w':metadata.get('power_limit_w',plan.get('power_limit_w')),'CPU_budget':None,'RAM_budget':None,'VRAM_budget_mib':plan.get('maximum_device_vram_mib'),'execution_deadline_s':plan.get('maximum_model_seconds')},'start_parameters':launch_data,'source_plan_sha256':plan_sha,'provenance_status':'KNOWN_FIELDS_ONLY; null means NOT MEASURED','evaluation_exposure':'Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.'}
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

def native_job_id(stage,a,planned,part):
 """Resolve only a pinned, proven pre-GPU failed attempt; never hide a rerun."""
 if part['job_id']==planned['id']:return planned['id']
 meta=a.get('execution_attempts') or {};path=stage/'EXECUTION_ATTEMPTS.json'
 if meta.get('path')!=str(path) or not path.exists() or digest(path)!=meta.get('sha256'):raise ValueError('Native execution replacement ledger missing or changed')
 ledger=read(path)
 if ledger['campaign_plan_sha256']!=a['campaign_plan_sha256']:raise ValueError('Native replacement campaign changed')
 entries=[x for x in ledger['replacements'] if x['part']==planned['index']]
 if len(entries)!=1:raise ValueError('Native replacement is ambiguous')
 e=entries[0]
 if e['original_job_id']!=planned['id'] or e['replacement_job_id']!=part['job_id'] or part.get('planned_job_id')!=planned['id']:raise ValueError('Native replacement identity mismatch')
 proof_path=pathlib.Path(e['failure_audit_path']);cp=pathlib.Path(e['replacement_contract_path'])
 if digest(proof_path)!=e['failure_audit_sha256'] or digest(cp)!=e['replacement_contract_sha256']:raise ValueError('Native replacement proof changed')
 proof=read(proof_path);old=pathlib.Path(proof['original_receipt_root'])
 if proof['decision']!='PRE_GPU_SOURCE_HANDOFF_LOCK_FAILURE_NO_MODEL_REQUESTS' or proof['model_requests_in_failed_attempt']!=0 or proof['GPU_execution_in_failed_attempt'] is not False or set(proof['original_files'])!={'CONTRACT.json','TRUST_SNAPSHOT.json'}:raise ValueError('Native replacement cannot repeat actual GPU generation')
 if proof['original_job_id']!=planned['id'] or proof['replacement_job_id']!=part['job_id'] or proof['part']!=planned['index']:raise ValueError('Native replacement failed-attempt binding changed')
 for name,value in proof['original_files'].items():
  if digest(old/name)!=value:raise ValueError('Native original failed attempt changed')
 if digest(proof_path.parent/'ORIGINAL_CONTROLLER_FAILURE.log')!=proof['journal_sha256'] or digest(cp)!=proof['replacement_contract_sha256']:raise ValueError('Native original controller failure changed')
 before=read(old/'CONTRACT.json');after=read(cp)
 if dict(after,id=planned['id'])!=before or after['id']!=part['job_id'] or after['parameters']['task_ids']!=planned['task_ids'] or digest(old/'CONTRACT.json')!=proof['original_contract_sha256']:raise ValueError('Native replacement altered the frozen experiment')
 return part['job_id']

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
  if part['part']!=planned['index'] or part['job_id']!=native_job_id(stage,a,planned,part) or part['task_ids']!=planned['task_ids']:raise ValueError('Native campaign partition changed')
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

def configuration_evidence(root, db, history, receipt):
 """Append public-safe observations to immutable identities, never rewrite profiles/runs.

 Only hash-pinned source rows are inspected. Aggregate timing rates require the
 exact task count and an independently matching request-wall sum. Logs, prompts,
 request bodies and model outputs are never exported.
 """
 root=pathlib.Path(root);configs={p['runtime_configuration_id']:p for p in history['profiles']};ce=[];me=[]
 sampler_keys=('temperature','seed','top_p','top_k','min_p','repeat_penalty','presence_penalty','frequency_penalty','typical_p','repeat_last_n','mirostat','mirostat_tau','mirostat_eta')
 for cid in sorted({r['runtime_configuration_id'] for r in history['runs']}):
  cfg=configs[cid];runs=[r for r in history['runs'] if r['runtime_configuration_id']==cid];sources=[];fields={};all_requests=[];all_replies=[];logs=[];files={}
  def pinned(path, expected, authority):
   path=pathlib.Path(path);path=path if path.is_absolute() else root/path
   if not path.resolve().is_relative_to(root.parent.resolve()) or not path.is_file() or digest(path)!=expected:raise ValueError('Configuration evidence source changed')
   key=str(path.resolve());files[key]=(path,expected)
   sources.append({'filename':path.name,'sha256':expected,'authority_audit_id':authority})
   return path
  for exp in sorted({r['experiment_id'] for r in runs}):
   entry=db['summary'].get(exp.lower(),{});ap=pathlib.Path(entry.get('audit_path',''));ap=ap if ap.is_absolute() else root/ap
   if not ap.is_file():continue
   original={r['audit_hash'] for r in runs if r['experiment_id']==exp}
   if digest(ap) not in original:continue
   aid=receipt(ap,digest(ap));audit=read(ap);folder=ap.parent;pins={}
   plan=root/'staging'/exp.lower()/'PLAN.json'
   if plan.is_file() and digest(plan)==cfg.get('source_plan_sha256'):
    original_plan=read(plan);pa=receipt(plan,digest(plan))
    sources.append({'filename':'PLAN.json','sha256':digest(plan),'authority_audit_id':pa})
    def plan_parameters(obj,prefix):
     for key,value in obj.items():
      if not re.fullmatch('[A-Za-z0-9_.-]{1,80}',key):continue
      path=prefix+'.'+key
      if isinstance(value,dict):plan_parameters(value,path)
      elif isinstance(value,(bool,int,float)) or isinstance(value,str) and re.fullmatch('[A-Za-z0-9_.+ -]{1,80}',value):fields[path]=value
    for name in ('fixed','runtime','sampling','source_sampling','coding_sampling','chat_template_kwargs','runtime_options','tuning'):
     if isinstance(original_plan.get(name),dict):plan_parameters(original_plan[name],'recorded_plan.'+name)
    for name in ('cache_mib','maximum_output_tokens','maximum_device_vram_mib','maximum_model_seconds','power_limit_w','engine_version','cuda_version','driver_version','seed'):
     value=original_plan.get(name)
     if isinstance(value,(bool,int,float)) or isinstance(value,str) and re.fullmatch('[A-Za-z0-9_.+ -]{1,80}',value):fields['recorded_plan.'+name]=value
   raw=folder/'RAW_HASHES.json'
   if raw.is_file():
    pins=read(raw)
    if pins.get('AUDIT.json') not in (None,digest(ap)):raise ValueError('Evidence audit/hash manifest mismatch')
    authority=receipt(raw,digest(raw))
    for name in ['LAUNCH.json','server.log','SAMPLES.jsonl','FUNCTIONAL.jsonl','BFCL.jsonl','AGENT.jsonl','HOST_PRECHECK.json']:
     if name in pins:pinned(folder/name,pins[name],authority)
   for rel,sha in audit.get('evidence',{}).items():
    if rel.startswith('staging/'+exp.lower()+'/measurements/') and pathlib.Path(rel).name in ('launch.json','server.log','FUNCTIONAL.jsonl','SAMPLES.jsonl','BFCL.jsonl','AGENT.jsonl'):pinned(root/rel,sha,aid)
   # Native broker campaigns: no inferred plan; captured launch and answer rows.
   for part in entry.get('parts',[]):
    pap=pathlib.Path(part['audit_path']);pap=pap if pap.is_absolute() else root/pap
    if digest(pap)!=part['audit_sha256']:raise ValueError('Native metadata audit changed')
    manifest=pap.parent/'RAW_HASHES.json';authority=receipt(manifest,digest(manifest));pins=read(manifest)
    for name in ('LAUNCH.json','HTTP_RESULTS.jsonl','server.log'):
     if name in pins:pinned(pap.parent/name,pins[name],authority)
  byfile={}
  for path,sha in files.values():
   if path.name=='server.log':logs.append(path.read_text(errors='replace'));continue
   if path.suffix=='.jsonl':
    records=[json.loads(line) for line in path.read_text().splitlines() if line.strip()];byfile[str(path)]=records
    for row in records:
     if row.get('kind')!='warmup' and isinstance(row.get('request'),dict):
      all_requests.append(row['request']);all_replies.append(row.get('native_reply') or row.get('reply') or {})
  # Request settings are evidence, not an excuse to overwrite the original profile.
  for key in sampler_keys:
   values=[r[key] for r in all_requests if key in r]
   if values and len(values)==len(all_requests) and all(v==values[0] for v in values) and isinstance(values[0],(int,float)):
    fields['runtime.observed_request_sampling.'+key]=values[0]
  # Actual server-returned sampler values are distinct from requested flags.
  settings=[reply.get('generation_settings') or reply.get('__verbose',{}).get('generation_settings') or {} for reply in all_replies]
  for key in (*sampler_keys,'n_predict','ignore_eos','stream','cache_prompt','n_keep','n_discard','reasoning_format','reasoning_in_content','backend_sampling','speculative.types'):
   values=[a.get(key) for a in settings]
   if values and all(v is not None and v==values[0] for v in values) and isinstance(values[0],(bool,int,float,str,list)):
    value=values[0]
    if isinstance(value,str) and not re.fullmatch('[A-Za-z0-9_.+ -]{1,80}',value):continue
    if isinstance(value,list) and not all(isinstance(v,str) and re.fullmatch('[A-Za-z0-9_.+ -]{1,40}',v) for v in value):continue
    fields['runtime.observed_generation_settings.'+key]=value
  kwargs=[r.get('chat_template_kwargs') for r in all_requests]
  if kwargs and all(isinstance(k,dict) and k==kwargs[0] for k in kwargs):
   for k in ('enable_thinking','reasoning_effort','thinking_budget'):
    if k in kwargs[0] and isinstance(kwargs[0][k],(bool,int,float,str)):
     fields['runtime.observed_template_controls.'+k]=kwargs[0][k]
     if k=='enable_thinking' and cfg['runtime'].get('native_template_controls') is None:fields['requested.thinking']=kwargs[0][k]
  joined='\n'.join(logs)
  versions=set(re.findall(r'\bversion:\s*([0-9]+\.[0-9]+\.[0-9]+(?:-[A-Za-z0-9.]+)?)',joined))
  if len(versions)==1:fields['engine.version']=versions.pop()
  builds=re.findall(r'common_params_print_info: build (\d+) \(([^)]+)\)',joined)
  if builds and len(set(builds))==1:
   number,commit=builds[0];fields['engine.reported_build_number']=int(number)
   if re.fullmatch('[a-f0-9]{40}',commit):fields['engine.git_commit']=commit
   elif commit=='unknown':fields['engine.version_provenance_note']='Pinned historical server log reports build '+number+' (unknown); no identifiable upstream version or commit. Binary and CUDA-library hashes remain authoritative.'
  archs=set(re.findall(r'CUDA : ARCHS = ([0-9, ]+) \|',joined))
  if len(archs)==1:fields['engine.reported_compiled_CUDA_archs']=archs.pop().strip()
  # Only record explicit, uniform GGUF metadata printed by the actual engine.
  architectures=set(re.findall(r'general\.architecture\s+\S+\s*=\s*([A-Za-z0-9_]+)',joined))
  if len(architectures)==1:fields['model.architecture']=architectures.pop()
  if fields:
   evidence={'runtime_configuration_id':cid,'fields':fields,'sources':sorted({H(s):s for s in sources}.values(),key=H),'interpretation':'Additional observations from pinned original execution evidence. Immutable original profile unchanged; reported build identity is not an upstream release. Requested options do not establish effective kernel dispatch.'}
   evidence['evidence_id']='evidence-'+H(evidence);ce.append(evidence)
  for run in runs:
   candidates=[]
   for filename,records in byfile.items():
    # Select only this measured discipline, excluding warmup/QA and other suites.
    if run['discipline']=='coding':selected=[r for r in records if r.get('suite') in (None,'standard') and (r.get('task_id') or r.get('task') or r.get('id') or '').removeprefix('standard:').startswith('HumanEval/')]
    elif run['discipline']=='tools' and pathlib.Path(filename).name=='BFCL.jsonl':selected=records
    elif run['discipline']=='mbpp':selected=[r for r in records if r.get('kind')=='coding' and str(r.get('task','')).lower().startswith(('mbpp','mbppplus'))]
    elif run['discipline'].startswith('long'):selected=[r for r in records if r.get('kind')==('validation' if run['discipline']=='long32k_validation' else 'long')]
    else:selected=[]
    if selected:candidates.append(selected)
   # Duplicated SAMPLES/FUNCTIONAL logs are alternative witnesses, not extra work.
   if run['experiment_id']=='R448':candidates=[[r for rows in byfile.values() for r in rows if r.get('kind')=='coding']]
   accepted=[]
   for rows in candidates:
    wall=sum(r.get('e2e_s',0) for r in rows)
    ids=[r.get('task_id') or r.get('task') or r.get('id') for r in rows]
    if len(rows)==run['tasks'] and len(set(ids))==len(rows) and finite(run.get('wall_s')) and math.isclose(wall,run['wall_s'],rel_tol=1e-7,abs_tol=1e-5):accepted.append(rows)
   if not accepted:continue
   rows=accepted[0];timings=[(r.get('native_reply') or r.get('reply') or {}).get('timings',{}) for r in rows];values={}
   for name,count_key,time_key in [('prefill','prompt_n','prompt_ms'),('decode','predicted_n','predicted_ms')]:
    if all(finite(t.get(count_key)) and t[count_key]>=0 and finite(t.get(time_key)) and t[time_key]>0 for t in timings):
     tokens=sum(t[count_key] for t in timings);ms=sum(t[time_key] for t in timings)
     values[name+'_tok_s']=1000*tokens/ms;values[name+'_tokens']=tokens;values[name+'_engine_ms']=ms
   if 'decode_tokens' in values and values['decode_tokens']>0 and finite(run.get('gpu_j')):values['gpu_j_per_output_token']=run['gpu_j']/values['decode_tokens']
   if values:
    item={'run_id':run['run_id'],'runtime_configuration_id':cid,'values':values,'tasks':len(rows),'wall_sum_s':sum(r['e2e_s'] for r in rows),'sources':sorted({H(s):s for s in sources}.values(),key=H),'aggregation':'Rate = sum of recorded token counts / sum of engine timing seconds for the exact task set; excludes startup/warmup. GPU J/output token uses gross case-window GPU energy including prefill. Engine prefill time is not TTFT. No unseen holdout claim.'}
    item['evidence_id']='measurement-'+H(item);me.append(item)
 return ce,me

def weight_integrity_review(a,rows,plan,decision):
 """Verify a complete CPU tensor census; export metrics, never model values."""
 if a.get('analysis_id')!='OMNICODER_V1_V2_CPU_WEIGHT_INTEGRITY' or a.get('status')!='COMPLETE_ALL_COMPARABLE_TENSORS':raise ValueError('Incomplete weight comparison')
 if a.get('new_GPU_runs')!=0 or a.get('new_model_requests')!=0 or a.get('model_files_modified') is not False or a.get('execution_uid')!=65534 or a.get('input_FDs_read_only') is not True:raise ValueError('Unverified CPU/read-only execution')
 controls=('q6_zero','q6_nonzero','q6_negative_control','different_encodings_equal_values','q8_signed_values','native_and_numpy_agree')
 if any(a.get('controls',{}).get(k) is not True for k in controls):raise ValueError('Missing decoder controls')
 A,B=a['headers'];names=set(A['tensors'])&set(B['tensors']);matched={k for k in names if A['tensors'][k]['shape']==B['tensors'][k]['shape']}
 if set(A['tensors'])!=set(B['tensors']) or matched!=set(A['tensors']) or A['tensor_count']!=len(matched) or B['tensor_count']!=len(matched):raise ValueError('Report requires complete matched tensor rosters')
 if len(rows)!=len(matched) or {r['name'] for r in rows}!=matched or len(rows)!=a['compared_tensors']:raise ValueError('Missing/duplicate tensor results')
 groups={};public_rows=[]
 keep=('name','parameters','type_A','type_B','changed_values_exact','equal_values_exact','max_abs_difference','mean_abs_difference','rmse','relative_l2_A','cosine_similarity','payload_sha256_A','payload_sha256_B','decoder_reference_checks','decoder_max_abs_difference')
 for r in rows:
  name=r['name'];ta=A['tensors'][name];tb=B['tensors'][name];n=r['parameters']
  if not re.fullmatch('[A-Za-z0-9_.-]{1,160}',name) or type(n) is not int or n<=0 or n!=ta['parameters'] or n!=tb['parameters'] or n!=math.prod(ta['shape']):raise ValueError('Tensor identity/count mismatch')
  if r['type_A']!=ta['type_name'] or r['type_B']!=tb['type_name']:raise ValueError('Tensor precision mismatch')
  if type(r['changed_values_exact']) is not int or not 0<=r['changed_values_exact']<=n or r['equal_values_exact']!=n-r['changed_values_exact']:raise ValueError('Invalid tensor difference count')
  if any(not finite(r[k]) or r[k]<0 for k in ('max_abs_difference','mean_abs_difference','rmse','squared_difference_sum','squared_norm_A','squared_norm_B','decoder_max_abs_difference')):raise ValueError('Invalid tensor metric')
  if not math.isclose(r['rmse']**2*n,r['squared_difference_sum'],rel_tol=1e-10,abs_tol=1e-15) or r['decoder_reference_checks']<2:raise ValueError('Unverified tensor decoder/metric')
  if any(not re.fullmatch('[a-f0-9]{64}',r[k]) for k in ('payload_sha256_A','payload_sha256_B')):raise ValueError('Missing tensor payload identity')
  g=groups.setdefault(r['type_A']+' / '+r['type_B'],{'tensors':0,'parameters':0,'changed_tensors':0,'changed_values_exact':0,'squared_difference_sum':0.0,'max_abs_difference':0.0})
  for k,v in [('tensors',1),('parameters',n),('changed_tensors',int(r['changed_values_exact']>0)),('changed_values_exact',r['changed_values_exact']),('squared_difference_sum',r['squared_difference_sum'])]:g[k]+=v
  g['max_abs_difference']=max(g['max_abs_difference'],r['max_abs_difference']);public_rows.append({k:r[k] for k in keep})
 totals={'compared_parameters':sum(r['parameters'] for r in rows),'changed_values_exact':sum(r['changed_values_exact'] for r in rows),'changed_tensors':sum(r['changed_values_exact']>0 for r in rows),'identical_tensors':sum(r['changed_values_exact']==0 for r in rows)}
 if any(a[k]!=v for k,v in totals.items()):raise ValueError('Tensor aggregate mismatch')
 rmse=math.sqrt(sum(r['squared_difference_sum'] for r in rows)/totals['compared_parameters'])
 if not math.isclose(rmse,a['global_rmse'],rel_tol=1e-12,abs_tol=1e-15):raise ValueError('Global RMSE mismatch')
 represented='DIFFERENT_RECONSTRUCTED_WEIGHTS' if totals['changed_values_exact'] else 'IDENTICAL_RECONSTRUCTED_WEIGHTS'
 if a['represented_weight_identity']!=represented or decision['represented_weight_identity']!=represented or decision['underlying_checkpoint_verdict']!='NOT_UNAMBIGUOUSLY_DETERMINABLE':raise ValueError('Unsupported checkpoint identity claim')
 artifacts=[]
 for i,version in enumerate(('V1','V2')):
  p=plan[version];actual=a['artifacts'][i]
  if actual['sha256']!=p['sha256'] or actual['bytes']!=p['bytes']:raise ValueError('Wrong compared artifact')
  artifacts.append({k:p[k] for k in ('source_repository','source_revision','filename','sha256','bytes')})
 for g in groups.values():g['rmse']=math.sqrt(g.pop('squared_difference_sum')/g['parameters'])
 keys=('general.architecture','general.name','general.quantization_version','general.file_type','general.size_label','tokenizer.ggml.model','tokenizer.ggml.pre','tokenizer.ggml.tokens','tokenizer.ggml.merges','tokenizer.ggml.token_type','tokenizer.chat_template')
 metadata=[{k:h['metadata'][k] for k in keys if k in h['metadata']} for h in (A,B)]
 # Strings are deliberately limited to named public GGUF fields; no template text.
 for m in metadata:
  if isinstance(m.get('tokenizer.chat_template'),str):m['tokenizer.chat_template']={'utf8_sha256':hashlib.sha256(m['tokenizer.chat_template'].encode()).hexdigest()}
 rel=math.sqrt(sum(r['squared_difference_sum'] for r in rows)/sum(r['squared_norm_A'] for r in rows))
 if not math.isclose(rel,a['global_relative_l2_A'],rel_tol=1e-12,abs_tol=1e-15) or max(r['max_abs_difference'] for r in rows)!=a['global_max_abs_difference']:raise ValueError('Global difference metric mismatch')
 agreements={prefix:all(A['metadata'].get(k)==B['metadata'].get(k) for k in set(A['metadata'])|set(B['metadata']) if k.startswith(prefix)) for prefix in ('qwen35.','tokenizer.')}
 return {'analysis_id':a['analysis_id'],'at_utc':decision['at_utc'],'represented_weight_identity':represented,'underlying_checkpoint_verdict':decision['underlying_checkpoint_verdict'],**totals,'compared_tensors':len(rows),'global_rmse':rmse,'global_relative_l2_A':rel,'global_max_abs_difference':a['global_max_abs_difference'],'type_pairs':groups,'type_counts_A':A['type_counts'],'type_counts_B':B['type_counts'],'metadata_agreement':agreements,'identical_quantized_tensors':[r['name'] for r in rows if r['changed_values_exact']==0 and r['type_A']!='F32'],'metadata':metadata,'artifacts':artifacts,'decoder_controls':a['controls'],'decoder_identities':a['decoder_identities'],'NumPy_version':a['NumPy_version'],'elapsed_s':a['elapsed_s'],'quantization_noise_conclusion':a['quantization_noise_conclusion'],'training_history_conclusion':a['training_history_conclusion'],'new_GPU_runs':0,'tensor_results':public_rows}

def build(root,db,comparison,experiments,receipt,sanitize,previous):
 root=pathlib.Path(root);reg=read(root/'BENCHMARK_REGISTER.json');profiles=[];runs=[];defs={d['benchmark_id']:d for d in reg['definitions']}
 for item in reg.get('artifact_weight_reviews',[]):
  if set(item)!={'review_id','audit_path','audit_sha256','tensor_results_path','tensor_results_sha256','plan_path','plan_sha256','decision_path','decision_sha256'}:raise ValueError('Unreviewed artifact review schema')
  originals={}
  for key in ('audit','tensor_results','plan','decision'):
   p=(root/item.pop(key+'_path')).resolve()
   if not p.is_relative_to(root.resolve()) or digest(p)!=item[key+'_sha256']:raise ValueError('Artifact review source changed')
   originals[key]=p
  a=read(originals['audit']);plan=read(originals['plan']);decision=read(originals['decision']);rows=[json.loads(s) for s in originals['tensor_results'].read_text().splitlines()]
  if a['tensor_results_sha256']!=item['tensor_results_sha256'] or a['source_plan_sha256']!=item['plan_sha256']:raise ValueError('Artifact review lineage mismatch')
  item['result']=weight_integrity_review(a,rows,plan,decision)
  item['evidence_audit_ids']=[ident for k in originals if (ident:=receipt(originals[k],item[k+'_sha256']))]
  sources=[]
  for source in decision['source_evidence']:
   p=(root/source['path']).resolve()
   if not p.is_relative_to(root.resolve()) or digest(p)!=source['sha256']:raise ValueError('Weight review provenance changed')
   sources.append({'role':source['role'],'sha256':source['sha256'],'audit_id':receipt(p,source['sha256']),'url':source.get('url')})
  item['result']['source_evidence']=sources
  item['result']['provenance_findings']={k:decision['provenance_findings'][k] for k in ('V1_quantizer','V2_quantizer','V2_upstream_lineage','reported_faulty_release_relationship','cached_source_object_observation')}
  cleanup=decision['artifact_availability'];cp=(root/cleanup['cleanup_result_path']).resolve()
  if not cp.is_relative_to(root.resolve()) or digest(cp)!=cleanup['cleanup_result_sha256']:raise ValueError('Cleanup evidence changed')
  c=read(cp)
  if c['deleted_count']!=len(c['deleted_files']) or c['main_unchanged'] is not True or c['historical_audits_and_hashes_modified'] is not False:raise ValueError('Invalid artifact availability evidence')
  item['result']['artifact_availability']={k:c[k] for k in ('completed_at_utc','deleted_files','deleted_count','deleted_allocated_bytes','main_unchanged','main_alias_preserved','historical_audits_and_hashes_modified','note')}
  item['result']['artifact_availability']['audit_id']=receipt(cp,cleanup['cleanup_result_sha256'])
 for item in reg.get('archived_diagnostics',[]):
  required={'experiment_id','issue','at_utc','analysis_path','analysis_sha256','followup_path','followup_sha256','new_GPU_runs','original_results_unchanged','weight_provenance_path','weight_provenance_sha256'}
  if set(item) not in (required,required|{'operator_stop_path','operator_stop_sha256'}):raise ValueError('Unreviewed diagnostic export schema')
  if 'operator_stop_path' in item:
   sp=(root/item.pop('operator_stop_path')).resolve()
   if not sp.is_relative_to(root.resolve()) or digest(sp)!=item['operator_stop_sha256']:raise ValueError('Operator stop evidence changed')
   stop=read(sp)
   if stop['no_automatic_resume'] is not True or stop['new_GPU_runs']!=0 or stop['full_census_completed'] is not False:raise ValueError('Invalid partial-census stop decision')
   item['operator_stop']={k:stop[k] for k in ('at_utc','status','completed_tensors','compared_parameters','classifications','full_census_completed','completed_evidence_preserved','no_automatic_resume','scope')}
   item['operator_stop_audit_id']=receipt(sp,item['operator_stop_sha256'])
  ap=root/item.pop('analysis_path');fp=root/item.pop('followup_path')
  if digest(ap)!=item['analysis_sha256'] or digest(fp)!=item['followup_sha256']:raise ValueError('Archived diagnostic changed')
  a=read(ap);follow=read(fp)
  if a['analysis_kind']!='ARCHIVED_RESPONSE_DIAGNOSTIC_ISSUE12' or a['source_experiment_audit_sha256']!=db['summary']['r448']['audit_sha256'] or a['new_GPU_runs']!=0 or follow['new_GPU_runs']!=0 or follow['source_audit_sha256']!=item['analysis_sha256']:raise ValueError('Diagnostic source mismatch')
  item['audit_id']=receipt(ap,item['analysis_sha256']);item['followup_audit_id']=receipt(fp,item['followup_sha256'])
  wp=root/item.pop('weight_provenance_path')
  if digest(wp)!=item['weight_provenance_sha256']:raise ValueError('Weight provenance review changed')
  w=read(wp)
  if w['kind']!='OXCODER_WEIGHT_PROVENANCE_REVIEW' or w['new_GPU_runs']!=0:raise ValueError('Wrong weight review')
  item['weight_provenance_audit_id']=receipt(wp,item['weight_provenance_sha256'])
  item['weight_provenance']={k:w[k] for k in ('at_utc','local_R448_artifact','upstream_safetensors','source_lineage','external_claim','independent_header_inventory','next_decision','sources')}
  item['summary']={k:a[k] for k in ('source_experiment_audit_sha256','quality_score_unchanged','classification','overall','empty_final_content','nonempty_final_content','empty_wall_share_percent','empty_completion_token_share_percent','engine_configuration','parser_checks','historical_comparisons','decision')}
  item['statistics_method']='Median and linearly interpolated P90 at position(n-1)*0.9; request wall sums exclude startup/warmup/scoring. Reasoning characters are not token counts.'
  item['followup']={k:follow[k] for k in ('status','common_constraints','primary_metric','secondary_metrics','practical_minimum','early_stop','proposals','not_justified','source_review')}
  dev=follow['development_inputs'];item['followup']['development_inputs']={k:dev[k] for k in ('sha256','case_ids','prompts','scoring')}
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
 ce,me=configuration_evidence(root,db,result,receipt)
 result['configuration_evidence']=frozen_merge(prior.get('configuration_evidence',[]),ce,'evidence_id')
 result['measurement_evidence']=frozen_merge(prior.get('measurement_evidence',[]),me,'evidence_id')
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
 observed_fields={}
 for kind,identity,tag in [('configuration_evidence','runtime_configuration_id','evidence-'),('measurement_evidence','run_id','measurement-')]:
  seen_evidence=set()
  for e in data.get(kind,[]):
   if e['evidence_id']!=tag+H({k:v for k,v in e.items() if k!='evidence_id'}) or e['evidence_id'] in seen_evidence:raise ValueError('Invalid evidence content identity')
   seen_evidence.add(e['evidence_id'])
   if e['runtime_configuration_id'] not in profiles or identity=='run_id' and e['run_id'] not in seen:raise ValueError('Orphan evidence')
   if not e.get('sources') or any(not re.fullmatch('[a-f0-9]{64}',s.get('sha256','')) or not s.get('authority_audit_id') for s in e['sources']):raise ValueError('Missing evidence provenance')
   if kind=='measurement_evidence':
    original=next(r for r in data['runs'] if r['run_id']==e['run_id'])
    if original['runtime_configuration_id']!=e['runtime_configuration_id'] or original['tasks']!=e['tasks'] or not math.isclose(original['wall_s'],e['wall_sum_s'],rel_tol=1e-7,abs_tol=1e-5):raise ValueError('Timing evidence/profile/task/wall mismatch')
    if any(not finite(v) or v<0 for v in e['values'].values()):raise ValueError('Invalid recorded timing metric')
    for name in ('prefill','decode'):
     vals=e['values']
     if name+'_tok_s' in vals and (vals[name+'_engine_ms']<=0 or not math.isclose(vals[name+'_tok_s'],1000*vals[name+'_tokens']/vals[name+'_engine_ms'],rel_tol=1e-12)):raise ValueError('Invalid recorded token-rate conversion')
   if kind=='configuration_evidence':
    for key,v in e['fields'].items():
     pair=(e['runtime_configuration_id'],key)
     if pair in observed_fields and observed_fields[pair]!=v:raise ValueError('Conflicting evidence annotations')
     observed_fields[pair]=v
     cur=profiles[e['runtime_configuration_id']]
     for part in key.split('.'):cur=cur.get(part) if isinstance(cur,dict) else None
     if cur is not None and cur!=v:raise ValueError('Evidence contradicts immutable profile')
 return True

def pair_delta(a,b):
 keys=['benchmark_identity_id','evaluated_task_set_hash','scorer_version','tasks']
 if any(a[k]!=b[k] for k in keys):return {'comparable':False,'reason':'Different benchmark/task set/scorer/count; no delta calculated.'}
 def percent(x,y):return (y/x-1)*100 if finite(x) and finite(y) and x>0 else None
 return {'comparable':True,'quality_delta_pp':b['score_percent']-a['score_percent'],'latency_delta_percent':percent(a.get('wall_s'),b.get('wall_s')),'energy_per_success_delta_percent':percent(a.get('gpu_j_per_success'),b.get('gpu_j_per_success')),'interpretation':'Whole-profile comparison. No causal optimization claim without a dedicated independent audit.'}

def master_catalog(register, history):
 """Presentation identities only; never rewrite the immutable research ledger."""
 columns=[]; assignments={}; definitions={d['benchmark_id']:d for d in register['definitions']}
 def protocol(run):
  return {k:run.get(k) for k in ('benchmark_id','benchmark_identity_id','benchmark_revision','dataset_split_hash','evaluated_task_set_hash','scorer_version','tasks','metric')}
 def add(definition, runs, scope):
  identity=protocol(runs[0]) if runs else {
   'benchmark_id':definition['benchmark_id'],'benchmark_identity_id':definition_identity(definition),
   'benchmark_revision':definition.get('benchmark_revision'),'dataset_split_hash':definition.get('dataset_split_hash'),
   'evaluated_task_set_hash':definition.get('expected_task_ids_hash'),'scorer_version':definition.get('scorer_version'),
   'tasks':definition.get('required_task_count'),'metric':definition.get('metric')}
  item={'key':'benchmark-'+H({'protocol':identity,'scope':scope}),'name':definition.get('name',identity['benchmark_id']),
        'scope':scope,'protocol':identity,'definition':{k:definition.get(k) for k in
        ('benchmark_id','benchmark_revision','version','hf_dataset_id','dataset_split','dataset_split_hash','required_task_count','scorer_version','official_definition_verified','provider_repository','required_evaluation_settings')},
        'registered':identity['benchmark_id'] in definitions,'records':len(runs)}
  columns.append(item)
  for run in runs:assignments[run['run_id']]=item['key']
 for definition in register['definitions']:
  full=[r for r in history['runs'] if r['benchmark_id']==definition['benchmark_id'] and r['official_eligible'] and r['benchmark_identity_id']==definition_identity(definition)]
  groups={}
  for run in full:groups.setdefault(H(protocol(run)),[]).append(run)
  if groups:
   for _,runs in sorted(groups.items()):add(definition,runs,'OFFICIAL_LOCAL')
  else:add(definition,[],'OFFICIAL_LOCAL')
 groups={}
 for run in history['runs']:
  if run['run_id'] in assignments:continue
  scope='OFFICIAL_LOCAL' if run['official_eligible'] else 'LOCAL_SUPPLEMENTAL' if run['benchmark_id'].startswith('local-') else 'UNQUALIFIED_FULL' if run.get('status')=='FULL_NATIVE_CODING_OFFICIAL_API_PENDING' else 'HISTORICAL'
  groups.setdefault((scope,H(protocol(run))),[]).append(run)
 for (scope,_),runs in sorted(groups.items()):
  definition=definitions.get(runs[0]['benchmark_id'],{'benchmark_id':runs[0]['benchmark_id'],'name':runs[0]['benchmark_id']})
  add(definition,runs,scope)
 if set(assignments)!={r['run_id'] for r in history['runs']}:raise ValueError('Master table lost a measured record')
 return {'schema_version':1,'benchmark_columns':columns,'run_columns':assignments,
         'mean_policy':'User-selected unweighted arithmetic mean of exact-protocol replicate means. All selected results required. Official mode accepts admitted results only. Never select a replicate maximum.',
         'missing_label':'NICHT ERFASST'}

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
 if register.get('archived_diagnostics'):page+='## Archived response diagnostics\n\n[OxCoder R448: output-cap and reasoning-channel investigation](oxcoder-diagnostic.md). Original scores and profile identities remain unchanged; this is a read-only explanation, not an optimized model result.\n\n'
 if register.get('artifact_weight_reviews'):page+='## Artifact integrity\n\n[OmniCoder V1 / V2: complete CPU weight comparison](weight-integrity.md). Different quantized representations are measured; underlying checkpoint and fine-tuning identity remain inconclusive. Historical benchmark results are preserved.\n\n'
 page+='## Next evidence gaps\n\n'+table(['Priority','Technical decision / next step','GPU initially required'],[[x['priority'],x['action'],x.get('GPU_required_initially')] for x in register['next_test_priorities']])
 page+='[Benchmark definitions and publisher evidence](benchmark-register.md) · [Local agent and synthetic tests](local-benchmarks.md) · [Reproduction](reproduce.md)\n\nEach profile records unknown fields as null (**NOT MEASURED**). An absent MTP/graph/cache setting is never assumed off. No-MTP execution does not establish that weights are original. Actual kernel execution is distinct from a requested backend. Historical development suites were reused; no unseen-holdout or absence-of-overfitting claim is made.\n'
 write(docs/'benchmarks.md',page)
 page='# Configuration Comparison & Benchmark Master Table\n\n**Default: Alle gemessenen Ergebnisse.** One continuous row per immutable configuration appearing in `history.runs`, with no pagination. Official, historical, supplemental and unqualified measured results are visible together, in distinct protocol/status columns. Plans and result-free configuration attempts remain in the [separate archive](configuration-archive.md). Every recorded profile field and startup flag is available through the categorized column picker. Each benchmark column is bound to its exact register definition, dataset/task set, scorer and qualification track. Unknown means **NICHT ERFASST**, never off or zero. Failed and weaker configurations remain visible.\n\nUse **Nur offiziell qualifizierte Ergebnisse** to optionally restrict the display. **Durchschnittsmodus** only changes which exact protocols may enter the user-selected mean; it does not hide historical measurements in the default table. The user-defined arithmetic mean is not an official benchmark score; every selected result must exist for the exact same configuration. Distinct original run observations use their arithmetic mean, with count and dispersion; admission-history duplicates do not create extra observations. Provenance-defined observation counts do not establish statistical independence. Conflicting judgments are excluded from numerical summaries.\n\n<div id="all-measured-results" aria-live="polite"></div>\n\n## Comparing individual measurements\n\n<div id="configuration-comparison" aria-live="polite"></div>\n\n## Data coverage and missing fields\n\nModel names and file names are not proof of architecture, parameter count, QAT, SVD, original weights or the executed kernel. Requested flags and verified execution remain separate fields. Engine versions are never substituted with build hashes. Newly discovered fields automatically become selectable; historical fields are supplemented only through hash-bound evidence annotations; immutable profiles and results are never rewritten. Historical server logs reporting `build 0 (unknown)` cannot establish an upstream release or Git commit. Build IDs, executable hashes and CUDA-library hashes remain separate identities.\n\n'
 gap_paths=['model.hf_revision','model.hf_repository','model.parameter_count','model.qat','model.svd','model.architecture','engine.version','engine.git_commit','engine.fork_repository','engine.cuda_version','engine.driver_version','engine.executed_kernel_backend_path','runtime.thinking_level','runtime.reasoning_budget_tokens','optimizations.speculation_effective','optimizations.flash_attention_effective','optimizations.cuda_graphs.actual_capture_replay']
 def field(obj,path):
  for key in path.split('.'):
   if not isinstance(obj,dict) or key not in obj:return None
   obj=obj[key]
  return obj
 measured_ids={r['runtime_configuration_id'] for r in history['runs']};measured_profiles=[p for p in history['profiles'] if p['runtime_configuration_id'] in measured_ids]
 def observed(p,path):
  values=[e['fields'][path] for e in history.get('configuration_evidence',[]) if e['runtime_configuration_id']==p['runtime_configuration_id'] and path in e['fields']]
  return values[0] if values else field(p,path)
 page+=table(['Recorded field','Profiles with a value','Profiles without a value'],[[path,sum(observed(p,path) is not None for p in measured_profiles),sum(observed(p,path) is None for p in measured_profiles)] for path in gap_paths])
 page+='Coverage counts above refer only to measured configurations. Additional column-picker fields expose pinned observed sampler/template controls, engine-reported build information and per-benchmark timing/energy provenance. TTFT remains unrecorded for non-streaming replies; prompt evaluation time is not TTFT. GPU J/output token includes prefill energy in the same case window.\n\n'
 page+='Explicit presentation fields use only recorded options: MTP is true for `draft-mtp`, false for explicit `none`, and unknown otherwise. Thinking mode uses an explicit `enable_thinking` template boolean; a reasoning-parser flag does not prove thinking mode. Model names, optimization-knob zero values and absent flags never establish effective execution.\n\n'
 page+='Prefill/decode/TTFT and other costs are shown only where the original run actually records them. Request wall time is not silently renamed total system latency. Performance columns are benchmark-specific, not pooled across unrelated tasks. CSV exports all filtered rows with the currently selected columns, complete identities and available audit links. CSV formula-like text is escaped.\n\nThe Top-5 analysis describes observed configurations and missing coverage. Suggested controlled A/B work is a research hypothesis, not a causal explanation, predicted speedup or automatic GPU authorization.\n\n[Immutable configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) · [Benchmark definitions and publisher evidence](benchmark-register.md) · [Original experiments](results.md)\n\n'
 page+='## Provenance gaps — excluded from reconstructed profiles\n\n'+table(['Experiment','Reason','Original audit'],[[g['experiment_id'],g['reason'],audit_links([g['audit_id']])] for g in history.get('provenance_gaps',[])])
 page+='## UI reproduction checks\n\nRun `python -m unittest discover -s scripts` and `node --test scripts/test_master_table.cjs` with Node.js 22 or newer. The optional real-browser acceptance script is `scripts/test_master_browser.cjs`: it accepts a site root URL and artifact directory and uses Playwright 1.64.1. Browser screenshots, CSVs and reports belong outside the public export tree. It runs with GPU rendering disabled. Development asset overrides are explicitly reported and must be disabled for the final published-site check.\n\nFilters accept substrings, `=value`, `!=value`, numeric comparisons such as `>=80`, and `?` for unknown. The CSV always includes immutable configuration IDs, all filtered rows and the currently visible columns. Long field values can be inspected directly in a table dialog without leaving the page.\n\n'
 if register.get('archived_diagnostics'):
  diagnostic='# OxCoder R448: archived response diagnosis\n\nRead-only investigation of [issue12](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/12). **No new GPU runs, model requests or changes to original benchmark results.**\n\n'
  for item in register['archived_diagnostics']:
   if item.get('operator_stop'):
    stop=item['operator_stop'];diagnostic+='## Current operator decision\n\n**Stopped at the user’s explicit request; no automatic resume.** '+str(stop['completed_tensors'])+' source tensors were compared before the stop; this is not a complete census. The user is selecting an alternative artifact. All partial evidence is retained. Earlier proposed GPU follow-ups below are historical plans, not scheduled work.\n\n```json\n'+pretty(stop)+'\n```\n\n'+audit_links([item['operator_stop_audit_id']])+'\n\n'
   a=item['summary'];diagnostic+='## Confirmed observations\n\nAll'+str(a['empty_final_content']['tasks'])+' empty final responses reached'+str(a['engine_configuration']['output_cap'])+' completion tokens with `finish_reason=length`. Their archived reasoning equals the complete raw text, with no closing thinking tag. All'+str(a['nonempty_final_content']['tasks'])+' nonempty final responses contain the closing tag and their final-channel text matches the text after that tag. This establishes an exhausted output budget before final-answer emission in the recorded profile; it does not prove why the model reasons for so long.\n\n'
   diagnostic+=table(['Group','Tasks','Passed','Wall sum s','Median s','P90 s','Completion tokens','Recorded decode tok/s'],[[name,x['tasks'],x['solved'],x['wall_sum_s'],x['wall_median_s'],x['wall_p90_s'],x['completion_tokens_total'],x['recorded_decode_tok_s']] for name,x in [('All',a['overall']),('Empty final',a['empty_final_content']),('Final present',a['nonempty_final_content'])]])
   diagnostic+='Original success remains '+str(a['quality_score_unchanged']['solved'])+'/'+str(a['quality_score_unchanged']['tasks'])+'. Empty-final requests consumed '+str(round(a['empty_wall_share_percent'],2))+'% of summed request latency. '+item['statistics_method']+' Exact reasoning-token counts were not supplied by the API: **NOT RECORDED**. Completion-token counts are measured; they are not silently relabelled reasoning-token counts.\n\n'
   diagnostic+='## Parser, template and scoring checks\n\n```json\n'+pretty(a['parser_checks'])+'\n```\n\nThe frozen template preopens thinking. The `deepseek` response mode separates reasoning into its own field. No unrecognised closing-tag variant or missing post-close final text is observed. The source meaning of `--no-reasoning-preserve` concerns retained assistant history; none of these requests contains prior assistant messages. This is not evidence that toggling that flag would fix the failures. The scorer correctly used final content under its declared answer contract; reasoning-only fenced code is not retroactively promoted to a valid answer.\n\n'
   diagnostic+='## Historical profiles: comparison limits\n\n'+table(['Experiment','Profile','Endpoint / protocol','Output cap','MTP','Solved','Median s','P90 s','Completion tokens','Empty final'],[[x['experiment_id'],x['model'],x['interface'],x['output_cap'],x['MTP'],str(x['score_solved'])+'/164',x['statistics']['wall_median_s'],x['statistics']['wall_p90_s'],x['statistics']['completion_tokens_total'],x['empty_content']] for x in a['historical_comparisons']])
   diagnostic+='OmniCoder2 and Qwen3.5 used preclosed thinking prompts, greedy temperature0 and a1024-token limit through the historical completion endpoint. OxCoder used native chat, thinking enabled, temperature1 and4096 tokens. Quantization, weights and MTP also differ. These are **whole-profile historical observations**, not causal proof of intrinsic model speed or superiority.\n\n'
   diagnostic+='## Weight identity: higher-priority hold on further OxCoder GPU work\n\nA [reported upstream tensor-identity concern](https://huggingface.co/OrionLLM/OxCoder-9B/discussions/3) was acknowledged by the maintainer as a possible export/checkpoint problem. That report is external evidence, not our completed independent tensor census. Our retrieved HF metadata shows that the currently published safetensors LFS object equals the original upload. No corrected weight payload is established by that history. The tested Q6 artifact matches its pinned quantizer identity, but exact conversion lineage to an upstream checkpoint is not supplied.\n\nThe independent header inspection finds760 shared tensors and15 additional Qwen MTP tensors;48 shared tensors have different stored dtypes. Headers alone do not prove equal values. The source tensor-payload census is tracked separately and must not be prematurely labelled complete. All further OxCoder optimization proposals below are **on hold pending weight-identity review**, in addition to their separate GPU-approval and900-second requirements.\n\n```json\n'+pretty(item['weight_provenance'])+'\n```\n\n'+audit_links([item['weight_provenance_audit_id']])+'\n\n'
   diagnostic+='## Frozen R448 profile\n\n```json\n'+pretty(a['engine_configuration'])+'\n```\n\n## Proposed isolated follow-up — not executed\n\n**Separate GPU approval is required by issue12, as is trusted enforcement of the900-second budget for the entire paired trial.** No GPU experiment is authorized or started by this report. P0 changes only explicit thinking true versus false; P1 separately tests a genuine1024-token reasoning budget inside an unchanged4096 total output budget. Native-template switching and actual reasoning-budget support must be verified before execution. Four frozen development cases are proposed; no official HumanEval failures are selected for tuning. This screen cannot qualify a general benchmark winner.\n\n```json\n'+pretty(item['followup'])+'\n```\n\n'
   diagnostic+='## Evidence and remaining hypotheses\n\nSource experiment SHA256: `'+a['source_experiment_audit_sha256']+'`. Diagnostic SHA256: `'+item['analysis_sha256']+'`. Follow-up plan SHA256: `'+item['followup_sha256']+'`. '+audit_links([item['audit_id'],item['followup_audit_id']])+'\n\n**LOCALLY MEASURED:** the original outputs, finish reasons, counters, timing and unchanged score. **LOCAL SOURCE REVIEW:** template and flag meanings, with source hashes in the plan. **NOT VERIFIED:** benefit or quality of thinking-off/budgeted thinking, larger-output profiles, parser alternatives and cross-model causal effects. Original inputs, answers and judgments remain unchanged.\n\n'
  write(docs/'oxcoder-diagnostic.md',diagnostic)
 if register.get('artifact_weight_reviews'):
  review='# OmniCoder V1 / V2: CPU weight integrity\n\nThis artifact review adds **zero GPU experiments, model requests or benchmark scores**. All historical configuration IDs, scores, qualifications and negative findings remain unchanged.\n\n'
  for item in register['artifact_weight_reviews']:
   a=item['result'];review+='## Decision\n\n**Different dequantized GGUF representations are proven. Underlying checkpoint / new fine-tuning: NOT UNAMBIGUOUSLY DETERMINABLE.** This is the requested three-way verdict at the source-weight level. Different file hashes or reconstruction grids do not prove a new trained checkpoint.\n\n'
   review+=table(['Measured scope','Value'],[['Date (UTC)',a['at_utc']],['Matched tensors',a['compared_tensors']],['Compared weight values',a['compared_parameters']],['Changed tensors',a['changed_tensors']],['Numerically identical tensors',a['identical_tensors']],['Exactly different reconstructed values',a['changed_values_exact']],['Global RMSE',a['global_rmse']],['Relative L2 against V1',a['global_relative_l2_A']],['Maximum absolute difference',a['global_max_abs_difference']],['CPU comparison elapsed seconds',a['elapsed_s']]])
   review+='Both files contain '+str(a['compared_tensors'])+' shape-matched tensors. Shared F32 equality and other metadata agreement are reported explicitly below; these are observations, not proof of identical remaining unquantized source weights.\n\n'+table(['Observed identity check','Measured result'],[['Identical quantized tensors',', '.join(a['identical_quantized_tensors'])],['Architecture metadata agreement',a['metadata_agreement']['qwen35.']],['Tokenizer / template metadata agreement',a['metadata_agreement']['tokenizer.']]])
   review+='## Exact artifact identities\n\n'+table(['Artifact','Bytes','SHA256','Pinned quantizer source'],[[x['filename'],x['bytes'],'`'+x['sha256']+'`','['+x['source_repository']+'](https://huggingface.co/'+x['source_repository']+'/tree/'+x['source_revision']+')'] for x in a['artifacts']])
   review+='## Precision policy is different despite the Q6_K labels\n\n'+table(['V1 / V2 storage','Tensors','Weight values','Changed tensors','Changed values','RMSE','Max abs'],[[k,g['tensors'],g['parameters'],g['changed_tensors'],g['changed_values_exact'],g['rmse'],g['max_abs_difference']] for k,g in a['type_pairs'].items()])
   review+='Actual V1 storage counts: `'+json.dumps(a['type_counts_A'],sort_keys=True)+'`. Actual V2 counts: `'+json.dumps(a['type_counts_B'],sort_keys=True)+'`. A same-precision Q6_K pair can still use different quantizer versions or calibration. A changed decoded value is not by itself a trained-weight delta.\n\n'+a['quantization_noise_conclusion']+'\n\n'
   review+='## Source provenance and reported faulty release\n\n'+table(['Question','Finding'],[[k,v if isinstance(v,str) else '`'+json.dumps(v,sort_keys=True)+'`'] for k,v in a['provenance_findings'].items()])
   review+='The cached upstream LFS observation is explicitly **external metadata**, not a completed independent source-tensor comparison. No new OxCoder investigation was resumed. Establishing whether V2 came from an originally faulty or corrected release requires an exact upstream conversion revision plus trustworthy original/corrected source payloads. Those prerequisites are absent.\n\n'
   review+='## Method and limits\n\nInputs were opened read-only, then all parsing and numerical work ran as UID65534 with GPU devices hidden, one CPU thread and a 768 MiB service limit. Both full-file SHA256 values were verified before comparison; inode, size and modification time were rechecked afterward. All comparable tensors were decoded completely in bounded chunks; no tensor sampling substitutes for the full comparison. Native C and NumPy implementations were cross-checked on the first/last chunk of every tensor, plus zero/nonzero/signed and deliberately changed controls. This is two CPU implementations from the reviewed engine tooling, not an independent unquantized training oracle. Float32 reconstructed values are compared exactly; differences use float64 accumulation. No model inference or task-quality claim follows from this audit.\n\n'
   review+='The missing quantization-noise control is a matched unquantized source pair, or controlled re-quantizations of a known common source with pinned conversion/calibration recipes. Without it, no significance threshold is invented. The original main V2 artifact remains the reproducible identity of its historical benchmark results.\n\n'
   review+='[All per-tensor measurements](artifact-reviews/omnicoder-tensors.md). [Public numerical dataset](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json) (`artifact_weight_reviews`): counts, metrics and tensor payload hashes only; no weight values or model files.\n\n'
   review+='## Preserved and removed artifacts\n\n'
   c=a['artifact_availability'];review+=str(c['deleted_count'])+' other OmniCoder2 GGUF variants were removed at the user’s explicit request, freeing'+str(c['deleted_allocated_bytes'])+' allocated bytes. The main Q6_K file and its alias remain. Historical audits/hashes and scientific qualification are preserved. Removed variants, including the grafted MTP artifact, need re-fetch or reconstruction before replay; historical qualification does not imply current local artifact availability.\n\n'+table(['Removed artifact'],[[name] for name in c['deleted_files']])
   review+='## Evidence\n\n'+audit_links(item['evidence_audit_ids']+[c['audit_id']])+'\n\n'+table(['Source','Pinned SHA256','Original reference'],[[x['role'],'`'+x['sha256']+'`','[Source]('+x['url']+')'] for x in a['source_evidence']])
   review+='Original numerical audit SHA256: `'+item['audit_sha256']+'`. Original tensor journal SHA256: `'+item['tensor_results_sha256']+'`. Source plan SHA256: `'+item['plan_sha256']+'`. Decision SHA256: `'+item['decision_sha256']+'`.\n\n**LOCALLY MEASURED:** full artifact identities, tensor layouts and all matched dequantized comparisons. **EXTERNALLY EVIDENCED:** publisher recipes, repository revisions and LFS metadata. **NOT VERIFIED:** a distinct fine-tune, differences beyond controlled quantization noise, exact V2 upstream conversion lineage or a corrected initial release.\n\n'
   tensors='# OmniCoder: complete per-tensor numerical comparison\n\n[Scope, artifact identities, methods and limits](../weight-integrity.md). These are CPU reconstruction differences, not benchmark performance or training-delta significance tests. Full payload hashes and decoder controls are in the public benchmark register.\n\n'
   tensors+=table(['Tensor','V1 / V2','Values','Changed values','RMSE','Max abs','Relative L2 V1'],[[r['name'],r['type_A']+' / '+r['type_B'],r['parameters'],r['changed_values_exact'],r['rmse'],r['max_abs_difference'],r['relative_l2_A']] for r in a['tensor_results']]);write(docs/'artifact-reviews/omnicoder-tensors.md',tensors)
  write(docs/'weight-integrity.md',review)
 write(docs/'configuration-comparison.md',page)
 archive='# Configuration archive\n\nPlans, configuration attempts and profiles without benchmark result records are preserved here, separately from the [measured-result master table](configuration-comparison.md). Execution evidence does not imply a scored benchmark or qualification.\n\n<div id="configuration-history"></div>\n\n## Profiles without benchmark result records\n\n'
 archive+=table(['Model','Immutable profile','Evidence'],[[p['model']['name'],'['+p['runtime_configuration_id'][:20]+'](configuration-profiles/'+p['runtime_configuration_id']+'.md)','No benchmark result in history.runs; inspect archived attempt evidence'] for p in history['profiles'] if p['runtime_configuration_id'] not in measured_ids])
 write(docs/'configuration-archive.md',archive)
 profiles={p['runtime_configuration_id']:p for p in history['profiles']}
 # Remove only stale generated previews; append-only ledger profiles remain retained.
 for stale in (docs/'configuration-profiles').glob('cfg-*.md'):
  if re.fullmatch(r'cfg-[a-f0-9]{64}',stale.stem) and stale.stem not in profiles:stale.unlink()
 for ident,p in profiles.items():
  runs=[r for r in history['runs'] if r['runtime_configuration_id']==ident];attempts=[a for a in history['attempts'] if a['runtime_configuration_id']==ident]
  annotations=[e for e in history.get('configuration_evidence',[]) if e['runtime_configuration_id']==ident]
  s='# '+str(p['model']['name'])+' · '+ident[:16]+'\n\n[Back to configuration comparison](../configuration-comparison.md)\n\nProfile ID: `'+ident+'`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.\n\n'
  for title,key in [('Model and weights','model'),('Engine and backend','engine'),('Optimizations','optimizations'),('Runtime and sampler','runtime'),('Ordered startup parameters','start_parameters')]:
   s+='## '+title+'\n\n```json\n'+pretty(p[key])+'\n```\n\n'
  s+='## Results and original audits\n\n'+table(['Experiment','Benchmark / scope','Success','Wall s','GPU J / success','Peak VRAM MiB','Original audits'],[[r['experiment_id'],r['benchmark_id']+' / '+r['status'],str(r['solved'])+'/'+str(r['tasks']),r['wall_s'],r['gpu_j_per_success'],r['peak_vram_mib'],audit_links(r['audit_ids'],'../')] for r in runs])
  s+='Separate benchmark qualification audits: '+audit_links([r.get('qualification_audit_id') for r in runs],'../')+'\n\n'
  s+=table(['Experiment / arm','Execution evidence','Scientific decision','Original audit'],[[a['experiment_id']+' / '+str(a['arm_index']),a['execution_status'],a['scientific_status'],audit_links([a['audit_id']],'../')] for a in attempts])
  if annotations:
   s+='## Additional hash-bound execution evidence\n\nThese observations supplement the original immutable profile; they do not assign a release version to an unidentified historical build. Declared plan controls, observed request settings and executed sampler settings remain separate.\n\n```json\n'+pretty(annotations)+'\n```\n\n'
   s+='Evidence metadata: '+audit_links(sorted({src['authority_audit_id'] for e in annotations for src in e['sources']}),'../')+'\n\n'
  timings=[e for e in history.get('measurement_evidence',[]) if e['runtime_configuration_id']==ident]
  if timings:s+='## Recorded engine timings and energy denominator\n\n```json\n'+pretty(timings)+'\n```\n\n'
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
 payload={'register':register,'history':history,'models':models,'master':master_catalog(register,history)}
 write(assets/'leaderboard-data.js','window.V100Leaderboard='+json.dumps(payload,ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')+';\n')
