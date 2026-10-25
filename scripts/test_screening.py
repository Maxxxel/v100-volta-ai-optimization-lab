import copy,json,unittest
from screening import validate,wilson,render,project_group
class ScreeningTests(unittest.TestCase):
 def fixture(self):
  group={'successes':12,'completed':16,'wilson95':wilson(12,16),'completed_request_wall_s':10.,'completion_tokens':100,'GPU_j_per_success_lower':5.}
  return {'official_benchmark':False,'tasks_per_category':16,'rows':[{'model':'Example','configuration':{'model_sha256':'a'*64},'status':'SCREENING VOLLSTÄNDIG','results':{'coding':copy.deepcopy(group),'tools':copy.deepcopy(group)},'audit_sha256':'b'*64,'independent_review_sha256':'c'*64,'parent_experiment_id':'R1'}]}
 def test_valid_development_projection(self):validate(self.fixture())
 def test_official_claim_rejected(self):
  d=self.fixture();d['official_benchmark']=True
  with self.assertRaises(AssertionError):validate(d)
 def test_no_missing_to_zero(self):
  d=self.fixture();d['rows'][0]['results']=None;validate(d);self.assertIn('NOT MEASURED',render(d))
 def test_no_duplicate_configuration(self):
  d=self.fixture();d['rows'].append(copy.deepcopy(d['rows'][0]))
  with self.assertRaises(AssertionError):validate(d)
 def test_wrong_counts_or_intervals_rejected(self):
  for key,value in [('successes',17),('completed',17),('wilson95',[0,1])]:
   d=self.fixture();d['rows'][0]['results']['coding'][key]=value
   with self.assertRaises(AssertionError):validate(d)
 def test_no_pagination_no_official_average(self):
  s=render(self.fixture());self.assertNotIn('pagination',s);self.assertNotIn('Overall score',s);self.assertIn('not an official benchmark',s);self.assertIn('Details',s)
 def test_wilson_extremes(self):
  self.assertEqual(wilson(0,0),None);self.assertEqual(wilson(0,16)[0],0);self.assertEqual(wilson(16,16)[1],1)

class PublishedSeparation(unittest.TestCase):
 def test_screening_never_enters_official_runs(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1]
  history=json.loads((root/'data/configuration-history.json').read_text())
  self.assertFalse(any(r.get('benchmark_id')=='model-screening32-v1' for r in history['runs']))

class EnergyCosts(unittest.TestCase):
 def test_zero_success_group_retains_measured_energy(self):
  g=project_group({'successes':0,'completed':16,'GPU_counter':{'lower_j':100,'upper_j':120}})
  self.assertEqual(g['gpu_energy_j_lower'],100);self.assertIsNone(g['GPU_j_per_success_lower'])
 def test_unknown_energy_is_not_zero(self):
  g=project_group({'successes':10,'completed':16})
  self.assertIsNone(g['gpu_energy_j_lower'])

class ConfigurationIdentity(unittest.TestCase):
 def test_same_weights_distinct_runtime_profiles_remain_separate(self):
  d=ScreeningTests().fixture();other=copy.deepcopy(d['rows'][0]);other['configuration']['parent_profile_id']='different-actual-native-profile';d['rows'].append(other);validate(d)

class IndependentValidation(unittest.TestCase):
 def data(self):
  d=ScreeningTests().fixture();g=project_group({'successes':7,'completed':8})
  d['independent_validation16']={'official_benchmark':False,'rows':[{'model':str(i),'experiment_id':'R'+str(509+i),'status':'INDEPENDENT_VALIDATION16_COMPLETE','groups':{'coding':copy.deepcopy(g),'tools':copy.deepcopy(g)},'audit_sha256':'a'*64,'independent_review_sha256':'b'*64} for i in range(3)]};return d
 def test_independent_data_stays_separate(self):validate(self.data())
 def test_cannot_promote_to_official_or_substitute16_task_groups(self):
  d=self.data();d['independent_validation16']['official_benchmark']=True
  with self.assertRaises(AssertionError):validate(d)
  d=self.data();d['independent_validation16']['rows'][0]['groups']['coding']['completed']=16
  with self.assertRaises(AssertionError):validate(d)
 def test_missing_validation_is_not_zero(self):
  d=self.data();r=d['independent_validation16']['rows'][0];r['groups']=None;r['status']='NOT MEASURED';validate(d)

