import copy,hashlib,json,tempfile,unittest
from pathlib import Path
from reproducibility import build,hybrid_recurrent_state_semantics,logprobs_diagnostic_path,lost_task_first_divergence,qwen35_warmup_repeatability,seed_execution_path,summarize_nexus_policy_case,summarize_server_prompt_path,verify_aa_runtime_identity,validate_r635_pair
from export import projection

def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,sort_keys=True))
class RuntimeIdentity(unittest.TestCase):
 def test_only_review_and_lease_may_differ(self):
  a={'model':'hash','native_recipe':{'seed':1001},'review':'old','execution_review':'old'}
  b={**a,'review':'new','execution_review':'new'}
  x={'argv':['engine','--ctx-size','16384'],'environment':{'O2_GPU_BUILD_LEASE':'old','OMP_NUM_THREADS':'4'}}
  y={**x,'environment':{**x['environment'],'O2_GPU_BUILD_LEASE':'new'}}
  verify_aa_runtime_identity([a,b],[x,y])
  with self.assertRaises(AssertionError):verify_aa_runtime_identity([a,{**b,'native_recipe':{'seed':1002}}],[x,y])
  with self.assertRaises(AssertionError):verify_aa_runtime_identity([a,b],[x,{**y,'argv':['other-engine']}])
  with self.assertRaises(AssertionError):verify_aa_runtime_identity([a,b],[x,{**y,'environment':{**y['environment'],'OMP_NUM_THREADS':'8'}}])
 def test_qwen_aa_rejects_changed_tokens_and_policy(self):
  cases={str(i):{'reported_result':{'task_success':i<27,'policy_gate_pass':i<31}} for i in range(33)}
  turns={str(i):{'request':{'seed':1001},'reply':{'__verbose':{'tokens':[i]}}} for i in range(150)}
  inputs={str(i):{'prompt_token_ids':[i]} for i in range(150)}
  a={'agent_case':cases,'agent_turn':turns,'input_identity':inputs};b=copy.deepcopy(a);validate_r635_pair(a,b)
  b['agent_turn']['0']['reply']['__verbose']['tokens']=[99]
  with self.assertRaises(AssertionError):validate_r635_pair(a,b)
  b=copy.deepcopy(a);b['agent_case']['0']['reported_result']['policy_gate_pass']=False
  with self.assertRaises(AssertionError):validate_r635_pair(a,b)
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

class SeedPath(unittest.TestCase):
 def test_reconciles_request_and_server_seed_and_greedy_conditions(self):
  hashes={
   'tools/server/server-schema.cpp':'1f9d7b73b4363b90b08de0360b0a5ce0b3d152750bfb8d587a367e90c7904050',
   'tools/server/server-context.cpp':'6b5fdf2b246017b074c239e8f0b93f9d6952b4715501269627fec7a11b00bab7',
   'common/sampling.cpp':'b6a1f963fd75fd17d12bafb59351a1009d2358dd789dba7ed10943340f8e5553',
   'tools/server/server-common.cpp':'c4d53b4c72ca825434a035a4b632c8bc71e709d22fe33ca149fde95cee8460a1',
  }
  data={'build_source':{'commit':'097cf33d9499b1eade67d51e16d7c75427e7b267','checks':{k:{'actual':v,'proof':v} for k,v in hashes.items()}},
        'profiles':{'r616':{'configured_seed':1001,'request_count':1,'request_seeds':{'1001':1},'server_reported_seeds':{'1001':1}}}}
  turns={'private-turn':{'request':{'seed':1001,'stream':False,'tools':[]},'reply':{'__verbose':{'generation_settings':{'seed':1001,'temperature':0,'n_probs':0,'backend_sampling':False,'samplers':['temperature'],'dynatemp_range':0}}}}}
  out=seed_execution_path(data,{'r616':(turns,{})},Path('/tmp/no-r535-fixture'))
  self.assertEqual(out['profiles']['r616']['source_greedy_condition_requests'],1)
  self.assertTrue(out['profiles']['r616']['all_request_and_reported_seeds_match'])
  self.assertNotIn('private-turn',json.dumps(out))
  lp=logprobs_diagnostic_path(data,{'r616':(turns,{})})
  self.assertEqual(lp['non_stream_with_tools'],1)
  self.assertEqual(lp['default_top_logprobs'],20)
  self.assertIn('distribution sampler',lp['sampler_effect'])
  self.assertNotIn('private-turn',json.dumps(lp))
  turns['private-turn']['reply']['__verbose']['generation_settings']['seed']=7
  with self.assertRaises(AssertionError):seed_execution_path(data,{'r616':(turns,{})},Path('/tmp/no-r535-fixture'))

 def test_unknown_engine_source_does_not_claim_pinned_behavior(self):
  self.assertIsNone(seed_execution_path({'build_source':{'commit':'b'*40}},{},Path('/tmp/no-r535-fixture')))

