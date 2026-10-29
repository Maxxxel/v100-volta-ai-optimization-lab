import hashlib,json,tempfile,unittest
from pathlib import Path
from reproducibility import build,lost_task_first_divergence,summarize_nexus_policy_case
from export import projection

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

class LostTaskMapping(unittest.TestCase):
 def captures(self, prompt_change=False):
  case='private-case-id'; baseline_checks=[{'id':case,'task_success':True}];candidate_checks=[{'id':case,'task_success':False}]
  base=[];candidate=[]
  prompts=[1505,1637,1790]
  output_lengths_base=[39,39,558];output_lengths_candidate=[39,39,166,182,318]
  for turn,n in enumerate(prompts):
   ids=list(range(n));candidate_ids=list(range(n))
   if prompt_change and turn==2:candidate_ids[-1]+=1
   token_id=f'{case}--turn{turn}';aout=[turn+1]*output_lengths_base[turn];bout=aout if turn<2 else [98]*output_lengths_candidate[turn]
   for dest,cache,out,prompt_ids,cache_n in ((base,False,aout,ids,0),(candidate,True,bout,candidate_ids,[0,1543,1675][turn])):
    dest.extend([
     {'kind':'input_identity','id':token_id,'prompt_token_count':n,'prompt_token_ids':prompt_ids,'prompt_token_ids_sha256':hashlib.sha256(json.dumps(prompt_ids,separators=(',',':')).encode()).hexdigest()},
     {'kind':'agent_turn','id':token_id,'request':{'cache_prompt':cache,'seed':1001,'temperature':0},'reply':{'__verbose':{'tokens':out,'timings':{'cache_n':cache_n}}}},
    ])
  for turn,length in ((3,182),(4,318)):
   token_id=f'{case}--turn{turn}';candidate.append({'kind':'agent_turn','id':token_id,'request':{'cache_prompt':True,'seed':1001,'temperature':0},'reply':{'__verbose':{'tokens':[98]*length,'timings':{'cache_n':0}}}})
  return baseline_checks,candidate_checks,base,candidate
 def test_maps_only_scoped_lost_task_and_discloses_token_cost(self):
  a,b,ar,br=self.captures();out=lost_task_first_divergence(a,b,ar,br)
  self.assertEqual(out['turns'][2]['first_difference_index'],0)
  self.assertEqual(out['turns'][2]['candidate_cached_tokens'],1675)
  self.assertEqual(out['agent_trajectory'],{'baseline_turns':3,'candidate_turns':5,'extra_candidate_turns':2,'baseline_generated_tokens':636,'candidate_generated_tokens':744})
  self.assertNotIn('private-case-id',json.dumps(out))
 def test_changed_prompt_ids_fail_closed(self):
  a,b,ar,br=self.captures(prompt_change=True)
  with self.assertRaises(AssertionError):lost_task_first_divergence(a,b,ar,br)

class NexusPolicyMapping(unittest.TestCase):
 def sample(self,corrupt_cache=False):
  base_case={'task_success':False,'policy_gate_pass':True,'policy_violations':0,'rejected_calls':0,'all_tools_simulated':True,'production_tools_connected':False,'trace':[]}
  cand_case={'task_success':False,'policy_gate_pass':False,'policy_violations':1,'rejected_calls':1,'all_tools_simulated':True,'production_tools_connected':False,'trace':[{'kind':'tool_response','policy_rejected':True}]}
  base_req={'seed':1001,'temperature':0,'max_tokens':4096,'cache_prompt':False};cand_req={**base_req,'cache_prompt':True}
  out_a=[7]*368;out_b=[8]*65
  base_reply={'__verbose':{'tokens':out_a}}
  cand_reply={'__verbose':{'tokens':out_b}}
  pilot=[]
  for i in range(8):
   cached=i%2==1;tokens=(out_b[:] if cached else out_a[:])
   if corrupt_cache and i==1:tokens[1]=9
   pilot.append({'request':{**base_req,'cache_prompt':cached},'reply':{'__verbose':{'tokens':tokens,'timings':{'cache_n':1711 if cached else 0},'generation_settings':{'seed':1001,'temperature':0}}}})
  return base_case,cand_case,base_req,cand_req,base_reply,cand_reply,pilot
 def test_reproduces_case_local_cache_association_without_overclaim(self):
  args=self.sample();out=summarize_nexus_policy_case(*args,[1]*1785,args[6])
  self.assertEqual(out['cache_repeats_match_candidate'],4)
  self.assertEqual(out['first_difference_index'],0)
  self.assertEqual(out['task_success_changed_cases'],0)
  self.assertIn('WHOLE_TASK_CAUSALITY_NOT_ESTABLISHED',out['classification'])
  public=projection({'nexus_policy_case_mapping':out});encoded=json.dumps(public)
  self.assertNotIn('case_id',encoded);self.assertNotIn('prompt_token_ids',encoded);self.assertNotIn('private-case-id',encoded)
 def test_inconsistent_repeated_cache_output_fails_closed(self):
  args=self.sample(corrupt_cache=True)
  with self.assertRaises(AssertionError):summarize_nexus_policy_case(*args,[1]*1785,args[6])
if __name__=='__main__':unittest.main()
