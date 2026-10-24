"""Portable corruption/privilege-free projection controls; no real Git or GPU."""
import copy,hashlib,json,pathlib,tempfile,unittest
from unittest.mock import patch
import leaderboard as lb

class PairedCodingProjection(unittest.TestCase):
 def fixture(self,directory):
  root=pathlib.Path(directory)/'source';stage=root/'staging/review';stage.mkdir(parents=True)
  repo=root.parent/'public-repository';(repo/'data').mkdir(parents=True)
  write=lambda p,d:p.write_text(json.dumps(d))
  exps=['R101','R102'];runs=[];profiles=[];records=[];bound={}
  for index,exp in enumerate(exps):
   s=root/'staging'/exp.lower();(s/'official-api-replay').mkdir(parents=True)
   audit=s/'AUDIT.json';write(audit,{'experiment_id':exp,'measurement_valid':True})
   stdout=s/'official-api-replay'/('official-api-'+exp.lower()+'.stdout')
   statuses=[dict(task_id='HumanEval/'+str(i),base='pass',plus='fail' if index and i==0 else 'pass') for i in range(164)]
   stdout.write_text(''.join('TASK_STATUS '+json.dumps(x)+'\n' for x in statuses))
   cfg='cfg-'+str(index+1)*64;model='model-'+str(index+1)*64
   runs.append(dict(run_id='run-'+exp,experiment_id=exp,official_eligible=True,tasks=164,solved=164-index,benchmark_identity_id='bench-shared',dataset_split_hash='split-shared',runtime_configuration_id=cfg,model_artifact_id=model,audit_hash=lb.digest(audit)))
   profiles.append(dict(runtime_configuration_id=cfg,model={'name':'Public model '+str(index)}))
   records.append(dict(experiment_id=exp,runtime_configuration_id=cfg,model_artifact_id=model,tasks=164,solved=164-index,original_audit_sha256=lb.digest(audit),admission_views=['run-'+exp],deduplicated_observations=1))
   bound.update({str(audit):lb.digest(audit),str(stdout):lb.digest(stdout)})
  history={'runs':runs,'profiles':profiles};raw=json.dumps(history).encode();h=repo/'data/configuration-history.json';h.write_bytes(raw);bound[str(h)]=hashlib.sha256(raw).hexdigest()
  code=stage/'paired_native_coding.py';code.write_text('# reviewed analysis identity; not executed\n')
  plan=stage/'PAIRED_NATIVE_CODING_PLAN.json';write(plan,{'experiments':exps,'reference':'R101'});bound[str(plan)]=lb.digest(plan)
  pair=dict(A='R101',B='R102',tasks=164,both_success=163,A_only_success=1,B_only_success=0,neither_success=0,A_successes=164,B_successes=163,net_success_change_B_minus_A=-1)
  a=dict(kind='DESCRIPTIVE_OFFICIAL_API_NATIVE164_PAIRED_REVIEW',at_utc='2026-10-24T00:00:00Z',GPU_runs=0,model_requests=0,factor_coverage_increment=0,Champion_changed=False,source_files_sha256=bound,source_code_sha256=lb.digest(code),plan_sha256=lb.digest(plan),profiles=records,reference='R101',benchmark_identity_id='bench-shared',dataset_split_hash='split-shared',all_pairs=[pair],versus_reference=[pair],private_notes='NEVER_EXPORT_PRIVATE_NOTE')
  ap=stage/'REVIEW.json';sp=stage/'SNAPSHOT.json'
  def seal():
   write(ap,a);write(sp,dict(analysis_review_sha256=lb.digest(ap),git_path='data/configuration-history.json',immutable_public_git_commit='a'*40,file_sha256=hashlib.sha256(raw).hexdigest(),mutable_source_path_at_analysis=str(h)))
   return dict(audit_path=str(ap.relative_to(root)),audit_sha256=lb.digest(ap),snapshot_path=str(sp.relative_to(root)),snapshot_sha256=lb.digest(sp))
  return root,a,raw,h,code,seal
 def project(self,root,entry,raw):
  with patch('subprocess.check_output',return_value=raw) as git:
   result=lb.paired_coding_review(root,entry,lambda p,h:'audit-'+h[:20])
   self.assertEqual(git.call_args.args[0],['git','show','a'*40+':data/configuration-history.json'])
   return result
 def test_frozen_history_survives_live_additions_and_exports_no_private_input(self):
  with tempfile.TemporaryDirectory() as d:
   root,a,raw,h,code,seal=self.fixture(d);entry=seal();h.write_text('{"new_live_history":true}')
   out=self.project(root,entry,raw);self.assertEqual(out['versus_reference'][0]['A_only_success'],1)
   encoded=json.dumps(out)
   for secret in (str(root),'NEVER_EXPORT_PRIVATE_NOTE','TASK_STATUS','source_files_sha256','mutable_source_path'):
    self.assertNotIn(secret,encoded)
   self.assertEqual(len(out['profiles']),2);self.assertFalse(out['Champion_changed']);self.assertEqual(out['GPU_runs'],0)
   self.assertEqual(len(out['task_ids']),164);self.assertTrue(all(type(x) is bool for row in out['task_pass'].values() for x in row))
   lb.validate_paired_projection(out)
   for mode in ['judgment','identity','aggregate','scope']:
    changed=copy.deepcopy(out)
    if mode=='judgment':changed['task_pass']['R102'][0]=True
    elif mode=='identity':changed['task_ids'][0]='private-task'
    elif mode=='aggregate':changed['all_pairs'][0]['A_only_success']=2
    else:changed['GPU_runs']=1
    with self.subTest(public_corruption=mode),self.assertRaises(ValueError):lb.validate_paired_projection(changed)
 def test_resigned_counts_duplicate_views_gpu_claim_and_missing_tasks_fail_closed(self):
  for mode in ['counts','duplicates','gpu','missing_tasks','code','git']:
   with self.subTest(mode=mode),tempfile.TemporaryDirectory() as d:
    root,a,raw,h,code,seal=self.fixture(d)
    if mode=='counts':a['all_pairs'][0]['B_only_success']=1
    elif mode=='duplicates':a['profiles'][0]['admission_views']*=2
    elif mode=='gpu':a['GPU_runs']=1
    elif mode=='missing_tasks':
     p=root/'staging/r101/official-api-replay/official-api-r101.stdout';p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n');a['source_files_sha256'][str(p)]=lb.digest(p)
    elif mode=='code':code.write_text('# changed analysis\n')
    entry=seal()
    if mode=='git':raw=b'{"changed":true}'
    with self.assertRaises(ValueError):self.project(root,entry,raw)

if __name__=='__main__':unittest.main()
