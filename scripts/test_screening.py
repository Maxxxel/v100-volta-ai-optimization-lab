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
 def test_explicit_transport_is_visible_without_claiming_native_tool_training(self):
  d=self.fixture();d['rows'][0]['configuration']['tool_transport']='EXPLICIT_GENERIC_XML_JSON_BRIDGE_PHI_ROLE_DELIMITERS_NOT_NATIVE_TRAINING'
  page=render(d);self.assertIn('tool bridge</small>',page);self.assertIn('no native tool-training claim',page)
  self.assertNotIn('tool bridge</small>',render(self.fixture()))

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
 def test_mixed_screen_links_full_coding_only_with_the_exact_tool_envelope(self):
  from screening import same_native_inference
  base,screen=self.profiles();screen['adapter']='llama-native-coding';before=copy.deepcopy((base,screen))
  self.assertTrue(same_native_inference(base,screen,'coding'));self.assertEqual((base,screen),before)
  for key,value in [('tool_choice','required'),('parallel_tool_calls',False),('temperature',.5)]:
   wrong=copy.deepcopy(screen);wrong['native_recipe']['request_options'][key]=value
   self.assertFalse(same_native_inference(base,wrong,'coding'))
 def test_scoring_view_links_original_capture_once_and_rejects_identity_drift(self):
  import tempfile
  from pathlib import Path
  from screening import matching_full_runs,H
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);stage=root/'staging/r1';stage.mkdir(parents=True);raw=root/'raw';raw.mkdir()
   actual,screen=self.profiles();screen['adapter']='llama-native-coding'
   (raw/'profile.json').write_text(json.dumps(actual));(raw/'AUDIT.json').write_text('{}')
   audit=stage/'AUDIT.json';audit.write_text(json.dumps({'parts':[{'audit_path':str(raw/'AUDIT.json'),'audit_sha256':H(raw/'AUDIT.json')}]}))
   base={'run_id':'old','experiment_id':'R1','runtime_configuration_id':'cfg','model_artifact_id':'artifact','audit_hash':H(audit),'official_eligible':False,'benchmark_identity_id':'bench','discipline':'coding'}
   view={**base,'run_id':'new','audit_hash':'c'*64,'official_eligible':True,'scoring_view_of_run_id':'old','same_GPU_measurement':True,'additional_GPU_runs':0}
   view['qualification_audit']={'original_preliminary_audit_sha256':base['audit_hash'],'audit_hash':view['audit_hash'],'scoring_view_of_run_id':'old','same_GPU_measurement':True,'additional_GPU_runs':0}
   profiles={'cfg':{'model':{'artifact_sha256':'a'*64},'runtime':{'power_limit_w':300}}}
   history={'runs':[base,view,{**view,'run_id':'counter-view'}]}
   self.assertEqual(len(matching_full_runs(root,history,profiles,screen,'a'*64)),1)
   for field,value in [('runtime_configuration_id','other'),('model_artifact_id','other'),('additional_GPU_runs',False),('dataset_split_hash','other')]:
    bad=copy.deepcopy(view);bad[field]=value
    if field=='runtime_configuration_id':profiles['other']=copy.deepcopy(profiles['cfg'])
    with self.assertRaises(ValueError):matching_full_runs(root,{'runs':[base,bad]},profiles,screen,'a'*64)
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
 def test_new_family_screens_link_corrected_official_views_without_duplicate_audits(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];data=json.loads((root/'data/screening.json').read_text())
  expected={'R553':{'R570'},'R554':{'R560','R564'},'R555':{'R566'},'R556':{'R561','R563'},'R557':{'R568'}}
  for screen,experiments in expected.items():
   row=next(r for r in data['rows'] if r['experiment_id']==screen)
   self.assertEqual(row['full_benchmark_status'],'MATCHED_FULL_LOCAL_RESULTS')
   self.assertTrue(experiments.issubset({r['experiment_id'] for r in row['full_benchmark_runs']}))
   identities=[(r['experiment_id'],r['benchmark_identity_id'],r['runtime_configuration_id'],r['audit_hash']) for r in row['full_benchmark_runs']]
   self.assertEqual(len(identities),len(set(identities)))
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

