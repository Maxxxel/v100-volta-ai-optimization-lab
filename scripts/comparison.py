"""Audited, allowlisted benchmark projection and offline SVG charts.
No GPU access. Counts and costs come from pinned audits, never chart literals.
"""
import hashlib, html, json, math, pathlib, re, statistics
MODELS = {'omni':('OmniCoder2 9B','Q6_K'), 'q35':('Qwen3.5 9B','Q4_K_M'), 'q38':('Qwen3.8 27B','GSQ/RCO IQ3_S'), 'ornith':('Ornith 1.5 9B','Q6_K'), 'bonsai':('Ternary Bonsai 2 27B','PQ2_0'), 'oxcoder':('OxCoder 9B','Q6_K')}
def model_entries(models):
    order=[k for k in MODELS if k in models]+sorted(set(models)-set(MODELS))
    return [{'id':k,'name':models[k][0],'quantization':models[k][1]} for k in order]
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(pathlib.Path(p).read_text())
def finite(x):return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def ratio(a,b):return a/b if finite(a) and finite(b) and b>0 else None
def fingerprint(x):return hashlib.sha256(json.dumps(x,sort_keys=True,allow_nan=False,separators=(',',':')).encode()).hexdigest()
def check(data):
    if 'measurement_fingerprint' in data and data['measurement_fingerprint']!=fingerprint({k:v for k,v in data.items() if k!='measurement_fingerprint'}):raise ValueError('Comparison measurement fingerprint mismatch')
    ids=set()
    for row in data['records']:
        if row['id'] in ids:raise ValueError('Duplicate comparison record')
        ids.add(row['id']);n=row['tasks'];s=row['solved']
        if not (type(n) is int and n>0 and type(s) is int and 0<=s<=n):raise ValueError('Invalid benchmark denominator')
        if row['task_sha256']!=data['cohorts'][row['discipline']]['task_sha256']:raise ValueError('Incompatible task identity in comparison cohort')
        expected_n=data['cohorts'][row['discipline']].get('task_count')
        if expected_n is not None and n!=expected_n:raise ValueError('Incompatible cohort task count')
        if not row['audit_ids'] or not all(re.fullmatch('[a-f0-9]{64}',h) for h in row['audit_sha256']):raise ValueError('Missing pinned audit')
        for k in ('wall_s','gpu_j','peak_vram_mib'):
            if row[k] is not None and (not finite(row[k]) or row[k]<0):raise ValueError('Invalid or nonfinite cost')
    return True