class FirstNativeModelScreen(unittest.TestCase):
 def test_source_only_model_cannot_borrow_engine_parent_benchmarks(self):
  d=ScreeningTests().fixture();d['rows'][0]['full_benchmark_status']='NOT MEASURED';html=render(d)
  self.assertNotIn('R1 archive</a>',html);self.assertIn('<td>NOT MEASURED</td>',html)
 def test_published_first_screen_identity_sampling_and_scope(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];data=json.loads((root/'data/screening.json').read_text());r=next(x for x in data['rows'] if x['experiment_id']=='R514');cfg=r['configuration'];native=cfg['recorded_native_profile']
  self.assertEqual(r['full_benchmark_status'],'NOT MEASURED');self.assertEqual(r['selection_status'],'WEITERE DIAGNOSE');self.assertEqual(cfg['quantization'],'Q8_0');self.assertEqual(cfg['model_sha256'],'0ad885ffd4bb022fc4f0d33a3308fa108ef8613159d3b3a67e23abca056b7a6c')
  self.assertEqual(native['model']['parameters_in_GGUF'],752393024);self.assertEqual(native['runtime']['sampling']['temperature'],1.0);self.assertEqual(native['runtime']['sampling']['top_p'],1.0);self.assertEqual(native['runtime']['sampling']['top_k'],20);self.assertEqual(native['runtime']['max_output'],4096)
  self.assertEqual(r['results']['coding']['successes'],0);self.assertIsNone(r['results']['coding']['GPU_j_per_success_lower']);self.assertEqual(r['results']['tools']['successes'],7)
  self.assertFalse(any(x['experiment_id']=='R514' for x in json.loads((root/'data/configuration-history.json').read_text())['runs']))

class AdditionalArtifactScope(unittest.TestCase):
 def test_deferred_nongraft_is_cpu_review_not_another_gpu_profile(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];d=json.loads((root/'data/screening.json').read_text());item=next(x for x in d['other_local_artifacts'] if x['artifact']=='Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf')
  self.assertEqual(item['status'],'DEFERRED');self.assertIs(item['experimentally_screened'],False);self.assertRegex(item['audit_sha256'],r'^[0-9a-f]{64}$');self.assertTrue((root/'docs/audits'/str(item['audit_id']+'.md')).exists())
  self.assertFalse(any(x['configuration']['model_sha256']=='64b53b64c7aa39f20a7e54bd80582fe595b1d745624ee8a72e92508c0326d810' for x in d['rows']))

 def test_alternate_omni_is_distinct_measured_profile_not_new_finetune_proof(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];data=json.loads((root/'data/screening.json').read_text());a=next(x for x in data['rows'] if x['experiment_id']=='R515');b=next(x for x in data['rows'] if x['experiment_id']=='R497')
  self.assertNotEqual(a['configuration']['model_sha256'],b['configuration']['model_sha256']);self.assertEqual(a['configuration']['request_options'],b['configuration']['request_options']);self.assertEqual(a['selection_status'],'VERTIEFUNG EMPFOHLEN');self.assertIn('confounded',a['source_provenance_limits']);self.assertEqual(a['full_benchmark_status'],'MATCHED_FULL_LOCAL_RESULTS');self.assertEqual({r['experiment_id'] for r in a['full_benchmark_runs']},{'R516','R517'});self.assertEqual(a['results']['coding']['successes'],14);self.assertEqual(a['results']['tools']['successes'],14);self.assertEqual(a['comparison_summary']['additional_peak_vram_mib'],324)

class HtmlArtifactDetails(unittest.TestCase):
 def test_collapsed_artifact_review_is_a_real_link_not_literal_markdown(self):
  d=ScreeningTests().fixture();d['other_local_artifacts']=[{'artifact':'example.gguf','status':'DEFERRED','reason':'CPU-only review','audit_id':'audit-'+('a'*20)}]
  html=render(d);self.assertIn('<a href="../audits/audit-'+('a'*20)+'/">CPU review</a>',html);self.assertNotIn('[CPU review](',html);self.assertIn('<ul><li><strong>example.gguf</strong>',html)

