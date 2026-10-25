import copy
import json
import unittest
from unittest.mock import patch
import export
import pipeline


class TimingProjection(unittest.TestCase):
    def fixture(self):
        return {'schema': 1, 'GPU_jobs_started_by_this_report': 0,
                'observed_at_utc': '2026-10-25T20:00:00Z',
                'private_log': 'DO_NOT_PUBLISH',
                'current': {'experiment_id': 'R539', 'phase': 'AUDITED_RESULT_AVAILABLE', 'pid': 123},
                'experiments': [{'experiment_id': 'R538', 'source_audit_sha256': 'a'*64,
                                 'quality': {'completed': 199, 'planned': 200, 'solved': 167},
                                 'durations': {'task_phase_s': None, 'startup_total_s': 157.9, 'private': 'DO_NOT_PUBLISH'},
                                 'resources': {}, 'timestamps': {}, 'publication': {}, '_clock': {'private': 123}}]}

    def test_partial_and_missing_end_never_become_complete_or_zero(self):
        result = pipeline.project(self.fixture())
        row = result['experiments'][0]
        self.assertEqual(row['status'], 'PARTIAL')
        self.assertIsNone(row['durations']['task_phase_s'])
        self.assertEqual(row['quality']['completed'], 199)
        page = pipeline.render(result)
        self.assertIn('199/200', page)
        self.assertIn('NOT MEASURED', page)
        self.assertIn('not a live monitor', page)
        self.assertIn('not measured GPU idle time', page)

    def test_positive_allowlist_drops_private_extras(self):
        result = json.dumps(pipeline.project(self.fixture()))
        for word in ('DO_NOT_PUBLISH', '_clock', 'private_log', 'pid'):
            self.assertNotIn(word, result)

    def test_invalid_counts_and_untrusted_identity_fail_closed(self):
        for key, value in [('experiment_id', '../R1'), ('source_audit_sha256', 'bad')]:
            data = self.fixture(); data['experiments'][0][key] = value
            with self.assertRaises(AssertionError): pipeline.project(data)
        data = self.fixture(); data['experiments'][0]['quality']['solved'] = 200
        with self.assertRaises(AssertionError): pipeline.project(data)

    def test_no_arbitrary_strings_nonfinite_or_negative_measurements(self):
        for value in ('6035', -1, float('nan'), float('inf'), True):
            self.assertIsNone(pipeline.number(value))
        self.assertEqual(pipeline.number(0), 0)
        data = self.fixture(); data['current']['phase'] = 'DO_NOT_PUBLISH'
        with self.assertRaises(AssertionError): pipeline.project(data)

    def test_cpu_phases_drop_command_arguments_and_error_bodies(self):
        data = self.fixture(); data['CPU_pipeline_events'] = [
            {'experiment_id': 'R539', 'phase': 'export', 'event': 'END', 'status': 'FAILED',
             'duration_s': 1.25, 'command': 'DO_NOT_PUBLISH', 'error': 'DO_NOT_PUBLISH'},
            {'experiment_id': 'R539', 'phase': 'start_gpu', 'event': 'END', 'duration_s': 1}]
        result = pipeline.project(data)
        self.assertEqual(len(result['CPU_phases']), 1)
        self.assertEqual(result['CPU_phases'][0]['duration_s'], 1.25)
        self.assertNotIn('DO_NOT_PUBLISH', json.dumps(result))


class MtpProjection(unittest.TestCase):
    def test_changed_review_hash_rejected_before_load(self):
        with patch.object(export, 'digest', return_value='b'*64), patch.object(export, 'load') as load:
            with self.assertRaises(AssertionError):
                export.mtp_development_result('/synthetic', {'path': '/synthetic/review.json', 'sha256': 'a'*64}, lambda *a: None)
            load.assert_not_called()

    def test_incompatible_scope_or_qualified_claim_rejected(self):
        review = {'experiment_id': 'R539', 'baseline_experiment_id': 'R515',
                  'status': 'PROMISING_REQUIRES_FRESH_CONFIRMATION', 'single_MTP_treatment_verified': True,
                  'winner_qualified': False, 'official_benchmark': False, 'GPU_runs_in_review': 0}
        for key, value in [('winner_qualified', True), ('official_benchmark', True),
                           ('single_MTP_treatment_verified', False), ('baseline_experiment_id', 'R487')]:
            changed = copy.deepcopy(review); changed[key] = value
            with patch.object(export, 'digest', return_value='a'*64), patch.object(export, 'load', return_value=changed):
                with self.assertRaises(AssertionError):
                    export.mtp_development_result('/synthetic', {'path': '/synthetic/review.json', 'sha256': 'a'*64}, lambda *a: None)


if __name__ == '__main__': unittest.main()
