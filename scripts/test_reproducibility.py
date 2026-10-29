import hashlib,json,tempfile,unittest
from pathlib import Path
from reproducibility import build

def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,sort_keys=True))
class HistoricalComparison(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.profiles={};self.raw={}
  for ident,cache,tokens in [('r1',False,[10,11]),('r2',True,[10,12])]:
   raw=self.root/('raw-'+ident);raw.mkdir();profile={'model_sha256':'a'*64,'native_recipe':{'request_options':{'seed':1001,'temperature':0}}};write(raw/'profile.json',profile)
   req={'seed':1001,'temperature':0,'cache_prompt':cache};rows=[{'kind':'agent_turn','id':'x','request':req,'reply':{'__verbose':{'generation_settings':{'seed':1001},'tokens':tokens}}},{'kind':'input_identity','id':'x','prompt_token_ids':[1,2]}];(raw/'HTTP_RESULTS.jsonl').write_text('\n'.join(json.dumps(r) for r in rows)+'\n');pins={n:h(raw/n) for n in ('profile.json','HTTP_RESULTS.jsonl')};write(raw/'RAW_HASHES.json',pins);audit=self.root/'staging'/ident/'AUDIT.json';write(audit,{'raw_root':str(raw)});self.raw[ident]=raw
   self.profiles[ident]={'audit_sha256':h(audit),'raw_responses_sha256':pins['HTTP_RESULTS.jsonl'],'profile_sha256':pins['profile.json'],'model_sha256':'a'*64,'configured_seed':1001,'configured_temperature':0,'request_count':1,'request_seeds':{'1001':1},'server_reported_seeds':{'1001':1},'input_token_ids_recorded':1,'output_token_ids_recorded':1}
  review={'profiles':self.profiles,'paired_historical':{'r1_r2':{'same_request_except_cache_flag':1,'different_prompt_token_sequences':0,'same_prompt_and_same_output_tokens':0,'same_prompt_and_different_output_tokens':1}},'build_source':{'commit':'b'*40}};write(self.root/'staging/reproducibility-20261029/REPRODUCIBILITY_REVIEW.json',review)
 def tearDown(self):self.tmp.cleanup()
 def test_aggregate_does_not_expose_tasks(self):
  out=build(self.root);self.assertEqual(out['paired_historical']['r1_r2']['different_outputs'],1);self.assertNotIn('prompt_token_ids',json.dumps(out));self.assertNotIn(str(self.root),json.dumps(out))
 def test_modified_capture_fails_closed(self):
  with (self.raw['r2']/'HTTP_RESULTS.jsonl').open('a') as f:f.write(' ')
  with self.assertRaises(AssertionError):build(self.root)
 def test_unsubstantiated_timing_is_rejected(self):
  fixed={'GPU_runs':0,'pairs':{'r1_r2':{'matched_requests':999,'reference_audit_sha256':'x','candidate_audit_sha256':'y'}}}
  write(self.root/'staging/reproducibility-20261029/FIXED_OUTPUT_TIMING_REVIEW.json',fixed)
  with self.assertRaises(AssertionError):build(self.root)
if __name__=='__main__':unittest.main()