class NativeAgentDevelopmentPublication(unittest.TestCase):
 def fixture(self):
  return {'status':'DEVELOPMENT_AGENT18_COMPLETE','measurement_valid':True,'official_benchmark':False,'winner_qualified':False,'full_benchmark_score_claimed':False,'tasks':18,'solved':10,'planned_tasks':18,'task_phase_s':123.,'model_sha256':'a'*64,'raw_root':'PRIVATE','scored_tasks':[{'private':'DO NOT EXPORT'}]}
 def test_projection_is_development_only_and_excludes_private_cases(self):
  from export import metrics
  m=metrics(self.fixture())['native_agent18_development']
  self.assertEqual(m['solved'],10);self.assertEqual(m['tasks'],18);self.assertFalse(m['official_benchmark'])
  self.assertNotIn('PRIVATE',json.dumps(m));self.assertNotIn('DO NOT EXPORT',json.dumps(m));self.assertNotIn('gpu_j_per_success_lower',m)
 def test_incomplete_or_official_promotion_rejected(self):
  from export import metrics
  for update in [{'tasks':17},{'official_benchmark':True},{'winner_qualified':True},{'solved':19}]:
   obj=self.fixture();obj.update(update)
   with self.assertRaises(AssertionError):metrics(obj)

 def test_no_official_result_or_missing_cost_fabrication_in_agent_view(self):
  from export import metrics
  from screening import render_native_agent_development
  e={'id':'R999','model':'Mock profile','aggregate_metrics':metrics(self.fixture())}
  html=render_native_agent_development([e]);self.assertIn('10/18',html);self.assertIn('NOT MEASURED',html);self.assertIn('Not Terminal-Bench',html)
  self.assertEqual(render_native_agent_development([]),'')

 def test_agent_development_does_not_enter_official_history(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1]
  history=json.loads((root/'data/configuration-history.json').read_text())
  self.assertFalse(any(r.get('experiment_id')=='R518' or r.get('benchmark_id')=='frozen-agent18-native-development-v1' for r in history['runs']))

 def test_agent_context_failures_are_explicit_without_changing_denominator(self):
  from export import metrics
  from screening import render_native_agent_development
  obj=self.fixture();obj.update(technical_preflight_cases=2,technical_request_errors=0)
  e={'id':'R999','model':'Mock profile','aggregate_metrics':metrics(obj)}
  html=render_native_agent_development([e]);self.assertIn('2 / 0',html);self.assertIn('10/18',html);self.assertIn('Preflight / HTTP failures',html)

class IndependentGroupedStatistics(unittest.TestCase):
 def test_independent_distribution_matches_group_enumeration_boundaries(self):
  from export import grouped_sign_probability
  self.assertEqual(grouped_sign_probability([-1]*9),2/512)
  self.assertEqual(grouped_sign_probability([-3]*3),.25)
  self.assertEqual(grouped_sign_probability([0,0]),1)
  self.assertEqual(grouped_sign_probability([-1,1,0]),1)
 def test_group_review_note_is_data_bound_and_not_official_score(self):
  from export import metrics
  from screening import render_native_agent_development
  obj=NativeAgentDevelopmentPublication().fixture();e={'id':'R999','model':'Mock profile','aggregate_metrics':metrics(obj),'native_agent_grouped_review':{'aggregate_metrics':{'quality':{'frozen_tasks_per_model':18,'frozen_generalization_groups':10}}}}
  html=render_native_agent_development([e]);self.assertIn('18 tasks share 10 original generalization groups',html);self.assertIn('exploratory and unadjusted',html);self.assertIn('|\n\nThe 18 tasks',html)

class FixedProfileValidationIdentity(unittest.TestCase):
 def pair(self):
  a={'model':'m','runtime':'engine','chat_template':'template','adapter':'native-tools','assets':{'m':'a'*64,'engine':'b'*64},'native_recipe':{'argv_tail':['-c','8192'],'context':8192,'environment':{},'warmups':[],'http_timeout_policy':'REMAINING_TASK_TIME','maximum_tasks':200,'maximum_generation_requests':201,'request_options':{'temperature':0,'max_tokens':4096,'chat_template_kwargs':{'enable_thinking':False}}}}
  b=copy.deepcopy(a);b['native_recipe'].update(maximum_tasks=16,maximum_generation_requests=17,preflight_all_inputs=True)
  return a,b
 def test_only_validation_collection_changes_are_permitted(self):
  from screening import same_validation_inference
  a,b=self.pair();self.assertTrue(same_validation_inference(b,a))
 def test_sampler_context_kernel_template_and_timeout_drift_rejected(self):
  from screening import same_validation_inference
  for key,value in [('context',16384),('environment',{'FORCE_MMQ':'1'}),('http_timeout_policy','other')]:
   a,b=self.pair();b['native_recipe'][key]=value;self.assertFalse(same_validation_inference(b,a))
  for key,value in [('model','other'),('runtime','fork'),('chat_template','other'),('assets',{'m':'c'*64})]:
   a,b=self.pair();b[key]=value;self.assertFalse(same_validation_inference(b,a))
  a,b=self.pair();b['native_recipe']['request_options']['temperature']=.6;self.assertFalse(same_validation_inference(b,a))
 def test_additional_validation_exposure_is_explicit(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];data=json.loads((root/'data/screening.json').read_text())
  for row in data['independent_validation16']['rows']:
   if row['model'].endswith(' · OFF/T0') and row['groups'] is not None:
    self.assertIn('exposed',row['validation_exposure']);self.assertRegex(row['additional_plan_sha256'],r'^[a-f0-9]{64}$')