class Qwen35WarmupRepeatability(unittest.TestCase):
 def fixture(self,diverge=False):
  tmp=tempfile.TemporaryDirectory();root=Path(tmp.name);model='02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d'
  template='/private/qwen35-template.jinja';runtime='/private/runtime/llama-server';records=[]
  for run,ident in enumerate(('r501','r509','r519','r535')):
   raw=root/f'raw-{ident}';raw.mkdir();profile={'model_sha256':model,'chat_template':template,
    'assets':{template:'a'*64,runtime:'b'*64},'native_recipe':{'argv_tail':['--model','/private/qwen.gguf','--ctx-size','8192','--seed','1001'],
     'context':8192,'environment':{'GGML_CUDA_GRAPH_OPT':'0'},'request_options':{'seed':1001,'temperature':0,'cache_prompt':False}}}
   write(raw/'profile.json',profile);write(raw/'LAUNCH.json',{'run':ident});(raw/'server.log').write_text('server started\n')
   rows=[]
   for wid,prompt,n_predict,content in [('warmup-0','synthetic warmup OK',1,'OK'),('warmup-1','synthetic labels',128,'A B C')]:
    if diverge and ident=='r535' and wid=='warmup-1':content='A B D'
    rows.append({'kind':'warmup','id':wid,'request':{'prompt':prompt,'seed':1001,'temperature':0,'n_predict':n_predict,'cache_prompt':False,'ignore_eos':True,'stream':False},
     'reply':{'content':content,'tokens':[],'tokens_predicted':n_predict,'stop_type':'limit','generation_settings':{'seed':1001,'temperature':0,'backend_sampling':False}}})
   (raw/'HTTP_RESULTS.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
   pins={name:h(raw/name) for name in ('profile.json','LAUNCH.json','HTTP_RESULTS.jsonl','server.log')};write(raw/'RAW_HASHES.json',pins)
   write(root/'phase_o2_restart_20261015_2245'/f'staging/{ident}/AUDIT.json',{'raw_root':str(raw),'GPU_execution_observed':True,'original_raw_files_sha256':pins})
  return tmp,root
 def test_hash_verified_same_prompt_warmups_are_narrow_text_evidence(self):
  tmp,root=self.fixture()
  try:
   out=qwen35_warmup_repeatability(root);self.assertEqual(out['distinct_gpu_experiments'],4)
   self.assertEqual([x['tokens_predicted'] for x in out['warmups']],[1,128])
   self.assertTrue(all(x['token_ids']=='NOT_CAPTURED' for x in out['warmups']))
   self.assertNotIn('synthetic warmup OK',json.dumps(out));self.assertNotIn('A B C',json.dumps(out))
  finally:tmp.cleanup()
 def test_changed_output_text_fails_closed(self):
  tmp,root=self.fixture(diverge=True)
  try:
   with self.assertRaises(AssertionError):qwen35_warmup_repeatability(root)
  finally:tmp.cleanup()

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

class ServerPromptPath(unittest.TestCase):
 def test_aligns_server_task_to_captured_request_without_exporting_task_id(self):
  with tempfile.TemporaryDirectory() as td:
   log=Path(td)/'server.log'
   log.write_text('\n'.join([
    '0.00.001.000 I slot launch_slot_: id 0 | task 0 | processing task, is_child = 0',
    '0.00.001.001 I slot operator(): id 0 | task 0 | new prompt, task.n_tokens = 11',
    '0.00.001.002 I slot print_timing: id 0 | task 0 | prompt eval time = 1.0 ms / 11 tokens',
    '0.00.001.003 I slot print_timing: id 0 | task 0 | eval time = 2.0 ms / 3 tokens',
    '0.00.002.000 I slot launch_slot_: id 0 | task 7 | processing task, is_child = 0',
    '0.00.002.001 I slot operator(): id 0 | task 7 | new prompt, task.n_tokens = 100',
    '0.00.002.002 I slot print_timing: id 0 | task 7 | prompt eval time = 5.0 ms / 4 tokens',
    '0.00.002.003 I slot print_timing: id 0 | task 7 | eval time = 6.0 ms / 8 tokens',
   ])+'\n')
   rows=[{'kind':'warmup','start_ns':0},
         {'kind':'agent_turn','id':'selected','start_ns':1,'request':{'cache_prompt':True},
          'reply':{'usage':{'prompt_tokens':100,'completion_tokens':8,'prompt_tokens_details':{'cached_tokens':96}},
                   '__verbose':{'timings':{'cache_n':96}}}}]
   out=summarize_server_prompt_path(rows,log,'selected')
   self.assertEqual(out['exact_input_and_completion_token_matches'],1)
   self.assertEqual(out['server_input_eval_tokens'],4)
   self.assertEqual(out['selected_reported_cached_tokens'],96)
   self.assertNotIn('task_id',json.dumps(out))
   rows[1]['reply']['usage']['completion_tokens']=9
   with self.assertRaises(AssertionError):summarize_server_prompt_path(rows,log,'selected')

class HybridCheckpointSource(unittest.TestCase):
 def test_partial_checkpoint_excludes_attention_but_keeps_recurrent_state(self):
  hybrid='''void state_write() {
    if ((flags & LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY) == 0) {
        mem_attn->state_write(io, seq_id, flags);
    }
    mem_recr->state_write(io, seq_id, flags);
  }
  void state_read() {
    const bool read_attn = (flags & LLAMA_STATE_SEQ_FLAGS_PARTIAL_ONLY) == 0;
    if (read_attn) {
        mem_attn->state_read(io, seq_id, flags);
    }
    mem_recr->state_read(io, seq_id, flags);
  }'''.splitlines()
  recurrent='''void llama_memory_recurrent::state_write() {}
  state_write_data(io, cell_ranges_data);
  void llama_memory_recurrent::state_read() {}'''.splitlines()
  result=hybrid_recurrent_state_semantics(hybrid,recurrent)
  self.assertGreater(result['hybrid_source_lines']['recurrent_write_after_guard'],result['hybrid_source_lines']['attention_write'])
  self.assertGreater(result['hybrid_source_lines']['recurrent_read_after_guard'],result['hybrid_source_lines']['attention_read'])
  self.assertTrue(result['recurrent_source_lines']['state_write_data'])
  broken=[line for line in hybrid if 'mem_recr->state_write' not in line]
  with self.assertRaises(AssertionError):hybrid_recurrent_state_semantics(broken,recurrent)

if __name__=='__main__':unittest.main()
