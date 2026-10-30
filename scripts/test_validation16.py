import json
from pathlib import Path
import tempfile
import unittest

import validation16


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj))


def fixture(root):
    scores = {'R509': (8, 6), 'R510': (7, 7), 'R511': (8, 6), 'R526': (6, 5), 'R527': (7, 5), 'R644': (8, 5), 'R645': (8, 5)}
    for ident, (coding, tools) in scores.items():
        folder = Path(root) / 'staging' / ident.lower()
        capture = {'GPU_execution_observed': True, 'all_replies_match_root_event_stream': True,
                   'full16_completed': True, 'completed_requests': 16}
        dump(folder / 'CAPTURE_REVIEW.json', capture)
        groups = {}
        for key, successes in (('coding', coding), ('tools', tools)):
            groups[key] = {
                'completed': 8, 'successes': successes, 'final_text_present': 8,
                'valid_terminal_output': successes, 'length_stops': 0,
                'completion_tokens': 80, 'completed_request_wall_s': 2.0,
                'tokens_s_completed_requests': 40.0,
                'successful_tasks_s_completed_requests': successes / 2.0,
                'GPU_j_per_success_lower': 10.0, 'GPU_j_per_success_upper': 12.0,
                'wilson95': [0.2, 0.9], 'missing_tasks': 0, 'task_ids': [f'{key}-{i}' for i in range(8)],
            }
        audit = {'experiment_id': ident, 'at_utc': '2026-10-24T00:00:00Z',
                 'status': 'INDEPENDENT_VALIDATION16_COMPLETE', 'measurement_valid': True,
                 'GPU_execution_observed': True, 'official_benchmark': False,
                 'winner_qualified': False, 'full_benchmark_score_claimed': False,
                 'completed_requests': 16, 'planned_requests': 16, 'groups': groups,
                 'task_phase_s': 10, 'task_limit_s': 1200, 'peak_device_vram_mib': 7000,
                 'timeouts': 0, 'capture_review_sha256': validation16.digest(folder / 'CAPTURE_REVIEW.json')}
        if ident in ('R644', 'R645'):
            audit['original_raw_files_sha256'] = {'HTTP_RESULTS.jsonl': 'f' * 64}
        dump(folder / 'AUDIT.json', audit)
        review = {'audit_sha256': validation16.digest(folder / 'AUDIT.json'),
                  'status': 'INDEPENDENT_CPU_REPLAY_IDENTICAL', 'replayed_requests': 16,
                  'changed_judgments': [], 'GPU_runs': 0, 'model_requests': 0}
        dump(folder / 'INDEPENDENT_REVIEW.json', review)
        dump(folder / 'EXECUTION_REVIEW.json', {'scope_kind': 'FROZEN_EXISTING_MODEL_VALIDATION16',
              'status': 'APPROVED_FRESH_FULL_SUITE_SINGLE_SESSION', 'parent_profile': 'frozen-profile'})
        if ident in ('R644', 'R645'):
            dump(folder / 'TOOL_FAILURE_REVIEW.json', {'status': 'CPU_SOURCE_CHECKED',
                'audit_sha256': validation16.digest(folder / 'AUDIT.json'), 'raw_sha256': 'f' * 64,
                'observed': [{'task_id':str(i), 'expected_calls': 0, 'observed_calls': 1, 'tools_executed': False} for i in range(3)]})
        if ident == 'R645':
            other = Path(root) / 'staging/r644'
            dump(folder / 'PAIRED_REVIEW.json', {'status':'UNBALANCED_EXPOSED_PAIRED_DIAGNOSTIC',
                'audit_sha256': {'R644':validation16.digest(other / 'AUDIT.json'), 'R645':validation16.digest(folder / 'AUDIT.json')},
                'review_sha256': {'R644':validation16.digest(other / 'INDEPENDENT_REVIEW.json'), 'R645':validation16.digest(folder / 'INDEPENDENT_REVIEW.json')},
                'identical_requests':16, 'task_outcome_agreements':16, 'identical_output_token_sequences':14})
            dump(folder / 'TOOL_TOKEN_REVIEW.json', {'status':'CPU_SOURCE_CHECKED',
                'pair_review_sha256': validation16.digest(folder / 'PAIRED_REVIEW.json'),
                'audits': {'R644':validation16.digest(other / 'AUDIT.json'), 'R645':validation16.digest(folder / 'AUDIT.json')},
                'matched_cases':8, 'same_output_tokens':8, 'same_tool_names_and_parsed_arguments':8,
                'tool_choice':'auto', 'gpu_runs':0,
                'cases':[{'task_id':str(i), 'identical_tokens':True, 'identical_tool_names_and_parsed_arguments':True} for i in range(8)]})


class Validation16Projection(unittest.TestCase):
    def test_only_complete_cpu_replayed_aggregates_are_exported(self):
        with tempfile.TemporaryDirectory() as td:
            fixture(td)
            result = validation16.build(td)
        self.assertEqual([x['experiment_id'] for x in result['rows']],
                         ['R509', 'R510', 'R511', 'R526', 'R527', 'R644', 'R645'])
        self.assertFalse(result['official_benchmark'])
        self.assertEqual([(x['coding']['successes'], x['tools']['successes'])
                          for x in result['rows']], [(8, 6), (7, 7), (8, 6), (6, 5), (7, 5), (8, 5), (8, 5)])
        encoded = json.dumps(result)
        self.assertNotIn('coding-0', encoded)
        self.assertNotIn('tools-0', encoded)
        self.assertNotIn('task_ids', encoded)

    def test_modified_audit_is_rejected_by_independent_review_hash(self):
        with tempfile.TemporaryDirectory() as td:
            fixture(td)
            p = Path(td) / 'staging/r509/AUDIT.json'
            audit = json.loads(p.read_text())
            audit['groups']['coding']['successes'] -= 1
            p.write_text(json.dumps(audit))
            with self.assertRaises(AssertionError):
                validation16.build(td)

    def test_partial_capture_is_not_projected_as_complete(self):
        with tempfile.TemporaryDirectory() as td:
            fixture(td)
            folder = Path(td) / 'staging/r509'
            audit = json.loads((folder / 'AUDIT.json').read_text())
            audit['completed_requests'] = 15
            dump(folder / 'AUDIT.json', audit)
            review = json.loads((folder / 'INDEPENDENT_REVIEW.json').read_text())
            review['audit_sha256'] = validation16.digest(folder / 'AUDIT.json')
            dump(folder / 'INDEPENDENT_REVIEW.json', review)
            with self.assertRaises(AssertionError):
                validation16.build(td)

    def test_tool_failure_review_must_match_source_audit(self):
        with tempfile.TemporaryDirectory() as td:
            fixture(td)
            p = Path(td) / 'staging/r644/TOOL_FAILURE_REVIEW.json'
            review = json.loads(p.read_text())
            review['raw_sha256'] = '0' * 64
            dump(p, review)
            with self.assertRaises(AssertionError):
                validation16.build(td)


if __name__ == '__main__':
    unittest.main()
