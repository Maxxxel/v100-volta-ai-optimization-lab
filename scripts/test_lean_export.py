"""Lean-harness reporting preserves negative and missing evidence."""
import copy,json,pathlib,unittest
from render import lean_harness_report
from lean_metrics import measured_sum
class LeanReport(unittest.TestCase):
 def test_missing_measurement_is_not_zero(self):
  self.assertIsNone(measured_sum([3,None]));self.assertIsNone(measured_sum([]));self.assertEqual(measured_sum([0,3]),3)
 def test_negative_result_is_separate_and_all_costs_remain(self):
  es=json.loads((pathlib.Path(__file__).resolve().parents[1]/'data/experiments.json').read_text())
  lean=[e for e in es if e.get('aggregate_metrics',{}).get('native_lean_harness_ablation')]
  self.assertTrue(lean);before=copy.deepcopy(lean);page=lean_harness_report(lean)
  for phrase in ['28/33','25/33','301561','293897','rejected','NOT MEASURED','not official benchmarks','Failed tasks remain','No population-equivalence']:
   self.assertIn(phrase,page)
  self.assertEqual(lean,before)
 def test_qualification_cannot_be_smuggled_into_report(self):
  e={'aggregate_metrics':{'native_lean_harness_ablation':{'official_benchmark':True,'winner_qualified':False}}}
  with self.assertRaises(AssertionError):lean_harness_report([e])

class LeanProtocolIdentity(unittest.TestCase):
 def test_unknown_dataset_is_rejected_before_raw_projection(self):
  from unittest.mock import patch
  import export
  audit={'status':'LEAN_HARNESS_DEVELOPMENT66_COMPLETE','measurement_valid':True,'GPU_execution_observed':True,'dataset_id':'renamed-unknown-protocol'}
  with patch.object(export,'digest',return_value='a'*64),patch.object(export,'load',return_value=audit):
   with self.assertRaises(AssertionError):export.verified_native_lean_harness(pathlib.Path('/public-fixture'),{'audit_path':'/public-fixture/audit.json','audit_sha256':'a'*64},lambda *_:None)
 def test_development_gate_never_becomes_qualification_in_report(self):
  es=json.loads((pathlib.Path(__file__).resolve().parents[1]/'data/experiments.json').read_text())
  row=copy.deepcopy(next(e for e in es if e.get('aggregate_metrics',{}).get('native_lean_harness_ablation')))
  r=row['aggregate_metrics']['native_lean_harness_ablation'];r['dataset_id']='jarvis-lean-tool-json-ablation33-v1';r['comparison']['decision']='DEVELOPMENT_ONLY_REQUIRES_INDEPENDENT_CONFIRMATION'
  page=lean_harness_report([row]);self.assertIn('compact tool-result JSON',page);self.assertIn('no promotion',page);self.assertNotIn('Decision: rejected',page);self.assertIn('not official benchmarks',page)
 def test_arm_identity_is_not_silently_relabelled(self):
  from lean_metrics import reviews
  case={'kind':'agent_case','id':'compact-tool-json-v1--case','reported_result':{'all_tools_simulated':True,'production_tools_connected':False,'task_scope_pass':True}}
  with self.assertRaises(ValueError):reviews({'experiment_id':'CPU'},[case],'a'*64,[],lambda *_:None)
