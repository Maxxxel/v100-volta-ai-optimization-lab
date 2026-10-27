"""Public role projection gates; synthetic metadata, no private fixtures."""
import copy,unittest
from unittest.mock import patch
import export

class FinalCandidateReview(unittest.TestCase):
 def inputs(self):
  import json,pathlib
  p=pathlib.Path(__file__).resolve().parents[1]/'data'
  return [json.loads((p/n).read_text()) for n in ('screening.json','configuration-history.json','experiments.json')]
 def test_every_inventory_profile_and_exact_qualified_run_remains_visible(self):
  from render import final_qualification_review
  s,h,e=self.inputs();before=copy.deepcopy((s,h,e));page=final_qualification_review(s,h,e)
  for row in s['rows']:self.assertIn(row['model'],page);self.assertIn(row['configuration']['model_sha256'][:12],page)
  for run in h['runs']:
   if run.get('official_eligible') and run['benchmark_id'] in {'humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200'}:
    self.assertIn(run['runtime_configuration_id'],page);self.assertIn(run['experiment_id'],page)
  self.assertEqual((s,h,e),before)
 def test_new_unknown_candidate_requires_explicit_review(self):
  from render import final_qualification_review
  s,h,e=self.inputs();s['rows'][0]['experiment_id']='R999'
  with self.assertRaises(ValueError):final_qualification_review(s,h,e)
 def test_no_profile_transfer_or_implicit_new_GPU_authority(self):
  from render import final_qualification_review
  page=final_qualification_review(*self.inputs())
  for phrase in ['Top-3 selection pending','coding150/164 is a separate build','16K is a different context profile','startup extension is not authorized','not Terminal-Bench','separately admitted harness experiments']:
   self.assertIn(phrase,page)

class FrozenBaselineGates(unittest.TestCase):
 def inputs(self):
  import json,pathlib
  p=pathlib.Path(__file__).resolve().parents[1]/'data'
  return [json.loads((p/n).read_text()) for n in ('configuration-history.json','benchmark-register.json','experiments.json')]
 def test_three_concrete_nonexecuting_packets_preserve_profile_and_capture_identity(self):
  from leaderboard import freeze_final_baselines,validate_final_baselines
  h,r,e=self.inputs();before=copy.deepcopy(h);f=freeze_final_baselines(h,r,e,'2026-10-27T00:00:00+00:00');validate_final_baselines(f,h)
  self.assertEqual(len(f['selected']),3);self.assertEqual(h,before);self.assertEqual(f['new_GPU_runs'],0)
  for s in f['selected']:
   self.assertFalse(s['production_approved']);self.assertEqual(len(s['benchmark_captures']),2);self.assertFalse(s['baseline_packet']['export_grants_execution_authority'])
  gemma=next(s for s in f['selected'] if s['selection_id']=='coding-specialist');self.assertIsNone(gemma['authored_agent_context']['result']);self.assertEqual(gemma['authored_agent_context']['status'],'NOT MEASURED_AT_SELECTED_8K_CONTEXT')
 def test_capture_mismatch_fails_closed(self):
  from leaderboard import freeze_final_baselines
  h,r,e=self.inputs();run=next(v for v in h['runs'] if v['experiment_id']=='R489' and v['official_eligible']);p=next(v for v in h['profiles'] if v['runtime_configuration_id']==run['runtime_configuration_id']);p['runtime']['context']='16384'
  with self.assertRaises(ValueError):freeze_final_baselines(h,r,e,'2026-10-27T00:00:00+00:00')
 def test_freeze_survives_new_unrelated_history_but_rejects_changed_evidence(self):
  from leaderboard import freeze_final_baselines,validate_final_baselines
  h,r,e=self.inputs();f=freeze_final_baselines(h,r,e,'2026-10-27T00:00:00+00:00');h['unrelated_future_metadata']='append only';self.assertTrue(validate_final_baselines(f,h))
  first=f['selected'][0]['benchmark_captures'][0]['run_ids'][0];next(v for v in h['runs'] if v['run_id']==first)['solved']-=1
  with self.assertRaises(ValueError):validate_final_baselines(f,h)
 def test_tampered_packet_is_rejected(self):
  from leaderboard import freeze_final_baselines,validate_final_baselines
  h,r,e=self.inputs();f=freeze_final_baselines(h,r,e,'2026-10-27T00:00:00+00:00');f['selected'][0]['baseline_packet']['profile']['runtime']['sampling']['temperature']=1
  with self.assertRaises(ValueError):validate_final_baselines(f,h)
 def test_rendered_selection_keeps_agent_context_and_nonselection_limits(self):
  from leaderboard import freeze_final_baselines
  from render import render_final_selection
  h,r,e=self.inputs();f=freeze_final_baselines(h,r,e,'2026-10-27T00:00:00+00:00');page=render_final_selection(f,h)
  for text in ['85.35% ·2/3','86.06% ·2/3','84.13% ·2/3','NOT MEASURED at selected8K','Nexus','Qwen3.5','Nemotron','gpt-oss','cold-switch overhead','Issue18','frozen-baselines.json']:
   self.assertIn(text,page)

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
