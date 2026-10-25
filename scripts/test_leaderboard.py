"""Scientific admission and immutable-history regression controls (CPU only)."""
import copy,json,pathlib,tempfile,unittest
from validate import validation_event_matches
from leaderboard import H,definition_identity,official_gate,frozen_merge,validate_history,pair_delta,profile,render,verify_broker_capture,native_coverage,native_complete_run,native_partial_run,native_job_id,master_catalog,digest,configuration_evidence,weight_integrity_review,same_quantizer_review,engine_source_annotations,profile_label_annotation
ROOT=pathlib.Path(__file__).resolve().parents[1]
class LeaderboardTests(unittest.TestCase):
 def label_fixture(self):
  label='native_Q4_0_QAT_T1.0_K64_output4096_nonthinking_noMTP_single_session_native_tools'
  cfg={'runtime_configuration_id':'cfg-'+'a'*64,'model':{'variant':label,'artifact_sha256':'b'*64,'quantization':'Q6_K'}}
  identity={'model_sha256':'b'*64,'quantization':'Q6_K'};native={'model_sha256':'b'*64,'native_recipe':{'request_options':{'temperature':0}}}
  entry={'runtime_configuration_id':cfg['runtime_configuration_id'],'original_descriptive_label':label,'model_artifact_sha256':'b'*64,'immutable_profile_sha256':'c'*64,'checkpoint_variant':None,'checkpoint_variant_verdict':'NOT_RECORDED','recorded_QAT':None,'original_profile_unchanged':True,'measured_scores_unchanged':True,'recorded_quantization':'Q6_K','recorded_temperature':0,'recorded_top_k':None}
  return entry,cfg,identity,native
 def test_known_tool_harness_suffix_is_not_checkpoint_evidence(self):
  for label,repo,temperature in [('Slopus-9B-CodeCore-Merge','Kukedlc/Slopus-9B',.6),('OmniCoder Opus Distill-9B-CodeCore-Merge','mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF',.6),('OmniCoder Slopus Distill-9B','Kukedlc/Slopus-9B',0)]:
   entry,cfg,identity,native=self.label_fixture();entry.update(original_descriptive_label=label,recorded_temperature=temperature);cfg['model'].update(variant=label,hf_repository=repo);identity['hf_repository']=repo;native['native_recipe']['request_options']['temperature']=temperature
   before=copy.deepcopy((entry,cfg,identity,native));out=profile_label_annotation(entry,cfg,identity,native)
   self.assertIsNone(out['checkpoint_variant']);self.assertEqual((entry,cfg,identity,native),before);self.assertEqual(out['original_descriptive_label'],label)
 def test_harness_suffix_correction_cannot_hide_another_repository(self):
  entry,cfg,identity,native=self.label_fixture();label='Slopus-9B-CodeCore-Merge';entry.update(original_descriptive_label=label,recorded_temperature=.6);cfg['model'].update(variant=label,hf_repository='other/model');identity['hf_repository']='other/model';native['native_recipe']['request_options']['temperature']=.6
  with self.assertRaises(ValueError):profile_label_annotation(entry,cfg,identity,native)
 def test_copied_description_correction_keeps_original_and_unknown_variant(self):
  args=self.label_fixture();before=copy.deepcopy(args);out=profile_label_annotation(*args)
  self.assertEqual(args,before);self.assertIsNone(out['checkpoint_variant']);self.assertEqual(out['QAT_evidence'],'NOT_RECORDED');self.assertEqual(out['recorded_quantization'],'Q6_K');self.assertIsNone(out['recorded_top_k'])
 def test_description_correction_rejects_identity_tuning_or_evidence_rewrites(self):
  for mode in ('configuration','artifact','label','quantization','sampler','top-k','qat','variant','rewrite','no-defect'):
   entry,cfg,identity,native=self.label_fixture()
   if mode=='configuration':entry['runtime_configuration_id']='cfg-'+'d'*64
   elif mode=='artifact':native['model_sha256']='d'*64
   elif mode=='label':cfg['model']['variant']='valid unrelated profile'
   elif mode=='quantization':identity['quantization']='Q4_0'
   elif mode=='sampler':entry['recorded_temperature']=1
   elif mode=='top-k':entry['recorded_top_k']=64
   elif mode=='qat':entry['recorded_QAT']=False
   elif mode=='variant':entry['checkpoint_variant']='instruct'
   elif mode=='rewrite':entry['measured_scores_unchanged']=False
   else:entry['recorded_temperature']=native['native_recipe']['request_options']['temperature']=1
   with self.subTest(mode=mode),self.assertRaises(ValueError):profile_label_annotation(entry,cfg,identity,native)
 def engine_source_fixture(self):
  contract={'reference_commit':'a'*40,'upstream_commit':'b'*40,'reference_inputs_canonical_sha256':'c'*64,'local_patch_sha256':'d'*64,'remote_url':'https://github.com/ggml-org/llama.cpp.git'}
  cbytes=json.dumps(contract).encode();sha=lambda b:__import__('hashlib').sha256(b).hexdigest()
  def ids(server,cuda):return {'/build/runtime/llama-server':server*64,'/build/runtime/libggml-cuda.so.0.26.0':cuda*64}
  main={'engine':'/builds/main/runtime/llama-server','identities':ids('1','2'),'source_proof':{'commit':'a'*40,'source_inputs_sha256':'c'*64,'source_contract_sha256':sha(cbytes)}}
  mbytes=json.dumps(main).encode();patch={'parent':'/builds/main','parent_manifest_sha256':sha(mbytes),'patch_sha256':'e'*64}
  cache={'engine':'/builds/cache/runtime/llama-server','identities':ids('1','3'),'source_proof':patch}
  bonsai={'source_commit':'f'*40,'status':'CPU_BUILD_COMPLETE_STATIC_SM70_PRESENT_GPU_UNTESTED','runtime_path':'/builds/bonsai/runtime','runtime_files_sha256':ids('4','5')}
  return {'main-build.json':main,'main-source-contract.json':contract,'cache-build.json':cache,'cache-patch.json':patch,'bonsai-build.json':bonsai,'bonsai-plan.json':{'source_commit':'f'*40},'_bytes':{'main-build.json':mbytes,'main-source-contract.json':cbytes}}
 def test_engine_source_label_is_not_a_release_and_distinguishes_cuda_variants(self):
  rows=engine_source_annotations(self.engine_source_fixture());self.assertEqual(len(rows),3);self.assertTrue(all(r['release_version'] is None for r in rows))
  self.assertEqual(rows[0]['source_base_commit'],rows[1]['source_base_commit']);self.assertEqual(rows[0]['binary_sha256'],rows[1]['binary_sha256']);self.assertNotEqual(rows[0]['kernel_library_sha256'],rows[1]['kernel_library_sha256'])
  self.assertEqual([r['build_id'] for r in rows],['main','cache','bonsai']);self.assertIn('HBM cache',rows[1]['source_version_label'])
 def test_engine_source_review_rejects_broken_contract_parent_and_binary_links(self):
  for mode in ('commit','contract-hash','parent-hash','parent-name','missing-binary','ambiguous-library','unfinished-build','bonsai-commit'):
   raw=self.engine_source_fixture()
   if mode=='commit':raw['main-source-contract.json']['reference_commit']='e'*40
   elif mode=='contract-hash':raw['_bytes']['main-source-contract.json']=b'changed'
   elif mode=='parent-hash':raw['cache-patch.json']['parent_manifest_sha256']='0'*64
   elif mode=='parent-name':raw['cache-patch.json']['parent']='/builds/other'
   elif mode=='missing-binary':raw['main-build.json']['identities'].pop('/build/runtime/llama-server')
   elif mode=='ambiguous-library':raw['main-build.json']['identities']['/build/runtime/libggml-cuda.so.0.21.0']='9'*64
   elif mode=='unfinished-build':raw['bonsai-build.json']['status']='INCOMPLETE'
   else:raw['bonsai-plan.json']['source_commit']='0'*40
   with self.subTest(mode=mode),self.assertRaises(ValueError):engine_source_annotations(raw)
 def payload_fixture(self):
  plan={key:{'repository':'owner/model','revision':'c'*40,'filename':key+'.gguf','bytes':300,'sha256':letter*64} for key,letter in [('V1','a'),('V2','b')]}
  rows=[{'name':'matrix.weight','shape':[256],'type':'Q6_K','parameters':256,'payload_bytes':210,'byte_identical':True,'payload_sha256_V1':'d'*64,'payload_sha256_V2':'d'*64}]
  header={'tensor_descriptors_equal':True,'V2_data_start':32,'V1_header':{'data_start':32,'type_counts':{'Q6_K':1},'tensors':{'matrix.weight':{'shape':[256],'type_name':'Q6_K','parameters':256,'bytes':210}}},'metadata_differences':{'general.name':{'V1':'Version1','V2':'Version2'}}}
  a={'analysis_id':'OMNICODER_SAME_QUANTIZER_V1_V2_PAYLOAD_COMPARISON','status':'COMPLETE_ALL_TENSOR_PAYLOADS','new_GPU_runs':0,'new_model_requests':0,'original_weights_modified':False,'execution_uid':65534,'V2_input_read_only':True,'compared_tensors':1,'compared_parameters':256,'compared_payload_bytes':210,'identical_tensor_payloads':1,'different_tensor_payloads':0,'represented_weight_verdict':'IDENTICAL_MODEL_WEIGHTS_PROVEN_FOR_ALL_STORED_GGUF_TENSORS','artifacts':[{'version':k,**v,'actual_sha256':v['sha256']} for k,v in plan.items()],'elapsed_s':1.,'numerical_interpretation':'Same typed bytes imply equal decoded values.','source_checkpoint_limit':'No source training identity claim.'}
  return a,header,rows,plan
 def test_complete_identical_typed_payloads_do_not_require_identical_file_hashes(self):
  a,h,rows,p=self.payload_fixture();v=same_quantizer_review(a,h,rows,p);self.assertNotEqual(v['artifacts'][0]['sha256'],v['artifacts'][1]['sha256']);self.assertEqual(v['different_tensor_payloads'],0);self.assertIn('IDENTICAL_MODEL_WEIGHTS',v['represented_weight_verdict'])
 def test_payload_census_rejects_partial_wrong_format_hash_and_false_identity(self):
  for mode in ('missing','duplicate','shape','type','hash','aggregate','model','unreviewed-metadata'):
   a,h,rows,p=self.payload_fixture()
   if mode=='missing':rows.clear()
   elif mode=='duplicate':rows.append(copy.deepcopy(rows[0]))
   elif mode=='shape':rows[0]['shape']=[128,2]
   elif mode=='type':rows[0]['type']='F32'
   elif mode=='hash':rows[0]['payload_sha256_V2']='e'*64
   elif mode=='aggregate':a['compared_payload_bytes']=209
   elif mode=='model':a['artifacts'][0]['actual_sha256']='e'*64
   else:h['metadata_differences']['unreviewed']={'V1':'extra','V2':'other'}
   with self.subTest(mode=mode),self.assertRaises(ValueError):same_quantizer_review(a,h,rows,p)
 def test_different_payloads_cannot_be_called_identical_without_dequantization(self):
  a,h,rows,p=self.payload_fixture();rows[0].update(byte_identical=False,payload_sha256_V2='e'*64);a.update(identical_tensor_payloads=0,different_tensor_payloads=1)
  with self.assertRaises(ValueError):same_quantizer_review(a,h,rows,p)
  a['represented_weight_verdict']='DIFFERENT_STORED_PAYLOADS_DEQUANTIZATION_REQUIRED';self.assertIn('DEQUANTIZATION_REQUIRED',same_quantizer_review(a,h,rows,p)['represented_weight_verdict'])
 def test_payload_public_projection_excludes_unapproved_fields(self):
  a,h,rows,p=self.payload_fixture();a['artifacts'][0]['private_source']='private file';rows[0]['sampled_weights']=[1.,2.];result=same_quantizer_review(a,h,rows,p);self.assertNotIn('private_source',str(result));self.assertNotIn('sampled_weights',str(result))
 def weight_fixture(self):
  rows=[]
  for name,changed in [('norm.weight',False),('matrix.weight',True)]:
   rows.append({'name':name,'parameters':2,'type_A':'F32','type_B':'F32','changed_values_exact':int(changed),'equal_values_exact':2-int(changed),'max_abs_difference':float(changed),'mean_abs_difference':.5*changed,'rmse':(0.5*changed)**.5,'squared_difference_sum':float(changed),'squared_norm_A':2.,'squared_norm_B':5. if changed else 2.,'relative_l2_A':(0.5*changed)**.5,'cosine_similarity':None,'payload_sha256_A':'a'*64,'payload_sha256_B':('b' if changed else 'a')*64,'decoder_reference_checks':2,'decoder_max_abs_difference':0.})
  header={'tensors':{r['name']:{'parameters':2,'shape':[2],'type_name':'F32'} for r in rows},'tensor_count':2,'metadata':{'general.architecture':'test','tokenizer.chat_template':'private template text'},'type_counts':{'F32':2}}
  artifact={'source_repository':'owner/model','source_revision':'c'*40,'filename':'test.gguf','sha256':'d'*64,'bytes':42};plan={'V1':artifact,'V2':artifact}
  a={'analysis_id':'OMNICODER_V1_V2_CPU_WEIGHT_INTEGRITY','status':'COMPLETE_ALL_COMPARABLE_TENSORS','new_GPU_runs':0,'new_model_requests':0,'model_files_modified':False,'execution_uid':65534,'input_FDs_read_only':True,'headers':[header,copy.deepcopy(header)],'controls':{k:True for k in ('q6_zero','q6_nonzero','q6_negative_control','different_encodings_equal_values','q8_signed_values','native_and_numpy_agree')},'compared_tensors':2,'compared_parameters':4,'changed_values_exact':1,'changed_tensors':1,'identical_tensors':1,'global_rmse':.5,'global_relative_l2_A':.5,'global_max_abs_difference':1.,'represented_weight_identity':'DIFFERENT_RECONSTRUCTED_WEIGHTS','artifacts':[{'sha256':'d'*64,'bytes':42}]*2,'decoder_identities':{},'NumPy_version':'fixture','elapsed_s':1.,'quantization_noise_conclusion':'No source pair.','training_history_conclusion':'Not established.'}
  decision={'at_utc':'2026-10-23','represented_weight_identity':a['represented_weight_identity'],'underlying_checkpoint_verdict':'NOT_UNAMBIGUOUSLY_DETERMINABLE'}
  return a,rows,plan,decision
 def test_weight_census_has_no_training_or_benchmark_claim(self):
  result=weight_integrity_review(*self.weight_fixture());self.assertEqual(result['compared_parameters'],4);self.assertEqual(result['underlying_checkpoint_verdict'],'NOT_UNAMBIGUOUSLY_DETERMINABLE');self.assertNotIn('private template text',str(result));self.assertNotIn('score_percent',result)
 def test_weight_census_rejects_omitted_duplicate_and_misidentified_tensors(self):
  for mode in ('omit','duplicate','shape','precision','parameters'):
   a,rows,p,d=self.weight_fixture()
   if mode=='omit':rows.pop()
   elif mode=='duplicate':rows[1]=copy.deepcopy(rows[0])
   elif mode=='shape':a['headers'][1]['tensors']['matrix.weight']['shape']=[3]
   elif mode=='precision':rows[0]['type_B']='Q6_K'
   else:rows[0]['parameters']=3
   with self.subTest(mode=mode),self.assertRaises(ValueError):weight_integrity_review(a,rows,p,d)
 def test_weight_census_rejects_unverified_controls_costs_and_identity_claims(self):
  for mode in ('GPU','root','write','decoder','rmse','hash','finetune','aggregate'):
   a,rows,p,d=self.weight_fixture()
   if mode=='GPU':a['new_GPU_runs']=1
   elif mode=='root':a['execution_uid']=0
   elif mode=='write':a['input_FDs_read_only']=False
   elif mode=='decoder':a['controls']['q6_negative_control']=False
   elif mode=='rmse':rows[0]['rmse']=1.
   elif mode=='hash':a['artifacts'][0]={'sha256':'e'*64,'bytes':42}
   elif mode=='finetune':d['underlying_checkpoint_verdict']='NEW_FINE_TUNE_PROVEN'
   else:a['changed_values_exact']=3
   with self.subTest(mode=mode),self.assertRaises(ValueError):weight_integrity_review(a,rows,p,d)
 def fixture(self):
  ids=['a','b'];d={'benchmark_id':'test','benchmark_revision':'r1','dataset_split_hash':'a'*64,'scorer_version':'v1','required_task_count':2,'expected_task_ids_hash':H(ids),'official_definition_verified':True,'metric':'pass_at_1_percent'}
  r={'audit_hash':'b'*64,'runtime_configuration_id':'cfg-test','tasks':2,'solved':1,'score_percent':50,'benchmark_id':'test','benchmark_identity_id':definition_identity(d),'dataset_split_hash':d['dataset_split_hash'],'scorer_version':'v1'}
  proof={k:True for k in ['complete_task_set','official_scorer_verified','all_canonical_controls_passed','no_task_exclusions','prompt_protocol_verified','unique_task_ids_verified','metrics_verified','independent_audit_verified']}
  proof.update(benchmark_identity_id=definition_identity(d),dataset_split_hash=d['dataset_split_hash'],scorer_version='v1',audit_hash=r['audit_hash'],runtime_configuration_id=r['runtime_configuration_id'],tasks=2,solved=1,task_ids=ids,official_pass_at_1=.5)
  return r,d,proof
 def test_full_conformant_fixture(self):
  self.assertTrue(official_gate(*self.fixture()))
 def test_browser_projection_does_not_duplicate_non_UI_tensor_journals_or_mutate_archives(self):
  from leaderboard import browser_register
  register={'definitions':[{'benchmark_id':'fixture'}],'model_label_annotations':[{'display_name':'fixture'}],'profile_label_reviews':[],'artifact_weight_reviews':[{'tensor_results':['fixture']}],'same_quantizer_weight_reviews':[{'tensor_results':['fixture']}],'candidate_research':[]}
  before=copy.deepcopy(register);small=browser_register(register)
  self.assertEqual(register,before)
  for key in ('definitions','model_label_annotations','profile_label_reviews','candidate_research'):self.assertEqual(small[key],register[key])
  self.assertNotIn('artifact_weight_reviews',small);self.assertNotIn('same_quantizer_weight_reviews',small)
 def test_subsets_exceptions_and_missing_proofs_denied(self):
  for key in ['complete_task_set','official_scorer_verified','all_canonical_controls_passed','no_task_exclusions','prompt_protocol_verified','independent_audit_verified']:
   r,d,p=self.fixture();p[key]=False;self.assertFalse(official_gate(r,d,p),key)
  r,d,p=self.fixture();self.assertFalse(official_gate(r,d,None))
 def test_wrong_tasks_duplicate_tasks_and_denominator_denied(self):
  for ids in [['a'],['a','a'],['a','c']]:
   r,d,p=self.fixture();p['task_ids']=ids;self.assertFalse(official_gate(r,d,p))
  r,d,p=self.fixture();r['tasks']=1;self.assertFalse(official_gate(r,d,p))
 def test_version_hash_model_and_count_bindings(self):
  for key in ['benchmark_identity_id','dataset_split_hash','scorer_version','audit_hash','runtime_configuration_id','solved']:
   r,d,p=self.fixture();p[key]='wrong';self.assertFalse(official_gate(r,d,p),key)
  for key in ['benchmark_revision','dataset_split_hash','scorer_version','expected_task_ids_hash']:
   r,d,p=self.fixture();d[key]=None;self.assertFalse(official_gate(r,d,p))
 def test_unsupported_aggregation_cannot_use_simple_percentage(self):
  r,d,p=self.fixture();d['metric']='BFCL_official_aggregation';p['benchmark_identity_id']=definition_identity(d);r['benchmark_identity_id']=definition_identity(d);self.assertFalse(official_gate(r,d,p))
 def bfcl_fixture(self):
  r,d,p=self.fixture();ids=[f'simple_python_{i}' for i in range(400)]
  d.update(benchmark_id='bfcl-v4-simple-python-full400',required_task_count=400,expected_task_ids_hash=H(sorted(ids)),metric='bfcl_simple_python_ast_accuracy_percent')
  r.update(benchmark_id=d['benchmark_id'],benchmark_identity_id=definition_identity(d),tasks=400,solved=300,score_percent=75)
  p.pop('official_pass_at_1');p.update(benchmark_identity_id=definition_identity(d),tasks=400,solved=300,task_ids=ids,official_category='simple_python',category_only=True,official_correct_count=300,official_category_accuracy=.75)
  return r,d,p
 def test_complete_bfcl_category_has_its_own_metric(self):
  self.assertTrue(official_gate(*self.bfcl_fixture()))
 def test_parallel_multiple200_requires_its_own_exact_category_metric(self):
  r,d,p=self.bfcl_fixture();ids=[f'parallel_multiple_{i}' for i in range(200)]
  d.update(benchmark_id='bfcl-v4-parallel-multiple-full200',required_task_count=200,expected_task_ids_hash=H(sorted(ids)),metric='bfcl_parallel_multiple_ast_accuracy_percent')
  r.update(benchmark_id=d['benchmark_id'],benchmark_identity_id=definition_identity(d),tasks=200,solved=150)
  p.update(benchmark_identity_id=definition_identity(d),tasks=200,solved=150,task_ids=ids,official_category='parallel_multiple',official_correct_count=150)
  self.assertTrue(official_gate(r,d,p))
  for field,value in (('official_category','simple_python'),('category_only',False),('tasks',400),('task_ids',ids[:199])):
   self.assertFalse(official_gate(r,d,{**p,field:value}),field)
  wrong={**d,'metric':'bfcl_simple_python_ast_accuracy_percent'};p['benchmark_identity_id']=r['benchmark_identity_id']=definition_identity(wrong)
  self.assertFalse(official_gate(r,wrong,p))
 def test_bfcl_subset_or_whole_leaderboard_cannot_masquerade_as_category(self):
  for key,value in [('category_only',False),('official_category','overall'),('official_correct_count',299),('official_category_accuracy',.9),('all_canonical_controls_passed',False)]:
   r,d,p=self.bfcl_fixture();p[key]=value;self.assertFalse(official_gate(r,d,p),key)
  for key,value in [('benchmark_id','bfcl-v4-full'),('required_task_count',100)]:
   r,d,p=self.bfcl_fixture();d[key]=value;r['benchmark_id']=d['benchmark_id'];r['benchmark_identity_id']=p['benchmark_identity_id']=definition_identity(d);self.assertFalse(official_gate(r,d,p),key)
 def test_bfcl_requires_complete_unique_ids_and_exact_score(self):
  for ids in [[f'simple_python_{i}' for i in range(100)],['simple_python_0']*400]:
   r,d,p=self.bfcl_fixture();p['task_ids']=ids;self.assertFalse(official_gate(r,d,p))
  r,d,p=self.bfcl_fixture();p.pop('official_category_accuracy');p['official_pass_at_1']=.75;self.assertFalse(official_gate(r,d,p))
 def test_pass_at_one_must_match_the_recorded_numerator(self):
  r,d,p=self.fixture();p['official_pass_at_1']=.9;r['score_percent']=90;self.assertFalse(official_gate(r,d,p))
 def test_definition_verification_is_not_a_model_replay(self):
  event={'kind':'BFCL_FULL400_CATEGORY_DEFINITION_ADMISSION','audit_sha256':'a'*64,'GPU_runs':0,'model_results_admitted':0};audit={'original_sha256':'a'*64,'aggregate_metrics':{'new_GPU_runs':0,'model_results_admitted':0}}
  self.assertTrue(validation_event_matches(event,audit))
  for field,value in [('GPU_runs',1),('model_results_admitted',1),('audit_sha256','b'*64),('kind','UNKNOWN')]:
   self.assertFalse(validation_event_matches({**event,field:value},audit),field)
  changed=copy.deepcopy(audit);changed['aggregate_metrics']['model_results_admitted']=1;self.assertFalse(validation_event_matches(event,changed))
 def test_cpu_replay_validation_still_requires_matching_scores(self):
  event={'experiment_id':'R1','audit_sha256':'a'*64,'tasks':164,'solved':100,'changed_judgements':[]};audit={'original_sha256':'a'*64,'aggregate_metrics':{'models':{'R1':{'tasks':164,'solved':100,'changed_judgements':[]}}}}
  self.assertTrue(validation_event_matches(event,audit));self.assertFalse(validation_event_matches({**event,'solved':101},audit));self.assertFalse(validation_event_matches(event,{}))
 def test_known_upstream_exception_requires_full_pinned_controls(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']}
  r=next(r for r in h['runs'] if r['official_eligible']);d=defs[r['benchmark_id']];p=r['qualification_audit'];self.assertTrue(official_gate(r,d,p))
  self.assertEqual(p['tasks'],164);self.assertFalse(p['all_canonical_controls_passed'])
  for key,value in [('task_ids',['HumanEval/0']),('control_task_count',163),('other_canonical_tasks_passed',162),('all_negative_controls_rejected',False),('unchanged_official_oracle_and_dataset',False),('full_task_set_independently_replayed',False),('official_oracle_source_sha256','0'*64)]:
   changed=copy.deepcopy(p);changed['canonical_reference_exception'][key]=value;self.assertFalse(official_gate(r,d,changed),key)
  changed=copy.deepcopy(p);changed['no_task_exclusions']=False;self.assertFalse(official_gate(r,d,changed))
 def test_mtp_warning_survives_official_api_admission(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());r=next(r for r in h['runs'] if r['official_eligible'] and r['experiment_id']=='R118');self.assertIn('not lossless',r['warning']);self.assertIn('local memory/time limits',r['warning'])
 def test_history_append_only(self):
  old=[{'id':'a','score':1}];new=[{'id':'b','score':2}];self.assertEqual(len(frozen_merge(old,new,'id')),2)
  with self.assertRaises(ValueError):frozen_merge(old,[{'id':'a','score':2}],'id')
  self.assertEqual(old,[{'id':'a','score':1}])
 def test_real_history_hashes_and_unknowns(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']};self.assertTrue(validate_history(h,defs))
  self.assertTrue(any(p['engine']['version'] is None for p in h['profiles']))
  h['runs'][0]['solved']+=1
  with self.assertRaises(ValueError):validate_history(h,defs)
 def test_historical_subset_cannot_be_promoted(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']}
  h['runs'][0]['official_eligible']=True;h['runs'][0]['run_id']='run-'+H({k:v for k,v in h['runs'][0].items() if k!='run_id'})
  with self.assertRaises(ValueError):validate_history(h,defs)
 def test_engine_and_weight_identity_come_from_executed_argv(self):
  plan={'model_sha256':'b'*64,'runtime_identities':{'/art/model.gguf':'a'*64,'/bin/llama-server':'c'*64}}
  p=profile(plan,{'argv':['/bin/llama-server','--model','/art/model.gguf','--spec-type','none']},'test','Test','Q6','R1','d'*64,lambda x:x)
  self.assertEqual(p['model']['artifact_sha256'],'a'*64);self.assertEqual(p['engine']['name'],'llama.cpp-compatible');self.assertIsNone(p['engine']['version']);self.assertNotIn('/art/model.gguf',str(p))
  self.assertEqual(p['optimizations']['speculation_type'],'none');self.assertIsNone(p['optimizations']['cuda_graphs']['actual_capture_replay'])
 def captured_fixture(self):
  assets={'/runtime/build/runtime/model.gguf':'a'*64,'/runtime/build/runtime/llama-server':'b'*64,'/runtime/build/runtime/libggml-cuda.so':'c'*64,'/templates/chat.jinja':'d'*64}
  options={'temperature':1.0,'seed':1001,'chat_template_kwargs':{'enable_thinking':True},'max_tokens':4096}
  native={'model':'/runtime/build/runtime/model.gguf','runtime':'/runtime/build/runtime','chat_template':'/templates/chat.jinja','assets':assets,'native_recipe':{'request_options':options}}
  launch={'argv':['/runtime/build/runtime/llama-server','--model',native['model'],'--ctx-size','8192','--spec-type','none','--reasoning','on'],'environment':{},'uid':65534,'native_request_options':copy.deepcopy(options)}
  p=profile({'runtime_identities':assets},launch,'test','Test','Q6','R9','e'*64,lambda s:s,{'sampling':{'temperature':1.0,'seed':1001},'chat_template_kwargs':options['chat_template_kwargs'],'output_cap':4096,'template_sha256':assets[native['chat_template']]})
  p['source_provenance']={'kind':'BROKER_NATIVE_CAPTURED_CONFIGURATION','frozen_model_profile_sha256':H(native)}
  return p,native,launch
 def test_native_capture_preserves_actual_configuration_without_a_score(self):
  p,n,l=self.captured_fixture();self.assertTrue(verify_broker_capture(p,n,l));self.assertNotIn('score',p)
 def test_native_capture_rejects_false_identities_and_tuning(self):
  changes=[('model','artifact_sha256','f'*64),('engine','binary_sha256','f'*64),('engine','kernel_library_sha256','f'*64),('engine','build_id','other'),('runtime','context','4096'),('runtime','max_output',1024),('runtime','sampling',{'temperature':0}),('runtime','native_template_controls',{'enable_thinking':False}),('optimizations','speculation_type','mtp'),('source_provenance','frozen_model_profile_sha256','f'*64),('start_parameters','exact_private_launch_sha256','f'*64)]
  for section,key,value in changes:
   p,n,l=self.captured_fixture();p[section][key]=value
   with self.subTest(section=section,key=key):
    with self.assertRaises(ValueError):verify_broker_capture(p,n,l)
 def test_native_capture_rejects_unverified_privilege_or_recipe(self):
  p,n,l=self.captured_fixture();l['uid']=0;p['start_parameters']['exact_private_launch_sha256']=H(l)
  with self.assertRaises(ValueError):verify_broker_capture(p,n,l)
 def test_native_full_coverage_rejects_partial_duplicate_and_changed_denominators(self):
  ids=[f'HumanEval/{i}' for i in range(164)];parts=[{'part':1,'task_ids':ids}];scores=[{'part':1,'tasks':164,'solved':82}];self.assertEqual(native_coverage(parts,scores,ids),82)
  for bad in [[{'part':1,'task_ids':ids[:-1]}],[{'part':1,'task_ids':ids[:-1]+[ids[0]]}]]:
   with self.assertRaises(ValueError):native_coverage(bad,scores,ids)
  with self.assertRaises(ValueError):native_coverage(parts,[{'part':1,'tasks':164,'solved':165}],ids)
  with self.assertRaises(ValueError):native_coverage(parts,[],ids)
 def test_native_partial_result_has_no_run_even_with_profile_present(self):
  self.assertIsNone(native_complete_run('/not/read',{'full_benchmark_score_claimed':False},{},{},lambda *x:None))
 def partial_native_fixture(self,root):
  def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj)+'\n');return digest(path)
  def lines(path,rows):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(''.join(json.dumps(x)+'\n' for x in rows));return digest(path)
  cfg,native,launch=self.captured_fixture();ids=['HumanEval/0','HumanEval/1'];native['selected_task_inputs']={'cases':[{'id':i,'messages':[{'role':'user','content':'synthetic fixture'}]} for i in ids]};cfg['source_provenance']['frozen_model_profile_sha256']=H({k:v for k,v in native.items() if k!='selected_task_inputs'});cfg['runtime'].update(power_limit_w=300,execution_deadline_s=840)
  stage=root/'staging/r9';out=root/'results';score=stage/'scoring/partial';out.mkdir();score.mkdir(parents=True)
  campaign={'expected_task_ids':[f'HumanEval/{i}' for i in range(164)],'immutable_profile_identity_sha256':cfg['source_provenance']['frozen_model_profile_sha256']};ps=save(stage/'CAMPAIGN_PLAN.json',campaign);cfg['source_plan_sha256']=ps
  save(out/'LAUNCH.json',launch);save(out/'profile.json',native);save(out/'CONTRACT.json',{'power_w':300,'runtime_seconds':840})
  raw=lines(out/'HTTP_RESULTS.jsonl',[{'kind':'coding','id':case['id'],'request':{**native['native_recipe']['request_options'],'messages':case['messages']}} for case in native['selected_task_inputs']['cases']])
  samples=lines(score/'JUDGE_SAMPLES.jsonl',[{'task_id':i,'code':'synthetic fixture'} for i in ids]);lines(score/'r9-judge-partial.stdout',[{'task_id':i,'checks':{'base':{'status':'pass'},'plus':{'status':'pass' if n==0 else 'fail'}}} for n,i in enumerate(ids)])
  helper=save(root/'quality_eval.py',{'fixture':'not executed'});paths=[root/'staging/r101'/n for n in ['JUDGE_TASKS.jsonl','calibration3.stdout','calibration5.stdout']]
  for path in paths:save(path,{'fixture':'not executed'})
  save(score/'SCORING_PLAN.json',{'raw_answers_sha256':raw,'judge_samples_sha256':samples,'helper_sha256':helper});save(score/'r9-judge-partial.receipt.json',{'input_sha256':{str(p):digest(p) for p in [score/'JUDGE_SAMPLES.jsonl',root/'quality_eval.py',*paths]}})
  save(out/'RAW_HASHES.json',{n:digest(out/n) for n in ('LAUNCH.json','profile.json','CONTRACT.json')})
  final={'experiment_id':'R9','status':'STOPPED_USER_WHOLE_BENCHMARK_TIME_BUDGET','full_benchmark_score_claimed':False,'campaign_plan_sha256':ps,'raw_root':str(out),'raw_files_sha256':{p.name:digest(p) for p in out.iterdir()},'scoring_files_sha256':{p.name:digest(p) for p in score.iterdir()},'prefix_measurement':{'per_task':[{'id':i,'e2e_s':1,'gpu_energy_j':2} for i in ids]},'peak_device_vram_mib':100,'scored_tasks':2,'solved_observed_tasks':1,'at_utc':'2026-01-01T00:00:00Z'};ap=stage/'TIME_BUDGET_AUDIT.json';ah=save(ap,final);source={**final,'audit_path':str(ap),'audit_sha256':ah};bench={'benchmark_id':'humanevalplus-v0.1.10','benchmark_revision':'fixture','dataset_split_hash':'a'*64,'required_task_count':164};return source,cfg,bench,final,save
 def test_partial_native_result_is_visible_with_exact_actual_denominator(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.partial_native_fixture(root);run=native_partial_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20]);self.assertEqual((run['solved'],run['tasks'],run['intended_tasks']),(1,2,164));self.assertEqual(run['score_percent'],50);self.assertEqual(run['status'],'PARTIAL');self.assertFalse(run['official_eligible']);self.assertFalse(run['full_benchmark_score_claimed']);self.assertEqual(run['gpu_j'],4)
   path=pathlib.Path(final['raw_root'])/'HTTP_RESULTS.jsonl';path.write_text('{}\n')
   with self.assertRaisesRegex(ValueError,'raw evidence'):native_partial_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def test_partial_native_does_not_accept_changed_configuration_or_missing_oracles(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.partial_native_fixture(root);bad=copy.deepcopy(cfg);bad['optimizations']['speculation_type']='draft-mtp'
   with self.assertRaises(ValueError):native_partial_run(root,source,bad,bench,lambda p,h:'audit-'+h[:20])
   stage=root/'staging/r9/scoring/partial';rp=stage/'r9-judge-partial.receipt.json';receipt=json.loads(rp.read_text());receipt['input_sha256'].pop(str(root/'staging/r101/calibration5.stdout'));save(rp,receipt);final['scoring_files_sha256'][rp.name]=digest(rp);source['audit_sha256']=save(pathlib.Path(source['audit_path']),final)
   with self.assertRaisesRegex(ValueError,'oracle/corpus'):native_partial_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def native_files_fixture(self,root,part_size=8):
  """Synthetic metadata fixtures only; never model/GPU measurements."""
  def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj)+'\n');return digest(p)
  ids=[f'HumanEval/{i}' for i in range(164)];cfg,native,launch=self.captured_fixture();native['adapter']='llama-native-coding';cfg['source_provenance']['frozen_model_profile_sha256']=H(native)
  plans=[{'index':i//part_size+1,'id':f'r9-native-part{i//part_size+1:02d}','task_ids':ids[i:i+part_size]} for i in range(0,164,part_size)]
  campaign={'parts':plans,'part_count':len(plans),'expected_task_ids':ids,'immutable_profile_identity_sha256':H(native),'source_workload_sha256':'f'*64};campaign_sha=save(root/'staging/r9/CAMPAIGN_PLAN.json',campaign);cfg['source_plan_sha256']=campaign_sha
  parts=[];scores=[]
  for plan in plans:
   i=plan['index'];tasks=plan['task_ids'];folder=root/'results'/str(i);sc=root/'scores'/str(i);folder.mkdir(parents=True);sc.mkdir(parents=True)
   raw=save(folder/'HTTP_RESULTS.jsonl',{'fixture':'not actual model output'});lh=save(folder/'LAUNCH.json',launch);ph=save(folder/'profile.json',native);ch=save(folder/'CONTRACT.json',{'id':plan['id'],'parameters':{'dataset':'standard164','task_ids':tasks}});save(folder/'RAW_HASHES.json',{'HTTP_RESULTS.jsonl':raw,'LAUNCH.json':lh,'profile.json':ph,'CONTRACT.json':ch})
   ap=folder/'AUDIT.json';ah=save(ap,{'measurement_valid':True,'GPU_execution_observed':True,'case_ids':tasks,'case_inference_wall_s':len(tasks),'case_gpu_energy_j':2*len(tasks),'peak_device_vram_mib':100})
   save(folder/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED','starts':1,'audit_sha256':ah})
   decisions=[{'task_id':task,'checks':{'base':{'status':'pass'},'plus':{'status':'pass' if int(task.split('/')[1])%2==0 else 'fail'}}} for task in tasks];solved=sum(x['checks']['plus']['status']=='pass' for x in decisions)
   judge=sc/f'r9-judge-part{i:02d}.stdout';judge.write_text(''.join(json.dumps(x)+'\n' for x in decisions));samples=save(sc/'JUDGE_SAMPLES.jsonl',{'fixture':True});jr=save(sc/f'r9-judge-part{i:02d}.receipt.json',{'fixture':True});save(sc/'SCORING_PLAN.json',{'raw_answers_sha256':raw,'judge_samples_sha256':samples,'helper_sha256':'e'*64});sp=sc/'AUDIT.json';sh=save(sp,{'tasks':len(tasks),'solved':solved,'task_ids':tasks})
   parts.append({'part':i,'job_id':plan['id'],'task_ids':tasks,'audit_path':str(ap),'audit_sha256':ah,'raw_answers_sha256':raw,'launch_sha256':lh,'profile_snapshot_sha256':ph,'contract_sha256':ch});scores.append({'part':i,'tasks':len(tasks),'solved':solved,'audit_path':str(sp),'audit_sha256':sh,'judge_stdout_sha256':digest(judge),'judge_samples_sha256':samples,'judge_receipt_sha256':jr})
  final={'experiment_id':'R9','full_benchmark_score_claimed':True,'collected_tasks':164,'scored_tasks':164,'campaign_plan_sha256':campaign_sha,'parts':parts,'scoring':scores,'scopes':{'standard_full164':{'tasks':164,'solved':82,'wall_s':164,'gpu_energy_j':328}},'at_utc':'2026-01-01T00:00:00Z'};ap=root/'staging/r9/AUDIT.json';ah=save(ap,final);source={'audit_path':str(ap),'audit_sha256':ah,'full_benchmark_score_claimed':True};d={'benchmark_id':'fixture-native164','required_task_count':164,'expected_task_ids_hash':H(sorted(ids)),'benchmark_revision':'fixture','dataset_split_hash':'a'*64};return source,cfg,d,final,save
 def test_native_complete_files_remain_unqualified_without_api_proof(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.native_files_fixture(root);run=native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20]);self.assertEqual(run['tasks'],164);self.assertEqual(run['solved'],82);self.assertFalse(run['official_eligible']);self.assertIsNone(run['qualification_audit']);self.assertEqual(run['gpu_j'],328)
 def test_full_coding_counter_stays_separate_from_missing_power_integral(self):
  from unittest.mock import patch
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.native_files_fixture(root,part_size=164)
   folder=pathlib.Path(final['parts'][0]['audit_path']).parent;gp=folder/'AUDIT.json';g=json.loads(gp.read_text());g['case_gpu_energy_j']=None;h=save(gp,g);final['parts'][0]['audit_sha256']=h;save(folder/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED','starts':1,'audit_sha256':h});final['scopes']['standard_full164']['gpu_energy_j']=None;source['audit_sha256']=save(pathlib.Path(source['audit_path']),final);source['energy_counter_review']={'fixture':'separate reviewed method'}
   counter={'tasks':164,'solved':82,'lower_j':320.,'upper_j':340.,'audit_id':'counter-fixture'}
   with patch('leaderboard.reviewed_counter_measurement',return_value=counter) as review:
    receipt=lambda p,h:'audit-'+h[:20];run=native_complete_run(root,source,cfg,bench,receipt)
    review.assert_called_once_with(source,folder,[f'HumanEval/{i}' for i in range(164)],82,receipt,kind='coding')
   self.assertIsNone(run['gpu_j']);self.assertIsNone(run['gpu_j_per_success']);self.assertEqual(run['counter_energy'],counter);self.assertIn('counter-fixture',run['audit_ids']);self.assertFalse(run['official_eligible'])
 def test_full_coding_counter_cannot_pool_different_model_sessions(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.native_files_fixture(root);source['energy_counter_review']={'fixture':'not a single session'}
   with self.assertRaisesRegex(ValueError,'one measured session'):native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def test_explicit_empty_template_controls_are_preserved(self):
  cfg=profile({'model_sha256':'a'*64},{'argv':[]},'fixture','Fixture','Q6_K','R9','b'*64,lambda x:x,{'chat_template_kwargs':{}})
  self.assertEqual(cfg['runtime']['native_template_controls'],{})
  unknown=profile({'model_sha256':'a'*64},{'argv':[]},'fixture','Fixture','Q6_K','R9','b'*64,lambda x:x)
  self.assertIsNone(unknown['runtime']['native_template_controls'])
 def test_single_session_workload_comes_from_original_broker_snapshot(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.native_files_fixture(root)
   cp=root/'staging/r9/CAMPAIGN_PLAN.json';campaign=json.loads(cp.read_text());workload=campaign.pop('source_workload_sha256');campaign['dataset']='pinned164';final['campaign_plan_sha256']=save(cp,campaign);cfg['source_plan_sha256']=final['campaign_plan_sha256']
   folder=pathlib.Path(final['parts'][0]['audit_path']).parent;snapshot=folder/'TRUST_SNAPSHOT.json';snapshot_sha=save(snapshot,{'task_datasets':{'pinned164':{'task_ids':campaign['expected_task_ids'],'task_count':164,'original_workload_sha256':workload}}});pins=json.loads((folder/'RAW_HASHES.json').read_text());pins['TRUST_SNAPSHOT.json']=snapshot_sha;save(folder/'RAW_HASHES.json',pins);final['source_workload_sha256']=workload;source['audit_sha256']=save(pathlib.Path(source['audit_path']),final)
   run=native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20]);self.assertEqual(run['evaluated_task_set_hash'],workload)
   final['source_workload_sha256']='0'*64;source['audit_sha256']=save(pathlib.Path(source['audit_path']),final)
   with self.assertRaisesRegex(ValueError,'workload identity'):native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
   snapshot.write_text('{}')
   with self.assertRaisesRegex(ValueError,'snapshot changed'):native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def test_native_complete_files_cannot_hide_a_missing_part_or_changed_source(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,final,save=self.native_files_fixture(root);child=pathlib.Path(final['parts'][-1]['audit_path']);child.write_text('{}')
   with self.assertRaisesRegex(ValueError,'child audit'):native_complete_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
  p,n,l=self.captured_fixture();l['native_request_options']['max_tokens']=1024;p['start_parameters']['exact_private_launch_sha256']=H(l)
  with self.assertRaises(ValueError):verify_broker_capture(p,n,l)
 def replacement_fixture(self,root):
  # Synthetic proof metadata only; no model output or actual GPU measurement.
  def save(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value));return digest(path)
  old=root/'old';retry=root/'retry';tasks=['HumanEval/0'];before={'id':'r9-old','profile':'fixed','parameters':{'task_ids':tasks}};save(old/'CONTRACT.json',before);save(old/'TRUST_SNAPSHOT.json',{'fixture':True});after=dict(before,id='r9-retry');cp=retry/'CONTRACT.json';save(cp,after);log=retry/'ORIGINAL_CONTROLLER_FAILURE.log';log.write_text('fixture pre-GPU failure')
  proof={'decision':'PRE_GPU_SOURCE_HANDOFF_LOCK_FAILURE_NO_MODEL_REQUESTS','model_requests_in_failed_attempt':0,'GPU_execution_in_failed_attempt':False,'original_files':{x.name:digest(x) for x in old.iterdir()},'original_job_id':'r9-old','replacement_job_id':'r9-retry','part':1,'original_receipt_root':str(old),'journal_sha256':digest(log),'replacement_contract_sha256':digest(cp),'original_contract_sha256':digest(old/'CONTRACT.json')};fp=retry/'PROOF.json';save(fp,proof)
  entry={'part':1,'original_job_id':'r9-old','replacement_job_id':'r9-retry','failure_audit_path':str(fp),'failure_audit_sha256':digest(fp),'replacement_contract_path':str(cp),'replacement_contract_sha256':digest(cp)};lp=root/'EXECUTION_ATTEMPTS.json';save(lp,{'campaign_plan_sha256':'a'*64,'replacements':[entry]});a={'campaign_plan_sha256':'a'*64,'execution_attempts':{'path':str(lp),'sha256':digest(lp)}};planned={'index':1,'id':'r9-old','task_ids':tasks};part={'job_id':'r9-retry','planned_job_id':'r9-old'};return a,planned,part,proof,fp,lp,save
 def test_execution_replacement_requires_bound_pre_gpu_evidence(self):
  with tempfile.TemporaryDirectory() as temp:
   root=pathlib.Path(temp);a,p,part,*_=self.replacement_fixture(root);self.assertEqual(native_job_id(root,a,p,part),'r9-retry')
   with self.assertRaises(ValueError):native_job_id(root,{},p,part)
 def test_execution_replacement_cannot_hide_existing_generation(self):
  with tempfile.TemporaryDirectory() as temp:
   root=pathlib.Path(temp);a,p,part,proof,fp,lp,save=self.replacement_fixture(root);proof['model_requests_in_failed_attempt']=1;save(fp,proof);ledger=json.loads(lp.read_text());ledger['replacements'][0]['failure_audit_sha256']=digest(fp);save(lp,ledger);a['execution_attempts']['sha256']=digest(lp)
   with self.assertRaisesRegex(ValueError,'repeat actual GPU generation'):native_job_id(root,a,p,part)
 def test_execution_replacement_cannot_change_model_profile(self):
  with tempfile.TemporaryDirectory() as temp:
   root=pathlib.Path(temp);a,p,part,proof,fp,lp,save=self.replacement_fixture(root);cp=root/'retry/CONTRACT.json';contract=json.loads(cp.read_text());contract['profile']='other';save(cp,contract);proof['replacement_contract_sha256']=digest(cp);save(fp,proof);ledger=json.loads(lp.read_text());ledger['replacements'][0].update(failure_audit_sha256=digest(fp),replacement_contract_sha256=digest(cp));save(lp,ledger);a['execution_attempts']['sha256']=digest(lp)
   with self.assertRaisesRegex(ValueError,'altered the frozen experiment'):native_job_id(root,a,p,part)
 def test_master_catalog_covers_register_and_retains_each_exact_protocol(self):
  reg=json.loads((ROOT/'data/benchmark-register.json').read_text());hist=json.loads((ROOT/'data/configuration-history.json').read_text());before=copy.deepcopy(hist);view=master_catalog(reg,hist)
  self.assertEqual(hist,before);self.assertEqual(set(view['run_columns']),{r['run_id'] for r in hist['runs']})
  for definition in reg['definitions']:
   self.assertTrue(any(c['scope']=='OFFICIAL_LOCAL' and c['protocol']['benchmark_id']==definition['benchmark_id'] for c in view['benchmark_columns']))
  by={c['key']:c for c in view['benchmark_columns']}
  for run in hist['runs']:
   col=by[view['run_columns'][run['run_id']]];self.assertEqual(col['protocol']['scorer_version'],run['scorer_version']);self.assertEqual(col['protocol']['tasks'],run['tasks']);self.assertEqual(col['protocol']['evaluated_task_set_hash'],run['evaluated_task_set_hash'])
   if not run['official_eligible']:self.assertNotEqual(col['scope'],'OFFICIAL_LOCAL')
 def test_master_catalog_does_not_pool_distinct_scorers_or_task_sets(self):
  definition={'benchmark_id':'test','name':'Test','benchmark_revision':'r1','dataset_split_hash':'a'*64,'required_task_count':400,'scorer_version':'official'}
  base={'benchmark_id':'test','benchmark_identity_id':'old','benchmark_revision':'r1','dataset_split_hash':'a'*64,'evaluated_task_set_hash':'b'*64,'scorer_version':'alpha','tasks':100,'metric':'observed_success_percent','official_eligible':False}
  runs=[dict(base,run_id='one'),dict(base,run_id='two',scorer_version='beta'),dict(base,run_id='three',evaluated_task_set_hash='c'*64)]
  view=master_catalog({'definitions':[definition]},{'runs':runs});self.assertEqual(len(set(view['run_columns'].values())),3)
  full=next(c for c in view['benchmark_columns'] if c['scope']=='OFFICIAL_LOCAL');self.assertEqual(full['records'],0);self.assertEqual(full['protocol']['tasks'],400)
 def test_family_grouping_is_presentation_only_and_preserves_protocol_identity(self):
  reg=json.loads((ROOT/'data/benchmark-register.json').read_text());hist=json.loads((ROOT/'data/configuration-history.json').read_text());before=copy.deepcopy((reg,hist));view=master_catalog(reg,hist)
  for c in view['benchmark_columns']:
   self.assertEqual(c['key'],'benchmark-'+H({'protocol':c['protocol'],'scope':c['scope']}))
   self.assertTrue(c['family_id']);self.assertTrue(c['family_name'])
   if c['protocol']['benchmark_id'].startswith('bfcl-'):
    self.assertEqual(c['family_id'],'bfcl')
   if c['protocol']['benchmark_id']=='humanevalplus-v0.1.10':self.assertEqual(c['family_name'],'HumanEval+')
  self.assertEqual((reg,hist),before)
  self.assertEqual({c['category'] for c in view['comparison_categories']},{'coding','tools','agents'})
  self.assertEqual({c['benchmark_id'] for c in view['comparison_categories']},{'humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200','terminal-bench-2.1'})
  unknown={'benchmark_id':'unknown-new-suite','name':'HumanEval+ lookalike'}
  col=master_catalog({'definitions':[unknown]},{'runs':[]})['benchmark_columns'][0]
  self.assertEqual(col['family_id'],'unknown-new-suite','No name-based grouping of unknown protocols')
 def test_deltas_require_same_task_set_and_scorer(self):
  a={'benchmark_identity_id':'a','evaluated_task_set_hash':'b','scorer_version':{'x':1},'tasks':2,'score_percent':50,'wall_s':10,'gpu_j_per_success':100};b={**a,'score_percent':100,'wall_s':8,'gpu_j_per_success':None}
  d=pair_delta(a,b);self.assertTrue(d['comparable']);self.assertEqual(d['quality_delta_pp'],50);self.assertAlmostEqual(d['latency_delta_percent'],-20);self.assertIsNone(d['energy_per_success_delta_percent']);self.assertIn('Whole-profile',d['interpretation'])
  for key in ['benchmark_identity_id','evaluated_task_set_hash','scorer_version','tasks']:
   c={**b,key:'different'};self.assertFalse(pair_delta(a,c)['comparable'])
 def test_publisher_and_local_views_separate_and_no_mean(self):
  reg=json.loads((ROOT/'data/benchmark-register.json').read_text());hist=json.loads((ROOT/'data/configuration-history.json').read_text());comp=json.loads((ROOT/'data/comparison.json').read_text())
  with tempfile.TemporaryDirectory() as tmp:
   d=pathlib.Path(tmp);(d/'benchmarks.md').write_text('# Old\n\n## Official benchmark results and overall mean\n\n91.04%\n\n## Configuration parameters and ranked benchmark results\n\nHistorical details\n');(d/'local-benchmarks.md').write_text('# Local')
   render(reg,hist,comp,d)
   main=(d/'benchmarks.md').read_text();supp=(d/'supplemental-comparison.md').read_text();self.assertIn('configuration-comparison.md#all-measured-results',main);self.assertNotIn('official-leaderboard',main);self.assertNotIn('all-measured-results\"',supp);self.assertNotIn('91.04%',supp);self.assertEqual(main,supp);self.assertNotIn('| ---',main);self.assertNotIn('<div',main);self.assertNotIn('reported_score',main);self.assertIn('EXTERNAL PUBLISHER SELF-REPORTS',(d/'benchmark-register.md').read_text());self.assertEqual(len(list((d/'configuration-profiles').glob('*.md'))),len(hist['profiles']))
 def evidence_fixture(self,tmp):
  root=pathlib.Path(tmp);folder=root/'staging/r1';folder.mkdir(parents=True)
  (folder/'AUDIT.json').write_text('{}')
  def row(i,suite='standard',seconds=1):
   return {'task_id':'HumanEval/'+str(i),'suite':suite,'e2e_s':seconds,'request':{'temperature':0,'seed':1},'native_reply':{'timings':{'prompt_n':10,'prompt_ms':100,'predicted_n':20,'predicted_ms':500}}}
  (folder/'FUNCTIONAL.jsonl').write_text('\n'.join(json.dumps(x) for x in [row(0),row(1),row(0,'long_context_stress',5)]))
  (folder/'server.log').write_text('common_params_print_info: build 0 (unknown)\nCUDA : ARCHS = 700 |\ngeneral.architecture str = qwen35\n')
  pins={p.name:digest(p) for p in folder.iterdir()};(folder/'RAW_HASHES.json').write_text(json.dumps(pins))
  cfg={'runtime_configuration_id':'cfg-test','runtime':{'native_template_controls':None}}
  run={'run_id':'run-test','runtime_configuration_id':'cfg-test','experiment_id':'R1','audit_hash':digest(folder/'AUDIT.json'),'discipline':'coding','tasks':2,'wall_s':2,'gpu_j':40}
  db={'summary':{'r1':{'audit_path':str(folder/'AUDIT.json')}}}
  return root,folder,db,{'profiles':[cfg],'runs':[run]}
 def test_pinned_exact_task_timing_projection_and_unknown_upstream_version(self):
  with tempfile.TemporaryDirectory() as tmp:
   root,folder,db,h=self.evidence_fixture(tmp);before=copy.deepcopy(h)
   ce,me=configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20]);self.assertEqual(h,before)
   self.assertEqual(ce[0]['fields']['model.architecture'],'qwen35');self.assertNotIn('engine.version',ce[0]['fields']);self.assertIn('unknown',ce[0]['fields']['engine.version_provenance_note'])
   self.assertEqual(me[0]['values']['prefill_tok_s'],100);self.assertEqual(me[0]['values']['decode_tok_s'],40);self.assertEqual(me[0]['values']['gpu_j_per_output_token'],1)
   self.assertNotIn('ttft_s',me[0]['values']);self.assertEqual(me[0]['tasks'],2)
   self.assertNotIn('HumanEval/',json.dumps(ce)+json.dumps(me));self.assertTrue(all(x['authority_audit_id'] for x in me[0]['sources']))
 def test_unknown_quantization_uses_only_unambiguous_pinned_engine_type(self):
  for log,known,expected in [('print_info: file type = Q8_0\n','NOT MEASURED','Q8_0'),('print_info: file type = Q8_0\nprint_info: file type = Q6_K\n','NOT MEASURED',None),('model filename: something-Q8_0.gguf\n','NOT MEASURED',None),('print_info: file type = Q8_0\n','Q6_K',None)]:
   with self.subTest(log=log,known=known),tempfile.TemporaryDirectory() as tmp:
    root,folder,db,h=self.evidence_fixture(tmp);h['profiles'][0]['model']={'quantization':known};before=copy.deepcopy(h);p=folder/'server.log';p.write_text(p.read_text()+log);pins=json.loads((folder/'RAW_HASHES.json').read_text());pins['server.log']=digest(p);(folder/'RAW_HASHES.json').write_text(json.dumps(pins));ce,_=configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20]);self.assertEqual(ce[0]['fields'].get('model.quantization'),expected);self.assertEqual(h,before)
 def test_task_phase_uses_original_audit_not_mutable_summary_and_checks_scope(self):
  for seconds in (3,1):
   with self.subTest(seconds=seconds),tempfile.TemporaryDirectory() as tmp:
    root,folder,db,h=self.evidence_fixture(tmp);audit=folder/'AUDIT.json';audit.write_text(json.dumps({'task_phase_s':seconds,'startup_s':7}))
    pinned=digest(audit);pins=json.loads((folder/'RAW_HASHES.json').read_text());pins['AUDIT.json']=pinned;(folder/'RAW_HASHES.json').write_text(json.dumps(pins))
    db['summary']['r1'].update(audit_sha256=pinned,task_phase_s=999);h['runs'][0].update(audit_hash=pinned,solved=1)
    if seconds==1:
     with self.assertRaisesRegex(ValueError,'shorter than recorded'):configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20])
    else:
     _,me=configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20]);self.assertEqual(me[0]['values']['task_phase_s'],3);self.assertEqual(me[0]['values']['successful_tasks_per_task_phase_s'],1/3);self.assertEqual(me[0]['values']['startup_s'],7)
     self.assertTrue(any(s['filename']=='AUDIT.json' and s['sha256']==pinned for s in me[0]['sources']))
 def test_explicit_unknown_metadata_can_be_supplemented_but_known_values_cannot(self):
  for value in (None,'NOT MEASURED','NICHT ERFASST','Q6_K'):
   with self.subTest(value=value):
    p,_,_=self.captured_fixture();p['model']['quantization']=value;p['runtime_configuration_id']='cfg-'+H({k:v for k,v in p.items() if k!='runtime_configuration_id'});before=copy.deepcopy(p)
    e={'runtime_configuration_id':p['runtime_configuration_id'],'fields':{'model.quantization':'Q8_0'},'sources':[{'filename':'server.log','sha256':'a'*64,'authority_audit_id':'audit-'+'a'*20}]};e['evidence_id']='evidence-'+H(e);data={'profiles':[p],'runs':[],'attempts':[],'configuration_evidence':[e]}
    if value=='Q6_K':
     with self.assertRaisesRegex(ValueError,'contradicts immutable'):validate_history(data,{})
    else:
     self.assertTrue(validate_history(data,{}));other=copy.deepcopy(e);other['fields']['model.quantization']='Q6_K';other['evidence_id']='evidence-'+H({k:v for k,v in other.items() if k!='evidence_id'});data['configuration_evidence'].append(other)
     with self.assertRaisesRegex(ValueError,'Conflicting evidence'):validate_history(data,{})
    self.assertEqual(p,before)
 def test_modified_execution_evidence_is_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root,folder,db,h=self.evidence_fixture(tmp);(folder/'server.log').write_text('version: 99.0.0')
   with self.assertRaisesRegex(ValueError,'source changed'):configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20])
 def test_timing_requires_matching_count_and_independent_wall_sum(self):
  for key,value in [('tasks',3),('wall_s',9)]:
   with tempfile.TemporaryDirectory() as tmp:
    root,folder,db,h=self.evidence_fixture(tmp);h['runs'][0][key]=value
    ce,me=configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20]);self.assertTrue(ce);self.assertEqual(me,[])
 def test_no_metadata_reconstruction_from_different_original_audit(self):
  with tempfile.TemporaryDirectory() as tmp:
   root,folder,db,h=self.evidence_fixture(tmp);h['runs'][0]['audit_hash']='a'*64
   ce,me=configuration_evidence(root,db,h,lambda p,s:'audit-'+s[:20]);self.assertEqual(ce,[]);self.assertEqual(me,[])

 def test_archived_diagnostic_is_not_new_benchmark_or_qualification(self):
  reg=json.loads((ROOT/'data/benchmark-register.json').read_text());history=json.loads((ROOT/'data/configuration-history.json').read_text())
  items=reg.get('archived_diagnostics',[]);self.assertTrue(items)
  for d in items:
   self.assertEqual(d['new_GPU_runs'],0);self.assertTrue(d['original_results_unchanged']);self.assertNotIn('analysis_path',d);self.assertNotIn('followup_path',d)
   a=d['summary'];self.assertEqual(sum(a['classification'].values()),a['overall']['tasks']);self.assertEqual(a['quality_score_unchanged']['solved'],a['overall']['solved'])
   self.assertEqual(a['parser_checks']['empty_reasoning_equals_raw_trimmed'],a['empty_final_content']['tasks']);self.assertEqual(a['parser_checks']['nonempty_final_equals_raw_post_close_trimmed'],a['nonempty_final_content']['tasks'])
   self.assertEqual(a['parser_checks']['explicit_reasoning_token_counts_available'],0)
   self.assertEqual(d['followup']['common_constraints']['whole_benchmark_seconds'],900);self.assertIn('SEPARATE_GPU_APPROVAL',d['followup']['status'])
   self.assertNotIn('case_diagnostics',a);self.assertNotIn('source_evidence',a)
   w=d['weight_provenance'];self.assertTrue(w['local_R448_artifact']['current_published_LFS_matches']);self.assertTrue(w['upstream_safetensors']['current_equals_original_upload_LFS']);self.assertEqual(w['source_lineage']['exact_quantizer_to_upstream_checkpoint_derivation'],'NOT VERIFIED');self.assertFalse(w['independent_header_inventory']['header_comparison_is_payload_comparison']);self.assertNotIn('weight_provenance_path',d)
  self.assertTrue(all(r['benchmark_id']!='ARCHIVED_RESPONSE_DIAGNOSTIC_ISSUE12' for r in history['runs']))

