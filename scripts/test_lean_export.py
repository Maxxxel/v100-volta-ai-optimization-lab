"""Lean-harness reporting preserves negative and missing evidence."""
import copy,json,pathlib,unittest
from render import lean_harness_report
from lean_metrics import measured_sum
class LeanReport(unittest.TestCase):
 def test_missing_measurement_is_not_zero(self):
  self.assertIsNone(measured_sum([3,None]));self.assertIsNone(measured_sum([]));self.assertEqual(measured_sum([0,3]),3)
 def test_negative_result_is_separate_and_all_costs_remain(self):
  es=json.loads((pathlib.Path(__file__).resolve().parents[1]/'data/experiments.json').read_text())
  lean=[e for e in es if e.get('aggregate_metrics',{}).get('native_lean_harness_ablation')]
  self.assertTrue(lean);before=copy.deepcopy(lean);page=lean_harness_report(lean)
  for phrase in ['28/33','25/33','301561','293897','rejected','NOT MEASURED','not official benchmarks','Failed tasks remain','No population-equivalence']:
   self.assertIn(phrase,page)
  self.assertEqual(lean,before)
 def test_qualification_cannot_be_smuggled_into_report(self):
  e={'aggregate_metrics':{'native_lean_harness_ablation':{'official_benchmark':True,'winner_qualified':False}}}
  with self.assertRaises(AssertionError):lean_harness_report([e])

class LeanProtocolIdentity(unittest.TestCase):
 def test_unknown_dataset_is_rejected_before_raw_projection(self):
  from unittest.mock import patch
  import export
  audit={'status':'LEAN_HARNESS_DEVELOPMENT66_COMPLETE','measurement_valid':True,'GPU_execution_observed':True,'dataset_id':'renamed-unknown-protocol'}
  with patch.object(export,'digest',return_value='a'*64),patch.object(export,'load',return_value=audit):
   with self.assertRaises(AssertionError):export.verified_native_lean_harness(pathlib.Path('/public-fixture'),{'audit_path':'/public-fixture/audit.json','audit_sha256':'a'*64},lambda *_:None)
 def test_development_gate_never_becomes_qualification_in_report(self):
  es=json.loads((pathlib.Path(__file__).resolve().parents[1]/'data/experiments.json').read_text())
  row=copy.deepcopy(next(e for e in es if e.get('aggregate_metrics',{}).get('native_lean_harness_ablation')))
  r=row['aggregate_metrics']['native_lean_harness_ablation'];r['dataset_id']='jarvis-lean-tool-json-ablation33-v1';r['comparison']['decision']='DEVELOPMENT_ONLY_REQUIRES_INDEPENDENT_CONFIRMATION'
  page=lean_harness_report([row]);self.assertIn('compact tool-result JSON',page);self.assertIn('no promotion',page);self.assertNotIn('Decision: rejected',page);self.assertIn('not official benchmarks',page)
 def test_arm_identity_is_not_silently_relabelled(self):
  from lean_metrics import reviews
  case={'kind':'agent_case','id':'compact-tool-json-v1--case','reported_result':{'all_tools_simulated':True,'production_tools_connected':False,'task_scope_pass':True}}
  with self.assertRaises(ValueError):reviews({'experiment_id':'CPU'},[case],'a'*64,[],lambda *_:None)


class TransformPublication(unittest.TestCase):
 def test_reverse_slice_syntax_is_not_an_address(self):
  from validate import content_errors
  colon=chr(58)*2
  self.assertEqual(content_errors('ARMS['+colon+'-1]'),[])
 def test_actual_private_ipv6_addresses_remain_blocked(self):
  from validate import content_errors
  colon=chr(58)*2
  for literal in ('['+colon+']','['+colon+'1]'):
   self.assertIn('nonpublic IPv6 address',content_errors(literal))
 def test_only_named_pure_transform_assets_are_allowlisted(self):
  from validate import allowed
  self.assertTrue(allowed(pathlib.Path('docs/assets/harness/preaction-checklist.py')))
  self.assertFalse(allowed(pathlib.Path('docs/assets/harness/unreviewed.py')))
 def test_published_sources_match_captured_module_identity(self):
  import hashlib
  root=pathlib.Path(__file__).resolve().parents[1];rows=json.loads((root/'data/experiments.json').read_text());count=0
  for row in rows:
   r=row.get('aggregate_metrics',{}).get('native_lean_harness_ablation') or row.get('aggregate_metrics',{}).get('native_lean_harness_screen')
   if r and r.get('transform_source'):
    item=r['transform_source'];self.assertEqual(hashlib.sha256((root/'docs'/item['file']).read_bytes()).hexdigest(),r['implementation']['transform_module_sha256']);self.assertEqual(item['license'],'MIT');count+=1
  self.assertEqual(count,3)

