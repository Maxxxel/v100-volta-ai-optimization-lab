"""Scientific and confidentiality controls using public metadata, never weights."""
import copy, json, pathlib, unittest
from derivatives import projection

ROOT = pathlib.Path(__file__).resolve().parents[1]


class DerivativeResearchTests(unittest.TestCase):
    def fixture(self):
        register = json.loads((ROOT / 'data/benchmark-register.json').read_text())
        a = copy.deepcopy(register['candidate_research'][0])
        history = json.loads((ROOT / 'data/configuration-history.json').read_text())
        hashes = {x['kind']: x['sha256'] for x in a['evidence']}
        a.update(CPU_audit_sha256=hashes['CPU_audit'])
        cpu = {'status': 'COMPLETE_BOUNDED_CPU_PROBES', 'execution_uid': 65534,
               'new_GPU_runs': 0, 'model_execution': False, 'full_model_downloads': 0,
               'controls': a['cpu_controls'], 'results': a['cpu_results'],
               'range_receipts': a['cpu_range_receipts'], 'headers': {}}
        for h in a['cpu_structure']:
            cpu['headers'][h['repository']] = [{'parameters': h['parameters'], 'dtype_counts': h['dtype_counts'],
                                               'header_sha256': h['header_sha256'][0],
                                               'tensors': {str(i): {} for i in range(h['tensor_count'])}}]
        gguf = {'new_GPU_runs': 0, 'model_execution': False, 'full_model_downloads': 0, 'results': []}
        for h in a['gguf_headers']:
            tensors = {}
            for name, count in h['type_counts'].items():
                for i in range(count):
                    tensors[name + str(i)] = {'type_name': name}
            gguf['results'].append({'repository': h['repository'], 'revision': h['revision'],
                                   'file': {'rfilename': h['filename'], 'size': h['published_bytes'], 'lfs': {'sha256': h['published_sha256']}},
                                   'header_sha256': h['header_sha256'], 'header': {
                                       'gguf_version': h['gguf_version'], 'tensor_count': h['tensor_count'],
                                       'type_counts': h['type_counts'], 'tensors': tensors, 'metadata': {
                                           'general.architecture': h['architecture'], 'qwen35.block_count': h['layers'],
                                           'qwen35.context_length': h['declared_context_tokens']}}})
        plans = {'profiles': a['proposed_profiles'], 'specialist_plan': a['specialist_plan']}
        replay = copy.deepcopy(a['independent_replay']); replay['new_GPU_runs'] = 0
        return a, cpu, replay, gguf, plans, history

    def test_inventory_is_not_new_models_or_local_benchmark_coverage(self):
        result = projection(*self.fixture())
        self.assertEqual(len(result['candidates']), 105)
        self.assertEqual(len(result['proposed_profiles']), 3)
        self.assertEqual(result['new_GPU_runs'], 0)
        self.assertTrue(all(not c['local_gpu_qualified'] and c['local_quality'] == 'NOT MEASURED' for c in result['candidates']))
        self.assertTrue(all(not c['official_ranking_eligible'] for c in result['publisher_claims']))
        self.assertEqual(len(result['requested_six']), 6)

    def test_projection_never_exports_raw_weights_code_templates_or_unknown_fields(self):
        args = self.fixture(); a, cpu, _, _, plans, _ = args
        a['candidates'][0]['source_code'] = 'DO_NOT_EXPORT'
        a['candidates'][0]['artifacts'][0]['raw_weights'] = 'DO_NOT_EXPORT'
        cpu['results'][0]['pairs'][0]['sample_values'] = 'DO_NOT_EXPORT'
        a['candidates'][0]['tokenizer_chat_template'] = 'DO_NOT_EXPORT'
        a['publisher_claims'][0]['settings']['private_prompt'] = 'DO_NOT_EXPORT'
        plans['profiles'][0]['engine']['private_path'] = 'DO_NOT_EXPORT'
        self.assertNotIn('DO_NOT_EXPORT', json.dumps(projection(*args)))

    def test_incomplete_or_privileged_cpu_evidence_is_rejected(self):
        for mode in ('root', 'GPU', 'model', 'control', 'partial-replay', 'wrong-audit', 'whole-census', 'quality-claim'):
            args = self.fixture(); a, cpu, replay, _, _, _ = args
            if mode == 'root': cpu['execution_uid'] = 0
            elif mode == 'GPU': a['new_GPU_runs'] = 1
            elif mode == 'model': cpu['model_execution'] = True
            elif mode == 'control': cpu['controls']['BF16_known_values'] = False
            elif mode == 'partial-replay': replay['raw_fragment_hashes_verified'] -= 1
            elif mode == 'wrong-audit': replay['source_audit_sha256'] = '0' * 64
            elif mode == 'whole-census': cpu['results'][0]['full_tensor_census'] = True
            else: cpu['results'][0]['training_or_quality_improvement_proven'] = True
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                projection(*args)

    def test_proposals_cannot_become_measured_results_or_reset_the_budget(self):
        for mode in ('allow-GPU', 'score', 'budget', 'artifact', 'gui', 'published-official', 'duplicate'):
            args = self.fixture(); a, _, _, _, plans, _ = args
            if mode == 'allow-GPU': plans['profiles'][0]['new_GPU_execution_authorized'] = True
            elif mode == 'score': plans['profiles'][0]['metrics']['success'] = 90
            elif mode == 'budget': plans['profiles'][0]['whole_benchmark_wall_budget_s'] = 901
            elif mode == 'artifact': plans['profiles'][0]['model_sha256'] = '0' * 64
            elif mode == 'gui': plans['specialist_plan']['GPU_allowed'] = True
            elif mode == 'published-official': a['publisher_claims'][0]['official_ranking_eligible'] = True
            else: a['candidates'].append(copy.deepcopy(a['candidates'][0]))
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                projection(*args)

    def test_historical_reference_binding_cannot_change_scores_or_configurations(self):
        for key in ('score_percent', 'audit_hash', 'runtime_configuration_id'):
            args = self.fixture(); args[0]['references'][0][key] = 'changed'
            with self.subTest(key=key), self.assertRaises(ValueError):
                projection(*args)


if __name__ == '__main__':
    unittest.main()
