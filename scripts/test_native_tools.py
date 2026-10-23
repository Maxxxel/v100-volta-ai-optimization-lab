"""Synthetic provenance fixtures only: no GPU, model, tool execution or private data."""
import copy,json,pathlib,tempfile,unittest
import test_leaderboard as fixtures
from leaderboard import H,digest,native_tool_run
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
if __name__=='__main__':unittest.main()
