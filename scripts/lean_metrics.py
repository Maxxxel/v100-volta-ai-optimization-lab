"""Postprocess one paired capture. No inference, admission or score repair."""
import math

ARMS=('reference','compact-system-v1')

def measured_sum(values):
    values=list(values)
    return sum(values) if values and all(type(v) in (int,float) and math.isfinite(v) and v>=0 for v in values) else None

def reviews(audit,records,audit_sha,telemetry,counter_bounds,arms=ARMS):
    cases=[r for r in records if r['kind']=='agent_case']
    turns=[r for r in records if r['kind']=='agent_turn']
    errors=[r for r in records if r['kind']=='agent_error']
    identities=[r for r in records if r['kind']=='input_identity']
    parsed={arm:[] for arm in arms}
    for case in cases:
        arm,source_id=case['id'].split('--',1)
        if arm not in parsed or any(x['source_id']==source_id for x in parsed[arm]):raise ValueError('Unknown/repeated paired case')
        result=case['reported_result']
        if result.get('all_tools_simulated') is not True or result.get('production_tools_connected') is not False or result.get('task_scope_pass') is not True:raise ValueError('Simulation boundary failed')
        parsed[arm].append({'source_id':source_id,'case':case})
    reports=[]
    for arm in arms:
        selected=parsed[arm];ids={x['case']['id'] for x in selected}
        belongs=lambda r:any(r['id'].startswith(i+'--turn') for i in ids)
        responses=[r for r in turns if belongs(r)];failed=[r for r in errors if belongs(r)]
        token_ids=[r for r in identities if r['case_id'] in ids]
        solved=sum(x['case']['reported_result']['task_success'] for x in selected)
        policy=sum(x['case']['reported_result']['policy_gate_pass'] for x in selected)
        wall=measured_sum(x['case']['e2e_s'] for x in selected)
        # Pass ALL intervals so unselected/interleaved arms break energy groups.
        energy=counter_bounds(telemetry,cases,[x['case']['id'] for x in selected]) if selected else None
        usage=[r['reply'].get('usage',{}) for r in responses]
        prompt=measured_sum(u.get('prompt_tokens') for u in usage)
        completion=measured_sum(u.get('completion_tokens') for u in usage)
        reasoning=measured_sum(u.get('completion_tokens_details',{}).get('reasoning_tokens') for u in usage)
        attempted_prompt=measured_sum(r['prompt_token_count'] for r in token_ids)
        total=prompt+completion if not failed and prompt is not None and completion is not None else None
        transform=[r for x in selected for r in x['case'].get('harness_rewrite_receipts',[])]
        cpu=measured_sum(r.get('transform_cpu_ns') for r in transform)
        overhead=measured_sum(r.get('transform_wall_ns') for r in transform)
        response_wall=measured_sum(r['e2e_s'] for r in responses)
        memory=[v['device_vram_bytes']/2**20 for v in telemetry if any(x['case']['start_ns']<=v['at_ns']<=x['case']['end_ns'] for x in selected)]
        report={'arm':arm,'completed_cases':len(selected),'planned_cases':33,'complete':len(selected)==33,
                'solved':solved,'policy_gate_passes':policy,'case_wall_s':wall,
                'response_wall_s':response_wall,
                'completion_tokens_per_response_second':completion/response_wall if completion is not None and response_wall else None,
                'model_calls_attempted':len(responses)+len(failed),'request_errors':len(failed),
                'input_tokens_attempted':attempted_prompt,'input_tokens_reported':prompt,
                'completion_tokens_reported':completion,'reasoning_tokens_reported':reasoning,
                'total_tokens_reported':total,'transform_cpu_s':cpu/1e9 if cpu is not None else None,
                'transform_wall_s':overhead/1e9 if overhead is not None else None,
                'tool_calls':measured_sum(x['case']['reported_result'].get('total_tool_calls') for x in selected),
                'policy_violations':measured_sum(x['case']['reported_result'].get('policy_violations') for x in selected),
                'rejected_calls':measured_sum(x['case']['reported_result'].get('rejected_calls') for x in selected),
                'invalid_actions':measured_sum(x['case']['reported_result'].get('invalid_actions') for x in selected),
                'peak_sampled_device_vram_mib':max(memory) if memory else None,
                'GPU_counter':energy,'GPU_j_per_success_lower':energy['lower_j']/solved if energy and solved else None,
                'GPU_j_per_success_upper':energy['upper_j']/solved if energy and solved else None,
                'successful_tasks_per_s':solved/wall if len(selected)==33 and wall else None}
        reports.append(report)
    quality={'experiment_id':audit['experiment_id'],'source_audit_sha256':audit_sha,
             'GPU_runs':0,'model_requests':0,'official_benchmark':False,'winner_qualified':False,
             'paired_unique_cases':33,'case_executions':len(cases),'arms':reports,
             'scope':'Exposed authored33 cases/11 correlated families, alternating AB/BA. Reasoning tokens are not inferred; completion tokens include reasoning when the API does. Transformation CPU and wall time include audit/preservation work. Failed tasks remain in cost numerators. Not a new model benchmark or population equivalence test.'}
    comparison={'experiment_id':audit['experiment_id'],'candidate_audit_sha256':audit_sha,
                'official_benchmark':False,'winner_qualified':False,'GPU_runs':0,'model_requests':0,
                'comparable':all(r['complete'] for r in reports),'decision':'INCOMPLETE_NO_PROMOTION'}
    if len(arms)==1:
        quality.update(paired_unique_cases=0,source_unique_cases=33,scope='B-only33 exposed development cases. Stored original-request control is a separate historical measurement, not a fresh paired run or official benchmark. Failed tasks remain in costs; no population equivalence or adoption.')
        comparison.update(comparable=False,decision='SCREEN_REQUIRES_VERIFIED_STORED_REFERENCE')
        return quality,comparison
    if comparison['comparable']:
        left,right=parsed[arms[0]],parsed[arms[1]]
        if [r['source_id'] for r in left]!=[r['source_id'] for r in right]:raise ValueError('Paired task order differs')
        before,after=reports
        comparison.update(paired_gained=sum(not a['case']['reported_result']['task_success'] and b['case']['reported_result']['task_success'] for a,b in zip(left,right)),
                          paired_lost=sum(a['case']['reported_result']['task_success'] and not b['case']['reported_result']['task_success'] for a,b in zip(left,right)),
                          new_policy_failure_cases=sum(a['case']['reported_result']['policy_gate_pass'] and not b['case']['reported_result']['policy_gate_pass'] for a,b in zip(left,right)))
        def reduction(old,new):return 100*(1-new/old) if old and new is not None else None
        comparison['token_reduction_percent']=reduction(before['total_tokens_reported'],after['total_tokens_reported'])
        comparison['latency_reduction_percent']=reduction(before['case_wall_s'],after['case_wall_s'])
        comparison['conservative_energy_per_success_reduction_percent']=reduction(before['GPU_j_per_success_lower'],after['GPU_j_per_success_upper'])
        safety=before['policy_violations'] is not None and after['policy_violations'] is not None and after['policy_violations']<=before['policy_violations'] and comparison['new_policy_failure_cases']==0
        comparison['observed_quality_and_policy_gate']=after['solved']>=before['solved'] and safety
        comparison['decision']='DEVELOPMENT_ONLY_REQUIRES_INDEPENDENT_CONFIRMATION' if comparison['observed_quality_and_policy_gate'] else 'REJECT_OBSERVED_QUALITY_OR_POLICY_REGRESSION'
    return quality,comparison

