import importlib.util,pathlib,unittest
P=pathlib.Path(__file__).resolve().parent
def module(name):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module('validate');e=module('export')
class PublicationSafety(unittest.TestCase):
 def test_native_experiment_pages_show_registered_full_and_partial_results(self):
  import json
  root=P.parent;history=json.loads((root/'data/configuration-history.json').read_text())
  for experiment in ('R481','R482'):
   runs=[r for r in history['runs'] if r['experiment_id']==experiment];self.assertTrue(runs)
   page=(root/'docs/experiments'/f'{experiment}.md').read_text()
   for run in runs:
    self.assertIn(str(run['solved'])+'/'+str(run['tasks']),page)
    self.assertIn(run['status'],page);self.assertIn(run['benchmark_identity_id'],page)
    self.assertIn(run['runtime_configuration_id'],page)
    for audit in run['audit_ids']:self.assertIn(audit,page)
 def test_compact_history_preserves_every_value_within_existing_file_budget(self):
  import json,tempfile
  from unittest.mock import patch
  data={'profiles':[{'id':'x','unknown':None,'disabled':False,'text':'ä\ntext','score':85.0}], 'runs':[{'ids':['R1','R2']}]}
  with tempfile.TemporaryDirectory() as directory,patch.object(e,'HERE',pathlib.Path(directory)):
   e.write('configuration-history.json',data)
   raw=(pathlib.Path(directory)/'data/configuration-history.json').read_text()
   self.assertEqual(json.loads(raw),data)
   self.assertEqual(raw.count('\n'),1)
   self.assertLess(len(raw),len(json.dumps(data,indent=2)))
   with self.assertRaises(ValueError):e.write('configuration-history.json',{'score':float('nan')})
 def test_budget_partial_exports_counts_and_costs_without_private_responses(self):
  raw={'status':'STOPPED_USER_WHOLE_BENCHMARK_TIME_BUDGET','full_benchmark_score_claimed':False,'expected_tasks':164,'collected_tasks':140,'scored_tasks':140,'solved_observed_tasks':99,'prefix_measurement':{'case_inference_wall_s':751.5,'case_gpu_energy_j':148069.1,'per_task':[{'response':'private text','address':'sensitive-network-value'}],'prompt_token_ids':[123]}}
  out=e.metrics(raw);part=out['partial_benchmark_evidence'];self.assertEqual(part['solved_observed_tasks'],99);self.assertEqual(part['request_interval_wall_s'],751.5);self.assertFalse(part['full_benchmark_score_claimed']);self.assertNotIn('private',str(out));self.assertNotIn('sensitive-network-value',str(out));self.assertNotIn('token_ids',str(out))
  raw['solved_observed_tasks']=141;self.assertNotIn('partial_benchmark_evidence',e.metrics(raw))
 def test_context_capacity_exports_only_valid_ranges_and_aggregate_denominators(self):
  raw={'factor':'R19','context_tokens':32768,'observed_cases':2,'planned_cases':12,'scopes':{'common':{'observed':12,'solved':12,'actual_input_token_range':[14743,14817],'per_task':[{'prompt':'private prompt','token_ids':[1,2]}]},'extended':{'observed':2,'solved':2,'actual_input_token_range':[29500,29600],'messages':['private answer']},'untrusted':{'actual_input_token_range':[1,2]}},'responses':['private']}
  out=e.metrics(raw);self.assertEqual(out['observed_cases'],2);self.assertEqual(out['planned_cases'],12);self.assertEqual(out['context_profile_token_ranges']['extended']['minimum_tokens'],29500);self.assertNotIn('private',str(out));self.assertNotIn('per_task',str(out));self.assertNotIn('token_ids',str(out));self.assertNotIn('untrusted',out['context_profile_token_ranges'])
  raw['scopes']['extended']['actual_input_token_range']=[1,40000];self.assertNotIn('extended',e.metrics(raw)['context_profile_token_ranges'])
 def test_r407_independent_review_exports_scope_correction_without_payloads(self):
  raw={'scope_correction':'Frozen plan text overstates the slot assignment; use immutable targets instead.','history_slot_targets':{'slot0':12,'slot1':9,'ordinal_ranges':'0-8 slot0; 9-17 slot1; 18-20 slot0'},'treatment_comparison':'Slot0 snapshot unchanged across Slot1 erase.','slot1_erase_confirmed_n_erased':3248,'data_leak_or_GDN_bug_proven':False,'full_isolation_or_quality_qualification':False,'private_path':'/'+'opt/private/audit.json','prompt':'private text'}
  out=e.snippets(raw);self.assertEqual(out['history_slot_targets']['slot0'],12);self.assertEqual(out['history_slot_targets']['slot1'],9);self.assertIn('scope_correction',out);self.assertFalse(out['data_leak_or_GDN_bug_proven']);self.assertNotIn('private_path',str(out));self.assertNotIn('private text',str(out))
 def test_r405_exports_only_aggregate_confirmation_metrics(self):
  raw={'experiment_id':'R405','factor':'A02','arm_totals':{'A0':{'tasks':12,'successes':0,'wall_s_sum':48.259,'prompt_tokens':87160},'B':{'tasks':12,'successes':4,'wall_s_sum':13.977,'prompt_tokens':5876}},'arm_GPU_energy':{'A0':{'gpu_energy_j':13105.0},'B':{'gpu_energy_j':3735.0}},'comparisons':{'positive_successes_A0':0,'positive_successes_B':0,'negative_false_calls_A0':4,'negative_false_calls_B':0,'gained_tasks':4,'lost_tasks':0},'aggregate_latency_gain_fraction':0.710375,'peak_GPU_VRAM_bytes':8542224384,'max_GPU_temperature_c':64,'responses':['private response']}
  out=e.metrics(raw)['A02_BMT07_independent_confirmation'];self.assertEqual(out['baseline']['successes'],0);self.assertEqual(out['candidate']['successes'],4);self.assertEqual(out['positive_case_successes'],{'A0':0,'B':0});self.assertEqual(out['negative_false_tool_calls'],{'A0':4,'B':0});self.assertEqual(out['GPU_energy_j_by_arm'],{'A0':13105.0,'B':3735.0});self.assertFalse(out['winner_qualified']);self.assertNotIn('private',str(out));self.assertNotIn('prompt_tokens',str(out))
 def test_r405_audit_excerpt_preserves_baseline_errors_and_candidate_gains(self):
  raw={'experiment_id':'R405','factor':'A02','arm_totals':{'A0':{'tasks':12,'successes':0,'wall_s_sum':48.259},'B':{'tasks':12,'successes':4,'wall_s_sum':13.977}},'false_positive_negative_calls':[{'arm':'A0','calls':['synthetic-private-call']}],'candidate_false_positive_negative_calls':[],'task_success_gained':['private-task-1','private-task-2','private-task-3','private-task-4'],'task_success_lost':[],'aggregate_latency_gain_fraction':0.710375,'arm_GPU_energy':{'A0':{'gpu_energy_j':13105.0},'B':{'gpu_energy_j':3735.0}},'peak_GPU_VRAM_bytes':8542224384,'max_GPU_temperature_c':64}
  out=e.metrics(raw)['A02_BMT07_independent_confirmation'];self.assertEqual(out['gained_tasks'],4);self.assertEqual(out['negative_false_tool_calls'],{'A0':1,'B':0});self.assertNotIn('synthetic-private-call',str(out));self.assertNotIn('private-task',str(out))
 def test_awq_proxy_never_exports_scales_weights_or_development_prompts(self):
  raw={'measurement_type':'CPU_FIRST_MLP_NATIVE_Q4K_AWQ_INPUT_SCALING_PROXY','GPU_runs':0,'proxy_gate_passed':False,'development_evaluated':True,'development_error_reduction_percent':4.9243,'source_quantization':'Q6_K','target_quantization':'Q4_K','scales':['private vector'],'weights':['private tensor'],'fit_data':'private corpus','cases':[{'prompt':'private conversation'}]}
  out=e.metrics(raw)['CPU_first_MLP_AWQ_proxy'];self.assertFalse(out['proxy_gate_passed']);self.assertEqual(out['GPU_runs'],0);self.assertEqual(out['development_error_reduction_percent'],4.9243);self.assertNotIn('private',str(out));self.assertNotIn('scales',str(out));self.assertNotIn('weights',str(out))
 def test_awq_unexecuted_development_does_not_export_a_success_or_error_gain(self):
  raw={'measurement_type':'CPU_FIRST_MLP_NATIVE_Q4K_AWQ_INPUT_SCALING_PROXY','development_evaluated':False,'proxy_gate_passed':True,'development_error_ratio':0,'development_error_reduction_percent':100}
  out=e.metrics(raw)['CPU_first_MLP_AWQ_proxy'];self.assertFalse(out['proxy_gate_passed']);self.assertNotIn('development_error_ratio',out);self.assertNotIn('development_error_reduction_percent',out)
 def test_mlp_calibration_exports_counts_without_calibration_channel_vectors(self):
  raw={'measurement_type':'GPU_NATIVE_FIRST_MLP_INPUT_FORWARD_OBSERVER_ADMISSION','model_starts':1,'actual_generation_requests':0,'completed_chunks':4,'calibration_fidelity_passed':True,'meanabs_channels':4096,'quantizer_fits':0,'winner_qualified':False,'channel_meanabs':['private vector'],'raw_capture_sha256':{'private file':'private hash'},'observations':[{'chunk':0,'tokens':512,'control_logits_byte_identical':True,'input_token_ids':[1],'raw_activations':['private tensor']}]}
  out=e.metrics(raw)['forward_MLP_calibration_admission'];self.assertEqual(out['meanabs_channels'],4096);self.assertEqual(out['quantizer_fits'],0);self.assertEqual(out['actual_generation_requests'],0);self.assertFalse(out['winner_qualified']);self.assertNotIn('private',str(out));self.assertNotIn('input_token_ids',str(out));self.assertNotIn('channel_meanabs',str(out))
 def test_nuq_proxy_exports_errors_without_private_codebooks_or_samples(self):
  raw={'measurement_type':'CPU_UNWEIGHTED_NUQ4_DEVELOPMENT_RECONSTRUCTION_PROXY','GPU_runs':0,'model_quality_measured':False,'proxy_error_reduction_percent':33.15,'codebooks':['private values'],'normalizers':['private values'],'probes':['private values'],'cases':[{'layer':3,'role':'K','NUQ_uniform_error_ratio':.67,'centroids':['private values'],'activations':['private values']},{'layer':3,'role':'private label','NUQ_SSE':1}]}
  out=e.metrics(raw)['CPU_NUQ_development_proxy'];self.assertEqual(out['GPU_runs'],0);self.assertFalse(out['model_quality_measured']);self.assertEqual(len(out['numeric_reconstruction_cases']),1);self.assertNotIn('private',str(out));self.assertNotIn('centroids',str(out));self.assertNotIn('activations',str(out));self.assertEqual(out['proxy_error_reduction_percent'],33.15)
 def test_forward_calibration_never_exports_activations_logits_or_calibration_text(self):
  raw={'measurement_type':'GPU_NATIVE_PRE_ROPE_KV_FORWARD_OBSERVER_ADMISSION','model_starts':1,'actual_generation_requests':0,'completed_chunks':4,'calibration_fidelity_passed':True,'new_experimental_factor_coverage':0,'quantizer_fits':0,'winner_qualified':False,'raw_capture_sha256':{'private tensor path':'private hash'},'activations':[1.0],'corpus':'private text','observations':[{'chunk':0,'tokens':512,'control_logits_byte_identical':True,'maximum_abs_logit_difference':0,'raw_logits':[2.0],'tensor_name':'private tensor','input_token_ids':[1,2]}]}
  out=e.metrics(raw)['forward_KV_calibration_admission'];self.assertEqual(out['actual_generation_requests'],0);self.assertEqual(out['new_experimental_factor_coverage'],0);self.assertEqual(out['quantizer_fits'],0);self.assertFalse(out['winner_qualified']);self.assertTrue(out['fidelity_checks'][0]['control_logits_byte_identical']);self.assertNotIn('private',str(out));self.assertNotIn('raw_logits',str(out));self.assertNotIn('input_token_ids',str(out));self.assertNotIn('activations',str(out))
 def test_kivi_component_exports_numeric_shapes_not_private_tensor_payloads(self):
  raw={'measurement_type':'GPU_UPSTREAM_KIVI_2BIT_SM70_COMPONENT_NUMERICAL_ADMISSION','model_starts':0,'actual_GPU_inference':False,'original12_quality_cases':0,'winner_qualified':False,'upstream_commit':'a'*40,'cases':[{'IC':256,'OC':8192,'NMSE':4.3e-8,'synthetic_cache_quantization_NMSE':.101,'residual_buffer_included':False,'role':'private tensor role','tensor_bytes':'private payload','output_token_ids':[1,2]},{'NMSE':float('nan'),'seed':'private secret'}]}
  out=e.metrics(raw)['KIVI_SM70_component'];self.assertFalse(out['actual_GPU_inference']);self.assertFalse(out['winner_qualified']);self.assertEqual(out['model_starts'],0);self.assertEqual(out['original12_quality_cases'],0);self.assertEqual(len(out['numeric_component_cases']),1);self.assertEqual(out['numeric_component_cases'][0]['IC'],256);self.assertEqual(out['numeric_component_cases'][0]['synthetic_cache_quantization_NMSE'],.101);self.assertFalse(out['numeric_component_cases'][0]['residual_buffer_included']);self.assertNotIn('private',str(out));self.assertNotIn('tensor_bytes',str(out))
 def test_llguidance_screen_exports_historical_scope_without_original_answers(self):
  raw={'measurement_type':'GPU_ACTUAL_LLGUIDANCE_TYPED_SCHEMA_QA12_SCREEN','observed_cases':12,'wall_s':6.09,'matched_reference_wall_s':5.12,'screen_passed':False,'winner_qualified':False,'token_distribution_preserved':False,'cases':[{'content':'private original answer','prompt':'private task'}]}
  out=e.metrics(raw)['LLGuidance_QA12_screen'];self.assertFalse(out['winner_qualified']);self.assertFalse(out['token_distribution_preserved']);self.assertFalse(out['screen_passed']);self.assertEqual(out['matched_reference_wall_s'],5.12);self.assertNotIn('private',str(out))
 def test_completion_export_retains_framing_limit_without_outputs(self):
  raw={'measurement_type':'GPU_FIXED_SCHEMA_NATIVE_STOP_FRAMING_SCREEN','timed_pairs':40,'receiver_framing_required':True,'raw_candidate_is_not_complete_JSON':True,'paired_geomean_E2E_change_percent':-4.0,'original12_quality_cases':0,'winner_qualified':False,'responses':[{'content':'private JSON'}],'native_requests':[{'prompt':'private prompt'}]}
  out=e.metrics(raw)['schema_completion_protocol'];self.assertTrue(out['receiver_framing_required']);self.assertTrue(out['raw_candidate_is_not_complete_JSON']);self.assertFalse(out['winner_qualified']);self.assertEqual(out['timed_pairs'],40);self.assertNotIn('private',str(out))
 def test_mock_calibration_never_turns_unrun_holdout_into_zero_risk(self):
  raw={'measurement_type':'GPU_MOCK_ACTION_SELECTIVE_RISK_CALIBRATION_SCREEN','calibration_cases':80,'holdout_pairs':0,'underlying_holdout_decisions_equal':True,'thresholds_fitted':0,'holdout_unsafe_allows_A':None,'holdout_unsafe_allows_B':None,'original12_quality_cases':0,'case_details':[{'trusted':'private context','oracle':'private answer'}]}
  out=e.metrics(raw)['mock_action_calibration'];self.assertIsNone(out['holdout_unsafe_allows_A']);self.assertIsNone(out['holdout_unsafe_allows_B']);self.assertIsNone(out['underlying_holdout_decisions_equal']);self.assertFalse(out['holdout_comparison_performed']);self.assertEqual(out['holdout_pairs'],0);self.assertEqual(out['original12_quality_cases'],0);self.assertNotIn('private',str(out))
 def test_acquisition_export_does_not_publish_token_scores_or_prompts(self):
  raw={'measurement_type':'GPU_HEAD_FREE_PROBABILITY_ACQUISITION_SCREEN','matched_pairs':6,'calibration_fits':0,'original12_quality_cases':0,'comparisons':[{'case':'private prompt label','round':1,'token_IDs_equal':True,'A_e2e_s':1.0,'B_e2e_s':1.1,'token_ids':[1,2],'completion_probabilities':[{'token':'private generated text','logprob':-2}]}]}
  out=e.metrics(raw)['probability_acquisition'];self.assertEqual(out['calibration_fits'],0);self.assertEqual(out['original12_quality_cases'],0);self.assertTrue(out['matched_acquisition_costs'][0]['token_IDs_equal']);self.assertNotIn('private',str(out));self.assertNotIn('token_ids',str(out));self.assertNotIn('logprob',str(out))
 def test_scope_reassessment_exports_only_public_rationale(self):
  raw={'deferral_reassessment_20261022':{'previous_status':'DEFERRED','current_status':'OPEN','priority':'P1','decision':'REOPEN_HEAD_FREE_ONLY','new_GPU_execution':False,'previous_evidence':[{'path':'private evidence path'}],'native_source':'private source payload'}}
  out=e.scope_reassessment(raw);self.assertEqual(out['current_status'],'OPEN');self.assertFalse(out['new_GPU_execution']);self.assertNotIn('private',str(out));self.assertIsNone(e.scope_reassessment({}))
 def test_weighted_V_comparison_publishes_aggregate_errors_without_inputs(self):
  raw={'measurement_type':'GPU_WEIGHTEDV_FP32_EXACT_INPUT_NUMERICAL_SCREEN','native_cases_per_arm':6,'candidate_passed_cases':4,'model_starts':0,'identical_tensor_upload_bytes_SHA_verified':True,'tensor_upload_SHA_records':['private fixture bytes'],'numerical_comparisons':[{'case':'private fixture','A_NMSE':0.00068,'B_NMSE':0.00067,'change_percent':-1.2,'response':'private response'}]}
  out=e.metrics(raw)['weighted_V_precision_component'];self.assertEqual(out['candidate_passed_cases'],4);self.assertEqual(out['model_starts'],0);self.assertTrue(out['identical_tensor_upload_bytes_SHA_verified']);self.assertEqual(out['NMSE_comparisons'][0]['B_NMSE'],0.00067);self.assertNotIn('private',str(out));self.assertNotIn('case',out['NMSE_comparisons'][0])
 def test_corrected_attention_scope_keeps_original_mapping_visible(self):
  raw={'axis_factors':['HBM18'],'original_audit_factor_mapping':{'axis_factors':['C10','K01','HBM08']},'related_factors_not_isolated_treatments':['K01','HBM08'],'factor_mapping_correction':{'reason':'Attention dispatch is not an MMQ tile intervention'}}
  out=e.factor_assignment(raw)
  self.assertEqual(out['current_factor_ids'],['HBM18']);self.assertIn('C10',out['original_audit_factor_ids']);self.assertNotIn('C10',out['current_factor_ids']);self.assertEqual(out['related_context_factor_ids'],['HBM08','K01'])
 def test_native_numerical_counts_exclude_fixture_and_execution_logs(self):
  raw={'numerical_result':{'cases_count':6,'passed_cases':6,'NMSE_limit':0.0005,'cases':['private fixture'],'execution_markers':['private log'],'model_starts':0}}
  self.assertEqual(e.metrics(raw),{'numerical_component':{'cases_count':6,'passed_cases':6,'NMSE_limit':0.0005,'model_starts':0}})
 def test_startup_reference_and_CPU_transport_roles_do_not_leak_payloads(self):
  raw={'baseline':{'model_starts':3,'median_startup_to_first_reply_s':2.47,'startup_range_percent':28.76,'startup_observations':[{'response':'private reply'}],'messages':[{'content':'private conversation'}]},'candidate_model_starts':0,'actual_candidate_GPU_execution':False,'reference_only_calibration':True,'source_cases':24,'candidate_primary_dispatch_events':18,'per_case':[{'reply':'private'}]}
  out=e.metrics(raw)
  self.assertEqual(out['baseline'],{'model_starts':3,'median_startup_to_first_reply_s':2.47,'startup_range_percent':28.76})
  self.assertEqual(out['candidate_model_starts'],0);self.assertFalse(out['actual_candidate_GPU_execution']);self.assertTrue(out['reference_only_calibration']);self.assertEqual(out['candidate_primary_dispatch_events'],18);self.assertNotIn('private',str(out))
 def test_queue_resource_screen_preserves_unmeasured_quality_and_hides_payloads(self):
  raw={'measurement_type':'GPU_C16_FRACTIONAL_QUEUE_MEMORY_SCREEN','variants':[{'value':'0.25x','requests':4,'quality_cases':0,'peak_device_vram_mib':7354.5,'memory_saved_vs_A0_mib':2,'minimum_memory_saving_mib':64,'primary_memory_gate_passed':False,'response':'private text','quality':[{'content':'private reply'}]},{'value':'private-value','requests':4}]}
  out=e.metrics(raw)['queue_memory_variants'];self.assertEqual(len(out),1);self.assertEqual(out[0]['capacity_setting'],'0.25x');self.assertEqual(out[0]['quality_cases'],0);self.assertFalse(out[0]['primary_memory_gate_passed']);self.assertNotIn('private',str(out))
 def test_gemma_power_cycles_export_only_finite_numeric_aggregates(self):
  raw={'factor':'H03','model':'gemma4','unique_tasks':12,'planned_cycles':3,'cycle_metrics':[{'cycle':0,'observed':12,'solved':12,'wall_s':134.0,'gpu_j_per_success':2400,'passed':True,'response':'private reply','case_id':'private id','gpu_energy_j_approx':float('nan')}],'per_task':[{'content':'private'}]}
  out=e.metrics(raw);self.assertEqual(out['unique_tasks'],12);self.assertEqual(out['energy_stability_cycles'],[{'cycle':0,'observed':12,'solved':12,'wall_s':134.0,'gpu_j_per_success':2400,'passed':True}]);self.assertNotIn('private',str(out));self.assertNotIn('nan',str(out))
  raw['cycle_metrics']=[{}]*4;self.assertNotIn('energy_stability_cycles',e.metrics(raw))
 def test_prefix_cache_export_is_aggregate_only(self):
  raw={'extended_technique':'MODEL_BONSAI_PREFIX_REUSE_FIRST3_SCREEN','planned_tasks':3,'full3_score_claimed':True,'wall_reduction_percent_vs_A0':-3.5,'prefix_cache':{'cases_with_hits':3,'requests_with_hits':19,'cached_tokens':41087,'first_turn_cached_tokens':0,'messages':['private'],'private_id':'secret'},'per_case_cache':[{'id':'private','cached_tokens':123}]}
  out=e.metrics(raw);self.assertEqual(out['prefix_cache'],{'cases_with_hits':3,'requests_with_hits':19,'cached_tokens':41087,'first_turn_cached_tokens':0});self.assertEqual(out['wall_reduction_percent_vs_A0'],-3.5);self.assertNotIn('private',str(out));self.assertNotIn('secret',str(out))
 def test_credentials_and_network_are_rejected(self):
  examples=['gh'+'p_'+'A'*30,'-----BEGIN '+'RSA PRIVATE KEY-----','192'+'.168.42.18','sensor'+'.bedroom_temperature','fd00'+':'*2+'12',':'*2+'1','https://user'+':secret'+'@example.com']
  for x in examples:
   with self.subTest(category=examples.index(x)):self.assertTrue(v.content_errors(x))
 def test_projection_cannot_export_conversations(self):
  raw={'metrics':{'solved':13,'tasks':18,'messages':[{'content':'private conversation'}],'prompt_text':'private text','per_task':{'private_entity':{}}},'response':'private output','authorization':'secret'}
  out=e.metrics(raw);self.assertEqual(out,{'metrics':{'solved':13,'tasks':18}})
 def test_speculation_aggregates_do_not_export_token_or_case_details(self):
  raw={'memory_saved_vs_R244_device_mib':1834,'actual_ngram_draft':{'draft_tokens':288,'accepted_tokens':288,'acceptance_percent':100,'output_token_ids':[1,2,3],'prompt':'private text'},'successful_task_wall_s':125.5,'task_metrics':[{'id':'private-case','response':'private'}]}
  self.assertEqual(e.metrics(raw),{'memory_saved_vs_R244_device_mib':1834,'actual_ngram_draft':{'draft_tokens':288,'accepted_tokens':288,'acceptance_percent':100},'successful_task_wall_s':125.5})
 def test_managed_memory_counter_is_separate_from_physical_vram(self):
  raw={'actual_managed_allocator':{'calls':5,'successful_calls':5,'cumulative_bytes_not_peak':7005214976,'logical_allocation_is_not_NVML_residency':True,'pointer_address':'private'},'peak_process_vram_mib':478,'peak_device_vram_mib':7452.5,'CT_memory_observed':{'maximum_new_swap_bytes':0}}
  out=e.metrics(raw);self.assertEqual(out['peak_device_vram_mib'],7452.5);self.assertEqual(out['peak_process_vram_mib'],478);self.assertTrue(out['actual_managed_allocator']['managed_bytes_are_not_residency']);self.assertNotIn('pointer_address',out['actual_managed_allocator'])
 def test_slot_diagnostic_keeps_valid_critical_and_changed_prefix_distinct(self):
  raw={'prefix_envelopes_same':20,'actual_history_requests':21,'critical_matches_previous_valid':True,'critical_matches_previous_bad':False,'other_slot_erased':False,'response':{'content':'private'}}
  self.assertEqual(e.metrics(raw),{k:v for k,v in raw.items() if k!='response'})
 def test_unknown_files_and_weights_rejected(self):
  for f in ['.env','weights.gguf','data/unreviewed.json','docs/private.log','scripts/extra.py']:
   self.assertFalse(v.allowed(pathlib.Path(f)))
 def test_nonpublic_source_url_rejected(self):
  self.assertIsNone(e.url('https://'+'192'+'.168.42.18/private'))
  self.assertIsNone(e.url('https://user'+':secret'+'@github.com/repo'))
 def test_missing_is_not_zero(self):self.assertEqual(e.metrics({'metrics':{'ttft_s':None,'solved':0}}),{'metrics':{'solved':0}})
if __name__=='__main__':unittest.main()
