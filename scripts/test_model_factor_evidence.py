import unittest
from model_factor_evidence import build, reviewed_dispositions, reviewed_hardware_dispositions, reviewed_architecture_exclusions
from render import cache_policy_matrix_evidence
class ModelFactorEvidence(unittest.TestCase):
 def test_exact_model_and_audit_required(self):
  factors=[{'id':'R22'},{'id':'K02'}];data=[{'id':'R1','model':'Gemma 4 12B','audit_id':'a','factor_ids':['R22']},{'id':'R2','model':'Qwen3.8','audit_id':'b','factor_ids':['R22']},{'id':'R3','model':'Qwen3.5','audit_id':None,'factor_ids':['R22']},{'id':'R4','model':'Gemma 4 / Nexus','audit_id':'c','factor_ids':['K02']},{'id':'R5','model':'Nexus','audit_id':'d','factor_ids':['K02']}];out=build(factors,data)
  self.assertEqual(out['R22']['Gemma 4'],['R1']);self.assertEqual(out['R22']['Qwen3.8'],['R2']);self.assertEqual(out['R22']['Qwen3.5'],[]);self.assertEqual(out['K02']['Gemma 4'],[]);self.assertEqual(out['K02']['Nexus'],['R5'])
 def test_reviewed_dispositions_require_matching_audits(self):
  with self.assertRaises(ValueError):reviewed_dispositions([])
 def test_gemma_key_cache_preserves_historical_control_limit(self):
  import copy,json
  from pathlib import Path
  experiments=json.loads((Path(__file__).resolve().parents[1]/'data/experiments.json').read_text())
  row=next(x for x in reviewed_dispositions(experiments) if x[0]=='K01' and x[1]=='Gemma 4')
  self.assertIn('151/164',row[-1]);self.assertIn('not an independent seed',row[-1])
  altered=copy.deepcopy(experiments);next(x for x in altered if x['id']=='R610')['aggregate_metrics']['comparison']['candidate_successes']=152
  with self.assertRaises(ValueError):reviewed_dispositions(altered)
 def test_mtp_history_never_promotes_failed_qwen_start(self):
  import copy,json
  from pathlib import Path
  experiments=json.loads((Path(__file__).resolve().parents[1]/'data/experiments.json').read_text());rows=reviewed_dispositions(experiments)
  self.assertEqual(next(r[2] for r in rows if r[0]=='S03' and r[3]=='R179'),'QUALIFIED')
  qwen=next(r for r in rows if r[0]=='S03' and r[3]=='R602');self.assertEqual(qwen[2],'PARTIAL');self.assertIn('no task-quality',qwen[-1])
  altered=copy.deepcopy(experiments);next(x for x in altered if x['id']=='R602')['aggregate_metrics']['actual_generation_requests']=1
  with self.assertRaises(ValueError):reviewed_dispositions(altered)
  candidate=next(r for r in rows if r[0]=='S03' and r[3]=='R542');self.assertEqual(candidate[2],'PARTIAL');self.assertIn('coding gate fell by three',candidate[-1])
  altered=copy.deepcopy(experiments);next(x for x in altered if x['id']=='R541')['aggregate_metrics']['quality']['net_success_change']=0
  with self.assertRaises(ValueError):reviewed_dispositions(altered)
 def test_hardware_exclusions_require_existing_audit_and_scope(self):
  factors=[{'id':x,'status':'NOT_APPLICABLE','evidence_ids':['audit-1']} for x in ('R16','HBM20','HBM21')]
  out=reviewed_hardware_dispositions(factors,[{'id':'audit-1'}])
  self.assertEqual(len(out),3)
  self.assertTrue(all(len(v['models'])==5 and not v['gpu_test'] and v['reopen'] for v in out.values()))
  with self.assertRaises(ValueError):reviewed_hardware_dispositions(factors,[])
  factors[0]['status']='PARTIAL'
  with self.assertRaises(ValueError):reviewed_hardware_dispositions(factors,[{'id':'audit-1'}])
 def test_architecture_exclusions_are_model_scoped_and_audit_bound(self):
  import json
  from pathlib import Path
  p=Path(__file__).resolve().parents[1]/'data';f=json.loads((p/'factors.json').read_text());a=json.loads((p/'audit-excerpts.json').read_text())
  result=reviewed_architecture_exclusions(f,a)
  self.assertEqual(result['BMT12']['models'],('OmniCoder',));self.assertNotIn('Gemma 4',result['HBM24']['models'])
  self.assertFalse(result['BMT12']['gpu_test']);self.assertTrue(result['BMT12']['reopen'])
  with self.assertRaises(ValueError):reviewed_architecture_exclusions(f,[])
 def test_cache_followup_requires_matching_tokens_and_policy(self):
  import copy, json
  from pathlib import Path
  repro=json.loads((Path(__file__).resolve().parents[1]/'data/snapshot.json').read_text())['reproducibility_review']
  rows=cache_policy_matrix_evidence(repro)
  self.assertEqual([x[1] for x in rows],['Nexus','OmniCoder'])
  self.assertTrue(all('0/2' in x[4] and 'selected case' in x[4] for x in rows))
  altered=copy.deepcopy(repro);altered['r641_policy_abba']['arms'][1]['policy_passes']=1
  with self.assertRaises(ValueError):cache_policy_matrix_evidence(altered)
  altered=copy.deepcopy(repro);altered['r642_policy_abba']['comparisons'][2]['turns'][2]['prompt_token_ids_equal']=False
  with self.assertRaises(ValueError):cache_policy_matrix_evidence(altered)
if __name__=='__main__':unittest.main()