class AdditionalValidationRows(unittest.TestCase):
 def test_additional_fixed_profiles_do_not_replace_original_rows(self):
  d=IndependentValidation().data()
  for eid in ['R526','R527']:
   r=copy.deepcopy(d['independent_validation16']['rows'][0]);r.update(model=eid,experiment_id=eid);d['independent_validation16']['rows'].append(r)
  validate(d);self.assertEqual(len(d['independent_validation16']['rows']),5)
 def test_duplicate_validation_experiments_rejected(self):
  d=IndependentValidation().data();d['independent_validation16']['rows'].append(copy.deepcopy(d['independent_validation16']['rows'][0]))
  with self.assertRaises(AssertionError):validate(d)

class JarvisQualification(unittest.TestCase):
 def fixture(self):
  d=ScreeningTests().fixture();d['qualification_phase']={'status':'JARVIS_QUALIFICATION_IN_PROGRESS_SCREENING_COMPLETE','candidates':[{'profile':'Example','source_experiments':['R1'],'full_benchmark_records':[{'official_eligible':True}],'official_agents':'NOT MEASURED'}],'validation':{'status':'FROZEN_NOT_RELEASED_NO_MODEL_RESULTS','cases':33,'generalization_groups':11,'golden_QA_passed':33,'wrong_final_QA_rejected':33,'forbidden_action_QA_rejected':33,'model_requests':0},'terminal_bench':{'tasks':89,'revision':'a'*40,'evaluator_version':'0.24.0','sources':['https://example.com/source']},'gemma_context':{'experiment_id':'R528','model_requests':0,'quality_score':None,'CPU_fix_tests':21},'multi_agent_plan':{'arms':['Single-Agent','Planner + Worker','Planner + Worker + Reviewer'],'total_task_budget_s':1200,'per_arm_task_budget_s':400,'GPU_concurrency':1}}
  return d
 def test_cpu_controls_never_become_model_scores(self):
  from screening import render_qualification
  d=self.fixture();validate(d);text=render_qualification(d)
  self.assertIn('zero model responses',text);self.assertIn('harness checks, not model scores',text);self.assertNotIn('33/33',text);self.assertIn('Official agent qualification: NOT MEASURED',text)
 def test_no_measured_quality_for_startup_failure(self):
  d=self.fixture();d['qualification_phase']['gemma_context']['quality_score']=0
  with self.assertRaises(AssertionError):validate(d)
 def test_no_budget_reset_between_roles(self):
  d=self.fixture();d['qualification_phase']['multi_agent_plan']['per_arm_task_budget_s']=1200
  with self.assertRaises(AssertionError):validate(d)
 def test_no_fake_official_agents_or_model_calls(self):
  d=self.fixture();d['qualification_phase']['candidates'][0]['official_agents']='QUALIFIED'
  with self.assertRaises(AssertionError):validate(d)
  d=self.fixture();d['qualification_phase']['validation']['model_requests']=1
  with self.assertRaises(AssertionError):validate(d)
 def test_partial_candidate_evidence_remains_partial(self):
  from screening import render_qualification
  d=self.fixture();d['qualification_phase']['candidates'][0]['full_benchmark_records'][0]['official_eligible']=False
  self.assertIn('incomplete evidence remains PARTIAL',render_qualification(d))

