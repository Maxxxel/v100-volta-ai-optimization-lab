import copy,inspect,json,pathlib,tempfile,unittest,hashlib
import leaderboard as l
class CounterView(unittest.TestCase):
 def fixture(self,root,solved=150):
  stage=root/'staging/r999';stage.mkdir(parents=True);raw=stage/'raw';raw.mkdir();ids=['HumanEval/'+str(i) for i in range(164)]
  records=[{'id':x,'kind':'coding','start_ns':10+2*i,'end_ns':11+2*i} for i,x in enumerate(ids)]
  telemetry=[{'at_ns':v+1,'nvml_begin_ns':v,'gpu_energy_counter_mj':j} for v,j in [(0,0),(200,100000),(400,200000)]]
  for name,rows in [('HTTP_RESULTS.jsonl',records),('GPU_TELEMETRY.jsonl',telemetry)]: (raw/name).write_text(''.join(json.dumps(x)+'\n' for x in rows))
  ap=stage/'AUDIT.json';ap.write_text(json.dumps({'experiment_id':'R999','collected_tasks':164,'parts':[{'audit_path':str(raw/'AUDIT.json'),'task_ids':ids}]}))
  measurement=l.counter_energy_bounds(telemetry,records,ids);measurement.update(solved=solved,j_per_success_lower=measurement['lower_j']/solved,j_per_success_upper=measurement['upper_j']/solved)
  p=stage/'ENERGY.json';p.write_text(json.dumps({'status':'BOUNDED_REPORTED_HARDWARE_COUNTER_ENERGY','GPU_runs':0,'model_requests':0,'source_API':'nvmlDeviceGetTotalEnergyConsumption','counter_unit':'mJ','selected_task_ids':ids,'source_function_sha256':hashlib.sha256(inspect.getsource(l.counter_energy_bounds).encode()).hexdigest(),'source_files_sha256':{str(f):l.digest(f) for f in [ap,raw/'HTTP_RESULTS.jsonl',raw/'GPU_TELEMETRY.jsonl']},'measurement':measurement}))
  return {'experiment_id':'R999','audit_hash':l.digest(ap),'solved':149},{'solved':150,'audit_ids':['original']},{'energy_counter_review':{'path':str(p.relative_to(root)),'sha256':l.digest(p)}}
 def test_official_success_denominator_without_mutating_original(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);original,result,review=self.fixture(root);before=copy.deepcopy(original);out=l.scoring_view_counter(root,original,result,review,lambda p,h:'counter-audit');self.assertEqual(original,before);self.assertEqual(out['counter_energy']['solved'],150);self.assertAlmostEqual(out['counter_energy']['j_per_success_upper'],200/150);self.assertNotIn('counter_energy',result)
 def test_preliminary_denominator_cannot_be_reused(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);a,b,c=self.fixture(root,149)
   with self.assertRaises(ValueError):l.scoring_view_counter(root,a,b,c,lambda p,h:'counter-audit')
 def test_bad_receipt_rejected(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);a,b,c=self.fixture(root);c['energy_counter_review']['sha256']='0'*64
   with self.assertRaises(ValueError):l.scoring_view_counter(root,a,b,c,lambda p,h:'counter-audit')
 def test_existing_views_without_supplement_unchanged(self):
  value={'solved':128,'audit_ids':[]};self.assertIs(l.scoring_view_counter('/missing',{},value,{},None),value)
if __name__=='__main__':unittest.main()
