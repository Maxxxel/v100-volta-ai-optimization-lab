import unittest
from model_factor_evidence import build, reviewed_dispositions
from render import cache_policy_matrix_evidence
class ModelFactorEvidence(unittest.TestCase):
 def test_exact_model_and_audit_required(self):
  factors=[{'id':'R22'},{'id':'K02'}];data=[{'id':'R1','model':'Gemma 4 12B','audit_id':'a','factor_ids':['R22']},{'id':'R2','model':'Qwen3.8','audit_id':'b','factor_ids':['R22']},{'id':'R3','model':'Qwen3.5','audit_id':None,'factor_ids':['R22']},{'id':'R4','model':'Gemma 4 / Nexus','audit_id':'c','factor_ids':['K02']},{'id':'R5','model':'Nexus','audit_id':'d','factor_ids':['K02']}];out=build(factors,data)
  self.assertEqual(out['R22']['Gemma 4'],['R1']);self.assertEqual(out['R22']['Qwen3.8'],['R2']);self.assertEqual(out['R22']['Qwen3.5'],[]);self.assertEqual(out['K02']['Gemma 4'],[]);self.assertEqual(out['K02']['Nexus'],['R5'])
 def test_reviewed_dispositions_require_matching_audits(self):
  with self.assertRaises(ValueError):reviewed_dispositions([])
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