class GemmaCorrectedContextEvidence(unittest.TestCase):
 def test_corrected_gpu_result_remains_development_and_original_failure_unknown(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];d=json.loads((root/'data/screening.json').read_text());g=d['qualification_phase']['gemma_context'];c=g['corrective_result']
  self.assertEqual(g['experiment_id'],'R528');self.assertIsNone(g['quality_score']);self.assertTrue(g['GPU_retry_admitted'])
  self.assertEqual(c['experiment_id'],'R529');self.assertEqual(c['tasks'],18);self.assertEqual(c['solved'],c['reference_solved']);self.assertEqual(c['context_preflight_errors'],0);self.assertEqual(c['HTTP_errors'],0);self.assertEqual(c['identical_first_turn_prompt_hashes'],18);self.assertFalse(c['official_benchmark']);self.assertFalse(c['winner_qualified'])
  history=json.loads((root/'data/configuration-history.json').read_text());self.assertFalse(any(r['experiment_id']=='R529' for r in history['runs']))
 def test_actual_captured_context_and_output_are_exposed_without_changing_original(self):
  from pathlib import Path
  root=Path(__file__).resolve().parents[1];es=json.loads((root/'data/experiments.json').read_text());m={e['id']:e['aggregate_metrics']['native_agent18_development'] for e in es if e.get('aggregate_metrics',{}).get('native_agent18_development')}
  self.assertEqual(m['R520']['context_tokens'],8192);self.assertEqual(m['R529']['context_tokens'],16384);self.assertEqual(m['R520']['max_output_tokens'],m['R529']['max_output_tokens']);self.assertNotEqual(m['R520']['bridge_source_sha256'],m['R529']['bridge_source_sha256'])

class AgentValidation33Presentation(unittest.TestCase):
 def data(self):
  d=JarvisQualification().fixture();d['qualification_phase']['model_validation']=[{'experiment_id':'R530','model':'CPU fixture only','audit_sha256':'a'*64,'metrics':{'tasks':33,'planned_tasks':33,'solved':21,'official_benchmark':False,'winner_qualified':False,'data_role':'FROZEN33_VALIDATION_AUTHORED_FAMILIES_NOT_OFFICIAL'}}];return d
 def test_model_validation_separate_from_cpu_controls_and_official_scores(self):
  from screening import render_qualification
  d=self.data();validate(d);out=render_qualification(d)
  self.assertIn('21/33',out);self.assertIn('NOT MEASURED',out);self.assertIn('not Terminal-Bench',out);self.assertNotIn('zero model responses',out)
 def test_validation_cannot_become_official_or_duplicate(self):
  d=self.data();d['qualification_phase']['model_validation'][0]['metrics']['official_benchmark']=True
  with self.assertRaises(AssertionError):validate(d)
  d=self.data();d['qualification_phase']['model_validation']*=2
  with self.assertRaises(AssertionError):validate(d)
 def test_unknown_metrics_remain_missing(self):
  from screening import render_qualification
  out=render_qualification(self.data());self.assertIn('NOT MEASURED–NOT MEASURED',out);self.assertNotIn('0.00',out)

