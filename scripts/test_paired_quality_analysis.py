import json
import pathlib
import unittest

from render import render_paired_profile_quality


ROOT = pathlib.Path(__file__).resolve().parents[1]


class PairedProfileQualityTest(unittest.TestCase):
    def setUp(self):
        self.analysis = json.loads((ROOT / "data/paired-quality-analysis-2026-10-29.json").read_text())

    def test_only_matching_complete_protocols_and_all_profiles_are_rendered(self):
        page = render_paired_profile_quality(self.analysis)
        for name in ("OmniCoder", "Gemma4", "Nexus", "Qwen3.5", "Qwen3.8"):
            self.assertIn(name, page)
        self.assertIn("HumanEval+164", page)
        self.assertIn("BFCL parallel_multiple200", page)
        self.assertIn("whole native profiles", page)
        self.assertIn("does not change the R585 frozen roles", page)
        self.assertIn("assets/paired-quality-analysis-2026-10-29.json", page)

    def test_all_paired_outcomes_partition_the_exact_task_denominator(self):
        for family, total in (("HumanEval+", 164), ("BFCL_parallel_multiple", 200)):
            section = self.analysis[family]
            self.assertEqual(len(section["profiles"]), 5)
            self.assertEqual(len(section["pairwise"]), 10)
            for pair in section["pairwise"]:
                self.assertEqual(pair["N"], total)
                self.assertEqual(pair["A_only_pass"] + pair["B_only_pass"] + pair["both_pass"] + pair["both_fail"], total)

    def test_cpu_reanalysis_cannot_be_mislabeled_as_new_gpu_results(self):
        method = self.analysis["method"]
        self.assertTrue(method["cpu_only"])
        self.assertEqual(method["new_gpu_runs"], 0)
        self.assertEqual(method["new_model_requests"], 0)

    def test_renderer_rejects_incomplete_or_mixed_benchmark_pairs(self):
        changed = json.loads(json.dumps(self.analysis))
        changed["HumanEval+"]["pairwise"][0]["N"] = 163
        with self.assertRaises(AssertionError):
            render_paired_profile_quality(changed)


if __name__ == "__main__":
    unittest.main()
