import copy,json,unittest
from screening import validate,wilson,render
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
 def test_no_duplicate_checkpoint(self):
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