def screen_reviews(audit,records,audit_sha,telemetry,counter_bounds,reference_quality,reference_records,reference_audit_sha,reference_quality_sha):
    """Pure case-matched screen; caller verifies immutable reference provenance."""
    arm='preaction-checklist-v1'
    quality,comparison=reviews(audit,records,audit_sha,telemetry,counter_bounds,arms=(arm,))
    assert reference_quality['experiment_id']=='R587' and reference_quality['source_audit_sha256']==reference_audit_sha
    assert reference_quality['official_benchmark'] is reference_quality['winner_qualified'] is False
    baseline=next(r for r in reference_quality['arms'] if r['arm']=='reference')
    before=[r for r in reference_records if r['kind']=='agent_case' and r['id'].startswith('reference--')]
    after=[r for r in records if r['kind']=='agent_case']
    assert baseline['complete'] and len(before)==33 and len({r['id'] for r in before})==33
    assert sum(r['reported_result']['task_success'] for r in before)==baseline['solved']
    assert sum(r['reported_result']['policy_gate_pass'] for r in before)==baseline['policy_gate_passes']
    assert sum(r['e2e_s'] for r in before)==baseline['case_wall_s']
    source=lambda r:r['id'].split('--',1)[1]
    assert [source(r) for r in after]==[source(r) for r in before[:len(after)]]
    comparison.update(reference_experiment_id='R587',reference_arm='reference',reference_audit_sha256=reference_audit_sha,reference_quality_sha256=reference_quality_sha,fresh_contemporaneous_control=False,paired_GPU_execution=False,comparable=quality['arms'][0]['complete'],decision='INCOMPLETE_SCREEN_NO_PROMOTION')
    if not comparison['comparable']:return quality,comparison
    candidate=quality['arms'][0]
    comparison.update(case_matched=33,paired_gained=sum(not a['reported_result']['task_success'] and b['reported_result']['task_success'] for a,b in zip(before,after)),paired_lost=sum(a['reported_result']['task_success'] and not b['reported_result']['task_success'] for a,b in zip(before,after)),new_policy_failure_cases=sum(a['reported_result']['policy_gate_pass'] and not b['reported_result']['policy_gate_pass'] for a,b in zip(before,after)))
    def reduction(old,new):return 100*(1-new/old) if old and new is not None else None
    comparison.update(token_reduction_percent=reduction(baseline['total_tokens_reported'],candidate['total_tokens_reported']),latency_reduction_percent=reduction(baseline['case_wall_s'],candidate['case_wall_s']),conservative_energy_per_success_reduction_percent=reduction(baseline['GPU_j_per_success_lower'],candidate['GPU_j_per_success_upper']))
    gate=candidate['solved']>=baseline['solved'] and candidate['policy_violations'] is not None and candidate['policy_violations']<=baseline['policy_violations'] and comparison['new_policy_failure_cases']==0
    comparison['observed_quality_and_policy_gate']=gate
    comparison['decision']='SCREEN_ONLY_REQUIRES_FRESH_CONTROL_AND_HOLDOUT' if gate else 'REJECT_OBSERVED_QUALITY_OR_POLICY_REGRESSION'
    comparison['scope']='Historical-control screening deltas only; no causal speedup, equivalence, Champion or production adoption. Missing metrics stay unknown.'
    return quality,comparison
