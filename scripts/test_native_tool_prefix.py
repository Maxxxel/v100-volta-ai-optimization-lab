"""Synthetic CPU fixtures; never exported as scientific measurements."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import datetime,types
from unittest.mock import patch
import leaderboard
from leaderboard import H,digest,native_tool_coverage,verify_native_tool_prefix


class ToolPrefix(unittest.TestCase):
 def coverage(self,count=2):
  ids=['simple_python_'+str(i) for i in range(400)]
  a=dict(collected_tasks=count,scored_tasks=count,full_benchmark_score_claimed=False,status='STOPPED_USER_TASK_TIME_BUDGET')
  return ids[:count],ids,ids.copy(),a,dict(benchmark_id='bfcl-v4-simple-python-full400',required_task_count=400,expected_task_ids_hash=H(sorted(ids)))

 def test_parallel_multiple200_has_exact_own_full_and_partial_scope(self):
  ids=['parallel_multiple_'+str(i) for i in range(200)]
  bench=dict(benchmark_id='bfcl-v4-parallel-multiple-full200',required_task_count=200,expected_task_ids_hash=H(sorted(ids)))
  full=dict(collected_tasks=200,scored_tasks=200,full_benchmark_score_claimed=True,status='FULL_NATIVE_TOOLS_OFFICIAL_API_PENDING')
  self.assertFalse(native_tool_coverage(ids,ids,ids,full,bench))
  partial=dict(collected_tasks=80,scored_tasks=80,full_benchmark_score_claimed=False,status='STOPPED_USER_TASK_TIME_BUDGET')
  self.assertTrue(native_tool_coverage(ids[:80],ids,ids,partial,bench))
  for wrong in ('bfcl-v4-simple-python-full400','bfcl-v4-full','unknown'):
   with self.subTest(wrong=wrong),self.assertRaises(ValueError):native_tool_coverage(ids,ids,ids,full,{**bench,'benchmark_id':wrong})

 def test_complete_category_and_prefix_have_distinct_scopes(self):
  self.assertTrue(native_tool_coverage(*self.coverage()))
  args=list(self.coverage(400));args[3].update(full_benchmark_score_claimed=True,status='FULL_NATIVE_TOOLS_OFFICIAL_API_PENDING')
  self.assertFalse(native_tool_coverage(*args))

 def test_no_full_claim_or_changed_denominator_for_a_prefix(self):
  for mode in ('full-claim','wrong-count','wrong-scorer-count','other-stop','zero','duplicate','reordered','short-plan','wrong-benchmark'):
   args=list(self.coverage())
   if mode=='full-claim':args[3]['full_benchmark_score_claimed']=True
   elif mode=='wrong-count':args[3]['collected_tasks']=400
   elif mode=='wrong-scorer-count':args[3]['scored_tasks']=1
   elif mode=='other-stop':args[3]['status']='UNEXPLAINED_EXECUTION_FAILURE'
   elif mode=='zero':args[0]=[]
   elif mode=='duplicate':args[0]=[args[0][0]]*2
   elif mode=='reordered':args[0].reverse()
   elif mode=='short-plan':args[1]=args[1][:2]
   else:args[4]['required_task_count']=2
   with self.subTest(mode=mode),self.assertRaises(ValueError):native_tool_coverage(*args)

 def fixture(self,root):
  out=root/'raw';out.mkdir()
  rows=[dict(kind='warmup',id='warmup-0'),dict(kind='native_tool',id='simple_python_0',reply={'content':'fixture'})]
  def save(p,d):p.write_text(json.dumps(d));return digest(p)
  save(out/'LAUNCH.json',{'uid':65534})
  (out/'CT_STDOUT.log').write_text('\n'.join('TASK_EVENT '+json.dumps(r) for r in rows)+'\n')
  tele=dict(processes=[{'host_pid':100}],device_vram_bytes=2*2**30,ecc_uncorrected=0,temperature_c=60,power_limit_w=300,clock_throttle_event_mask=0)
  (out/'GPU_TELEMETRY.jsonl').write_text(json.dumps(tele)+'\n')
  (root/'TIMEOUT_JOURNAL.jsonl').write_text(json.dumps({'MESSAGE':'RuntimeError: Pure task1200s budget exhausted'})+'\n')
  proof=dict(kind='POST_STOP_PARTIAL_COLLECTION_INTEGRITY_RECEIPT',derived_hash_manifest=True,full_score_or_successful_GPU_completion_claimed=False,source_controller_completion_available=False,GPU_reruns=0,model_queries=0,native_tool_complete_responses=1,expected_tasks=400,original_files_sha256={p.name:digest(p) for p in out.iterdir()},timeout_journal_sha256=digest(root/'TIMEOUT_JOURNAL.jsonl'))
  save(out/'POST_STOP_CAPTURE.json',proof)
  return out,dict(partial_collection=True,execution_uid=65534),dict(power_w=300,temperature_c=90,vram_mib=14336),rows,proof,save

 def test_independent_capture_deadline_and_guard_proof_is_required(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);out,gpu,c,rows,proof,_=self.fixture(root)
   self.assertEqual(verify_native_tool_prefix(root,out,gpu,c,rows,1),out/'POST_STOP_CAPTURE.json')

 def test_rehashed_tampering_and_unsafe_hardware_do_not_become_valid_partial_results(self):
  for mode in ('changed-reply','no-deadline','ECC','hot','VRAM','throttle','parallel','wrong-UID','full-completion','false-count','GPU-repeat','changed-original'):
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);out,gpu,c,rows,proof,save=self.fixture(root)
    if mode=='changed-reply':rows[-1]['reply']['content']='modified'
    elif mode=='no-deadline':
     (root/'TIMEOUT_JOURNAL.jsonl').write_text(json.dumps({'MESSAGE':'unknown failure'})+'\n');proof['timeout_journal_sha256']=digest(root/'TIMEOUT_JOURNAL.jsonl')
    elif mode in ('ECC','hot','VRAM','throttle','parallel'):
     tele=json.loads((out/'GPU_TELEMETRY.jsonl').read_text())
     if mode=='ECC':tele['ecc_uncorrected']=1
     elif mode=='hot':tele['temperature_c']=90
     elif mode=='VRAM':tele['device_vram_bytes']=14337*2**20
     elif mode=='throttle':tele['clock_throttle_event_mask']=0x20
     else:tele['processes']*=2
     save(out/'GPU_TELEMETRY.jsonl',tele);proof['original_files_sha256']['GPU_TELEMETRY.jsonl']=digest(out/'GPU_TELEMETRY.jsonl')
    elif mode=='wrong-UID':save(out/'LAUNCH.json',{'uid':0});proof['original_files_sha256']['LAUNCH.json']=digest(out/'LAUNCH.json')
    elif mode=='full-completion':save(out/'HOST_COMPLETION.json',{'status':'GPU_COMPLETE_AUDITED'})
    elif mode=='false-count':proof['native_tool_complete_responses']=400
    elif mode=='GPU-repeat':proof['GPU_reruns']=1
    else:(out/'LAUNCH.json').write_text('changed')
    save(out/'POST_STOP_CAPTURE.json',proof)
    with self.assertRaises((ValueError,json.JSONDecodeError)):verify_native_tool_prefix(root,out,gpu,c,rows,1)

 def test_transport_stop_is_distinct_from_budget_and_requires_privileged_http_trace(self):
  for mode in ('valid','as-deadline','no-controller-fault','model-text-only','wrong-scope'):
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);out,gpu,c,rows,proof,save=self.fixture(root)
    status='STOPPED_NATIVE_TRANSPORT_TIMEOUT';proof['capture_stop_kind']=status
    trace='response.begin()\nself._read_status()\nTimeoutError: timed out\n'
    p=out/'CT_STDOUT.log';p.write_text(p.read_text()+trace);proof['original_files_sha256'][p.name]=digest(p)
    journal=root/'TIMEOUT_JOURNAL.jsonl';journal.write_text(json.dumps({'MESSAGE':'AssertionError: Fixed CT worker failed'})+'\n')
    if mode=='as-deadline':status='STOPPED_USER_TASK_TIME_BUDGET'
    elif mode=='no-controller-fault':journal.write_text(json.dumps({'MESSAGE':'unexplained'})+'\n')
    elif mode=='model-text-only':
     p.write_text(''.join('TASK_EVENT '+json.dumps(r)+'\n' for r in rows)+json.dumps({'reply':trace})+'\n');proof['original_files_sha256'][p.name]=digest(p)
    elif mode=='wrong-scope':proof['capture_stop_kind']='STOPPED_USER_TASK_TIME_BUDGET'
    proof['timeout_journal_sha256']=digest(journal);save(out/'POST_STOP_CAPTURE.json',proof)
    if mode=='valid':
     args=list(self.coverage());args[3]['status']=status;self.assertTrue(native_tool_coverage(*args))
     self.assertEqual(verify_native_tool_prefix(root,out,gpu,c,rows,1,status),out/'POST_STOP_CAPTURE.json')
    else:
     with self.assertRaises(ValueError):verify_native_tool_prefix(root,out,gpu,c,rows,1,status)


class WrapperStop(unittest.TestCase):
 """Synthetic journal/ownership fixtures only; no actual privileged files."""
 def fixture(self,root):
  c={'id':'r990-wrapper-fixture','runtime_seconds':1200}
  def save(p,v):p.write_text(json.dumps(v));return digest(p)
  initial=root/'INITIAL.json';save(initial,{'trial_id':c['id'],'contract_sha256':H(c),'policy':{'task_seconds':1200,'startup_seconds':180,'cleanup_seconds':60,'wall_seconds':1440}})
  marker=root/(c['id']+'.started');m={'trial':c['id'],'at':datetime.datetime.fromtimestamp(1800000000,datetime.timezone.utc).isoformat(),'sha256':'b'*64,'actual_RuntimeMaxSec':1310,'whole_benchmark_budget':{'timing_scope':'TASK_PHASE_ONLY','phase':'startup','remaining_s':1200,'clock_sha256':{'initial':digest(initial)}}};save(marker,m)
  review={'kind':'VERIFIED_PROTECTED_GPU_WRAPPER_TIMEOUT','trial_id':c['id'],'contract_sha256':H(c),'GPU_reruns':0,'clock_reset':False,'protected_start_marker_file':str(marker),'protected_initial_clock_file':str(initial),'source_files_sha256':{str(p):digest(p) for p in (marker,initial)}};save(root/'WRAPPER_STOP_REVIEW.json',review)
  unit='v100-gpu-'+c['id']+'.service';base={'UNIT':unit,'_PID':'1','_UID':'0'}
  journal=[{**base,'MESSAGE':unit+': Service reached runtime time limit. Stopping.','__REALTIME_TIMESTAMP':str(1800001310100000)},{**base,'MESSAGE':unit+": Failed with result 'timeout'.",'__REALTIME_TIMESTAMP':str(1800001312100000)}]
  return c,review,journal,m,save
 def valid(self,root,c,journal,uid=0,mode=0o100644):
  # Model protected-source ownership without requiring root in CI. No actual
  # filesystem permissions, broker state, GPU or operating-system log is changed.
  with patch.object(leaderboard.pathlib.Path,'stat',return_value=types.SimpleNamespace(st_uid=uid,st_mode=mode)):
   return leaderboard.verified_wrapper_stop(root,c,journal,['b'*64])
 def test_real_timeout_metadata_and_pinned_original_clock_required(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);c,review,journal,m,save=self.fixture(root);self.assertEqual(self.valid(root,c,journal),review)
 def test_manual_stop_wrong_unit_or_nonroot_journal_cannot_masquerade_as_wrapper_deadline(self):
  for field,value in (('_PID','100'),('_UID','1001'),('UNIT','other.service'),('MESSAGE','Stopped manually'),('__REALTIME_TIMESTAMP','1800000010000000')):
   with self.subTest(field=field),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);c,review,journal,m,save=self.fixture(root);journal[0][field]=value
    with self.assertRaises(ValueError):self.valid(root,c,journal)
 def test_changed_marker_unknown_runner_and_unprotected_source_rejected(self):
  for mode in ('changed','runner','owner','writable'):
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);c,review,journal,m,save=self.fixture(root);p=Path(review['protected_start_marker_file'])
    if mode=='changed':p.write_text('{}')
    if mode=='runner':
     m['sha256']='c'*64;review['source_files_sha256'][str(p)]=save(p,m);save(root/'WRAPPER_STOP_REVIEW.json',review)
    with self.assertRaises(ValueError):self.valid(root,c,journal,uid=1001 if mode=='owner' else 0,mode=0o100666 if mode=='writable' else 0o100644)
 def test_rehashed_changed_policy_or_contract_does_not_reset_budget(self):
  for field in ('policy','contract'):
   with self.subTest(field=field),tempfile.TemporaryDirectory() as tmp:
    root=Path(tmp);c,review,journal,m,save=self.fixture(root)
    if field=='contract':c['id']='r991-renamed-wrapper'
    else:
     initial=Path(review['protected_initial_clock_file']);data=json.loads(initial.read_text());data['policy']['task_seconds']=1201;save(initial,data);m['whole_benchmark_budget']['clock_sha256']['initial']=digest(initial);save(Path(review['protected_start_marker_file']),m)
     for p in list(review['source_files_sha256']):review['source_files_sha256'][p]=digest(p)
     save(root/'WRAPPER_STOP_REVIEW.json',review)
    with self.assertRaises(ValueError):self.valid(root,c,journal)
 def test_missing_systemd_timeout_event_cannot_be_inferred_from_failed_child(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);c,review,journal,m,save=self.fixture(root)
   with self.assertRaises(ValueError):self.valid(root,c,journal[1:])

if __name__=='__main__':unittest.main()
