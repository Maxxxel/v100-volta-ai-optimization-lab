"""Synthetic provenance fixtures only: no GPU, model, tool execution or private data."""
import copy,inspect,hashlib,json,pathlib,tempfile,unittest
import test_leaderboard as fixtures
from leaderboard import H,digest,native_tool_run,native_reused_tool_run,counter_energy_bounds
class NativeToolsTests(unittest.TestCase):
 def fixture(self,root):
  def save(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj)+'\n');return digest(p)
  def lines(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r)+'\n' for r in rows));return digest(p)
  stage=root/'staging/r9';out=root/'results';old=root/'staging/r281';category=root/'staging/leaderboard-register/bfcl-simple-python400';ids=[f'simple_python_{i}' for i in range(400)]
  cfg,native,launch=fixtures.LeaderboardTests().captured_fixture();native['adapter']='llama-native-tools';native['selected_task_inputs']={'cases':[{'id':i,'messages':[{'role':'user','content':'synthetic fixture'}],'tools':[],'native_tools_sha256':H([]),'expected_native_tools_sha256':H([]),'original_question_sha256':'c'*64} for i in ids]};native_sha=H({k:v for k,v in native.items() if k!='selected_task_inputs'});cfg['source_provenance']['frozen_model_profile_sha256']=native_sha
  campaign={'expected_task_ids':ids,'immutable_profile_identity_sha256':native_sha};plan_sha=save(stage/'CAMPAIGN_PLAN.json',campaign);cfg['source_plan_sha256']=plan_sha;cfg_sha=save(stage/'CONFIGURATION_PROFILE.json',cfg)
  for n,v in [('profile.json',native),('LAUNCH.json',launch),('CONTRACT.json',{'parameters':{'task_ids':ids}})]:save(out/n,v)
  rows=[{'kind':'native_tool','id':i,'request':{**native['native_recipe']['request_options'],'messages':native['selected_task_inputs']['cases'][n]['messages'],'tools':[]},'e2e_s':1} for n,i in enumerate(ids)]
  for row in rows:row['request_sha256']=H(row['request'])
  raw_sha=lines(out/'HTTP_RESULTS.jsonl',rows);save(out/'RAW_HASHES.json',{n:digest(out/n) for n in ('profile.json','LAUNCH.json','CONTRACT.json','HTTP_RESULTS.jsonl')})
  gpu={'measurement_valid':True,'GPU_execution_observed':True,'per_task':[{'id':i,'e2e_s':1,'gpu_energy_j':2,'energy_complete':True} for i in ids],'case_inference_wall_s':400,'case_gpu_energy_j':800,'peak_device_vram_mib':7000};gpu_sha=save(out/'AUDIT.json',gpu);save(out/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED','audit_sha256':gpu_sha})
  task_sha=save(category/'TASKS.json',{'tasks':native['selected_task_inputs']['cases']});tools_sha=save(category/'TOOLS.json',{'tasks':[{'id':i,'tools':[],'tools_sha256':H([])} for i in ids]});prep_sha=save(category/'PREPARATION_AUDIT.json',{'TASKS_sha256':task_sha,'TOOLS_sha256':tools_sha})
  ds={'source_question_file_sha256':'a'*64,'source_answer_file_sha256':'b'*64,'source_revision':'fixture','tasks_file':str(category/'TASKS.json'),'tools_file':str(category/'TOOLS.json'),'tasks_sha256':task_sha,'tools_sha256':tools_sha};save(out/'TRUST_SNAPSHOT.json',{'task_datasets':{'bfcl-v4-simple-python-full400':ds}})
  worker_sha=save(stage/'score_native.py',{'fixture':'not executable'});utils_sha=save(stage/'OFFICIAL_BFCL_UTILS.txt',{'fixture':'not executable'});adapter_sha=save(old/'quality_eval_frozen.py',{'fixture':'not executable'});bundle_sha=save(old/'BFCL_ANALYSIS_SUBSET.tar',{'fixture':True});save(root/'staging/bfcl/INPUTS.tar',{'fixture':True})
  scoring_sha=save(stage/'SCORING_PLAN.json',{'case_ids':ids,'responses_sha256':raw_sha,'worker_sha256':worker_sha,'official_utils_sha256':utils_sha})
  bindings=[root/'staging/bfcl/INPUTS.tar',old/'BFCL_ANALYSIS_SUBSET.tar',old/'quality_eval_frozen.py',out/'HTTP_RESULTS.jsonl',category/'TASKS.json',stage/'OFFICIAL_BFCL_UTILS.txt',stage/'SCORING_PLAN.json',stage/'score_native.py']
  observed=[{'id':i,'official_AST_success':n<300} for n,i in enumerate(ids)]+[{'kind':'summary','tasks':400,'official_AST_solved':300,'practical_solved':280,'official_revision':'fixture','official_functions_modified':False,'model_requests':0,'tool_executions':0}];receipts=[]
  for label in ('score','replay'):
   oh=lines(stage/(label+'.stdout'),observed);rh=save(stage/(label+'.receipt.json'),{'returncode':0,'properties':'Result=success\nExecMainStatus=0','input_sha256':{str(p):digest(p) for p in bindings}});receipts.append({'label':label,'stdout_sha256':oh,'receipt_sha256':rh})
  a={'experiment_id':'R9','benchmark_id':'bfcl-v4-simple-python-full400','campaign_plan_sha256':plan_sha,'runtime_configuration_profile_sha256':cfg_sha,'model_starts':1,'parts':[{'audit_path':str(out/'AUDIT.json'),'audit_sha256':gpu_sha}],'collected_tasks':400,'scored_tasks':400,'full_benchmark_score_claimed':True,'scoring_plan_sha256':scoring_sha,'scoring_receipts':receipts,'changed_replay_judgements':[],'solved_observed_tasks':300,'practical_solved':280,'protocol_valid':390,'complete':395,'at_utc':'2026-01-01T00:00:00Z'};ap=stage/'AUDIT.json';ah=save(ap,a)
  source={'benchmark_id':a['benchmark_id'],'audit_path':str(ap),'audit_sha256':ah};bench={'benchmark_id':a['benchmark_id'],'benchmark_revision':'fixture','dataset_split_hash':'a'*64,'reference_answers_sha256':'b'*64,'required_task_count':400,'expected_task_ids_hash':H(sorted(ids)),'preparation_audit_sha256':prep_sha,'scorer_version':{'native_score_wrapper_sha256':worker_sha,'official_native_format_sha256':utils_sha,'frozen_checker_adapter_sha256':adapter_sha,'frozen_checker_bundle_sha256':bundle_sha},'metric':'bfcl_simple_python_ast_accuracy_percent'}
  return source,cfg,bench,a,save,lines
 def project(self,root,source,cfg,bench):return native_tool_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def test_complete_category_is_pending_not_automatic_qualification(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);r=self.project(root,source,cfg,bench);self.assertEqual((r['solved'],r['tasks'],r['score_percent']),(300,400,75));self.assertEqual(r['practical_protocol']['solved'],280);self.assertEqual((r['wall_s'],r['gpu_j']),(400,800));self.assertFalse(r['official_eligible']);self.assertIsNone(r['qualification_audit'])
 def test_partial_cannot_claim_complete_official_category(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);a['scored_tasks']=399;source['audit_sha256']=save(pathlib.Path(source['audit_path']),a)
   with self.assertRaisesRegex(ValueError,'not complete'):self.project(root,source,cfg,bench)
 def test_self_hashed_new_checker_is_not_a_reviewed_official_scorer(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);save(root/'staging/r281/quality_eval_frozen.py',{'changed':True})
   with self.assertRaisesRegex(ValueError,'unreviewed checker'):self.project(root,source,cfg,bench)
 def test_corrupted_raw_responses_are_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);save(root/'results/HTTP_RESULTS.jsonl',{'changed':True})
   with self.assertRaisesRegex(ValueError,'raw identity'):self.project(root,source,cfg,bench)
 def test_practical_score_cannot_replace_official_ast_score(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);a['solved_observed_tasks']=280;source['audit_sha256']=save(pathlib.Path(source['audit_path']),a)
   with self.assertRaisesRegex(ValueError,'score mismatch'):self.project(root,source,cfg,bench)
 def test_replay_difference_is_rejected_even_after_its_hash_is_updated(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.fixture(root);p=root/'staging/r9/replay.stdout';rows=[json.loads(x) for x in p.read_text().splitlines()];rows[0]['official_AST_success']=False;a['scoring_receipts'][1]['stdout_sha256']=lines(p,rows);source['audit_sha256']=save(pathlib.Path(source['audit_path']),a)
   with self.assertRaisesRegex(ValueError,'replay mismatch'):self.project(root,source,cfg,bench)
class FullCounterSupplementTests(unittest.TestCase):
 project=NativeToolsTests.project
 def fixture(self,root):
  source,cfg,bench,a,save,lines=NativeToolsTests().fixture(root);out=root/'results';stage=root/'staging/r9';raw=out/'HTTP_RESULTS.jsonl';rows=[json.loads(l) for l in raw.read_text().splitlines()]
  for i,r in enumerate(rows):r.update(start_ns=i*1000000000,end_ns=(i+1)*1000000000)
  lines(raw,rows);gpu=json.loads((out/'AUDIT.json').read_text());gpu['case_gpu_energy_j']=None
  for r in gpu['per_task']:r.update(gpu_energy_j=None,energy_complete=False)
  gh=save(out/'AUDIT.json',gpu);save(out/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED','audit_sha256':gh});a['parts'][0]['audit_sha256']=gh;save(out/'RAW_HASHES.json',{n:digest(out/n) for n in ('profile.json','LAUNCH.json','CONTRACT.json','HTTP_RESULTS.jsonl')});sp=stage/'SCORING_PLAN.json';d=json.loads(sp.read_text());d['responses_sha256']=digest(raw);a['scoring_plan_sha256']=save(sp,d)
  for entry in a['scoring_receipts']:
   rp=stage/(entry['label']+'.receipt.json');d=json.loads(rp.read_text());d['input_sha256'][str(raw)]=digest(raw);d['input_sha256'][str(sp)]=digest(sp);entry['receipt_sha256']=save(rp,d)
  source['audit_sha256']=save(stage/'AUDIT.json',a);tele=out/'GPU_TELEMETRY.jsonl';lines(tele,[{'nvml_begin_ns':i*1000000000,'at_ns':i*1000000000,'gpu_energy_counter_mj':i*1000} for i in range(401)]);ids=[r['id'] for r in rows];measurement=counter_energy_bounds([json.loads(l) for l in tele.read_text().splitlines()],rows,ids);measurement.update(solved=300,j_per_success_lower=measurement['lower_j']/300,j_per_success_upper=measurement['upper_j']/300)
  review={'status':'BOUNDED_REPORTED_HARDWARE_COUNTER_ENERGY','GPU_runs':0,'model_requests':0,'source_API':'nvmlDeviceGetTotalEnergyConsumption','counter_unit':'mJ','selected_task_ids':ids,'source_function_sha256':hashlib.sha256(inspect.getsource(counter_energy_bounds).encode()).hexdigest(),'source_files_sha256':{str(p):digest(p) for p in [raw,tele,stage/'AUDIT.json']},'measurement':measurement};path=stage/'ENERGY_COUNTER_REVIEW.json';source['energy_counter_review']={'path':str(path),'sha256':save(path,review)};return source,cfg,bench,review,path,save
 def test_counter_bounds_do_not_fill_a_failed_power_integral(self):
  with tempfile.TemporaryDirectory() as t:
   root=pathlib.Path(t);source,cfg,bench,review,path,save=self.fixture(root);r=self.project(root,source,cfg,bench);self.assertIsNone(r['gpu_j']);self.assertIsNone(r['gpu_j_per_success']);self.assertEqual(r['counter_energy']['lower_j'],400);self.assertEqual(r['counter_energy']['j_per_success_lower'],400/300);self.assertIn(r['counter_energy']['audit_id'],r['audit_ids'])
 def test_rehashed_bounds_or_success_denominator_cannot_change_the_measurement(self):
  for field,value in [('lower_j',399),('solved',400),('j_per_success_lower',1)]:
   with tempfile.TemporaryDirectory() as t:
    root=pathlib.Path(t);source,cfg,bench,review,path,save=self.fixture(root);review['measurement'][field]=value;source['energy_counter_review']['sha256']=save(path,review)
    with self.subTest(field=field),self.assertRaisesRegex(ValueError,'bounds/success'):self.project(root,source,cfg,bench)
 def test_original_telemetry_changes_cannot_be_hidden_by_the_counter_receipt(self):
  with tempfile.TemporaryDirectory() as t:
   root=pathlib.Path(t);source,cfg,bench,review,path,save=self.fixture(root);(root/'results/GPU_TELEMETRY.jsonl').write_text('{}\n')
   with self.assertRaisesRegex(ValueError,'source changed'):self.project(root,source,cfg,bench)
 def test_an_unreviewed_method_is_rejected_even_with_a_new_receipt_hash(self):
  with tempfile.TemporaryDirectory() as t:
   root=pathlib.Path(t);source,cfg,bench,review,path,save=self.fixture(root);review['source_function_sha256']='0'*64;source['energy_counter_review']['sha256']=save(path,review)
   with self.assertRaisesRegex(ValueError,'method/task'):self.project(root,source,cfg,bench)
class ReusedNativeToolsTests(unittest.TestCase):
 fixture=NativeToolsTests.fixture
 def reused_fixture(self,root):
  source,cfg,bench,a,save,lines=self.fixture(root);stage=pathlib.Path(source['audit_path']).parent;out=root/'results';native=json.loads((out/'profile.json').read_text());base=copy.deepcopy(native);base.pop('selected_task_inputs');allids=[c['id'] for c in native['selected_task_inputs']['cases']];newids=allids[40:];raw=[json.loads(l) for l in (out/'HTTP_RESULTS.jsonl').read_text().splitlines()]
  for r in raw:r['reply']={}
  old=raw[:40];fresh=raw[40:];lines(stage/'ORIGINAL40.jsonl',old);reused_sha=lines(stage/'REUSED_RESPONSES.jsonl',old);merged_sha=lines(stage/'MERGED_RESPONSES.jsonl',raw);lines(out/'HTTP_RESULTS.jsonl',fresh);native['selected_task_inputs']['cases']=native['selected_task_inputs']['cases'][40:];save(out/'profile.json',native);save(out/'CONTRACT.json',{'parameters':{'task_ids':newids}})
  snap=json.loads((out/'TRUST_SNAPSHOT.json').read_text());snap['profiles']={'base':base};save(out/'TRUST_SNAPSHOT.json',snap);save(stage/'EXECUTION_REVIEW.json',{'parent_profile':'base'})
  reuse={'status':'FROZEN_CATEGORY_REUSE_SOURCE_AND_RECIPE_VERIFIED','quality_filtering':False,'base_profile_identity_sha256':H(base),'reused_task_ids':allids[:40],'remaining_task_ids':newids,'existing_official_AST_solved':40,'source_files_sha256':{str(stage/'ORIGINAL40.jsonl'):digest(stage/'ORIGINAL40.jsonl')}};reuse_sha=save(stage/'REUSE_VALIDATION.json',reuse)
  plan={'experiment_id':'R9','expected_task_ids':allids,'new_task_ids':newids,'reused_task_ids':allids[:40],'immutable_profile_identity_sha256':H(base),'base_profile_identity_sha256':H(base),'reuse_validation_sha256':reuse_sha,'reused_responses_sha256':reused_sha};plan_sha=save(stage/'CAMPAIGN_PLAN.json',plan);cfg['source_plan_sha256']=plan_sha;cfg_sha=save(stage/'CONFIGURATION_PROFILE.json',cfg)
  gpu=json.loads((out/'AUDIT.json').read_text());gpu.update(per_task=gpu['per_task'][40:],case_ids=newids,execution_uid=65534,model_starts=1,case_inference_wall_s=360,case_gpu_energy_j=720);gpu_sha=save(out/'AUDIT.json',gpu);save(out/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED','audit_sha256':gpu_sha});save(out/'RAW_HASHES.json',{n:digest(out/n) for n in ('profile.json','LAUNCH.json','CONTRACT.json','HTTP_RESULTS.jsonl')})
  scoreplan=json.loads((stage/'SCORING_PLAN.json').read_text());scoreplan.update(responses_sha256=merged_sha,new_responses_sha256=digest(out/'HTTP_RESULTS.jsonl'),reused_responses_sha256=reused_sha);scoreplan_sha=save(stage/'SCORING_PLAN.json',scoreplan)
  for entry in a['scoring_receipts']:
   rp=stage/(entry['label']+'.receipt.json');execution=json.loads(rp.read_text());execution['input_sha256'].pop(str(out/'HTTP_RESULTS.jsonl'));execution['input_sha256'][str(stage/'MERGED_RESPONSES.jsonl')]=merged_sha;execution['input_sha256'][str(stage/'SCORING_PLAN.json')]=scoreplan_sha;entry['receipt_sha256']=save(rp,execution)
  a.update(new_model_starts=1,campaign_plan_sha256=plan_sha,runtime_configuration_profile_sha256=cfg_sha,merged_responses_sha256=merged_sha,scoring_plan_sha256=scoreplan_sha,matched_performance={'tasks':360,'solved':260,'task_ids_hash':H(sorted(newids)),'wall_s':360,'gpu_j':720,'gpu_j_per_success':720/260,'successful_tasks_per_s':260/360,'peak_vram_mib':7000});a['parts'][0]['audit_sha256']=gpu_sha;source['audit_sha256']=save(pathlib.Path(source['audit_path']),a);return source,cfg,bench,a,save,lines
 def reused_project(self,root,source,cfg,bench):return native_reused_tool_run(root,source,cfg,bench,lambda p,h:'audit-'+h[:20])
 def test_reused400_quality_never_inherits360_costs_as_full400_metrics(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.reused_fixture(root);r=self.reused_project(root,source,cfg,bench);self.assertEqual((r['solved'],r['tasks']),(300,400));self.assertIsNone(r['wall_s']);self.assertIsNone(r['gpu_j']);self.assertIsNone(r['gpu_j_per_success']);self.assertEqual(r['matched_performance']['tasks'],360);self.assertEqual(r['matched_performance']['gpu_j_per_success'],720/260);self.assertFalse(r['official_eligible'])
 def test_360_energy_cannot_be_divided_by400_quality_successes(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.reused_fixture(root);a['matched_performance']['gpu_j_per_success']=720/300;source['audit_sha256']=save(pathlib.Path(source['audit_path']),a)
   with self.assertRaisesRegex(ValueError,'cost scope/count'):self.reused_project(root,source,cfg,bench)
 def test_changed_historical_witness_is_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.reused_fixture(root);save(root/'staging/r9/ORIGINAL40.jsonl',{'changed':True})
   with self.assertRaisesRegex(ValueError,'original witness'):self.reused_project(root,source,cfg,bench)
 def test_merged_reply_cannot_be_silently_replaced(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.reused_fixture(root);stage=pathlib.Path(source['audit_path']).parent;rows=[json.loads(l) for l in (stage/'MERGED_RESPONSES.jsonl').read_text().splitlines()];rows[0]['reply']={'changed':True};a['merged_responses_sha256']=lines(stage/'MERGED_RESPONSES.jsonl',rows);source['audit_sha256']=save(pathlib.Path(source['audit_path']),a)
   with self.assertRaisesRegex(ValueError,'merged answers'):self.reused_project(root,source,cfg,bench)
 def test_reuse_profile_changes_are_not_a_controlled_same_profile(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);source,cfg,bench,a,save,lines=self.reused_fixture(root);snap=root/'results/TRUST_SNAPSHOT.json';d=json.loads(snap.read_text());d['profiles']['base']['native_recipe']['request_options']['temperature']=0.2;save(snap,d)
   with self.assertRaisesRegex(ValueError,'historical inference profile'):self.reused_project(root,source,cfg,bench)
class CounterEnergyTests(unittest.TestCase):
 def trace(self):return [{'nvml_begin_ns':i*1000000000,'at_ns':i*1000000000,'gpu_energy_counter_mj':i*100000} for i in range(11)]
 def rows(self):return [{'id':str(i),'start_ns':(i*2+1)*1000000000,'end_ns':(i*2+2)*1000000000} for i in range(4)]
 def test_exact_boundaries_recover_known_counter_energy(self):
  r=counter_energy_bounds(self.trace(),self.rows(),['0','1','2','3']);self.assertEqual((r['lower_j'],r['upper_j']),(700,700));self.assertEqual(r['groups'],1);self.assertEqual(r['included_between_request_setup_s'],3)
 def test_unselected_task_groups_are_excluded(self):
  r=counter_energy_bounds(self.trace(),self.rows(),['0','2']);self.assertEqual((r['lower_j'],r['upper_j']),(200,200));self.assertEqual(r['tasks'],2);self.assertEqual(r['groups'],2)
 def test_query_uncertainty_is_bounded_never_interpolated(self):
  t=self.trace()
  for x in t:x['nvml_begin_ns']-=100000000;x['at_ns']+=100000000
  r=counter_energy_bounds(t,self.rows(),['0','1']);self.assertEqual((r['lower_j'],r['upper_j']),(100,500));self.assertLessEqual(r['lower_j'],300);self.assertGreaterEqual(r['upper_j'],300)
 def test_missing_or_reset_counters_fail_closed(self):
  for value in (None,-1,False):
   t=self.trace();t[5]['gpu_energy_counter_mj']=value
   with self.subTest(value=value),self.assertRaises(ValueError):counter_energy_bounds(t,self.rows(),['0'])
  t=self.trace();t[5]['gpu_energy_counter_mj']=0
  with self.assertRaises(ValueError):counter_energy_bounds(t,self.rows(),['0'])
 def test_missing_brackets_or_duplicate_tasks_fail_closed(self):
  with self.assertRaises(ValueError):counter_energy_bounds(self.trace()[2:],self.rows(),['0'])
  with self.assertRaises(ValueError):counter_energy_bounds(self.trace(),self.rows(),['0','0'])
  with self.assertRaises(ValueError):counter_energy_bounds(self.trace(),self.rows(),['missing'])
if __name__=='__main__':unittest.main()
