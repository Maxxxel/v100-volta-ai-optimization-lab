"""Strict public aggregate projection of local pipeline receipts. No process control."""
import datetime
import math
import re

DURATIONS = ('startup_total_s', 'task_phase_s', 'warmup_requests_s', 'completed_request_s',
             'CPU_unit_execution_sum_s', 'CPU_scoring_outer_wall_s', 'preparation_s',
             'broker_admission_s', 'model_load_only_s', 'security_integrity_s', 'GPU_busy_s', 'cloud_wait_s')
RESOURCES = ('peak_vram_mib', 'integral_gpu_j', 'counter_lower_j', 'counter_upper_j')


def number(value):
    if type(value) in (int, float) and math.isfinite(value) and value >= 0:
        return value
    return None


def timestamp(value):
    try:
        parsed = datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))
        return parsed.astimezone(datetime.timezone.utc).isoformat() if parsed.tzinfo else None
    except (ValueError, AttributeError):
        return None


def project(source):
    assert source.get('schema') == 1 and source.get('GPU_jobs_started_by_this_report') == 0
    records = []
    for entry in source['experiments']:
        ident = entry['experiment_id']
        assert re.fullmatch(r'R[1-9][0-9]{1,3}', ident)
        assert re.fullmatch('[a-f0-9]{64}', entry['source_audit_sha256'])
        q = entry['quality']
        failed = entry.get('result_status') == 'FAILED' and q['completed'] == 0 and q['solved'] is None
        if failed:
            assert type(q['completed']) is int and type(q['planned']) is int and q['planned'] > 0
        else:
            assert all(type(q[k]) is int for k in ('completed', 'planned', 'solved'))
            assert 0 <= q['solved'] <= q['completed'] <= q['planned']
        record = {'experiment_id': ident, 'audit_sha256': entry['source_audit_sha256'],
                  'status': 'FAILED' if failed else 'COMPLETE' if q['completed'] == q['planned'] else 'PARTIAL',
                  'quality': {k: q[k] for k in ('completed', 'planned', 'solved')},
                  'durations': {k: number(entry['durations'].get(k)) for k in DURATIONS},
                  'resources': {k: number(entry['resources'].get(k)) for k in RESOURCES},
                  'timestamps': {k: timestamp(entry['timestamps'].get(k)) for k in
                                 ('initial_at_utc', 'task_begin_at_utc', 'task_end_at_utc', 'audit_at_utc')},
                  'CI_build_s': number(entry['publication'].get('CI_build_s')),
                  'CI_deploy_s': number(entry['publication'].get('CI_deploy_s'))}
        records.append(record)
    phases = []
    for event in source.get('CPU_pipeline_events', []):
        if event.get('event') != 'END':
            continue
        if event.get('phase') not in ('collect', 'independent_review', 'integrity', 'export', 'render',
                                      'tests', 'security', 'build', 'commit', 'push', 'deployment_check'):
            continue
        assert re.fullmatch(r'R[1-9][0-9]{1,3}', event['experiment_id'])
        phases.append({'experiment_id': event['experiment_id'], 'phase': event['phase'],
                       'at_utc': timestamp(event.get('at_utc')), 'duration_s': number(event.get('duration_s')),
                       'status': 'COMPLETE' if event.get('status') == 'COMPLETE' else 'FAILED'})
    current = source.get('current', {})
    ident = current.get('experiment_id')
    assert ident is None or re.fullmatch(r'R[1-9][0-9]{1,3}', ident)
    allowed_phases = {'NOT MEASURED', 'GPU_CONTROL_ACTIVE', 'NO_ACTIVE_GPU_CONTROL_OBSERVED', 'AUDITED_RESULT_AVAILABLE'}
    assert current.get('phase', 'NOT MEASURED') in allowed_phases
    lock = source.get('diagnosis', {}).get('interactive_publication_lock', {})
    lock_result = {'start_at_utc': timestamp(lock.get('start_at_utc')),
                   'release_at_utc': timestamp(lock.get('release_at_utc')),
                   'observed_hold_window_s': number(lock.get('observed_hold_window_s'))}
    for key in ('start_evidence_sha256', 'release_evidence_sha256'):
        value = lock.get(key)
        lock_result[key] = value if isinstance(value, str) and re.fullmatch('[a-f0-9]{64}', value) else None
    return {'schema': 1, 'observed_at_utc': timestamp(source.get('observed_at_utc')),
            'current': {'experiment_id': ident, 'phase': current.get('phase', 'NOT MEASURED')},
            'experiments': records, 'CPU_phases': phases,
            'verified_capacity_events': number(source.get('cloud', {}).get('verified_capacity_events')),
            'capacity_only_wait_s': None, 'waiting_admitted_experiments': None,
            'publication_lock_observation': lock_result}


def render(data):
    def cell(v):
        return 'NOT MEASURED' if v is None else str(round(v, 3)) if isinstance(v, float) else str(v)
    text = '# Pipeline Performance\n\n'
    text += '**Verified snapshot: ' + cell(data['observed_at_utc']) + '. This static page is not a live monitor.**\n\n'
    text += 'Last observed: ' + cell(data['current']['experiment_id']) + ' · ' + data['current']['phase'] + '.\n\n'
    text += '| Experiment | Status | Tasks completed / planned | Startup s | Task s | CPU unit s | CI build / deploy s |\n'
    text += '|---|---|---|---|---|---|---|\n'
    for e in reversed(data['experiments']):
        q, d = e['quality'], e['durations']
        row = ['['+e['experiment_id']+'](experiments/'+e['experiment_id']+'.md)', e['status'],
               str(q['completed'])+'/'+str(q['planned']), cell(d['startup_total_s']), cell(d['task_phase_s']),
               cell(d['CPU_unit_execution_sum_s']), cell(e['CI_build_s'])+' / '+cell(e['CI_deploy_s'])]
        text += '| ' + ' | '.join(row) + ' |\n'
    text += '\nStartup includes admission, loading and warm-up. CPU unit sums can include failed diagnostics; they are not total overhead. '
    text += 'CI may overlap later experiments. Missing task-end receipts remain unknown, including R538. '
    text += 'Between-experiment gaps are not measured GPU idle time or cloud downtime.\n\n'
    lock = data['publication_lock_observation']
    if lock['observed_hold_window_s'] is not None:
        text += '**Confirmed publication blocker:** an interactive process held the publication lock for '+cell(lock['observed_hold_window_s'])+' seconds. '
        text += 'The lock was released. This blocked publication, not an already running GPU job. Uncommitted documentation was an additional gate. '
        text += 'Publication locks must remain scoped to one bounded process.\n\n'
    text += 'Automation reuses the existing collector and publication timer: isolated CPU scoring/replay, hash checks, export, tests, commit and push. '
    text += 'Publication failures cannot start or repeat GPU jobs. Push retries and deployment checks are bounded. '
    text += 'New GPU work still requires its reviewed broker contract.\n\n'
    text += '<details><summary>Measured CPU publication phases</summary>\n\n| Experiment | Phase | Status | Seconds |\n|---|---|---|---|\n'
    for e in data['CPU_phases']:
        text += '| ' + ' | '.join([e['experiment_id'], e['phase'], e['status'], cell(e['duration_s'])]) + ' |\n'
    text += '\n</details>\n\nOnly recorded phase windows are shown. Unknown preparation, broker-wait and cloud-wait durations are not estimated. '
    text += 'Pending admission is not inferred from a queue entry. [Methodology](methodology.md) · [Research archive](archive.md).\n'
    return text
