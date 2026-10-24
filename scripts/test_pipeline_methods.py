"""CPU-study export boundaries; private analysis inputs are never executed."""
import copy,json,pathlib,tempfile,unittest
from leaderboard import digest,pipeline_method_review,browser_register
class PipelineProjectionTests(unittest.TestCase):
 def fixture(self,root):
  source=root/'source.json';source.write_text(json.dumps({'private_evidence':'PRIVATE_PROOF_CONTENT'}));audit=root/'audit.json'
  summary=dict(review_id='CPU_METHODS',date='2026-10-24',evidence='CPU_RETROSPECTIVE',new_GPU_runs=0,census={},sampling_sizes=[8,16],resamples_per_condition=1000,total_resampled_subsets=2000,cohorts={},cohort_source_experiments=[],simulation=[],controls={},decision={'current_GPU_policy_changed':False,'hard_quality_gate_adopted':False},nexus_development={'status':'PLANNED_NOT_EXECUTED_NOT_BROKER_ADMITTED'},budget={},multi_agent={},limitations=[])
  a=dict(kind='CPU_PIPELINE_METHODS_REVIEW',status='DECISION_COMPLETE_NO_GPU_ADMISSION',new_GPU_runs=0,new_model_requests=0,original_audits_modified=False,official_results_modified=False,benchmark_admission_policy_changed=False,source_files_sha256={str(source):digest(source)},analysis_plan_sha256='a'*64,analysis_result_sha256='b'*64,source_code_sha256='c'*64,public_summary=summary)
  audit.write_text(json.dumps(a));return audit,source,a
 def entry(self,p):return {'audit_path':p.name,'audit_sha256':digest(p)}
 def test_only_safe_summary_is_exported(self):
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);audit,source,a=self.fixture(root);out=pipeline_method_review(root,self.entry(audit),lambda p,h:'audit-'+h[:20]);text=json.dumps(out)
   for secret in ['PRIVATE_PROOF_CONTENT','source_files_sha256','audit_path',str(root)]:self.assertNotIn(secret,text)
   self.assertEqual(out['audit_sha256'],digest(audit));self.assertFalse(out['decision']['hard_quality_gate_adopted'])
 def test_changed_source_and_changed_audit_are_rejected(self):
  for changed in ('source','audit'):
   with self.subTest(changed=changed),tempfile.TemporaryDirectory() as folder:
    root=pathlib.Path(folder);audit,source,a=self.fixture(root);entry=self.entry(audit)
    if changed=='source':source.write_text('{}')
    else:audit.write_text('{}')
    with self.assertRaises(ValueError):pipeline_method_review(root,entry,lambda p,h:'id')
 def test_fake_GPU_claim_or_policy_change_cannot_be_exported(self):
  for field,value in [('new_GPU_runs',1),('new_model_requests',1),('benchmark_admission_policy_changed',True),('original_audits_modified',True),('official_results_modified',True)]:
   with self.subTest(field=field),tempfile.TemporaryDirectory() as folder:
    root=pathlib.Path(folder);audit,source,a=self.fixture(root);a[field]=value;audit.write_text(json.dumps(a))
    with self.assertRaises(ValueError):pipeline_method_review(root,self.entry(audit),lambda p,h:'id')
 def test_unknown_or_nested_raw_inputs_are_rejected(self):
  for mode in ('unknown','nested','activated-gate'):
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as folder:
    root=pathlib.Path(folder);audit,source,a=self.fixture(root)
    if mode=='unknown':a['public_summary']['raw_root']='private'
    elif mode=='nested':a['public_summary']['census']['messages']=[{'content':'private'}]
    else:a['public_summary']['decision']['hard_quality_gate_adopted']=True
    audit.write_text(json.dumps(a))
    with self.assertRaises(ValueError):pipeline_method_review(root,self.entry(audit),lambda p,h:'id')
 def test_study_stays_out_of_interactive_score_bundle(self):
  original={'definitions':[{'benchmark_id':'unchanged'}],'pipeline_method_reviews':[{'simulation':'not a model score'}]};saved=copy.deepcopy(original);out=browser_register(original)
  self.assertEqual(original,saved);self.assertEqual(out['definitions'],original['definitions']);self.assertNotIn('pipeline_method_reviews',out)
