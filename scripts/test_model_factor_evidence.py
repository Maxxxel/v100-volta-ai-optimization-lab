import unittest
from model_factor_evidence import build, reviewed_dispositions
class ModelFactorEvidence(unittest.TestCase):
 def test_exact_model_and_audit_required(self):
  factors=[{'id':'R22'},{'id':'K02'}];data=[{'id':'R1','model':'Gemma 4 12B','audit_id':'a','factor_ids':['R22']},{'id':'R2','model':'Qwen3.8','audit_id':'b','factor_ids':['R22']},{'id':'R3','model':'Qwen3.5','audit_id':None,'factor_ids':['R22']},{'id':'R4','model':'Gemma 4 / Nexus','audit_id':'c','factor_ids':['K02']},{'id':'R5','model':'Nexus','audit_id':'d','factor_ids':['K02']}];out=build(factors,data)
  self.assertEqual(out['R22']['Gemma 4'],['R1']);self.assertEqual(out['R22']['Qwen3.8'],['R2']);self.assertEqual(out['R22']['Qwen3.5'],[]);self.assertEqual(out['K02']['Gemma 4'],[]);self.assertEqual(out['K02']['Nexus'],['R5'])
 def test_reviewed_dispositions_require_matching_audits(self):
  with self.assertRaises(ValueError):reviewed_dispositions([])
if __name__=='__main__':unittest.main()
