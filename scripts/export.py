#!/usr/bin/env python3
"""Publish-schema projection. Reads canonical metadata and explicitly allowlisted reviewed source-reproduction assets; never copies arbitrary files or logs.
No source code execution, downloads, GPU requests, or source mutations.
"""
import argparse, collections, copy, fcntl, hashlib, html, json, math, pathlib, re, sys
from urllib.parse import urlsplit, urlunsplit
HERE = pathlib.Path(__file__).resolve().parents[1]
STATUS = {'QUALIFIED','TESTED_NEGATIVE','PARTIAL','OPEN','DEFERRED','NOT_APPLICABLE'}
DOMAINS = {'github.com','raw.githubusercontent.com','huggingface.co','arxiv.org','doi.org','docs.nvidia.com','developer.nvidia.com','nvidia.com','wiki.archlinux.org','precipice.tech','reddit.com','www.reddit.com','ollama.com','docs.ollama.com','evalplus.github.io','gorilla.cs.berkeley.edu','squidfunk.github.io','docs.github.com'}
DENY = re.compile(r'(?i)(?:\b(?:(?:pve|proxmox)-[a-z0-9-]+|localhost)\b|(?:/opt/|/root/|/home/|/run/|/var/)[^\s,;\]\)"\']*|\b(?:10|127)\.\d+\.\d+\.\d+\b|\b192\.168\.\d+\.\d+\b|\b172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+\b|\bGPU-[a-f0-9-]{16,}|\b(?:sensor|switch|light|climate|automation|person|device_tracker|input_boolean)\.[a-z0-9_]+|\b[a-z0-9-]+\.(?:local|lan|internal)\b)')
SECRET = re.compile(r'(?i)(?:gh[pousr]_[a-z0-9]{12,}|github_pat_[a-z0-9_]{12,}|sk-[a-z0-9]{16,}|-----BEGIN .*PRIVATE KEY-----|(?:password|passwd|api[_-]?key|access[_-]?token|authorization)\s*[:=]\s*[^\s,;]{8,})')
SAFEKEY = re.compile(r'^[A-Za-z0-9_+().% -]{1,100}$')
# Only aggregate scientific branches; never raw responses, cases, per-task outputs or prompts.
METRIC_ROOTS = {'native_metrics','context_tokens','slots','actual_KV_unified','models','comparisons','metrics','comparison','delta','long_metrics','quality','original12','quality_original12','original12_nonregression','peak_process_vram_mib','peak_device_vram_mib','memory_saved_mib','numerical','numerical_reference','numerical_failures','numerical_tests','model_starts','requests','actual_generation_requests','actual_GPU_execution','new_GPU_runs','old_native_model_starts_verified','primary_archives_checked','observations','unique_quality_tasks','quality_losses','format_passes','semantic_passes','tasks','solved','total_wall_s','wall_s','gpu_j_per_success','gpu_energy_j','stability','A','B','arms','reference','candidate','full_standard164','custom_long_context16','scopes','score_rule','model_comparison_progress'}
METRIC_ROOTS |= {'factors_reviewed','original_variant_cells','existing_unique_evidence_files_SHA_verified','new_model_starts','scientific_status_changes','experimental_factor_coverage_changes'}
METRIC_ROOTS |= {'model_results_admitted','canonical_positive_controls_verified','negative_controls_verified','new_control_runs'}
METRIC_ROOTS |= {'prefill_geomean_E2E_change_percent','actual_private_cublas126'}
DOMAINS.add('pypi.org')
DOMAINS.update({'gist.github.com','images.nvidia.com'})
METRIC_ROOTS |= {'object_size_change_percent','decoded_cubin_byte_identity','decoded_PTX_byte_identity','explicit_NVCCflag_applied','original_inputs_preserved'}
METRIC_ROOTS |= {'baseline','binary','reference_only_calibration','actual_reference_GPU_inference','actual_candidate_GPU_execution','candidate_model_starts','source_cases','authorized_cases','denied_cases','baseline_primary_dispatch_events','candidate_primary_dispatch_events','before_commit_process_crash_controls','after_commit_process_crash_controls','authority_revocation_controls','malformed_envelope_controls','separate_session_controls','denied_deliveries','component_wall_s'}
# Explicit numeric aggregate fields for speculation memory/task-cost screens.
METRIC_ROOTS |= {'prefix_envelopes_same','actual_history_requests','critical_matches_previous_valid','critical_matches_previous_bad','critical_prompt_tokens','critical_output_tokens','concurrent_generation_requests','other_slot_erased','actual_managed_allocator','CT_memory_observed','decode_e2e_reduction_percent_vs_A0','actual_ngram_draft','memory_saved_vs_R244_device_mib','memory_saved_vs_R245_device_mib','successful_task_wall_s','successful_task_cost_change_percent_vs_R245','gpu_energy_j_approx','observed_tasks','full18_score_claimed','model_requests','actual_ngram_proposals_observed','timing_confirmation_needed','fixed_parameters'}
METRIC_ROOTS |= {'observed_original_QA_cases','original12_full_score_claimed','diagnostic_semantic_passes','diagnostic_format_passes','new_QA_cases','reused_QA_cases','unique_QA_cases','quality_wall_s','quality_gpu_energy_j','gpu_j_per_semantic_success','semantic_successes_per_s','actual_full_GPU_offload','actual_sampler_control_passed'}
BLOCK_KEYS = re.compile(r'(?i)(?:prompt|response|answer|output|content|messages|transcript|token_ids|per_task|per_case|samples|observations|input|argv|environment|paths?|commands?|logs?|error|trace|qkv|tensor|activation|workload|case_id|tools|entities|sequence|proposals|findings|password|credential|secret|authorization|entity|address|port_number|pin$)')
TEXT_KEYS = {'decision','qualification','interpretation','limits','limitations','hypothesis','research_question','scope','timing_note','score_rule','reference','note','unit','aggregation','metric_aggregation','primary','outlier_rule','kind','role','cache','quantization','engine_build','cuda_toolkit','context','batch','ubatch','threads','n_gpu_layers','temperature','seed','type_k','type_v','mtp','model','model_id','status','measurement_type','evidence_class','screen_passed','winner_qualified'}
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path): return json.loads(path.read_text())
def text(value, limit=3500):
    if not isinstance(value,str): return None
    if SECRET.search(value): raise ValueError('Secret-like value rejected in selected research field')
    value=DENY.sub('[REDACTED]',value)
    return value[:limit] + (' [abridged]' if len(value)>limit else '')
def url(value):
    if not isinstance(value,str): return None
    try: u=urlsplit(value)
    except ValueError: return None
    if u.scheme!='https' or u.hostname not in DOMAINS or u.username or u.password: return None
    return urlunsplit(('https',u.netloc,u.path,'',''))
def urls(obj):
    found=set()
    if isinstance(obj,str):
        for x in re.findall(r'https://[^\s<>"\]\)]+',obj):
            u=url(x)
            if u: found.add(u)
    elif isinstance(obj,dict):
        for k,v in obj.items():
            if k not in {'evidence','per_task','identity','accountability','original_variant_inventory'}: found.update(urls(v))
    elif isinstance(obj,list):
        for x in obj: found.update(urls(x))
    return sorted(found)
def projection(obj, depth=0):
    """Whitelist numeric/boolean aggregate leaves; only named public metadata strings."""
    if depth>9: return None
    if obj is None or isinstance(obj,bool): return obj
    if isinstance(obj,(int,float)):
        return obj if not isinstance(obj,float) or math.isfinite(obj) else None
    if isinstance(obj,list):
        # No numeric dumps or sampled time-series. Short lists of aggregate dicts only.
        if len(obj)>24: return None
        values=[projection(x,depth+1) for x in obj if isinstance(x,dict)]
        return [x for x in values if x] or None
    if isinstance(obj,dict):
        result={}
        for k,v in obj.items():
            if not SAFEKEY.fullmatch(k) or BLOCK_KEYS.search(k): continue
            if isinstance(v,str):
                if k in TEXT_KEYS: result[k]=text(v)
                elif k.endswith('sha256') and re.fullmatch('[a-f0-9]{64}',v): result[k]=v
            else:
                clean=projection(v,depth+1)
                if clean is not None: result[k]=clean
        return result or None
    return None
def agent_policy_counts(cases):
    # Called only after independently replayed33-case captures and hashes pass.
    assert len(cases)==33
    fields=('policy_gate_pass','task_scope_pass')
    assert all(type(c.get('reported_result',{}).get(k)) is bool for c in cases for k in fields)
    return {'policy_gate_passes':sum(c['reported_result']['policy_gate_pass'] for c in cases),
            'task_scope_passes':sum(c['reported_result']['task_scope_pass'] for c in cases)}

def agent_quality_diagnostics(cases):
    """Aggregate replayed judgments only; never publish traces or tool arguments.

    Case counts and event counts have different denominators. Missing event or
    parser observations stay unknown, rather than becoming an observed zero.
    """
    assert len(cases)==33
    results=[c['reported_result'] for c in cases]
    assert all(isinstance(r.get('failure_reasons'),list) and all(isinstance(x,str) for x in r['failure_reasons']) for r in results)
    reasons=[set(r['failure_reasons']) for r in results]
    out={k+'_cases':sum(k in row for row in reasons) for k in
         ('missing_valid_final','invalid_final_contract','wrong_final_status','wrong_reason_code','incorrect_facts')}
    out['final_contract_failure_cases']=sum(bool(row&{'missing_valid_final','invalid_final_contract'}) for row in reasons)
    for source,prefix in [('policy_violations','policy_violation'),('rejected_calls','rejected_tool_call'),('invalid_actions','invalid_action')]:
        counts=[r.get(source) for r in results]
        known=all(type(n) is int and n>=0 for n in counts)
        out[prefix+'_events']=sum(counts) if known else None
        out[prefix+'_cases']=sum(n>0 for n in counts) if known else None
    rounds=[r.get('round_metrics') for r in results]
    known=all(isinstance(rows,list) and rows and all(type(x.get('parse_failed')) is bool for x in rows) for rows in rounds)
    out['parse_failed_rounds']=sum(x['parse_failed'] for rows in rounds for x in rows) if known else None
    out['parse_failed_cases']=sum(any(x['parse_failed'] for x in rows) for rows in rounds) if known else None
    out['evidence_or_postcondition_failure_cases']=sum(any(x.startswith(('required_evidence_missing:','evidence_order_failed:')) or x in ('postcondition_failed','effect_incomplete','private_behavior_failed') for x in row) for row in reasons)
    out['scope']='Replayed local33 simulated cases; categories overlap. Cases are not events, parser success is not semantic correctness, and blocked proposals are not executed production actions.'
    return out

def metrics(obj):
    result={k:projection(v) for k,v in obj.items() if k in METRIC_ROOTS and projection(v) is not None}
    reserved=obj.get('dataset_id')=='jarvis-lean-holdout-20261027-v1' and obj.get('planned_tasks')==33
    validation33=(obj.get('dataset_id')=='jarvis-agent-validation-20261025-v1' or reserved) and obj.get('planned_tasks')==33
    if obj.get('status') in ('VALIDATION33_COMPLETE','LEAN_RESERVED_VALIDATION33_COMPLETE') and ('planned_tasks' in obj or 'dataset_id' in obj):assert validation33
    agent_count=33 if validation33 else 18
    if obj.get('status') in ('DEVELOPMENT_AGENT18_COMPLETE','VALIDATION33_COMPLETE','LEAN_RESERVED_VALIDATION33_COMPLETE','PARTIAL_TECHNICAL_REVIEW_REQUIRED') and obj.get('planned_tasks')==agent_count:
        assert obj.get('official_benchmark') is False and obj.get('winner_qualified') is False and obj.get('full_benchmark_score_claimed') is False
        assert type(obj.get('tasks')) is int and type(obj.get('solved')) is int and 0<=obj['solved']<=obj['tasks']<=agent_count and obj.get('planned_tasks')==agent_count
        if obj['status'] in ('DEVELOPMENT_AGENT18_COMPLETE','VALIDATION33_COMPLETE','LEAN_RESERVED_VALIDATION33_COMPLETE'):assert obj['tasks']==agent_count and obj.get('measurement_valid') is True
        keys=('tasks','solved','planned_tasks','model_starts','actual_generation_requests','technical_request_errors','technical_preflight_cases','completion_tokens','completed_request_wall_s','case_wall_s','task_phase_s','task_limit_s','peak_device_vram_mib','gpu_j_per_success_lower','gpu_j_per_success_upper','successful_tasks_per_s','tokens_s_completed_requests')
        agent={k:obj[k] for k in keys if type(obj.get(k)) in (int,float) and math.isfinite(obj[k]) and obj[k]>=0}
        for k in ('model_sha256','profile_sha256','independent_review_sha256'):
            if re.fullmatch('[a-f0-9]{64}',str(obj.get(k))):agent[k]=obj[k]
        counter=obj.get('GPU_counter') or {}
        if counter:
            assert counter.get('method')=='NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1'
            agent['GPU_counter']={k:counter[k] for k in ('lower_j','upper_j','group_window_s','complete_request_s') if type(counter.get(k)) in (int,float) and math.isfinite(counter[k]) and counter[k]>=0}
        agent.update(official_benchmark=False,winner_qualified=False,data_role=('RESERVED33_MODEL_UNSEEN_FIXTURES_CORRELATED_FAMILIES_NOT_OFFICIAL' if reserved else 'FROZEN33_VALIDATION_AUTHORED_FAMILIES_NOT_OFFICIAL' if validation33 else 'PREVIOUSLY_USED_DEVELOPMENT18_NOT_TERMINAL_BENCH_NOT_HOLDOUT'))
        result['native_lean_reserved_validation33' if reserved else 'native_validation33' if validation33 else 'native_agent18_development']=agent
    event_recovery=(obj.get('status')=='PARTIAL_WRAPPER_STOP_EVENT_RESPONSES_CPU_REPLAYED'
                    and obj.get('independent_CPU_judgements_identical') is True)
    if (obj.get('status')=='STOPPED_USER_WHOLE_BENCHMARK_TIME_BUDGET' or event_recovery) and obj.get('full_benchmark_score_claimed') is False:
        counts={k:obj.get(k) for k in ('expected_tasks','collected_tasks','scored_tasks','solved_observed_tasks')}
        if all(type(v) is int for v in counts.values()) and 0<=counts['solved_observed_tasks']<=counts['scored_tasks']<=counts['collected_tasks']<counts['expected_tasks']:
            evidence={**counts,'full_benchmark_score_claimed':False,'scope':'BUDGET_LIMITED_PARTIAL_TASK_SET; NOT_A_FULL_OFFICIAL_SCORE'}
            if event_recovery:
                evidence.update(scope='TECHNICAL_WRAPPER_STOP_EVENT_RECOVERY; NOT_A_FULL_OFFICIAL_SCORE',
                                independent_CPU_judgements_identical=True,
                                original_HTTP_and_input_token_capture_missing=True,
                                whole_task_energy_j=None,completed_task_phase_s=None)
            measured=obj.get('prefix_measurement') or obj.get('measurement_summary') or {}
            for original,public in [('case_inference_wall_s','request_interval_wall_s'),('case_gpu_energy_j','request_interval_gross_GPU_j'),('collected_task_inference_wall_s','request_interval_wall_s'),('collected_task_GPU_energy_j','request_interval_gross_GPU_j')]:
                v=measured.get(original)
                if type(v) in (float,int) and math.isfinite(v) and v>=0:evidence[public]=v
            result['partial_benchmark_evidence']=evidence
    if obj.get('experiment_id') in ('R444','R445','R446'):
        for k in ('observed_cases','planned_cases','complete_cases','protocol_valid_cases','full_pilot','coding_wall_s','coding_gpu_energy_j_approx','independent_native_case_recount','maximum_NMSE_bound','supervised_interval_seconds','supervised_interval_gpu_J','execution_uid'):
            v=obj.get(k)
            if type(v) in (int,float,bool) and (type(v) is not float or math.isfinite(v)):result[k]=v
    if obj.get('extended_technique') in ('MODEL_BONSAI_PREFIX_REUSE_FIRST3_SCREEN','MODEL_BONSAI_PREFIX_REUSE_FULL18_CONFIRMATION','MODEL_BONSAI_PREFIX_REUSE_FRESH_COLD_CONTROL'):
        for k in ('planned_tasks','full3_score_claimed','total_task_wall_s','wall_reduction_percent_vs_A0','GPU_J_per_success_reduction_percent_vs_A0','control_comparable','control_wall_drift_percent','control_energy_drift_percent','candidate_same3_wall_reduction_percent','candidate_same3_GPU_Jsuccess_reduction_percent','qualification_candidate_passed'):
            value=obj.get(k)
            if type(value) in (int,float,bool) and (type(value) is not float or math.isfinite(value)):result[k]=value
        cache=obj.get('prefix_cache')
        if isinstance(cache,dict):
            result['prefix_cache']={k:cache[k] for k in ('cases_with_hits','requests_with_hits','cached_tokens','first_turn_cached_tokens') if type(cache.get(k)) is int and 0<=cache[k]<2**63}
    if obj.get('extended_technique')=='MODEL_BONSAI_AGENT18_INDEPENDENT_REPRODUCTION':
        for k in ('reproduction_passed','allround_practical_gate_reopened','energy_drift_percent_vs_source','total_task_wall_s','full_task_wall_change_percent_vs_control'):
            value=obj.get(k)
            if type(value) in (int,float,bool) and (type(value) is not float or math.isfinite(value)):result[k]=value
        for source,target in (('reference_success_losses','previous_success_losses_count'),('additional_policy_violations','additional_policy_failures_count')):
            if isinstance(obj.get(source),list):result[target]=len(obj[source])
    if obj.get('factor')=='H03' and obj.get('model')=='gemma4':
        fields=('observed_cases','planned_cases','full_36_executions_claimed','unique_tasks','completed_cycles','planned_cycles','control_comparable','control_wall_drift_percent','control_energy_drift_percent','energy_saving_percent_vs_stored','wall_change_percent_vs_stored','candidate_energy_saving_percent_vs_fresh','candidate_wall_change_percent_vs_fresh','qualification_candidate_passed')
        numeric=lambda v:type(v) in (int,float,bool) and (type(v) is not float or math.isfinite(v))
        result.update({k:obj[k] for k in fields if numeric(obj.get(k))})
        allowed=('cycle','observed','solved','wall_s','gpu_energy_j_approx','gpu_j_per_success','energy_saving_percent','wall_change_percent','passed')
        cycles=obj.get('cycle_metrics')
        if isinstance(cycles,list) and len(cycles)<=3:
            result['energy_stability_cycles']=[{k:row[k] for k in allowed if numeric(row.get(k))} for row in cycles if isinstance(row,dict)]
    if obj.get('factor')=='R19':
        for name in ('observed_cases','planned_cases','observed','planned','full12_observed','full_pilot2_score_claimed','full_remaining10_score_claimed','native_output_cap','full_12_semantic_score_claimed','common_control_passed','common_wall_change_percent_vs16K','common_GPU_J_per_success_change_percent_vs16K','VRAM_increase_MiB_vs16K'):
            value=obj.get(name)
            if isinstance(value,(int,float,bool)) and (not isinstance(value,float) or math.isfinite(value)):result[name]=value
        ranges={}
        context=obj.get('context_tokens')
        if type(context) is int and context>0:
            for name,scope in (obj.get('scopes') if isinstance(obj.get('scopes'),dict) else {}).items():
                if name not in ('common','extended','validation') or not isinstance(scope,dict):continue
                band=scope.get('actual_input_token_range')
                if isinstance(band,list) and len(band)==2 and all(type(x) is int for x in band) and 0<band[0]<=band[1]<=context:
                    ranges[name]={'minimum_tokens':band[0],'maximum_tokens':band[1]}
        if ranges:result['context_profile_token_ranges']=ranges
    if obj.get('experiment_id')=='R404' and obj.get('factor')=='A02':
        audit={}
        for arm,name in (('A0','baseline'),('B','candidate')):
            source=obj.get('arm_totals',{}).get(arm,obj.get('baseline' if arm=='A0' else 'candidate',{}))
            if isinstance(source,dict):
                aliases={}
                if 'tasks' not in source and 'requests' in source:aliases['tasks']='requests'
                if 'wall_s_sum' not in source and 'wall_s' in source:aliases['wall_s_sum']='wall_s'
                audit[name]={k:source.get(aliases.get(k,k)) for k in ('tasks','successes','wall_s_sum','wall_s_median','prompt_tokens','successful_tasks_per_s') if isinstance(source.get(aliases.get(k,k)),(int,float,bool)) and (not isinstance(source.get(aliases.get(k,k)),float) or math.isfinite(source[aliases.get(k,k)]))}
        comparisons=obj.get('comparisons',{})
        audit['positive_calculation_successes']={'A0':comparisons.get('positive_successes_A0',0),'B':comparisons.get('positive_successes_B',0)}
        calls=obj.get('false_positive_negative_calls')
        audit['negative_false_tool_calls']={'A0':len([x for x in calls if x.get('arm')=='A0']) if isinstance(calls,list) else comparisons.get('negative_false_calls_A0',0),'B':len(obj['candidate_false_positive_negative_calls']) if isinstance(obj.get('candidate_false_positive_negative_calls'),list) else comparisons.get('negative_false_calls_B',0)}
        audit['gained_tasks']=len(obj['task_success_gained']) if isinstance(obj.get('task_success_gained'),list) else obj.get('gained_tasks',comparisons.get('gained_tasks',0))
        audit['lost_tasks']=len(obj['task_success_lost']) if isinstance(obj.get('task_success_lost'),list) else obj.get('lost_tasks',comparisons.get('lost_tasks',0))
        latency=obj.get('aggregate_latency_gain_fraction')
        if not isinstance(latency,(int,float)):latency=comparisons.get('aggregate_e2e_latency_gain_percent');latency=latency/100 if isinstance(latency,(int,float)) else None
        audit['aggregate_request_latency_gain_percent']=100*latency if isinstance(latency,(int,float)) else None
        energy=obj.get('arm_GPU_energy_j',{})
        if not energy and isinstance(obj.get('GPU_energy_j'),dict):energy={arm:{'gpu_energy_j':value} for arm,value in obj['GPU_energy_j'].items()}
        audit['GPU_energy_j_by_arm']={arm:value['gpu_energy_j'] for arm,value in energy.items() if arm in ('A0','B') and isinstance(value,dict) and isinstance(value.get('gpu_energy_j'),(int,float))}
        peak=obj.get('peak_GPU_VRAM_bytes')
        if not isinstance(peak,(int,float)):peak=comparisons.get('peak_GPU_VRAM_mib')
        if isinstance(peak,(int,float)):audit['peak_device_vram_mib']=peak/1048576 if peak>100000 else peak
        audit['winner_qualified']=False;audit['champion_changed']=False;audit['scope']='SYNTHETIC_SCREEN_ONLY; four candidate successes are safe abstentions; all positive calculations failed in both arms'
        result['A02_BMT07_provenance_retrieval_screen']=audit
    if obj.get('experiment_id')=='R405' and obj.get('factor')=='A02':
        arms=obj.get('arm_totals',{})
        energy=obj.get('arm_GPU_energy',{})
        comparisons=obj.get('comparisons',{})
        result['A02_BMT07_independent_confirmation']={
            'baseline':{k:arms.get('A0',{}).get(k) for k in ('tasks','successes','wall_s_sum','wall_s_median','successful_tasks_per_s')},
            'candidate':{k:arms.get('B',{}).get(k) for k in ('tasks','successes','wall_s_sum','wall_s_median','successful_tasks_per_s')},
            'positive_case_successes':{'A0':comparisons.get('positive_successes_A0',0),'B':comparisons.get('positive_successes_B',0)},
            'negative_false_tool_calls':{
                'A0':len([x for x in obj.get('false_positive_negative_calls',[]) if x.get('arm')=='A0']) if isinstance(obj.get('false_positive_negative_calls'),list) else comparisons.get('negative_false_calls_A0',0),
                'B':len(obj['candidate_false_positive_negative_calls']) if isinstance(obj.get('candidate_false_positive_negative_calls'),list) else comparisons.get('negative_false_calls_B',0)},
            'gained_tasks':len(obj['task_success_gained']) if isinstance(obj.get('task_success_gained'),list) else comparisons.get('gained_tasks',0),
            'lost_tasks':len(obj['task_success_lost']) if isinstance(obj.get('task_success_lost'),list) else comparisons.get('lost_tasks',0),
            'aggregate_request_latency_gain_percent':100*obj.get('aggregate_latency_gain_fraction',0),
            'GPU_energy_j_by_arm':{arm:value.get('gpu_energy_j') for arm,value in energy.items() if arm in ('A0','B') and isinstance(value,dict)},
            'peak_device_vram_mib':obj.get('peak_GPU_VRAM_bytes',0)/1048576,
            'max_temperature_c':obj.get('max_GPU_temperature_c'),
            'winner_qualified':False,'champion_changed':False,
            'scope':'INDEPENDENT SYNTHETIC ABSTENTION SCREEN; all positive calculations failed in both arms'
        }
    if obj.get('measurement_type')=='CPU_FIRST_MLP_NATIVE_Q4K_AWQ_INPUT_SCALING_PROXY':
        fields=('unquantized_boundary_NMSE','unquantized_equivalence_limit','ratios_fitted','fit_rows','fit_source_tokens','chosen_ratio','fit_error_ratio','fit_gate_passed','development_evaluated','development_rows','development_source_tokens','development_A_SSE','development_B_SSE','development_error_ratio','development_error_reduction_percent','proxy_gate_passed','GPU_runs','model_starts','optimizer_steps','new_experimental_factor_coverage','winner_qualified','model_quality_measured','model_performance_measured')
        aggregate={k:obj[k] for k in fields if isinstance(obj.get(k),(int,float,bool)) and (not isinstance(obj[k],float) or math.isfinite(obj[k]))}
        for k in ('source_quantization','target_quantization'):
            if obj.get(k) in ('Q6_K','Q4_K'):aggregate[k]=obj[k]
        if not obj.get('development_evaluated'):
            aggregate['development_evaluated']=False;aggregate['proxy_gate_passed']=False
            for k in ('development_A_SSE','development_B_SSE','development_error_ratio','development_error_reduction_percent'):aggregate.pop(k,None)
        result['CPU_first_MLP_AWQ_proxy']=aggregate
    if obj.get('measurement_type')=='CPU_UNWEIGHTED_NUQ4_DEVELOPMENT_RECONSTRUCTION_PROXY':
        fields=('GPU_runs','model_starts','optimizer_steps','codebook_fits','completed_books','planned_books','development_values','development_sequences','precision_bits','numerical_proxy_gate_passed','winner_qualified','model_quality_measured','model_performance_measured','new_experimental_factor_coverage','geomean_error_ratio','proxy_error_reduction_percent','uniform_logical_payload_bytes','NUQ_logical_payload_bytes','additional_logical_LUT_bytes','uniform_aligned256_estimate_bytes','NUQ_aligned256_estimate_bytes','independent_full_development_reconstruction')
        aggregate={k:obj[k] for k in fields if isinstance(obj.get(k),(int,float,bool)) and (not isinstance(obj[k],float) or math.isfinite(obj[k]))}
        cases=[]
        for row in obj.get('cases',[]):
            if not isinstance(row,dict) or row.get('role') not in ('K','V') or type(row.get('layer')) is not int or row['layer'] not in range(3,32,4):continue
            clean={k:row[k] for k in ('layer','elements','fit_sample_count','Lloyd_iterations','NUQ_uniform_error_ratio','NUQ_SSE','uniform_SSE','NUQ_NMSE','uniform_NMSE','FP16_floor_SSE','sparse_entries','sparse_fraction') if isinstance(row.get(k),(int,float,bool)) and (not isinstance(row[k],float) or math.isfinite(row[k]))}
            clean['role']=row['role'];cases.append(clean)
        if cases:aggregate['numeric_reconstruction_cases']=cases
        result['CPU_NUQ_development_proxy']=aggregate
    if obj.get('measurement_type') in ('GPU_NATIVE_PRE_ROPE_KV_FORWARD_OBSERVER_ADMISSION','GPU_NATIVE_FIRST_MLP_INPUT_FORWARD_OBSERVER_ADMISSION'):
        fields=('model_starts','actual_generation_requests','forward_calls_completed','completed_chunks','planned_chunks','tokens_per_chunk','captured_named_tensors','raw_activation_bytes','calibration_fidelity_passed','original12_quality_cases','optimizer_steps','quantizer_fits','new_experimental_factor_coverage','winner_qualified','peak_device_vram_mib','meanabs_channels')
        aggregate={k:obj[k] for k in fields if isinstance(obj.get(k),(int,float,bool)) and (not isinstance(obj[k],float) or math.isfinite(obj[k]))}
        checks=[]
        for row in obj.get('observations',[]):
            if not isinstance(row,dict):continue
            checks.append({k:row[k] for k in ('chunk','tokens','captured_named_tensors','finite_logits','control_logits_byte_identical','maximum_abs_logit_difference','vocabulary_logits','quantizer_fits','optimizer_steps') if isinstance(row.get(k),(int,float,bool)) and (not isinstance(row[k],float) or math.isfinite(row[k]))})
        if checks:aggregate['fidelity_checks']=checks
        if aggregate:result['forward_MLP_calibration_admission' if obj.get('measurement_type')=='GPU_NATIVE_FIRST_MLP_INPUT_FORWARD_OBSERVER_ADMISSION' else 'forward_KV_calibration_admission']=aggregate
    if obj.get('measurement_type')=='GPU_UPSTREAM_KIVI_2BIT_SM70_COMPONENT_NUMERICAL_ADMISSION':
        allowed=('native_cases','passed_cases','NMSE_limit','native_binary_SM','model_starts','operator_processes','actual_GPU_inference','original12_quality_cases','numerical_gate_passed','screen_passed','winner_qualified','peak_device_vram_mib')
        component={k:obj[k] for k in allowed if isinstance(obj.get(k),(int,float,bool)) and (not isinstance(obj[k],float) or math.isfinite(obj[k]))}
        fields=('IC','OC','query_heads','KV_heads','M','bits','group','seed','native_binary_SM','registers','output_elements','NMSE','limit','max_abs_error','finite','passed','synthetic_cache_quantization_NMSE','packed_bytes','scale_zero_bytes','F16_cache_bytes','residual_buffer_included')
        cases=[]
        for row in obj.get('cases',[]):
            if not isinstance(row,dict):continue
            clean={k:row[k] for k in fields if isinstance(row.get(k),(int,float,bool)) and (not isinstance(row[k],float) or math.isfinite(row[k]))}
            if clean:cases.append(clean)
        if cases:component['numeric_component_cases']=cases
        commit=obj.get('upstream_commit')
        if isinstance(commit,str) and re.fullmatch('[0-9a-f]{40}',commit):component['upstream_commit']=commit
        if component:result['KIVI_SM70_component']=component
    if obj.get('measurement_type')=='GPU_ACTUAL_LLGUIDANCE_TYPED_SCHEMA_QA12_SCREEN':
        fields=('observed_cases','planned_cases','actual_llguidance_requests','model_starts','wall_s','matched_reference_wall_s','archived_reference_E2E_change_percent','gpu_energy_j_approx','peak_device_vram_mib','screen_passed','winner_qualified','token_distribution_preserved')
        result['LLGuidance_QA12_screen']={k:obj[k] for k in fields if isinstance(obj.get(k),(int,float,bool)) and (not isinstance(obj[k],float) or math.isfinite(obj[k]))}
    if obj.get('measurement_type')=='GPU_FIXED_SCHEMA_NATIVE_STOP_FRAMING_SCREEN':
        fields=('model_starts','requests','template_requests','timed_pairs','functional_gate_passed','actual_stop_intervention_executed','paired_geomean_E2E_change_percent','correct_mock_labels_per_arm','minimum_E2E_reduction_percent','peak_device_vram_mib','hardware_guards_passed','receiver_framing_required','raw_candidate_is_not_complete_JSON','original12_quality_cases','screen_passed','winner_qualified','request_GPU_j_A_approx','request_GPU_j_B_approx','request_GPU_j_change_percent')
        aggregate={k:obj[k] for k in fields if k in obj and (obj[k] is None or isinstance(obj[k],(int,float,bool)))}
        if aggregate:result['schema_completion_protocol']=aggregate
    if obj.get('measurement_type')=='GPU_MOCK_ACTION_SELECTIVE_RISK_CALIBRATION_SCREEN':
        fields=('model_starts','requests','calibration_cases','calibration_correct_decisions','calibration_unsafe_allows','holdout_pairs','underlying_holdout_decisions_equal','thresholds_fitted','holdout_unsafe_allows_A','holdout_unsafe_allows_B','correct_allow_retention','holdout_abstentions','holdout_request_wall_A_s','holdout_request_wall_B_s','holdout_GPU_j_A_approx','holdout_GPU_j_B_approx','peak_device_vram_mib','hardware_guards_passed','original12_quality_cases','winner_qualified','screen_passed')
        aggregate={k:obj[k] for k in fields if k in obj and (obj[k] is None or isinstance(obj[k],(int,float,bool)))}
        if obj.get('holdout_pairs')==0:
            # A vacuous True from an empty loop does not prove a comparison.
            aggregate['underlying_holdout_decisions_equal']=None
            aggregate['holdout_comparison_performed']=False
        for k in ('calibration_request_GPU_j_approx','calibration_request_wall_s'):
            if isinstance(obj.get(k),(int,float)):aggregate[k]=obj[k]
        confusion=obj.get('calibration_confusion')
        if isinstance(confusion,dict):
            aggregate['calibration_confusion']={label:{pred:value for pred,value in row.items() if pred in {'allow','deny','ask'} and type(value) is int} for label,row in confusion.items() if label in {'allow','deny','ask'} and isinstance(row,dict)}
        if aggregate:result['mock_action_calibration']=aggregate
    if obj.get('measurement_type')=='GPU_HEAD_FREE_PROBABILITY_ACQUISITION_SCREEN':
        fields=('matched_pairs','all_paired_token_IDs_equal','probability_metadata_valid','probability_token_entries','nondegenerate_top_logprob_entries','model_starts','requests','calibration_fits','original12_quality_cases','task_successes_measured','peak_device_vram_mib','screen_passed')
        aggregate={k:obj[k] for k in fields if isinstance(obj.get(k),(int,float,bool))}
        pairs=[]
        for row in obj.get('comparisons',[]):
            if not isinstance(row,dict):continue
            pairs.append({k:row[k] for k in ('round','token_IDs_equal','A_e2e_s','B_e2e_s','E2E_change_percent','A_GPU_j','B_GPU_j','A_energy_coverage','B_energy_coverage') if isinstance(row.get(k),(int,float,bool))})
        if pairs:aggregate['matched_acquisition_costs']=pairs
        if aggregate:result['probability_acquisition']=aggregate
    if obj.get('measurement_type')=='GPU_WEIGHTEDV_FP32_EXACT_INPUT_NUMERICAL_SCREEN':
        allowed=('native_cases_per_arm','baseline_passed_cases','candidate_passed_cases','NMSE_limit','model_starts','operator_processes','tensor_upload_records','identical_tensor_upload_bytes_SHA_verified','actual_precision_dispatch_verified','candidate_numerical_gate_passed','peak_device_vram_mib')
        component={k:obj[k] for k in allowed if isinstance(obj.get(k),(int,float,bool))}
        comparisons=[]
        for value in obj.get('numerical_comparisons',[]):
            if not isinstance(value,dict):continue
            aggregate={k:value[k] for k in ('A_NMSE','B_NMSE','change_percent') if isinstance(value.get(k),(int,float))}
            if aggregate:comparisons.append(aggregate)
        if comparisons:component['NMSE_comparisons']=comparisons
        if component:result['weighted_V_precision_component']=component
    if obj.get('measurement_type')=='GPU_C16_FRACTIONAL_QUEUE_MEMORY_SCREEN':
        variants=[]
        for value in obj.get('variants',[]):
            if not isinstance(value,dict) or value.get('value') not in {'0.25x','0.5x'}: continue
            aggregate={k:value[k] for k in ('requests','model_starts','warmup_requests','quality_cases','peak_device_vram_mib','memory_saved_vs_A0_mib','minimum_memory_saving_mib','primary_memory_gate_passed','screen_passed','measurement_valid') if isinstance(value.get(k),(int,float,bool))}
            aggregate['capacity_setting']=value['value'];aggregate['scope']='EARLY_MEMORY_SCREEN_ONLY';variants.append(aggregate)
        if variants:result['queue_memory_variants']=variants
    numerical=obj.get('numerical_result')
    if isinstance(numerical,dict):
        aggregate={k:projection(numerical[k]) for k in ('cases_count','passed_cases','NMSE_limit','numerical_gate_passed','private_library_mapping_verified','model_starts','wall_s') if isinstance(numerical.get(k),(int,float,bool))}
        if aggregate:result['numerical_component']=aggregate
    # The conservative log-key filter excludes 'logical'; expose only this
    # explicitly verified boolean under a public accounting label.
    managed=obj.get('actual_managed_allocator')
    if isinstance(managed,dict) and managed.get('logical_allocation_is_not_NVML_residency') is True:
        result.setdefault('actual_managed_allocator',{})['managed_bytes_are_not_residency']=True
    return result