class QualificationDecisionProvenance(unittest.TestCase):
 def fixture(self,root):
  from screening import H
  folder=root/'staging/r530';folder.mkdir(parents=True)
  def write(path,value):path.write_text(json.dumps(value));return H(path)
  quality={'source_audit_sha256':'a'*64,'tasks':33,'solved':21,'quality':{'policy_gate_passes':29,'task_scope_passes':33}}
  qh=write(folder/'QUALITY_REVIEW.json',quality)
  ih=write(folder/'INDEPENDENT_REVIEW.json',{'status':'INDEPENDENT_CPU_REPLAY_IDENTICAL','result':{'all_scores_and_effects_reproduced':True}})
  metrics={'solved':21,'tasks':33,'task_phase_s':400,'peak_device_vram_mib':7000,'gpu_j_per_success_lower':4000,'gpu_j_per_success_upper':4002}
  row={'experiment_id':'R530','model':'CPU fixture only','audit_sha256':'a'*64,**metrics,'quality_review_sha256':qh,'independent_review_sha256':ih,'policy_gate_passes':29,'task_scope_passes':33,'decision':'RETAIN_REFERENCE','reason':'More confirmation required.','optimization_after_qualification':'Only after confirmation.'}
  review={'schema':1,'official_benchmark':False,'winner_qualified':False,'population_ranking':False,'dataset_id':'jarvis-agent-validation-20261025-v1','dataset_sha256':'b'*64,'authored_groups':11,'cases_per_profile':33,'new_GPU_runs':0,'model_profiles':1,'profiles':[row],'review_scope':'CPU unit fixture only','next_decisions':['Confirm independently.']}
  path=root/'review.json';phase={'decision_review':{'path':str(path),'sha256':write(path,review)},'frozen_agent_validation':{'private_dataset_sha256':'b'*64}}
  measured=[{'experiment_id':'R530','model':'CPU fixture only','audit_sha256':'a'*64,'metrics':metrics}]
  return phase,review,measured,path
 def test_decision_reuses_verified_results_without_claiming_official_rank(self):
  import tempfile
  from pathlib import Path
  from screening import qualification_decisions
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);phase,_,measured,_=self.fixture(root)
   result=qualification_decisions(root,phase,measured)
   self.assertEqual(result['profiles'][0]['policy_gate_passes'],29);self.assertFalse(result['official_benchmark']);self.assertFalse(result['winner_qualified'])
   self.assertNotIn('private_dataset_sha256',result)
 def test_rejects_score_reinterpretation_duplicate_or_missing_profile(self):
  import tempfile
  from pathlib import Path
  from screening import qualification_decisions,H
  for fault in ('score','duplicate','missing','official','policy'):
   with self.subTest(fault=fault),tempfile.TemporaryDirectory() as directory:
    root=Path(directory);phase,review,measured,path=self.fixture(root)
    if fault=='score':review['profiles'][0]['solved']=22
    elif fault=='duplicate':review['profiles']*=2;review['model_profiles']=2
    elif fault=='missing':review['profiles']=[];review['model_profiles']=0
    elif fault=='official':review['official_benchmark']=True
    elif fault=='policy':review['profiles'][0]['policy_gate_passes']=33
    path.write_text(json.dumps(review));phase['decision_review']['sha256']=H(path)
    with self.assertRaises(AssertionError):qualification_decisions(root,phase,measured)
 def test_mutated_evidence_fails_closed(self):
  import tempfile
  from pathlib import Path
  from screening import qualification_decisions
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);phase,_,measured,_=self.fixture(root)
   (root/'staging/r530/QUALITY_REVIEW.json').write_text('{}')
   with self.assertRaises(AssertionError):qualification_decisions(root,phase,measured)
 def test_rendered_next_step_does_not_repeat_completed_source_admission(self):
  from screening import render_qualification
  d=AgentValidation33Presentation().data();d['qualification_phase']['decision_review']={'profiles':[{'model':'CPU fixture','experiment_id':'R530','policy_gate_passes':29,'reason':'Confirm independently.'}],'review_sha256':'a'*64,'next_decisions':['Keep deterministic permissions.']}
  out=render_qualification(d);self.assertIn('29/33',out);self.assertIn('not a winner qualification',out);self.assertNotIn('Next: source-admit',out)

class EmptyThoughtScientificCorrection(unittest.TestCase):
 def diagnosis(self):
  return {'model':'CPU fixture only','applicable_profile_experiment_ids':['R530'],'audit_sha256':'c'*64,'CPU_controls':20,'parser_roundtrips':12,'template_controls':8,'empty_thought_sections':90,'nonempty_thought_sections':0,'original_scores_changed':False,'GPU_runs':0,'official_benchmark':False,'decision_summary':'No lost reasoning demonstrated.'}
 def test_markers_are_not_evidence_of_nonempty_reasoning(self):
  from screening import thought_section_counts
  self.assertEqual(thought_section_counts(['<|channel>thought\n \t<channel|>','ordinary output']),{'empty':1,'nonempty':0,'unclosed':0})
 def test_actual_content_and_literal_backslash_are_not_empty(self):
  from screening import thought_section_counts
  values=['<|channel>thought\ntext<channel|>',r'<|channel>thought\n<channel|>']
  self.assertEqual(thought_section_counts(values),{'empty':0,'nonempty':2,'unclosed':0})
 def test_missing_and_truncated_raw_content_cannot_become_empty_evidence(self):
  from screening import thought_section_counts
  with self.assertRaises(AssertionError):thought_section_counts([None])
  self.assertEqual(thought_section_counts(['<|channel>thought unfinished']),{'empty':0,'nonempty':0,'unclosed':1})
 def test_correction_remains_separate_from_existing_model_score(self):
  from screening import render_qualification
  d=AgentValidation33Presentation().data();d['qualification_phase']['gemma_context']['diagnostic_resolution']=self.diagnosis()
  validate(d);text=render_qualification(d)
  self.assertIn('hypothesis is withdrawn',text);self.assertIn('20 model-free controls',text);self.assertIn('21/33',text)
  d['qualification_phase']['gemma_context']['diagnostic_resolution']['original_scores_changed']=True
  with self.assertRaises(AssertionError):validate(d)
 def test_amendment_preserves_original_decision_and_requires_source_identity(self):
  import tempfile
  from pathlib import Path
  from screening import qualification_decisions
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);phase,_,measured,_=QualificationDecisionProvenance().fixture(root)
   result=qualification_decisions(root,phase,measured,self.diagnosis());row=result['profiles'][0]
   self.assertEqual(row['original_decision_reason'],'More confirmation required.');self.assertEqual(row['reason'],'No lost reasoning demonstrated.');self.assertEqual(row['decision_amendment_sha256'],'c'*64)

