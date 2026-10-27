import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("caveman_shape_study.py")
SPEC = importlib.util.spec_from_file_location("caveman_shape_study", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class CavemanShapeStudyTests(unittest.TestCase):
    def test_fixtures_are_deterministic_safe_and_cover_scopes(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            first = module.make_fixtures(Path(a))
            second = module.make_fixtures(Path(b))
            summary = lambda root, rows: [(r["id"], r["scope"], r["input_bytes"], r["input_sha256"])
                                          for r in rows]
            self.assertEqual(summary(a, first), summary(b, second))
            self.assertEqual(len(first), 23)
            cave = [r for r in first if r["scope"] == "CaveBench-inspired"]
            self.assertEqual(len(cave), 6)
            self.assertTrue(all(60_000 <= r["input_bytes"] <= 95_000 for r in cave))
            self.assertEqual(len([r for r in first if r["scope"] == "CaveBench-inspired-size-sweep"]), 12)
            self.assertEqual(len([r for r in first if r["scope"] == "Jarvis-shaped"]), 4)
            noop = next(r for r in first if r["scope"] == "negative-control")
            self.assertTrue(noop["expected_passthrough"])
            for root in (Path(a), Path(b)):
                for path in root.iterdir():
                    if path.is_file():
                        content = path.read_bytes()
                        self.assertNotIn(b"192.168.", content)
                        self.assertNotIn(b"/opt/v100", content)


if __name__ == "__main__":
    unittest.main()
