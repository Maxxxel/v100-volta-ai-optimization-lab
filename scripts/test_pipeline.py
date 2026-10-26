import copy
import json
import unittest
from unittest.mock import patch
import export
import pipeline


class TimingProjection(unittest.TestCase):
    def fixture(self):
        return {'schema': 1, 'GPU_jobs_started_by_this_report': 0,
                'observed_at_utc': '2026-10-25T20:00:00Z',
                'private_log': 'DO_NOT_PUBLISH',
                'current': {'experiment_id': 'R539', 'phase': 'AUDITED_RESULT_AVAILABLE', 'pid': 123},
                'experiments': [{'experiment_id': 'R538', 'source_audit_sha256': 'a'*64,
                                 'quality': {'completed': 199, 'planned': 200, 'solved': 167},
                                 'durations': {'task_phase_s': None, 'startup_total_s': 157.9, 'private': 'DO_NOT_PUBLISH'},
                                 'resources': {}, 'timestamps': {}, 'publication': {}, '_clock': {'private': 123}}]}

    def test_partial_and_missing_end_never_become_complete_or_zero(self):
        result = pipeline.project(self.fixture())
        row = result['experiments'][0]
        self.assertEqual(row['status'], 'PARTIAL')
        self.assertIsNone(row['durations']['task_phase_s'])
        self.assertEqual(row['quality']['completed'], 199)
        page = pipeline.render(result)
        self.assertIn('199/200', page)
        self.assertIn('NOT MEASURED', page)
        self.assertIn('not a live monitor', page)
        self.assertIn('not measured GPU idle time', page)

    def test_positive_allowlist_drops_private_extras(self):
        result = json.dumps(pipeline.project(self.fixture()))
        for word in ('DO_NOT_PUBLISH', '_clock', 'private_log', 'pid'):
            self.assertNotIn(word, result)

    def test_invalid_counts_and_untrusted_identity_fail_closed(self):
        for key, value in [('experiment_id', '../R1'), ('source_audit_sha256', 'bad')]:
            data = self.fixture(); data['experiments'][0][key] = value
            with self.assertRaises(AssertionError): pipeline.project(data)
        data = self.fixture(); data['experiments'][0]['quality']['solved'] = 200
        with self.assertRaises(AssertionError): pipeline.project(data)

    def test_no_arbitrary_strings_nonfinite_or_negative_measurements(self):
        for value in ('6035', -1, float('nan'), float('inf'), True):
            self.assertIsNone(pipeline.number(value))
        self.assertEqual(pipeline.number(0), 0)
        data = self.fixture(); data['current']['phase'] = 'DO_NOT_PUBLISH'
        with self.assertRaises(AssertionError): pipeline.project(data)

    def test_cpu_phases_drop_command_arguments_and_error_bodies(self):
        data = self.fixture(); data['CPU_pipeline_events'] = [
            {'experiment_id': 'R539', 'phase': 'export', 'event': 'END', 'status': 'FAILED',
             'duration_s': 1.25, 'command': 'DO_NOT_PUBLISH', 'error': 'DO_NOT_PUBLISH'},
            {'experiment_id': 'R539', 'phase': 'start_gpu', 'event': 'END', 'duration_s': 1}]
        result = pipeline.project(data)
        self.assertEqual(len(result['CPU_phases']), 1)
        self.assertEqual(result['CPU_phases'][0]['duration_s'], 1.25)
        self.assertNotIn('DO_NOT_PUBLISH', json.dumps(result))


