"""Read-only exact-token recurrence analysis; no tokenizer, inference or tools."""
import argparse
import collections
import hashlib
import json
from pathlib import Path


def identity(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def prefix_length(sequences):
    if not sequences:
        return 0
    for index, values in enumerate(zip(*sequences)):
        if len(set(values)) != 1:
            return index
    return min(map(len, sequences))


def analyze(records):
    inputs = [r for r in records if r.get('kind') == 'input_identity']
    turns = [r for r in records if r.get('kind') == 'agent_turn']
    indexed = {r['id']: r for r in turns}
    if not inputs or len(indexed) != len(turns) or len({r['id'] for r in inputs}) != len(inputs) or set(indexed) != {r['id'] for r in inputs}:
        raise ValueError('Missing or duplicate input/response identities')
    groups = collections.defaultdict(list)
    for r in inputs:
        ids = r['prompt_token_ids']
        if not isinstance(ids, list) or any(type(t) is not int or t < 0 for t in ids) or len(ids) != r['prompt_token_count'] or identity(ids) != r['prompt_token_ids_sha256']:
            raise ValueError('Token identity/count mismatch')
        turn = indexed[r['id']]
        if identity(turn['request']) != r['request_sha256'] or turn['request_sha256'] != r['request_sha256'] or turn['reply']['usage']['prompt_tokens'] != len(ids):
            raise ValueError('Request/usage identity mismatch')
        if turn['request'].get('cache_prompt') is not False:
            raise ValueError('This retrospective requires explicitly uncached requests')
        if r['arm'] not in ('single', 'planner_worker', 'planner_worker_reviewer') or r['role'] not in ('planner', 'worker', 'reviewer'):
            raise ValueError('Unknown role/arm; private labels must not be exported')
        groups[(r['arm'], r['role'], r['source_case_id'])].append(ids)
    arms = {}
    roles = collections.defaultdict(list)
    for (arm, role, _), sequences in groups.items():
        entry = arms.setdefault(arm, {'requests': 0, 'input_tokens': 0, 'repeated_within_case_prefix_tokens_after_first': 0})
        entry['requests'] += len(sequences)
        entry['input_tokens'] += sum(map(len, sequences))
        entry['repeated_within_case_prefix_tokens_after_first'] += prefix_length(sequences) * (len(sequences) - 1)
        roles[(arm, role)].extend(sequences)
    cross_case = [{'arm': arm, 'role': role, 'requests': len(sequences), 'common_prefix_tokens': prefix_length(sequences)} for (arm, role), sequences in sorted(roles.items())]
    return {'arms': arms, 'cross_case_role_prefixes': cross_case, 'requests': len(inputs),
            'GPU_runs': 0, 'model_requests': 0, 'measured_speedup': None, 'measured_energy_saving': None,
            'scope': 'Exact repeated token-ID prefixes, including task/history content; not isolated system/tool preamble tokens. No tokens removed, cache replay, model execution or causal savings measured. Same-case prefixes do not imply safe state reuse across roles or tasks.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--sha256', required=True)
    args = parser.parse_args()
    if args.input.stat().st_size > 64 * 1024 * 1024:
        raise ValueError('Input exceeds bounded retrospective size')
    raw = args.input.read_bytes()
    if hashlib.sha256(raw).hexdigest() != args.sha256:
        raise ValueError('Original archive hash mismatch')
    result = analyze([json.loads(line) for line in raw.splitlines() if line.strip()])
    result['source_HTTP_sha256'] = args.sha256
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
