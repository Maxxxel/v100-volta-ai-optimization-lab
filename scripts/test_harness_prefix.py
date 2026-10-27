import copy
import unittest
from harness_prefix import analyze, identity, prefix_length


class PrefixTests(unittest.TestCase):
    def fixture(self):
        rows = []
        for name, case, tokens in [('a', 'private-A', [1, 2, 3]), ('b', 'private-A', [1, 2, 4, 5]), ('c', 'private-B', [1, 9])]:
            request = {'cache_prompt': False}
            rows.append({'kind': 'input_identity', 'id': name, 'source_case_id': case, 'arm': 'single', 'role': 'worker', 'prompt_token_ids': tokens, 'prompt_token_count': len(tokens), 'prompt_token_ids_sha256': identity(tokens), 'request_sha256': identity(request)})
            rows.append({'kind': 'agent_turn', 'id': name, 'request': request, 'request_sha256': identity(request), 'reply': {'usage': {'prompt_tokens': len(tokens)}}})
        return rows

    def test_exact_recurrence_never_becomes_a_savings_claim_or_private_payload(self):
        rows = self.fixture(); before = copy.deepcopy(rows); result = analyze(rows)
        self.assertEqual(rows, before)
        self.assertEqual(result['arms']['single'], {'requests': 3, 'input_tokens': 9, 'repeated_within_case_prefix_tokens_after_first': 2})
        self.assertEqual(result['cross_case_role_prefixes'][0]['common_prefix_tokens'], 1)
        self.assertIsNone(result['measured_speedup']); self.assertIsNone(result['measured_energy_saving'])
        self.assertNotIn('private-A', str(result)); self.assertNotIn('prompt_token_ids', str(result))

    def test_missing_duplicate_or_mutated_witness_rejected(self):
        for change in ('missing', 'duplicate', 'tokens', 'usage', 'cache'):
            with self.subTest(change=change):
                rows = self.fixture()
                if change == 'missing': rows.pop()
                if change == 'duplicate': rows.append(copy.deepcopy(rows[1]))
                if change == 'tokens': rows[0]['prompt_token_ids'][0] = 8
                if change == 'usage': rows[1]['reply']['usage']['prompt_tokens'] = 99
                if change == 'cache':
                    rows[1]['request']['cache_prompt'] = True
                    rows[1]['request_sha256'] = rows[0]['request_sha256'] = identity(rows[1]['request'])
                with self.assertRaises(ValueError): analyze(rows)

    def test_empty_singleton_and_shorter_prefix(self):
        self.assertEqual(prefix_length([]), 0)
        self.assertEqual(prefix_length([[1, 2]]), 2)
        self.assertEqual(prefix_length([[1, 2], [1]]), 1)
        self.assertEqual(prefix_length([[], [1]]), 0)
