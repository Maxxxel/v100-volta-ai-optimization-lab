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
 flags=t['runtime_flags'];env=t['environment_knobs'];kwargs=metadata['chat_template_kwargs'] if 'chat_template_kwargs' in metadata else plan.get('chat_template_kwargs')
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
 workload_sha=campaign.get('source_workload_sha256')
 if workload_sha is None:
  # One-session campaigns bind the original workload via the immutable broker
  # trust snapshot instead of rewriting an already submitted experiment plan.
  first=pathlib.Path(a['parts'][0]['audit_path']).parent;snapshot=first/'TRUST_SNAPSHOT.json';pins=read(first/'RAW_HASHES.json')
  if digest(snapshot)!=pins.get('TRUST_SNAPSHOT.json'):raise ValueError('Native workload snapshot changed')
  descriptor=read(snapshot)['task_datasets'][campaign['dataset']]
  if descriptor['task_ids']!=expected or descriptor.get('task_count')!=164 or descriptor.get('original_workload_sha256')!=a.get('source_workload_sha256'):raise ValueError('Native workload identity missing or mismatched')
  workload_sha=descriptor['original_workload_sha256']
 energy=sum(energies) if all(v is not None for v in energies) else None;scope=a['scopes']['standard_full164']
 if scope['tasks']!=164 or not math.isclose(scope['wall_s'],wall,rel_tol=1e-10) or (scope['gpu_energy_j'] is None)!=(energy is None) or energy is not None and not math.isclose(scope['gpu_energy_j'],energy,rel_tol=1e-10):raise ValueError('Native aggregate costs mismatch')
 return {'record_schema_version':SCHEMA,'benchmark_id':bench['benchmark_id'],'benchmark_identity_id':definition_identity(bench),'benchmark_revision':bench['benchmark_revision'],'dataset_split_hash':bench['dataset_split_hash'],'evaluated_task_set_hash':workload_sha,'scorer_version':{'adapter_sha256':helper},'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':a['experiment_id'],'audit_hash':source['audit_sha256'],'audit_ids':audits,'source_audit_hashes':hashes,'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'discipline':'coding','tasks':164,'solved':solved,'score_percent':100*solved/164,'metric':'observed_success_percent','wall_s':wall,'gpu_j':energy,'gpu_j_per_success':energy/solved if energy is not None and solved else None,'peak_vram_mib':max(peaks),'repeat_range':None,'date':a['at_utc'][:10],'status':'FULL_NATIVE_CODING_OFFICIAL_API_PENDING','status_reason':'All164 original answers and per-part scoring/costs verified; independent official API qualification is separate.','official_eligible':False,'qualification_audit':None,'warning':'Declared native template/sampling and local output/context limits apply. No publisher-protocol equivalence, model superiority or causal optimization benefit is implied. Monitoring corrections and data recovery remain in original audit lineage.','causal_optimization_proof':None,'measurement_conditions':{'hardware':'Tesla V100-SXM2 16 GB HBM2','cache_condition':'Completion HTTP intervals; startup, warmups and CPU evaluation excluded; see original per-request cache setting.','date':a['at_utc'][:10],'output_cap':cfg['runtime']['max_output'],'sampling':cfg['runtime']['sampling'],'power_limit_w':cfg['runtime']['power_limit_w']}}

def counter_energy_bounds(telemetry, records, selected_ids):
 """Reported NVML-counter bounds, no interpolation; include within-group setup."""
 import bisect
 if not telemetry or len(telemetry)<2 or any(type(t.get('gpu_energy_counter_mj')) is not int or t['gpu_energy_counter_mj']<0 or type(t.get('at_ns')) is not int or type(t.get('nvml_begin_ns')) is not int or t['nvml_begin_ns']>t['at_ns'] for t in telemetry):raise ValueError('Missing counter/query timestamps')
 ends=[t['at_ns'] for t in telemetry];begins=[t['nvml_begin_ns'] for t in telemetry];energy=[t['gpu_energy_counter_mj'] for t in telemetry]
 if any(ends[i]<=ends[i-1] or begins[i]<=begins[i-1] or energy[i]<energy[i-1] for i in range(1,len(energy))) or energy[-1]<=energy[0]:raise ValueError('Counter reset or unordered/nonadvancing trace')
 ids=[r['id'] for r in records];chosen=set(selected_ids)
 if not selected_ids or len(chosen)!=len(selected_ids) or len(set(ids))!=len(ids) or any(i not in ids for i in selected_ids):raise ValueError('Missing or repeated selected counter tasks')
 groups=[];active=None;request_ns=0;last=None
 for r in records:
  a,b=r['start_ns'],r['end_ns']
  if type(a) is not int or type(b) is not int or a>=b or last is not None and a<last:raise ValueError('Unordered/invalid request interval')
  last=b
  if r['id'] in chosen:
   request_ns+=b-a
   if active is None:active=[a,b];groups.append(active)
   else:active[1]=b
  else:active=None
 low=high=duration=0
 for a,b in groups:
  before_a=bisect.bisect_right(ends,a)-1;after_a=bisect.bisect_left(begins,a);before_b=bisect.bisect_right(ends,b)-1;after_b=bisect.bisect_left(begins,b)
  if min(before_a,before_b)<0 or max(after_a,after_b)>=len(energy):raise ValueError('Counter boundaries not bracketed')
  lower=max(0,energy[before_b]-energy[after_a]);upper=energy[after_b]-energy[before_a]
  if upper<lower:raise ValueError('Invalid counter bounds')
  low+=lower;high+=upper;duration+=b-a
 return {'method':'NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1','tasks':len(selected_ids),'groups':len(groups),'lower_j':low/1000,'upper_j':high/1000,'group_window_s':duration/1e9,'complete_request_s':request_ns/1e9,'included_between_request_setup_s':(duration-request_ns)/1e9,'max_query_duration_s':max(t['at_ns']-t['nvml_begin_ns'] for t in telemetry)/1e9,'scope':'Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.'}

def native_reused_tool_run(root,source,cfg,bench,receipt):
 """Full/partial quality is separate from costs measured only on new requests."""
 root=pathlib.Path(root);ap=pathlib.Path(source['audit_path']);ap=ap if ap.is_absolute() else root/ap
 if digest(ap)!=source['audit_sha256']:raise ValueError('Reused tool audit changed')
 a=read(ap);stage=ap.parent;plan=read(stage/'CAMPAIGN_PLAN.json');reuse=read(stage/'REUSE_VALIDATION.json');rp=stage/'REUSED_RESPONSES.jsonl';merged=stage/'MERGED_RESPONSES.jsonl';sp=stage/'SCORING_PLAN.json';scoreplan=read(sp)
 if digest(stage/'CAMPAIGN_PLAN.json')!=a['campaign_plan_sha256'] or cfg['source_plan_sha256']!=a['campaign_plan_sha256'] or digest(stage/'CONFIGURATION_PROFILE.json')!=a['runtime_configuration_profile_sha256'] or read(stage/'CONFIGURATION_PROFILE.json')!=cfg:raise ValueError('Reused tool profile/campaign changed')
 if digest(stage/'REUSE_VALIDATION.json')!=plan['reuse_validation_sha256'] or digest(rp)!=plan['reused_responses_sha256'] or digest(merged)!=a['merged_responses_sha256'] or digest(sp)!=a['scoring_plan_sha256']:raise ValueError('Reused tool response/plan changed')
 if reuse['quality_filtering'] is not False or reuse['status']!='FROZEN_CATEGORY_REUSE_SOURCE_AND_RECIPE_VERIFIED' or len(a['parts'])!=1 or a['new_model_starts']!=1:raise ValueError('Unreviewed or filtered reuse')
 for file,h in reuse['source_files_sha256'].items():
  if digest(file)!=h:raise ValueError('Reused tool original witness changed')
 part=a['parts'][0];gp=pathlib.Path(part['audit_path']);out=gp.parent
 if digest(gp)!=part['audit_sha256']:raise ValueError('Reused tool GPU audit changed')
 gpu=read(gp);native=read(out/'profile.json');launch=read(out/'LAUNCH.json');contract=read(out/'CONTRACT.json');snapshot=read(out/'TRUST_SNAPSHOT.json');descriptor=snapshot['task_datasets'][bench['benchmark_id']];pins=read(out/'RAW_HASHES.json')
 for name in ('profile.json','LAUNCH.json','CONTRACT.json','HTTP_RESULTS.jsonl'):
  if digest(out/name)!=pins[name]:raise ValueError('Reused tool raw source changed')
 verify_broker_capture(cfg,native,launch)
 if gpu.get('measurement_valid') is not True or gpu.get('GPU_execution_observed') is not True or launch['uid']!=65534 or native.get('adapter')!='llama-native-tools':raise ValueError('Reused tool GPU execution unverified')
 if H({k:v for k,v in native.items() if k!='selected_task_inputs'})!=plan['immutable_profile_identity_sha256']:raise ValueError('Reused tool native snapshot changed')
 def inference(p):
  q={k:v for k,v in p.items() if k not in ('execution_review','review','task_time_policy','selected_task_inputs')};q['native_recipe']={k:v for k,v in p['native_recipe'].items() if k not in ('maximum_tasks','maximum_generation_requests','maximum_runtime_seconds')};return q
 review=read(stage/'EXECUTION_REVIEW.json');base=snapshot['profiles'][review['parent_profile']]
 if H(base)!=plan['base_profile_identity_sha256'] or H(base)!=reuse['base_profile_identity_sha256'] or inference(native)!=inference(base):raise ValueError('Reused tool historical inference profile differs')
 if descriptor['source_question_file_sha256']!=bench['dataset_split_hash'] or descriptor['source_answer_file_sha256']!=bench['reference_answers_sha256'] or descriptor['source_revision']!=bench['benchmark_revision']:raise ValueError('Reused tool benchmark revision differs')
 tasks=pathlib.Path(descriptor['tasks_file']);tools=pathlib.Path(descriptor['tools_file']);prep=root/'staging/leaderboard-register/bfcl-simple-python400/PREPARATION_AUDIT.json'
 if digest(prep)!=bench['preparation_audit_sha256'] or digest(tasks)!=descriptor['tasks_sha256'] or digest(tools)!=descriptor['tools_sha256'] or descriptor['tasks_sha256']!=read(prep)['TASKS_sha256'] or descriptor['tools_sha256']!=read(prep)['TOOLS_sha256']:raise ValueError('Reused tool corpus differs')
 old=[json.loads(l) for l in rp.read_text().splitlines()];fresh=[r for r in map(json.loads,(out/'HTTP_RESULTS.jsonl').read_text().splitlines()) if r.get('kind')=='native_tool']
 if not fresh:return None
 oldids=[r['id'] for r in old];newids=[r['id'] for r in fresh];expected=plan['expected_task_ids']
 if oldids!=plan['reused_task_ids'] or oldids!=reuse['reused_task_ids'] or len(oldids)!=40 or set(oldids).intersection(newids) or newids!=plan['new_task_ids'][:len(newids)] or contract['parameters']['task_ids']!=plan['new_task_ids']:raise ValueError('Reused tool task coverage differs')
 if plan['new_task_ids']!=[i for i in expected if i not in oldids] or reuse['remaining_task_ids']!=plan['new_task_ids']:raise ValueError('Reused tool missing-task complement differs')
 byid={r['id']:r for r in old+fresh};ids=[i for i in expected if i in byid];observed=[json.loads(l) for l in merged.read_text().splitlines()]
 if len(byid)!=len(old)+len(fresh) or observed!=[byid[i] for i in ids] or scoreplan['case_ids']!=ids or scoreplan['responses_sha256']!=digest(merged) or scoreplan['new_responses_sha256']!=digest(out/'HTTP_RESULTS.jsonl') or scoreplan['reused_responses_sha256']!=digest(rp):raise ValueError('Reused tool merged answers differ')
 full=len(ids)==bench['required_task_count'] and H(sorted(ids))==bench['expected_task_ids_hash']
 if full!=a['full_benchmark_score_claimed'] or a['collected_tasks']!=len(ids) or a['scored_tasks']!=len(ids):raise ValueError('Reused tool partial/full counts differ')
 if full:
  completion=read(out/'HOST_COMPLETION.json')
  if completion['status']!='GPU_COMPLETE_AUDITED' or completion['audit_sha256']!=digest(gp):raise ValueError('Reused tool new360 completion missing')
 original={r['id']:r for r in read(tasks)['tasks']};schemas={r['id']:r for r in read(tools)['tasks']}
 for ident,row in byid.items():
  if row['request']!={**native['native_recipe']['request_options'],'messages':original[ident]['messages'],'tools':schemas[ident]['tools']}:raise ValueError('Reused tool original request differs')
 if scoreplan['worker_sha256']!=bench['scorer_version']['native_score_wrapper_sha256'] or scoreplan['official_utils_sha256']!=bench['scorer_version']['official_native_format_sha256'] or digest(stage/'score_native.py')!=scoreplan['worker_sha256'] or digest(stage/'OFFICIAL_BFCL_UTILS.txt')!=scoreplan['official_utils_sha256']:raise ValueError('Reused tool official scorer differs')
 for file,key in [('quality_eval_frozen.py','frozen_checker_adapter_sha256'),('BFCL_ANALYSIS_SUBSET.tar','frozen_checker_bundle_sha256')]:
  if digest(root/'staging/r281'/file)!=bench['scorer_version'][key]:raise ValueError('Reused tool unreviewed checker')
 required={str(root/'staging/bfcl/INPUTS.tar'),str(root/'staging/r281/BFCL_ANALYSIS_SUBSET.tar'),str(root/'staging/r281/quality_eval_frozen.py'),str(merged),str(tasks),str(stage/'OFFICIAL_BFCL_UTILS.txt'),str(sp),str(stage/'score_native.py')};scored=[]
 for entry in a['scoring_receipts']:
  stdout=stage/(entry['label']+'.stdout');receiptfile=stage/(entry['label']+'.receipt.json');execution=read(receiptfile)
  if digest(stdout)!=entry['stdout_sha256'] or digest(receiptfile)!=entry['receipt_sha256'] or execution['returncode']!=0 or 'Result=success' not in execution['properties'] or set(execution['input_sha256'])!=required:raise ValueError('Reused tool CPU receipt differs')
  for file,h in execution['input_sha256'].items():
   if digest(file)!=h:raise ValueError('Reused tool CPU input differs')
  rows=[json.loads(l) for l in stdout.read_text().splitlines()];decisions=[r for r in rows if 'id' in r]
  if [r['id'] for r in decisions]!=ids or rows[-1]['tasks']!=len(ids) or rows[-1].get('official_revision')!=bench['benchmark_revision'] or rows[-1].get('official_functions_modified') is not False or rows[-1].get('model_requests')!=0 or rows[-1].get('tool_executions')!=0:raise ValueError('Reused tool scoring coverage/provenance differs')
  scored.append(rows)
 if len(scored)!=2 or scored[0]!=scored[1] or a['changed_replay_judgements']:raise ValueError('Reused tool replay differs')
 decisions={r['id']:r for r in scored[0] if 'id' in r};solved=sum(decisions[i]['official_AST_success'] for i in ids);newsolved=sum(decisions[i]['official_AST_success'] for i in newids)
 if solved!=a['solved_observed_tasks'] or sum(decisions[i]['official_AST_success'] for i in oldids)!=reuse['existing_official_AST_solved'] or a['practical_solved']!=scored[0][-1]['practical_solved']:raise ValueError('Reused tool quality counts differ')
 costs={r['id']:r for r in gpu['per_task']}
 if set(costs)!=set(newids) or gpu['case_ids']!=newids or gpu['execution_uid']!=65534 or gpu['model_starts']!=1:raise ValueError('Reused tool cost task set differs')
 for r in fresh:
  if not finite(r['e2e_s']) or r['e2e_s']<=0 or not math.isclose(costs[r['id']]['e2e_s'],r['e2e_s'],rel_tol=1e-10):raise ValueError('Reused tool request timing differs')
 wall=sum(costs[i]['e2e_s'] for i in newids);energy=sum(costs[i]['gpu_energy_j'] for i in newids) if all(costs[i].get('energy_complete') is True and finite(costs[i].get('gpu_energy_j')) for i in newids) else None;perf=a['matched_performance']
 if perf['tasks']!=len(newids) or perf['solved']!=newsolved or perf['task_ids_hash']!=H(sorted(newids)) or not math.isclose(perf['wall_s'],wall,rel_tol=1e-10) or perf['gpu_j']!=energy or perf['gpu_j_per_success']!=(energy/newsolved if energy is not None and newsolved else None):raise ValueError('Reused tool matched cost scope/count differs')
 if perf['successful_tasks_per_s']!=newsolved/wall or perf['peak_vram_mib']!=gpu['peak_device_vram_mib']:raise ValueError('Reused tool success rate/VRAM differs')
 timing=[r['reply'].get('timings',{}) for r in fresh]
 for name,nkey,tkey in [('prefill','prompt_n','prompt_ms'),('decode','predicted_n','predicted_ms')]:
  if name+'_tok_s' in perf:
   if not all(finite(t.get(nkey)) and t[nkey]>=0 and finite(t.get(tkey)) and t[tkey]>0 for t in timing) or not math.isclose(perf[name+'_tok_s'],1000*sum(t[nkey] for t in timing)/sum(t[tkey] for t in timing),rel_tol=1e-12):raise ValueError('Reused tool scoped token rate differs')
 counter_reference=None
 energy_review=source.get('energy_counter_review')
 if energy_review:
  import inspect
  ep=pathlib.Path(energy_review['path']);ep=ep if ep.is_absolute() else root/ep
  if digest(ep)!=energy_review['sha256']:raise ValueError('Counter energy review changed')
  er=read(ep)
  if er['status']!='BOUNDED_REPORTED_HARDWARE_COUNTER_ENERGY' or er['GPU_runs']!=0 or er['model_requests']!=0 or er['counter_unit']!='mJ' or er['source_API']!='nvmlDeviceGetTotalEnergyConsumption' or er['selected_task_ids']!=newids or er['source_function_sha256']!=hashlib.sha256(inspect.getsource(counter_energy_bounds).encode()).hexdigest():raise ValueError('Unverified counter energy method/scope')
  for file,h in er['source_files_sha256'].items():
   if digest(file)!=h:raise ValueError('Counter energy original source changed')
  newbounds=counter_energy_bounds([json.loads(l) for l in (out/'GPU_TELEMETRY.jsonl').read_text().splitlines()],fresh,newids)
  for k,v in newbounds.items():
   if er['Bonsai_R455'][k]!=v:raise ValueError('Counter energy candidate bounds differ')
  if er['Bonsai_R455']['solved']!=newsolved or er['Bonsai_R455']['j_per_success_lower']!=newbounds['lower_j']/newsolved or er['Bonsai_R455']['j_per_success_upper']!=newbounds['upper_j']/newsolved:raise ValueError('Counter energy success denominator differs')
  la=read(root/'staging/r453/AUDIT.json');lg=pathlib.Path(la['parts'][0]['audit_path']).parent;lrows=[r for r in map(json.loads,(lg/'HTTP_RESULTS.jsonl').read_text().splitlines()) if r.get('kind')=='native_tool'];lb=counter_energy_bounds([json.loads(l) for l in (lg/'GPU_TELEMETRY.jsonl').read_text().splitlines()],lrows,newids);lj={r['id']:r for r in map(json.loads,(root/'staging/r453/r453-native-score.stdout').read_text().splitlines()) if 'id' in r};lsolved=sum(lj[i]['official_AST_success'] for i in newids)
  for k,v in lb.items():
   if er['LFM_R453'][k]!=v:raise ValueError('Counter energy reference bounds differ')
  if er['LFM_R453']['solved']!=lsolved or er['LFM_R453']['j_per_success_lower']!=lb['lower_j']/lsolved or er['LFM_R453']['j_per_success_upper']!=lb['upper_j']/lsolved:raise ValueError('Counter energy reference denominator differs')
  perf=copy.deepcopy(perf);perf['counter_energy']=er['Bonsai_R455'];counter_reference={'experiment_id':'R453','runtime_configuration_id':la['runtime_configuration_id'],'counter_energy':er['LFM_R453'],'audit_id':receipt(root/'staging/r453/AUDIT.json',digest(root/'staging/r453/AUDIT.json')),'kind':'Same tasks, stored native profile; no balanced A/B or causal claim'}
 audits=[receipt(ap,digest(ap)),receipt(gp,digest(gp)),receipt(stage/'REUSE_VALIDATION.json',digest(stage/'REUSE_VALIDATION.json'))]
 if energy_review:audits.append(receipt(ep,digest(ep)))
 if not all(audits):raise ValueError('Reused tool original audit unavailable')
 return {'record_schema_version':SCHEMA,'benchmark_id':bench['benchmark_id'],'benchmark_identity_id':definition_identity(bench),'benchmark_revision':bench['benchmark_revision'],'dataset_split_hash':bench['dataset_split_hash'],'evaluated_task_set_hash':H(sorted(ids)),'evaluated_task_ids':ids,'scorer_version':bench['scorer_version'],'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':a['experiment_id'],'audit_hash':digest(ap),'audit_ids':audits,'source_audit_hashes':[digest(ap),digest(gp),digest(stage/'REUSE_VALIDATION.json')],'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'discipline':'tools','tasks':len(ids),'intended_tasks':400,'solved':solved,'score_percent':100*solved/len(ids),'metric':bench['metric'],'wall_s':None,'gpu_j':None,'gpu_j_per_success':None,'peak_vram_mib':gpu['peak_device_vram_mib'],'repeat_range':None,'date':a['at_utc'][:10],'status':'FULL_NATIVE_TOOLS_REUSE_OFFICIAL_API_PENDING' if full else 'PARTIAL','status_reason':'All preserved and new task replies independently replayed. Full fresh400 performance is not measured; new-task costs have their own explicit denominator.','official_eligible':False,'qualification_audit':None,'full_benchmark_score_claimed':full,'matched_performance':perf,'matched_reference':counter_reference,'practical_protocol':{'solved':a['practical_solved'],'valid':a['protocol_valid'],'complete':a['complete'],'tasks':len(ids)},'warning':'Only one BFCL category. Quality includes40 verified original replies; measured performance covers new tasks only, not a fresh400 run or causal speedup. Interrupted/uncollected tasks are unmeasured, never zero. No Champion claim.','causal_optimization_proof':None,'measurement_conditions':{'hardware':'Tesla V100-SXM2 16 GB HBM2','quality_tasks':len(ids),'performance_tasks':len(newids),'cache_condition':'New complete-request intervals only; excludes startup, warmup, CPU scoring and any incomplete trailing request. Historical timing is not pooled.','date':a['at_utc'][:10],'output_cap':cfg['runtime']['max_output'],'sampling':cfg['runtime']['sampling'],'power_limit_w':cfg['runtime']['power_limit_w']}}

def reviewed_counter_measurement(source,out,ids,solved,receipt):
 """Optional bounded-counter supplement; never replaces a failed power integral."""
 descriptor=source.get('energy_counter_review')
 if not descriptor:return None
 import inspect
 path=pathlib.Path(descriptor['path'])
 if digest(path)!=descriptor['sha256']:raise ValueError('Counter supplement receipt changed')
 review=read(path)
 if review.get('status')!='BOUNDED_REPORTED_HARDWARE_COUNTER_ENERGY' or review.get('GPU_runs')!=0 or review.get('model_requests')!=0 or review.get('source_API')!='nvmlDeviceGetTotalEnergyConsumption' or review.get('counter_unit')!='mJ' or review.get('selected_task_ids')!=ids or review.get('source_function_sha256')!=hashlib.sha256(inspect.getsource(counter_energy_bounds).encode()).hexdigest():raise ValueError('Counter supplement method/task identity differs')
 for name,h in review['source_files_sha256'].items():
  if digest(name)!=h:raise ValueError('Counter supplement source changed')
 required=[out/'HTTP_RESULTS.jsonl',out/'GPU_TELEMETRY.jsonl']
 if any(review['source_files_sha256'].get(str(p))!=digest(p) for p in required):raise ValueError('Counter supplement lacks original response/telemetry bindings')
 rows=[r for r in map(json.loads,(out/'HTTP_RESULTS.jsonl').read_text().splitlines()) if r.get('kind')=='native_tool'];observed=counter_energy_bounds([json.loads(l) for l in (out/'GPU_TELEMETRY.jsonl').read_text().splitlines()],rows,ids);claimed=review['measurement']
 if any(claimed.get(k)!=v for k,v in observed.items()) or claimed.get('solved')!=solved or claimed.get('j_per_success_lower')!=(observed['lower_j']/solved if solved else None) or claimed.get('j_per_success_upper')!=(observed['upper_j']/solved if solved else None):raise ValueError('Counter supplement bounds/success denominator differ')
 aid=receipt(path,digest(path))
 if not aid:raise ValueError('Counter supplement audit unavailable')
 return {**claimed,'audit_id':aid}

def native_tool_run(root,source,cfg,bench,receipt):
 """One native BFCL category, bound to original inputs, responses and CPU receipts."""
 if source.get('benchmark_id')!='bfcl-v4-simple-python-full400':return None
 root=pathlib.Path(root);ap=pathlib.Path(source['audit_path']);ap=ap if ap.is_absolute() else root/ap
 if digest(ap)!=source['audit_sha256']:raise ValueError('Native tool audit changed')
 a=read(ap);stage=ap.parent;campaign=read(stage/'CAMPAIGN_PLAN.json');cp=stage/'CONFIGURATION_PROFILE.json'
 if digest(stage/'CAMPAIGN_PLAN.json')!=a['campaign_plan_sha256'] or digest(cp)!=a['runtime_configuration_profile_sha256'] or read(cp)!=cfg:raise ValueError('Native tool configuration lineage changed')
 if cfg['source_plan_sha256']!=a['campaign_plan_sha256'] or len(a['parts'])!=1 or a['model_starts']!=1:raise ValueError('Native tool single-session evidence missing')
 part=a['parts'][0];gp=pathlib.Path(part['audit_path']);out=gp.parent
 if digest(gp)!=part['audit_sha256']:raise ValueError('Native tool GPU audit changed')
 gpu=read(gp);completion=read(out/'HOST_COMPLETION.json');pins=read(out/'RAW_HASHES.json');native=read(out/'profile.json');launch=read(out/'LAUNCH.json');contract=read(out/'CONTRACT.json')
 if completion['status']!='GPU_COMPLETE_AUDITED' or completion['audit_sha256']!=digest(gp) or gpu.get('measurement_valid') is not True or gpu.get('GPU_execution_observed') is not True:raise ValueError('Native tool GPU execution not proven')
 for name in ('HTTP_RESULTS.jsonl','profile.json','LAUNCH.json','CONTRACT.json'):
  if digest(out/name)!=pins[name]:raise ValueError('Native tool raw identity changed')
 verify_broker_capture(cfg,native,launch)
 if native['adapter']!='llama-native-tools' or H({k:v for k,v in native.items() if k!='selected_task_inputs'})!=campaign['immutable_profile_identity_sha256']:raise ValueError('Native tool adapter/profile mismatch')
 dataset=read(out/'TRUST_SNAPSHOT.json')['task_datasets'][bench['benchmark_id']]
 if dataset['source_question_file_sha256']!=bench['dataset_split_hash'] or dataset['source_answer_file_sha256']!=bench['reference_answers_sha256'] or dataset['source_revision']!=bench['benchmark_revision']:raise ValueError('Native tool dataset revision mismatch')
 if digest(dataset['tasks_file'])!=dataset['tasks_sha256'] or digest(dataset['tools_file'])!=dataset['tools_sha256']:raise ValueError('Native tool corpus changed')
 preparation=root/'staging/leaderboard-register/bfcl-simple-python400/PREPARATION_AUDIT.json'
 if digest(preparation)!=bench['preparation_audit_sha256']:raise ValueError('Native tool conversion review changed')
 prepared=read(preparation)
 if dataset['tasks_sha256']!=prepared['TASKS_sha256'] or dataset['tools_sha256']!=prepared['TOOLS_sha256']:raise ValueError('Native tool unreviewed transformed corpus')
 for name,key in [('quality_eval_frozen.py','frozen_checker_adapter_sha256'),('BFCL_ANALYSIS_SUBSET.tar','frozen_checker_bundle_sha256')]:
  if digest(root/'staging/r281'/name)!=bench['scorer_version'][key]:raise ValueError('Native tool unreviewed checker')
 cases={x['id']:x for x in native['selected_task_inputs']['cases']};rows=[json.loads(l) for l in (out/'HTTP_RESULTS.jsonl').read_text().splitlines()];answers=[x for x in rows if x.get('kind')=='native_tool'];ids=[x['id'] for x in answers]
 if ids!=contract['parameters']['task_ids'] or ids!=campaign['expected_task_ids'] or len(set(ids))!=len(ids):raise ValueError('Native tool missing or repeated tasks')
 full=len(ids)==bench['required_task_count'] and H(sorted(ids))==bench['expected_task_ids_hash']
 if not full or a['collected_tasks']!=len(ids) or a['scored_tasks']!=len(ids) or a['full_benchmark_score_claimed'] is not True:raise ValueError('Native tool category not complete')
 original_cases={x['id']:x for x in read(dataset['tasks_file'])['tasks']};original_tools={x['id']:x for x in read(dataset['tools_file'])['tasks']}
 for r in answers:
  case=cases[r['id']];original=original_cases[r['id']];tools=original_tools[r['id']]
  if case['messages']!=original['messages'] or case['tools']!=tools['tools'] or case['original_question_sha256']!=original['original_question_sha256'] or case['native_tools_sha256']!=original['expected_native_tools_sha256'] or H(case['tools'])!=tools['tools_sha256']:raise ValueError('Native tool original task/schema mismatch')
  body={**native['native_recipe']['request_options'],'messages':case['messages'],'tools':case['tools']}
  if r['request']!=body or r['request_sha256']!=H(body):raise ValueError('Native tool input changed')
 scoreplan=read(stage/'SCORING_PLAN.json')
 if digest(stage/'SCORING_PLAN.json')!=a['scoring_plan_sha256'] or scoreplan['responses_sha256']!=digest(out/'HTTP_RESULTS.jsonl') or scoreplan['case_ids']!=ids:raise ValueError('Native tool scorer input changed')
 if scoreplan['worker_sha256']!=bench['scorer_version']['native_score_wrapper_sha256'] or scoreplan['official_utils_sha256']!=bench['scorer_version']['official_native_format_sha256']:raise ValueError('Native tool official scorer changed')
 required={str(root/'staging/bfcl/INPUTS.tar'),str(root/'staging/r281/BFCL_ANALYSIS_SUBSET.tar'),str(root/'staging/r281/quality_eval_frozen.py'),str(out/'HTTP_RESULTS.jsonl'),dataset['tasks_file'],str(stage/'OFFICIAL_BFCL_UTILS.txt'),str(stage/'SCORING_PLAN.json'),str(stage/'score_native.py')}
 scored=[]
 for entry in a['scoring_receipts']:
  label=entry['label'];stdout=stage/(label+'.stdout');rp=stage/(label+'.receipt.json');execution=read(rp)
  if digest(stdout)!=entry['stdout_sha256'] or digest(rp)!=entry['receipt_sha256'] or execution['returncode']!=0 or 'Result=success' not in execution['properties'] or 'ExecMainStatus=0' not in execution['properties']:raise ValueError('Native tool CPU scoring receipt invalid')
  if set(execution['input_sha256'])!=required:raise ValueError('Native tool CPU dependencies incomplete')
  for file,h in execution['input_sha256'].items():
   if digest(file)!=h:raise ValueError('Native tool CPU dependency changed')
  if digest(stage/'score_native.py')!=scoreplan['worker_sha256'] or digest(stage/'OFFICIAL_BFCL_UTILS.txt')!=scoreplan['official_utils_sha256']:raise ValueError('Native tool scorer source mismatch')
  observed=[json.loads(l) for l in stdout.read_text().splitlines()];judgements=[x for x in observed if 'id' in x]
  if [x['id'] for x in judgements]!=ids or observed[-1]['tasks']!=len(ids):raise ValueError('Native tool scoring coverage mismatch')
  if observed[-1].get('official_revision')!=bench['benchmark_revision'] or observed[-1].get('official_functions_modified') is not False or observed[-1].get('model_requests')!=0 or observed[-1].get('tool_executions')!=0:raise ValueError('Native tool scorer provenance mismatch')
  if any(type(x['official_AST_success']) is not bool for x in judgements):raise ValueError('Native tool nonboolean score')
  scored.append(observed)
 if len(scored)!=2 or scored[0]!=scored[1] or a['changed_replay_judgements']:raise ValueError('Native tool replay mismatch')
 solved=sum(x['official_AST_success'] for x in scored[0] if 'id' in x)
 if solved!=a['solved_observed_tasks'] or solved!=scored[0][-1]['official_AST_solved']:raise ValueError('Native tool score mismatch')
 if a['practical_solved']!=scored[0][-1]['practical_solved']:raise ValueError('Native tool practical score mismatch')
 costs={x['id']:x for x in gpu['per_task']}
 if set(costs)!=set(ids):raise ValueError('Native tool costs missing')
 for r in answers:
  if not math.isclose(r['e2e_s'],costs[r['id']]['e2e_s'],rel_tol=1e-10,abs_tol=1e-8):raise ValueError('Native tool timing mismatch')
 wall=sum(costs[i]['e2e_s'] for i in ids);energy=sum(costs[i]['gpu_energy_j'] for i in ids) if all(finite(costs[i].get('gpu_energy_j')) and costs[i].get('energy_complete') is True for i in ids) else None
 if not math.isclose(wall,gpu['case_inference_wall_s'],rel_tol=1e-10) or energy!=gpu['case_gpu_energy_j']:raise ValueError('Native tool aggregate metrics mismatch')
 audits=[receipt(ap,digest(ap)),receipt(gp,digest(gp))]
 if not all(audits):raise ValueError('Native tool audit unavailable')
 result={'record_schema_version':SCHEMA,'benchmark_id':bench['benchmark_id'],'benchmark_identity_id':definition_identity(bench),'benchmark_revision':bench['benchmark_revision'],'dataset_split_hash':bench['dataset_split_hash'],'evaluated_task_set_hash':H(sorted(ids)),'evaluated_task_ids':ids,'scorer_version':bench['scorer_version'],'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':a['experiment_id'],'audit_hash':digest(ap),'audit_ids':audits,'source_audit_hashes':[digest(ap),digest(gp)],'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'discipline':'tools','tasks':len(ids),'solved':solved,'score_percent':100*solved/len(ids),'metric':bench['metric'],'wall_s':wall,'gpu_j':energy,'gpu_j_per_success':energy/solved if energy is not None and solved else None,'peak_vram_mib':gpu['peak_device_vram_mib'],'repeat_range':None,'date':a['at_utc'][:10],'status':'FULL_NATIVE_TOOLS_OFFICIAL_API_PENDING','status_reason':'Complete400 native Python category with identical independent CPU replay; official admission is separate.','official_eligible':False,'qualification_audit':None,'warning':'One official BFCL category, not BFCL overall. Practical protocol checks are separate from official AST. No publisher equivalence, unseen holdout, model superiority, causal optimization or Champion claim.','causal_optimization_proof':None,'practical_protocol':{'solved':a['practical_solved'],'valid':a['protocol_valid'],'complete':a['complete'],'tasks':len(ids)},'measurement_conditions':{'hardware':'Tesla V100-SXM2 16 GB HBM2','cache_condition':'Native completion-HTTP intervals; startup/warmup/CPU scoring excluded; per-request native caching in exact recipe.','date':a['at_utc'][:10],'output_cap':cfg['runtime']['max_output'],'sampling':cfg['runtime']['sampling'],'power_limit_w':cfg['runtime']['power_limit_w']}}

 counter=reviewed_counter_measurement(source,out,ids,solved,receipt)
 if counter:result["counter_energy"]=counter;result["audit_ids"].append(counter["audit_id"])
 return result

def native_partial_run(root,source,cfg,bench,receipt):
 """Measured/scored native prefixes stay visible, without full-suite admission."""
 if source.get('full_benchmark_score_claimed') is not False or source.get('status') not in ('STOPPED_USER_WHOLE_BENCHMARK_TIME_BUDGET','STOPPED_USER_TASK_TIME_BUDGET'):return None
 root=pathlib.Path(root);path=pathlib.Path(source['audit_path']);path=path if path.is_absolute() else root/path
 if digest(path)!=source['audit_sha256']:raise ValueError('Partial campaign audit changed')
 a=read(path);stage=root/'staging'/a['experiment_id'].lower();campaign=read(stage/'CAMPAIGN_PLAN.json')
 if digest(stage/'CAMPAIGN_PLAN.json')!=a['campaign_plan_sha256'] or cfg['source_plan_sha256']!=a['campaign_plan_sha256']:raise ValueError('Partial configuration/campaign changed')
 expected=campaign['expected_task_ids'];groups=[];audits=[receipt(path,source['audit_sha256'])];source_hashes=[source['audit_sha256']]
 if a.get('raw_root'):
  out=pathlib.Path(a['raw_root']);score=stage/'scoring/partial';stdout=score/(a['experiment_id'].lower()+'-judge-partial.stdout');execution=score/(a['experiment_id'].lower()+'-judge-partial.receipt.json')
  for name,h in a['raw_files_sha256'].items():
   if digest(out/name)!=h:raise ValueError('Partial raw evidence changed')
  for name,h in a['scoring_files_sha256'].items():
   if digest(score/name)!=h:raise ValueError('Partial score evidence changed')
  groups.append((out,score,stdout,execution,a['prefix_measurement']))
 else:
  bypart={p['part']:p for p in a['parts']}
  for score in a['scoring']:
   part=bypart[score['part']];ap=pathlib.Path(part['audit_path']);sp=pathlib.Path(score['audit_path'])
   if digest(ap)!=part['audit_sha256'] or digest(sp)!=score['audit_sha256']:raise ValueError('Partial component audit changed')
   gpu=read(ap);completion=read(ap.parent/'HOST_COMPLETION.json')
   if completion['status']!='GPU_COMPLETE_AUDITED' or completion['audit_sha256']!=part['audit_sha256'] or gpu.get('measurement_valid') is not True or gpu.get('GPU_execution_observed') is not True:raise ValueError('Partial chunk not executed/audited')
   groups.append((ap.parent,sp.parent,sp.parent/(a['experiment_id'].lower()+f"-judge-part{part['part']:02d}.stdout"),sp.parent/(a['experiment_id'].lower()+f"-judge-part{part['part']:02d}.receipt.json"),gpu))
   audits.extend([receipt(ap,part['audit_sha256']),receipt(sp,score['audit_sha256'])]);source_hashes.extend([part['audit_sha256'],score['audit_sha256']])
 reference=pathlib.Path(source['parts'][0]['audit_path']).parent if source.get('parts') else pathlib.Path(a['raw_root'])
 reference_launch=read(reference/'LAUNCH.json');verify_broker_capture(cfg,read(reference/'profile.json'),reference_launch)
 stable=lambda launch:{'argv':launch['argv'],'environment':{k:v for k,v in launch['environment'].items() if k!='O2_GPU_BUILD_LEASE'},'request_options':launch['native_request_options']}
 ids=[];solved=0;wall=0;energy=0;energy_known=True;peaks=[];helper=None
 for out,score,stdout,execution,gpu in groups:
  native=read(out/'profile.json');launch=read(out/'LAUNCH.json');contract=read(out/'CONTRACT.json');plan=read(score/'SCORING_PLAN.json');samples=score/'JUDGE_SAMPLES.jsonl';raw=out/'HTTP_RESULTS.jsonl'
  if H({k:v for k,v in native.items() if k!='selected_task_inputs'})!=campaign['immutable_profile_identity_sha256']:raise ValueError('Partial native profile drift')
  if stable(launch)!=stable(reference_launch):raise ValueError('Partial launch recipe drift')
  validation_cfg=copy.deepcopy(cfg);validation_cfg['start_parameters']['exact_private_launch_sha256']=H(launch);verify_broker_capture(validation_cfg,native,launch)
  pins=read(out/'RAW_HASHES.json')
  for name in ('LAUNCH.json','profile.json','CONTRACT.json'):
   if digest(out/name)!=pins[name]:raise ValueError('Partial raw configuration changed')
  if cfg['runtime']['power_limit_w']!=contract['power_w'] or cfg['runtime']['execution_deadline_s']!=contract['runtime_seconds']:raise ValueError('Partial runtime limit mismatch')
  if digest(raw)!=plan['raw_answers_sha256'] or digest(samples)!=plan['judge_samples_sha256']:raise ValueError('Partial scorer input changed')
  receipt_data=read(execution)
  if receipt_data['input_sha256'].get(str(samples))!=digest(samples) or receipt_data['input_sha256'].get(str(root/'quality_eval.py'))!=plan['helper_sha256']:raise ValueError('Partial CPU sandbox binding mismatch')
  required_inputs={str(samples),str(root/'quality_eval.py'),str(root/'staging/r101/JUDGE_TASKS.jsonl'),str(root/'staging/r101/calibration3.stdout'),str(root/'staging/r101/calibration5.stdout')}
  if set(receipt_data['input_sha256'])!=required_inputs:raise ValueError('Partial CPU oracle/corpus binding missing')
  for file,h in receipt_data['input_sha256'].items():
   if digest(file)!=h:raise ValueError('Partial CPU dependency changed')
  if helper is not None and helper!=plan['helper_sha256']:raise ValueError('Partial scorer changed across groups')
  helper=plan['helper_sha256'];sample_ids=[x['task_id'] for x in map(json.loads,samples.read_text().splitlines())];judgements=[json.loads(l) for l in stdout.read_text().splitlines()];jids=[x['task_id'] for x in judgements]
  if jids!=sample_ids[:len(jids)] or len(set(jids))!=len(jids) or set(ids).intersection(jids) or not set(jids).issubset(expected):raise ValueError('Partial task IDs repeated or mismatched')
  raw_rows=[json.loads(l) for l in raw.read_text().splitlines()];requests={x['id']:x for x in raw_rows if x.get('kind')=='coding'};costs={x['id']:x for x in gpu['per_task']}
  cases={x['id']:x for x in native['selected_task_inputs']['cases']}
  for ident in jids:
   if ident not in requests or requests[ident]['request']['messages']!=cases[ident]['messages'] or requests[ident]['request']!={**native['native_recipe']['request_options'],'messages':cases[ident]['messages']}:raise ValueError('Partial coding input changed')
   cost=costs[ident]
   if not finite(cost['e2e_s']) or cost['e2e_s']<=0:raise ValueError('Partial request timing missing')
   wall+=cost['e2e_s'];value=cost.get('gpu_energy_j');energy_known=energy_known and finite(value);energy+=value if finite(value) else 0
  ids.extend(jids);solved+=sum(x['checks']['base']['status']==x['checks']['plus']['status']=='pass' for x in judgements);peaks.append(gpu.get('peak_device_vram_mib',a.get('peak_device_vram_mib')))
 if not ids:return None
 if len(ids)>=len(expected) or len(expected)!=164 or any(not x for x in audits):raise ValueError('Invalid partial/full coverage or missing audit')
 if a.get('raw_root') and (len(ids)!=a['scored_tasks'] or solved!=a['solved_observed_tasks']):raise ValueError('Partial scored counts changed')
 energy=energy if energy_known else None;peaks=[x for x in peaks if finite(x)]
 return {'record_schema_version':SCHEMA,'benchmark_id':bench['benchmark_id'],'benchmark_identity_id':definition_identity(bench),'benchmark_revision':bench['benchmark_revision'],'dataset_split_hash':bench['dataset_split_hash'],'evaluated_task_set_hash':H(sorted(ids)),'evaluated_task_ids':ids,'scorer_version':{'adapter_sha256':helper},'model_artifact_id':cfg['model_artifact_id'],'runtime_configuration_id':cfg['runtime_configuration_id'],'experiment_id':a['experiment_id'],'audit_hash':source['audit_sha256'],'audit_ids':audits,'source_audit_hashes':source_hashes,'model_family_id':cfg['model']['family_id'],'model_name':cfg['model']['name'],'discipline':'coding','tasks':len(ids),'intended_tasks':len(expected),'solved':solved,'score_percent':100*solved/len(ids),'metric':'observed_success_percent','wall_s':wall,'gpu_j':energy,'gpu_j_per_success':energy/solved if energy is not None and solved else None,'peak_vram_mib':max(peaks) if peaks else None,'repeat_range':None,'date':a['at_utc'][:10],'status':'PARTIAL','status_reason':'Actual scored task subset under the captured configuration; remaining tasks are unmeasured, never zero.','official_eligible':False,'qualification_audit':None,'full_benchmark_score_claimed':False,'warning':'PARTIAL: different task subsets are not directly comparable full-suite scores. Only hash-bound same-profile scored outputs are included; any additional unbound historical reuse is excluded. Request-window costs exclude startup/scoring.','causal_optimization_proof':None,'measurement_conditions':{'hardware':'Tesla V100-SXM2 16 GB HBM2','cache_condition':'Native completion-HTTP intervals; model startup excluded','date':a['at_utc'][:10],'output_cap':cfg['runtime']['max_output'],'sampling':cfg['runtime']['sampling'],'power_limit_w':cfg['runtime']['power_limit_w']}}

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
  tool_choices=[r.get('tool_choice') for r in all_requests]
  if tool_choices and all(v==tool_choices[0] for v in tool_choices) and tool_choices[0] in ('auto','none','required'):fields['runtime.native_tool_choice_requested']=tool_choices[0]
  kwargs=[r.get('chat_template_kwargs') for r in all_requests]
  if kwargs and all(isinstance(k,dict) and k==kwargs[0] for k in kwargs):
   for k in ('enable_thinking','reasoning_effort','thinking_budget'):
    if k in kwargs[0] and isinstance(kwargs[0][k],(bool,int,float,str)):
     fields['runtime.observed_template_controls.'+k]=kwargs[0][k]
     if k=='enable_thinking' and cfg['runtime'].get('native_template_controls') is None:fields['requested.thinking']=kwargs[0][k]
  joined='\n'.join(logs)
  file_types=set(re.findall(r'^print_info:\s*file type\s*=\s*([A-Z0-9_]+)\s*$',joined,re.M))
  if len(file_types)==1:
   observed_type=next(iter(file_types));fields['model.observed_GGUF_file_type']=observed_type
   if cfg.get('model',{}).get('quantization') in (None,'NOT MEASURED','NICHT ERFASST') and observed_type=='Q8_0':fields['model.quantization']='Q8_0'
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
    if run['discipline']=='coding':selected=[r for r in records if r.get('kind') not in ('input_identity','warmup') and r.get('suite') in (None,'standard') and (r.get('task_id') or r.get('task') or r.get('id') or '').removeprefix('standard:').startswith('HumanEval/')]
    elif run['discipline']=='tools' and pathlib.Path(filename).name=='BFCL.jsonl':selected=records
    elif run['discipline']=='mbpp':selected=[r for r in records if r.get('kind')=='coding' and str(r.get('task','')).lower().startswith(('mbpp','mbppplus'))]
    elif run['discipline'].startswith('long'):selected=[r for r in records if r.get('kind')==('validation' if run['discipline']=='long32k_validation' else 'long')]
    else:selected=[]
    if selected:candidates.append(selected)
   # Duplicated SAMPLES/FUNCTIONAL logs are alternative witnesses, not extra work.
   if cfg.get('source_provenance',{}).get('kind')=='BROKER_NATIVE_CAPTURED_CONFIGURATION':
    measured_ids=set(run.get('evaluated_task_ids',[]))
    candidates=[[r for filename,rows in byfile.items() if pathlib.Path(filename).name=='HTTP_RESULTS.jsonl' for r in rows if r.get('kind')==('native_tool' if run['discipline']=='tools' else 'coding') and (not measured_ids or r.get('id') in measured_ids)]]
   accepted=[]
   for rows in candidates:
    wall=sum(r.get('e2e_s',0) for r in rows)
    ids=[r.get('task_id') or r.get('task') or r.get('id') for r in rows]
    if len(rows)==run['tasks'] and len(set(ids))==len(rows) and finite(run.get('wall_s')) and math.isclose(wall,run['wall_s'],rel_tol=1e-7,abs_tol=1e-5):accepted.append(rows)
   if not accepted:continue
   rows=accepted[0];timings=[(r.get('native_reply') or r.get('reply') or {}).get('timings',{}) for r in rows];values={}
   # Keep the real task phase (including request preparation) distinct from
   # the sum of completion-HTTP windows, without changing immutable run IDs.
   summary=db['summary'].get(run['experiment_id'].lower(),{});phase_source=None
   if summary.get('audit_sha256')==run['audit_hash']:
    original=pathlib.Path(summary['audit_path']);original=original if original.is_absolute() else root/original
    if digest(original)!=run['audit_hash']:raise ValueError('Task-phase original audit changed')
    actual=read(original)
    if finite(actual.get('task_phase_s')) and actual['task_phase_s']>0:
     if actual['task_phase_s']+1e-6<run['wall_s']:raise ValueError('Task phase shorter than recorded request windows')
     values['task_phase_s']=actual['task_phase_s'];values['successful_tasks_per_task_phase_s']=run['solved']/actual['task_phase_s']
     if finite(actual.get('startup_s')):values['startup_s']=actual['startup_s']
     phase_source={'filename':original.name,'sha256':run['audit_hash'],'authority_audit_id':receipt(original,run['audit_hash'])}
   for name,count_key,time_key in [('prefill','prompt_n','prompt_ms'),('decode','predicted_n','predicted_ms')]:
    if all(finite(t.get(count_key)) and t[count_key]>=0 and finite(t.get(time_key)) and t[time_key]>0 for t in timings):
     tokens=sum(t[count_key] for t in timings);ms=sum(t[time_key] for t in timings)
     values[name+'_tok_s']=1000*tokens/ms;values[name+'_tokens']=tokens;values[name+'_engine_ms']=ms
   if 'decode_tokens' in values and values['decode_tokens']>0 and finite(run.get('gpu_j')):values['gpu_j_per_output_token']=run['gpu_j']/values['decode_tokens']
   if values:
    item={'run_id':run['run_id'],'runtime_configuration_id':cid,'values':values,'tasks':len(rows),'wall_sum_s':sum(r['e2e_s'] for r in rows),'sources':sorted({H(s):s for s in sources}.values(),key=H),'aggregation':'Rate = sum of recorded token counts / sum of engine timing seconds for the exact task set; excludes startup/warmup. GPU J/output token uses gross case-window GPU energy including prefill. Engine prefill time is not TTFT. No unseen holdout claim.'}
    if 'task_phase_s' in values:
     item['sources']=sorted({H(s):s for s in [*item['sources'],phase_source]}.values(),key=H)
     item['task_phase_scope']='Recorded audited task phase includes input/template/token preparation between requests; completion-HTTP window sums are separate. Startup/warmup and CPU scoring are excluded from task-phase throughput.'
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

def same_quantizer_review(a,header,rows,plan):
 """Byte equality plus identical typed layouts proves equal decoded GGUF values."""
 if a.get('analysis_id')!='OMNICODER_SAME_QUANTIZER_V1_V2_PAYLOAD_COMPARISON' or a.get('status')!='COMPLETE_ALL_TENSOR_PAYLOADS':raise ValueError('Incomplete same-quantizer review')
 if a.get('new_GPU_runs')!=0 or a.get('new_model_requests')!=0 or a.get('original_weights_modified') is not False or a.get('execution_uid')!=65534 or a.get('V2_input_read_only') is not True:raise ValueError('Unverified read-only CPU comparison')
 if header.get('tensor_descriptors_equal') is not True or header['V1_header']['data_start']!=header['V2_data_start']:raise ValueError('Incompatible tensor layouts')
 tensors=header['V1_header']['tensors']
 if len(rows)!=len(tensors) or len({r['name'] for r in rows})!=len(rows) or {r['name'] for r in rows}!=set(tensors):raise ValueError('Incomplete or duplicate payload census')
 for r in rows:
  t=tensors[r['name']]
  if r['shape']!=t['shape'] or r['type']!=t['type_name'] or r['parameters']!=t['parameters'] or r['payload_bytes']!=t['bytes']:raise ValueError('Wrong tensor payload identity')
  if not re.fullmatch('[A-Za-z0-9_.-]{1,160}',r['name']) or type(r['byte_identical']) is not bool:raise ValueError('Invalid tensor payload record')
  if any(not re.fullmatch('[a-f0-9]{64}',r[k]) for k in ('payload_sha256_V1','payload_sha256_V2')):raise ValueError('Missing payload hash')
  if r['byte_identical']!=(r['payload_sha256_V1']==r['payload_sha256_V2']):raise ValueError('Contradictory tensor equality')
 counts={'compared_tensors':len(rows),'compared_parameters':sum(r['parameters'] for r in rows),'compared_payload_bytes':sum(r['payload_bytes'] for r in rows),'identical_tensor_payloads':sum(r['byte_identical'] for r in rows),'different_tensor_payloads':sum(not r['byte_identical'] for r in rows)}
 if any(a[k]!=v for k,v in counts.items()):raise ValueError('Payload census aggregate mismatch')
 equal=counts['different_tensor_payloads']==0
 verdict='IDENTICAL_MODEL_WEIGHTS_PROVEN_FOR_ALL_STORED_GGUF_TENSORS' if equal else 'DIFFERENT_STORED_PAYLOADS_DEQUANTIZATION_REQUIRED'
 if a['represented_weight_verdict']!=verdict:raise ValueError('Unsupported represented-weight verdict')
 for i,key in enumerate(('V1','V2')):
  if any(a['artifacts'][i][k]!=v for k,v in plan[key].items()) or a['artifacts'][i]['actual_sha256']!=plan[key]['sha256']:raise ValueError('Wrong compared model artifact')
 allowed={'general.name','general.basename','general.source.url','general.url','mradermacher.quantized_at'}
 if not set(header['metadata_differences'])<=allowed:raise ValueError('New metadata difference needs scientific/public review')
 artifacts=[{k:x[k] for k in ('version','repository','revision','filename','bytes','sha256','actual_sha256')} for x in a['artifacts']]
 public_rows=[{k:r[k] for k in ('name','shape','type','parameters','payload_bytes','byte_identical','payload_sha256_V1','payload_sha256_V2')} for r in rows]
 return {'analysis_id':a['analysis_id'],'represented_weight_verdict':verdict,**counts,'artifacts':artifacts,'metadata_differences':header['metadata_differences'],'type_counts':header['V1_header']['type_counts'],'elapsed_s':a['elapsed_s'],'numerical_interpretation':a['numerical_interpretation'],'source_checkpoint_limit':a['source_checkpoint_limit'],'new_GPU_runs':0,'tensor_results':public_rows}

def engine_source_annotations(raw):
 """Recover source revisions from linked build receipts, not binary-name guesses.

 A source base plus local patches is not an upstream release tag. Match both
 executable and CUDA library identities before attaching the annotation.
 """
 main=raw['main-build.json'];contract=raw['main-source-contract.json'];cache=raw['cache-build.json'];patch=raw['cache-patch.json'];bonsai=raw['bonsai-build.json'];bp=raw['bonsai-plan.json']
 if main['source_proof']['commit']!=contract['reference_commit'] or main['source_proof']['source_inputs_sha256']!=contract['reference_inputs_canonical_sha256']:raise ValueError('Engine source contract mismatch')
 if main['source_proof']['source_contract_sha256']!=H_BYTES(raw['_bytes']['main-source-contract.json']):raise ValueError('Engine contract hash mismatch')
 if cache['source_proof']!=patch or patch['parent_manifest_sha256']!=H_BYTES(raw['_bytes']['main-build.json']):raise ValueError('Engine patch ancestry mismatch')
 if pathlib.PurePosixPath(patch['parent']).name!=pathlib.PurePosixPath(main['engine']).parent.parent.name:raise ValueError('Wrong engine patch parent')
 if bonsai['source_commit']!=bp['source_commit'] or bonsai['status']!='CPU_BUILD_COMPLETE_STATIC_SM70_PRESENT_GPU_UNTESTED':raise ValueError('Incomplete Bonsai source build')
 def identity(item):
  ids=item.get('identities',item.get('runtime_files_sha256'));server=[v for k,v in ids.items() if pathlib.PurePosixPath(k).name=='llama-server'];cuda=[v for k,v in ids.items() if re.fullmatch(r'libggml-cuda\.so\.[0-9]+\.[0-9]+\.[0-9]+',pathlib.PurePosixPath(k).name)]
  if len(server)!=1 or len(cuda)!=1 or any(not re.fullmatch('[a-f0-9]{64}',v) for v in server+cuda):raise ValueError('Ambiguous engine binary/library identity')
  return server[0],cuda[0]
 result=[]
 for item,base,flavour in [(main,contract['reference_commit'],'local patches'),(cache,contract['reference_commit'],'local patches + HBM cache'),(bonsai,bonsai['source_commit'],'Bonsai PQ2 SM70')]:
  if not re.fullmatch('[a-f0-9]{40}',base):raise ValueError('Unverified source revision')
  server,cuda=identity(item);build_id=pathlib.PurePosixPath(item.get('engine',item.get('runtime_path',''))).parent.parent.name if 'engine' in item else pathlib.PurePosixPath(item['runtime_path']).parent.name
  result.append({'build_id':build_id,'binary_sha256':server,'kernel_library_sha256':cuda,'source_base_commit':base,
   'source_version_label':base[:7]+' + '+flavour,'release_version':None,
   'source_repository':contract['remote_url'].removesuffix('.git') if item is not bonsai else None,
   'local_variant':flavour,'comparison_upstream_commit':contract['upstream_commit'] if item is not bonsai else None,
   'source_inputs_sha256':main['source_proof']['source_inputs_sha256'] if item is not bonsai else None,
   'patch_sha256':patch['patch_sha256'] if item is cache else contract['local_patch_sha256'] if item is main else None})
 return result

def H_BYTES(raw):
 return hashlib.sha256(raw).hexdigest()

def build(root,db,comparison,experiments,receipt,sanitize,previous):
 root=pathlib.Path(root);reg=read(root/'BENCHMARK_REGISTER.json');profiles=[];runs=[];defs={d['benchmark_id']:d for d in reg['definitions']}
 for item in reg.get('engine_source_reviews',[]):
  ap=(root/item.pop('audit_path')).resolve()
  if not ap.is_relative_to(root.resolve()) or digest(ap)!=item['audit_sha256']:raise ValueError('Engine source review changed')
  a=read(ap)
  if a['kind']!='ENGINE_SOURCE_VERSION_REVIEW' or a['new_GPU_runs']!=0:raise ValueError('Invalid engine source review')
  raw={'_bytes':{}}
  required={'main-build.json','main-source-contract.json','cache-build.json','cache-patch.json','bonsai-build.json','bonsai-plan.json'}
  if set(a['raw_sources'])!=required:raise ValueError('Incomplete engine source receipts')
  for name,sha in a['raw_sources'].items():
   p=ap.parent/name
   if digest(p)!=sha:raise ValueError('Engine source receipt changed')
   raw['_bytes'][name]=p.read_bytes();raw[name]=read(p)
  engines=engine_source_annotations(raw)
  if engines!=a['engines']:raise ValueError('Engine source interpretation mismatch')
  item.update(audit_id=receipt(ap,item['audit_sha256']),engines=engines,raw_sources=a['raw_sources'],interpretation=a['interpretation'])
 for item in reg.get('same_quantizer_weight_reviews',[]):
  if set(item)!={'review_id','at_utc',*(k+suffix for k in ('audit','header','tensor_results','plan','verification','rename') for suffix in ('_path','_sha256'))}:raise ValueError('Unreviewed same-quantizer export schema')
  paths={}
  for key in ('audit','header','tensor_results','plan','verification','rename'):
   p=(root/item.pop(key+'_path')).resolve()
   if not p.is_relative_to(root.resolve()) or digest(p)!=item[key+'_sha256']:raise ValueError('Same-quantizer review source changed')
   paths[key]=p
  a=read(paths['audit']);header=read(paths['header']);plan=read(paths['plan']);rows=[json.loads(s) for s in paths['tensor_results'].read_text().splitlines()]
  if a['header_audit_sha256']!=item['header_sha256'] or a['source_plan_sha256']!=item['plan_sha256'] or a['tensor_results_sha256']!=item['tensor_results_sha256']:raise ValueError('Same-quantizer review lineage mismatch')
  item['result']=same_quantizer_review(a,header,rows,plan)
  v=read(paths['verification']);n=read(paths['rename'])
  if v['payload_audit_sha256']!=item['audit_sha256'] or v['tensor_results_sha256']!=item['tensor_results_sha256'] or v['matching_previous_V2_tensor_payload_hashes']!=a['compared_tensors'] or v['complete_data_region_covered'] is not True or v['original_main_preserved'] is not True or v['service_terminal_properties']!={'MainPID':'0','Result':'success','ExecMainStatus':'0','ActiveState':'inactive'}:raise ValueError('Missing independent payload verification')
  if n['retained_main_sha256']!=plan['V2']['sha256'] or n['deleted_file_sha256']!=plan['V1']['sha256'] or n['original_main_bytes_and_mtime_unchanged'] is not True or n['historical_audits_and_reference_ids_modified'] is not False or n['old_model_path_preserved_as_compatibility_symlink'] is not True:raise ValueError('Invalid rename/dedup evidence')
  item['result']['independent_verification']={k:v[k] for k in ('matching_previous_V2_tensor_payload_hashes','complete_data_region_covered','body_bytes','original_main_preserved','service_terminal_properties')}
  item['result']['rename_and_dedup']={k:n[k] for k in ('at_utc','status','retained_main_filename','retained_main_sha256','retained_original_inode','original_main_bytes_and_mtime_unchanged','original_GGUF_metadata_unchanged','old_model_path_preserved_as_compatibility_symlink','new_short_alias_targets_retained_main','deleted_regular_file','deleted_file_sha256','deleted_allocated_bytes','historical_audits_and_reference_ids_modified','new_GPU_runs','display_name','classification')}
  reg.setdefault('model_label_annotations',[]).append({'artifact_sha256':n['retained_main_sha256'],'display_name':n['display_name'],'historical_label_retained':True,'review_id':item['review_id'],'audit_sha256':item['rename_sha256']})
  item['evidence_audit_ids']=[ident for k,p in paths.items() if (ident:=receipt(p,item[k+'_sha256']))]
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
  is_tools=a.get('benchmark_id')=='bfcl-v4-simple-python-full400'
  bench=defs[a['benchmark_id']] if is_tools else defs[reg['local_cohort_classification']['coding']['benchmark_id']]
  complete=(native_reused_tool_run(root,a,cfg,bench,receipt) if a.get('reused_task_count') else native_tool_run(root,a,cfg,bench,receipt)) if is_tools else native_complete_run(root,a,cfg,bench,receipt)
  if complete:
   if complete.get('full_benchmark_score_claimed') is not False:qualify(complete,bench)
   complete['run_id']='run-'+H(complete);runs.append(complete)
  partial=None if is_tools else native_partial_run(root,a,cfg,bench,receipt)
  if partial:
   partial['run_id']='run-'+H(partial);runs.append(partial)
 prior=previous or {'profiles':[],'runs':[],'attempts':[]}
 result={'schema_version':SCHEMA,'profiles':frozen_merge(prior['profiles'],profiles,'runtime_configuration_id'),'runs':frozen_merge(prior['runs'],runs,'run_id'),'attempts':frozen_merge(prior['attempts'],history_attempts,'attempt_id'),'provenance_gaps':frozen_merge(prior.get('provenance_gaps',[]),gaps,'gap_id')}
 ce,me=configuration_evidence(root,db,result,receipt)
 result['configuration_evidence']=frozen_merge(prior.get('configuration_evidence',[]),ce,'evidence_id')
 result['measurement_evidence']=frozen_merge(prior.get('measurement_evidence',[]),me,'evidence_id')
 validate_history(result,defs)
 for item in reg.get('candidate_research',[]):
  from derivatives import collect as collect_derivatives
  public=collect_derivatives(root,item,result,receipt)
  item.pop('audit_path');item.update(public)
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
     # Historical explicit unknown markers carry no measured value. The original
     # content-addressed profile remains untouched; only pinned annotations fill them.
     unknown=cur is None or isinstance(cur,str) and cur in ('NOT MEASURED','NICHT ERFASST')
     if not unknown and cur!=v:raise ValueError('Evidence contradicts immutable profile')
 return True

def pair_delta(a,b):
 keys=['benchmark_identity_id','evaluated_task_set_hash','scorer_version','tasks']
 if any(a[k]!=b[k] for k in keys):return {'comparable':False,'reason':'Different benchmark/task set/scorer/count; no delta calculated.'}
 def percent(x,y):return (y/x-1)*100 if finite(x) and finite(y) and x>0 else None
 return {'comparable':True,'quality_delta_pp':b['score_percent']-a['score_percent'],'latency_delta_percent':percent(a.get('wall_s'),b.get('wall_s')),'energy_per_success_delta_percent':percent(a.get('gpu_j_per_success'),b.get('gpu_j_per_success')),'interpretation':'Whole-profile comparison. No causal optimization claim without a dedicated independent audit.'}

def master_catalog(register, history):
 """Presentation identities only; never rewrite the immutable research ledger."""
 columns=[]; assignments={}; definitions={d['benchmark_id']:d for d in register['definitions']}
 # Families are display groups, never scoring or protocol identities. Unknown
 # definitions stay separate until deliberately mapped; no name-based pooling.
 families={
  'humanevalplus-v0.1.10':('humanevalplus','HumanEval+'),
  'mbppplus-v0.2.0':('mbppplus','MBPP+'),
  'bfcl-v4-full':('bfcl','BFCL'),'bfcl-v3-full':('bfcl','BFCL'),
  'bfcl-v4-simple-python-full400':('bfcl','BFCL'),
  'swe-bench-verified':('swe-bench','SWE-bench'),'swe-bench-pro':('swe-bench','SWE-bench'),
  'terminal-bench-2.1':('terminal-bench','Terminal-Bench'),
  'livecodebench':('livecodebench','LiveCodeBench'),
  'local-agents':('local-agents','Local agents (supplemental)'),
  'local-long16k':('local-long-context','Local long context (supplemental)'),
  'local-long32k_validation':('local-long-context','Local long context (supplemental)')}
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
  item['family_id'],item['family_name']=families.get(identity['benchmark_id'],(identity['benchmark_id'],item['name']))
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
  scope='OFFICIAL_LOCAL' if run['official_eligible'] else 'LOCAL_SUPPLEMENTAL' if run['benchmark_id'].startswith('local-') else 'PARTIAL' if run.get('status')=='PARTIAL' else 'UNQUALIFIED_FULL' if run.get('status')=='FULL_NATIVE_CODING_OFFICIAL_API_PENDING' else 'HISTORICAL'
  groups.setdefault((scope,H(protocol(run))),[]).append(run)
 for (scope,_),runs in sorted(groups.items()):
  definition=definitions.get(runs[0]['benchmark_id'],{'benchmark_id':runs[0]['benchmark_id'],'name':runs[0]['benchmark_id']})
  add(definition,runs,scope)
 if set(assignments)!={r['run_id'] for r in history['runs']}:raise ValueError('Master table lost a measured record')
 return {'schema_version':1,'benchmark_columns':columns,'run_columns':assignments,
         'mean_policy':'User-selected unweighted arithmetic mean of exact-protocol replicate means, at most one protocol per family. All selected results required. Official mode accepts admitted results only. Never select a replicate maximum.',
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
 # Old result URLs are aliases, never competing leaderboard/table views.
 alias='# Model comparison has one home\n\n[Open the complete benchmark table](configuration-comparison.md#all-measured-results). Full, partial, historical and qualified benchmark results appear together there, with their original task counts and statuses.\n\nThis older URL redirects automatically. Original measurements, protocol definitions, source datasets, profile identities and audits remain preserved.\n'
 for route in ('benchmarks.md','supplemental-comparison.md'):
  write(docs/route,alias)
 page='# Configuration Comparison & Benchmark Master Table\n\n**Default: Alle gemessenen Ergebnisse.** One continuous row per immutable configuration with a measured benchmark result in `history.runs`, with no pagination. Own local supplemental tests are excluded from this table and its mean, including the full preset; they remain available under [local benchmarks](local-benchmarks.md). Configurations measured only on those local tests stay in that separate area. The default **Kompakt** view shows one score column per benchmark family, plus model, quantization, engine, version and the user-selected mean. Each family has an explicit protocol selector: registered dataset revision, task set, scorer and qualification track remain distinct. The preferred default is an officially admitted local protocol when available, even when a particular configuration has no result for it. **One central table includes measured full and PARTIAL results in the same benchmark-family column.** Cells always disclose their actual solved/task denominator and status. By default each configuration shows its best-qualified available protocol, then coverage, never a score maximum. Choosing an exact protocol enables strict matching for that family; **Vollständig** retains every exact protocol column and measurement field. Build-ID is omitted from all presets by request; it remains available in result details, profiles and the column picker. Plans and result-free configuration attempts remain in the [separate archive](configuration-archive.md). Every recorded profile field and startup flag is available through the categorized column picker. Each benchmark column is bound to its exact register definition, dataset/task set, scorer and qualification track. Unknown means **NICHT ERFASST**, never off or zero. Failed and weaker configurations remain visible.\n\nUse **Nur offiziell qualifizierte Ergebnisse** to optionally restrict the display. **Durchschnittsmodus** controls admission to the custom average, separately from the family protocol selectors and the optional row filter. Exploratory averages are explicitly labelled. Quality, speed and energy presets expose their relevant parameters and measurements; score cells open complete result and configuration details. The user-defined arithmetic mean is not an official benchmark score: sum of selected percentages divided by the number of selected **families**, at most one exact protocol per family. Every selected result must exist for the exact same immutable configuration; otherwise **NICHT BERECHENBAR**, never zero or a mean over fewer benchmarks. Distinct original run observations use their arithmetic mean, with count and dispersion; admission-history duplicates do not create extra observations. Provenance-defined observation counts do not establish statistical independence. Conflicting judgments are excluded from numerical summaries.\n\n<div id="all-measured-results" aria-live="polite"></div>\n\n## Data coverage and missing fields\n\nModel names and file names are not proof of architecture, parameter count, QAT, SVD, original weights or the executed kernel. Requested flags and verified execution remain separate fields. Engine versions are never substituted with build hashes. Newly discovered fields automatically become selectable; historical fields are supplemented only through hash-bound evidence annotations; immutable profiles and results are never rewritten. Historical server logs reporting `build 0 (unknown)` cannot establish an upstream release or Git commit. Build IDs, executable hashes and CUDA-library hashes remain separate identities.\n\n'
 gap_paths=['model.hf_revision','model.hf_repository','model.parameter_count','model.qat','model.svd','model.architecture','engine.version','engine.git_commit','engine.fork_repository','engine.cuda_version','engine.driver_version','engine.executed_kernel_backend_path','runtime.thinking_level','runtime.reasoning_budget_tokens','optimizations.speculation_effective','optimizations.flash_attention_effective','optimizations.cuda_graphs.actual_capture_replay']
 def field(obj,path):
  for key in path.split('.'):
   if not isinstance(obj,dict) or key not in obj:return None
   obj=obj[key]
  return obj
 measured_ids={r['runtime_configuration_id'] for r in history['runs']}
 comparison_ids={r['runtime_configuration_id'] for r in history['runs'] if not r['benchmark_id'].startswith('local-')}
 measured_profiles=[p for p in history['profiles'] if p['runtime_configuration_id'] in comparison_ids]
 gap_paths+=['engine.source_base_commit','engine.source_version_label']
 def observed(p,path):
  values=[e['fields'][path] for e in history.get('configuration_evidence',[]) if e['runtime_configuration_id']==p['runtime_configuration_id'] and path in e['fields']]
  if path in ('engine.source_base_commit','engine.source_version_label'):
   values=[e[path.removeprefix('engine.')] for review in register.get('engine_source_reviews',[]) for e in review['engines'] if all(p['engine'].get(k)==e[k] for k in ('build_id','binary_sha256','kernel_library_sha256'))]
  return values[0] if values else field(p,path)
 page+=table(['Recorded field','Profiles with a value','Profiles without a value'],[[path,sum(observed(p,path) is not None for p in measured_profiles),sum(observed(p,path) is None for p in measured_profiles)] for path in gap_paths])
 page+='Coverage counts above refer to the measured benchmark configurations shown in this table, excluding local-only supplemental profiles. **Engine-Version / Quellstand** shows a recorded release when available, otherwise the independently linked source-base commit plus local patch variant. A source revision is not an invented upstream release tag. Matching requires the build, server SHA256 and CUDA-library SHA256; shared executable bytes alone cannot establish identical kernels. Source receipts and patch lineage are linked in each profile; unknown historical release tags stay unknown. OmniCoder V1/V2 naming is unified as **OmniCoder 9B** in the display while immutable original labels and separate measured configurations are preserved. Additional column-picker fields expose pinned observed sampler/template controls and per-benchmark timing/energy provenance. TTFT remains unrecorded for non-streaming replies; prompt evaluation time is not TTFT. GPU J/output token includes prefill energy in the same case window.\n\n'
 page+='Explicit presentation fields use only recorded options: MTP is true for `draft-mtp`, false for explicit `none`, and unknown otherwise. Thinking mode uses an explicit `enable_thinking` template boolean; a reasoning-parser flag does not prove thinking mode. Model names, optimization-knob zero values and absent flags never establish effective execution.\n\n'
 page+='Prefill/decode/TTFT and other costs are shown only where the original run actually records them. Request wall time is not silently renamed total system latency. Performance columns are benchmark-specific, not pooled across unrelated tasks. CSV exports all filtered rows with the currently selected columns, complete identities and available audit links. CSV formula-like text is escaped.\n\nThe Top-5 analysis describes observed configurations and missing coverage. Suggested controlled A/B work is a research hypothesis, not a causal explanation, predicted speedup or automatic GPU authorization.\n\n[Immutable configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) · [Benchmark definitions and publisher evidence](benchmark-register.md) · [Original experiments](results.md)\n\n'
 page+='## Provenance gaps — excluded from reconstructed profiles\n\n'+table(['Experiment','Reason','Original audit'],[[g['experiment_id'],g['reason'],audit_links([g['audit_id']])] for g in history.get('provenance_gaps',[])])
 page+='## UI reproduction checks\n\nRun `python -m unittest discover -s scripts` and `node --test scripts/test_master_table.cjs` with Node.js 22 or newer. The optional real-browser acceptance script is `scripts/test_master_browser.cjs`: it accepts a site root URL and artifact directory and uses Playwright 1.64.1. Browser screenshots, CSVs and reports belong outside the public export tree. It runs with GPU rendering disabled. Development asset overrides are explicitly reported and must be disabled for the final published-site check.\n\nFilters accept substrings, `=value`, `!=value`, numeric comparisons such as `>=80`, and `?` for unknown. The CSV always includes immutable configuration IDs, all filtered rows, the currently visible columns and the exact identities of displayed family protocols and protocols selected for the mean, including when their result is missing. Long field values can be inspected directly in a table dialog without leaving the page.\n\n'
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
 if register.get('same_quantizer_weight_reviews'):
  same='# OmniCoder V1 / V2: same-quantizer weight comparison\n\nThis follow-up uses mradermacher Q6_K for both versions. The [earlier bartowski/mradermacher comparison](weight-integrity.md) remains a separate measured result. **No GPU jobs, model inference, benchmark score changes or edits to original main weights.**\n\n'
  for item in register['same_quantizer_weight_reviews']:
   a=item['result'];equal=a['different_tensor_payloads']==0
   same+='## Verdict\n\n'+('**Identical model weights proven — for every stored tensor in these two exact GGUF files.** All tensor names, shapes, GGML types and payload bytes match. Deterministic dequantization therefore produces the same numerical values for every tensor. This is stronger than matching file sizes or sampled tensor checks.\n\n' if equal else '**Different stored payloads. Numerical/source-weight identity is not yet established; dequantization remains required.**\n\n')
   same+='This does not prove the identity or training history of every unquantized upstream checkpoint. It does not establish whether an original upstream publication was faulty or subsequently corrected. It directly establishes what is stored in the retained deployed artifacts.\n\n'
   same+=table(['Measured scope','Value'],[['Review recorded (UTC)',item['at_utc']],['Compared tensors',a['compared_tensors']],['Compared weight values',a['compared_parameters']],['Compared tensor payload bytes',a['compared_payload_bytes']],['Byte-identical tensor payloads',a['identical_tensor_payloads']],['Different tensor payloads',a['different_tensor_payloads']],['Elapsed download + CPU comparison s',a['elapsed_s']],['New GPU runs',a['new_GPU_runs']]])
   same+='## Exact files and source revisions\n\n'+table(['Version','File','Bytes','Locally verified SHA256','Pinned quantizer repository'],[[x['version'],x['filename'],x['bytes'],'`'+x['actual_sha256']+'`','['+x['repository']+'](https://huggingface.co/'+x['repository']+'/tree/'+x['revision']+')'] for x in a['artifacts']])
   same+='Different complete-file hashes are **not** a weight-difference proof. Full-file hashes were independently verified locally for both files; the entire tensor payload of each was then checked. Storage counts for each file: `'+json.dumps(a['type_counts'],sort_keys=True)+'`. Same publisher or Q6_K label alone would not establish equal recipes. Here, actual tensor formats and complete payloads provide the evidence.\n\n'
   same+='## Recorded metadata differences\n\n'+table(['Field','V1','V2'],[[k,v['V1'],v['V2']] for k,v in sorted(a['metadata_differences'].items())])
   same+='The bounded header comparison found the listed metadata differences; all other parsed metadata agree, including tokenizer arrays, template and architecture. Quantization dates above are file metadata, not an independently established release chronology.\n\n'
   same+='## Method\n\nFirst inspect pinned publisher LFS hashes without downloading weight files. Because those hashes differ, inspect a bounded V1 header and compare it with the previously fully verified main V2. All tensor descriptors agree. Then download only the necessary single V1 Q6_K file, verify its complete SHA256, fully rehash the read-only local main V2, and compare **every byte of every tensor** in bounded chunks. Each tensor has separate SHA256 identities and an actual byte-equality result. The existing reviewed GGUF parser is reused to recheck both complete files. Network access, parsing and comparison run unprivileged as UID65534 with GPU devices hidden; the service survives terminal disconnection. Main V2 inode, size and modification time remain unchanged.\n\n'
   same+=a['numerical_interpretation']+'\n\nNo repeated full dequantization or GPU benchmark is needed to prove decoded equality when the type, dimensions and every payload byte already match. This proof concerns quantized stored weights; it is not an inference-performance or model-training claim.\n\n'
   same+='## Relation to the earlier result\n\nThe earlier result compared different quantizer implementations and per-tensor precision policies. Its measured reconstruction differences remain valid. This same-quantizer follow-up addresses that confound directly and does not rewrite the earlier audit. Historical benchmark results continue to identify the exact artifact and runtime tested; no score is copied into a new model row, and no fine-tuning advantage is inferred from a version label.\n\n'
   same+='## Canonical name and duplicate removal\n\nThe retained original main file is now named `'+a['rename_and_dedup']['retained_main_filename']+'`. Its original inode, full SHA256, modification time and internal GGUF metadata remain intact. Old paths remain compatibility symlinks; frozen references and historical audit identities are preserved. The newly downloaded mradermacher V1 regular-file copy was removed after comparison; its short filename now links to the retained main artifact. This frees '+str(a['rename_and_dedup']['deleted_allocated_bytes'])+' allocated bytes. The earlier bartowski comparison artifact was not part of this deletion.\n\nFor the exact checked main hash, the presentation name is **'+a['rename_and_dedup']['display_name']+'**. Original historical model labels remain accessible and are not rewritten inside immutable profiles or runs. Other quantizations and grafted artifacts are not automatically renamed or declared tensor-identical.\n\n'
   same+='[Complete per-tensor equality table](artifact-reviews/omnicoder-same-quantizer-tensors.md). Full payload hashes are in the [public benchmark register](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json), under `same_quantizer_weight_reviews`. No model values or weights are redistributed.\n\n## Audit identities\n\n'+audit_links(item['evidence_audit_ids'])+'\n\n'+table(['Evidence','Original SHA256'],[[k,'`'+item[k+'_sha256']+'`'] for k in ('audit','header','tensor_results','plan','verification','rename')])
   same+='**LOCALLY MEASURED:** complete file hashes, all tensor layouts and every tensor payload. **EXTERNALLY EVIDENCED:** publisher repository identities and LFS metadata. **NOT VERIFIED:** unquantized training lineage, publisher intent, a repaired upstream release or new V1 task-performance measurements.\n\n'
   detail='# Same-quantizer OmniCoder: every tensor payload\n\n[Artifact identities, full method and limits](../weight-integrity-same-quantizer.md). Payload hash prefixes below are for scanning only; full hashes are preserved in the public benchmark register and the original journal.\n\n'
   detail+=table(['Tensor','GGML type','Weight values','Payload bytes','Byte-identical','V1 SHA256 prefix','V2 SHA256 prefix'],[[r['name'],r['type'],r['parameters'],r['payload_bytes'],r['byte_identical'],r['payload_sha256_V1'][:16],r['payload_sha256_V2'][:16]] for r in a['tensor_results']]);write(docs/'artifact-reviews/omnicoder-same-quantizer-tensors.md',detail)
  write(docs/'weight-integrity-same-quantizer.md',same)
  old=docs/'weight-integrity.md';write(old,old.read_text().replace('\n\nThis artifact review','\n\n**Follow-up:** [same-quantizer mradermacher V1/V2 comparison](weight-integrity-same-quantizer.md) addresses the different-quantizer confound. This earlier report remains unchanged in scope.\n\nThis artifact review',1))
 # Exactly one comparison table; optional provenance is prose, not additional
 # result tables that the project owner must navigate between.
 def prose_table(match):
  lines=match.group(0).splitlines();head=[x.strip() for x in lines[0].strip('|').split('|')];rows=lines[2:]
  return '\n'.join('- '+' · '.join(label+': '+value.strip() for label,value in zip(head,line.strip('|').split('|'))) for line in rows)+'\n'
 details=page.partition('## Data coverage and missing fields')[2]
 details=re.sub(r'(?m)^\|[^\n]*\n(?:\|[^\n]*\n?)+',prose_table,details)
 page='# Model Comparison & Benchmark Results\n\nOne table for every measured configuration. Full and **PARTIAL** results share one column per benchmark family; every cell shows its actual **solved / evaluated** count and qualification. Missing values are never zero. Select a score to inspect its exact protocol, settings, runtime, energy and original audit.\n\nThe optional official-only filter excludes partial and unqualified results. The custom mean follows its selected exact protocols; partial task sets never silently enter the official mean. Different task subsets do not establish model superiority.\n\n<div id="all-measured-results" aria-live="polite"></div>\n\n<details>\n<summary>Scientific provenance, parameter coverage and reproduction</summary>\n\n'+details+'\n</details>\n'
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
  display_name=register.get('model_family_labels',{}).get(p['model']['family_id'],p['model']['name'])
  s='# '+str(display_name)+' · '+ident[:16]+'\n\n[Back to configuration comparison](../configuration-comparison.md)\n\nProfile ID: `'+ident+'`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.\n\n'
  for title,key in [('Model and weights','model'),('Engine and backend','engine'),('Optimizations','optimizations'),('Runtime and sampler','runtime'),('Ordered startup parameters','start_parameters')]:
   s+='## '+title+'\n\n```json\n'+pretty(p[key])+'\n```\n\n'
  for review in register.get('engine_source_reviews',[]):
   for e in review['engines']:
    if all(p['engine'].get(k)==e[k] for k in ('build_id','binary_sha256','kernel_library_sha256')):
     s+='## Verified engine source revision\n\nThe original profile remains immutable. This matched build receipt supplies a source-base revision plus local patch lineage, not a reconstructed upstream release tag.\n\n```json\n'+pretty(e)+'\n```\n\n'+audit_links([review['audit_id']],'../')+'\n\n'
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
