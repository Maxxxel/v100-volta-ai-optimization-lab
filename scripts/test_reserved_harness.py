"""CPU-only synthetic fixtures; never exported as model measurements."""
import copy,json,pathlib,unittest
from export import metrics,reserved_validation_work
from render import reserved_harness_report
class ReservedMetrics(unittest.TestCase):
 def test_usage_counts_failures_and_preserves_unmeasured_reasoning(self):
  records=[{'kind':'agent_turn','reply':{'usage':{'prompt_tokens':10,'completion_tokens':3}}},{'kind':'agent_turn','reply':{'usage':{'prompt_tokens':20,'completion_tokens':4}}},{'kind':'agent_case','reported_result':{'task_success':False,'policy_violations':1,'rejected_calls':1,'total_tool_calls':2}}];before=copy.deepcopy(records);r=reserved_validation_work(records)['measured_work'];self.assertEqual(r['input_output_tokens'],37);self.assertEqual(r['completed_model_calls'],2);self.assertEqual(r['policy_violations'],1);self.assertIsNone(r['reasoning_tokens']);self.assertEqual(records,before)
 def test_missing_is_not_zero(self):
  r=reserved_validation_work([{'kind':'agent_turn','reply':{}},{'kind':'agent_case','reported_result':{}}])['measured_work']
  for k in ('input_tokens','output_tokens','reasoning_tokens','input_output_tokens','policy_violations','tool_calls'):self.assertIsNone(r[k])
 def test_separate_namespace_not_official_or_old_validation(self):
  r=metrics(dict(status='LEAN_RESERVED_VALIDATION33_COMPLETE',dataset_id='jarvis-lean-holdout-20261027-v1',planned_tasks=33,tasks=33,solved=1,official_benchmark=False,winner_qualified=False,full_benchmark_score_claimed=False,measurement_valid=True))
  self.assertIn('native_lean_reserved_validation33',r);self.assertNotIn('native_validation33',r);self.assertNotIn('native_agent18_development',r);self.assertFalse(r['native_lean_reserved_validation33']['official_benchmark'])
 def test_wrong_dataset_cannot_claim_reserved_complete(self):
  with self.assertRaises(AssertionError):metrics(dict(status='LEAN_RESERVED_VALIDATION33_COMPLETE',dataset_id='unregistered',planned_tasks=33))
class ReservedRender(unittest.TestCase):
 def fixture(self):
  r=dict(dataset_id='jarvis-lean-holdout-20261027-v1',official_benchmark=False,winner_qualified=False,solved=1,tasks=33,planned_tasks=33,policy_gate_passes=32,measured_work=dict(input_tokens=123,output_tokens=456,completed_model_calls=10),case_wall_s=12,gpu_j_per_success_lower=1,gpu_j_per_success_upper=2,peak_device_vram_mib=3,technical_preflight_cases=1,technical_request_errors=0,context_tokens=8192,max_output_tokens=4096,model_sha256='a'*64,profile_sha256='b'*64,parent_profile_sha256='c'*64,scorer_sha256='d'*64,implementation=dict(engine_binary_sha256='e'*64,template_sha256='f'*64))
  return dict(id='CPU_FIXTURE',model='Synthetic fixture',aggregate_metrics={'native_lean_reserved_validation33':r})
 def test_reserved_results_are_separate_honest_and_not_a_winner(self):
  row=self.fixture();before=copy.deepcopy(row);s=reserved_harness_report([row]);self.assertIn('1/33',s);self.assertIn('correlated authored families',s);self.assertIn('Not an official leaderboard',s);self.assertIn('preflight failures',s);self.assertIn('NOT RECORDED',s);self.assertEqual(row,before)
 def test_missing_tokens_do_not_render_as_zero_or_none(self):
  row=self.fixture();row['aggregate_metrics']['native_lean_reserved_validation33']['measured_work']['input_tokens']=None;s=reserved_harness_report([row]);self.assertIn('NOT MEASURED / 456',s);self.assertNotIn('None',s)
 def test_cannot_promote_to_official_via_renderer(self):
  row=self.fixture();row['aggregate_metrics']['native_lean_reserved_validation33']['official_benchmark']=True
  with self.assertRaises(AssertionError):reserved_harness_report([row])

class PublishedReservedEvidence(unittest.TestCase):
 def source(self):
  root=pathlib.Path(__file__).resolve().parents[1];es=json.loads((root/'data/experiments.json').read_text());snapshot=json.loads((root/'data/snapshot.json').read_text());return root,es,snapshot
 def test_three_frozen_profile_captures_keep_gemma_preflight_limit(self):
  _,es,_=self.source();rows={e['id']:e['aggregate_metrics']['native_lean_reserved_validation33'] for e in es if e.get('aggregate_metrics',{}).get('native_lean_reserved_validation33')}
  self.assertTrue({'R589','R590','R591'} <= set(rows));self.assertTrue(all(r['context_tokens']==8192 and r['max_output_tokens']==4096 and not r['official_benchmark'] and not r['winner_qualified'] for r in rows.values()));self.assertTrue(rows['R589']['complete_inference']);self.assertTrue(rows['R590']['complete_inference']);self.assertTrue(rows['R591']['complete_capture']);self.assertFalse(rows['R591']['complete_inference']);self.assertEqual(len(rows['R591']['preflight_limits']),2)
  for e in rows['R591']['preflight_limits']:self.assertGreater(e['prompt_tokens']+e['max_output_tokens'],e['context_tokens'])
 def test_new_research_cannot_enter_official_benchmark_history(self):
  root,_,_=self.source();history=json.loads((root/'data/configuration-history.json').read_text());self.assertFalse(any(r['experiment_id'] in ('R589','R590','R591','R618') for r in history['runs']))
 def test_frozen_reference_links_exact_audited_profiles_and_keeps_limits(self):
  _,es,snapshot=self.source();ref=snapshot['lean_harness_review']['frozen_reference'];self.assertEqual(len(ref['profiles']),3);self.assertEqual(ref['budgets']['TASK_total_seconds'],1200);self.assertEqual(ref['budgets']['max_VRAM_mib'],14336)
  for p in ref['profiles']:
   row=next(e for e in es if e['id']==p['experiment_id'])['aggregate_metrics']['native_lean_reserved_validation33'];self.assertEqual(row['profile_sha256'],p['captured_profile_sha256']);self.assertEqual(row['model_sha256'],p['model_sha256']);self.assertFalse(p['optimized_harness_qualified'])
  self.assertIn('now exposed',ref['next_goal_boundary'])

if __name__=='__main__':unittest.main()