def development_result(root,entry,receipt):
    """Bounded projection of an independently replayed A/B/C development run.

    Does not create a benchmark definition, history run or highscore row.
    """
    root=pathlib.Path(root).resolve()
    if set(entry)!={'path','sha256'}:raise ValueError('Invalid development review reference')
    rp=(root/entry['path']).resolve()
    if not rp.is_relative_to(root) or digest(rp)!=entry['sha256']:raise ValueError('Development review changed')
    review=load(rp)
    if review.get('status')!='INDEPENDENT_DEVELOPMENT_REPLAY_IDENTICAL_NOT_OFFICIAL_QUALIFICATION' or review.get('changed_judgments')!=[] or review.get('actual_request_deltas_verified') is not True or review.get('GPU_runs')!=0 or review.get('model_requests')!=0 or review.get('winner_qualified') is not False:raise ValueError('Development replay is not verified')
    ap=pathlib.Path(review['audit_path']).resolve()
    if not ap.is_relative_to(root) or digest(ap)!=review['audit_sha256']:raise ValueError('Development original audit changed')
    audit=load(ap)
    if audit.get('experiment_id')!=review.get('experiment_id') or audit.get('measurement_valid') is not True or audit.get('GPU_execution_observed') is not True or audit.get('official_benchmark') is not False or audit.get('winner_qualified') is not False or audit.get('full_benchmark_score_claimed') is not False:raise ValueError('Invalid development evidence scope')
    if not re.fullmatch(r'R[1-9][0-9]{1,3}',audit['experiment_id']) or not 0<=audit['complete_ABC_task_triples']*3<=audit['completed_requests']<=audit['planned_requests'] or audit['task_limit_s']!=1200:raise ValueError('Invalid development task counts/budget')
    raw=pathlib.Path(audit['raw_root']).resolve()
    if not raw.is_relative_to(root.parent):raise ValueError('Development capture outside canonical workspace')
    for name,h in audit['original_raw_files_sha256'].items():
        source=(raw/name).resolve()
        if not source.is_relative_to(raw) or digest(source)!=h:raise ValueError('Development original capture changed')
    native=load(raw/'profile.json');recipe=native['native_recipe']
    arms=[]
    for arm in ('A','B','C'):
        scopes=audit['matched_arms_by_category'][arm]
        row={'arm':arm,'thinking_requested':arm=='A','temperature':0.0 if arm=='C' else 0.6,
             'max_output_tokens':recipe['request_options']['max_tokens']}
        for category in ('coding','tools'):
            scope=scopes[category]
            if type(scope['completed']) is not int or type(scope['successes']) is not int or not 0<=scope['successes']<=scope['completed']:raise ValueError('Invalid development success counts')
            allowed=('completed','successes','final_text_present','valid_terminal_output','length_stops','completed_request_wall_s','completion_tokens','GPU_j_per_success_lower','GPU_j_per_success_upper')
            row[category]={k:scope[k] for k in allowed}
        arms.append(row)
    if any(sum(row[c]['completed'] for c in ('coding','tools'))!=audit['complete_ABC_task_triples'] for row in arms):raise ValueError('Development matched coverage differs')
    if review['replayed_requests']!=audit['completed_requests'] or review['matched_base_tasks']!=audit['complete_ABC_task_triples']:raise ValueError('Development replay coverage differs')
    return {'experiment_id':audit['experiment_id'],'evidence':'LOKAL_GEMESSEN_DEVELOPMENT_ONLY','official_benchmark':False,
            'completed_requests':audit['completed_requests'],'planned_requests':audit['planned_requests'],
            'matched_base_tasks':audit['complete_ABC_task_triples'],'task_phase_s':audit['task_phase_s'],
            'peak_device_vram_mib':audit['peak_device_vram_mib'],'arms':arms,
            'model_sha256':native['model_sha256'],'engine_binary_sha256':native['assets'][native['runtime']+'/llama-server'],
            'context':recipe['context'],'task_limit_s':audit['task_limit_s'],
            'audit_ids':[receipt(ap,review['audit_sha256']),receipt(rp,entry['sha256'])]}

def mtp_development_result(root,entry,receipt):
    """Verified aggregate projection; no benchmark registration or screening recount."""
    root=pathlib.Path(root).resolve();p=pathlib.Path(entry['path']).resolve()
    assert p.is_relative_to(root) and digest(p)==entry['sha256']
    review=load(p)
    assert review['experiment_id']=='R539' and review['baseline_experiment_id']=='R515'
    assert review['status']=='PROMISING_REQUIRES_FRESH_CONFIRMATION'
    assert review['single_MTP_treatment_verified'] is True
    assert review['winner_qualified'] is False and review['official_benchmark'] is False and review['GPU_runs_in_review']==0
    for name,h in review['source_files_sha256'].items():
        original=pathlib.Path(name).resolve()
        assert original.is_relative_to(root.parent) and digest(original)==h
    a=load(root/'staging/r515/AUDIT.json');b=load(root/'staging/r539/AUDIT.json')
    for audit in (a,b):
        assert audit['measurement_valid'] and audit['GPU_execution_observed']
        assert audit['completed_requests']==audit['planned_requests']==32
        assert not audit['official_benchmark'] and not audit['winner_qualified']
    assert review['comparison']['baseline_task_s']==a['task_phase_s']
    assert review['comparison']['candidate_task_s']==b['task_phase_s']
    result={k:projection(review[k]) for k in ('comparison','quality')}
    result.update(status=text(review['status']),scope=text(review['scope']),next_action=text(review['next_action']),
                  official_benchmark=False,winner_qualified=False,audit_id=receipt(p,entry['sha256']))
    result['profiles']=[{'experiment_id':eid,'task_phase_s':audit['task_phase_s'],
                        'peak_device_vram_mib':audit['peak_device_vram_mib'],
                        'coding_solved':audit['groups']['coding']['successes'],
                        'tools_solved':audit['groups']['tools']['successes'],
                        'counter_lower_j':review['GPU_counter'][eid]['lower_j'],
                        'counter_upper_j':review['GPU_counter'][eid]['upper_j']}
                       for eid,audit in (('R515',a),('R539',b))]
    return result

def mtp_confirmation_projection(review,audit,profile):
    """Aggregate development A/B evidence, never an official benchmark row."""
    ident=review['experiment_id'];assert ident==audit['experiment_id'] and ident in ('R540','R551')
    positive_status=('FRESH_AB_DEVELOPMENT_SPEED_CONFIRMED_OFFICIAL_QUALIFICATION_PENDING' if ident=='R540'
                     else 'FRESH_AB_DEVELOPMENT_SPEED_CONFIRMED_EXISTING_QUALIFICATIONS_REUSED')
    assert review['status'] in (positive_status,'FRESH_AB_DEVELOPMENT_GATE_NOT_MET')
    passed=review['status']==positive_status
    if 'development_gate_passed' in review:assert type(review['development_gate_passed']) is bool and review['development_gate_passed']==passed
    assert review['winner_qualified'] is False and review['official_benchmark'] is False and review['GPU_runs_in_review']==0
    assert audit['measurement_valid'] and audit['GPU_execution_observed']
    assert audit['completed_requests']==audit['planned_requests']==64 and audit['model_starts']==2
    assert not audit['official_benchmark'] and not audit['winner_qualified']
    assert review['quality']['paired_tasks']==32 and type(review['quality']['paired_success_losses']) is int and 0<=review['quality']['paired_success_losses']<=32
    if passed:assert review['quality']['paired_success_losses']==0
    if isinstance(audit.get('scored_tasks'),list):
        cases={r['id']:r['success'] for r in audit['scored_tasks']}
        assert len(cases)==64 and all(type(v) is bool for v in cases.values())
        ids=[k[:-3] for k in cases if k.endswith('--A')];assert len(ids)==32
        assert all(k+'--B' in cases for k in ids)
        assert sum(cases[k+'--A'] and not cases[k+'--B'] for k in ids)==review['quality']['paired_success_losses']
    assert 0<review['single_task_clock_s']<=1200 and review['task_limit_s']==1200
    result={'status':text(review['status']),'scope':text(review['scope']),'next_action':text(review['next_action']),
            'official_benchmark':False,'winner_qualified':False,'single_task_clock_s':review['single_task_clock_s'],
            'comparison':projection(review['comparison']),'quality':projection(review['quality']),'arms':[]}
    for arm in ('A','B'):
        r=review['arms'][arm];g=audit['arms'][arm]
        assert g['coding']['completed']==g['tools']['completed']==16
        assert r['tasks']==32 and r['coding_successes']==g['coding']['successes'] and r['tool_successes']==g['tools']['successes']
        assert r['successes']==r['coding_successes']+r['tool_successes']
        assert math.isclose(r['response_wall_s'],sum(v['completed_request_wall_s'] for v in g.values()),abs_tol=1e-8)
        keys=('coding_successes','tool_successes','tasks','successes','response_wall_s','arm_including_setup_s','peak_device_vram_mib','completion_tokens',
              'GPU_j_per_success_lower','GPU_j_per_success_upper','reported_generation_window_tokens_s','draft_counter_responses','draft_generated','draft_accepted')
        result['arms'].append({'arm':arm,**{k:r.get(k) for k in keys}})
    result['identities']={'model_sha256':profile['model_sha256'],
                         'engine_binary_sha256':profile['assets'][profile['runtime']+'/llama-server']}
    if 'native_mtp_integrated' in profile:
        assert ident=='R551' and 'native_mtp_draft' not in profile
        assert profile['native_mtp_integrated']=={'version':'QWEN38_INTEGRATED_TARGET_MTP_V1','model_sha256':'58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f','draft_max':3,'draft_min':1}
        assert profile['model_sha256']==profile['native_mtp_integrated']['model_sha256']
        assert result['identities']['engine_binary_sha256']=='08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54'
        counters=review['arms']['B'];assert type(counters.get('draft_generated')) is int and counters['draft_generated']>0
        assert type(counters.get('draft_accepted')) is int and 0<=counters['draft_accepted']<=counters['draft_generated']
        result['identities']['integrated_head_target_sha256']=profile['model_sha256']
        result['draft_binding_kind']='INTEGRATED_TARGET_HEAD_NO_SEPARATE_DRAFT_FILE'
    else:
        assert ident=='R540'
        result['identities']['draft_sha256']=profile['native_mtp_draft']['sha256']
    assert all(re.fullmatch('[a-f0-9]{64}',h) for h in result['identities'].values())
    return result

def verified_mtp_confirmation_result(root,entry,receipt):
    root=pathlib.Path(root).resolve();p=pathlib.Path(entry['path']).resolve()
    assert p.is_relative_to(root) and digest(p)==entry['sha256']
    review=load(p)
    for name,h in review['source_files_sha256'].items():
        source=pathlib.Path(name).resolve();assert source.is_relative_to(root.parent) and digest(source)==h
    ident=review['experiment_id'];assert ident in ('R540','R551')
    audit=load(root/'staging'/ident.lower()/'AUDIT.json');profile=load(pathlib.Path(audit['raw_root'])/'profile.json')
    result=mtp_confirmation_projection(review,audit,profile)
    result['audit_id']=receipt(p,entry['sha256'])
    return result

def verified_coding_mtp_comparison(root,entry,receipt,candidate="R541"):
    baseline,count={"R541":("R516",164),"R542":("R517",200)}[candidate]
    root=pathlib.Path(root).resolve();path=pathlib.Path(entry['path']).resolve()
    assert path.is_relative_to(root) and digest(path)==entry['sha256']
    review=load(path)
    assert review['experiment_id']==candidate and review['GPU_runs_in_review']==0 and review['winner_qualified'] is False
    assert review['official_benchmark_result_valid'] is True
    for name,h in review['source_files_sha256'].items():
        source=pathlib.Path(name).resolve();assert source.is_relative_to(root.parent) and digest(source)==h
    profiles=[]
    for eid in (baseline,candidate):
        measured=review['profiles'][eid];audit=load(root/'staging'/eid.lower()/'AUDIT.json')
        assert measured['tasks']==audit['collected_tasks']==audit['scored_tasks']==count
        assert measured['solved']==audit['solved_observed_tasks']
        profiles.append({'experiment_id':eid,**{k:measured[k] for k in ('tasks','solved','response_wall_s','task_phase_s','peak_device_vram_mib','GPU_j_per_success_lower','GPU_j_per_success_upper')}})
    return {'profiles':profiles,'quality':projection(review['quality']),'comparison':projection(review['comparison']),
            'quality_gate_passed':review['predeclared_quality_gate_passed'],'speed_gate_passed':review['predeclared_speed_gate_passed'],
            'decision':text(review['decision']),'scope':text(review['scope']),'winner_qualified':False,'audit_id':receipt(path,entry['sha256'])}
def verified_qualification_review(root,entry,receipt):
    root=pathlib.Path(root).resolve();path=pathlib.Path(entry['qualification_review_path']).resolve()
    assert path.is_relative_to(root/'staging') and digest(path)==entry['qualification_review_sha256']
    review=load(path);assert review['experiment_id']==entry['experiment_id']
    assert (review.get('candidate_audit_sha256') or review.get('source_audit_sha256'))==entry['audit_sha256']
    assert review['winner_qualified'] is False and review['GPU_runs']==0 and review['model_requests']==0
    assert review['source_files_sha256']
    for name,h in review['source_files_sha256'].items():
        source=pathlib.Path(name).resolve();assert source.is_relative_to(root.parent) and digest(source)==h
    for eid,profile in review['profiles'].items():
        assert re.fullmatch(r'R[1-9][0-9]{1,3}',eid)
        audit_path=root/'staging'/eid.lower()/'AUDIT.json';assert review['source_files_sha256'].get(str(audit_path))==digest(audit_path)
        a=load(audit_path)
        if a.get('status') in ('OPTIMIZATION_DEVELOPMENT_COMPLETE','SCREENING VOLLSTÄNDIG'):
            assert a['official_benchmark'] is False and a['winner_qualified'] is False
            assert a['completed_requests']==a['planned_requests']==len(a['scored_tasks'])
            assert len({t['id'] for t in a['scored_tasks']})==a['completed_requests']
            assert all(type(t['success']) is bool for t in a['scored_tasks'])
            assert sum(g['completed'] for g in a['groups'].values())==a['completed_requests']
            assert sum(g['successes'] for g in a['groups'].values())==sum(t['success'] for t in a['scored_tasks'])
            assert profile['tasks']==a['completed_requests'] and profile['solved']==sum(t['success'] for t in a['scored_tasks'])
        else:
            assert profile['tasks']==a.get('collected_tasks',a.get('tasks')) and profile['solved']==a.get('solved_observed_tasks',a.get('solved'))
        assert profile['task_phase_s']==a['task_phase_s']
        assert profile['peak_device_vram_mib']==a.get('peak_device_vram_mib',a.get('measurement_summary',{}).get('peak_device_vram_mib'))
    return {'audit_id':receipt(path,entry['qualification_review_sha256']),'decision':text(review['decision']),
            'scope':text(review['scope']),'gates':projection(review['predeclared_gates']),
            'comparison_class':text(review.get('comparison_class')),'aggregate_metrics':metrics(review)}

def role_case_costs(records,telemetry):
    """Read-only paired R537 costs. Never export requests, answers or fixture IDs."""
    from leaderboard import counter_energy_bounds
    identities={r['id']:r for r in records if r.get('kind')=='input_identity'}
    turns={r['id']:r for r in records if r.get('kind')=='agent_turn'}
    assert len(identities)==sum(r.get('kind')=='input_identity' for r in records)
    assert len(turns)==sum(r.get('kind')=='agent_turn' for r in records) and set(turns)==set(identities)
    cases=[r for r in records if r.get('kind')=='orchestration_case'];assert len({c['id'] for c in cases})==len(cases);order=list(dict.fromkeys(r['source_case_id'] for r in cases));output=[]
    def total(values):return sum(values) if values and all(type(x) is int and x>=0 for x in values) else None
    for case in cases:
        assert case['arm'] in ('single','planner_worker','planner_worker_reviewer') and type(case['reported_result']['task_success']) is type(case['reported_result']['policy_gate_pass']) is bool
        assert case['e2e_s']==(case['end_ns']-case['start_ns'])/1e9
        selected=[r for ident,r in turns.items() if identities[ident]['case_id']==case['id']]
        assert len(selected)==case['attempted_requests'] and sum(case['role_calls'].values())==len(selected)
        assert all(identities[r['id']]['source_case_id']==case['source_case_id'] and identities[r['id']]['arm']==case['arm'] for r in selected)
        assert all(case['start_ns']<=r['start_ns']<r['end_ns']<=case['end_ns'] for r in selected)
        usage=[r['reply'].get('usage',{}) for r in selected]
        energy=counter_energy_bounds(telemetry,[case],[case['id']])
        output.append({'case':'case-'+str(order.index(case['source_case_id'])+1).zfill(2),'source_case_sha256':hashlib.sha256(case['source_case_id'].encode()).hexdigest(),
          'arm':case['arm'],'success':case['reported_result']['task_success'],'policy_pass':case['reported_result']['policy_gate_pass'],
          'model_calls':len(selected),'role_calls':{k:case['role_calls'][k] for k in ('worker','planner','reviewer')},
          'reported_prompt_tokens':total([u.get('prompt_tokens') for u in usage]),'recorded_input_token_count':total([identities[r['id']].get('prompt_token_count') for r in selected]),
          'completion_tokens':total([u.get('completion_tokens') for u in usage]),'case_seconds':case['e2e_s'],
          'GPU_j_lower':energy['lower_j'],'GPU_j_upper':energy['upper_j'],'simulator_callbacks':case['simulator_callbacks']})
    return {'paired_cases':len(order),'case_executions':len(cases),'rows':output,'new_GPU_runs':0,'new_model_requests':0,
      'not_measured':['separate preamble tokens per step','separate reasoning tokens','compaction events','streaming TTFT','reviewer error-detection accuracy'],
      'scope':'Archived complete R537 replies only. Prompt counts include recurrent history; they do not isolate preamble cost. Five exposed paired cases, fixed arm order, not15 independent tasks or an H0/H1 ablation. Per-case energy brackets can overlap at boundaries and must not be summed as an authoritative arm total. GPU energy excludes CPU/system energy. No official benchmark, equivalence or causal harness winner.'}