class OrchestrationCPUSeparation(unittest.TestCase):
 def data(self):
  d=JarvisQualification().fixture();d['qualification_phase']['multi_agent_plan']['CPU_controls']={'audit_sha256':'a'*64,'guard_tests':18,'scripted_case_executions':15,'paired_unique_cases':5,'scripted_callbacks':67,'model_results_measured':False,'GPU_admitted':False,'GPU_runs':0,'official_benchmark':False};return d
 def test_scripted_role_checks_never_become_a_model_score(self):
  from screening import render_qualification
  d=self.data();validate(d);out=render_qualification(d)
  self.assertIn('15 scripted case executions on 5 paired development tasks',out);self.assertIn('not model scores',out);self.assertNotIn('15/15',out)
 def test_no_implied_GPU_admission_or_actual_model_result(self):
  for field in ['GPU_admitted','model_results_measured','official_benchmark']:
   d=self.data();d['qualification_phase']['multi_agent_plan']['CPU_controls'][field]=True
   with self.subTest(field=field),self.assertRaises(AssertionError):validate(d)

class OrchestrationMeasuredPresentation(unittest.TestCase):
 def data(self):
  d=OrchestrationCPUSeparation().data()
  d['qualification_phase']['multi_agent_plan']['results']=[{'experiment_id':'R999','model':'Synthetic presentation fixture','paired_unique_cases':5,'case_executions':15,'official_benchmark':False,'winner_qualified':False,'correction_audit_id':'audit-'+'a'*20,'arms':[dict(arm=name,complete=True,completed_cases=5,planned_cases=5,solved=n,policy_gate_passes=4,arm_wall_s=10.0,tokens_s_completed_requests=None,gpu_j_per_success_lower=None,gpu_j_per_success_upper=None,peak_sampled_device_vram_mib=None) for name,n in [('single',2),('planner_worker',2),('planner_worker_reviewer',3)]]}]
  return d
 def test_measured_arms_never_claim_official_score_or_winner(self):
  from screening import render_qualification
  d=self.data();validate(d);out=render_qualification(d)
  self.assertIn('Agent role comparison',out);self.assertIn('2/5',out);self.assertIn('3/5',out);self.assertIn('NOT MEASURED',out)
  self.assertIn('not fifteen independent observations',out);self.assertNotIn('GPU source/admission review remains pending',out)
 def test_cannot_promote_pilot_to_official_or_independent_15_tasks(self):
  for k,v in [('official_benchmark',True),('winner_qualified',True),('paired_unique_cases',15)]:
   d=self.data();d['qualification_phase']['multi_agent_plan']['results'][0][k]=v
   with self.subTest(field=k),self.assertRaises(AssertionError):validate(d)
 def test_missing_arm_or_duplicate_experiment_is_rejected(self):
  import copy
  d=self.data();d['qualification_phase']['multi_agent_plan']['results'].append(copy.deepcopy(d['qualification_phase']['multi_agent_plan']['results'][0]))
  with self.assertRaises(AssertionError):validate(d)
  d=self.data();d['qualification_phase']['multi_agent_plan']['results'][0]['arms'].pop()
  with self.assertRaises(AssertionError):validate(d)


class FrozenCohortScope(unittest.TestCase):
 def test_new_measured_variant_does_not_rewrite_old_shortlist(self):
  from screening import cohort_review_scope
  a,outside=cohort_review_scope([{'experiment_id':'R530'},{'experiment_id':'R543'}],{'model_profiles':1,'profiles':[{'experiment_id':'R530'}]})
  self.assertEqual(outside,['R543']);self.assertEqual(set(a),{'R530','R543'})
 def test_missing_reviewed_profile_and_duplicate_rows_rejected(self):
  from screening import cohort_review_scope
  for measured,review in [([{'experiment_id':'R543'}],{'model_profiles':1,'profiles':[{'experiment_id':'R530'}]}),([{'experiment_id':'R530'}]*2,{'model_profiles':1,'profiles':[{'experiment_id':'R530'}]}),([{'experiment_id':'R530'}],{'model_profiles':2,'profiles':[{'experiment_id':'R530'}]*2})]:
   with self.assertRaises(AssertionError):cohort_review_scope(measured,review)