class CrossCategoryConfigurationLinks(unittest.TestCase):
 def profiles(self):
  base={'adapter':'llama-native-coding','assets':{'target':'a'*64,'engine':'b'*64},'native_recipe':{'argv_tail':['--spec-type','none'],'context':8192,'environment':{},'warmups':[],'http_timeout_policy':'REMAINING_TASK_TIME','request_options':{'temperature':0,'max_tokens':4096,'chat_template_kwargs':{'enable_thinking':False}}}}
  tools=copy.deepcopy(base);tools['adapter']='llama-native-tools';tools['native_recipe']['request_options'].update(tool_choice='auto',parallel_tool_calls=True)
  return base,tools
 def test_only_reviewed_tool_envelope_may_differ(self):
  from screening import same_native_inference
  base,tools=self.profiles();before=copy.deepcopy((base,tools));self.assertTrue(same_native_inference(tools,base,'tools'));self.assertTrue(same_native_inference(base,base,'coding'));self.assertEqual((base,tools),before)
 def test_artifact_engine_sampler_thinking_and_tool_mode_drift_stay_separate(self):
  from screening import same_native_inference
  base,tools=self.profiles()
  for key,value in [('temperature',.6),('max_tokens',2048),('chat_template_kwargs',{'enable_thinking':True}),('tool_choice','required'),('parallel_tool_calls',False)]:
   changed=copy.deepcopy(tools);changed['native_recipe']['request_options'][key]=value;self.assertFalse(same_native_inference(changed,base,'tools'))
  changed=copy.deepcopy(tools);changed['assets']['engine']='c'*64;self.assertFalse(same_native_inference(changed,base,'tools'))
  self.assertFalse(same_native_inference(tools,base,'coding'))

class ValidationExposure(unittest.TestCase):
 def test_completed_validation_is_not_described_as_untouched(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1]
  data=json.loads((root/'data/screening.json').read_text())
  holdout=data['holdout']
  self.assertEqual(holdout['evaluated_profiles'],sum(r['groups'] is not None for r in data['independent_validation16']['rows']))
  self.assertGreater(holdout['evaluated_profiles'],0)
  self.assertIn('no longer untouched',holdout['scope'])
  self.assertIn('unexecuted',holdout['scope_at_freeze'])

class ReferenceQualificationLinks(unittest.TestCase):
 def test_existing_reference_results_link_only_matching_conditions(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1]
  data=json.loads((root/'data/screening.json').read_text())
  expected={'OmniCoder-9B':{'R471','R478'},'Qwen3.5-9B':{'R474'},'Gemma4-12B':{'R472'}}
  for model,experiments in expected.items():
   row=next(r for r in data['rows'] if r['model']==model)
   self.assertEqual(row['full_benchmark_status'],'MATCHED_FULL_LOCAL_RESULTS')
   self.assertTrue(experiments.issubset({r['experiment_id'] for r in row['full_benchmark_runs']}))
 def test_native_thinking_screen_does_not_inherit_fast_profile_scores(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1]
  data=json.loads((root/'data/screening.json').read_text())
  for model,forbidden in [('Nexus-9B',{'R488','R489'}),('Opus Distill-9B',{'R490','R491'}),('Slopus-9B',{'R493','R494'}),('Ornith-1.5-9B',{'R495','R496'})]:
   row=next(r for r in data['rows'] if r['model']==model)
   self.assertFalse(forbidden.intersection(r['experiment_id'] for r in row['full_benchmark_runs']))

 def test_different_http_deadline_policy_is_not_silently_equivalent(self):
  from screening import same_native_inference
  base,tools=CrossCategoryConfigurationLinks().profiles()
  tools['native_recipe']['http_timeout_policy']='REMAINING_TASK_TIME'
  base['native_recipe']['http_timeout_policy']=None
  self.assertFalse(same_native_inference(tools,base,'tools'))