def verified_native_tools_confirmation(root,entry,receipt):
    """Independent public projection of two full/partial200 arms; no pooled score."""
    from leaderboard import counter_energy_bounds
    root=pathlib.Path(root).resolve();ap=pathlib.Path(entry['audit_path']).resolve()
    assert ap==root/'staging/r546/AUDIT.json' and digest(ap)==entry['audit_sha256']
    a=load(ap);assert a['experiment_id']=='R546' and a['measurement_valid'] and a['GPU_execution_observed']
    assert a['official_benchmark'] is False and a['winner_qualified'] is False and a['full_benchmark_score_claimed'] is False
    assert a['status'] in ('FRESH_TOOLS_AB400_COMPLETE','PARTIAL')
    raw=pathlib.Path(a['raw_root']).resolve();assert raw.is_relative_to(root.parent/'research/mcp-workspace')
    assert all(digest(raw/n)==h for n,h in a['original_raw_files_sha256'].items())
    p=load(raw/'profile.json');contract=load(raw/'CONTRACT.json');plan=load(ap.parent/'CAMPAIGN_PLAN.json')
    assert digest(ap.parent/'CAMPAIGN_PLAN.json')==a['campaign_plan_sha256']
    assert digest(ap.parent/'PREDECLARED_PLAN.json')==a['predeclared_plan_sha256']
    assert contract['id']=='r546-native-mtp-tools-confirmation400' and contract['runtime_seconds']==1200
    assert p['native_recipe']['mtp_tools_confirmation']=={'version':'MTP_TOOLS_AB400_V1','arms':['A','B'],'base_requests_per_arm':200,'model_starts':2,'total_task_seconds':1200,'includes_model_setup':True}
    base_ids=['parallel_multiple_'+str(i) for i in range(200)]
    assert contract['parameters']=={'dataset':'omni-native-mtp-tools-confirmation400-v1','task_ids':[v+'--'+arm for arm in ('A','B') for v in base_ids]}
    rows=[json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()]
    telemetry=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
    official_descriptor=load(raw/'TRUST_SNAPSHOT.json')['task_datasets']['bfcl-v4-parallel-multiple-full200']
    official_task_file=pathlib.Path(official_descriptor['tasks_file']).resolve()
    assert official_task_file.is_relative_to(root) or (official_task_file.name=='TASKS.json' and official_task_file.parent.name=='bfcl-parallel-multiple200' and official_task_file.parent.parent.name=='task_datasets')
    assert digest(official_task_file)==official_descriptor['tasks_sha256']
    answers=[v for v in rows if v.get('kind')=='native_tool'];assert [v['id'] for v in answers]==contract['parameters']['task_ids'][:len(answers)]
    launch=load(raw/'LAUNCH.json') if (raw/'LAUNCH.json').exists() else {}
    arm_windows=launch.get('arms',[])
    assert len({v['arm'] for v in arm_windows})==len(arm_windows)
    if a['status']=='FRESH_TOOLS_AB400_COMPLETE':
        assert launch.get('single_shared_task_clock') is True and launch.get('model_setup_charged_to_task_budget') is True
        assert [v['arm'] for v in arm_windows]==['A','B'] and arm_windows[0]['end_ns']<=arm_windows[1]['start_ns']
    result={'status':text(a['status']),'decision':text(a['decision']),'scope':text(a['data_scope']),
            'official_benchmark':False,'winner_qualified':False,'shared_task_phase_s':a['task_phase_s'],
            'shared_task_limit_s':1200,'setup_in_shared_budget':True,'comparison':projection(a['comparison']),
            'gates':projection(a['predeclared_gates']),'arms':[],'identities':{'model_sha256':p['model_sha256'],
            'draft_sha256':p['native_mtp_draft']['sha256'],'engine_binary_sha256':p['assets'][p['runtime']+'/llama-server']}}
    for arm in ('A','B'):
        selected=[v for v in answers if v['id'].endswith('--'+arm)];stored=a['profiles'][arm]
        assert stored['tasks']==len(selected)
        if not selected:
            assert stored['solved'] is None
            result['arms'].append({'arm':arm,'tasks':0,'solved':None,'status':'NOT MEASURED'});continue
        ids=[v['id'][:-3] for v in selected];assert ids==base_ids[:len(selected)]
        derived=ap.parent/arm/'RESPONSES.jsonl';mapped=[json.loads(l) for l in derived.read_text().splitlines()]
        scoring_plan=load(ap.parent/arm/'SCORING_PLAN.json');original_plan=load(root/'staging/r542/SCORING_PLAN.json')
        assert scoring_plan['case_ids']==ids and scoring_plan['responses_sha256']==digest(derived) and scoring_plan['task_manifest_sha256']==official_descriptor['tasks_sha256']
        for key in ('worker_sha256','official_utils_sha256','task_manifest_sha256','source_revision'):
            assert scoring_plan[key]==original_plan[key]
        assert digest(ap.parent/'score_native.py')==scoring_plan['worker_sha256']=='3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666'
        assert digest(ap.parent/'OFFICIAL_BFCL_UTILS.txt')==scoring_plan['official_utils_sha256']=='3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd'
        expected=[]
        for v in selected:
            row=copy.deepcopy(v);row['id']=v['id'][:-3];expected.append(row)
        assert mapped==expected,'CPU input view must only remove the closed arm suffix'
        parsed=[]
        for suffix in ('score','replay'):
            label='r546-'+arm.lower()+'-'+suffix;rp=ap.parent/arm/(label+'.receipt.json');execution=load(rp)
            assert execution['returncode']==0 and 'Result=success' in execution['properties']
            for name,h in execution['input_sha256'].items():
                path=pathlib.Path(name).resolve();assert (path.is_relative_to(root) or path==official_task_file) and digest(path)==h
            out=ap.parent/arm/(label+'.stdout');parsed.append([json.loads(l) for l in out.read_text().splitlines()])
            assert any(v['receipt_path']==str(rp) and v['receipt_sha256']==digest(rp) and v['stdout_sha256']==digest(out) for v in a['scoring_receipts'])
        assert parsed[0]==parsed[1]
        summary=parsed[0][-1];scored=[v for v in parsed[0] if 'id' in v]
        assert [v['id'] for v in scored]==ids and summary['tasks']==len(selected)
        assert summary['model_requests']==summary['tool_executions']==0 and summary['official_revision']==scoring_plan['source_revision']
        assert stored['solved']==summary['official_AST_solved']==sum(v['official_AST_success'] for v in scored)
        for key in ('practical_solved','protocol_valid'):assert stored[key]==summary[key]
        assert stored['complete_final_answers']==summary['complete']
        energy=counter_energy_bounds(telemetry,selected,[v['id'] for v in selected]);assert energy==stored['GPU_counter']
        for side in ('lower','upper'):
            assert stored['GPU_j_per_success_'+side]==(energy[side+'_j']/stored['solved'] if stored['solved'] else None)
        wall=sum(v['e2e_s'] for v in selected);tokens=sum(v['reply']['usage']['completion_tokens'] for v in selected)
        assert wall==stored['response_wall_s'] and tokens==stored['completion_tokens']
        def measured_total(key):
            values=[v['reply'].get('timings',{}).get(key) for v in selected]
            return sum(values) if values and all(type(v) in (int,float) and math.isfinite(v) and v>=0 for v in values) else None
        engine_timings={key:measured_total(key) for key in ('prompt_n','prompt_ms','predicted_n','predicted_ms','draft_n','draft_n_accepted')}
        for name,tokens_key,ms_key in [('prefill','prompt_n','prompt_ms'),('decode','predicted_n','predicted_ms')]:
            engine_timings[name+'_reported_tok_s']=1000*engine_timings[tokens_key]/engine_timings[ms_key] if engine_timings[tokens_key] is not None and engine_timings[ms_key] is not None and engine_timings[ms_key]>0 else None
        engine_timings['scope']='Sum of recorded engine token counts divided by summed engine milliseconds, not HTTP throughput or streaming TTFT. Missing counters remain unknown.'
        observed_window=next((v for v in arm_windows if v['arm']==arm),None);hardware={}
        if observed_window:
            import statistics
            argv=observed_window['launch']['argv'];expected_spec='none' if arm=='A' else 'draft-mtp'
            assert argv[argv.index('--spec-type')+1]==expected_spec
            assert observed_window['launch']['native_request_options']==p['native_recipe']['request_options']
            start,end=observed_window['start_ns'],observed_window['end_ns']
            assert start<=selected[0]['start_ns']<selected[-1]['end_ns']<=end
            observed=[v for v in telemetry if start<=v['at_ns']<=end]
            hardware={'arm_including_setup_s':(end-start)/1e9,
                'peak_device_vram_mib':max(v['device_vram_bytes'] for v in observed)/2**20 if observed and all('device_vram_bytes' in v for v in observed) else None,
                'SM_clock_median_MHz':statistics.median(v['sm_clock_mhz'] for v in observed) if observed and all('sm_clock_mhz' in v for v in observed) else None,
                'memory_clock_MHz':sorted({v['mem_clock_mhz'] for v in observed}) if observed and all('mem_clock_mhz' in v for v in observed) else None,
                'max_temperature_C':max(v['temperature_c'] for v in observed) if observed and all('temperature_c' in v for v in observed) else None}
        result['arms'].append({'arm':arm,'engine_timings':engine_timings,'hardware_window':hardware,'MTP':'OFF' if arm=='A' else 'Q6 draft / max3 min1','tasks':len(selected),
                'solved':stored['solved'],'practical_solved':stored['practical_solved'],'protocol_valid':stored['protocol_valid'],
                'response_wall_s':wall,'completion_tokens':tokens,'GPU_counter_lower_j':energy['lower_j'],'GPU_counter_upper_j':energy['upper_j'],
                'GPU_j_per_success_lower':stored['GPU_j_per_success_lower'],'GPU_j_per_success_upper':stored['GPU_j_per_success_upper'],
                'original_scorer_replay_identical':True})
    if a['status']=='FRESH_TOOLS_AB400_COMPLETE':
        assert len(answers)==400 and all(v['tasks']==200 for v in result['arms']) and 0<a['task_phase_s']<=1200
        host=load(raw/'HOST_COMPLETION.json');gpu=load(raw/'AUDIT.json')
        assert host['status']=='GPU_COMPLETE_AUDITED' and host['audit_sha256']==digest(raw/'AUDIT.json') and gpu['one_shared_task_clock']
        x,y=a['profiles']['A'],a['profiles']['B'];g=load(ap.parent/'PREDECLARED_PLAN.json')['predeclared_gates']
        assert a['comparison']['response_latency_reduction']==1-y['response_wall_s']/x['response_wall_s']
        assert a['comparison']['GPU_j_per_success_reduction_conservative']==1-y['GPU_j_per_success_upper']/x['GPU_j_per_success_lower']
        expected_gates={'quality':y['solved']>=x['solved'] and y['solved']>=g['candidate_successes_minimum'],
            'protocol':y['protocol_valid']>=x['protocol_valid'],
            'latency':a['comparison']['response_latency_reduction']>=g['minimum_response_latency_reduction'],
            'energy':a['comparison']['GPU_j_per_success_reduction_conservative']>=g['minimum_GPU_j_per_success_reduction'],'all400':True}
        assert a['predeclared_gates']==expected_gates
        expected_decision='FRESH_TOOL_SPECIFIC_OBSERVED_GATES_PASS_NOT_ALLROUND_CHAMPION' if all(expected_gates.values()) else 'FRESH_TOOL_SPECIFIC_CONFIRMATION_GATE_FAILED'
        assert a['decision']==expected_decision
    else:
        assert a['decision']=='PARTIAL_NO_PROMOTION_NO_RETRY' and not a['predeclared_gates'] and not a['comparison']
    result['audit_id']=receipt(ap,entry['audit_sha256'])
    return result

