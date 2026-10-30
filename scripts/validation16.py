"""Public-safe aggregate projection for the frozen, non-official 8+8 validation."""
from pathlib import Path
import hashlib
import json

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())

PROFILES = {
    'R509': ('Qwen3.5-9B', 'R474'),
    'R510': ('Gemma4-12B', 'R472'),
    'R511': ('OmniCoder-9B', 'R478'),
    'R526': ('Nexus-9B · OFF/T0', 'R489'),
    'R527': ('Ornith-1.5-9B · OFF/T0', 'R496'),
    'R644': ('Qwen3.8-27B · IQ3_S · MTP3', 'R547'),
    'R645': ('Qwen3.8-27B · IQ3_S · MTP OFF', 'R502'),
}


def build(root):
    root = Path(root)
    rows = []
    for experiment, (model, parent) in PROFILES.items():
        folder = root / 'staging' / experiment.lower()
        audit_path = folder / 'AUDIT.json'
        review_path = folder / 'INDEPENDENT_REVIEW.json'
        capture_path = folder / 'CAPTURE_REVIEW.json'
        execution_path = folder / 'EXECUTION_REVIEW.json'
        audit, review, capture, execution = [load(p) for p in
            (audit_path, review_path, capture_path, execution_path)]
        audit_hash = digest(audit_path)
        assert audit['experiment_id'] == experiment
        assert audit['status'] == 'INDEPENDENT_VALIDATION16_COMPLETE'
        assert audit['measurement_valid'] is True and audit['GPU_execution_observed'] is True
        assert audit['official_benchmark'] is False and audit['winner_qualified'] is False
        assert audit['full_benchmark_score_claimed'] is False
        assert audit['completed_requests'] == audit['planned_requests'] == 16
        assert 0 <= audit['task_phase_s'] <= audit['task_limit_s'] <= 1200
        assert audit['timeouts'] == 0
        assert review['audit_sha256'] == audit_hash
        assert review['status'] == 'INDEPENDENT_CPU_REPLAY_IDENTICAL'
        assert review['replayed_requests'] == 16 and review['changed_judgments'] == []
        assert review['GPU_runs'] == review['model_requests'] == 0
        assert capture['GPU_execution_observed'] is True
        assert capture['all_replies_match_root_event_stream'] is True
        assert capture['full16_completed'] is True and capture['completed_requests'] == 16
        assert audit['capture_review_sha256'] == digest(capture_path)
        assert execution['scope_kind'] == 'FROZEN_EXISTING_MODEL_VALIDATION16'
        assert execution['status'] == 'APPROVED_FRESH_FULL_SUITE_SINGLE_SESSION'
        assert execution['parent_profile']

        categories = {}
        assert set(audit['groups']) == {'coding', 'tools'}
        for category in ('coding', 'tools'):
            m = audit['groups'][category]
            assert m['completed'] == 8 and 0 <= m['successes'] <= 8
            assert m['missing_tasks'] == 0 and len(m['task_ids']) == 8
            # Deliberately export aggregates only; never task identifiers or outputs.
            categories[category] = {
                'completed': 8,
                'successes': m['successes'],
                'final_text_present': m['final_text_present'],
                'valid_terminal_output': m['valid_terminal_output'],
                'completion_tokens': m['completion_tokens'],
                'completed_request_wall_s': m['completed_request_wall_s'],
                'tokens_per_second': m['tokens_s_completed_requests'],
                'successful_tasks_per_second': m['successful_tasks_s_completed_requests'],
                'gpu_j_per_success_lower': m['GPU_j_per_success_lower'],
                'gpu_j_per_success_upper': m['GPU_j_per_success_upper'],
                'wilson95_descriptive': m['wilson95'],
            }
            assert categories[category]['final_text_present'] <= 8
            assert categories[category]['valid_terminal_output'] <= 8
            assert all(isinstance(categories[category][k], (int, float)) for k in
                       ('completion_tokens', 'completed_request_wall_s', 'tokens_per_second',
                        'successful_tasks_per_second', 'gpu_j_per_success_lower',
                        'gpu_j_per_success_upper'))

        rows.append({
            'experiment_id': experiment,
            'model': model,
            'parent_experiment_id': parent,
            'parent_profile': execution['parent_profile'],
            'at_utc': audit['at_utc'],
            'status': 'COMPLETE_NON_OFFICIAL_VALIDATION',
            'tasks_per_category': 8,
            'task_phase_s': audit['task_phase_s'],
            'peak_device_vram_mib': audit['peak_device_vram_mib'],
            'coding': categories['coding'],
            'tools': categories['tools'],
            'audit_sha256': audit_hash,
            'independent_review_sha256': digest(review_path),
            'capture_review_sha256': digest(capture_path),
            'limitations': 'Fixed 8+8 task set; shared across profiles and exposed to researchers. Descriptive small-sample evidence only; not official, not a population ranking, not a Champion gate.',
        })
        if experiment in ('R644', 'R645'):
            tool_review = load(folder / 'TOOL_FAILURE_REVIEW.json')
            assert tool_review['status'] == 'CPU_SOURCE_CHECKED'
            assert tool_review['audit_sha256'] == audit_hash
            assert tool_review['raw_sha256'] == audit['original_raw_files_sha256']['HTTP_RESULTS.jsonl']
            cases = tool_review['observed']
            assert len(cases) == 8 - categories['tools']['successes']
            assert all(x['expected_calls'] == 0 and x['observed_calls'] == 1 and x['tools_executed'] is False for x in cases)
            rows[-1]['unexpected_tool_call_cases'] = len(cases)
        if experiment == 'R645':
            pair = load(folder / 'PAIRED_REVIEW.json')
            assert pair['status'] == 'UNBALANCED_EXPOSED_PAIRED_DIAGNOSTIC'
            assert pair['audit_sha256']['R645'] == audit_hash
            assert pair['audit_sha256']['R644'] == digest(root / 'staging/r644/AUDIT.json')
            assert pair['review_sha256']['R645'] == digest(review_path)
            assert pair['review_sha256']['R644'] == digest(root / 'staging/r644/INDEPENDENT_REVIEW.json')
            assert pair['identical_requests'] == 16 and pair['task_outcome_agreements'] == 16
            assert 0 <= pair['identical_output_token_sequences'] <= 16
            on_tool_review = load(root / 'staging/r644/TOOL_FAILURE_REVIEW.json')
            assert {x['task_id'] for x in cases} == {x['task_id'] for x in on_tool_review['observed']}
            token_review_path = folder / 'TOOL_TOKEN_REVIEW.json'
            token_review = load(token_review_path)
            assert token_review['status'] == 'CPU_SOURCE_CHECKED'
            assert token_review['pair_review_sha256'] == digest(folder / 'PAIRED_REVIEW.json')
            assert token_review['audits'] == pair['audit_sha256']
            assert token_review['matched_cases'] == token_review['same_output_tokens'] == token_review['same_tool_names_and_parsed_arguments'] == 8
            assert token_review['tool_choice'] == 'auto' and token_review['gpu_runs'] == 0
            assert len({x['task_id'] for x in token_review['cases']}) == 8
            assert all(x['identical_tokens'] is True and x['identical_tool_names_and_parsed_arguments'] is True for x in token_review['cases'])
            rows[-1]['paired_with_r644'] = {'identical_requests': 16,
                'identical_output_token_sequences': pair['identical_output_token_sequences'],
                'task_outcome_agreements': 16, 'review_sha256': digest(folder / 'PAIRED_REVIEW.json'),
                'tool_output_token_matches': 8, 'tool_token_review_sha256': digest(token_review_path)}
    assert len(rows) == len(PROFILES)
    return {'schema': 1, 'benchmark_id': 'frozen-jarvis-validation16-v1',
            'official_benchmark': False, 'purpose': 'SUPPLEMENTARY_PROFILE_VALIDATION_ONLY',
            'rows': rows}