class MtpProjection(unittest.TestCase):
    def confirmation_fixture(self):
        audit={'experiment_id':'R540','measurement_valid':True,'GPU_execution_observed':True,'completed_requests':64,'planned_requests':64,'model_starts':2,'official_benchmark':False,'winner_qualified':False,'arms':{}}
        review={'experiment_id':'R540','status':'FRESH_AB_DEVELOPMENT_SPEED_CONFIRMED_OFFICIAL_QUALIFICATION_PENDING','winner_qualified':False,'official_benchmark':False,'GPU_runs_in_review':0,'quality':{'paired_tasks':32,'paired_success_losses':0},'single_task_clock_s':120,'task_limit_s':1200,'scope':'Synthetic CPU fixture only.','next_action':'Not a real benchmark.','comparison':{},'arms':{}}
        for arm in ('A','B'):
            audit['arms'][arm]={c:{'successes':14,'completed':16,'completed_request_wall_s':1.0} for c in ('coding','tools')}
            review['arms'][arm]={'tasks':32,'coding_successes':14,'tool_successes':14,'successes':28,'response_wall_s':2.0}
        profile={'model_sha256':'a'*64,'native_mtp_draft':{'sha256':'b'*64},'runtime':'engine','assets':{'engine/llama-server':'c'*64}}
        return review,audit,profile

    def test_confirmation_is_separate_from_official_scores(self):
        review,audit,profile=self.confirmation_fixture()
        result=export.mtp_confirmation_projection(review,audit,profile)
        self.assertEqual([p['arm'] for p in result['arms']],['A','B'])
        self.assertFalse(result['official_benchmark']);self.assertFalse(result['winner_qualified'])
        self.assertNotIn('benchmark_id',result);self.assertNotIn('runtime_configuration_id',result)

    def test_confirmation_rejects_partial_coverage_and_changed_metrics(self):
        for kind in ('partial','lost','winner','time','response','subtasks'):
            review,audit,profile=self.confirmation_fixture()
            if kind=='partial':audit['completed_requests']=63
            elif kind=='lost':review['quality']['paired_success_losses']=1
            elif kind=='winner':review['winner_qualified']=True
            elif kind=='time':review['single_task_clock_s']=1201
            elif kind=='response':review['arms']['B']['response_wall_s']=1.0
            else:audit['arms']['A']['coding']['completed']=15
            with self.assertRaises(AssertionError):export.mtp_confirmation_projection(review,audit,profile)

    def test_changed_review_hash_rejected_before_load(self):
        with patch.object(export, 'digest', return_value='b'*64), patch.object(export, 'load') as load:
            with self.assertRaises(AssertionError):
                export.mtp_development_result('/synthetic', {'path': '/synthetic/review.json', 'sha256': 'a'*64}, lambda *a: None)
            load.assert_not_called()

    def test_incompatible_scope_or_qualified_claim_rejected(self):
        review = {'experiment_id': 'R539', 'baseline_experiment_id': 'R515',
                  'status': 'PROMISING_REQUIRES_FRESH_CONFIRMATION', 'single_MTP_treatment_verified': True,
                  'winner_qualified': False, 'official_benchmark': False, 'GPU_runs_in_review': 0}
        for key, value in [('winner_qualified', True), ('official_benchmark', True),
                           ('single_MTP_treatment_verified', False), ('baseline_experiment_id', 'R487')]:
            changed = copy.deepcopy(review); changed[key] = value
            with patch.object(export, 'digest', return_value='a'*64), patch.object(export, 'load', return_value=changed):
                with self.assertRaises(AssertionError):
                    export.mtp_development_result('/synthetic', {'path': '/synthetic/review.json', 'sha256': 'a'*64}, lambda *a: None)