class TerminalGate(unittest.TestCase):
 def test_missing_gate_stays_missing(self):
  from screening import terminal_final_gate
  self.assertIsNone(terminal_final_gate('.',None))
 def test_forged_gate_and_outside_source_rejected(self):
  import tempfile,hashlib
  from pathlib import Path
  from screening import terminal_final_gate
  with tempfile.TemporaryDirectory() as folder:
   root=Path(folder);p=root/'gate.json';p.write_text('{}')
   with self.assertRaises(AssertionError):terminal_final_gate(root,{'path':str(p),'sha256':'0'*64})
   with self.assertRaises(AssertionError):terminal_final_gate(root/'other',{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})

class TerminalGateSourceBinding(unittest.TestCase):
 def test_verified_source_only_no_go_cannot_be_promoted_or_rehashed_over_changed_source(self):
  import tempfile,hashlib
  from pathlib import Path
  from screening import terminal_final_gate
  with tempfile.TemporaryDirectory() as folder:
   root=Path(folder);source=root/'source.txt';source.write_text('pinned source')
   gate={'GPU_runs':0,'model_requests':0,'foreign_task_or_verifier_code_executed':False,'status':'NO_GO_CURRENT_LOCAL_CAMPAIGN_UNDER_FINAL_FREEZE','official_complete_local_result':'NOT MEASURED','official_scorer_admitted':False,'task_count':89,'task_configurations_verified':89,'source_required_files_present':89,'task_budget_seconds':1200,'source_files_sha256':{str(source):hashlib.sha256(source.read_bytes()).hexdigest()}}
   fields=('at_utc','Harbor_source_revision','source_task_resources','publisher_configurations','hub_content_digest','hub_digest_to_git_tree_mapping','budget_interpretation','blockers','not_hardware_exclusion','decision_scope','reopening_requirements','final_report_policy','sources')
   gate.update({k:[] if k in ('publisher_configurations','blockers','reopening_requirements','sources') else 'source evidence' for k in fields})
   p=root/'gate.json'
   def seal():
    p.write_text(json.dumps(gate));return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
   self.assertEqual(terminal_final_gate(root,seal())['status'],gate['status'])
   gate['GPU_runs']=1
   with self.assertRaises(AssertionError):terminal_final_gate(root,seal())
   gate['GPU_runs']=0;descriptor=seal();source.write_text('changed')
   with self.assertRaises(AssertionError):terminal_final_gate(root,descriptor)

class TechnicalBlockerProjection(unittest.TestCase):
 def fixture(self, root):
  import pathlib,hashlib
  raw=pathlib.Path(root);profile=raw/'profile.json';profile.write_text(json.dumps({'model_sha256':'a'*64}))
  audit=raw/'audit.json';a={'experiment_id':'R562','model':'Example','measurement_valid':False,'never_task_started':True,'GPU_inference_task_execution_observed':False,'GPU_model_allocation_observed':True,'completed_requests':0,'scored_tasks':0,'solved_observed_tasks':None,'raw_root':str(raw),'raw_files_sha256':{'profile.json':hashlib.sha256(profile.read_bytes()).hexdigest()},'status':'FAILED','decision':'TECHNICALLY_BLOCKED_STARTUP180_BEFORE_TASKS','peak_device_vram_mib':12496.5}
  def seal():
   audit.write_text(json.dumps(a));return {'model':'Example','model_sha256':'a'*64,'technical_blocker_audit':{'path':str(audit),'sha256':hashlib.sha256(audit.read_bytes()).hexdigest()}}
  return a,seal
 def test_startup_allocation_is_not_quality_or_inference(self):
  import tempfile
  from screening import technical_blocker
  with tempfile.TemporaryDirectory() as d:
   a,seal=self.fixture(d);v=technical_blocker(seal());self.assertEqual(v['experiment_id'],'R562');self.assertIsNone(v['quality_score']);self.assertFalse(v['GPU_inference_task_execution_observed']);self.assertTrue(v['GPU_model_allocation_observed']);self.assertNotIn('raw_root',v)
  self.assertIsNone(technical_blocker({}))
 def test_wrong_audit_identity_or_actual_inference_rejected(self):
  import tempfile
  from screening import technical_blocker
  with tempfile.TemporaryDirectory() as d:
   a,seal=self.fixture(d)
   for key,value in [('model','Different'),('GPU_inference_task_execution_observed',True),('never_task_started',False),('scored_tasks',1),('solved_observed_tasks',0)]:
    original=a[key];a[key]=value
    with self.assertRaises(AssertionError):technical_blocker(seal())
    a[key]=original
   entry=seal();entry['model_sha256']='b'*64
   with self.assertRaises(AssertionError):technical_blocker(entry)
   entry=seal();entry['technical_blocker_audit']['sha256']='0'*64
   with self.assertRaises(AssertionError):technical_blocker(entry)
 def test_blocked_link_visible_without_official_or_screening_score(self):
  f=ScreeningTests().fixture();row=f['rows'][0];row['results']=None;row['status']='TECHNISCH BLOCKIERT';row['technical_blocker']={'experiment_id':'R562','decision':'TECHNICALLY_BLOCKED_STARTUP180_BEFORE_TASKS'}
  page=render(f);self.assertIn('R562 startup audit',page);self.assertIn('NOT MEASURED',page)

