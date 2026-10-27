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
