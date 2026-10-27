import unittest
from lean_metrics import original_toon_overhead
class OriginalToonCosts(unittest.TestCase):
 def test_parent_and_child_CPU_are_separate_and_no_inferred_energy(self):
  v=original_toon_overhead([{'kind':'agent_case','harness_rewrite_receipts':[{'tool_results':[{'codec_wall_ns':10**9,'codec_parent_cpu_ns':10**7,'codec_children_cpu_ns':5*10**8}]}]}])
  self.assertEqual(v['codec_wall_s'],1);self.assertEqual(v['codec_parent_CPU_s'],.01);self.assertEqual(v['codec_children_CPU_s'],.5);self.assertIsNone(v['host_CPU_energy_j'])
 def test_missing_subprocess_measurement_is_unknown(self):
  v=original_toon_overhead([{'kind':'agent_case','harness_rewrite_receipts':[{'tool_results':[{}]}]}]);self.assertIsNone(v['codec_children_CPU_s']);self.assertIsNone(v['codec_wall_s'])
 def test_empty_capture_and_other_events_do_not_become_zero_cost(self):
  v=original_toon_overhead([{'kind':'agent_turn','harness_rewrite_receipts':[{'tool_results':[{}]}]}]);self.assertEqual(v['request_transforms'],0);self.assertIsNone(v['codec_parent_CPU_s'])
if __name__=='__main__':unittest.main()
