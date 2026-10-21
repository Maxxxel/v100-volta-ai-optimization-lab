import importlib.util,pathlib,unittest
P=pathlib.Path(__file__).resolve().parent
def module(name):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module('validate');e=module('export')
class PublicationSafety(unittest.TestCase):
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
 def test_unknown_files_and_weights_rejected(self):
  for f in ['.env','weights.gguf','data/unreviewed.json','docs/private.log','scripts/extra.py']:
   self.assertFalse(v.allowed(pathlib.Path(f)))
 def test_nonpublic_source_url_rejected(self):
  self.assertIsNone(e.url('https://'+'192'+'.168.42.18/private'))
  self.assertIsNone(e.url('https://user'+':secret'+'@github.com/repo'))
 def test_missing_is_not_zero(self):self.assertEqual(e.metrics({'metrics':{'ttft_s':None,'solved':0}}),{'metrics':{'solved':0}})
if __name__=='__main__':unittest.main()
