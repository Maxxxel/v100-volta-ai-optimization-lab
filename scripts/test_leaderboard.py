"""Scientific admission and immutable-history regression controls (CPU only)."""
import copy,json,pathlib,tempfile,unittest
from leaderboard import H,definition_identity,official_gate,frozen_merge,validate_history,pair_delta,profile,render
ROOT=pathlib.Path(__file__).resolve().parents[1]
class LeaderboardTests(unittest.TestCase):
 def fixture(self):
  ids=['a','b'];d={'benchmark_id':'test','benchmark_revision':'r1','dataset_split_hash':'a'*64,'scorer_version':'v1','required_task_count':2,'expected_task_ids_hash':H(ids),'official_definition_verified':True,'metric':'pass_at_1_percent'}
  r={'audit_hash':'b'*64,'runtime_configuration_id':'cfg-test','tasks':2,'solved':1,'score_percent':50,'benchmark_id':'test','benchmark_identity_id':definition_identity(d),'dataset_split_hash':d['dataset_split_hash'],'scorer_version':'v1'}
  proof={k:True for k in ['complete_task_set','official_scorer_verified','all_canonical_controls_passed','no_task_exclusions','prompt_protocol_verified','unique_task_ids_verified','metrics_verified','independent_audit_verified']}
  proof.update(benchmark_identity_id=definition_identity(d),dataset_split_hash=d['dataset_split_hash'],scorer_version='v1',audit_hash=r['audit_hash'],runtime_configuration_id=r['runtime_configuration_id'],tasks=2,solved=1,task_ids=ids,official_pass_at_1=.5)
  return r,d,proof
 def test_full_conformant_fixture(self):
  self.assertTrue(official_gate(*self.fixture()))
 def test_subsets_exceptions_and_missing_proofs_denied(self):
  for key in ['complete_task_set','official_scorer_verified','all_canonical_controls_passed','no_task_exclusions','prompt_protocol_verified','independent_audit_verified']:
   r,d,p=self.fixture();p[key]=False;self.assertFalse(official_gate(r,d,p),key)
  r,d,p=self.fixture();self.assertFalse(official_gate(r,d,None))
 def test_wrong_tasks_duplicate_tasks_and_denominator_denied(self):
  for ids in [['a'],['a','a'],['a','c']]:
   r,d,p=self.fixture();p['task_ids']=ids;self.assertFalse(official_gate(r,d,p))
  r,d,p=self.fixture();r['tasks']=1;self.assertFalse(official_gate(r,d,p))
 def test_version_hash_model_and_count_bindings(self):
  for key in ['benchmark_identity_id','dataset_split_hash','scorer_version','audit_hash','runtime_configuration_id','solved']:
   r,d,p=self.fixture();p[key]='wrong';self.assertFalse(official_gate(r,d,p),key)
  for key in ['benchmark_revision','dataset_split_hash','scorer_version','expected_task_ids_hash']:
   r,d,p=self.fixture();d[key]=None;self.assertFalse(official_gate(r,d,p))
 def test_unsupported_aggregation_cannot_use_simple_percentage(self):
  r,d,p=self.fixture();d['metric']='BFCL_official_aggregation';p['benchmark_identity_id']=definition_identity(d);r['benchmark_identity_id']=definition_identity(d);self.assertFalse(official_gate(r,d,p))
 def bfcl_fixture(self):
  r,d,p=self.fixture();ids=[f'simple_python_{i}' for i in range(400)]
  d.update(benchmark_id='bfcl-v4-simple-python-full400',required_task_count=400,expected_task_ids_hash=H(sorted(ids)),metric='bfcl_simple_python_ast_accuracy_percent')
  r.update(benchmark_id=d['benchmark_id'],benchmark_identity_id=definition_identity(d),tasks=400,solved=300,score_percent=75)
  p.pop('official_pass_at_1');p.update(benchmark_identity_id=definition_identity(d),tasks=400,solved=300,task_ids=ids,official_category='simple_python',category_only=True,official_correct_count=300,official_category_accuracy=.75)
  return r,d,p
 def test_complete_bfcl_category_has_its_own_metric(self):
  self.assertTrue(official_gate(*self.bfcl_fixture()))
 def test_bfcl_subset_or_whole_leaderboard_cannot_masquerade_as_category(self):
  for key,value in [('category_only',False),('official_category','overall'),('official_correct_count',299),('official_category_accuracy',.9),('all_canonical_controls_passed',False)]:
   r,d,p=self.bfcl_fixture();p[key]=value;self.assertFalse(official_gate(r,d,p),key)
  for key,value in [('benchmark_id','bfcl-v4-full'),('required_task_count',100)]:
   r,d,p=self.bfcl_fixture();d[key]=value;r['benchmark_id']=d['benchmark_id'];r['benchmark_identity_id']=p['benchmark_identity_id']=definition_identity(d);self.assertFalse(official_gate(r,d,p),key)
 def test_bfcl_requires_complete_unique_ids_and_exact_score(self):
  for ids in [[f'simple_python_{i}' for i in range(100)],['simple_python_0']*400]:
   r,d,p=self.bfcl_fixture();p['task_ids']=ids;self.assertFalse(official_gate(r,d,p))
  r,d,p=self.bfcl_fixture();p.pop('official_category_accuracy');p['official_pass_at_1']=.75;self.assertFalse(official_gate(r,d,p))
 def test_pass_at_one_must_match_the_recorded_numerator(self):
  r,d,p=self.fixture();p['official_pass_at_1']=.9;r['score_percent']=90;self.assertFalse(official_gate(r,d,p))
 def test_known_upstream_exception_requires_full_pinned_controls(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']}
  r=next(r for r in h['runs'] if r['official_eligible']);d=defs[r['benchmark_id']];p=r['qualification_audit'];self.assertTrue(official_gate(r,d,p))
  self.assertEqual(p['tasks'],164);self.assertFalse(p['all_canonical_controls_passed'])
  for key,value in [('task_ids',['HumanEval/0']),('control_task_count',163),('other_canonical_tasks_passed',162),('all_negative_controls_rejected',False),('unchanged_official_oracle_and_dataset',False),('full_task_set_independently_replayed',False),('official_oracle_source_sha256','0'*64)]:
   changed=copy.deepcopy(p);changed['canonical_reference_exception'][key]=value;self.assertFalse(official_gate(r,d,changed),key)
  changed=copy.deepcopy(p);changed['no_task_exclusions']=False;self.assertFalse(official_gate(r,d,changed))
 def test_mtp_warning_survives_official_api_admission(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());r=next(r for r in h['runs'] if r['official_eligible'] and r['experiment_id']=='R118');self.assertIn('not lossless',r['warning']);self.assertIn('local memory/time limits',r['warning'])
 def test_history_append_only(self):
  old=[{'id':'a','score':1}];new=[{'id':'b','score':2}];self.assertEqual(len(frozen_merge(old,new,'id')),2)
  with self.assertRaises(ValueError):frozen_merge(old,[{'id':'a','score':2}],'id')
  self.assertEqual(old,[{'id':'a','score':1}])
 def test_real_history_hashes_and_unknowns(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']};self.assertTrue(validate_history(h,defs))
  self.assertTrue(any(p['engine']['version'] is None for p in h['profiles']))
  h['runs'][0]['solved']+=1
  with self.assertRaises(ValueError):validate_history(h,defs)
 def test_historical_subset_cannot_be_promoted(self):
  h=json.loads((ROOT/'data/configuration-history.json').read_text());defs={d['benchmark_id']:d for d in json.loads((ROOT/'data/benchmark-register.json').read_text())['definitions']}
  h['runs'][0]['official_eligible']=True;h['runs'][0]['run_id']='run-'+H({k:v for k,v in h['runs'][0].items() if k!='run_id'})
  with self.assertRaises(ValueError):validate_history(h,defs)
 def test_engine_and_weight_identity_come_from_executed_argv(self):
  plan={'model_sha256':'b'*64,'runtime_identities':{'/art/model.gguf':'a'*64,'/bin/llama-server':'c'*64}}
  p=profile(plan,{'argv':['/bin/llama-server','--model','/art/model.gguf','--spec-type','none']},'test','Test','Q6','R1','d'*64,lambda x:x)
  self.assertEqual(p['model']['artifact_sha256'],'a'*64);self.assertEqual(p['engine']['name'],'llama.cpp-compatible');self.assertIsNone(p['engine']['version']);self.assertNotIn('/art/model.gguf',str(p))
  self.assertEqual(p['optimizations']['speculation_type'],'none');self.assertIsNone(p['optimizations']['cuda_graphs']['actual_capture_replay'])
 def test_deltas_require_same_task_set_and_scorer(self):
  a={'benchmark_identity_id':'a','evaluated_task_set_hash':'b','scorer_version':{'x':1},'tasks':2,'score_percent':50,'wall_s':10,'gpu_j_per_success':100};b={**a,'score_percent':100,'wall_s':8,'gpu_j_per_success':None}
  d=pair_delta(a,b);self.assertTrue(d['comparable']);self.assertEqual(d['quality_delta_pp'],50);self.assertAlmostEqual(d['latency_delta_percent'],-20);self.assertIsNone(d['energy_per_success_delta_percent']);self.assertIn('Whole-profile',d['interpretation'])
  for key in ['benchmark_identity_id','evaluated_task_set_hash','scorer_version','tasks']:
   c={**b,key:'different'};self.assertFalse(pair_delta(a,c)['comparable'])
 def test_publisher_and_local_views_separate_and_no_mean(self):
  reg=json.loads((ROOT/'data/benchmark-register.json').read_text());hist=json.loads((ROOT/'data/configuration-history.json').read_text());comp=json.loads((ROOT/'data/comparison.json').read_text())
  with tempfile.TemporaryDirectory() as tmp:
   d=pathlib.Path(tmp);(d/'benchmarks.md').write_text('# Old\n\n## Official benchmark results and overall mean\n\n91.04%\n\n## Configuration parameters and ranked benchmark results\n\nHistorical details\n');(d/'local-benchmarks.md').write_text('# Local')
   render(reg,hist,comp,d)
   main=(d/'benchmarks.md').read_text();supp=(d/'supplemental-comparison.md').read_text();self.assertIn(str(sum(r['official_eligible'] for r in hist['runs']))+' eligible official runs',main);self.assertIn('NOT MEASURED',main);self.assertNotIn('91.04%',supp);self.assertNotIn('reported_score',main);self.assertIn('EXTERNAL PUBLISHER SELF-REPORTS',(d/'benchmark-register.md').read_text());self.assertEqual(len(list((d/'configuration-profiles').glob('*.md'))),len(hist['profiles']))
if __name__=='__main__':unittest.main()
