import importlib.util,pathlib,unittest
P=pathlib.Path(__file__).resolve().parent
def module(name):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module('validate');e=module('export')
class PublicationSafety(unittest.TestCase):
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