def verified_native_lean_harness(root, summary, receipt):
    """Public aggregate projection after original capture + isolated replay checks."""
    root=pathlib.Path(root);ap=pathlib.Path(summary['audit_path']);assert digest(ap)==summary['audit_sha256'];a=load(ap)
    protocols={'jarvis-original-caveman-node-shrink-screen33-v1':('LEAN_HARNESS_SCREEN33_COMPLETE',33,0,('upstream-node-shrink-v1',)),'jarvis-original-caveman-toon-screen33-v1':('LEAN_HARNESS_SCREEN33_COMPLETE',33,0,('upstream-tool-toon-v1',)),'jarvis-original-miniswe-native-screen33-v1':('LEAN_HARNESS_SCREEN33_COMPLETE',33,0,('original-mini-swe-native-v1',)),'jarvis-lean-system-ablation33-v1':('LEAN_HARNESS_DEVELOPMENT66_COMPLETE',66,33,('reference','compact-system-v1')),'jarvis-lean-tool-json-ablation33-v1':('LEAN_HARNESS_DEVELOPMENT66_COMPLETE',66,33,('reference','compact-tool-json-v1')),'jarvis-lean-preaction-screen33-v1':('LEAN_HARNESS_SCREEN33_COMPLETE',33,0,('preaction-checklist-v1',))}
    assert a['dataset_id'] in protocols
    status,count,paired,arms=protocols[a['dataset_id']];screen=count==33
    assert a['status']==status and a['measurement_valid'] and a['GPU_execution_observed']
    assert a['paired_unique_cases']==paired and a['tasks']==a['case_executions']==count
    assert a['official_benchmark'] is False and a['winner_qualified'] is False
    rp=pathlib.Path(summary['independent_review_path']);assert digest(rp)==summary['independent_review_sha256']==a['independent_review_sha256'];review=load(rp)
    assert review['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and review['GPU_runs']==review['model_requests']==0
    result=review['result'];assert result['complete'] and result['scored_tasks']==count and result['solved']==a['solved'] and result['all_scores_and_effects_reproduced'] and result['real_evaluator_uid']!=0
    assert result['model_requests']==result['GPU_runs']==result['production_tool_actions']==0 and result['official_benchmark'] is False
    raw=pathlib.Path(a['raw_root']).resolve();assert raw.is_relative_to((root.parent/'research/mcp-workspace').resolve())
    assert all(digest(raw/n)==h for n,h in a['original_raw_files_sha256'].items())
    profile=load(raw/'profile.json');assert digest(raw/'profile.json')==a['profile_sha256']
    assert profile['assets'][profile['model']]==a['model_sha256']==result['model_artifact_sha256'] and load(raw/'LAUNCH.json')['uid']==65534
    completion=load(raw/'HOST_COMPLETION.json');assert completion['status']=='GPU_COMPLETE_AUDITED' and completion['audit_sha256']==digest(raw/'AUDIT.json')
    cp=pathlib.Path(review['CPU_receipt_file']);assert cp.parent==ap.parent and cp.name in {a['experiment_id'].lower()+'-protocol-file-identity-correction.receipt.json',a['experiment_id'].lower()+'-agent18-replay.receipt.json',a['experiment_id'].lower()+'-agent18-replay-permissions.receipt.json'}
    stdout=cp.with_name(cp.name.replace('.receipt.json','.stdout'));assert digest(cp)==review['CPU_receipt_sha256'] and digest(stdout)==review['CPU_stdout_sha256']
    cpu=load(cp);assert cpu['returncode']==0 and 'Result=success\n' in cpu['properties'] and 'ExecMainStatus=0\n' in cpu['properties'] and 'PrivateDevices=yes\n' in cpu['properties'] and 'NoNewPrivileges=yes\n' in cpu['properties']
    assert [json.loads(l.split(' ',1)[1]) for l in stdout.read_text().splitlines() if l.startswith('AGENT18_REPLAY_JSON ')]==[result]
    permission_fix=ap.parent/'CPU_REPLAY_PERMISSION_CORRECTION.json'
    if cp.name.endswith('-permissions.receipt.json'):
        fix=load(permission_fix)
        assert fix['kind']=='CPU_JAIL_MOUNTPOINT_PERMISSION_CORRECTION' and fix['GPU_reruns']==0 and fix['original_responses_or_scoring_changed'] is False
        assert fix['original_replay_plan_sha256']==digest(ap.parent/'CPU_REPLAY_PLAN.json')
        failed=ap.parent/(a['experiment_id'].lower()+'-agent18-replay.receipt.json')
        assert digest(failed)==fix['failed_CPU_receipt_sha256']
        assert 'ExecMainStatus=200\n' in load(failed)['properties']
    plan_path=ap.parent/'CPU_REPLAY_PLAN.json';plan=load(plan_path)
    assert plan['scorer_sha256']==review['scorer_sha256']
    assert digest(plan_path)==review['replay_plan_sha256'] and result['original_input_sha256']==plan['input_sha256']
    assert plan['input_sha256']['profile.json']==digest(raw/'profile.json') and plan['input_sha256']['responses.jsonl']==digest(raw/'HTTP_RESULTS.jsonl')
    assert plan['scorer_sha256'] in cpu['input_sha256'].values() and all(h in cpu['input_sha256'].values() for h in plan['input_sha256'].values())
    qp=pathlib.Path(summary['quality_review_path']);assert digest(qp)==summary['quality_review_sha256'];quality=load(qp)
    xp=pathlib.Path(summary['comparison_review_path']);assert digest(xp)==summary['comparison_review_sha256'];comparison=load(xp)
    records=[json.loads(l) for l in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()]
    telemetry=[json.loads(l) for l in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
    from leaderboard import counter_energy_bounds
    from lean_metrics import reviews
    if screen:
        ref_summary=load(root/'BENCHMARK_REFERENCES.json')['summary']['r587']
        ref_public=verified_native_lean_harness(root,ref_summary,receipt)
        assert ref_public['experiment_id']=='R587' and ref_public['model_sha256']==a['model_sha256']
        ref_audit=load(pathlib.Path(ref_summary['audit_path']));ref_raw=pathlib.Path(ref_audit['raw_root'])
        ref_profile=load(ref_raw/'profile.json')
        def inference_base(value):
            value=json.loads(json.dumps(value))
            for k in ('selected_task_inputs','execution_review','review','task_datasets'):value.pop(k,None)
            added=value['native_recipe']['harness_ablation']['module_assets']
            for k in added:value['assets'].pop(k)
            runtime_asset=value['native_recipe']['harness_ablation'].get('runtime_asset')
            if runtime_asset:
                assert runtime_asset['sha256']=='4b65354f98e563f0a3d6a2c21a5d5671eaac5a5ebac357fc58702904c6f544f4'
                assert value['assets'].pop(runtime_asset['path'])==runtime_asset['sha256']
            codec=value['native_recipe']['harness_ablation'].get('codec_asset')
            if codec:
                assert codec['sha256']=='80189ce6b009ea9fba762cdef88d568f20a8640fde4302f50a2cfcb36ab1d754' and value['assets'][codec['path']]==codec['sha256']
                value['assets'].pop(codec['path'])
            codecs=value['native_recipe']['harness_ablation'].get('codec_assets')
            if codecs:
                assert a['dataset_id']=='jarvis-original-caveman-node-shrink-screen33-v1' and len(codecs)==3
                expected={'/harness/caveman-node':'67ca5783febb8bf85736c79fcdd92c8d6d465a0eb2a082672bcdfa76a506751c','/harness/caveman-shrink.cjs':'87b89523c9466f7634b2f70dbaaa483648756e927127a4d11ba95f64003fde7f','/harness/caveman-shrink-request.cjs':'cb547fe1f29b5e3d7d6ef1e9b658c07d03519ae2c27c3050a74e9d6c489038b8'}
                assert {c['sandbox_path']:c['sha256']for c in codecs}==expected
                for c in codecs:
                    assert value['assets'].pop(c['path'])==c['sha256']
            value['native_recipe'].pop('harness_ablation');value['native_recipe'].pop('maximum_tasks')
            return json.dumps(value,sort_keys=True,separators=(',',':'))
        assert inference_base(profile)==inference_base(ref_profile)
        def original_cases(value,arm):
            rows=[]
            for c in value['selected_task_inputs']['cases']:
                if c['harness_arm']!=arm:continue
                c=json.loads(json.dumps(c));c['id']=c.pop('source_case_id');c.pop('harness_arm');rows.append(c)
            return json.dumps(rows,sort_keys=True,separators=(',',':'))
        assert original_cases(profile,arms[0])==original_cases(ref_profile,'reference')
        ref_quality=load(pathlib.Path(ref_summary['quality_review_path']))
        ref_records=[json.loads(l) for l in (ref_raw/'HTTP_RESULTS.jsonl').read_text().splitlines()]
        from lean_metrics import screen_reviews
        derived_quality,derived_comparison=screen_reviews(a,records,digest(ap),telemetry,counter_energy_bounds,ref_quality,ref_records,ref_summary['audit_sha256'],ref_summary['quality_review_sha256'])
        reference_data={'experiment_id':'R587','arm':'reference','audit_sha256':ref_summary['audit_sha256'],'quality_sha256':ref_summary['quality_review_sha256'],'metrics':next(r for r in ref_public['arms'] if r['arm']=='reference'),'new_GPU_runs':0,'fresh_contemporaneous_control':False}
    else:derived_quality,derived_comparison=reviews(a,records,digest(ap),telemetry,counter_energy_bounds,arms=arms)
    assert derived_quality==quality and derived_comparison==comparison
    assert len({r['id'] for r in records if r['kind']=='agent_case'})==count
    assert a['task_phase_s']<=a['task_limit_s']==1200 and a['model_starts']==1
    assert a['technical_request_errors']==a['technical_preflight_cases']==0
    # Explicit numeric allowlist: no prompts, entities, host paths or arbitrary metadata.
    allowed=('arm','completed_cases','planned_cases','complete','solved','policy_gate_passes','case_wall_s','response_wall_s','model_calls_attempted','request_errors','input_tokens_attempted','input_tokens_reported','completion_tokens_reported','reasoning_tokens_reported','total_tokens_reported','transform_cpu_s','transform_wall_s','tool_calls','policy_violations','rejected_calls','invalid_actions','peak_sampled_device_vram_mib','GPU_j_per_success_lower','GPU_j_per_success_upper','successful_tasks_per_s')
    changes=('decision','paired_gained','paired_lost','new_policy_failure_cases','token_reduction_percent','latency_reduction_percent','conservative_energy_per_success_reduction_percent','observed_quality_and_policy_gate')
    from lean_metrics import original_toon_overhead
    codec_overhead=original_toon_overhead(records) if a['dataset_id']=='jarvis-original-caveman-toon-screen33-v1' else None
    if a['dataset_id']=='jarvis-original-caveman-node-shrink-screen33-v1':
        from lean_metrics import original_node_shrink_overhead
        codec_overhead=original_node_shrink_overhead(records)
    return {'experiment_id':a['experiment_id'],'model':text(a['model']),'model_sha256':a['model_sha256'],'dataset_id':a['dataset_id'],'paired_unique_cases':paired,'case_executions':count,'screen_only':screen,**({'codec_overhead':codec_overhead} if codec_overhead is not None else {}),**({'stored_reference':reference_data} if screen else {}),'official_benchmark':False,'winner_qualified':False,'task_phase_s':a['task_phase_s'],
            'arms':[{k:r[k] for k in allowed} for r in quality['arms']], 'comparison':{k:comparison[k] for k in changes},
            'quality_audit_id':receipt(qp,summary['quality_review_sha256']),'independent_review_audit_id':receipt(rp,summary['independent_review_sha256']),'comparison_audit_id':receipt(xp,summary['comparison_review_sha256']),
            'correction_audit_id':receipt(permission_fix,digest(permission_fix)) if permission_fix.exists() else None,'implementation':{'transform_module_sha256':next(iter(profile['native_recipe']['harness_ablation']['module_assets'].values())),'engine_binary_sha256':profile['assets'][profile['runtime']+'/llama-server'],'transport_sha256':profile['native_recipe']['agent18']['transport_sha256'],'simulator_archive_sha256':profile['native_recipe']['agent18']['archive_sha256'],'source_commit':None,**({'upstream_repository':'https://github.com/JuliusBrussee/caveman','upstream_commit':'9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4','codec_binary_sha256':profile['native_recipe']['harness_ablation']['codec_asset']['sha256']} if a['dataset_id']=='jarvis-original-caveman-toon-screen33-v1' else {})},'profile_sha256':a['profile_sha256'],'scorer_sha256':review['scorer_sha256'],**({'upstream_Node_source':{'repository':'https://github.com/JuliusBrussee/caveman','commit':'9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4','license':'Apache-2.0','node_version':'24.22.0','artifacts':[{"name":pathlib.PurePosixPath(c['sandbox_path']).name,"sha256":c['sha256']}for c in profile['native_recipe']['harness_ablation']['codec_assets']]}}if a['dataset_id']=='jarvis-original-caveman-node-shrink-screen33-v1'else{}),'scope':quality['scope']}


def export_harness_sources(root,db,experiments):
    """Explicit lab-owned request adapters only; never privileged broker/runner code."""
    from validate import content_errors
    names={'R586':'system-prose.py','R587':'tool-json.py','R588':'preaction-checklist.py','R598':'original-toon-adapter.py','R600':'original-node-shrink-adapter.py'}
    for eid,name in names.items():
        row=experiments.get(eid,{})
        metrics=row.get('aggregate_metrics',{})
        result=metrics.get('native_lean_harness_ablation') or metrics.get('native_lean_harness_screen')
        if not result:continue
        summary=db['summary'][eid.lower()];audit=load(pathlib.Path(summary['audit_path']))
        profile=load(pathlib.Path(audit['raw_root'])/'profile.json')
        review_path=pathlib.Path(profile['execution_review']['file'])
        assert digest(review_path)==profile['execution_review']['sha256'];review=load(review_path)
        proof_path=pathlib.Path(review['lean_source_review_file'])
        assert digest(proof_path)==review['lean_source_review_sha256'];proof=load(proof_path)
        expected=result['implementation']['transform_module_sha256']
        choices=[x for x in proof['source_records'] if x['sha256']==expected and pathlib.Path(x['file']).suffix=='.py']
        assert choices,'Measured transform source not retained'
        source=pathlib.Path(choices[0]['file']);assert digest(source)==expected
        blob=source.read_bytes();assert not content_errors(blob.decode('utf-8'))
        import ast
        ast.parse(blob.decode('utf-8'))
        target=HERE/'docs/assets/harness'/name;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==blob,'Never overwrite historical transform source'
        else:target.write_bytes(blob);target.chmod(0o644)
        result['transform_source']={'file':'assets/harness/'+name,'sha256':expected,'license':'MIT','source_audit_id':row['audit_id'],'scope':'Exact lab-owned request transform; private task fixtures, responses, models and privileged execution code are excluded.'}
        if eid=='R600':
            wrapper_sha=next(c['sha256']for c in profile['native_recipe']['harness_ablation']['codec_assets']if c['sandbox_path']=='/harness/caveman-shrink-request.cjs')
            choices=[x for x in proof['source_records']if x['sha256']==wrapper_sha and pathlib.Path(x['file']).suffix=='.cjs']
            assert choices,'Original GPU request-wrapper source missing'
            wrapper=pathlib.Path(choices[0]['file']);blob=wrapper.read_bytes();assert digest(wrapper)==wrapper_sha and not content_errors(blob.decode())
            dest=HERE/'docs/assets/harness/original-node-shrink-request.cjs'
            if dest.exists():assert dest.read_bytes()==blob
            else:dest.write_bytes(blob)
            result['request_wrapper_source']={'file':'assets/harness/original-node-shrink-request.cjs','sha256':wrapper_sha,'license':'MIT'}



def verified_native_role_comparison(root, summary, receipt):
    """Public aggregate projection after original capture + isolated replay checks."""
    root=pathlib.Path(root);ap=pathlib.Path(summary['audit_path']);assert digest(ap)==summary['audit_sha256'];a=load(ap)
    assert a['status']=='DEVELOPMENT_ROLE_COMPARISON5_COMPLETE' and a['measurement_valid'] and a['GPU_execution_observed']
    assert a['dataset_id']=='jarvis-role-comparison-development5-v1' and a['paired_unique_cases']==5 and a['tasks']==a['case_executions']==15
    assert a['official_benchmark'] is False and a['winner_qualified'] is False
    rp=pathlib.Path(summary['independent_review_path']);assert digest(rp)==summary['independent_review_sha256']==a['independent_review_sha256'];review=load(rp)
    assert review['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and review['GPU_runs']==review['model_requests']==0
    result=review['result'];assert result['complete'] and result['scored_tasks']==15 and result['solved']==a['solved'] and result['all_scores_and_effects_reproduced'] and result['real_evaluator_uid']!=0
    assert result['model_requests']==result['GPU_runs']==result['production_tool_actions']==0 and result['official_benchmark'] is False
    raw=pathlib.Path(a['raw_root']).resolve();assert raw.is_relative_to((root.parent/'research/mcp-workspace').resolve())
    assert all(digest(raw/n)==h for n,h in a['original_raw_files_sha256'].items())
    profile=load(raw/'profile.json');assert digest(raw/'profile.json')==a['profile_sha256']
    assert profile['assets'][profile['model']]==a['model_sha256']==result['model_artifact_sha256'] and load(raw/'LAUNCH.json')['uid']==65534
    completion=load(raw/'HOST_COMPLETION.json');assert completion['status']=='GPU_COMPLETE_AUDITED' and completion['audit_sha256']==digest(raw/'AUDIT.json')
    cp=pathlib.Path(review['CPU_receipt_file']);assert cp.parent==ap.parent and cp.name in {a['experiment_id'].lower()+'-protocol-file-identity-correction.receipt.json',a['experiment_id'].lower()+'-agent18-replay.receipt.json'}
    stdout=cp.with_name(cp.name.replace('.receipt.json','.stdout'));assert digest(cp)==review['CPU_receipt_sha256'] and digest(stdout)==review['CPU_stdout_sha256']
    cpu=load(cp);assert cpu['returncode']==0 and 'Result=success\n' in cpu['properties'] and 'ExecMainStatus=0\n' in cpu['properties'] and 'PrivateDevices=yes\n' in cpu['properties'] and 'NoNewPrivileges=yes\n' in cpu['properties']
    assert [json.loads(l.split(' ',1)[1]) for l in stdout.read_text().splitlines() if l.startswith('AGENT18_REPLAY_JSON ')]==[result]
    correction=ap.parent/'CPU_SCORER_PROTOCOL_IDENTITY_CORRECTION.json'
    if correction.exists():
        fix=load(correction)
        assert fix['kind']=='REGISTERED_PROTOCOL_FILE_HASH_CPU_IDENTITY_CORRECTION' and fix['GPU_reruns']==0 and fix['original_replies_profiles_tasks_and_scoring_rules_changed'] is False
        plan_path=ap.parent/'CPU_SCORER_PROTOCOL_CORRECTED_PLAN.json';plan=load(plan_path);assert fix['corrected_scorer_sha256']==review['scorer_sha256']==plan['scorer_sha256']
        assert plan['input_sha256']['protocol.json']==fix['protocol_file_sha256']==profile['selected_task_inputs']['tools_sha256']
    else:
        plan_path=ap.parent/'CPU_REPLAY_PLAN.json';plan=load(plan_path);assert plan['scorer_sha256']==review['scorer_sha256'] and plan['input_sha256']['protocol.json']==profile['selected_task_inputs']['tools_sha256']
    assert digest(plan_path)==review['replay_plan_sha256'] and result['original_input_sha256']==plan['input_sha256']
    assert plan['input_sha256']['profile.json']==digest(raw/'profile.json') and plan['input_sha256']['responses.jsonl']==digest(raw/'HTTP_RESULTS.jsonl')
    assert plan['scorer_sha256'] in cpu['input_sha256'].values() and all(h in cpu['input_sha256'].values() for h in plan['input_sha256'].values())
    qp=pathlib.Path(summary['quality_review_path']);assert digest(qp)==summary['quality_review_sha256'];quality=load(qp)
    assert quality['source_audit_sha256']==digest(ap) and quality['paired_unique_cases']==5 and quality['case_executions']==15 and quality['official_benchmark'] is quality['winner_qualified'] is False
    records=[json.loads(l) for l in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];telemetry=[json.loads(l) for l in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
    cases=[r for r in records if r['kind']=='orchestration_case'];windows=[dict(id=r['arm'],start_ns=r['start_ns'],end_ns=r['end_ns']) for r in records if r['kind']=='orchestration_arm']
    assert len(cases)==15 and [x['id'] for x in windows]==['single','planner_worker','planner_worker_reviewer']
    from leaderboard import counter_energy_bounds
    assert [r['arm'] for r in quality['arms']]==[w['id'] for w in windows]
    for arm,window in zip(quality['arms'],windows):
        selected=[r for r in cases if r['arm']==arm['arm']];turns=[r for r in records if r['kind']=='agent_turn' and r['id'].startswith(arm['arm']+'--')]
        assert arm['complete'] and len(selected)==arm['completed_cases']==arm['planned_cases']==5
        assert sum(c['reported_result']['task_success'] for c in selected)==arm['solved']
        assert sum(c['reported_result']['policy_gate_pass'] for c in selected)==arm['policy_gate_passes']
        assert sum(c['reported_result']['task_scope_pass'] for c in selected)==arm['task_scope_passes']
        assert arm['arm_wall_s']==(window['end_ns']-window['start_ns'])/1e9 and arm['generation_requests']==len(turns)
        assert arm['completed_request_wall_s']==sum(r['e2e_s'] for r in turns)
        tokens=[r['reply'].get('usage',{}).get('completion_tokens') for r in turns]
        assert arm['completion_tokens_all_roles']==(sum(tokens) if tokens and all(type(v)is int and v>=0 for v in tokens) else None)
        energy=counter_energy_bounds(telemetry,windows,[arm['arm']]);assert energy==arm['GPU_counter']
        assert arm['gpu_j_per_success_lower']==(energy['lower_j']/arm['solved'] if arm['solved'] else None)
        assert arm['gpu_j_per_success_upper']==(energy['upper_j']/arm['solved'] if arm['solved'] else None)
        total=arm['completion_tokens_all_roles'];wall=arm['completed_request_wall_s']
        assert arm['tokens_s_completed_requests']==(total/wall if total is not None and wall else None)
        assert arm['successful_tasks_per_s']==arm['solved']/arm['arm_wall_s']
        memory=[r['device_vram_bytes']/2**20 for r in telemetry if r.get('nvml_begin_ns',r['at_ns'])>=window['start_ns'] and r['at_ns']<=window['end_ns'] and type(r.get('device_vram_bytes')) is int]
        assert arm['peak_sampled_device_vram_mib']==(max(memory) if memory else None)
        assert arm['technical_request_errors']==arm['technical_preflight_cases']==0
    comparison_path=pathlib.Path(summary['comparison_review_path']);assert digest(comparison_path)==summary['comparison_review_sha256'];comparison=load(comparison_path)
    assert comparison['candidate_audit_sha256']==digest(ap) and comparison['official_benchmark'] is comparison['winner_qualified'] is False
    base=[c for c in cases if c['arm']=='single'];paired=[]
    for name in ('planner_worker','planner_worker_reviewer'):
        candidate=[c for c in cases if c['arm']==name]
        assert [c['source_case_id'] for c in base]==[c['source_case_id'] for c in candidate]
        gained=sum(not a['reported_result']['task_success'] and b['reported_result']['task_success'] for a,b in zip(base,candidate))
        lost=sum(a['reported_result']['task_success'] and not b['reported_result']['task_success'] for a,b in zip(base,candidate))
        recorded=next(c for c in comparison['comparisons'] if c['candidate_arm']==name)
        assert recorded['comparable'] and recorded['paired_gained']==gained and recorded['paired_lost']==lost
        paired.append(dict(candidate_arm=name,paired_gained=gained,paired_lost=lost))
    allowed=('arm','complete','planned_cases','completed_cases','solved','policy_gate_passes','task_scope_passes','arm_wall_s','completion_tokens_all_roles','tokens_s_completed_requests','peak_sampled_device_vram_mib','successful_tasks_per_s','gpu_j_per_success_lower','gpu_j_per_success_upper','generation_requests','technical_request_errors','technical_preflight_cases')
    return {'experiment_id':a['experiment_id'],'model':text(a['model']),'model_sha256':a['model_sha256'],'dataset_id':a['dataset_id'],'paired_unique_cases':5,'case_executions':15,'official_benchmark':False,'winner_qualified':False,'arms':[{k:r[k] for k in allowed} for r in quality['arms']],
            'quality_audit_id':receipt(qp,summary['quality_review_sha256']),'independent_review_audit_id':receipt(rp,summary['independent_review_sha256']),'correction_audit_id':receipt(correction,digest(correction)) if correction.exists() else None,
            'retrospective':{**role_case_costs(records,telemetry),'source_identities':{'coordinator_sha256':profile['native_recipe']['orchestration']['module_sha256'],'transport_sha256':profile['native_recipe']['agent18']['transport_sha256'],'fixture_archive_sha256':profile['native_recipe']['agent18']['archive_sha256'],'independent_scorer_sha256':review['scorer_sha256'],'engine_binary_sha256':profile['assets'][profile['runtime']+'/llama-server'],'source_git_commit':None}},
            'paired_changes':paired,'scope':'Five exposed development tasks paired across three fixed-order harness arms. All role costs included; no official benchmark, population ranking, independent model inference replay or Champion.'}


def project_lean_research(root,receipt):
    """Allowlisted decision/source review; CPU reviews never become GPU results."""
    root=pathlib.Path(root);db=load(root/'BENCHMARK_REFERENCES.json');base=root/'staging/model-comparison-preparation/agent-qualification';p=base/'LEAN_HARNESS_PLAN.json'
    if not p.exists():return None
    plan=load(p);techniques=[{k:text(row.get(k)) for k in ('technique','status','priority','evidence','scope','next')} for row in plan['technique_review']]
    sources=[]
    for section,folder,identity in [('paper_implementation_followup','what-does-a-harness-buy','ANALYSIS_SOURCE_IDENTITIES.json'),('caveman_engine_followup','caveman','ENGINE_SOURCE_IDENTITIES.json')]:
        item=plan.get(section)
        if not item:continue
        identities=load(base/'harness-issues-sources'/folder/identity)
        for record in identities:
            src=base/'harness-issues-sources'/folder/record['path'];assert digest(src)==record['sha256'] and record['commit']==item['commit']
            if record['executed'] is not False:
                assert folder=='caveman' and record['path']=='skills/caveman-compress/scripts/validate.py'
                cpu=load(base/'CAVEMAN_UPSTREAM_VALIDATOR_CPU_CONTRACTS.json')
                assert digest(base/'CAVEMAN_UPSTREAM_VALIDATOR_CPU_CONTRACTS.json')==record['CPU_evidence_sha256'] and cpu['source_sha256']==record['sha256'] and cpu['uid']!=0 and cpu['GPU_calls']==cpu['model_calls']==0 and len(cpu['cases'])==9
            payload=src.read_bytes();assert hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()==record['git_blob_sha1']
        sources.append({'repository':url(item['repository']),'commit':item['commit'],'status':text(item['status']),'license':text(item.get('license')),'mechanisms':[text(v) for v in item['verified_mechanisms']],'scope':text(item.get('scope') or item.get('decision')),'files':[{'file':r['path'],'sha256':r['sha256'],'git_blob_sha1':r['git_blob_sha1']} for r in identities]})
    scopes=[]
    for name in ('LEAN_SCREENING32_APPLICABILITY_REVIEW.json','LEAN_EXACT_DUPLICATE_CONTEXT_VERIFICATION.json','LEAN_STRUCTURAL_JSON_FEASIBILITY.json'):
        f=base/name;row=load(f);assert row.get('GPU_runs',row.get('GPU_calls'))==0 and row.get('new_model_requests',row.get('model_requests')) in (None,0)
        scopes.append({'review_sha256':digest(f),'review_name':name,'scope':text(row['scope']),'GPU_runs':0,'model_requests':row.get('new_model_requests',row.get('model_requests')),'counts':projection(row.get('counts',{})),'profiles':[{'experiment_id':r['experiment_id'],'counts':projection(r['counts'])} for r in row.get('profiles',[])]})
    reference=None;pointer=load(pathlib.Path(root)/'BENCHMARK_REFERENCES.json').get('lean_harness_reference')
    if pointer:
        refpath=pathlib.Path(pointer['file']);assert digest(refpath)==pointer['sha256'];ref=load(refpath)
        assert ref['id']==pointer['id'] and all(row['optimized_harness_qualified'] is False for row in ref['profiles'])
        profiles=[]
        for row in ref['profiles']:
            audit=pathlib.Path(root)/'staging'/row['experiment_id'].lower()/'AUDIT.json';assert digest(audit)==row['audit_sha256'] and load(audit)['profile_sha256']==row['captured_profile_sha256']
            runtime=row['runtime_configuration'];request=runtime['request_options'];allowed={'cache_prompt','chat_template_kwargs','max_tokens','min_p','model','parallel_tool_calls','tool_choice','presence_penalty','repeat_penalty','return_tokens','seed','stream','temperature','top_k','top_p','verbose'}
            assert set(request)<=allowed
            profiles.append({'experiment_id':row['experiment_id'],'model':text(row['model']),'model_sha256':row['model_sha256'],'captured_profile_sha256':row['captured_profile_sha256'],'audit_sha256':row['audit_sha256'],'context_tokens':runtime['context'],'request_options':request,'engine_binary_sha256':runtime['engine_binary_sha256'],'template_sha256':runtime['template_sha256'],'transport_sha256':runtime['transport_sha256'],'optimized_harness_qualified':False})
        reference={'id':ref['id'],'status':ref['status'],'reference_sha256':digest(refpath),'source_files_sha256':ref['source_files_sha256'],'profiles':profiles,'budgets':ref['budgets'],'limits':[text(v) for v in ref['limits']],'next_goal_boundary':text(ref['next_goal_boundary'])}
    screening_rows=[]
    for current_experiment in ('R592','R593'):
        f=pathlib.Path(root)/'staging'/current_experiment.lower()/'HARNESS_COMPARISON.json'
        if not f.exists():continue
        comparison=load(f);assert comparison['official_benchmark'] is comparison['winner_qualified'] is False and comparison['request_preservation_checks']==32
        for original in comparison['source_records']:
            experiment=original['experiment_id'];assert experiment in ('R515',current_experiment)
            audit=pathlib.Path(root)/'staging'/experiment.lower()/'AUDIT.json';assert digest(audit)==original['audit_sha256']
            replay=audit.with_name('INDEPENDENT_REVIEW.json');assert digest(replay)==original['independent_review_sha256']
            raw=pathlib.Path(load(audit)['raw_root'])
            for name,h in original['raw_files_sha256'].items():assert digest(raw/name)==h
        for file,h in comparison['source_sha256'].items():assert digest(pathlib.Path(file))==h
        fields=('input_tokens','completion_tokens','reasoning_tokens','total_tokens','model_calls_completed','response_wall_s','task_wall_s','peak_device_vram_mib','successes','GPU_j_per_success_lower','GPU_j_per_success_upper')
        screening={key:comparison[key] for key in ('experiment_id','reference_experiment_id','decision','categories','token_reduction_percent','task_latency_reduction_including_captured_transform_percent','conservative_GPU_j_per_success_reduction_percent','captured_host_transform_wall_s','transform_cpu_s','fresh_contemporaneous_control','official_benchmark','winner_qualified')}
        screening.update(comparison_sha256=digest(f),reference={k:comparison['reference'][k]for k in fields},candidate={k:comparison['candidate'][k]for k in fields},audit_sha256={x['experiment_id']:x['audit_sha256']for x in comparison['source_records']},scope='Exposed frozen16coding+16mocktool development; stored R515 control, one candidate B run. No fresh A/B or qualified improvement. Input+completion totals; reasoning not separately reported. Failed tasks included in energy numerator; load/warmup and CPU energy excluded.')
        screening['candidate_kind']='actual pinned upstream style skill' if current_experiment=='R593' else 'local preamble rewrite'
        screening_rows.append(screening)
    screening=next((r for r in screening_rows if r['experiment_id']=='R592'),None)
    upstream_cpu=None;cp=base/'CAVEMAN_UPSTREAM_VALIDATOR_CPU_CONTRACTS.json'
    if cp.exists():
        row=load(cp);assert row['uid']!=0 and row['GPU_calls']==row['model_calls']==0
        upstream_cpu={'status':'CPU_VERIFIED_STRUCTURAL_CHECKS_ONLY','commit':row['upstream_commit'],'source_url':url(row['source_url']),'source_sha256':row['source_sha256'],'evidence_sha256':digest(cp),'GPU_calls':0,'model_calls':0,'cases':[{'case':r['case'],'validator_accepts':r['validator_accepts']}for r in row['cases']],'scope':'Actual pinned upstream validator in an unprivileged private-network/private-device CPU sandbox. Synthetic fixtures only; compressor/provider not invoked. Structural checks are not semantic or authorization preservation proof.'}
    confirmation=None;cp=pathlib.Path(root)/'staging/r594/HARNESS_COMPARISON.json'
    if cp.exists():
        row=load(cp);audit_path=cp.with_name('AUDIT.json');audit=load(audit_path);raw=pathlib.Path(audit['raw_root'])
        assert digest(audit_path)==row['audit_sha256'] and digest(cp.with_name('INDEPENDENT_REVIEW.json'))==row['independent_review_sha256']
        assert audit['status']=='HARNESS_AB64_DEVELOPMENT_COMPLETE' and row['requests']==64 and row['unique_tasks']==32 and row['request_preservation_checks']==64
        assert row['winner_qualified'] is row['official_benchmark'] is row['independent_confirmation'] is False
        for name,h in row['raw_files_sha256'].items():assert digest(raw/name)==h
        for file,h in row['source_sha256'].items():assert digest(pathlib.Path(file))==h
        assert digest(cp.with_name('COMPILATION_CPU_REVIEW.json'))==row['compilation_review_sha256']
        reference_proof=load(cp.with_name('HARNESS_REFERENCE_PROVENANCE.json'));assert reference_proof['R594_comparison_sha256']==digest(cp)
        parent=pathlib.Path(root)/'staging/r515/AUDIT.json';assert digest(parent)==reference_proof['reference_audit_sha256'];pr=pathlib.Path(load(parent)['raw_root']);assert digest(pr/'profile.json')==reference_proof['reference_profile_sha256'] and digest(pr/'HTTP_RESULTS.jsonl')==reference_proof['reference_responses_sha256']
        keys=('experiment_id','reference_arm','candidate_arm','unique_tasks','requests','model_starts','fresh_contemporaneous_control','paired_GPU_execution','official_benchmark','winner_qualified','independent_confirmation','categories','token_reduction_percent','request_latency_reduction_percent','GPU_j_per_success_reduction_bounds_percent','energy_saving_confirmed_by_counter_bounds','shared_TASK_phase_s','shared_unallocated_TASK_overhead_s','decision','model_sha256','context')
        confirmation={k:row[k]for k in keys};profile=load(raw/'profile.json');request=profile['native_recipe']['request_options'];binary=str(pathlib.PurePosixPath(profile['runtime'])/'llama-server')
        fields=('completed','successes','input_tokens','completion_tokens','reasoning_tokens','total_tokens','model_calls_completed','response_wall_s','task_wall_s','peak_device_vram_mib','GPU_j_per_success_lower','GPU_j_per_success_upper')
        confirmation.update(arms={a:{k:v[k]for k in fields}for a,v in row['arms'].items()},comparison_sha256=digest(cp),audit_sha256=row['audit_sha256'],profile_sha256=row['captured_profile_sha256'],at_utc=audit['at_utc'],engine_binary_sha256=profile['assets'].get(binary),engine_release_version=None,request_options={k:request.get(k)for k in ('max_tokens','temperature','seed','chat_template_kwargs')},compilation_cpu_ns=row['compilation_review']['cpu_ns'],compilation_wall_ns=row['compilation_review']['wall_ns'],scope='Exposed16coding+16mock-tool development; one fresh balanced A/B, same frozen Omni model/engine/native template. Per-arm latency sums request E2E intervals; joint TASK/startup/compilation are not divided. Counter brackets are not confidence intervals. Not a general Agent33 gain or official score; unseen confirmation still required.')
    mini=None;cp=base/'MINISWE_NATIVE_REFERENCE_PARITY_CPU.json'
    if cp.exists():
        row=load(cp);assert row['uid']==65534 and row['cases']==33 and row['callbacks_replayed']==154 and len(row['boundary_controls'])==3
        assert row['GPU_calls']==row['new_language_model_calls']==0 and row['all_requests_scores_and_effects_match_capture'] is True
        assert digest(base/'mini_swe_native_bridge.py')==row['bridge_sha256'] and digest(base/'MINISWE_NATIVE_REFERENCE_PARITY_INPUT_HASHES.json')==row['input_manifest_sha256'] and digest(base/'MINISWE_NATIVE_REFERENCE_PARITY_CPU.log')==row['log_sha256']
        manifest=load(base/'MINISWE_NATIVE_REFERENCE_PARITY_INPUT_HASHES.json');original=base/'harness-issues-sources/mini-swe-agent/src/minisweagent/agents/default.py';assert digest(original)==manifest['shared_files']['source/minisweagent/agents/default.py']
        mini={'status':row['disposition'],'commit':row['upstream_commit'],'package_version':row['upstream_version'],'runtime':row['runtime'],'reference_cases':33,'archived_callbacks':154,'boundary_controls':row['boundary_controls'],'new_GPU_runs':0,'new_model_calls':0,'source_sha256':digest(original),'bridge_sha256':row['bridge_sha256'],'evidence_sha256':digest(cp),'baseline_CPU_seconds':row['baseline_CPU']['cpu_ns']/1e9,'controller_CPU_seconds':row['candidate_CPU']['cpu_ns']/1e9,'bootstrap_CPU_seconds':row['core_initialization_CPU']['cpu_ns']/1e9,'scope':'Original complete DefaultAgent and native context controller, unchanged frozen policy/world/scorer;33 archived R536 cases,154 requests and effects reproduced. Scripted reply replay only, not new model quality. Stock upstream shell/provider prompts are not evaluated. Fixed-order CPU timings are descriptive; no token/call reduction or GPU performance claim.'}
    mini_gpu=None;mini_summary=db['summary'].get('r601')
    if mini_summary:
        mini_gpu=verified_native_lean_harness(root,mini_summary,receipt)
        assert mini_gpu['experiment_id']=='R601' and mini_gpu['dataset_id']=='jarvis-original-miniswe-native-screen33-v1'
        assert mini_gpu['case_executions']==33 and mini_gpu['paired_unique_cases']==0
        audit=load(pathlib.Path(mini_summary['audit_path']));quality=load(pathlib.Path(mini_summary['quality_review_path']))
        assert audit['factor']=='M07' and audit['native_core']=='minisweagent.agents.default'
        assert audit['controller_setup']['upstream_version']=='2.4.6' and audit['controller_setup']['archive_sha256']=='4b65354f98e563f0a3d6a2c21a5d5671eaac5a5ebac357fc58702904c6f544f4'
        assert len(quality['arms'])==1 and quality['arms'][0]['arm']=='original-mini-swe-native-v1'
        stored_reference_metrics=mini_gpu['stored_reference']['metrics']
        candidate=mini_gpu['arms'][0]
        assert candidate['solved']==stored_reference_metrics['solved'] and candidate['input_tokens_reported']==stored_reference_metrics['input_tokens_reported'] and candidate['completion_tokens_reported']==stored_reference_metrics['completion_tokens_reported']
        mini_gpu.update(upstream_version=audit['controller_setup']['upstream_version'],upstream_commit='04d809ceab9df28f9adaed044884180159172930',controller_archive_sha256=audit['controller_setup']['archive_sha256'],reference={'experiment_id':'R587','arm':'reference','solved':stored_reference_metrics['solved'],'policy_gate_passes':stored_reference_metrics['policy_gate_passes'],'input_tokens':stored_reference_metrics['input_tokens_reported'],'completion_tokens':stored_reference_metrics['completion_tokens_reported'],'model_calls':stored_reference_metrics['model_calls_attempted'],'case_wall_s':stored_reference_metrics['case_wall_s'],'GPU_j_per_success_lower':stored_reference_metrics['GPU_j_per_success_lower'],'GPU_j_per_success_upper':stored_reference_metrics['GPU_j_per_success_upper']},candidate={'solved':candidate['solved'],'policy_gate_passes':candidate['policy_gate_passes'],'input_tokens':candidate['input_tokens_reported'],'completion_tokens':candidate['completion_tokens_reported'],'model_calls':candidate['model_calls_attempted'],'case_wall_s':candidate['case_wall_s'],'GPU_j_per_success_lower':candidate['GPU_j_per_success_lower'],'GPU_j_per_success_upper':candidate['GPU_j_per_success_upper'],'controller_parent_CPU_s':audit['controller_parent_CPU_s'],'peak_device_vram_mib':audit['peak_device_vram_mib']},scope='R601 is a B-only exposed33 development screen compared with the stored R587 original arm, not a fresh contemporaneous A/B or holdout. Original mini-SWE DefaultAgent owns the controller; frozen native model, prompts/backend, permission simulator and scorer remain. The measured token and call counts are unchanged; no practical efficiency benefit, causal claim or qualification. Candidate upper GPU-J/success bound is 0.0054% below the historical reference lower bound, a negligible non-paired counter delta.')
    proxy=None;cp=base/'CAVEMAN_ORIGINAL_PROXY_RECORD_CPU.json'
    if cp.exists():
        row=load(cp);assert row['status']=='CPU_VERIFIED_ORIGINAL_PROXY_RECORD_SYNTHETIC_ONLY'
        assert row['uid']==65534 and row['GPU_calls']==row['model_calls']==row['external_provider_calls']==0
        assert row['full_original_proxy'] is True and row['winner_qualified'] is row['official_benchmark'] is False
        for name,h in row['evidence_sha256'].items():assert pathlib.Path(name).name==name and digest(base/name)==h
        assert digest(base/'caveman_proxy_record_cpu.py')==row['source_sha256']
        checks={r['case']:r for r in row['checks']};assert set(checks)=={'plain','tools','stream','error','unauthorized','unknown_mount'}
        for name in ('plain','tools','stream','error'):assert checks[name]['request_bytes_identical'] is checks[name]['response_bytes_identical'] is True and checks[name]['upstream_calls']==1
        assert checks['unauthorized']['status']==401 and checks['unknown_mount']['status']==404
        assert checks['unauthorized']['upstream_calls']==checks['unknown_mount']['upstream_calls']==0
        review=row['source_build_review'];assert row['binary_sha256']==review['binary_sha256'] and row['source_sha256']==review['driver_sha256']
        proxy={'status':row['status'],'commit':row['upstream_commit'],'binary_sha256':row['binary_sha256'],'driver_sha256':row['source_sha256'],'evidence_sha256':digest(cp),'upstream_source_files_verified':row['upstream_source_files_verified'],'checks':[{k:r[k]for k in ('case','status','upstream_calls')}for r in row['checks']],'new_GPU_runs':0,'new_model_calls':0,'at_utc':row['at_utc'],'scope':'Full original upstream proxy, CGO disabled, unprivileged offline CPU sandbox. Synthetic local OpenAI-compatible endpoint only. Four forwarded request/response fixtures preserved byte-for-byte; unauthorized and unknown routes denied without forwarding. No native engine, Harmony/provider completeness, compression quality, token savings or GPU performance qualification.'}
    toon=None;cp=base/'CAVEMAN_ORIGINAL_TOON_CPU_TESTS.json'
    if cp.exists():
        row=load(cp);assert row['status']=='CPU_VERIFIED_ORIGINAL_TOON_UPSTREAM_TESTS_ONLY' and row['GPU_calls']==row['model_calls']==0
        assert row['fuzz_campaign_executed'] is row['CGO_enabled'] is False and len(set(row['tests_passed']))==9
        log=base/'CAVEMAN_ORIGINAL_TOON_CPU_TESTS.log';assert digest(log)==row['log_sha256']
        events=[]
        for line in log.read_text().splitlines():
            try:events.append(json.loads(line))
            except ValueError:pass
        assert not any(r.get('Action')=='fail' for r in events)
        assert [r['Test']for r in events if r.get('Action')=='pass' and r.get('Test')]==row['tests_passed']
        for name,h in row['source_sha256'].items():assert digest(base/'harness-issues-sources/caveman'/name)==h
        toon={'status':row['status'],'commit':row['commit'],'tests_passed':row['tests_passed'],'evidence_sha256':digest(cp),'log_sha256':row['log_sha256'],'new_GPU_runs':0,'new_model_calls':0,'fuzz_campaign_executed':False,'scope':'Nine unmodified upstream TOON tests in an offline unprivileged CPU sandbox. Structural roundtrip only; no model interpretation, compression-quality, token or GPU-efficiency qualification.'}
        critical_path=base/'CAVEMAN_TOON_CRITICAL_CPU.json'
        if critical_path.exists():
            c=load(critical_path);assert c['commit']==row['commit'] and c['original_core_source_sha256']==row['source_sha256']
            assert c['GPU_calls']==c['model_calls']==0 and c['actually_transformed']==len(c['roundtrip_cases'])==10 and c['ambiguous_invalid_inputs_rejected']==3
            assert digest(base/'caveman_toon_critical_cpu_test.go')==c['test_source_sha256'] and digest(base/'CAVEMAN_TOON_CRITICAL_CPU.log')==c['log_sha256']
            textlog=(base/'CAVEMAN_TOON_CRITICAL_CPU.log').read_text();assert 'actual transformed fixtures=10/10; ambiguous/invalid inputs rejected=3' in textlog
            toon['critical_data_contracts']={'roundtrip_cases':c['roundtrip_cases'],'actually_transformed':10,'invalid_rejected':3,'evidence_sha256':digest(critical_path),'test_source_sha256':c['test_source_sha256']}
    proxy_gpu=None;cp=pathlib.Path(root)/'staging/r596/HARNESS_COMPARISON.json'
    if cp.exists():
        row=load(cp);audit=load(cp.with_name('AUDIT.json'));raw=pathlib.Path(audit['raw_root'])
        assert digest(cp.with_name('AUDIT.json'))==row['audit_sha256'] and digest(cp.with_name('INDEPENDENT_REVIEW.json'))==row['independent_review_sha256']
        assert audit['status']=='CAVEMAN_RECORD_AB64_DEVELOPMENT_COMPLETE' and row['experiment_id']=='R596' and row['request_preservation_checks']==64
        assert row['winner_qualified'] is row['official_benchmark'] is row['compression_enabled'] is False and row['native_requests_preserved']is True
        for name,h in row['raw_files_sha256'].items():assert digest(raw/name)==h
        for name,h in row['source_sha256'].items():assert digest(pathlib.Path(name))==h
        assert digest(cp.with_name('COMPILATION_CPU_REVIEW.json'))==row['compilation_review_sha256']
        keys=('experiment_id','decision','categories','token_reduction_percent','request_latency_reduction_percent','GPU_j_per_success_reduction_bounds_percent','energy_saving_confirmed_by_counter_bounds','shared_TASK_phase_s','observed_task_judgments_unchanged','native_requests_preserved','compression_enabled','model_sha256','context','proxy_binary_sha256','proxy_commit','warmup_requests','warmup_input_tokens','warmup_completion_tokens','warmup_request_E2E_s','native_non_TASK_before_cleanup_s','scope')
        fields=('successes','total_tokens','input_tokens','completion_tokens','reasoning_tokens','response_wall_s','task_wall_s','GPU_j_per_success_lower','GPU_j_per_success_upper')
        proxy_gpu={k:row[k]for k in keys};profile=load(raw/'profile.json')
        proxy_gpu.update(arms={arm:{k:value[k]for k in fields}for arm,value in row['arms'].items()},at_utc=audit['at_utc'],audit_sha256=row['audit_sha256'],comparison_sha256=digest(cp),profile_sha256=row['captured_profile_sha256'],winner_qualified=False,official_benchmark=False,requests=64,unique_tasks=32,model_starts=1,run_peak_vram_mib=audit['peak_device_vram_mib'],request_options={k:profile['native_recipe']['request_options'].get(k)for k in ('max_tokens','temperature','seed','chat_template_kwargs')},engine_release_version=None,engine_binary_sha256=profile['assets'].get(profile['runtime']+'/llama-server'))
    preinference=None;cp=pathlib.Path(root)/'staging/r595/AUDIT.json'
    if cp.exists():
        row=load(cp);assert row['status']=='BLOCKED_BEFORE_MODEL_START_NO_TASK_PHASE' and row['measurement_valid']is row['GPU_execution_observed']is False
        assert row['GPU_inference_runs']==row['model_starts']==0 and row['TASK_phase_started']is False and row['winner_qualified']is False
        raw=pathlib.Path(row['raw_root'])
        for name,h in row['original_raw_files_sha256'].items():assert digest(raw/name)==h
        preinference={'experiment_id':'R595','status':row['status'],'GPU_job_starts':1,'GPU_inference_runs':0,'model_starts':0,'TASK_phase_started':False,'audit_sha256':digest(cp),'scope':'Lab adapter attempted a host-only dataset read inside the restricted jail before model launch. No model/Caveman quality or performance measurement. Failed attempt preserved; corrected implementation has separate source review and identity.'}
    fresh_reserve=None
    fresh_manifest=base/'LEAN_FRESH_VALIDATION_MANIFEST.json'
    if fresh_manifest.exists():
        frozen=load(fresh_manifest);assert frozen['status']=='FROZEN_BEFORE_ANY_TARGET_MODEL_RESPONSE' and frozen['GPU_runs']==frozen['model_requests']==0
        for name,h in frozen['files'].items():assert digest(base/name)==h
        assert digest(base/'lean_screening_preamble.py')==frozen['candidate_sha256']
        controls_path=base/'LEAN_FRESH_VALIDATION_CPU_CONTROLS.json';controls=load(controls_path)
        assert controls['status']=='FRESH16_REFERENCE_AND_NEGATIVE_CPU_CONTROLS_PASS_NOT_GPU_ADMITTED' and controls['GPU_calls']==controls['model_calls']==0 and controls['manifest_sha256']==digest(fresh_manifest)
        assert len(controls['checks'])==16 and all(c['reference_success'] and c['negative_rejected'] and c['R594_transform_changes_only_system_prose'] for c in controls['checks'])
        fresh_reserve={'status':'CPU_PREPARATION_NOT_AN_ADMISSION_RECORD','coding':8,'tools':8,'new_GPU_runs':0,'new_model_calls':0,'manifest_sha256':digest(fresh_manifest),'CPU_controls_sha256':digest(controls_path),'candidate_experiment':'R594','candidate_sha256':frozen['candidate_sha256'],'created_at_utc':frozen['created_at_utc'],'source_task_hashes':frozen['files'],'scope':'Fresh authored task instances, fixed before target responses; candidate was already frozen. Same broad capability families, author knows candidate, no blinded-author or population-independence claim. Existing scorer and original exposed reserve retained. Prompts/oracles withheld; no benchmark score or GPU admission.'}
    fresh_result=None
    cp=pathlib.Path(root)/'staging/r599/HARNESS_COMPARISON.json'
    if cp.exists():
        row=load(cp);audit_path=cp.with_name('AUDIT.json');audit=load(audit_path);raw=pathlib.Path(audit['raw_root'])
        assert audit['status']=='HARNESS_FRESH_AB32_VALIDATION_COMPLETE' and row['requests']==32 and row['unique_tasks']==16 and row['request_preservation_checks']==32
        assert row['winner_qualified'] is row['official_benchmark'] is row['independent_confirmation'] is False
        assert digest(audit_path)==row['audit_sha256'] and digest(cp.with_name('INDEPENDENT_REVIEW.json'))==row['independent_review_sha256']
        replay=load(cp.with_name('INDEPENDENT_REVIEW.json'));assert replay['replayed_requests']==32 and not replay['changed_judgments']
        assert digest(fresh_manifest)==row['validation_manifest_sha256']
        for name,h in row['raw_files_sha256'].items():assert digest(raw/name)==h
        for file,h in row['source_sha256'].items():assert digest(pathlib.Path(file))==h
        keys=('experiment_id','unique_tasks','requests','model_starts','categories','token_reduction_percent','request_latency_reduction_percent','GPU_j_per_success_reduction_bounds_percent','energy_saving_confirmed_by_counter_bounds','shared_TASK_phase_s','shared_unallocated_TASK_overhead_s','decision','model_sha256','context','winner_qualified','official_benchmark')
        fresh_result={k:row[k]for k in keys}
        fields=('completed','successes','input_tokens','completion_tokens','reasoning_tokens','total_tokens','model_calls_completed','response_wall_s','task_wall_s','peak_device_vram_mib','GPU_j_per_success_lower','GPU_j_per_success_upper')
        fresh_result.update(arms={arm:{k:v[k]for k in fields}for arm,v in row['arms'].items()},audit_sha256=digest(audit_path),comparison_sha256=digest(cp),independent_review_sha256=row['independent_review_sha256'],manifest_sha256=digest(fresh_manifest),at_utc=audit['at_utc'],scope='New8 coding+8 mock-tool instances,32 balanced requests; candidate-aware authorship, no blinded or population-independence claim. One unchanged resident model. Per-arm latency sums request intervals, not full TASK time. GPU-energy intervals are query-timing bounds, not confidence intervals. No official benchmark or adoption.')
    proxy_compress_cpu=None
    decision_path=base/'CAVEMAN_PROXY_COMPRESS_POLICY_DECISION_CPU.json'
    if decision_path.exists():
        row=load(decision_path);assert row['status']=='DEFERRED_EXACT_FROZEN_PROFILE_RECOVERY_AND_UPSTREAM_ACCOUNTING_REQUIRED' and row['GPU_calls']==row['model_calls']==0
        a_path=base/row['base_CPU_file'];b_path=base/row['policy_CPU_file']
        assert digest(a_path)==row['base_CPU_sha256'] and digest(b_path)==row['policy_CPU_sha256']
        a,b=load(a_path),load(b_path);assert a['binary_sha256']==b['binary_sha256']==row['binary_sha256'] and a['source_archived_responses_sha256']==b['source_archived_responses_sha256']
        assert a['GPU_calls']==a['model_calls']==b['GPU_calls']==b['model_calls']==0 and a['uid']!=0 and b['uid']!=0 and b['synthetic_payg_header_control']is True
        assert len(a['archived_requests'])==len(b['archived_requests'])==154
        assert [r['input_sha256']for r in a['archived_requests']]==[r['input_sha256']for r in b['archived_requests']]
        assert all(r['request_bytes_identical']and r['JSON_identical']for r in a['archived_requests'])
        assert all(r['messages_identical']and not r['tools_identical']and r['changed_JSON_paths']==['/tools/length']for r in b['archived_requests'])
        assert any(json.loads(line).get('mode')=='compress'for line in a['effective_mode_log_lines']) and any(json.loads(line).get('mode')=='compress'for line in b['effective_mode_log_lines'])
        checks={r['case']:r for r in b['checks']};assert checks['tools']['forwarded_tool_names']==['inspect','caveman_retrieve']
        error=checks['error'];assert error['upstream_calls']==2 and [r['JSON_changes']for r in error['forwarded_attempts']]==[['/tools'],[]]
        assert checks['unauthorized']['upstream_calls']==checks['unknown_mount']['upstream_calls']==0
        before_source=load(base/'CAVEMAN_PROXY_COMPRESS_CPU_POLICY_CONTROL_SOURCE.json');assert before_source['original_source_sha256']==a['source_sha256']==hashlib.sha256(before_source['original_probe_source_utf8'].encode()).hexdigest()
        assert digest(base/'caveman_proxy_compress_cpu.py')==b['source_sha256']
        proxy_compress_cpu={'status':row['status'],'upstream_commit':row['upstream_commit'],'binary_sha256':row['binary_sha256'],'evidence_sha256':digest(decision_path),'base_control_sha256':digest(a_path),'policy_control_sha256':digest(b_path),'archived_request_count':154,'base_byte_identical':154,'policy_changed_catalogs':154,'policy_changed_messages':0,'added_tool':'caveman_retrieve','429_forwarded_attempts':2,'unauthorized_forwarded':0,'new_GPU_runs':0,'new_model_calls':0,'native_quality_measured':False,'native_token_benefit_measured':False,'conditions_for_reopening':row['conditions_for_reopening'],'scope':'Same154 archived native request bodies, original upstream binary, isolated CPU-only synthetic HTTP endpoints. A synthetic API-key header is the single classification control, not a production credential or policy change. No MCP service. Default mode passes through; recovery path adds a tool and can retry. No native model-quality, token, latency or energy result; no broad engine/model incompatibility claim.'}
    schema_cpu=None
    schema_path=base/'CAVEMAN_TOOLSCHEMA_CURRENT_PROFILE_DECISION.json'
    if schema_path.exists():
        row=load(schema_path);assert row['status']=='CPU_CONTRACT_REJECTED_EXACT_DEFAULT_TOOLSCHEMA_PROFILE'
        assert row['GPU_calls']==row['model_calls']==0 and row['catalogs']==10 and row['changed_catalogs']==row['changed_catalogs_with_missing_critical_clauses']==8 and row['unchanged_catalogs']==2
        inspection=pathlib.Path(row['source_inspection_file']);assert inspection.parent==base and digest(inspection)==row['source_inspection_sha256'];observed=load(inspection)
        original=base/'CAVEMAN_TOOLSCHEMA_ORIGINAL_CPU.json';assert digest(original)==row['original_CPU_review_sha256']
        prior=load(original);assert observed['same_original_engine_outputs_as_prior_control'] is True
        assert [(r['input_sha256'],r['output_sha256']) for r in observed['checks']]==[(r['input_sha256'],r['output_sha256']) for r in prior['checks']]
        for r in row['critical_clause_review']:
            changes=observed['checks'][r['catalog_index']]['description_changes'];assert len(changes)==1
            change=changes[0];assert hashlib.sha256(change['before'].encode()).hexdigest()==r['description_before_sha256'] and hashlib.sha256(change['after'].encode()).hexdigest()==r['description_after_sha256']
            assert r['missing_critical_clauses'] and all(x in change['before'] and x not in change['after'] for x in r['missing_critical_clauses'])
        schema_cpu={'status':row['status'],'commit':row['original_commit'],'binary_sha256':row['original_binary_sha256'],'evidence_sha256':digest(schema_path),'inspection_sha256':digest(inspection),'catalogs':10,'changed_catalogs':8,'unchanged_catalogs':2,'new_GPU_runs':0,'new_model_calls':0,'native_token_benefit_measured':False,'critical_clause_review':[{k:r[k] for k in ('catalog_index','function','missing_critical_clauses','description_before_sha256','description_after_sha256')} for r in row['critical_clause_review']],'decision':'Exact default mode not admitted: observed schema reductions remove explicit execution, authorization, provenance or preview-state clauses. Restoring all changed descriptions leaves all ten current catalogs unchanged. This is a CPU contract exclusion, not a native model-quality or performance result; other modes remain separate.'}
    model_compress_cpu=None
    model_cpu_path=base/'CAVEMAN_MODEL_COMPRESS_ORIGINAL_CPU.json'
    if model_cpu_path.exists():
        row=load(model_cpu_path)
        assert row['status']=='ORIGINAL_MODEL_COMPRESSION_ORCHESTRATOR_CPU_PROTOCOL_VERIFIED_ADDITIONAL_SAFETY_GATE_REQUIRED'
        assert row['GPU_calls']==row['model_calls']==0 and row['uid']==65534 and row['synthetic_HTTP_calls']==10 and len(row['checks'])==8
        assert all(r['passed'] is True for r in row['checks']) and sum(r['synthetic_HTTP_calls'] for r in row['checks'])==10
        assert row['upstream_validator_accepts_unprotected_permission_and_numeric_changes'] is True and row['protected_block_roundtrip'] is True and row['upstream_request_has_explicit_output_limit'] is False
        for name,h in row['evidence_sha256'].items():assert digest(base/name)==h
        log=load(base/'CAVEMAN_MODEL_COMPRESS_ORIGINAL_CPU.log')
        for key in ('checks','source_sha256','GPU_calls','model_calls','synthetic_HTTP_calls','uid'):assert log[key]==row[key]
        source_index={r['path']:r for r in load(base/'harness-issues-sources/caveman/ENGINE_SOURCE_IDENTITIES.json')}
        for name in ('compress.py','detect.py','validate.py'):
            record=source_index['skills/caveman-compress/scripts/'+name]
            assert record['commit']==row['commit'] and record['sha256']==row['source_sha256'][name]
        census=row['frozen_Agent33_payload_census'];a=load(pathlib.Path(root)/'staging/r536/AUDIT.json')
        assert census['responses_sha256']==a['original_raw_files_sha256']['HTTP_RESULTS.jsonl']
        model_compress_cpu={'status':row['status'],'commit':row['commit'],'evidence_sha256':digest(model_cpu_path),'source_sha256':row['source_sha256'],'checks':[{k:r[k] for k in ('check','passed','synthetic_HTTP_calls','compression_accepted')} for r in row['checks']],'synthetic_HTTP_calls':10,'new_GPU_runs':0,'new_model_calls':0,'source_url':'https://github.com/JuliusBrussee/caveman/blob/'+row['commit']+'/skills/caveman-compress/scripts/compress.py','critical_unprotected_changes_accepted':True,'protected_blocks_preserved':True,'explicit_provider_output_bound':False,'scope':'Actual original file orchestration and local HTTP transport, scripted synthetic replies only. No model quality, GPU efficiency or admission. Structural validation is insufficient for critical prose; explicit local output/runtime bounds and full call accounting remain required.','frozen_payload_census':{k:census[k] for k in ('source_experiment','responses_sha256','tool_history_occurrences','unique_tool_contents','unique_content_formats','tool_description_occurrences','unique_tool_descriptions','maximum_description_characters')}}
    toon_failure=None
    failure_path=pathlib.Path(root)/'staging/r597/AUDIT.json'
    if failure_path.exists():
        failure=load(failure_path);assert failure['status']=='FAILED_AFTER_MODEL_LOAD_BEFORE_TASK_NO_REQUESTS'
        assert failure['measurement_valid'] is False and failure['TASK_phase_started'] is False and failure['generation_requests']==failure['completed_requests']==0 and failure['model_starts']==1
        failure_raw=pathlib.Path(failure['raw_root']);assert failure_raw.resolve().is_relative_to((pathlib.Path(root).parent/'research/mcp-workspace').resolve())
        assert all(digest(failure_raw/n)==h for n,h in failure['original_raw_files_sha256'].items())
        assert (failure_raw/'HTTP_RESULTS.jsonl').stat().st_size==0
        samples=[json.loads(line) for line in (failure_raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
        assert len(samples)==failure['telemetry_samples'] and sum(bool(x['processes']) for x in samples)==failure['nonempty_GPU_process_samples']>0
        toon_failure={'experiment_id':'R597','status':failure['status'],'audit_sha256':digest(failure_path),'model_starts':1,'model_requests':0,'TASK_phase_started':False,'telemetry_samples':len(samples),'GPU_process_samples':failure['nonempty_GPU_process_samples'],'peak_device_vram_mib':failure['peak_device_vram_mib'],'official_benchmark':False,'winner_qualified':False,'quality_score':None,'task_latency_s':None,'task_energy_j':None,'cause':'Inner simulator clone rejected the candidate dataset; CPU fixture had retained the parent dataset. Separate CPU codec mount hit a host/CT path mismatch. No candidate response or quality measurement.'}
    return {'caveman_proxy_compress_CPU':proxy_compress_cpu,'fresh_harness_validation_GPU':fresh_result,'fresh_harness_validation_reserve':fresh_reserve,'caveman_schema_CPU':schema_cpu,'caveman_model_assisted_CPU':model_compress_cpu,'caveman_toon_pretask_failure':toon_failure,'caveman_preinference_failure':preinference,'caveman_proxy_record_GPU':proxy_gpu,'caveman_original_toon_CPU':toon,'caveman_proxy_record_CPU':proxy,'confirmation64':confirmation,'mini_swe_native_CPU':mini,'mini_swe_native_GPU':mini_gpu,'screening32_runs':screening_rows,'upstream_validator_CPU':upstream_cpu,'screening32':screening,'schema':1,'frozen_reference':reference,'canonical_plan_sha256':digest(p),'recommendation':'RETAIN_MEASURED_MINIMAL_REFERENCE_NO_QUALIFIED_ALTERNATIVE','official_benchmark':False,'new_factor_coverage':0,'techniques':techniques,'source_reviews':sources,'CPU_applicability':scopes,'limits':'Scoped tested alternatives and bounded technical reviews, not an exhaustive proof of globally optimal harness behavior. Deferred codecs/proxies have no local performance qualification.'}

def reserved_validation_work(records):
    """Count actual retained response usage; missing instrumentation stays null."""
    turns=[r for r in records if r['kind']=='agent_turn'];cases=[r for r in records if r['kind']=='agent_case']
    def measured_sum(values):return sum(values) if values and all(type(v)is int and v>=0 for v in values) else None
    inputs=measured_sum([r['reply'].get('usage',{}).get('prompt_tokens') for r in turns]);outputs=measured_sum([r['reply'].get('usage',{}).get('completion_tokens') for r in turns])
    work={'input_tokens':inputs,'output_tokens':outputs,'reasoning_tokens':measured_sum([r['reply'].get('usage',{}).get('completion_tokens_details',{}).get('reasoning_tokens') for r in turns]),'input_output_tokens':inputs+outputs if inputs is not None and outputs is not None else None,'completed_model_calls':len(turns),'policy_violations':measured_sum([c['reported_result'].get('policy_violations') for c in cases]),'rejected_calls':measured_sum([c['reported_result'].get('rejected_calls') for c in cases]),'tool_calls':measured_sum([c['reported_result'].get('total_tool_calls') for c in cases])}
    return {'measured_work':work}

def verified_native_agent_development(root, summary, receipt):
    """Verify original capture and isolated replay before public development costs."""
    root=pathlib.Path(root);ap=pathlib.Path(summary['audit_path']);assert digest(ap)==summary['audit_sha256'];a=load(ap)
    rp=pathlib.Path(summary['independent_review_path']);assert digest(rp)==summary['independent_review_sha256']==a['independent_review_sha256'];review=load(rp)
    assert review['status']=='INDEPENDENT_CPU_REPLAY_IDENTICAL' and review['GPU_runs']==review['model_requests']==0
    result=review['result'];assert result['real_evaluator_uid']!=0 and result['model_requests']==result['GPU_runs']==result['production_tool_actions']==0 and result['official_benchmark'] is False
    assert result['scored_tasks']==a['tasks'] and result['solved']==a['solved'] and result['all_scores_and_effects_reproduced']
    raw=pathlib.Path(a['raw_root']).resolve();assert raw.is_relative_to((root.parent/'research/mcp-workspace').resolve())
    assert all(digest(raw/n)==h for n,h in a['original_raw_files_sha256'].items())
    assert digest(raw/'profile.json')==a['profile_sha256'] and load(raw/'LAUNCH.json')['uid']==65534
    profile=load(raw/'profile.json');assert profile['assets'][profile['model']]==a['model_sha256']==result['model_artifact_sha256']
    cp=pathlib.Path(review.get('CPU_receipt_file',rp.parent/(a['experiment_id'].lower()+'-agent18-replay.receipt.json')))
    assert cp.parent==rp.parent and cp.name in {a['experiment_id'].lower()+'-agent18-replay.receipt.json',a['experiment_id'].lower()+'-scorer-order-correction.receipt.json'}
    stdout=cp.with_name(cp.name.replace('.receipt.json','.stdout'))
    assert digest(cp)==review['CPU_receipt_sha256'] and digest(stdout)==review['CPU_stdout_sha256'];cpu=load(cp)
    assert cpu['returncode']==0 and 'Result=success\n' in cpu['properties'] and 'ExecMainStatus=0\n' in cpu['properties']
    observed=[json.loads(l.split(' ',1)[1]) for l in stdout.read_text().splitlines() if l.startswith('AGENT18_REPLAY_JSON ')];assert observed==[result]
    reserved=a.get('dataset_id')=='jarvis-lean-holdout-20261027-v1'
    validation33=a.get('dataset_id')=='jarvis-agent-validation-20261025-v1' or reserved
    if a['status'] in ('DEVELOPMENT_AGENT18_COMPLETE','VALIDATION33_COMPLETE','LEAN_RESERVED_VALIDATION33_COMPLETE'):
        assert result['complete'] and result['cases']==(33 if validation33 else 18)
        completion=load(raw/'HOST_COMPLETION.json');assert completion['status']=='GPU_COMPLETE_AUDITED' and completion['audit_sha256']==digest(raw/'AUDIT.json')
    from leaderboard import counter_energy_bounds
    records=[json.loads(l) for l in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()];cases=[r for r in records if r['kind']=='agent_case'];telemetry=[json.loads(l) for l in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
    assert len(cases)==a['tasks'] and sum(c['reported_result']['task_success'] for c in cases)==a['solved']
    assert counter_energy_bounds(telemetry,cases,[c['id'] for c in cases])==a['GPU_counter']
    if validation33:
        frozen_path=root/'staging/model-comparison-preparation/agent-qualification'/('LEAN_HOLDOUT_TASKS.json' if reserved else 'PRIVATE_VALIDATION33.json')
        assert digest(frozen_path)==('c25de56c9629584ea22f0aae2b07ad81fadc09ff0b6205eb58c72bb305c96122' if reserved else 'acd45c1b43c2cebb1f9453707a76954275bf9810f2344e50e3707a654ed26b65')
        frozen=load(frozen_path)
        assert profile['selected_task_inputs']['dataset']==a['dataset_id'] and profile['selected_task_inputs']['cases']==frozen['cases']
        assert [c['id'] for c in cases]==[c['id'] for c in frozen['cases']][:len(cases)]
    m=metrics(a)['native_lean_reserved_validation33' if reserved else 'native_validation33' if validation33 else 'native_agent18_development'];m['independent_review_audit_id']=receipt(rp,summary['independent_review_sha256'])
    m['context_tokens']=profile['native_recipe']['context'];m['max_output_tokens']=profile['native_recipe']['request_options']['max_tokens'];m['bridge_source_sha256']=profile['native_recipe']['agent18']['transport_sha256']
    if validation33:
        if len(cases)==33:
            m.update(agent_policy_counts(cases));m['quality_diagnostics']=agent_quality_diagnostics(cases)
        elif reserved:
            assert all(type(c['reported_result'].get(k)) is bool for c in cases for k in ('policy_gate_pass','task_scope_pass'))
            m.update(policy_gate_passes=sum(c['reported_result']['policy_gate_pass'] for c in cases),task_scope_passes=sum(c['reported_result']['task_scope_pass'] for c in cases))
        else:raise AssertionError('Historical validation projection requires original complete33 capture')
    if reserved:
        plan=load(ap.parent/'CAMPAIGN_PLAN.json');assert digest(ap.parent/'CAMPAIGN_PLAN.json')==a['campaign_plan_sha256']
        assert plan['independent_holdout'] is (False if a['experiment_id']=='R625' else True) and plan['family_independent'] is False and plan['no_retuning_on_reserved_replies'] is True
        assert plan['holdout_plan_sha256']=='627675b304d7252b6e8136606dd83cb798559bfa7b544a40ac05b65c2987792a'
        assert digest(root/'staging/model-comparison-preparation/agent-qualification/LEAN_HOLDOUT_PLAN.json')==plan['holdout_plan_sha256']
        execution=load(pathlib.Path(profile['execution_review']['file']));assert digest(pathlib.Path(profile['execution_review']['file']))==profile['execution_review']['sha256']
        parent_path=pathlib.Path(execution['parent_model_snapshot_file']);parent=load(parent_path);assert digest(parent_path)==execution['parent_model_snapshot_sha256']
        pins={'a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052':'e8d6305a50fe0a2522475070c90e25dfbc373be7eba029870941c26a705d2973','b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c':'c1a06cb4be35d758d43a3a6056b0ab2bb4f5e2d1d197741ded1c43c6f4d54d1d','93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b':'40c9726c13614e7eb6a87a794e65c528bcddf5e32bef6bede930bb1ebc2bfb16'}
        if a['experiment_id']=='R618':pins['58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f']='20bf0fd11aae78ca8de25fcd600d6a4bd1e01ad18dd20e7ac6950be68e11ca73'
        if a['experiment_id']=='R625':pins['58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f']='855da15db648fbac7e74db7153dd2d0cc12a1e46bc6191705ceeb9ad27fc7c61'
        assert a['model_sha256'] in pins and digest(parent_path)==pins[a['model_sha256']]
        assert profile['native_recipe']['context']==8192 and profile['native_recipe']['agent18']['archive_sha256']=='1db8fe157575f6c69d169a9218a39702e6f900ea3717aa4072425199b080bed7'
        def native_identity(p):
            p=copy.deepcopy(p)
            for k in ('selected_task_inputs','review','execution_review','adapter','task_datasets','assets'):p.pop(k,None)
            for k in ('agent18','maximum_tasks','maximum_generation_requests','maximum_runtime_seconds','http_timeout_policy','preflight_all_inputs'):p['native_recipe'].pop(k,None)
            return p
        assert native_identity(profile)==native_identity(parent)
        m.update(reserved_validation_work(records),complete_capture=a['measurement_valid'] and a['tasks']==33,complete_inference=a['measurement_valid'] and a['tasks']==33 and a['technical_request_errors']==a['technical_preflight_cases']==0,family_independent=False,model_fixtures_unseen_at_freeze=plan['independent_holdout'],optimization_winner=False,profile_sha256=a['profile_sha256'],parent_profile_sha256=digest(parent_path),model_sha256=a['model_sha256'],scorer_sha256=review['scorer_sha256'],dataset_id=a['dataset_id'])
        domain_by_id={c['id']:c['task']['domain'] for c in frozen['cases']};domain_results={}
        for c in cases:
            domain=domain_by_id[c['id']];assert domain in ('code','ha','pve','poke','pal','astra');counts=domain_results.setdefault(domain,{'cases':0,'solved':0,'policy_gate_passes':0,'policy_violation_events':0})
            counts['cases']+=1;counts['solved']+=c['reported_result']['task_success'];counts['policy_gate_passes']+=c['reported_result']['policy_gate_pass'];counts['policy_violation_events']+=c['reported_result']['policy_violations']
        limits=[]
        for row in records:
            if row['kind']!='agent_preflight_error':continue
            assert row['reason'] in ('CONTEXT_BUDGET','TOKENIZER_FORMAT','API_PREFLIGHT_ERROR')
            ids=row.get('prompt_token_ids');count=len(ids) if isinstance(ids,list) and all(type(t)is int and t>=0 for t in ids) else None;maximum=row['request'].get('max_tokens')
            if row['reason']=='CONTEXT_BUDGET':assert count is not None and type(maximum)is int and count+maximum>profile['native_recipe']['context']
            limits.append({'domain':domain_by_id[row['case_id']],'turn':row['turn'],'reason':row['reason'],'prompt_tokens':count,'max_output_tokens':maximum,'context_tokens':profile['native_recipe']['context']})
        m['domain_results']=domain_results;m['preflight_limits']=limits
        qpath=ap.parent/'QUALITY_REVIEW.json';q=load(qpath);assert q['source_audit_sha256']==digest(ap) and q['measured_work']==m['measured_work']
        m['quality_audit_id']=receipt(qpath,digest(qpath));m['implementation']={'engine_binary_sha256':profile['assets'][profile['runtime']+'/llama-server'],'template_sha256':profile['assets'][profile['chat_template']],'transport_sha256':profile['native_recipe']['agent18']['transport_sha256'],'simulator_archive_sha256':profile['native_recipe']['agent18']['archive_sha256'],'source_commit':None}
    if validation33 and summary.get('replay_order_correction_path'):
        correction=pathlib.Path(summary['replay_order_correction_path']);assert digest(correction)==summary['replay_order_correction_sha256']
        document=load(correction);assert document['kind']=='CAPTURED_FIXTURE_ORDER_CPU_REPLAY_CORRECTION' and document['GPU_reruns']==0
        assert document['corrected_CPU_receipt_sha256']==digest(cp) and document['tasks_replayed']==a['tasks'] and document['solved']==a['solved']
        m['evaluation_correction_audit_id']=receipt(correction,summary['replay_order_correction_sha256'])
    if validation33 and summary.get('comparison_review_path'):
        comparison_path=pathlib.Path(summary['comparison_review_path']);assert digest(comparison_path)==summary['comparison_review_sha256']
        comparison=load(comparison_path);assert comparison['candidate_audit_sha256']==summary['audit_sha256']
        reference_id=comparison.get('reference_experiment_id')
        if reference_id is not None:
            assert re.fullmatch(r'R[1-9][0-9]{1,3}',reference_id)
            reference_path=root/'staging'/reference_id.lower()/'AUDIT.json';assert digest(reference_path)==comparison['reference_audit_sha256']
            reference=load(reference_path);assert reference['measurement_valid'] and reference['dataset_id']==a['dataset_id'] and reference['tasks']==33
            previous=pathlib.Path(reference['raw_root'])/'HTTP_RESULTS.jsonl'
            assert digest(previous)==reference['original_raw_files_sha256']['HTTP_RESULTS.jsonl']
            previous_cases=[row for row in map(json.loads,previous.read_text().splitlines()) if row['kind']=='agent_case']
            groups={c['id']:c['case']['generalization_group'] for c in frozen['cases']}
            paired=validation33_pairing(previous_cases,cases,groups)
            assert all(comparison['quality'][k]==v for k,v in paired.items())
            m['paired_validation']={**paired,'reference_experiment_id':reference_id,'scope':'Descriptive paired sensitivity on frozen authored families, not population superiority.'}
    return m

def validation33_pairing(reference,candidate,groups):
    """Recount pairs and verify the producer's enumeration with integer DP."""
    ids=[c['id'] for c in reference]
    assert ids and len(set(ids))==len(ids) and ids==[c['id'] for c in candidate] and set(ids)==set(groups)
    differences=collections.Counter({g:0 for g in groups.values()});gained=lost=0
    for old,new in zip(reference,candidate):
        a=old['reported_result']['task_success'];b=new['reported_result']['task_success']
        assert type(a) is bool and type(b) is bool
        gained+=not a and b;lost+=a and not b;differences[groups[old['id']]]+=int(b)-int(a)
    return {'tasks':len(ids),'frozen_groups':len(differences),'nonzero_groups':sum(v!=0 for v in differences.values()),
            'case_gained':gained,'case_lost':lost,'net_success_change':gained-lost,
            'group_sign_flip_two_sided_p':grouped_sign_probability(list(differences.values()))}

def grouped_sign_probability(differences):
    """Independent integer-distribution verifier for paired group sign flips."""
    counts={0:1}
    for delta in differences:
        assert type(delta) is int
        if not delta:continue
        next_counts=collections.Counter()
        for total,count in counts.items():next_counts[total+delta]+=count;next_counts[total-delta]+=count
        counts=dict(next_counts)
    observed=abs(sum(differences));return sum(n for total,n in counts.items() if abs(total)>=observed)/sum(counts.values())

def verify_native_grouped_review(root,document,summary):
    root=pathlib.Path(root);audits=document['source_audit_sha256_by_experiment'];cases={};groups=None;inputs=None
    for eid,expected in audits.items():
        assert re.fullmatch('R[1-9][0-9]{1,3}',eid) and summary[eid.lower()]['audit_sha256']==expected
        ap=root/'staging'/eid.lower()/'AUDIT.json';assert digest(ap)==expected;a=load(ap);assert a['measurement_valid'] and a['tasks']==18
        raw=pathlib.Path(a['raw_root']);assert raw.resolve().is_relative_to((root.parent/'research/mcp-workspace').resolve())
        assert digest(raw/'HTTP_RESULTS.jsonl')==a['original_raw_files_sha256']['HTTP_RESULTS.jsonl'] and digest(raw/'profile.json')==a['profile_sha256']
        profile=load(raw/'profile.json');current=profile['selected_task_inputs']
        if inputs is None:inputs=current;groups={e['id']:e['case']['generalization_group'] for e in current['cases']}
        else:assert current==inputs
        cases[eid]=[x for x in map(json.loads,(raw/'HTTP_RESULTS.jsonl').read_text().splitlines()) if x['kind']=='agent_case']
        assert len(cases[eid])==18 and [r['id'] for r in cases[eid]]==list(groups)
        model=document['models'][eid]
        assert all(model[k]==v for k,v in [('audit_sha256',expected),('solved',a['solved']),('tasks',18),('task_s',a['task_phase_s']),('peak_vram_mib',a['peak_device_vram_mib']),('GPU_j_per_success_lower',a['gpu_j_per_success_lower']),('GPU_j_per_success_upper',a['gpu_j_per_success_upper'])])
    assert document['quality']=={'frozen_tasks_per_model':18,'frozen_generalization_groups':len(set(groups.values())),'measured_model_profiles':len(cases)}
    reference=cases['R518']
    for eid,rows in cases.items():
        if eid=='R518':continue
        deltas=collections.Counter({g:0 for g in groups.values()});gained=lost=0
        for a,b in zip(reference,rows):
            x=a['reported_result']['task_success'];y=b['reported_result']['task_success'];assert type(x) is bool and type(y) is bool
            assert b['reported_result']['generalization_group']==groups[b['id']]
            deltas[groups[a['id']]]+=int(y)-int(x);gained+=not x and y;lost+=x and not y
        expected={'tasks':18,'frozen_groups':len(deltas),'nonzero_groups':sum(bool(x) for x in deltas.values()),'case_gained':gained,'case_lost':lost,'net_success_change':gained-lost,'group_sign_flip_two_sided_p':grouped_sign_probability(list(deltas.values()))}
        assert document['comparison'][eid]==expected
    assert document['official_benchmark'] is False and document['winner_qualified'] is False and document['GPU_runs']==document['model_requests']==0
    return True

def factor_assignment(summary):
    """A current correction controls the tested scope; original audit stays linked."""
    valid=lambda x:isinstance(x,str) and re.fullmatch(r'(?:R|K|C|H|Q|M|S|E|A|T|HBM|BMT)\d{2}',x)
    current=sorted({x for x in summary.get('axis_factors',[]) if valid(x)})
    old=summary.get('original_audit_factor_mapping',{})
    original=sorted({x for x in old.get('axis_factors',[]) if valid(x)})
    related=sorted({x for x in summary.get('related_factors_not_isolated_treatments',[]) if valid(x)}-set(current))
    return {'current_factor_ids':current,'original_audit_factor_ids':original,'related_context_factor_ids':related,'reason':text(summary.get('factor_mapping_correction',{}).get('reason'))}
def scope_reassessment(accountability):
    """Public rationale only; exclude local evidence paths and source payloads."""
    review=accountability.get('deferral_reassessment_20261022')
    if not isinstance(review,dict):return None
    allowed=('previous_status','current_status','priority','model_engine_compatibility','decision','next_action','expected_benefit')
    result={k:text(review[k]) for k in allowed if isinstance(review.get(k),str)}
    result['new_GPU_execution']=review.get('new_GPU_execution') is True
    return result
def snippets(obj):
    result={k:text(obj[k]) for k in ['decision','qualification','interpretation','hypothesis','research_question','scope','scope_correction','treatment_comparison','warmup_to_history_state','measurement_type','evidence_class','score_rule'] if isinstance(obj.get(k),str)}
    result.update({k:obj[k] for k in ['all_21_history_envelopes_match_R313','slot1_erase_confirmed_n_erased','slot0_snapshot_repeatability_at_all_3_boundaries','critical_response_matches_archived_R313_valid_envelope','data_leak_or_GDN_bug_proven','full_isolation_or_quality_qualification','speed_or_champion_claim'] if isinstance(obj.get(k),(bool,int))})
    targets=obj.get('history_slot_targets')
    if isinstance(targets,dict) and all(isinstance(targets.get(k),int) for k in ['slot0','slot1']) and isinstance(targets.get('ordinal_ranges'),str):
        result['history_slot_targets']={'slot0':targets['slot0'],'slot1':targets['slot1'],'ordinal_ranges':text(targets['ordinal_ranges'])}
    result.update({k:[text(x) for x in obj[k] if isinstance(x,str)] for k in ['limits','limitations'] if isinstance(obj.get(k),list)})
    return result
def write(name,obj):
    # Preserve the entire growing immutable history; formatting whitespace is
    # not research data. Keep the existing per-file publication limit intact.
    style={'separators':(',',':')} if name=='configuration-history.json' else {'indent':2}
    p=HERE/'data'/name;p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,sort_keys=True,allow_nan=False,**style)+'\n')
def main():
    arg=argparse.ArgumentParser();arg.add_argument('--source',required=True,type=pathlib.Path);args=arg.parse_args();root=args.source.resolve()
    for name in ['MATRIX.json','MATRIX_EXTENDED.json','QUEUE.json','BENCHMARK_REFERENCES.json','BENCHMARK_REGISTER.json','O2_EXPERIMENTS.jsonl']:
        if not (root/name).is_file(): raise ValueError('Missing canonical input: '+name)
    # Same existing project lock, short read-only snapshot; never interrupt an experiment.
    with (root/'source-handoff.lock').open('r') as lock:
        fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)
        originals=load(root/'MATRIX.json');matrix=load(root/'MATRIX_EXTENDED.json');db=load(root/'BENCHMARK_REFERENCES.json');ledger=(root/'O2_EXPERIMENTS.jsonl').read_text().splitlines()
        source_hashes={n:digest(root/n) for n in ['MATRIX.json','MATRIX_EXTENDED.json','QUEUE.json','BENCHMARK_REFERENCES.json','BENCHMARK_REGISTER.json','O2_EXPERIMENTS.jsonl']}
    catalog={};locations={};verified={};factor_links=collections.defaultdict(set)
    def receipt(path, expected=None):
        p=pathlib.Path(path)
        if not p.is_absolute():p=root/p
        p=p.resolve()
        if not p.is_relative_to(root.parent) or not p.is_file(): return None
        # Only known evidence metadata. Never read a log, script, model, or archive into the export.
        if p.suffix!='.json':return None
        h=digest(p)
        if expected and h!=expected:raise ValueError('Selected audit hash mismatch')
        eid='audit-'+h[:20]
        if eid not in catalog:
            try:a=load(p)
            except (ValueError,UnicodeError):return None
            if not isinstance(a,dict):return None
            catalog[eid]={'id':eid,'original_sha256':h,'original_bytes':p.stat().st_size,'original_filename':p.name if p.name in {'AUDIT.json','RESULTS.json','QUALIFICATION.json','INDEPENDENT_REVIEW.json','REFERENCE_ADMISSION.json'} else 'research-metadata.json','original_publicly_available':False,'excerpt_is_not_original':True,'statements':snippets(a),'aggregate_metrics':metrics(a)}
            locations[eid]=p
        catalog[eid]['original_pin_verified']=catalog[eid].get('original_pin_verified',False) or bool(expected)
        verified[str(p)]=h
        return eid
    # Metadata-only artifact decisions remain distinct from GPU experiments.
    for item in db['summary'].get('model_screening_progress',{}).get('artifact_applicability_reviews',[]):
        aid=receipt(item['audit_path'],item['audit_sha256'])
        if not aid:raise ValueError('Artifact applicability audit missing')
        review=load(locations[aid])
        if item.get('GPU_runs')!=0 or review.get('new_GPU_runs')!=0 or review.get('experimentally_screened') is not False:
            raise ValueError('CPU applicability cannot be reported as a new GPU screen')
    factors=[]; mapping={x['factor_id']:x for x in db['summary']['matrix_130_reconciliation']['axes']}
    for a in matrix['original_axes_reprioritized']+matrix['benchmark_technique_subcases']:
        c=a['accountability'];links=[]
        for e in c.get('evidence',[]):
            if isinstance(e,dict) and e.get('path'):
                ident=receipt(e['path'],e.get('sha256'))
                if ident:links.append(ident)
        variants=[]
        for v in c.get('original_variant_inventory',[]):
            refs=[]
            for w in v.get('archived_axis_bound_windows',[]):
                if w.get('path'):
                    ident=receipt(w['path'],w.get('sha256'))
                    if ident:refs.append(ident)
            review=v.get('sprint_scope_review',{})
            variants.append({'value':text(v['variant']),'historical_signed_states':[text(x) for x in v['original_cell_states']],'evidence_ids':sorted(set(refs)),'scope_status':review.get('status_in_concrete_scope'),'experimental_coverage':review.get('experimentally_covered'),'scope':text(review.get('scope')),'remaining_requirement':text(review.get('remaining_requirement')),'aggregate_metrics':projection(review.get('metrics'))})
        methods=a.get('research_source_updates_20261021') or c.get('research_source_updates_20261021') or {}
        f={'id':a['id'],'kind':'original' if a['id'] in mapping else 'additional','title':text(a['title']),'domain':a.get('domain',mapping.get(a['id'],{}).get('domain','transfer')),'status':c['status'],'experimentally_covered':c['experimentally_covered'],'omnicoder2_experimentally_covered':c.get('omnicoder2_experimentally_covered',False),'priority':a.get('current_priority_band',a.get('priority_band','P3')),'decision':text(c.get('decision_reason')),'coverage_scope':text(c.get('coverage_scope')),'remaining_scope':text(c.get('remaining_scope')),'reopening_conditions':text(c.get('reopening_conditions')),'prerequisites':[text(x) for x in c.get('missing_prerequisites',[]) if isinstance(x,str)],'next_action':text(c.get('next_action')),'linked_original_axes':a.get('linked_original_axes',[]),'evidence_ids':sorted(set(links)),'variants':variants,'primary_sources':urls(a)+urls(methods),'source_model_hypotheses':[text(x) for x in a.get('source_models',[])],'experiment_ids':[], 'per_model_original_coverage':[{ 'model':text(mc['model']), 'levels':[{ 'value':text(l['level']), 'signed_window_signatures':l.get('signed_window_signatures',[]), 'historical_states':l.get('original_cell_states',[]) } for l in mc.get('levels',[])]} for mc in mapping.get(a['id'],{}).get('model_level_coverage',[])]}
        model_findings=[db['summary'][key] for key,factor in (('r610','K01'),('r608','K02')) if a['id']==factor and key in db['summary']]
        if model_findings:
            f['model_specific_findings']=[]
            for finding in model_findings:
                evidence=[receipt(finding['audit_path'],finding['audit_sha256']),receipt(finding['comparison_review_path'],finding['comparison_review_sha256'])]; values=finding['comparison']
                if not all(evidence) or finding.get('winner_qualified') is not False:raise ValueError('Model-specific finding lacks verified evidence')
                measured=load(locations[evidence[0]]); paired=load(locations[evidence[1]])
                if paired.get('candidate_audit_sha256')!=digest(locations[evidence[0]]) or measured.get('solved_observed_tasks')!=values['candidate_successes'] or paired.get('reference_successes_on_compared_tasks')!=values['reference_successes'] or paired.get('tasks_compared')!=values['tasks'] or len(paired.get('paired_losses',[]))!=values['paired_losses'] or len(paired.get('paired_gains',[]))!=values['paired_gains']:raise ValueError('Model-specific finding does not match its measured outcomes')
                config=pathlib.Path(measured['runtime_configuration_profile_path'])
                if digest(config)!=measured['runtime_configuration_profile_sha256']:raise ValueError('Model-specific configuration changed')
                model=load(config)['model']
                f['model_specific_findings'].append({'model':text(model['name']+' '+model['quantization']),'model_sha256':model['artifact_sha256'],'variant':'q8_0 '+('key' if a['id']=='K01' else 'value')+' cache, other cache f16','status':'TESTED_NEGATIVE','scope':text(finding['scope']),'candidate_successes':values['candidate_successes'],'reference_successes':values['reference_successes'],'tasks':values['tasks'],'paired_losses':values['paired_losses'],'paired_gains':values['paired_gains'],'reopen':'Fresh balanced seed-controlled comparison or distinct long-context need with adequate quality and stability gates.','evidence_ids':evidence})
        reassessment=scope_reassessment(c)
        if reassessment:f['scope_reassessment']=reassessment
        assert f['status'] in STATUS
        factors.append(f)
    # Canonical sprint summaries and explicit existing audit paths; no recursive source-tree crawl.
    experiments={}
    for key,v in db['summary'].items():
        if not re.fullmatch(r'r\d+',key) or not isinstance(v,dict):continue
        ident=key.upper();p=v.get('audit_path') or v.get('audit') or v.get('artifact_build') or v.get('result_path') or v.get('build_final_receipt');expected=v.get('audit_sha256') or v.get('artifact_build_sha256') or v.get('result_sha256') or v.get('build_final_receipt_sha256');audit=receipt(p,expected) if isinstance(p,str) else None
        if not audit:
            candidate=root/'staging'/key/'AUDIT.json'
            if candidate.is_file():audit=receipt(candidate)
        if not audit:
            # Source/technical-only entries remain visible and explicitly unaudited.
            state='SUMMARY_ONLY_NOT_INDEPENDENTLY_AUDITED'
        else:state='ORIGINAL_AUDIT_HASH_VERIFIED'
        axes=v.get('axis_factors',[]);factor=v.get('factor')
        if factor in {x['id'] for x in factors}:axes=list(set(axes+[factor]))
        axes=[x for x in axes if isinstance(x,str) and re.fullmatch(r'(?:R|K|C|H|Q|M|S|E|A|T|HBM|BMT)\d{2}',x)]
        experiments[ident]={'id':ident,'date':text(v.get('at_utc')),'factor_ids':sorted(set(axes)),'audit_id':audit,'evidence_status':state,'statements':snippets(v),'aggregate_metrics':metrics(v),'winner_qualified':v.get('winner_qualified') is True,'model':text(v.get('model')),'reference_A0':v.get('reference_A0') if isinstance(v.get('reference_A0'),str) and re.fullmatch('[a-f0-9]{64}',v['reference_A0']) else None}
        if ident=='R615' and v.get('independent_review_path'):
            review_id=receipt(v['independent_review_path'],v['independent_review_sha256']);reference_id=receipt(root/'staging/r531/AUDIT.json')
            if not audit or not review_id or not reference_id:raise ValueError('R615 evidence missing')
            measured=load(locations[audit]);review=load(locations[review_id]);reference=load(locations[reference_id])
            if review.get('source_audit_sha256')!=digest(locations[audit]) or review.get('original_R531_audit_sha256')!=digest(locations[reference_id]):raise ValueError('R615 audit identity mismatch')
            folders=list((root.parent/'research/mcp-workspace/r615-nexus-prefix-token-abba').glob('host-*'))
            if len(folders)!=1:raise ValueError('R615 capture identity mismatch')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl';oldfolder=pathlib.Path(reference['raw_root']);oldpins=load(oldfolder/'RAW_HASHES.json');oldraw=oldfolder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review.get('source_responses_sha256') or digest(oldraw)!=oldpins['HTTP_RESULTS.jsonl'] or digest(oldraw)!=review.get('reference_responses_sha256'):raise ValueError('R615 raw capture changed')
            runs=[r for r in (json.loads(line) for line in raw.read_text().splitlines()) if r.get('kind')=='r615_request'];original=[r for r in (json.loads(line) for line in oldraw.read_text().splitlines()) if r.get('kind')=='agent_turn']
            if len(runs)!=16 or len(measured.get('turns',[]))!=4:raise ValueError('R615 incomplete request capture')
            for i in range(4):
                items=[runs[i+4*j] for j in range(4)];seq=[r['reply']['__verbose']['tokens'] for r in items];metric=measured['turns'][i];matches=[r for r in original if r['request_sha256']==items[0]['request_sha256']]
                if len(matches)!=1 or matches[0]['request']!=items[0]['request']:raise ValueError('R615 historical request mismatch')
                oldseq=matches[0]['reply']['__verbose']['tokens'];common=0
                for a,b in zip(oldseq,seq[0]):
                    if a!=b:break
                    common+=1
                expected={'turn':i+1,'same_request_as_R531':True,'R531_vs_fresh_A_tokens_identical':oldseq==seq[0],'R531_output_token_count':len(oldseq),'fresh_A_output_token_count':len(seq[0]),'common_prefix_tokens':common}
                if review['historical_vs_fresh_no_cache'][i]!=expected or metric['A_repeats_identical']!=(seq[0]==seq[3]) or metric['B_repeats_identical']!=(seq[1]==seq[2]) or metric['A1_B1_identical']!=(seq[0]==seq[1]):raise ValueError('R615 token comparison differs')
            experiments[ident]['related_audit_ids']=[review_id,reference_id]
            experiments[ident]['aggregate_metrics']['abba_diagnostic']=projection({'turns':measured['turns'],'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':measured['energy_counter'],'historical_vs_fresh_no_cache':review['historical_vs_fresh_no_cache']})
            experiments[ident]['statements']['diagnosis_scope']=text(review['scope'])
        if ident=='R620' and v.get('independent_review_path'):
            rid=receipt(v['independent_review_path'],v['independent_review_sha256']);pid=receipt(v['prompt_render_review_path'],v['prompt_render_review_sha256']);refid=receipt(root/'staging/r536/AUDIT.json');screenid=receipt(root/'staging/r616/AUDIT.json')
            if not audit or not rid or not pid or not refid or not screenid:raise ValueError('R620 evidence missing')
            measured=load(locations[audit]);review=load(locations[rid]);prompts=load(locations[pid]);reference=load(locations[refid])
            if review.get('source_audit_sha256')!=digest(locations[audit]) or prompts.get('source_audit_sha256')!=digest(locations[audit]) or measured.get('reference_audit_sha256')!=digest(locations[refid]) or measured.get('source_screen_audit_sha256')!=digest(locations[screenid]) or review.get('winner_qualified') is not False:raise ValueError('R620 source identity mismatch')
            folders=list((root.parent/'research/mcp-workspace/r620-omni-aa-abba-token-pilot').glob('host-*'))
            if len(folders)!=1:raise ValueError('R620 capture count differs')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl';oldfolder=pathlib.Path(reference['raw_root']);oldpins=load(oldfolder/'RAW_HASHES.json');oldraw=oldfolder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review['raw_responses_sha256'] or digest(oldraw)!=oldpins['HTTP_RESULTS.jsonl'] or digest(oldraw)!=prompts['historical_responses_sha256']:raise ValueError('R620 raw capture changed')
            captured=[json.loads(x) for x in raw.read_text().splitlines() if x];turns=[x for x in captured if x.get('kind')=='r620_request'];inputs=[x for x in captured if x.get('kind')=='r620_input'];historical=[x for x in (json.loads(t) for t in oldraw.read_text().splitlines() if t) if x.get('kind')=='agent_turn'];data=load(root/'staging/r620/PRIVATE_REQUESTS.json')['cases']
            if len(turns)!=24 or len(inputs)!=24 or len(data)!=24:raise ValueError('R620 incomplete')
            for x,y,c in zip(turns,inputs,data):
                if x['id']!=y['id'] or x['id']!=c['id'] or json.dumps(x['request'],ensure_ascii=True,allow_nan=False)!=c['request_json'] or y['prompt_token_ids']!=c['expected_prompt_token_ids'] or x['reply']['__verbose']['generation_settings']['seed']!=1001:raise ValueError('R620 input evidence differs')
            for i in range(3):
                group=[turns[i+3*j] for j in range(8)];seq=[x['reply']['__verbose']['tokens'] for x in group];cached=[x['reply']['usage']['prompt_tokens_details']['cached_tokens'] for x in group];aa=[seq[j] for j in (0,3,5,6)];bb=[seq[j] for j in (1,2,4,7)]
                def first(a,b):
                    n=0
                    for x,y in zip(a,b):
                        if x!=y:break
                        n+=1
                    return n
                expected={'turn':i+1,'no_cache_all_four_equal':all(x==aa[0] for x in aa),'no_cache_equal_across_sessions':aa[0]==aa[2],'cache_all_four_equal':all(x==bb[0] for x in bb),'every_cache_equals_baseline':all(x==aa[0] for x in bb),'cache_variants_differ_from_baseline':sum(x!=aa[0] for x in bb),'first_difference_positions_zero_based':[first(aa[0],x) if x!=aa[0] else None for x in bb],'cache_hit_turns':sum(cached[j]>0 for j in (1,2,4,7)),'output_lengths':[len(x) for x in seq]}
                if review['turns'][i]!=expected:raise ValueError('R620 token outcome differs')
                matching=[x for x in historical if x['request']==json.loads(data[i]['request_json'])]
                if len(matching)!=1 or prompts['turns'][i]['all_eight_report_original_prompt']!=all(x['reply']['__verbose']['prompt']==matching[0]['reply']['__verbose']['prompt'] for x in group):raise ValueError('R620 reported prompt differs')
            experiments[ident]['related_audit_ids']=[rid,pid,refid,screenid]
            safe_turns=[]
            for x in review['turns']:
                positions=[v for v in x['first_difference_positions_zero_based'] if v is not None]
                safe_turns.append({k:x[k] for k in ('turn','no_cache_equal_across_sessions','no_cache_all_four_equal','cache_variants_differ_from_baseline','cache_hit_turns')} | {'first_difference_position_zero_based':min(positions) if positions else None})
            experiments[ident]['aggregate_metrics']['repeatability_pilot']={'turns':safe_turns,'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':projection(measured['energy_counter'])}
            experiments[ident]['statements']['repeatability_limits']=text(review['limits'])
            experiments[ident]['statements']['repeatability_decision']=text(v['decision'])
        if ident=='R621' and v.get('independent_review_path'):
            rid=receipt(v['independent_review_path'],v['independent_review_sha256']);pid=receipt(v['prompt_render_review_path'],v['prompt_render_review_sha256']);refid=receipt(root/'staging/r531/AUDIT.json');screenid=receipt(root/'staging/r614/AUDIT.json')
            if not audit or not rid or not pid or not refid or not screenid:raise ValueError('R621 evidence missing')
            measured=load(locations[audit]);review=load(locations[rid]);prompts=load(locations[pid]);reference=load(locations[refid])
            if review.get('source_audit_sha256')!=digest(locations[audit]) or prompts.get('source_audit_sha256')!=digest(locations[audit]) or measured.get('reference_audit_sha256')!=digest(locations[refid]) or measured.get('source_screen_audit_sha256')!=digest(locations[screenid]) or review.get('winner_qualified') is not False:raise ValueError('R621 source identity mismatch')
            folders=list((root.parent/'research/mcp-workspace/r621-nexus-aa-abba-token-pilot').glob('host-*'))
            if len(folders)!=1:raise ValueError('R621 capture count differs')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl';oldfolder=pathlib.Path(reference['raw_root']);oldpins=load(oldfolder/'RAW_HASHES.json');oldraw=oldfolder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review['raw_responses_sha256'] or digest(oldraw)!=oldpins['HTTP_RESULTS.jsonl'] or digest(oldraw)!=prompts['historical_responses_sha256']:raise ValueError('R621 raw capture changed')
            captured=[json.loads(x) for x in raw.read_text().splitlines() if x];turns=[x for x in captured if x.get('kind')=='r621_request'];inputs=[x for x in captured if x.get('kind')=='r621_input'];historical=[x for x in (json.loads(t) for t in oldraw.read_text().splitlines() if t) if x.get('kind')=='agent_turn'];data=load(root/'staging/r621/PRIVATE_REQUESTS.json')['cases']
            if len(turns)!=32 or len(inputs)!=32 or len(data)!=32:raise ValueError('R621 incomplete')
            for x,y,c in zip(turns,inputs,data):
                if x['id']!=y['id'] or x['id']!=c['id'] or json.dumps(x['request'],ensure_ascii=True,allow_nan=False)!=c['request_json'] or y['prompt_token_ids']!=c['expected_prompt_token_ids'] or x['reply']['__verbose']['generation_settings']['seed']!=1001:raise ValueError('R621 input evidence differs')
            for i in range(4):
                group=[turns[i+4*j] for j in range(8)];seq=[x['reply']['__verbose']['tokens'] for x in group];cached=[x['reply']['usage']['prompt_tokens_details']['cached_tokens'] for x in group];aa=[seq[j] for j in (0,3,5,6)];bb=[seq[j] for j in (1,2,4,7)]
                def first(a,b):
                    n=0
                    for x,y in zip(a,b):
                        if x!=y:break
                        n+=1
                    return n
                expected={'turn':i+1,'no_cache_all_four_equal':all(x==aa[0] for x in aa),'no_cache_equal_across_sessions':aa[0]==aa[2],'cache_all_four_equal':all(x==bb[0] for x in bb),'every_cache_equals_baseline':all(x==aa[0] for x in bb),'cache_variants_differ_from_baseline':sum(x!=aa[0] for x in bb),'first_difference_positions_zero_based':[first(aa[0],x) if x!=aa[0] else None for x in bb],'cache_hit_turns':sum(cached[j]>0 for j in (1,2,4,7)),'output_lengths':[len(x) for x in seq]}
                if review['turns'][i]!=expected:raise ValueError('R621 token outcome differs')
                matching=[x for x in historical if x['request']==json.loads(data[i]['request_json'])]
                if len(matching)!=1 or prompts['turns'][i]['all_eight_report_original_prompt']!=all(x['reply']['__verbose']['prompt']==matching[0]['reply']['__verbose']['prompt'] for x in group):raise ValueError('R621 reported prompt differs')
            experiments[ident]['related_audit_ids']=[rid,pid,refid,screenid]
            safe_turns=[]
            for x in review['turns']:
                positions=[v for v in x['first_difference_positions_zero_based'] if v is not None]
                safe_turns.append({k:x[k] for k in ('turn','no_cache_equal_across_sessions','no_cache_all_four_equal','cache_variants_differ_from_baseline','cache_hit_turns')} | {'first_difference_position_zero_based':min(positions) if positions else None})
            experiments[ident]['aggregate_metrics']['repeatability_pilot']={'turns':safe_turns,'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':projection(measured['energy_counter'])}
            experiments[ident]['statements']['repeatability_limits']=text(review['limits'])
            experiments[ident]['statements']['repeatability_decision']=text(v['decision'])
        if ident=='R624' and v.get('independent_review_path'):
            rid=receipt(v['independent_review_path'],v['independent_review_sha256']);pid=receipt(v['prompt_render_review_path'],v['prompt_render_review_sha256']);refid=receipt(root/'staging/r534/AUDIT.json');screenid=receipt(root/'staging/r617/AUDIT.json')
            if not audit or not rid or not pid or not refid or not screenid:raise ValueError('R624 evidence missing')
            measured=load(locations[audit]);review=load(locations[rid]);prompts=load(locations[pid]);reference=load(locations[refid])
            if review.get('source_audit_sha256')!=digest(locations[audit]) or prompts.get('source_audit_sha256')!=digest(locations[audit]) or measured.get('reference_audit_sha256')!=digest(locations[refid]) or measured.get('source_screen_audit_sha256')!=digest(locations[screenid]) or review.get('winner_qualified') is not False:raise ValueError('R624 source identity mismatch')
            folders=list((root.parent/'research/mcp-workspace/r624-gemma-aa-abba-token-pilot').glob('host-*'))
            if len(folders)!=1:raise ValueError('R624 capture count differs')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl';oldfolder=pathlib.Path(reference['raw_root']);oldpins=load(oldfolder/'RAW_HASHES.json');oldraw=oldfolder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review['raw_responses_sha256'] or digest(oldraw)!=oldpins['HTTP_RESULTS.jsonl'] or digest(oldraw)!=prompts['historical_responses_sha256']:raise ValueError('R624 raw capture changed')
            captured=[json.loads(x) for x in raw.read_text().splitlines() if x];turns=[x for x in captured if x.get('kind')=='r624_request'];inputs=[x for x in captured if x.get('kind')=='r624_input'];historical=[x for x in (json.loads(t) for t in oldraw.read_text().splitlines() if t) if x.get('kind')=='agent_turn'];data=load(root/'staging/r624/PRIVATE_REQUESTS.json')['cases']
            if len(turns)!=32 or len(inputs)!=32 or len(data)!=32:raise ValueError('R624 incomplete')
            for x,y,c in zip(turns,inputs,data):
                if x['id']!=y['id'] or x['id']!=c['id'] or json.dumps(x['request'],ensure_ascii=True,allow_nan=False)!=c['request_json'] or y['prompt_token_ids']!=c['expected_prompt_token_ids'] or x['reply']['__verbose']['generation_settings']['seed']!=1001 or x['reply']['__verbose']['generation_settings']['temperature']!=1.0:raise ValueError('R624 input evidence differs')
            for i in range(4):
                group=[turns[i+4*j] for j in range(8)];seq=[x['reply']['__verbose']['tokens'] for x in group];cached=[x['reply']['usage']['prompt_tokens_details']['cached_tokens'] for x in group];aa=[seq[j] for j in (0,3,5,6)];bb=[seq[j] for j in (1,2,4,7)]
                def first(a,b):
                    n=0
                    for x,y in zip(a,b):
                        if x!=y:break
                        n+=1
                    return n
                expected={'turn':i+1,'no_cache_all_four_equal':all(x==aa[0] for x in aa),'no_cache_equal_across_sessions':aa[0]==aa[2],'cache_all_four_equal':all(x==bb[0] for x in bb),'every_cache_equals_baseline':all(x==aa[0] for x in bb),'cache_variants_differ_from_baseline':sum(x!=aa[0] for x in bb),'first_difference_positions_zero_based':[first(aa[0],x) if x!=aa[0] else None for x in bb],'cache_hit_turns':sum(cached[j]>0 for j in (1,2,4,7)),'output_lengths':[len(x) for x in seq]}
                if review['turns'][i]!=expected:raise ValueError('R624 token outcome differs')
                matching=[x for x in historical if x['request']==json.loads(data[i]['request_json'])]
                if len(matching)!=1 or prompts['turns'][i]['all_eight_report_original_prompt']!=all(x['reply']['__verbose']['prompt']==matching[0]['reply']['__verbose']['prompt'] for x in group):raise ValueError('R624 reported prompt differs')
            experiments[ident]['related_audit_ids']=[rid,pid,refid,screenid]
            safe_turns=[]
            for x in review['turns']:
                positions=[v for v in x['first_difference_positions_zero_based'] if v is not None]
                safe_turns.append({k:x[k] for k in ('turn','no_cache_equal_across_sessions','no_cache_all_four_equal','cache_variants_differ_from_baseline','cache_hit_turns')} | {'first_difference_position_zero_based':min(positions) if positions else None})
            experiments[ident]['aggregate_metrics']['repeatability_pilot']={'turns':safe_turns,'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':projection(measured['energy_counter'])}
            experiments[ident]['statements']['repeatability_limits']=text(review['limits'])
            experiments[ident]['statements']['repeatability_decision']=text(v['decision'])
        if ident=='R622' and v.get('independent_review_path'):
            rid=receipt(v['independent_review_path'],v['independent_review_sha256']);refid=receipt(root/'staging/r534/AUDIT.json');screenid=receipt(root/'staging/r617/AUDIT.json')
            if not audit or not rid or not refid or not screenid:raise ValueError('R622 evidence missing')
            measured=load(locations[audit]);review=load(locations[rid])
            if review['source_audit_sha256']!=digest(locations[audit]) or measured['reference_audit_sha256']!=digest(locations[refid]) or measured['source_screen_audit_sha256']!=digest(locations[screenid]) or review['winner_qualified'] is not False:raise ValueError('R622 source mismatch')
            folders=list((root.parent/'research/mcp-workspace/r622-gemma-seed-repeat-token-pilot').glob('host-*'))
            if len(folders)!=1:raise ValueError('R622 capture count differs')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review['raw_responses_sha256']:raise ValueError('R622 raw capture changed')
            captured=[json.loads(x) for x in raw.read_text().splitlines() if x];turns=[x for x in captured if x.get('kind')=='r622_request'];inputs=[x for x in captured if x.get('kind')=='r622_input'];data=load(root/'staging/r622/PRIVATE_REQUESTS.json')['cases']
            if len(turns)!=36 or len(inputs)!=36 or len(data)!=36:raise ValueError('R622 incomplete')
            for x,y,c in zip(turns,inputs,data):
                settings=x['reply']['__verbose']['generation_settings']
                if x['id']!=y['id'] or x['id']!=c['id'] or json.dumps(x['request'],ensure_ascii=True,allow_nan=False)!=c['request_json'] or y['prompt_token_ids']!=c['expected_prompt_token_ids'] or settings['seed']!=x['request']['seed'] or settings['temperature']!=1.0 or x['request']['cache_prompt'] is not False:raise ValueError('R622 input or sampler evidence differs')
            for i in range(3):
                group=[turns[i+3*j] for j in range(12)];seq=[x['reply']['__verbose']['tokens'] for x in group];seeds=[x['reply']['__verbose']['generation_settings']['seed'] for x in group]
                if seeds!=[1001,1002,1003,1003,1002,1001]*2:raise ValueError('R622 seed order differs')
                for seed in (1001,1002,1003):
                    variants=[x for x,k in zip(seq,seeds) if k==seed];row=next(x for x in review['turns'][i]['seeds'] if x['seed']==seed)
                    if row['within_session_1_equal']!=(variants[0]==variants[1]) or row['within_session_2_equal']!=(variants[2]==variants[3]) or row['across_session_equal']!=(variants[0]==variants[2]):raise ValueError('R622 repeat result differs')
                if review['turns'][i]['different_seed_outputs']!=len({tuple(x) for x in seq[:3]}):raise ValueError('R622 distinct seed result differs')
            experiments[ident]['related_audit_ids']=[rid,refid,screenid]
            experiments[ident]['aggregate_metrics']['seed_repeatability_pilot']={'turns':review['turns'],'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':projection(measured['energy_counter'])}
            experiments[ident]['statements']['repeatability_limits']=text(review['limits'])
            experiments[ident]['statements']['repeatability_decision']=text(v['decision'])
        if ident=='R623' and v.get('independent_review_path'):
            rid=receipt(v['independent_review_path'],v['independent_review_sha256']);refid=receipt(root/'staging/r550/AUDIT.json')
            if not audit or not rid or not refid:raise ValueError('R623 evidence missing')
            measured=load(locations[audit]);review=load(locations[rid])
            if review['source_audit_sha256']!=digest(locations[audit]) or measured['reference_audit_sha256']!=digest(locations[refid]) or review['winner_qualified'] is not False:raise ValueError('R623 source mismatch')
            folders=list((root.parent/'research/mcp-workspace/r623-qwen38-mtp-aa-token-pilot').glob('host-*'))
            if len(folders)!=1:raise ValueError('R623 capture count differs')
            folder=folders[0];pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl'
            if digest(raw)!=pins['HTTP_RESULTS.jsonl'] or digest(raw)!=review['raw_responses_sha256']:raise ValueError('R623 raw capture changed')
            captured=[json.loads(x) for x in raw.read_text().splitlines() if x];turns=[x for x in captured if x.get('kind')=='r623_request'];inputs=[x for x in captured if x.get('kind')=='r623_input'];data=load(root/'staging/r623/PRIVATE_REQUESTS.json')['cases']
            if len(turns)!=24 or len(inputs)!=24 or len(data)!=24:raise ValueError('R623 incomplete')
            for x,y,c in zip(turns,inputs,data):
                settings=x['reply']['__verbose']['generation_settings']
                if x['id']!=y['id'] or x['id']!=c['id'] or json.dumps(x['request'],ensure_ascii=True,allow_nan=False)!=c['request_json'] or y['prompt_token_ids']!=c['expected_prompt_token_ids'] or settings['seed']!=1001 or settings['temperature']!=0 or x['request']['cache_prompt'] is not False:raise ValueError('R623 input or sampler evidence differs')
            for i in range(3):
                group=[turns[i+3*j] for j in range(8)];seq=[x['reply']['__verbose']['tokens'] for x in group];row=review['turns'][i]
                if row['within_session_1_equal']!=all(x==seq[0] for x in seq[:4]) or row['within_session_2_equal']!=all(x==seq[4] for x in seq[4:]) or row['across_session_equal']!=(seq[0]==seq[4]):raise ValueError('R623 repeat result differs')
            experiments[ident]['related_audit_ids']=[rid,refid]
            experiments[ident]['aggregate_metrics']['mtp_repeatability_pilot']={'turns':review['turns'],'task_phase_s':measured['task_phase_s'],'peak_device_vram_mib':measured['peak_device_vram_mib'],'energy_counter':projection(measured['energy_counter'])}
            experiments[ident]['statements']['repeatability_limits']=text(review['limits'])
            experiments[ident]['statements']['repeatability_decision']=text(v['decision'])
        if ident=='R619' and v.get('cpu_tokenizer_review'):
            item=v['cpu_tokenizer_review'];rid=receipt(item['path'],item['sha256']);cid=receipt(item['receipt_path'],item['receipt_sha256']);review=load(locations[rid]) if rid else {};proof=load(locations[cid]) if cid else {};private=pathlib.Path(item['private_output_path'])
            if not rid or not cid or digest(private)!=item['private_output_sha256'] or proof.get('private_output_sha256')!=digest(private) or proof.get('review_sha256')!=digest(locations[rid]) or proof.get('gpu_calls')!=0 or proof.get('model_generations')!=0:raise ValueError('R619 CPU tokenizer evidence missing')
            raw=load(private);turns=raw.get('turns',[])
            if len(turns)!=3 or len(review.get('turns',[]))!=3 or review.get('reference_audit_sha256')!=digest(root/'staging/r536/AUDIT.json') or review.get('candidate_audit_sha256')!=digest(root/'staging/r616/AUDIT.json'):raise ValueError('R619 tokenizer provenance mismatch')
            for row,record in zip(turns,review['turns']):
                actual=row['token_ids'];expected=row['expected_token_ids'];prefix=0
                for x,y in zip(actual,expected):
                    if x!=y:break
                    prefix+=1
                if record['turn']!=row['turn'] or record['cpu_tokenizer_tokens']!=len(actual) or record['expected_prompt_tokens']!=len(expected) or record['identical']!=(actual==expected) or record['common_prefix_tokens']!=prefix:raise ValueError('R619 tokenizer result mismatch')
            experiments[ident].setdefault('related_audit_ids',[]).extend([rid,cid])
            experiments[ident]['aggregate_metrics']['cpu_tokenizer_replay']={'turns':len(turns),'identical':sum(x['token_ids']==x['expected_token_ids'] for x in turns),'GPU_runs':0,'model_requests':0}
            experiments[ident]['statements']['tokenizer_scope']='CPU vocabulary-only replay of archived rendered prompts with pinned library; the failed fresh preflight was not captured, so its mismatch cause remains undetermined.'
            if v.get('json_order_cpu_review'):
                item=v['json_order_cpu_review'];oid=receipt(item['path'],item['sha256']);o=load(locations[oid]) if oid else {};folder=root/'staging/reproducibility-20261029/template-cpu';journal=folder/'CPU_TEMPLATE_JOURNAL.txt'
                if not oid or digest(journal)!=o.get('raw_cpu_output_sha256') or digest(folder/'pilot.json')!=o.get('unordered_input_sha256') or digest(folder/'pilot-ordered.json')!=o.get('ordered_input_sha256'):raise ValueError('R619 order review provenance differs')
                controls=load(journal)
                if len(controls)!=2 or any(x['GPU_runs']!=0 or x['model_generations']!=0 or len(x['records'])!=3 for x in controls) or not all(not x['equal'] and x['actual_count']==x['expected_count']+8 and x['common_prefix_tokens']==61 for x in controls[0]['records']) or not all(x['equal'] for x in controls[1]['records']):raise ValueError('R619 order control differs')
                experiments[ident]['related_audit_ids'].append(oid)
                experiments[ident]['aggregate_metrics']['cpu_wire_order_control']={'inputs':3,'sorted_order_mismatches':3,'original_order_matches':3,'extra_tokens_per_prompt':8,'GPU_runs':0}
                experiments[ident]['statements']['tokenizer_scope']='CPU source and pinned-server checks reproduced the mismatch when JSON keys were sorted; preserving original tool-schema key order restored the three historical input token sequences. No model generation was performed.'
        if ident=='R625' and v.get('mtp_comparison_review'):
            item=v['mtp_comparison_review'];review_id=receipt(item['path'],item['sha256']);ref_id=receipt(root/'staging/r618/AUDIT.json')
            if not audit or not review_id or not ref_id:raise ValueError('R625 comparison evidence missing')
            review=load(locations[review_id]);off=load(locations[audit]);on=load(locations[ref_id])
            if review['reference_off_audit_sha256']!=digest(locations[audit]) or review['candidate_on_audit_sha256']!=digest(locations[ref_id]) or review['winner_qualified'] is not False:raise ValueError('R625 comparison provenance differs')
            records=[]
            for source in (off,on):
                folder=pathlib.Path(source['raw_root']);raw=folder/'HTTP_RESULTS.jsonl';pins=load(folder/'RAW_HASHES.json')
                if digest(raw)!=pins['HTTP_RESULTS.jsonl']:raise ValueError('R625 response evidence changed')
                rows=[json.loads(line) for line in raw.read_text().splitlines() if line];records.append(([x for x in rows if x.get('kind')=='agent_case'],{x['id']:x for x in rows if x.get('kind')=='agent_turn'},{x['id']:x for x in rows if x.get('kind')=='input_identity'}))
            (a,at,ai),(b,bt,bi)=records
            if len(a)!=33 or [x['id'] for x in a]!=[x['id'] for x in b]:raise ValueError('R625 task identity differs')
            for key in ('task_success','policy_gate_pass'):
                pairs=[(x['reported_result'][key],y['reported_result'][key]) for x,y in zip(a,b)];expected={'off_passed':sum(x for x,y in pairs),'on_passed':sum(y for x,y in pairs),'off_only':sum(x and not y for x,y in pairs),'on_only':sum(not x and y for x,y in pairs)}
                if review[key]!=expected:raise ValueError('R625 paired outcomes differ')
            for prefix,source in (('off',off),('on',on)):
                if review[prefix+'_task_s']!=source['task_phase_s'] or review[prefix+'_peak_vram_mib']!=source['peak_device_vram_mib'] or review[prefix+'_completion_tokens']!=source['completion_tokens'] or review[prefix+'_gpu_j_bounds']!=[source['GPU_counter']['lower_j'],source['GPU_counter']['upper_j']]:raise ValueError('R625 measured costs differ')
            matched=[k for k in at.keys()&bt.keys()&ai.keys()&bi.keys() if at[k]['request']==bt[k]['request']];same=[k for k in matched if ai[k]['prompt_token_ids']==bi[k]['prompt_token_ids']];equal=sum(at[k]['reply']['__verbose']['tokens']==bt[k]['reply']['__verbose']['tokens'] for k in same)
            if [review['matched_request_and_input_token_ids'],review['matched_request_different_input_ids'],review['matched_output_sequences_equal'],review['matched_output_sequences_different']]!=[len(same),len(matched)-len(same),equal,len(same)-equal]:raise ValueError('R625 token comparisons differ')
            profile=v['profile_comparison_review'];profile_id=receipt(profile['path'],profile['sha256'])
            if not profile_id:raise ValueError('R625 profile comparison missing')
            experiments[ident].setdefault('related_audit_ids',[]).extend([review_id,ref_id,profile_id])
            public_review=projection(review)
            for key in ('off_gpu_j_bounds','on_gpu_j_bounds','matched_request_and_input_token_ids','matched_request_different_input_ids','matched_output_sequences_equal','matched_output_sequences_different'):public_review[key]=review[key]
            experiments[ident]['aggregate_metrics']['mtp_paired_comparison']=public_review
            if v.get('mtp_fixed_work_review'):
                item=v['mtp_fixed_work_review'];fixed_id=receipt(item['path'],item['sha256']);fixed=load(locations[fixed_id]) if fixed_id else {}
                selected=[k for k in same if at[k]['reply']['__verbose']['tokens']==bt[k]['reply']['__verbose']['tokens']]
                if not fixed_id or fixed['off_audit_sha256']!=digest(locations[audit]) or fixed['on_audit_sha256']!=digest(locations[ref_id]) or fixed['matched_requests']!=len(selected) or fixed['winner_qualified'] is not False:raise ValueError('R625 fixed-work provenance differs')
                for label,turns in (('off',at),('on',bt)):
                    timings=[turns[k]['reply']['timings'] for k in selected];expected={key:round(sum(t[key] for t in timings),6) for key in ('prompt_n','prompt_ms','predicted_n','predicted_ms')};expected['request_e2e_s']=round(sum(turns[k]['e2e_s'] for k in selected),6)
                    if label=='on':expected.update(draft_n=sum(t.get('draft_n',0) for t in timings),draft_n_accepted=sum(t.get('draft_n_accepted',0) for t in timings))
                    if fixed['arms'][label].keys()!=expected.keys() or any(abs(fixed['arms'][label][k]-value)>0.00001 for k,value in expected.items()):raise ValueError('R625 fixed-work timing differs')
                experiments[ident]['related_audit_ids'].append(fixed_id)
                experiments[ident]['aggregate_metrics']['mtp_fixed_work']={'matched_requests':fixed['matched_requests'],'arms':fixed['arms'],'scope':text(fixed['scope'])}
            if v.get('mtp_policy_review'):
                item=v['mtp_policy_review'];policy_id=receipt(item['path'],item['sha256']);policy=load(locations[policy_id]) if policy_id else {}
                fa={x['id']:x['reported_result'] for x in a if not x['reported_result']['policy_gate_pass']};fb={x['id']:x['reported_result'] for x in b if not x['reported_result']['policy_gate_pass']}
                if not policy_id or policy['off_audit_sha256']!=digest(locations[audit]) or policy['on_audit_sha256']!=digest(locations[ref_id]) or fa.keys()!=fb.keys() or policy['same_failed_cases']!=len(fa) or policy['winner_qualified'] is not False:raise ValueError('R625 policy provenance differs')
                for label,cases in (('off',fa),('on',fb)):
                    rejected=[t for x in cases.values() for t in x['trace'] if t.get('policy_rejected')]
                    expected={'policy_failed_cases':len(cases),'rejected_calls':sum(x['rejected_calls'] for x in cases.values()),'policy_violations':sum(x['policy_violations'] for x in cases.values()),'simulated_tools_only':True,'production_tools_connected':False,'rejected_action_category':'simulated climate setting'}
                    if policy['arms'][label]!=expected or len(rejected)!=len(cases) or any(t['tool']!='ha.set_climate' for t in rejected) or not all(x['all_tools_simulated'] and not x['production_tools_connected'] for x in cases.values()):raise ValueError('R625 policy evidence differs')
                selected=[k for k in at.keys()&bt.keys()&ai.keys()&bi.keys() if any(k.startswith(case) for case in fa) and at[k]['request']==bt[k]['request'] and ai[k]['prompt_token_ids']==bi[k]['prompt_token_ids']]
                if policy['same_request_and_input_tokens']!=len(selected) or policy['same_output_tokens']!=sum(at[k]['reply']['__verbose']['tokens']==bt[k]['reply']['__verbose']['tokens'] for k in selected):raise ValueError('R625 policy token evidence differs')
                experiments[ident]['related_audit_ids'].append(policy_id)
                experiments[ident]['aggregate_metrics']['mtp_policy_review']={'same_failed_cases':policy['same_failed_cases'],'same_request_and_input_tokens':len(selected),'same_output_tokens':policy['same_output_tokens'],'arms':policy['arms'],'scope':text(policy['scope'])}
            experiments[ident]['statements']['comparison_scope']=text(review['scope'])
        if ident=='R618' and v.get('cross_model_review'):
            item=v['cross_model_review'];review_id=receipt(item['path'],item['sha256']);review=load(locations[review_id]) if review_id else {};candidate=load(locations[audit]) if audit else {};related=[review_id] if review_id else []
            if not audit or review.get('winner_qualified') is not False or review.get('GPU_runs')!=0:raise ValueError('R618 comparison evidence missing')
            def holdout_cases(record):
                folder=pathlib.Path(record['raw_root']);pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl'
                if digest(raw)!=pins['HTTP_RESULTS.jsonl']:raise ValueError('R618 response evidence changed')
                return [r for r in (json.loads(line) for line in raw.read_text().splitlines() if line) if r.get('kind')=='agent_case']
            new=holdout_cases(candidate)
            for key,ref in review['comparisons'].items():
                ref_id=receipt(root/('staging/'+key.lower()+'/AUDIT.json'));old_audit=load(locations[ref_id]) if ref_id else {};old=holdout_cases(old_audit)
                if digest(locations[audit])!=ref['candidate_audit_sha256'] or not ref_id or digest(locations[ref_id])!=ref['reference_audit_sha256'] or len(old)!=33 or [r['id'] for r in old]!=[r['id'] for r in new]:raise ValueError('R618 comparison provenance differs')
                for field in ('task_success','policy_gate_pass'):
                    ps=[(x['reported_result'][field],y['reported_result'][field]) for x,y in zip(old,new)];expected={'reference_passed':sum(x for x,y in ps),'candidate_passed':sum(y for x,y in ps),'lost':sum(x and not y for x,y in ps),'gained':sum(not x and y for x,y in ps)}
                    if ref[field]!=expected:raise ValueError('R618 paired outcomes differ')
                for prefix,source in (('reference',old_audit),('candidate',candidate)):
                    if ref[prefix+'_task_s']!=source['task_phase_s'] or ref[prefix+'_vram_mib']!=source['peak_device_vram_mib'] or ref[prefix+'_gpu_j_bounds']!=[source['GPU_counter']['lower_j'],source['GPU_counter']['upper_j']]:raise ValueError('R618 measured costs differ')
                related.append(ref_id)
            experiments[ident]['related_audit_ids']=related
            experiments[ident]['aggregate_metrics']['cross_model_comparison']=projection(review['comparisons'])
            experiments[ident]['statements']['comparison_scope']=text(review['scope'])
        if ident in ('R612','R614','R616','R617') and v.get('single_factor_review'):
            item=v['single_factor_review'];review_id=receipt(item['path'],item['sha256']);reference_id=receipt(root/({'R612':'staging/r534/AUDIT.json','R614':'staging/r531/AUDIT.json','R616':'staging/r536/AUDIT.json','R617':'staging/r534/AUDIT.json'}[ident]))
            if not audit or not review_id or not reference_id:raise ValueError('R612 paired source missing')
            review=load(locations[review_id]);ref=load(locations[reference_id]);candidate=load(locations[audit])
            if review.get('reference_audit_sha256')!=digest(locations[reference_id]) or review.get('candidate_audit_sha256')!=digest(locations[audit]) or review.get('winner_qualified') is not False:raise ValueError('R612 source audit mismatch')
            captures=[];turns=[]
            for record in (ref,candidate):
                folder=pathlib.Path(record['raw_root']);pins=load(folder/'RAW_HASHES.json');raw=folder/'HTTP_RESULTS.jsonl'
                if digest(raw)!=pins['HTTP_RESULTS.jsonl']:raise ValueError('R612 response evidence changed')
                parsed=[json.loads(line) for line in raw.read_text().splitlines() if line];captures.append([r for r in parsed if r.get('kind')=='agent_case']);turns.append([r for r in parsed if r.get('kind')=='agent_turn'])
            a,b=captures
            if len(a)!=33 or [r['id'] for r in a]!=[r['id'] for r in b]:raise ValueError('R612 task identity mismatch')
            for field in ('task_success','policy_gate_pass','task_scope_pass'):
                pairs=[(x['reported_result'][field],y['reported_result'][field]) for x,y in zip(a,b)];expected={'reference_passed':sum(x for x,y in pairs),'candidate_passed':sum(y for x,y in pairs),'lost':sum(x and not y for x,y in pairs),'gained':sum(not x and y for x,y in pairs)}
                if review['comparison']['quality'][field]!=expected:raise ValueError('R612 paired outcome mismatch')
            if ident in ('R614','R616','R617'):
                for records,key in zip(turns,('reference_cache','candidate_cache')):
                    usages=[r['reply']['usage'] for r in records];cached=[u['prompt_tokens_details']['cached_tokens'] for u in usages]
                    expected={'turns':len(usages),'cache_hit_turns':sum(v>0 for v in cached),'cached_tokens':sum(cached),'prompt_tokens':sum(u['prompt_tokens'] for u in usages),'completion_tokens':sum(u['completion_tokens'] for u in usages)}
                    if review['comparison'][key]!=expected:raise ValueError('R614 cache counters differ')
            experiments[ident]['related_audit_ids']=[review_id,reference_id]
            if ident=='R614' and v.get('policy_divergence_review'):
                item=v['policy_divergence_review'];diagnosis_id=receipt(item['path'],item['sha256']);diagnosis=load(locations[diagnosis_id]) if diagnosis_id else {}
                if diagnosis.get('reference_audit_sha256')!=digest(locations[reference_id]) or diagnosis.get('candidate_audit_sha256')!=digest(locations[audit]) or diagnosis.get('case_count_with_new_policy_failure')!=1:raise ValueError('R614 diagnosis provenance differs')
                cases=[x['id'] for x,y in zip(a,b) if x['reported_result']['policy_gate_pass'] and not y['reported_result']['policy_gate_pass']]
                if len(cases)!=1:raise ValueError('R614 diagnosis policy case differs')
                matched=[[r for r in rows if r['id'].startswith(cases[0]+'--turn')] for rows in turns]
                def semantic(m):return {'content':m.get('content'),'role':m.get('role'),'calls':[{'type':x.get('type'),'function':x.get('function')} for x in (m.get('tool_calls') or [])]}
                observed=[]
                for i,(x,y) in enumerate(zip(*matched),1):
                    equal_request={k:v for k,v in x['request'].items() if k!='cache_prompt'}=={k:v for k,v in y['request'].items() if k!='cache_prompt'};equal_reply=semantic(x['reply']['choices'][0]['message'])==semantic(y['reply']['choices'][0]['message']);observed.append({'turn_number':i,'requests_equal_except_cache_flag':equal_request,'generated_content_and_calls_equal':equal_reply,'candidate_cached_tokens':y['reply']['usage']['prompt_tokens_details']['cached_tokens']})
                    if not equal_request or not equal_reply:break
                if observed!=diagnosis.get('turns_before_divergence'):raise ValueError('R614 divergence evidence differs')
                experiments[ident]['related_audit_ids'].append(diagnosis_id)
                experiments[ident]['statements']['policy_diagnosis']=text(diagnosis['interpretation'])
                experiments[ident]['aggregate_metrics']['policy_diagnosis']=projection({'turns_before_divergence':observed,'case_count_with_new_policy_failure':1})
                if v.get('token_divergence_review'):
                    item=v['token_divergence_review'];token_id=receipt(item['path'],item['sha256']);token=load(locations[token_id]) if token_id else {};evidence=[]
                    for i,(x,y) in enumerate(zip(*matched),1):
                        if i>4:break
                        left=x['reply']['__verbose']['tokens'];right=y['reply']['__verbose']['tokens'];prefix=0
                        for u,w in zip(left,right):
                            if u!=w:break
                            prefix+=1
                        same={k:v for k,v in x['request'].items() if k!='cache_prompt'}=={k:v for k,v in y['request'].items() if k!='cache_prompt'}
                        evidence.append({'turn_number':i,'request_equal_except_cache':same,'candidate_cached_tokens':y['reply']['usage']['prompt_tokens_details']['cached_tokens'],'reference_output_tokens':len(left),'candidate_output_tokens':len(right),'equal_token_prefix_length':prefix,'identical_token_sequences':left==right})
                    if token.get('reference_audit_sha256')!=digest(locations[reference_id]) or token.get('candidate_audit_sha256')!=digest(locations[audit]) or token.get('turns')!=evidence:raise ValueError('R614 token divergence differs')
                    experiments[ident]['related_audit_ids'].append(token_id)
                    experiments[ident]['aggregate_metrics']['token_divergence']=projection({'turns':evidence})
            if ident=='R614' and v.get('state_path_review'):
                item=v['state_path_review'];state_id=receipt(item['path'],item['sha256']);state=load(locations[state_id]) if state_id else {}
                folder=pathlib.Path(candidate['raw_root']);pins=load(folder/'RAW_HASHES.json');log=folder/'server.log'
                if state.get('candidate_audit_sha256')!=digest(locations[audit]) or state.get('server_log_sha256')!=pins['server.log'] or digest(log)!=pins['server.log']:raise ValueError('R614 state log provenance differs')
                contents=log.read_text(errors='replace');expected={'restored_context_checkpoint':contents.count('restored context checkpoint'),'forced_full_prompt_reprocessing':contents.count('forcing full prompt re-processing'),'partial_sequence_removal_unsupported':contents.count('context does not support partial sequence removal'),'host_prompt_cache_disabled':contents.count('prompt cache is disabled')}
                if state.get('observed_log_counts')!=expected:raise ValueError('R614 state counts differ')
                experiments[ident]['related_audit_ids'].append(state_id)
                experiments[ident]['statements']['state_path_scope']=text(state['scope'])
                experiments[ident]['aggregate_metrics']['state_path_counts']=projection(expected)
            experiments[ident]['statements']['single_factor_decision']=text(review.get('decision',review['status']))
            experiments[ident]['statements']['single_factor_limits']=text(review['limits'])
            experiments[ident]['aggregate_metrics']['single_factor_comparison']=projection(review['comparison'])
        if ident in ('R608','R610') and v.get('comparison_review_path'):
            paired=receipt(v['comparison_review_path'],v['comparison_review_sha256']); energy_id=receipt(v['paired_energy_counter_review']['path'],v['paired_energy_counter_review']['sha256']); ref_id=receipt(root/'staging/r464/AUDIT.json')
            if not audit or not paired or not energy_id or not ref_id:raise ValueError('R608 comparison evidence missing')
            paired_data=load(locations[paired]); energy=load(locations[energy_id]); candidate=load(locations[audit]); reference=load(locations[ref_id]); comparison=v['comparison']
            if paired_data['candidate_audit_sha256']!=digest(locations[audit]) or paired_data['reference_audit_sha256']!=digest(locations[ref_id]) or energy['candidate_audit_sha256']!=digest(locations[audit]) or energy['reference_audit_sha256']!=digest(locations[ref_id]):raise ValueError('R608 source audit differs')
            verdicts=[]
            for source,trial in ((reference,'r464'),(candidate,ident.lower())):
                judge=root/'staging'/trial/'scoring/part01'/(trial+'-judge-part01.stdout')
                if digest(judge)!=source['scoring'][0]['judge_stdout_sha256']:raise ValueError('R608 judge source differs')
                rows=[json.loads(line) for line in judge.read_text().splitlines()];verdicts.append({x['task_id']:x['checks']['base']['status']==x['checks']['plus']['status']=='pass' for x in rows})
            left,right=verdicts
            if len(left)!=164 or left.keys()!=right.keys() or paired_data['paired_losses']!=[k for k in right if left[k] and not right[k]] or paired_data['paired_gains']!=[k for k in right if not left[k] and right[k]] or comparison['paired_losses']!=len(paired_data['paired_losses']) or comparison['paired_gains']!=len(paired_data['paired_gains']):raise ValueError('R608 paired task outcomes differ')
            from leaderboard import counter_energy_bounds
            for arm,source in (('reference',reference),('candidate',candidate)):
                row=energy['arms'][arm];manifest=pathlib.Path(row['raw_hashes_path']);raw=load(manifest);folder=manifest.parent
                if digest(manifest)!=row['raw_hashes_sha256']:raise ValueError('R608 raw manifest differs')
                for name,key in (('GPU_TELEMETRY.jsonl','telemetry_sha256'),('HTTP_RESULTS.jsonl','requests_sha256')):
                    if digest(folder/name)!=row[key] or raw.get(name)!=row[key]:raise ValueError('R608 counter input differs')
                telemetry=[json.loads(line) for line in (folder/'GPU_TELEMETRY.jsonl').read_text().splitlines()];requests=[x for x in (json.loads(line) for line in (folder/'HTTP_RESULTS.jsonl').read_text().splitlines()) if x.get('kind')=='coding'];bounds=counter_energy_bounds(telemetry,requests,[x['id'] for x in requests]);solved=source['solved_observed_tasks']
                if len(requests)!=164 or row['counter_bounds']!=bounds or row['successes']!=solved or comparison['counter_gpu_j_per_success_lower_'+arm]!=bounds['lower_j']/solved or comparison['counter_gpu_j_per_success_upper_'+arm]!=bounds['upper_j']/solved or comparison[arm+'_completion_tokens']!=sum(x['reply']['usage']['completion_tokens'] for x in requests):raise ValueError('R608 counter projection differs')
            experiments[ident]['related_audit_ids']=[paired,energy_id,ref_id]
            if ident=='R610' and v.get('duplicate_review'):
                item=v['duplicate_review'];duplicate_id=receipt(item['path'],item['sha256'])
                if not duplicate_id:raise ValueError('R610 duplicate review missing')
                duplicate=load(locations[duplicate_id]);original=root/'staging/r544/AUDIT.json'
                if duplicate.get('kind')!='DUPLICATE_PREVIOUSLY_VALID_BENCHMARK_TRANSPARENT_CORRECTION' or digest(original)!=duplicate['sources']['r544']['audit_sha256'] or digest(locations[audit])!=duplicate['sources']['r610']['audit_sha256']:raise ValueError('R610 duplicate review provenance differs')
                captures=[]
                for trial in ('r544','r610'):
                    audit_source=load(original if trial=='r544' else locations[audit]);folder=pathlib.Path(audit_source['parts'][0]['audit_path']).parent;raw=folder/'HTTP_RESULTS.jsonl';pins=folder/'RAW_HASHES.json'
                    if digest(raw)!=duplicate['sources'][trial]['response_sha256'] or digest(pins)!=duplicate['sources'][trial]['raw_hashes_sha256'] or load(pins)['HTTP_RESULTS.jsonl']!=digest(raw):raise ValueError('R610 repeat raw evidence differs')
                    captures.append({r['id']:r for r in (json.loads(line) for line in raw.read_text().splitlines()) if r.get('kind')=='coding'})
                x,y=captures
                if len(x)!=164 or x.keys()!=y.keys() or any(x[k]['request_sha256']!=y[k]['request_sha256'] or x[k]['reply']['choices']!=y[k]['reply']['choices'] or x[k]['reply']['usage']!=y[k]['reply']['usage'] for k in x):raise ValueError('R610 repeat results differ')
                experiments[ident]['related_audit_ids'].append(duplicate_id)
        if ident=='R607' and v.get('comparison_review_path'):
            review_id=receipt(v['comparison_review_path'],v['comparison_review_sha256'])
            reference_id=receipt(root/'staging/r510/AUDIT.json')
            if not audit or not review_id or not reference_id:raise ValueError('R607 paired provenance missing')
            review=load(locations[review_id]); reference=load(locations[reference_id]); candidate=load(locations[audit])
            if review['reference_audit_sha256']!=digest(locations[reference_id]) or review['candidate_audit_sha256']!=digest(locations[audit]):raise ValueError('R607 audit hashes differ')
            a={x['id']:x['success'] for x in reference['scored_tasks']};b={x['id']:x['success'] for x in candidate['scored_tasks']}
            if a.keys()!=b.keys() or len(a)!=16 or review['paired_losses']!=[k for k in a if a[k] and not b[k]] or review['paired_gains']!=[k for k in a if not a[k] and b[k]] or review['reference_successes']!=sum(a.values()) or review['candidate_successes']!=sum(b.values()):raise ValueError('R607 paired scores differ')
            experiments[ident]['related_audit_ids']=[review_id,reference_id]
        if ident=='R606' and v.get('token_review'):
            t=v['token_review']; review_id=receipt(t['path'],t['sha256'])
            if not audit or not review_id:raise ValueError('R606 token provenance missing')
            review=load(locations[review_id]); original=load(locations[audit]); paths=[pathlib.Path(p) for p,h in original['refs'].items() if h==review['raw_hashes_sha256']]
            if len(paths)!=1 or digest(paths[0])!=review['raw_hashes_sha256']:raise ValueError('R606 raw manifest changed')
            source=paths[0].parent/'HTTP_RESULTS.jsonl'; raw=load(paths[0])
            if digest(source)!=review['source_raw_sha256'] or raw.get('HTTP_RESULTS.jsonl')!=review['source_raw_sha256']:raise ValueError('R606 requests changed')
            rows=[json.loads(line) for line in source.read_text().splitlines()]
            for arm in ('A','B'):
                selected=[r for r in rows if r.get('kind') in ('coding','native_tool') and r['id'].endswith('--'+arm)]
                if len(selected)!=32 or sum(r['reply']['usage']['completion_tokens'] for r in selected)!=review['groups'][arm]['completion_tokens'] or v['comparison']['completion_tokens_'+arm]!=review['groups'][arm]['completion_tokens']:raise ValueError('R606 token count differs')
            experiments[ident]['related_audit_ids']=[review_id]
        if audit and ident in ('R603','R604','R605') and v.get('energy_counter_review'):
            entry=v['energy_counter_review'];review_id=receipt(entry['path'],entry['sha256'])
            if not review_id:raise ValueError('Energy counter review missing')
            energy=load(locations[review_id]);original=load(locations[audit]);evidence_hashes=set(original['refs'].values())
            if energy.get('experiment_id')!=ident or energy.get('status')!='INDEPENDENT_GPU_COUNTER_BOUNDS_CPU_REPLAY' or energy.get('winner_qualified') is not False or energy.get('source_audit_sha256') not in evidence_hashes or energy.get('raw_hashes_sha256') not in evidence_hashes or energy.get('quality_sha256') not in evidence_hashes:
                raise ValueError('Energy counter provenance differs')
            from leaderboard import counter_energy_bounds
            hash_paths=[pathlib.Path(path) for path,h in original['refs'].items() if h==energy['raw_hashes_sha256']]
            if len(hash_paths)!=1 or digest(hash_paths[0])!=energy['raw_hashes_sha256']:raise ValueError('Energy raw hashes changed')
            raw=hash_paths[0].parent;raw_hashes=load(hash_paths[0])
            for name,key in (('GPU_TELEMETRY.jsonl','telemetry_sha256'),('HTTP_RESULTS.jsonl','requests_sha256')):
                if digest(raw/name)!=energy[key] or raw_hashes.get(name)!=energy[key]:raise ValueError('Energy source changed')
            telemetry=[json.loads(line) for line in (raw/'GPU_TELEMETRY.jsonl').read_text().splitlines()]
            requests=[row for row in (json.loads(line) for line in (raw/'HTTP_RESULTS.jsonl').read_text().splitlines()) if row.get('kind') in ('coding','native_tool')]
            for arm,data in energy['arms'].items():
                comparison=v['comparison']
                selected=[row['id'] for row in requests if ident in ('R604','R605') or row['id'].endswith('--'+arm)]
                bounds=counter_energy_bounds(telemetry,requests,selected)
                solved=original['quality']['candidate_successes'] if ident in ('R604','R605') else sum(v['successes'] for v in original['quality'][arm].values())
                if bounds!=data['counter_bounds'] or data['successful_tasks']!=solved or solved<=0 or data['gpu_joules_per_success_lower']!=bounds['lower_j']/solved or data['gpu_joules_per_success_upper']!=bounds['upper_j']/solved or comparison.get('counter_gpu_j_per_success_lower_'+arm)!=data['gpu_joules_per_success_lower'] or comparison.get('counter_gpu_j_per_success_upper_'+arm)!=data['gpu_joules_per_success_upper']:
                    raise ValueError('Energy counter projection differs')
            if ident=='R604':
                reference=energy['historical_control']
                original_control=load(root/'staging/r487/AUDIT.json')['all_completed_arms']['C']
                if digest(root/'staging/r487/AUDIT.json')!=load(root/'staging/r604/PLAN.json')['control_audit_sha256'] or reference['counter_bounds']!=original_control['GPU_counter'] or reference['successful_tasks']!=original_control['successes'] or reference['gpu_joules_per_success_lower']!=reference['counter_bounds']['lower_j']/reference['successful_tasks'] or reference['gpu_joules_per_success_upper']!=reference['counter_bounds']['upper_j']/reference['successful_tasks'] or v['comparison'].get('counter_gpu_j_per_success_lower_reference')!=reference['gpu_joules_per_success_lower'] or v['comparison'].get('counter_gpu_j_per_success_upper_reference')!=reference['gpu_joules_per_success_upper']:
                    raise ValueError('Historical energy reference differs')
            if ident=='R605':
                reference=energy['historical_control'];baseline=root/'staging/r503/AUDIT.json';record=load(baseline)
                solved=sum(record['groups'][name]['successes'] for name in ('coding','tools'))
                lower=sum(record['groups'][name]['GPU_counter']['lower_j'] for name in ('coding','tools'))/solved
                upper=sum(record['groups'][name]['GPU_counter']['upper_j'] for name in ('coding','tools'))/solved
                if digest(baseline)!=load(root/'staging/r605/PLAN.json')['reference_audit_sha256'] or reference['audit_sha256']!=digest(baseline) or reference['successful_tasks']!=solved or reference['gpu_joules_per_success_lower']!=lower or reference['gpu_joules_per_success_upper']!=upper or v['comparison'].get('counter_gpu_j_per_success_lower_reference')!=lower or v['comparison'].get('counter_gpu_j_per_success_upper_reference')!=upper:
                    raise ValueError('Historical Gemma energy reference differs')
            experiments[ident]['related_audit_ids']=[review_id]
        if audit and ident=='R546' and v.get('status') in ('FRESH_TOOLS_AB400_COMPLETE','PARTIAL'):
            confirmed=verified_native_tools_confirmation(root,v,receipt)
            experiments[ident]['aggregate_metrics']['native_tools_confirmation']=confirmed
            catalog[audit]['aggregate_metrics']['native_tools_confirmation']=confirmed
        if audit and v.get('status')=='DEVELOPMENT_ROLE_COMPARISON5_COMPLETE':
            role=verified_native_role_comparison(root,v,receipt)
            experiments[ident]['aggregate_metrics']['native_role_comparison_development']=role
            experiments[ident]['model']=role['model'];experiments[ident]['date']=text(load(locations[audit]).get('at_utc'))
            catalog[audit]['aggregate_metrics']['native_role_comparison_development']=role
            experiments[ident]['related_audit_ids']=[role[k] for k in ('quality_audit_id','independent_review_audit_id','correction_audit_id')]
        if audit and v.get('status') in ('LEAN_HARNESS_DEVELOPMENT66_COMPLETE','LEAN_HARNESS_SCREEN33_COMPLETE'):
            lean=verified_native_lean_harness(root,v,receipt)
            key='native_lean_harness_screen' if lean['screen_only'] else 'native_lean_harness_ablation'
            experiments[ident]['aggregate_metrics'][key]=lean
            catalog[audit]['aggregate_metrics'][key]=lean
            if lean['dataset_id']=='jarvis-original-caveman-node-shrink-screen33-v1':
                metadata=load(locations[audit]);assert metadata['factor']=='A03' and metadata['factor_coverage_increment']==0
                experiments[ident].update(model=lean['model'],date=text(metadata['at_utc']),factor_ids=['A03'])
            elif lean['dataset_id']=='jarvis-original-miniswe-native-screen33-v1':
                metadata=load(locations[audit]);assert metadata['factor']=='M07' and metadata['factor_coverage_increment']==0
                experiments[ident].update(model=lean['model'],date=text(metadata['at_utc']),factor_ids=['M07'])
            experiments[ident]['related_audit_ids']=[lean[k] for k in ('quality_audit_id','independent_review_audit_id','comparison_audit_id','correction_audit_id') if lean.get(k)]
        native_key=next((key for key in ('native_lean_reserved_validation33','native_validation33','native_agent18_development') if catalog.get(audit,{}).get('aggregate_metrics',{}).get(key)), 'native_agent18_development')
        if audit and catalog[audit]['aggregate_metrics'].get(native_key):
            experiments[ident]['aggregate_metrics'][native_key]=verified_native_agent_development(root,v,receipt)
            experiments[ident]['model']=text(load(locations[audit]).get('model'));experiments[ident]['date']=text(load(locations[audit]).get('at_utc'))
            for kind in ('quality_review','comparison_review','output_limit_review','context_review','cohort_review'):
                if v.get(kind+'_path'):
                    supplemental=load(pathlib.Path(v[kind+'_path']))
                    assert supplemental['experiment_id']==ident and (supplemental.get('source_audit_sha256') or supplemental.get('candidate_audit_sha256'))==v['audit_sha256']
                    sid=receipt(v[kind+'_path'],v[kind+'_sha256']);assert sid
                    experiments[ident].setdefault('related_audit_ids',[]).append(sid)
                    if kind=='cohort_review':
                        assert verify_native_grouped_review(root,supplemental,db['summary'])
                        experiments[ident]['native_agent_grouped_review']={'audit_id':sid,'aggregate_metrics':catalog[sid]['aggregate_metrics']}


        if v.get('development_comparison_review'):
            if ident=='R539':experiments[ident]['mtp_development_comparison']=mtp_development_result(root,v['development_comparison_review'],receipt)
            else:experiments[ident]['development_comparison']=development_result(root,v['development_comparison_review'],receipt)
        if v.get('mtp_confirmation_review'):
            experiments[ident]['mtp_confirmation']=verified_mtp_confirmation_result(root,v['mtp_confirmation_review'],receipt)
        if v.get('qualification_review_path'):
            experiments[ident]['qualification_review']=verified_qualification_review(root,{**v,'experiment_id':ident},receipt)
        if v.get('coding_mtp_comparison_review'):
            experiments[ident]['coding_mtp_comparison']=verified_coding_mtp_comparison(root,v['coding_mtp_comparison_review'],receipt)
        if v.get('tools_mtp_comparison_review'):
            experiments[ident]['tools_mtp_comparison']=verified_coding_mtp_comparison(root,v['tools_mtp_comparison_review'],receipt,candidate='R542')
        if isinstance(v.get('audit_correction_path'),str) and re.fullmatch('[a-f0-9]{64}',str(v.get('audit_correction_sha256',''))):
            correction_id=receipt(v['audit_correction_path'],v['audit_correction_sha256'])
            if correction_id:
                experiments[ident]['independent_review']={'audit_id':correction_id,'statements':catalog[correction_id]['statements'],'aggregate_metrics':catalog[correction_id]['aggregate_metrics']}
                experiments[ident].setdefault('related_audit_ids',[]).append(correction_id)
        if v.get('factor_mapping_correction'):
            experiments[ident]['factor_mapping_correction']=factor_assignment(v)
            experiments[ident]['factor_ids']=experiments[ident]['factor_mapping_correction']['current_factor_ids']
        package=v.get('source_package')
        if isinstance(package,dict) and re.fullmatch('[a-f0-9]{64}',str(package.get('wheel_sha256',''))):
            experiments[ident]['source_package']={'name':text(package.get('name')),'version':text(package.get('version')),'url':url(package.get('url')),'license':text(package.get('license')),'wheel_sha256':package['wheel_sha256']}
    for f in factors:
        for aid in f['evidence_ids']:
            p=locations[aid];match=re.search(r'(?:^|/)r(\d+)(?:[-/]|$)',str(p),re.I)
            if match:
                ident='R'+str(int(match[1]));factor_links[ident].add(f['id'])
                if ident in experiments and not experiments[ident].get('audit_id'):
                    experiments[ident]['audit_id']=aid;experiments[ident]['evidence_status']='ORIGINAL_AUDIT_HASH_VERIFIED'
                if ident not in experiments:experiments[ident]={'id':ident,'factor_ids':[],'audit_id':aid,'related_audit_ids':[],'evidence_status':'ORIGINAL_AUDIT_HASH_VERIFIED','statements':catalog[aid]['statements'],'aggregate_metrics':catalog[aid]['aggregate_metrics'],'winner_qualified':False,'model':None,'date':None,'reference_A0':None}
                if aid not in experiments[ident].setdefault('related_audit_ids',[]):experiments[ident]['related_audit_ids'].append(aid)
                if ident=='R407' and p.name=='INDEPENDENT_REVIEW.json':experiments[ident]['independent_review']={'audit_id':aid,'statements':catalog[aid]['statements'],'aggregate_metrics':catalog[aid]['aggregate_metrics']}
                if ident=='R407' and p.name=='AUDIT.json':
                    experiments[ident]['factor_ids']=['K05'];experiments[ident]['model']='OmniCoder2';experiments[ident]['date']='2026-10-22'
        for exp in experiments.values():
            if f['id'] in exp['factor_ids'] or f['id'] in factor_links[exp['id']]:f['experiment_ids'].append(exp['id'])
    events=[]
    for line in ledger:
        e=json.loads(line);details=e.get('details') or {};details=details if isinstance(details,dict) else {};exp=details.get('experiment_id',e.get('experiment_id'));kind=e.get('kind','UNKNOWN')
        if not isinstance(kind,str) or not re.fullmatch('[A-Za-z0-9_:. -]{1,180}',kind):kind='REDACTED_EVENT_KIND'
        events.append({'sequence':len(events)+1,'date':text(e.get('at_utc')),'kind':kind,'experiment_id':exp if isinstance(exp,str) and re.fullmatch('R[0-9]+',exp) else None,'signature':e.get('signature') if isinstance(e.get('signature'),str) and re.fullmatch('[a-f0-9]{64}',e['signature']) else None,'factor_id':e.get('factor_id') if isinstance(e.get('factor_id'),str) and re.fullmatch('[A-Z]+[0-9]+|BASELINE',e['factor_id']) else None})
    windows=[]
    for w in db['summary']['matrix_130_reconciliation']['windows']:
        signature=w['signature'];path=w.get('result_path') or w.get('path');ident=receipt(path) if isinstance(path,str) else None
        # Reconciler paths can be window directories; use the exact canonical signature.
        if not ident:
            for base in [root,root.parent/'phase_o1_experiments']:
                pp=base/'windows'/signature[:16]/'RESULTS.json'
                if pp.is_file():ident=receipt(pp);break
        windows.append({'id':'W-'+signature[:16],'signature':signature,'factor_id':w.get('factor_id',w.get('factor')),'status':text(w.get('result_status')),'audit_id':ident,'scope':'Historical signed window; not an additional factor or independent qualification.'})
    references=[]
    for ident,v in db['records'].items():
        identity=v.get('identity',{}); hashes={}
        def hashes_only(x,prefix=''):
            if isinstance(x,dict):
                for k,z in x.items():
                    if isinstance(z,str) and re.fullmatch('[a-f0-9]{64}',z):hashes.setdefault(z,True)
                    elif isinstance(z,(dict,list)):hashes_only(z)
            elif isinstance(x,list):
                for z in x:hashes_only(z)
        hashes_only(identity)
        public_identity={k:projection(z) if not isinstance(z,str) else text(z) for k,z in identity.items() if k in {'cuda_toolkit','engine_build','cache','context','ctx_size','batch','ubatch','threads','sampler','clock_conditions','power_limit_w','n_gpu_layers','temperature','seed','quantization','KV','kv','mtp','max_draft','model_sha256','cases_sha256','benchmark_profile'}}
        launch=identity.get('launch',{})
        argv=launch.get('argv',[]) if isinstance(launch,dict) else []
        allowed_flags={'--ctx-size','--parallel','--n-gpu-layers','--threads','--threads-batch','--batch-size','--ubatch-size','--seed','--ctx-checkpoints','--cache-ram','--cache-reuse','--reasoning','--load-mode','--flash-attn','--cache-type-k','--cache-type-v','--draft-max','--draft-min','--draft-p-min','--spec-type','--n-draft'}
        safe_argv={}
        for pos,arg in enumerate(argv):
            if arg in allowed_flags and pos+1<len(argv) and re.fullmatch('[A-Za-z0-9_.+-]{1,48}',str(argv[pos+1])):safe_argv[arg]=argv[pos+1]
        public_identity['inference_flags']=safe_argv
        public_identity['request_numeric_settings']=projection(identity.get('request_settings'))
        env=launch.get('environment',{}) if isinstance(launch,dict) else {}
        public_identity['kernel_switches']={k:v for k,v in env.items() if k in {'GGML_CUDA_GRAPH_OPT','GGML_CUDA_O2_WEIGHT_CACHE_MIB','GGML_CUDA_DISABLE_GRAPHS','GGML_CUDA_FORCE_MMQ','GGML_CUDA_FORCE_CUBLAS'} and re.fullmatch('[0-9]+',str(v))}
        public_identity['workload_description']=text(identity.get('workloads'))
        references.append({'id':ident,'model':text(v.get('model')),'experiment_id':text(v.get('experiment_id')),'profile':text(v.get('profile')),'kind':text(v.get('kind')),'winner_qualified':v.get('winner_qualified') is True,'qualification':text(v.get('qualification')),'aggregate_metrics':metrics(v),'identity':public_identity,'identity_hashes':sorted(hashes),'identity_completeness':'PUBLIC_SUBSET; original hash binds full private record','limits':[text(x) for x in v.get('limits',[]) if isinstance(x,str)]})
    profiles=[{'id':k,'A0':v['A0'],'C':v.get('C'),'scope':'Champion only in this exact profile; no automatic production deployment.'} for k,v in db['profiles'].items()]
    challengers=[]
    for x in matrix['model_challengers']:
        challengers.append({'id':x['id'],'name':text(x['title']),'repository':url(x.get('repo')),'status':text(x.get('current_work_status',x.get('status'))),'priority':x.get('current_priority_band',x.get('priority_band')),'assessment':text(x.get('current_assessment_de',x.get('interpretation'))),'next_step':text(x.get('current_next_step_de',x.get('admission_test'))),'evidence_class':text(x.get('evidence_class')),'source_admission':projection(x.get('source_admission')),'local_scope':projection(x.get('local_evidence')),'current_experiment':text(x.get('current_experiment'))})
    sources=[]
    for x in matrix.get('research_source_integration_20261021',{}).get('sources',[]):
        source={'id':x['id'],'url':url(x['url']),'revision':text(x['revision']),'classification':x['classification'],'axes':x['linked_original_axes'],'scope':text(x['review_scope']),'obstacles':[text(y) for y in x.get('obstacles',[])],'evidence_class':'EXTERN_BELEGT','local_test_status':x['local_test_status']}
        if isinstance(x.get('content_sha256'),str) and re.fullmatch('[a-f0-9]{64}',x['content_sha256']):source['content_sha256']=x['content_sha256']
        sources.append(source)
    for source_id,name in [('VOLTA_MICROARCH','volta-paper-abs.html'),('HBM_POWER','hbm-paper-abs.html')]:
        original=root/'staging/r340/sources'/name
        if original.is_file():
            raw=original.read_text();metadata={}
            for key,value in re.findall(r'<meta name="(citation_[^"]+)" content="([^"]*)"',raw):metadata.setdefault(key,[]).append(html.unescape(value))
            for source in sources:
                if source['id']==source_id:source['bibliography']={k.replace('citation_',''):v for k,v in metadata.items() if k in {'citation_title','citation_author','citation_date','citation_arxiv_id','citation_pdf_url'}};source['bibliographic_source_sha256']=digest(original)
    subcases=[]
    for x in matrix.get('research_source_integration_20261021',{}).get('subcases',[]):
        subcases.append({k:text(x.get(k)) for k in ['id','title','classification','priority_band','mechanism','prerequisites','test_design','risks','decision','next_action','expected_knowledge_gain','local_test_status']} | {'axes':x['linked_original_axes'],'sources':x['source_ids'],'counts_as_factor':False})
    export_harness_sources(root,db,experiments)
    from comparison import build as build_comparison
    comparison=build_comparison(root,db,matrix,receipt)
    from leaderboard import build as build_leaderboard
    previous_file=HERE/'data/configuration-history.json'
    register,configuration_history=build_leaderboard(root,db,comparison,list(experiments.values()),receipt,text,load(previous_file) if previous_file.exists() else None)
    snapshot={'schema':1,'matrix_revision':matrix['revision'],'source_sha256':source_hashes,'source_date':matrix.get('updated_at_utc') or matrix['factor_accountability_summary']['at_utc'],'counts':{'original_factors':130,'additional_factors':32,'factors':len(factors),'model_challengers':len(challengers),'assessed_factors':len(factors),'experimentally_covered':sum(x['experimentally_covered'] for x in factors),'omnicoder2_experimentally_covered':sum(x['omnicoder2_experimentally_covered'] for x in factors),'scientific_status':dict(collections.Counter(x['status'] for x in factors)),'sprint_records':len(experiments),'signed_windows':len(windows),'ledger_events':len(events),'reference_records':len(references),'qualified_profile_pointers':sum(bool(x['C']) for x in profiles)},'limitations':['An assessed factor is not a hardware experiment. A sprint ID may describe a build, source review or failed attempt.','GPU intervention count: NOT MEASURED AS ONE COMPARABLE TOTAL. Component processes, model sessions and requests remain separate in each original audit.','A redacted excerpt cannot reproduce the original SHA256. That SHA binds the retained original; exported bytes have their own manifest.','Canonical rationale excerpts may remain in their original German. Surrounding documentation is English.','No private benchmark prompts, tool entities, model outputs, logs, host paths, GPU UUIDs or model weights are distributed. Exact task-level reproduction therefore remains incomplete for withheld local suites.']}
    snapshot['lean_harness_review']=project_lean_research(root,receipt)
    from reproducibility import build as build_reproducibility
    snapshot['reproducibility_review']=build_reproducibility(root)
    assert snapshot['counts']['factors']==162 and len(challengers)==11
    for name,obj in [('snapshot.json',snapshot),('factors.json',factors),('experiments.json',sorted(experiments.values(),key=lambda x:int(x['id'][1:]))),('audit-excerpts.json',list(catalog.values())),('signed-windows.json',windows),('history.json',events),('references.json',references),('profiles.json',profiles),('models.json',challengers),('comparison.json',comparison),('benchmark-register.json',register),('configuration-history.json',configuration_history),('model-benchmarks.json',metrics({'model_comparison_progress':db['summary'].get('model_comparison_progress',{})})),('sources.json',sources),('research-subcases.json',subcases)]:write(name,obj)
    from screening import build as build_screening
    write('screening.json',build_screening(root))
    timing_file=root.parent/'.public-sync/pipeline-status.json'
    if timing_file.is_file():
        from pipeline import project as project_pipeline
        timing=load(timing_file)
        for record in timing['experiments']:
            assert re.fullmatch(r'R[1-9][0-9]{1,3}',record['experiment_id'])
            assert digest(root/'staging'/record['experiment_id'].lower()/'AUDIT.json')==record['source_audit_sha256']
        write('pipeline-performance.json',project_pipeline(timing))
    # Local-only export receipt records the original locations; never place it in the public tree.
    receiptfile=HERE.parent/'PUBLIC_EXPORT_PRIVATE_RECEIPT.json';receiptfile.write_text(json.dumps({'source_revision':matrix['revision'],'source_sha256':source_hashes,'selected_original_paths_and_hashes':verified},indent=2)+'\n');receiptfile.chmod(0o600)
    print(json.dumps(snapshot['counts'],sort_keys=True))
if __name__=='__main__':main()