class OfflinePayloadTests(unittest.TestCase):
 def decode(self,source):
  import re
  decoder=json.JSONDecoder()
  raw_prefix='window.V100Leaderboard=JSON.parse('
  if source.startswith(raw_prefix):
   raw,_=decoder.raw_decode(source[len(raw_prefix):]);return json.loads(raw)
  prefix='(function(){const p='
  self.assertTrue(source.startswith(prefix))
  pool,end=decoder.raw_decode(source[len(prefix):]);rest=source[len(prefix)+end:]
  self.assertTrue(rest.startswith(';const s='))
  packed,end=decoder.raw_decode(rest[len(';const s='):]);rest=rest[len(';const s=')+end:]
  self.assertTrue(rest.startswith(';const r='))
  pattern,_=decoder.raw_decode(rest[len(';const r='):])
  return json.loads(re.sub(pattern,lambda m:pool[int(m.group(1))],packed))
 def test_plain_payload_retains_missing_zero_false_and_JSON_keys(self):
  from leaderboard import offline_payload
  data={'zero':0,'missing':None,'disabled':False,'empty':'','__proto__':{'prototype_data':'retained'}}
  source=offline_payload(data);self.assertEqual(self.decode(source),data)
 def test_packed_payload_preserves_quotes_unicode_arrays_and_every_field(self):
  from leaderboard import offline_payload
  text='recorded "quoted" field; path\\name\nDeutsch ä 日本語 <tag> '+'x'*128
  data={'rows':[{'field_with_long_identity_name':text,'unknown':None,'zero':0,'false':False,'array':[1,2,3]} for _ in range(100)]}
  source=offline_payload(data,0);self.assertTrue(source.startswith('(function()'))
  self.assertEqual(self.decode(source),data);self.assertNotIn('<',source)
  self.assertLess(len(source),len(offline_payload(data,10**9)))
  self.assertEqual(source,offline_payload(data,0))
 def test_reserved_sentinel_lookalike_is_original_data(self):
  from leaderboard import offline_payload
  data={'sentinel':'__V100_POOL_0__42','repeated':['long existing artifact identity '+('a'*128)]*100}
  source=offline_payload(data,0);self.assertEqual(self.decode(source),data)
 def test_nonfinite_numbers_are_rejected_before_publication(self):
  from leaderboard import offline_payload
  for value in [float('nan'),float('inf'),-float('inf')]:
   with self.assertRaises(ValueError):offline_payload({'value':value},0)