class HistoricalScreenPublication(unittest.TestCase):
 def records(self):
  root=pathlib.Path(__file__).resolve().parents[1];return root,json.loads((root/'data/experiments.json').read_text())
 def test_real_screen_uses_one_new_arm_and_a_separate_stored_control(self):
  _,rows=self.records();r=next(x for x in rows if x['id']=='R588')['aggregate_metrics']['native_lean_harness_screen'];self.assertTrue(r['screen_only']);self.assertEqual(r['case_executions'],33);self.assertEqual(r['paired_unique_cases'],0);self.assertEqual(len(r['arms']),1);self.assertEqual(r['arms'][0]['solved'],29);self.assertEqual(r['stored_reference']['metrics']['solved'],28);self.assertEqual(r['stored_reference']['new_GPU_runs'],0);self.assertFalse(r['stored_reference']['fresh_contemporaneous_control']);self.assertFalse(r['winner_qualified']);self.assertFalse(r['official_benchmark'])
 def test_screen_render_does_not_claim_fresh_balanced_execution(self):
  _,rows=self.records();row=next(x for x in rows if x['id']=='R588');page=lean_harness_report([row]);self.assertIn('B-only screen',page);self.assertIn('reference · R587 stored',page);self.assertIn('No new A0 run',page);self.assertIn('reproduced all33 outcomes',page);self.assertNotIn('alternating AB/BA',page)
 def test_exact_published_transforms_keep_reference_requests_unchanged(self):
  import importlib.util
  root,rows=self.records()
  for row in rows:
   r=row.get('aggregate_metrics',{}).get('native_lean_harness_ablation') or row.get('aggregate_metrics',{}).get('native_lean_harness_screen')
   if not r or not r.get('transform_source'):continue
   spec=importlib.util.spec_from_file_location('public_transform_'+row['id'],root/'docs'/r['transform_source']['file']);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
   system=module.KNOWN_SYSTEMS[1] if hasattr(module,'KNOWN_SYSTEMS') else module.ORIGINAL+module.REQUIRED if hasattr(module,'ORIGINAL') else 'unmodified system'
   body={'messages':[{'role':'system','content':system},{'role':'user','content':'Read the synthetic task'}],'tools':[],'temperature':0};before=copy.deepcopy(body)
   self.assertEqual(module.transform(body,'reference')[0],body);self.assertEqual(body,before)

class Frozen32ScreenReport(unittest.TestCase):
 def test_promising_screen_keeps_official_and_confirmation_boundaries(self):
  root=pathlib.Path(__file__).resolve().parents[1]
  research=json.loads((root/'data/snapshot.json').read_text())['lean_harness_review']
  r=research.get('screening32')
  if r is None:self.skipTest('No audited32-screen in this publication snapshot')
  before=copy.deepcopy(research);page=lean_harness_report([],research)
  for phrase in ('14/16','R515','R592','not a qualified gain','fresh controlled comparison','not upstream Caveman'):
   self.assertIn(phrase,page)
  self.assertFalse(r['official_benchmark']);self.assertFalse(r['winner_qualified']);self.assertFalse(r['fresh_contemporaneous_control']);self.assertEqual(research,before)
 def test_original_validator_contracts_are_not_compressor_or_GPU_evidence(self):
  root=pathlib.Path(__file__).resolve().parents[1];research=json.loads((root/'data/snapshot.json').read_text())['lean_harness_review'];cpu=research.get('upstream_validator_CPU')
  if cpu is None:self.skipTest('No original-validator CPU evidence in this snapshot')
  self.assertEqual(cpu['GPU_calls'],0);self.assertEqual(cpu['model_calls'],0);self.assertEqual(len(cpu['cases']),9)
  page=lean_harness_report([],research);self.assertIn('not generated compressor output',page);self.assertIn('remains under evaluation',page)

class OriginalSkillRejection(unittest.TestCase):
 def test_actual_skill_failure_is_retained_without_rejecting_other_components(self):
  root=pathlib.Path(__file__).resolve().parents[1];research=json.loads((root/'data/snapshot.json').read_text())['lean_harness_review']
  rows={r['experiment_id']:r for r in research.get('screening32_runs',[])}
  if 'R593' not in rows:self.skipTest('Original-skill GPU result absent from this snapshot')
  result=rows['R593'];self.assertEqual(result['categories']['coding']['candidate_successes'],2);self.assertEqual(result['categories']['tools']['candidate_successes'],6)
  self.assertEqual(result['categories']['coding']['lost'],12);self.assertEqual(result['categories']['tools']['lost'],8);self.assertFalse(result['winner_qualified']);self.assertFalse(result['official_benchmark'])
  page=lean_harness_report([],research)
  for phrase in ('Rejected exact profile','Coding 2/16','Tools 6/16','not its model-assisted compressor or proxy','only to this exact tested profile'):self.assertIn(phrase,page)
  self.assertIn('+196.531%',page)
