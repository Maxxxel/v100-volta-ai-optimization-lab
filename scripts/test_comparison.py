import copy,unittest,xml.etree.ElementTree as ET
from comparison import check,ratio,fingerprint,svg
class ComparisonTests(unittest.TestCase):
 def fixture(self):
  return {'cohorts':{'coding':{'task_sha256':'a'*64}},'records':[{'id':'a','tasks':164,'solved':132,'discipline':'coding','task_sha256':'a'*64,'audit_ids':['audit-abc'],'audit_sha256':['b'*64],'wall_s':12,'gpu_j':34,'peak_vram_mib':None}]}
 def test_cohort_mismatch_fails(self):
  d=self.fixture();d['records'][0]['task_sha256']='c'*64
  with self.assertRaises(ValueError):check(d)
 def test_counts_and_nonfinite_fail(self):
  for key,value in [('solved',165),('tasks',0),('wall_s',float('nan'))]:
   d=self.fixture();d['records'][0][key]=value
   with self.assertRaises(ValueError):check(d)
 def test_missing_is_not_zero(self):
  self.assertIsNone(ratio(None,10));self.assertIsNone(ratio(42,0));self.assertEqual(ratio(0,10),0)
  s=svg('Test','s',[{'label':'Missing','value':None}]);self.assertIn('NOT MEASURED',s);self.assertNotIn('fill="#51d8bc"',s)
 def test_zero_is_measured_and_svg_is_safe(self):
  s=svg('<b>','%', [{'label':'unsafe <script>&','value':0,'display':'0/10'}]);tree=ET.fromstring(s)
  self.assertIn('0/10',s);self.assertNotIn('<script>',s);self.assertNotIn('href=',s)
  self.assertTrue(all(x.tag.split('}')[-1] not in ('script','foreignObject') for x in tree.iter()))
 def test_content_identity_and_whisker(self):
  d=self.fixture();self.assertTrue(check(d));other=copy.deepcopy(d);other['records'][0]['solved']=131;self.assertNotEqual(fingerprint(d),fingerprint(other))
  s=svg('Repeated','s',[{'label':'A','value':10,'range':[9,11]}]);self.assertIn('stroke="#fff"',s)
if __name__=='__main__':unittest.main()