class NewFamilyEvidence(unittest.TestCase):
 def fixture(self):
  row={'model':'Phi-4','configuration':{'model_sha256':'a'*64,'quantization':'Q6_K'},'status':'SCREENING VOLLSTÄNDIG','local_artifact_available':True,'results':None,'full_benchmark_runs':[{'experiment_id':'R566','runtime_configuration_id':'cfg-a','benchmark_identity_id':'bench-a','audit_hash':'hash-a'}]}
  run={'experiment_id':'R566','runtime_configuration_id':'cfg-a','benchmark_identity_id':'bench-a','audit_hash':'hash-a','official_eligible':True,'full_benchmark_score_claimed':True,'benchmark_id':'humanevalplus-v0.1.10','benchmark_revision':{'commit':'exact'},'dataset_split_hash':'split','scorer_version':'scorer','model_artifact_id':'artifact-a','solved':134,'tasks':164,'wall_s':700.,'peak_vram_mib':13000.}
  profile={'runtime_configuration_id':'cfg-a','model_artifact_id':'artifact-a','model':{'artifact_sha256':'a'*64}}
  return {'rows':[row]},{'runs':[run],'profiles':[profile]}
 def test_exact_qualification_and_energy_alias_are_one_measurement(self):
  from render import new_family_evidence
  s,h=self.fixture();alias=copy.deepcopy(h['runs'][0]);alias['counter_energy']={'tasks':164,'solved':134,'j_per_success_lower':10.,'j_per_success_upper':11.};h['runs'].append(alias)
  r=new_family_evidence(s,h,[]);points=r['models'][0]['qualified_runs'];self.assertEqual(len(points),1);self.assertEqual(points[0]['counter_energy'],alias['counter_energy']);self.assertIsNone(r['models'][0]['screening_results'])
 def test_wrong_identity_historical_or_conflicting_score_cannot_transfer(self):
  from render import new_family_evidence
  for key,value in [('audit_hash','other'),('runtime_configuration_id','other'),('benchmark_identity_id','other'),('official_eligible',False),('full_benchmark_score_claimed',False),('tasks',32)]:
   s,h=self.fixture();h['runs'][0][key]=value
   with self.assertRaises(AssertionError):new_family_evidence(s,h,[])
  s,h=self.fixture();h['profiles'][0]['model']['artifact_sha256']='b'*64
  with self.assertRaises(AssertionError):new_family_evidence(s,h,[])
  s,h=self.fixture();alias=copy.deepcopy(h['runs'][0]);alias['solved']=135;h['runs'].append(alias)
  with self.assertRaises(AssertionError):new_family_evidence(s,h,[])
 def test_unlinked_missing_scores_are_not_borrowed_by_model_name(self):
  from render import new_family_evidence,new_family_section
  s,h=self.fixture();s['rows'][0]['full_benchmark_runs']=[];r=new_family_evidence(s,h,[]);self.assertEqual(r['models'][0]['qualified_runs'],[]);text=new_family_section(s,h,[]);self.assertIn('NOT MEASURED',text);self.assertNotIn('134/164',text);self.assertIn('dated baseline',text)
 def test_authored_agents_are_separate_profiles_not_official_scores(self):
  from render import new_family_evidence
  s,h=self.fixture();agent={'id':'R567','aggregate_metrics':{'native_validation33':{'model_sha256':'a'*64,'official_benchmark':False,'tasks':33,'planned_tasks':33,'profile_sha256':'different-agent-profile','solved':17}}}
  r=new_family_evidence(s,h,[agent]);self.assertEqual(r['agent_profiles'][0]['profile_sha256'],'different-agent-profile');self.assertEqual(len(r['models'][0]['qualified_runs']),1)
  agent['aggregate_metrics']['native_validation33']['official_benchmark']=True
  with self.assertRaises(AssertionError):new_family_evidence(s,h,[agent])