if __name__=='__main__':unittest.main()

class FrozenSingleSessionMetadata(unittest.TestCase):
 def test_contract_bound_alternate_spelling_and_tampering(self):
  from leaderboard import normalized_native_part
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);contract={'id':'example-job','profile':'example-profile','parameters':{'task_ids':['task-a','task-b']}}
   (root/'CONTRACT.json').write_text(json.dumps(contract));part={'contract_sha256':digest(root/'CONTRACT.json'),'job_id':'example-job'}
   p={'part':1,'tasks':['task-a','task-b'],'profile':'example-profile'};campaign={'part_count':1,'profile':'example-profile'};before=copy.deepcopy(p)
   result=normalized_native_part(p,campaign,root,part);self.assertEqual(result['id'],'example-job');self.assertEqual(result['task_ids'],p['tasks']);self.assertEqual(p,before)
   for key,value in [('profile','other'),('tasks',p['tasks'][:-1]),('part',2)]:
    changed={**p,key:value}
    with self.assertRaises(ValueError):normalized_native_part(changed,campaign,root,part)
   with self.assertRaises(ValueError):normalized_native_part(p,campaign,root,{**part,'contract_sha256':'0'*64})
 def test_original_partition_schema_is_preserved(self):
  from leaderboard import normalized_native_part
  p={'index':1,'id':'original-job','task_ids':['a']};self.assertEqual(normalized_native_part(p,{},None,{}),p)
