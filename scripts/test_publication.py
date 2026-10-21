import importlib.util,pathlib,unittest
P=pathlib.Path(__file__).resolve().parent
def module(name):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module('validate');e=module('export')
class PublicationSafety(unittest.TestCase):
 def test_credentials_and_network_are_rejected(self):
  examples=['gh'+'p_'+'A'*30,'-----BEGIN '+'RSA PRIVATE KEY-----','192'+'.168.42.18','sensor'+'.bedroom_temperature','fd'+ '00::12','::'+'1','https://user'+':secret'+'@example.com']
  for x in examples:
   with self.subTest(category=examples.index(x)):self.assertTrue(v.content_errors(x))
 def test_projection_cannot_export_conversations(self):
  raw={'metrics':{'solved':13,'tasks':18,'messages':[{'content':'private conversation'}],'prompt_text':'private text','per_task':{'private_entity':{}}},'response':'private output','authorization':'secret'}
  out=e.metrics(raw);self.assertEqual(out,{'metrics':{'solved':13,'tasks':18}})
 def test_unknown_files_and_weights_rejected(self):
  for f in ['.env','weights.gguf','data/unreviewed.json','docs/private.log','scripts/extra.py']:
   self.assertFalse(v.allowed(pathlib.Path(f)))
 def test_nonpublic_source_url_rejected(self):
  self.assertIsNone(e.url('https://'+'192'+'.168.42.18/private'))
  self.assertIsNone(e.url('https://user'+':secret'+'@github.com/repo'))
 def test_missing_is_not_zero(self):self.assertEqual(e.metrics({'metrics':{'ttft_s':None,'solved':0}}),{'metrics':{'solved':0}})
if __name__=='__main__':unittest.main()
