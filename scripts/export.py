#!/usr/bin/env python3
"""Publish-schema projection. Reads canonical metadata, never copies files or logs.
No source code execution, downloads, GPU requests, or source mutations.
"""
import argparse, collections, fcntl, hashlib, html, json, math, pathlib, re, sys
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
METRIC_ROOTS |= {'prefill_geomean_E2E_change_percent','actual_private_cublas126'}
DOMAINS.add('pypi.org')
DOMAINS.update({'gist.github.com','images.nvidia.com'})
METRIC_ROOTS |= {'object_size_change_percent','decoded_cubin_byte_identity','decoded_PTX_byte_identity','explicit_NVCCflag_applied','original_inputs_preserved'}
METRIC_ROOTS |= {'baseline','binary','reference_only_calibration','actual_reference_GPU_inference','actual_candidate_GPU_execution','candidate_model_starts','source_cases','authorized_cases','denied_cases','baseline_primary_dispatch_events','candidate_primary_dispatch_events','before_commit_process_crash_controls','after_commit_process_crash_controls','authority_revocation_controls','malformed_envelope_controls','separate_session_controls','denied_deliveries','component_wall_s'}
# Explicit numeric aggregate fields for speculation memory/task-cost screens.
METRIC_ROOTS |= {'prefix_envelopes_same','actual_history_requests','critical_matches_previous_valid','critical_matches_previous_bad','critical_prompt_tokens','critical_output_tokens','concurrent_generation_requests','other_slot_erased','actual_managed_allocator','CT_memory_observed','decode_e2e_reduction_percent_vs_A0','actual_ngram_draft','memory_saved_vs_R244_device_mib','memory_saved_vs_R245_device_mib','successful_task_wall_s','successful_task_cost_change_percent_vs_R245','gpu_energy_j_approx','observed_tasks','full18_score_claimed','model_requests','actual_ngram_proposals_observed','timing_confirmation_needed','fixed_parameters'}
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
def metrics(obj):
    result={k:projection(v) for k,v in obj.items() if k in METRIC_ROOTS and projection(v) is not None}
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
    return {k:text(obj[k]) for k in ['decision','qualification','interpretation','hypothesis','research_question','scope','measurement_type','evidence_class','score_rule'] if isinstance(obj.get(k),str)} | {k:[text(x) for x in obj[k] if isinstance(x,str)] for k in ['limits','limitations'] if isinstance(obj.get(k),list)}
def write(name,obj):
    p=HERE/'data'/name;p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n')
def main():
    arg=argparse.ArgumentParser();arg.add_argument('--source',required=True,type=pathlib.Path);args=arg.parse_args();root=args.source.resolve()
    for name in ['MATRIX.json','MATRIX_EXTENDED.json','QUEUE.json','BENCHMARK_REFERENCES.json','O2_EXPERIMENTS.jsonl']:
        if not (root/name).is_file(): raise ValueError('Missing canonical input: '+name)
    # Same existing project lock, short read-only snapshot; never interrupt an experiment.
    with (root/'source-handoff.lock').open('r') as lock:
        fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)
        originals=load(root/'MATRIX.json');matrix=load(root/'MATRIX_EXTENDED.json');db=load(root/'BENCHMARK_REFERENCES.json');ledger=(root/'O2_EXPERIMENTS.jsonl').read_text().splitlines()
        source_hashes={n:digest(root/n) for n in ['MATRIX.json','MATRIX_EXTENDED.json','QUEUE.json','BENCHMARK_REFERENCES.json','O2_EXPERIMENTS.jsonl']}
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
                if ident not in experiments:experiments[ident]={'id':ident,'factor_ids':[],'audit_id':aid,'evidence_status':'ORIGINAL_AUDIT_HASH_VERIFIED','statements':catalog[aid]['statements'],'aggregate_metrics':catalog[aid]['aggregate_metrics'],'winner_qualified':False,'model':None,'date':None,'reference_A0':None}
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
    snapshot={'schema':1,'matrix_revision':matrix['revision'],'source_sha256':source_hashes,'source_date':matrix.get('updated_at_utc') or matrix['factor_accountability_summary']['at_utc'],'counts':{'original_factors':130,'additional_factors':32,'factors':len(factors),'model_challengers':len(challengers),'assessed_factors':len(factors),'experimentally_covered':sum(x['experimentally_covered'] for x in factors),'omnicoder2_experimentally_covered':sum(x['omnicoder2_experimentally_covered'] for x in factors),'scientific_status':dict(collections.Counter(x['status'] for x in factors)),'sprint_records':len(experiments),'signed_windows':len(windows),'ledger_events':len(events),'reference_records':len(references),'qualified_profile_pointers':sum(bool(x['C']) for x in profiles)},'limitations':['An assessed factor is not a hardware experiment. A sprint ID may describe a build, source review or failed attempt.','GPU intervention count: NOT MEASURED AS ONE COMPARABLE TOTAL. Component processes, model sessions and requests remain separate in each original audit.','A redacted excerpt cannot reproduce the original SHA256. That SHA binds the retained original; exported bytes have their own manifest.','Canonical rationale excerpts may remain in their original German. Surrounding documentation is English.','No private benchmark prompts, tool entities, model outputs, logs, host paths, GPU UUIDs or model weights are distributed. Exact task-level reproduction therefore remains incomplete for withheld local suites.']}
    assert snapshot['counts']['factors']==162 and len(challengers)==11
    for name,obj in [('snapshot.json',snapshot),('factors.json',factors),('experiments.json',sorted(experiments.values(),key=lambda x:int(x['id'][1:]))),('audit-excerpts.json',list(catalog.values())),('signed-windows.json',windows),('history.json',events),('references.json',references),('profiles.json',profiles),('models.json',challengers),('model-benchmarks.json',metrics({'model_comparison_progress':db['summary'].get('model_comparison_progress',{})})),('sources.json',sources),('research-subcases.json',subcases)]:write(name,obj)
    # Local-only export receipt records the original locations; never place it in the public tree.
    receiptfile=HERE.parent/'PUBLIC_EXPORT_PRIVATE_RECEIPT.json';receiptfile.write_text(json.dumps({'source_revision':matrix['revision'],'source_sha256':source_hashes,'selected_original_paths_and_hashes':verified},indent=2)+'\n');receiptfile.chmod(0o600)
    print(json.dumps(snapshot['counts'],sort_keys=True))
if __name__=='__main__':main()