def build(root, db, matrix, receipt):
    root=pathlib.Path(root);summary=db['summary'];rows=[]
    registry=summary['model_comparison_chart_registry'];models=registry.get('models',MODELS)
    def audit(path,expected):
        p=pathlib.Path(path);p=p if p.is_absolute() else root/p
        if not expected or sha(p)!=expected:raise ValueError('Comparison audit pin mismatch')
        ident=receipt(p,expected)
        if not ident:raise ValueError('Comparison audit outside export contract')
        return load(p),p,ident
    def source(n):
        x=summary['r'+str(n)];return audit(x['audit_path'],x['audit_sha256'])
    def meta(plan_n, a, path):
        pth=root/f'staging/r{plan_n}/PLAN.json';p=load(pth)
        hp=path.parent/'HOST_PRECHECK.json';expected=(load(hp).get('plan_sha256') if hp.is_file() else None) or a.get('evidence',{}).get(str(pth.relative_to(root)))
        if expected and sha(pth)!=expected:raise ValueError('Comparison plan pin mismatch')
        argv=p.get('launch',{}).get('argv',[]);ident=p.get('runtime_identities',p.get('identities',{}));flags={}
        for flag in ('--ctx-size','--batch-size','--ubatch-size','--threads','--cache-type-k','--cache-type-v','--spec-type','--spec-draft-n-max','--reasoning'):
            if flag in argv and argv.index(flag)+1<len(argv):
                v=str(argv[argv.index(flag)+1])
                if re.fullmatch('[A-Za-z0-9_.+-]{1,40}',v):flags[flag]=v
        fixed=p.get('fixed',{});runtime={k:v for k,v in fixed.items() if k in ('ctx','slots','threads','temperature','seed','cache_prompt','thinking','batch_size','ubatch_size') and isinstance(v,(int,float,bool))}
        sampler=p.get('source_sampling') or p.get('coding_sampling') or {'temperature':fixed.get('temperature',0),'seed':fixed.get('seed',1001)}
        sampler={k:v for k,v in sampler.items() if k in ('temperature','top_p','top_k','min_p','presence_penalty','repeat_penalty','seed') and finite(v)}
        if finite(p.get('seed')):sampler.setdefault('seed',p['seed'])
        model_hash=p.get('model_sha256') or (p.get('profiles',[{}])[0].get('model_sha256') if p.get('profiles') else None)
        if not model_hash:
            hashes=[v for k,v in ident.items() if k.endswith('.gguf') and 'MTP-ONLY' not in k];model_hash=hashes[0] if len(hashes)==1 else None
        return p,{'engine':'llama.cpp / CUDA 12.8 / SM70 (exact audited binary below)','engine_binary_sha256':next((v for k,v in ident.items() if k.endswith('/llama-server')),None),'plan_sha256':sha(pth),'model_sha256':model_hash,'template_sha256':p.get('template_sha256') or (p.get('profiles',[{}])[0].get('template_sha256') if p.get('profiles') else None) or (ident.get(argv[argv.index('--chat-template-file')+1]) if '--chat-template-file' in argv else None),'process_peak_vram_mib':a.get('session',{}).get('peak_process_vram_mib'),'date':str(a.get('at_utc') or p.get('created_at_utc') or '')[:10] or 'NOT RECORDED','hardware':'Tesla V100-SXM2 16 GB HBM2','power_limit_w':p.get('power_limit_w',300 if plan_n==183 else None),'context_and_runtime':flags or runtime,'sampling':sampler,'scorer_adapter_sha256':p.get('judge_source_sha256'),'official_evalplus_provenance_sha256':p.get('judge_inputs_sha256',{}).get('EVALPLUS_PROVENANCE.json'),'cache_condition':'Warm model; per-request KV reset; OS file cache uncontrolled; model startup excluded','output_cap':p.get('maximum_output_tokens') or p.get('functional_workload',{}).get('max_output_tokens') or p.get('native_bfcl_workload',{}).get('max_output_tokens') or p.get('agent_workload',{}).get('max_output_tokens')}
    task_hashes={
        'coding':load(root/'staging/r217/PLAN.json')['functional_workload']['tasks_sha256'],
        'tools':load(root/'staging/r183/PLAN.json')['native_bfcl_workload']['tasks_sha256'],
        'agents':load(root/'staging/r219/PLAN.json')['agent_workload']['tasks_sha256']}
    def add(model,discipline,n,solved,wall,j,peak,ap,plan_n,a,aid,label,task_hash,spread=None,warning=None,extra_ids=None,extra_hashes=None):
        p,metadata=meta(plan_n,a,ap)
        if discipline=='agents':
            retained=p.get('agent_workload',{}).get('retain_prefix',False)
            metadata['context_and_runtime']['retain_prefix']=retained
            if retained:metadata['cache_condition']='Warm model; firstturn resets eachcase, laterturns retainprefix in one slot; OSfilecache uncontrolled, startup/warmupexcluded'
        row={'id':f'{model}-{discipline}-{plan_n}','model':model,'name':models[model][0],'quantization':models[model][1],'profile':label,'discipline':discipline,'tasks':n,'solved':solved,'wall_s':wall,'gpu_j':j,'peak_vram_mib':peak,'task_sha256':task_hash,'metadata':metadata,'audit_ids':[aid]+(extra_ids or []),'audit_sha256':[sha(ap)]+(extra_hashes or []),'experiment':a.get('experiment_id','R'+str(plan_n)),'repeat_range':spread,'warning':warning,'evidence_class':'LOCALLY MEASURED','comparability':'SAME_FROZEN_TASKS_AND_SCORING_WHOLE_CONFIGURATIONS'}
        rows.append(row)
    for model,n in registry['coding']:
        a,ap,aid=source(n);p=load(root/f'staging/r{n}/PLAN.json');sc=a['scopes']['standard_full164'];assert sc['tasks']==164 and a.get('measurement_valid',True)
        add(model,'coding',sc['tasks'],sc['solved'],sc['wall_s'],sc.get('gpu_energy_j_approx',sc.get('gpu_energy_j')),a.get('peak_device_vram_mib'),ap,n,a,aid,'MTP + weight cache; fast' if model=='omni' else 'Fast non-reasoning',p['functional_workload']['tasks_sha256'])
    for n in registry['classic_q38_coding']:
        a,ap,aid=source(n);p=load(root/f'staging/r{n}/PLAN.json');sc=a['scopes']['standard_full164'];assert sc['tasks']==164
        add('q38','coding',164,sc['solved'],sc['wall_s'],sc['gpu_energy_j'],a.get('peak_device_vram_mib'),ap,n,a,aid,'Fast; '+('MTP3' if n==118 else 'no MTP'),p['functional_workload']['tasks_sha256'],warning='MTP target-token identity is not lossless; no allround qualification' if n==118 else None)
    for model,n in registry['tools']:
        a,ap,aid=source(n);p=load(root/f'staging/r{n}/PLAN.json');sc=a['scopes']['overall'] if n==183 else {'tasks':a['observed_cases'],'solved':a['full_100_score'],'wall_s':a['wall_s'],'gpu_energy_j':a['gpu_energy_j_approx']};assert sc['tasks']==100
        if n==183:th=p['native_bfcl_workload']['tasks_sha256']
        else:
            inputs=root/f'staging/r{n}/INPUTS.json';original=root/'staging/r135/BFCL_TASKS.json'
            if sha(inputs)!=p['ct_files_sha256']['INPUTS.json'] or load(inputs)['tasks']!=load(original)['tasks']:raise ValueError('Tool cohort questions/schema changed')
            th=sha(original)
        add(model,'tools',100,sc['solved'],sc['wall_s'],sc['gpu_energy_j'],a.get('peak_device_vram_mib'),ap,n,a,aid,'MTP; fast' if model=='omni' else 'Fast non-reasoning',th)
    for model,n in registry['agents']:
        a,ap,aid=source(n);p=load(root/f'staging/r{n}/PLAN.json');assert a['full18_score_claimed'] and a['observed_tasks']==18
        warning='Additional policy violations observed; no assistant qualification' if a.get('additional_policy_violations') else None
        add(model,'agents',18,a['solved'],a['total_task_wall_s'],a['gpu_energy_j_approx'],a['peak_device_vram_mib'],ap,n,a,aid,('Thinking medium; prefix reuse; local2048; confirmation' if p['agent_workload'].get('retain_prefix') else 'Thinking medium; local2048; independent repeat') if model=='bonsai' else 'Fast non-reasoning; no MTP',p['agent_workload']['tasks_sha256'],warning=warning)
        if model=='bonsai':
            if p['agent_workload']['max_output_tokens']!=2048:raise ValueError('Bonsai agent repeat budget changed')
            rows[-1]['metadata']['measurement_batches']=f'R{n}:one full18-case prefixcandidate confirmation; no independentChampion fromfirst3screen' if p['agent_workload'].get('retain_prefix') else f'R{n}:one fresh18-case repeat of the same development tasks; not a newholdout or36independent tasks'
    a,ap,aid=source(261);p=load(root/'staging/r261/PLAN.json');assert a['full18_score_claimed'] and a['observed_tasks']==18
    add('q38','agents',18,a['solved'],a['total_task_wall_s'],a['gpu_energy_j_approx'],a['peak_device_vram_mib'],ap,261,a,aid,'Fast; MTP3',p['agent_workload']['tasks_sha256'],warning='Additional policy failure inherited; coding-specialist screen, no general assistant qualification')
    a,ap,aid=source(219);cycles=a['cycle_metrics'];q=summary['r220']['qualified_candidate'];assert len(cycles)==3 and all(x['solved']==q['metrics']['solved'] for x in cycles)
    qual=summary['r220'];_,_,qid=audit(qual['audit_path'],qual['audit_sha256']);p=load(root/'staging/r219/PLAN.json')
    spread={'cycles':3,'distinct_tasks':18,'wall_s':[min(x['total_wall_s'] for x in cycles),max(x['total_wall_s'] for x in cycles)],'gpu_j_per_success':[min(x['gpu_j_per_success'] for x in cycles),max(x['gpu_j_per_success'] for x in cycles)],'definition':'Observed min–max of three repeated 18-case cycle aggregates; not 54 independent tasks.'}
    add('omni','agents',18,q['metrics']['solved'],q['metrics']['total_wall_s'],q['metrics']['gpu_energy_j'],q['peak_device_vram_mib'],ap,219,a,aid,'MTP + weight cache; 300 W',p['agent_workload']['tasks_sha256'],spread=spread,extra_ids=[qid],extra_hashes=[qual['audit_sha256']])
    bonsai=next(x for x in matrix['model_challengers'] if x['id']=='BMC04')
    for dis,key,plan_n in [('coding','full_coding_evidence',271),('tools','full_tool_evidence',280),('agents','full_agent_evidence',286)]:
        ref=bonsai[key];a,ap,aid=audit(ref['path'],ref['sha256']);ids=[];hashes=[];parts=[]
        for ref in a['source_audits']:
            child,cp,ci=audit(ref['audit_path'],ref['audit_sha256']);ids.append(ci);hashes.append(ref['audit_sha256']);parts.append(child)
            pn=int(ref['experiment_id'][1:]);pp=root/f'staging/r{pn}/PLAN.json'
            if ref.get('plan_sha256') and sha(pp)!=ref['plan_sha256']:raise ValueError('Campaign plan mismatch')
        m=a.get('metrics',{})
        if dis=='coding':
            sc=a['scopes']['standard_full164'];assert sc['tasks']==164 and a['all180_official_base_AND_plus_recounted'];partrows=[x for child in parts for x in child.get('per_task',[]) if x.get('suite')=='standard'];assert len(partrows)==164 and sum(x['success'] for x in partrows)==sc['solved'];wall=sum(x['e2e_s'] for x in partrows);j=sum(x['gpu_energy_j_approx'] for x in partrows);n=164;solved=sc['solved'];peak=m['peak_device_vram_mib'];th=a['source_task_sha256']
        elif dis=='tools':n=m['observed_cases'];solved=m['solved'];wall=m['case_inference_wall_s'];j=m['case_GPU_energy_J_approx'];peak=m['peak_device_vram_mib'];th=a['source_tasks_sha256'];assert n==100
        else:n=a['observed_unique_cases'];solved=a['solved'];wall=a['total_case_wall_s'];j=a['GPU_energy_J_approx'];peak=a['peak_device_vram_mib'];th=a['source_tasks_sha256'];assert n==18
        add('bonsai',dis,n,solved,wall,j,peak,ap,plan_n,a,aid,'Thinking medium; '+('2048 output' if dis=='agents' else '4096 output'),th,extra_ids=ids,extra_hashes=hashes)
        if dis=='agents':
            executed=[load(root/f"staging/r{int(ref['experiment_id'][1:])}/PLAN.json") for ref in a['source_audits']]
            if any(plan['agent_workload']['max_output_tokens']!=2048 for plan in executed):raise ValueError('Bonsai agent campaign output budgets differ')
            rows[-1]['metadata']['measurement_batches']='R285:16 + R286:2 disjoint agent cases; R284 failed before agent generation and is excluded'
            rows[-1]['metadata']['output_cap']=2048
    mbpp_hash=None
    for model,n,parent_n in registry.get('mbpp223',[]):
        ref=summary['r'+str(n)];a,ap,aid=source(n);campaign,cp,cid=audit(ref['campaign_path'],ref['campaign_sha256']);review,rp,rid=audit(ref['independent_review_path'],ref['independent_review_sha256'])
        if not a['measurement_valid'] or review['exact_requests_token_counts_and_official_scores_verified']!=191:raise ValueError('MBPP new batch not fully audited')
        plan=load(root/f'staging/r{n}/PLAN.json');parent=load(root/f'staging/r{parent_n}/PLAN.json')
        if sha(root/f'staging/r{parent_n}/PLAN.json')!=plan['parent_original32_plan_sha256']:raise ValueError('MBPP parent plan changed')
        def normalized_launch(x):
            x=json.loads(json.dumps(x));v=x['argv'];v[v.index('--chat-template-file')+1]='PINNED_TEMPLATE';return x
        if any(plan[k]!=parent[k] for k in ('model_sha256','template_sha256','runtime_identities','source_sampling','maximum_output_tokens')) or normalized_launch(plan['launch'])!=normalized_launch(parent['launch']):raise ValueError('MBPP profile drift across batches')
        parts=[];extra_ids=[cid,rid];extra_hashes=[sha(cp),sha(rp)]
        for src in campaign['source_audits']:
            part,path,ident=audit(src['path'],src['sha256']);parts.extend(part['per_task']);extra_ids.append(ident);extra_hashes.append(src['sha256'])
        tasks=load(root/f'staging/r{parent_n}/TASKS.json')+load(root/f'staging/r{n}/TASKS.json')
        ids=[x['task_id'] for x in parts]
        if len(parts)!=223 or len(set(ids))!=223 or 'Mbpp/255' in ids or ids!=[x['task_id'] for x in tasks] or parts!=campaign['per_task']:raise ValueError('MBPP campaign task mismatch')
        if campaign['tasks']!=223 or campaign['full224_score'] or campaign['full378_score'] or campaign['solved']!=sum(x['success'] for x in parts):raise ValueError('MBPP denominator/score mismatch')
        for field,task_field in [('wall_s','e2e_s'),('gpu_energy_j','gpu_energy_j')]:
            if not math.isclose(campaign[field],sum(x[task_field] for x in parts),rel_tol=1e-10):raise ValueError('MBPP campaign costs mismatch')
        th=fingerprint({'dataset':plan['dataset_sha256'],'tasks':tasks,'score':'base AND plus','judge':plan['host_inputs_sha256'][str(root/'staging/model-comparison-preparation/mbppplus-v020/mbpp_evaluate.py')],'admission':plan['judge_admission_sha256']})
        if mbpp_hash is not None and th!=mbpp_hash:raise ValueError('MBPP model cohorts differ')
        mbpp_hash=th
        add(model,'mbpp',223,campaign['solved'],campaign['wall_s'],campaign['gpu_energy_j'],campaign['peak_device_vram_mib'],ap,n,a,aid,{'omni':'Original Q6; no MTP or weight cache','q38':'IQ3_S grafted MTP3; coding profile','gemma4':'Official QAT Q4_0; native fast; no MTP or weight cache'}.get(model,'Native coding profile; see measured conditions'),th,extra_ids=extra_ids,extra_hashes=extra_hashes,warning='Known native-tool/policy limitations remain; coding only, no allround or lossless claim.' if model=='q38' else ('Native-tool84/100 and agent9/18 with additional policy faults retained; coding results do not qualify an assistant.' if model=='gemma4' else None))
        rows[-1]['metadata']['scorer_adapter_sha256']=plan['host_inputs_sha256'][str(root/'staging/model-comparison-preparation/mbppplus-v020/mbpp_evaluate.py')]
        rows[-1]['metadata']['measurement_batches']=f'R{parent_n}:32 + R{n}:191, disjoint tasks; no repeats'
        rows[-1]['metadata']['chat_template_kwargs']={'enable_thinking':False}
    for discipline,specs in registry.get('native_long_context',{}).items():
        if discipline not in ('long16k','long32k_validation'):raise ValueError('Unknown long-context cohort')
        for model,n in specs:
            a,ap,aid=source(n);p=load(root/f'staging/r{n}/PLAN.json');ref=summary['r'+str(n)]
            if not a['measurement_valid'] or not a['full_12_semantic_score_claimed'] or a['observed_cases']!=12:raise ValueError('Partial context result cannot enter full12 chart')
            review,rp,rid=audit(ref['independent_review_path'],ref['independent_review_sha256'])
            count=review.get('long_native_exact_argument_scores_recomputed') if discipline=='long16k' else review.get('native_input_counts_source_sampler_and_scores_verified')
            if count!=12:raise ValueError('Context scores not independently audited')
            fixture='LONG_INPUTS.json' if discipline=='long16k' else 'VALIDATION_INPUTS.json';taskfile='LONG_CONTEXT_TASKS.json' if discipline=='long16k' else 'VALIDATION_TASKS.json';stage=root/f'staging/r{n}'
            if sha(stage/fixture)!=p['ct_files_sha256'][fixture] or sha(stage/taskfile)!=p['ct_files_sha256'][taskfile]:raise ValueError('Context fixture identity changed')
            inputs=load(stage/fixture);tasks=load(stage/taskfile);tasks=tasks['tasks'] if isinstance(tasks,dict) else tasks;parts=a['per_task']
            if len(inputs)!=12 or len(tasks)!=12 or len(parts)!=12:raise ValueError('Context denominator changed')
            descriptor=[]
            for item,task,part in zip(inputs,tasks,parts):
                if item['id']!=task['id'] or item['id']!=part['id'] or item['request']['max_tokens']!=256:raise ValueError('Context case order/output cap mismatch')
                descriptor.append({'id':item['id'],'messages':item['request']['messages'],'tools':item['request']['tools'],'tool_choice':item['request']['tool_choice'],'parallel_tool_calls':item['request']['parallel_tool_calls'],'expected_arguments':task['expected_arguments']})
            if a['solved']!=sum(x['score']['success'] for x in parts) or not math.isclose(a['wall_s'],sum(x['wall_s'] for x in parts),rel_tol=1e-10) or not math.isclose(a['gpu_energy_j_approx'],sum(x['gpu_energy_j_approx'] for x in parts),rel_tol=1e-10):raise ValueError('Context aggregate mismatch')
            expected_context=16384 if discipline=='long16k' else 32768
            if a['context_tokens']!=expected_context:raise ValueError('Context allocation cohort changed')
            th=fingerprint({'tasks':descriptor,'scorer_function_sha256':p['scorer_function_sha256'],'output_cap':256})
            if discipline in task_hashes and task_hashes[discipline]!=th:raise ValueError('Long-context questions/oracles/scorer differ')
            task_hashes[discipline]=th
            label=('Native fast; '+('T1' if model=='gemma4' else 'T0')+'; no MTP; '+str(expected_context//1024)+'K')
            add(model,discipline,12,a['solved'],a['wall_s'],a['gpu_energy_j_approx'],a['peak_device_vram_mib'],ap,n,a,aid,label,th,warning='Separate agent-policy failures remain; this is read-only synthetic inventory retrieval, not agent or assistant qualification.',extra_ids=[rid],extra_hashes=[ref['independent_review_sha256']])
            rows[-1]['metadata']['actual_input_token_range']=[min(x['actual_input_tokens'] for x in parts),max(x['actual_input_tokens'] for x in parts)]
            rows[-1]['metadata']['scorer_adapter_sha256']=p['scorer_function_sha256'];rows[-1]['metadata']['chat_template_kwargs']={'enable_thinking':False}
    historical=[]
    audit135=summary['r135'];_,_,aid135=audit(audit135['audit_path'],audit135['audit_sha256'])
    for key,model in [('omnicoder2','omni'),('qwen35','q35'),('qwen38','q38')]:
        rid=db['profiles']['o2-original12-synthetic-v1/'+key]['A0'];rec=db['records'][rid];ident=rec['identity'];ms=[]
        # The immutable reference's evidence includes the original measurement archive hashes.
        for k in ['prefill','prefill2048','prefill4096','decode']:
            m=rec['metrics'][k];obs=m['observations'];assert obs and finite(m['median']) and finite(m['mad'])
            ms.append({'workload':k,'median':m['median'],'mad':m['mad'],'n':len(obs),'sessions':m['sessions'],'unit':'tokens/s','actual_prompt_tokens':sorted(set(x['prompt_n'] for x in obs)),'generated_tokens':sorted(set(x['predicted_n'] for x in obs))})
        historical.append({'model':model,'name':models[model][0],'quantization':models[model][1],'record_id':rid,'audit_ids':[aid135],'audit_sha256':[audit135['audit_sha256']],'reference_identity_sha256':fingerprint(ident),'model_sha256':ident['model']['model_sha256'],'engine_binary_sha256':sorted(set(re.findall('[a-f0-9]{64}',json.dumps(ident.get('binary_sha256'))))),'date':'NOT RECORDED in imported reference identity; audited in R135','power_limit_w':ident.get('power_limit_w'),'hardware':'Tesla V100-SXM2 16 GB HBM2','conditions':{k:v for k,v in ident['runtime'].items() if isinstance(v,(int,float,bool))},'metrics':ms,'comparability':'HISTORICAL_SYNTHETIC_ONLY','note':'Different tokenizers and historical model/build identities. Not a current task-success ranking; no cross-tokenizer quality or useful-throughput inference.'})
    cohorts={d:{'task_sha256':h,'definition':{'coding':'HumanEvalPlus frozen 164; base AND plus; HumanEval/32 known invalid retained as failure (163 subset is separate).','tools':'Frozen balanced native-tool subset: 100 cases, 20 in each of five categories; official AST plus irrelevance rules; not full BFCL leaderboard.','agents':'Frozen 18 development agent tasks with unchanged effect/policy simulator; all tools isolated; not a new holdout.','long16k':'Twelve identical frozen long-inventory texts and typed native-call oracles; context16384, output256. Same requests/scoring with own native model templates/tokenizers and T0 versus T1 sampling. Original Omni16K partial R339 is excluded from full12 bars; Omni32K R338 remains a separate context/protocol evidence record. No full BFCL or agent claim.','long32k_validation':'Twelve identical subsequent local validation inventories frozen in R431 before Qwen screen outputs; context32768, output256, actualnative inputs above16384. Same texts/tools/oracles; own native tokenizers and T0 versus T1. Not a model-training holdout or population-accuracy claim. Partial runs remain on experiment pages and never become full12 scores.'}[d]} for d,h in task_hashes.items()}
    if mbpp_hash is not None:cohorts['mbpp']={'task_sha256':mbpp_hash,'task_count':223,'definition':'MBPP+ v0.2.0 original-test release pool: 223/224 tasks admitted before new model outputs; Mbpp/255 official canonical solution exceeds sandbox memory and is separately DEFERRED. Original32 + disjoint191, one answer per task, base AND plus. Not full224 or full378 leaderboard; separate from HumanEval and no proof of training exclusion.'}
    data={'schema':1,'models':model_entries(models),'cohorts':cohorts,'records':rows,'historical_native':historical,'rules':['No combined score. Counts are one observed answer per task unless repeated cycles are explicitly stated.','Whole configurations: model, tokenizer, native template, output budget, sampling, quantization and engine can differ. Task/scorer matching permits comparison of these profiles, not causal architecture claims.','GPU board energy includes failed task attempts; excludes load/warmup and CPU/system energy. Latency is measured request/case time; startup and judge time are excluded.','NOT MEASURED means no full comparable audited result in this cohort. Partial screens are not converted into full-suite scores.']}
    check(data);data['measurement_fingerprint']=fingerprint(data);return data

def svg(title,unit,values,maximum=None):
    """Compact responsive, self-contained SVG with no script or network references."""
    w=420;h=85+len(values)*96;maximum=maximum or max([x['value'] or 0 for x in values]+[1])*1.15
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(title)}. Units: {html.escape(unit)}. Missing observations are labelled NOT MEASURED. Whiskers follow the stated observed min-max or median-absolute-deviation definition, never an inferred confidence interval.</desc><rect width="420" height="{h}" rx="14" fill="#10232d"/><g font-family="system-ui,sans-serif" fill="#e8f3f5"><text x="18" y="29" font-size="16" font-weight="700">{html.escape(title)}</text>']
    for i,row in enumerate(values):
        y=61+i*96;label=html.escape(row['label']);v=row['value'];out.append(f'<text x="18" y="{y}" font-size="13">{label}</text>')
        if row.get('subtitle'):out.append(f'<text x="18" y="{y+17}" font-size="11" fill="#b6c6cf">{html.escape(row["subtitle"])}</text>')
        if v is None:out.append(f'<text x="18" y="{y+47}" fill="#b6c6cf" font-size="13">NOT MEASURED</text>');continue
        length=max(0,min(380,v/maximum*380));color='#f0b774' if row.get('warning') else '#51d8bc';out.append(f'<rect x="18" y="{y+28}" width="380" height="10" rx="5" fill="#24404a"/><rect x="18" y="{y+28}" width="{length:.3f}" height="10" rx="5" fill="{color}"/>')
        if row.get('range'):
            lo,hi=row['range'];x1=18+lo/maximum*380;x2=18+hi/maximum*380;out.append(f'<path d="M{x1:.3f} {y+23}v20 M{x1:.3f} {y+33}H{x2:.3f} M{x2:.3f} {y+23}v20" stroke="#fff" stroke-width="1.5"/>')
        text=row.get('display') or f'{v:,.2f} {unit}';out.append(f'<text x="18" y="{y+58}" font-size="13" fill="{color}">{html.escape(text)}</text>')
    return ''.join(out)+'</g></svg>\n'

def render(data,docs):
    docs=pathlib.Path(docs);dest=docs/'assets/benchmarks';dest.mkdir(parents=True,exist_ok=True)
    def write(p,text):
        if not p.exists() or p.read_text()!=text:p.write_text(text)
    def cell(x):return str(x if x is not None else 'NOT MEASURED').replace('|','\\|').replace('\n',' ')
    def table(headers,rs):return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(cell(x) for x in row)+' |\n' for row in rs)+'\n'
    page='# Model Comparison & Benchmarks\n\n<div class="hero"><strong>Measured tasks. Visible trade-offs.</strong><p>Separate coding, native tools and agent results on one V100. No combined score and no automatic winner.</p></div>\n\n'
    page+='\n'.join('- '+x for x in data['rules'])+'\n\nTeal bars are measured values; amber identifies a recorded policy warning. NOT MEASURED is never plotted as zero. The tables below each cohort provide exact profile metadata and original audit hashes. Error bars are omitted for single runs; repeated-cycle min–max and historical median absolute deviation (MAD) are labelled explicitly.\n\n'
    page+='Measurement-only fingerprint: `'+data['measurement_fingerprint']+'`. Charts change when these audited measurements/conditions change, independently of matrix revision. New full-suite results are admitted through the existing canonical benchmark reference registry after audit; changed task identities fail the cohort gate rather than silently entering a ranking. Download the [validated aggregate dataset](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/comparison.json).\n\n'
    disciplines=[('coding','Coding · HumanEvalPlus')]+([('mbpp','Coding · MBPP+ admitted 223')] if 'mbpp' in data['cohorts'] else [])+[('tools','Native Tools · balanced 100'),('agents','Agents · isolated 18')]+[(key,title) for key,title in [('long16k','Long inventory · 16K profiles'),('long32k_validation','Long inventory · new 32K validation')] if key in data['cohorts']]
    for dis,title in disciplines:
        rows=[x for x in data['records'] if x['discipline']==dis];by={x['model']:x for x in rows};page+='## '+title+'\n\n'+data['cohorts'][dis]['definition']+'\n\nTask identity: `'+data['cohorts'][dis]['task_sha256']+'`. **Task-matched whole-configuration comparisons**; native sampling, budgets and builds are shown below. These are development results, with no repeated-seed model-superiority claim. Record dates come from the original audit or frozen plan; missing dates remain labelled.\n\n'
        for metric,heading,unit in [('success','Successful tasks','%'),('latency','Mean task E2E','s / task'),('energy','GPU energy per success','J / success'),('vram','Peak device VRAM','MiB')]:
            vals=[]
            for model in data['models']:
                for r in [x for x in rows if x['model']==model['id']] or [None]:
                    v=None;ran=None;display=None
                    if r:
                        if metric=='success':v=r['solved']/r['tasks']*100;display=f"{r['solved']}/{r['tasks']} · {v:.1f}% · cycles={r['repeat_range']['cycles'] if r['repeat_range'] else 1}"
                        elif metric=='latency':v=ratio(r['wall_s'],r['tasks']);ran=[x/r['tasks'] for x in r['repeat_range']['wall_s']] if r['repeat_range'] else None
                        elif metric=='energy':v=ratio(r['gpu_j'],r['solved']);ran=r['repeat_range']['gpu_j_per_success'] if r['repeat_range'] else None
                        else:v=r['peak_vram_mib']
                    vals.append({'label':model['name']+' · '+model['quantization'],'subtitle':r['profile'] if r else None,'value':v,'range':ran,'display':display,'warning':bool(r and r['warning'])})
            name=f'{dis}-{metric}.svg';write(dest/name,svg(heading,unit,vals,100 if metric=='success' else None));page+=f'![{title}: {heading}; missing results labelled NOT MEASURED](assets/benchmarks/{name}){{ .benchmark-svg }}\n\n'
        page+=table(['Profile / record date','Success','Successful tasks/s','Total task time / GPU energy','Peak VRAM','Audit'],[[r['name']+' '+r['quantization']+' — '+r['profile']+' / '+r['metadata']['date'],f"{r['solved']}/{r['tasks']}",f"{r['solved']/r['wall_s']:.5f}" if r['wall_s'] else None,f"{r['wall_s']:.3f} s / {r['gpu_j']:.2f} J" if r['wall_s'] is not None and r['gpu_j'] is not None else None,r['peak_vram_mib'],f"[{r['experiment']}](experiments/{r['experiment']}.md)"] for r in rows])
        for r in rows:
            m=r['metadata'];page+='### '+r['name']+' · '+r['quantization']+' · '+r['experiment']+'\n\n'+r['profile']+'. '+(r['warning'] or 'No additional policy claim is inferred from this discipline.')+'\n\n'
            page+=table(['Condition','Audited value'],[['Separate process-VRAM observation (not device peak)',m['process_peak_vram_mib']],['Hardware / power',m['hardware']+' / '+str(m['power_limit_w'] if m['power_limit_w'] is not None else 'NOT RECORDED')+' W'],['Engine',m['engine']],['Date',m['date']],['Context, batching, KV, speculation',json.dumps(m['context_and_runtime'],sort_keys=True)],['Sampling / output cap',json.dumps(m['sampling'],sort_keys=True)+' / '+str(m['output_cap'] or 'NOT RECORDED')],['Cache / timing scope',m['cache_condition']],['Measurement batches',m.get('measurement_batches','Single suite or repeated cycles as stated')],['Actual template controls',json.dumps(m['chat_template_kwargs'],sort_keys=True) if m.get('chat_template_kwargs') else 'See pinned native request evidence'],['Actual input-token range (if exported)',json.dumps(m['actual_input_token_range']) if m.get('actual_input_token_range') else 'Not included in this public aggregate'],['Task count / repeats',str(r['tasks'])+' unique; '+(r['repeat_range']['definition'] if r['repeat_range'] else 'one observed answer per task; no repeated-run uncertainty measured')],['Model SHA-256',m['model_sha256'] or 'NOT RECORDED'],['Engine binary SHA-256',m['engine_binary_sha256'] or 'NOT RECORDED'],['Template SHA-256',m['template_sha256'] or 'See exact plan audit; not duplicated in public subset'],['Scorer adapter SHA-256',m['scorer_adapter_sha256'] or 'See audit scoring contract'],['EvalPlus provenance SHA-256',m['official_evalplus_provenance_sha256'] or 'Not applicable / not duplicated'],['Plan SHA-256',m['plan_sha256']]])
            page+='Original audit SHA-256 (originals retained privately; public excerpts are not the original files):\n\n'+''.join(f'- [{aid}](audits/{aid}.md): `{h}`\n' for aid,h in zip(r['audit_ids'],r['audit_sha256']))+'\n'
    page+='## Historical synthetic performance — separate protocol\n\nThese imported A0 records use historical model/build identities and synthetic native workloads. They are separate from task-success comparisons above. Token/s across tokenizers is a workload measurement, not useful-task superiority. **Bars: stored median; whiskers: median ± measured MAD; labels: MAD and sample size.** There are no invented confidence intervals.\n\n'
    for key,title in [('prefill','Prefill · ~512 tokens'),('prefill2048','Prefill · ~2K tokens'),('prefill4096','Prefill · ~4K tokens'),('decode','Decode · 128 tokens')]:
        values=[]
        for r in data['historical_native']:
            m=next(x for x in r['metrics'] if x['workload']==key);values.append({'label':r['name']+' · '+r['quantization'],'value':m['median'],'range':[max(0,m['median']-m['mad']),m['median']+m['mad']],'display':f"{m['median']:.2f} tok/s · MAD {m['mad']:.3f} · n={m['n']} ({m['sessions']} sessions)"})
        name='historical-'+key+'.svg';write(dest/name,svg(title,'tokens/s',values));page+=f'![Historical native {title}: median, MAD and sample size](assets/benchmarks/{name}){{ .benchmark-svg }}\n\n'
    for r in data['historical_native']:
        page+='### Historical '+r['name']+' · '+r['quantization']+'\n\n'+table(['Field','Original reference identity'],[['Hardware',r['hardware']],['Date',r['date']],['Power limit',r['power_limit_w'] if r['power_limit_w'] is not None else 'NOT RECORDED; do not assume current 300 W'],['Model SHA-256',r['model_sha256']],['Engine binary identity',json.dumps(r['engine_binary_sha256'],sort_keys=True)],['Runtime',json.dumps(r['conditions'],sort_keys=True)],['Reference',r['record_id']],['Audit SHA-256',r['audit_sha256'][0]]])+table(['Workload','Prompt token count(s)','Generated token count(s)','n / sessions'],[[m['workload'],m['actual_prompt_tokens'],m['generated_tokens'],str(m['n'])+' / '+str(m['sessions'])] for m in r['metrics']])+'\n'+f"[Original audit excerpt](audits/{r['audit_ids'][0]}.md). {r['note']}\n\n"
    page+='## Scientific metadata correction\n\nThe Bonsai agent campaign uses **2048 output tokens per turn**, from executed [R285](experiments/R285.md) and [R286](experiments/R286.md). Earlier chart metadata selected the failed pre-generation [R284](experiments/R284.md) plan and displayed 4096. The success counts, measured costs and immutable original audits are unchanged; coding/native-tool budgets remain separate.\n\n'
    page+='## Missing and partial evidence\n\nA missing bar means no complete audited result under that cohort. In particular, a native echo-control is not a BFCL score, a truncated QA screen is not HumanEval+, and a 2/4 agent early stop is not an 18-task score. See [all model admission stages and negative screens](models.md) and [experiment history](results.md). No existing negative result or qualification limit is removed.\n'
    write(docs/'benchmarks.md',page)
