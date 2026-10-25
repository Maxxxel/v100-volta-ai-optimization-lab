"""Public role projection gates; synthetic metadata, no private fixtures."""
import copy,unittest
from unittest.mock import patch
import export

class RolePublicGates(unittest.TestCase):
 def setUp(self):
  self.summary=dict(audit_path='/synthetic/staging/r999/AUDIT.json',audit_sha256='a'*64)
  self.audit=dict(status='DEVELOPMENT_ROLE_COMPARISON5_COMPLETE',measurement_valid=True,GPU_execution_observed=True,
                  dataset_id='jarvis-role-comparison-development5-v1',paired_unique_cases=5,tasks=15,case_executions=15,
                  official_benchmark=False,winner_qualified=False)
 def rejected(self,key,value):
  changed=copy.deepcopy(self.audit);changed[key]=value
  with patch.object(export,'digest',return_value='a'*64),patch.object(export,'load',return_value=changed):
   with self.assertRaises(AssertionError):export.verified_native_role_comparison('/synthetic',self.summary,lambda *args:None)
 def test_partial_not_a_complete_result(self):self.rejected('status','PARTIAL_TECHNICAL_REVIEW_REQUIRED')
 def test_fifteen_executions_not_independent_tasks(self):self.rejected('paired_unique_cases',15)
 def test_missing_GPU_evidence_not_a_local_model_result(self):self.rejected('GPU_execution_observed',False)
 def test_incomplete_capture_not_a_complete_result(self):self.rejected('case_executions',14)
 def test_not_an_official_benchmark(self):self.rejected('official_benchmark',True)
 def test_not_a_qualified_winner(self):self.rejected('winner_qualified',True)
 def test_wrong_protocol_rejected(self):self.rejected('dataset_id','official-agents')
 def test_changed_audit_hash_rejected_before_reading(self):
  with patch.object(export,'digest',return_value='b'*64),patch.object(export,'load',side_effect=AssertionError('must not read')) as read:
   with self.assertRaises(AssertionError):export.verified_native_role_comparison('/synthetic',self.summary,lambda *args:None)
   read.assert_not_called()
