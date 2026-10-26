"""Public paired-tool provenance; synthetic CPU fixtures never enter research data."""
import copy,hashlib,json,pathlib,tempfile,unittest
import export
from unittest.mock import patch
from leaderboard import counter_energy_bounds
class PairedTools(unittest.TestCase):
 def setUp(self):
  real_digest=export.digest
  def fixture_digest(path):
   path=pathlib.Path(path)
   if path.name=='score_native.py' and path.read_bytes()==b'CPU_FIXTURE_WORKER':return '3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666'
   if path.name=='OFFICIAL_BFCL_UTILS.txt' and path.read_bytes()==b'CPU_FIXTURE_UTILS':return '3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd'
   return real_digest(path)
  self.mock_digest=patch.object(export,'digest',side_effect=fixture_digest);self.mock_digest.start();self.addCleanup(self.mock_digest.stop)
 def fixture(self,tmp):
  root=pathlib.Path(tmp)/'canonical';stage=root/'staging/r546';stage.mkdir(parents=True);raw=root.parent/'research/mcp-workspace/CPU_ONLY/host-fixture';raw.mkdir(parents=True)
  def put(p,d):p.write_text(json.dumps(d));return p
  def lines(p,d):p.write_text(''.join(json.dumps(v)+'\n' for v in d));return p
  original={'worker_sha256':'3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666','official_utils_sha256':'3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd','task_manifest_sha256':'d'*64,'source_revision':'e'*40};(root/'staging/r542').mkdir()
  task_file=root/'OFFICIAL_FIXTURE_TASKS.json';put(task_file,{'CPU_FIXTURE_ONLY':True});original['task_manifest_sha256']=export.digest(task_file)
  put(root/'staging/r542/SCORING_PLAN.json',original)
  (stage/'score_native.py').write_bytes(b'CPU_FIXTURE_WORKER');(stage/'OFFICIAL_BFCL_UTILS.txt').write_bytes(b'CPU_FIXTURE_UTILS')
  p={'native_recipe':{'mtp_tools_confirmation':{'version':'MTP_TOOLS_AB400_V1','arms':['A','B'],'base_requests_per_arm':200,'model_starts':2,'total_task_seconds':1200,'includes_model_setup':True}},'model_sha256':'a'*64,'native_mtp_draft':{'sha256':'b'*64},'runtime':'/engine','assets':{'/engine/llama-server':'c'*64}}
  contract={'id':'r546-native-mtp-tools-confirmation400','runtime_seconds':1200,'parameters':{'dataset':'omni-native-mtp-tools-confirmation400-v1','task_ids':['parallel_multiple_'+str(i)+'--'+a for a in ('A','B') for i in range(200)]}}
  row={'kind':'native_tool','id':'parallel_multiple_0--A','start_ns':1000000000,'end_ns':2000000000,'e2e_s':1.0,'reply':{'usage':{'completion_tokens':1},'content':'PRIVATE_FIXTURE_TEXT'}}
  telemetry=[{'at_ns':i*500000000,'nvml_begin_ns':i*500000000,'gpu_energy_counter_mj':i*500} for i in range(6)]
  for n,d in [('profile.json',p),('CONTRACT.json',contract)]:put(raw/n,d)
  put(raw/'TRUST_SNAPSHOT.json',{'task_datasets':{'bfcl-v4-parallel-multiple-full200':{'tasks_file':str(task_file),'tasks_sha256':export.digest(task_file)}}})
  lines(raw/'HTTP_RESULTS.jsonl',[row]);lines(raw/'GPU_TELEMETRY.jsonl',telemetry)
  folder=stage/'A';folder.mkdir();mapped=copy.deepcopy(row);mapped['id']='parallel_multiple_0';lines(folder/'RESPONSES.jsonl',[mapped])
  plan={**original,'case_ids':[mapped['id']],'responses_sha256':export.digest(folder/'RESPONSES.jsonl')};put(folder/'SCORING_PLAN.json',plan)
  output=[{'id':mapped['id'],'official_AST_success':True},{'tasks':1,'official_AST_solved':1,'practical_solved':1,'protocol_valid':1,'complete':1,'model_requests':0,'tool_executions':0,'official_revision':original['source_revision']}];receipts=[]
  for suffix in ('score','replay'):
   name='r546-a-'+suffix;receipt=folder/(name+'.receipt.json');stdout=folder/(name+'.stdout');lines(stdout,output)
   put(receipt,{'returncode':0,'properties':'Result=success','input_sha256':{str(folder/'RESPONSES.jsonl'):export.digest(folder/'RESPONSES.jsonl'),str(stage/'score_native.py'):export.digest(stage/'score_native.py')}})
   receipts.append({'receipt_path':str(receipt),'receipt_sha256':export.digest(receipt),'stdout_sha256':export.digest(stdout)})
  energy=counter_energy_bounds(telemetry,[row],[row['id']]);put(stage/'CAMPAIGN_PLAN.json',{'CPU_FIXTURE_ONLY':True});put(stage/'PREDECLARED_PLAN.json',{'CPU_FIXTURE_ONLY':True})
  audit={'experiment_id':'R546','measurement_valid':True,'GPU_execution_observed':True,'official_benchmark':False,'winner_qualified':False,'full_benchmark_score_claimed':False,'status':'PARTIAL','raw_root':str(raw),'campaign_plan_sha256':export.digest(stage/'CAMPAIGN_PLAN.json'),'predeclared_plan_sha256':export.digest(stage/'PREDECLARED_PLAN.json'),'original_raw_files_sha256':{str(p.name):export.digest(p) for p in raw.iterdir()},'decision':'PARTIAL_NO_PROMOTION_NO_RETRY','data_scope':'Synthetic CPU fixture.','task_phase_s':None,'comparison':{},'predeclared_gates':{},'scoring_receipts':receipts,'profiles':{'A':{'tasks':1,'solved':1,'practical_solved':1,'protocol_valid':1,'complete_final_answers':1,'GPU_counter':energy,'response_wall_s':1.0,'completion_tokens':1,'GPU_j_per_success_lower':1.0,'GPU_j_per_success_upper':1.0},'B':{'tasks':0,'solved':None}}}
  put(stage/'AUDIT.json',audit)
  return root,stage,raw,audit
 def project(self,root,stage,audit):
  (stage/'AUDIT.json').write_text(json.dumps(audit));entry={'audit_path':str(stage/'AUDIT.json'),'audit_sha256':export.digest(stage/'AUDIT.json')}
  return export.verified_native_tools_confirmation(root,entry,lambda *a:'audit-fixture')
 def test_partial_missing_arm_stays_unknown_and_not_official(self):
  with tempfile.TemporaryDirectory() as tmp:
   root,stage,raw,audit=self.fixture(tmp);result=self.project(root,stage,audit)
   self.assertEqual(result['arms'][0]['solved'],1);self.assertIsNone(result['arms'][1]['solved']);self.assertIsNone(result['shared_task_phase_s']);self.assertFalse(result['official_benchmark']);self.assertFalse(result['winner_qualified']);self.assertNotIn('PRIVATE_FIXTURE_TEXT',json.dumps(result))
 def test_forged_scores_energy_runtime_or_winner_are_rejected(self):
  for key in ('solved','energy','official','winner','complete'):
   with tempfile.TemporaryDirectory() as tmp:
    root,stage,raw,audit=self.fixture(tmp)
    if key=='solved':audit['profiles']['A']['solved']=2
    elif key=='energy':audit['profiles']['A']['GPU_j_per_success_lower']=0
    elif key=='official':audit['official_benchmark']=True
    elif key=='winner':audit['winner_qualified']=True
    else:audit['status']='FRESH_TOOLS_AB400_COMPLETE'
    with self.subTest(key=key),self.assertRaises(AssertionError):self.project(root,stage,audit)
 def test_changed_mapping_replay_or_original_revision_rejected(self):
  for key in ('mapping','replay','revision','worker'):
   with tempfile.TemporaryDirectory() as tmp:
    root,stage,raw,audit=self.fixture(tmp)
    if key=='mapping':
     path=stage/'A/RESPONSES.jsonl';path.write_text(path.read_text().replace('PRIVATE_FIXTURE_TEXT','ALTERED'))
    elif key=='replay':(stage/'A/r546-a-replay.stdout').write_text('{}\n')
    elif key=='revision':
     path=stage/'A/SCORING_PLAN.json';d=json.loads(path.read_text());d['source_revision']='other';path.write_text(json.dumps(d))
    else:(stage/'score_native.py').write_text('print("unreviewed")')
    with self.subTest(key=key),self.assertRaises((AssertionError,KeyError)):self.project(root,stage,audit)
if __name__=='__main__':unittest.main()