class CodingMtpGate(unittest.TestCase):
    def fixture(self, root):
        import pathlib
        root=pathlib.Path(root)
        review={'experiment_id':'R541','GPU_runs_in_review':0,'winner_qualified':False,
                'official_benchmark_result_valid':True,'source_files_sha256':{},'profiles':{},
                'quality':{'net_success_change':-3},'comparison':{},'predeclared_quality_gate_passed':False,
                'predeclared_speed_gate_passed':True,'decision':'CODING_NONREGRESSION_GATE_FAILED_SPEED_QUALITY_TRADEOFF','scope':'CPU fixture only.'}
        for eid,solved in [('R516',134),('R541',131)]:
            folder=root/'staging'/eid.lower();folder.mkdir(parents=True)
            audit={'collected_tasks':164,'scored_tasks':164,'solved_observed_tasks':solved}
            (folder/'AUDIT.json').write_text(json.dumps(audit))
            review['profiles'][eid]={'tasks':164,'solved':solved,'response_wall_s':1.0,'task_phase_s':2.0,
                'peak_device_vram_mib':3.0,'GPU_j_per_success_lower':4.0,'GPU_j_per_success_upper':5.0}
        return root,review

    def project(self,root,review):
        path=root/'review.json';path.write_text(json.dumps(review))
        return export.verified_coding_mtp_comparison(root,{'path':str(path),'sha256':export.digest(path)},lambda *args:'audit-fixture')

    def test_valid_score_does_not_promote_failed_optimization(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root,review=self.fixture(tmp);result=self.project(root,review)
            self.assertEqual([p['solved'] for p in result['profiles']],[134,131])
            self.assertFalse(result['quality_gate_passed']);self.assertTrue(result['speed_gate_passed'])
            self.assertFalse(result['winner_qualified'])

    def test_changed_score_and_unsupported_winner_rejected(self):
        import tempfile
        for kind in ('score','winner','unqualified'):
            with tempfile.TemporaryDirectory() as tmp:
                root,review=self.fixture(tmp)
                if kind=='score':review['profiles']['R541']['solved']=134
                elif kind=='winner':review['winner_qualified']=True
                else:review['official_benchmark_result_valid']=False
                with self.assertRaises(AssertionError):self.project(root,review)

    def test_tools_category_stays_separate_and_has_exact200_denominator(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root,review=self.fixture(tmp)
            review['experiment_id']='R542';review['profiles']={('R517' if k=='R516' else 'R542'):{**v,'tasks':200} for k,v in review['profiles'].items()}
            for eid,v in review['profiles'].items():
                folder=root/'staging'/eid.lower();folder.mkdir(exist_ok=True)
                (folder/'AUDIT.json').write_text(json.dumps({'collected_tasks':200,'scored_tasks':200,'solved_observed_tasks':v['solved']}))
            path=root/'review.json';path.write_text(json.dumps(review));entry={'path':str(path),'sha256':export.digest(path)}
            result=export.verified_coding_mtp_comparison(root,entry,lambda *a:'audit-fixture',candidate='R542')
            self.assertEqual([p['experiment_id'] for p in result['profiles']],['R517','R542'])
            self.assertTrue(all(p['tasks']==200 for p in result['profiles']))
            with self.assertRaises(AssertionError):export.verified_coding_mtp_comparison(root,entry,lambda *a:'audit-fixture')

    def test_changed_original_provenance_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root,review=self.fixture(tmp);original=root/'original.json';original.write_text('{}')
            review['source_files_sha256'][str(original)]='0'*64
            with self.assertRaises(AssertionError):self.project(root,review)


class QualificationDecision(unittest.TestCase):
    def fixture(self,tmp):
        import pathlib
        root=pathlib.Path(tmp);profiles={};sources={}
        for eid,solved in [('R464',156),('R544',150)]:
            path=root/'staging'/eid.lower()/'AUDIT.json';path.parent.mkdir(parents=True)
            a={'collected_tasks':164,'solved_observed_tasks':solved,'task_phase_s':100.0,'peak_device_vram_mib':8000.0};path.write_text(json.dumps(a));sources[str(path)]=export.digest(path)
            profiles[eid]={'tasks':164,'solved':solved,'task_phase_s':100.0,'peak_device_vram_mib':8000.0}
        review={'experiment_id':'R544','candidate_audit_sha256':sources[str(root/'staging/r544/AUDIT.json')],
            'winner_qualified':False,'GPU_runs':0,'model_requests':0,'source_files_sha256':sources,'profiles':profiles,
            'decision':'QUALITY_GATE_FAILED','scope':'CPU fixture only, execution policies differ.',
            'predeclared_gates':{'quality':False},'comparison_class':'STORED_CONTROL_PROFILE_COMPARISON'}
        return root,review
    def project(self,root,review):
        path=root/'staging/r544/REVIEW.json';path.write_text(json.dumps(review))
        return export.verified_qualification_review(root,{'experiment_id':'R544','audit_sha256':export.digest(root/'staging/r544/AUDIT.json'),'qualification_review_path':str(path),'qualification_review_sha256':export.digest(path)},lambda *a:'audit-fixture')
    def test_failure_and_profile_comparison_are_preserved(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root,review=self.fixture(tmp);result=self.project(root,review)
            self.assertEqual(result['decision'],'QUALITY_GATE_FAILED');self.assertFalse(result['gates']['quality']);self.assertEqual(result['comparison_class'],'STORED_CONTROL_PROFILE_COMPARISON')
    def test_forged_score_resource_time_and_champion_rejected(self):
        import tempfile
        for key,value in [('solved',156),('tasks',200),('task_phase_s',1.0),('peak_device_vram_mib',1.0),('winner',True),('audit','0'*64)]:
            with tempfile.TemporaryDirectory() as tmp:
                root,review=self.fixture(tmp)
                if key=='winner':review['winner_qualified']=value
                elif key=='audit':review['candidate_audit_sha256']=value
                else:review['profiles']['R544'][key]=value
                with self.subTest(key=key),self.assertRaises(AssertionError):self.project(root,review)

    def test_development_counts_are_verified_without_official_promotion(self):
        import tempfile
        for mutation in (None,'duplicate','group_score','official','incomplete'):
            with tempfile.TemporaryDirectory() as tmp:
                root,review=self.fixture(tmp)
                for eid,profile in review['profiles'].items():
                    tasks=[{'id':str(i),'success':i<28} for i in range(32)]
                    a={'status':'OPTIMIZATION_DEVELOPMENT_COMPLETE','official_benchmark':False,'winner_qualified':False,
                       'completed_requests':32,'planned_requests':32,'scored_tasks':tasks,
                       'groups':{'coding':{'completed':16,'successes':14},'tools':{'completed':16,'successes':14}},
                       'task_phase_s':100.0,'peak_device_vram_mib':8000.0}
                    if eid=='R544':
                        if mutation=='duplicate':tasks[-1]['id']='0'
                        elif mutation=='group_score':a['groups']['coding']['successes']=15
                        elif mutation=='official':a['official_benchmark']=True
                        elif mutation=='incomplete':a['completed_requests']=31
                    path=root/'staging'/eid.lower()/'AUDIT.json';path.write_text(json.dumps(a))
                    review['source_files_sha256'][str(path)]=export.digest(path)
                    profile.update(tasks=32,solved=28)
                review['candidate_audit_sha256']=export.digest(root/'staging/r544/AUDIT.json')
                if mutation is None:self.assertEqual(self.project(root,review)['decision'],'QUALITY_GATE_FAILED')
                else:
                    with self.subTest(mutation=mutation),self.assertRaises(AssertionError):self.project(root,review)


class RoleRetrospective(unittest.TestCase):
    def fixture(self):
        identity={'kind':'input_identity','id':'turn-private','case_id':'private-case','source_case_id':'DO_NOT_PUBLISH','arm':'single','prompt_token_count':3}
        turn={'kind':'agent_turn','id':'turn-private','start_ns':1100000000,'end_ns':1900000000,'reply':{'content':'DO_NOT_PUBLISH','usage':{'prompt_tokens':3,'completion_tokens':4}}}
        case={'kind':'orchestration_case','id':'private-case','source_case_id':'DO_NOT_PUBLISH','arm':'single','start_ns':1000000000,'end_ns':2000000000,'e2e_s':1.0,'attempted_requests':1,'role_calls':{'worker':1,'planner':0,'reviewer':0},'simulator_callbacks':1,'reported_result':{'task_success':False,'policy_gate_pass':False}}
        telemetry=[{'at_ns':i*500000000,'nvml_begin_ns':i*500000000,'gpu_energy_counter_mj':i*500} for i in range(6)]
        return [identity,turn,case],telemetry
    def test_measured_failure_costs_and_token_counts_are_retained_without_private_text(self):
        records,telemetry=self.fixture();d=export.role_case_costs(records,telemetry);row=d['rows'][0]
        self.assertEqual(row['reported_prompt_tokens'],3);self.assertEqual(row['completion_tokens'],4);self.assertFalse(row['success']);self.assertEqual(row['GPU_j_lower'],1.0);self.assertEqual(row['GPU_j_upper'],1.0)
        self.assertNotIn('DO_NOT_PUBLISH',json.dumps(d));self.assertIn('separate preamble tokens per step',d['not_measured']);self.assertEqual(d['new_GPU_runs'],0)
    def test_missing_usage_stays_unknown_not_zero(self):
        records,telemetry=self.fixture();records[1]['reply']['usage'].pop('prompt_tokens')
        row=export.role_case_costs(records,telemetry)['rows'][0];self.assertIsNone(row['reported_prompt_tokens']);self.assertEqual(row['recorded_input_token_count'],3)
    def test_duplicate_callbacks_missing_identity_and_wrong_scope_fail_closed(self):
        for kind in ('duplicate','identity','arm','time'):
            records,telemetry=self.fixture()
            if kind=='duplicate':records.append(copy.deepcopy(records[1]))
            elif kind=='identity':records.pop(0)
            elif kind=='arm':records[-1]['arm']='DO_NOT_PUBLISH'
            else:records[-1]['e2e_s']=2.0
            with self.subTest(kind=kind),self.assertRaises(AssertionError):export.role_case_costs(records,telemetry)


if __name__ == '__main__': unittest.main()
