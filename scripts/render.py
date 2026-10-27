#!/usr/bin/env python3
"""Deterministic English documentation from the reviewed public data snapshot."""
import hashlib,json,pathlib,re,html
P=pathlib.Path(__file__).resolve().parents[1];D=P/'docs'
def read(n):return json.loads((P/'data'/n).read_text())
def put(n,s):
 p=D/n;p.parent.mkdir(parents=True,exist_ok=True)
 s=re.sub(r'(?ms)^```json\n.*?^```[ \t]*(?:\n|$)',lambda m:'<details class="lab-evidence"><summary>Structured evidence</summary>\n\n'+m.group(0)+'\n</details>\n',s)
 p.write_text(s.rstrip()+'\n')
def pretty(x):return '```json\n'+json.dumps(x,ensure_ascii=False,indent=2)+'\n```\n'
def esc(x):return str(x if x is not None else 'NOT MEASURED / not recorded').replace('|','\\|').replace('\n',' ')
def table(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(esc(x) for x in row)+' |\n' for row in rows)+'\n'
def issue16_source_section(review):
 assert review['GPU_runs']==review['model_weight_payload_downloaded_bytes']==0
 mix=review['mixtral'];assert mix['total_parameters']>30_000_000_000 and mix['guarded_device_bytes']==14336*1024**2 and mix['ideal_4bit_weight_bytes']==mix['total_parameters']/2
 rows=[]
 for r in review['derivatives']:
  assert r['local_result']=='NOT MEASURED' and r['weight_delta_verified'] is False
  if 'Q3_file_bytes' in r:
   assert r['Q4_file_bytes']>mix['guarded_device_bytes'] and r['Q3_bytes_remaining_before_workspace']==mix['guarded_device_bytes']-r['Q3_file_bytes']-r['nominal_F16_KV_bytes_at_8192']
  rows.append(['['+r['model']+']('+r['source_url']+')',r['revision'],r['decision'],r['reason'],r['next_step']])
 text=''
 text+='**No derivative GPU run or weight-payload download.** Local quality for these source-only leads: **NOT MEASURED**. Publisher training claims are not independently verified weight deltas or local benchmark results.\n\n'
 text+='['+mix['model']+']('+mix['source_url']+'): **'+mix['decision']+'** — '+mix['reason']+'\n\n'
 text+=table(['Source-pinned candidate','Revision','Decision','Evidence / limit','Reopen condition'],rows)
 hermes=next(r for r in review['derivatives'] if 'Q3_file_bytes' in r)
 text+='Hermes exact published file sizes: Q3_K_M '+str(hermes['Q3_file_bytes'])+'B; Q4_K_M '+str(hermes['Q4_file_bytes'])+'B. Q3 plus nominal8K F16 KV leaves '+str(hermes['Q3_bytes_remaining_before_workspace'])+'B before workspace and other allocations; this is arithmetic, **not measured resident VRAM or admission**. Published artifact checksums remain metadata, not local payload verification.\n\n'
 external=[]
 for r in review['external_reports']:
  assert r['status'].startswith('EXTERNAL_') and r['model_sha256'] is None
  external.append(['[Primary report]('+r['source_url']+')',r['gpu'],r['reported_engine'],r['test'],r['decode_tokens_s'],r['reported_spread_tokens_s']])
 text+='### External synthetic decode evidence — excluded from local rankings\n\n'+table(['Source','Reported GPU','Reported engine','Workload','Decode tok/s','Reported spread'],external)
 text+=review['scope']+' Exact external weight revisions, power limits, quality and energy are not established; neither report is a matched SXM2 experiment.\n\n'
 text+='Metadata snapshot SHA256: `'+review['metadata_source_sha256']+'`; external primary-source snapshot: `'+review['external_source_sha256']+'`; original Mixtral triage: `'+review['mixtral_triage_sha256']+'`.\n'
 return '\n??? note "Issue16 source-only addendum · Mixtral, GPT-OSS derivatives and external Volta reports"\n\n'+''.join(('    '+line if line else '')+'\n' for line in text.splitlines())+'\n'
def agent_diagnostics_table(agents):
 rows=[]
 def pair(d,first,second):
  return (str(d[first])+' / '+str(d[second])) if d.get(first) is not None and d.get(second) is not None else None
 for v in agents:
  d=v.get('quality_diagnostics') or {}
  rows.append([v['model'],'['+v['experiment_id']+'](experiments/'+v['experiment_id']+'.md)',
   d.get('policy_violation_cases'),pair(d,'rejected_tool_call_cases','rejected_tool_call_events'),
   pair(d,'invalid_action_cases','invalid_action_events'),d.get('final_contract_failure_cases'),
   pair(d,'parse_failed_cases','parse_failed_rounds'),d.get('wrong_final_status_cases'),d.get('wrong_reason_code_cases'),
   d.get('incorrect_facts_cases'),d.get('evidence_or_postcondition_failure_cases')])
 return table(['Profile','Original replay','Policy violation cases /33','Rejected tool calls: cases / events','Invalid actions: cases / events','Final-contract failure cases /33','Parser failures: cases / rounds','Wrong final status cases /33','Wrong reason cases /33','Incorrect facts cases /33','Evidence/postcondition failure cases /33'],rows)
THEORY={
'R01':'Generation threads control host-side scheduling and CPU work. With full GPU offload, extra threads need not increase decode speed; CPU contention can increase latency.',
'R02':'Batch-processing threads govern host work during prompt evaluation. Their benefit depends on a demonstrated host bottleneck, not GPU thread-block occupancy.',
'R03':'Logical batch limits tokens admitted to one graph evaluation. It differs from physical microbatching and must be controlled separately.',
'R04':'Physical microbatches split a logical batch into GPU evaluations. They trade GEMM efficiency against workspace, graph and recurrent-state memory.',
'R05':'Multiple slots can amortize matrix work across requests but share GPU memory and scheduling. Correct independent conversation states are a prerequisite for throughput claims.',
'R06':'Flash attention fuses attention operations to reduce intermediate memory traffic. Actual support depends on head dimensions, KV formats and compiled SM70 kernels.',
'R07':'The host prompt-state cache budget controls retained reusable states. A larger limit helps only when valid states are actually hit or evicted.',
'R08':'Reusing cached prefixes avoids repeated prompt evaluation, provided tokenizer, positions, model, cache and recurrent state identities match.',
'R09':'Context shifting discards or repositions old tokens. Hybrid recurrent state and interleaved multi-section RoPE require architecture-specific correctness.',
'R10':'A unified KV pool changes allocation across sequences. Pool layout and sequence isolation must be checked separately from raw allocation size.',
'R11':'A per-slot token cap can limit accepted requests without shrinking the underlying fixed KV pool. Admission limits and allocated VRAM are different measurements.',
'R12':'Prompt caching retains attention and recurrent state across requests. Invalid reuse can change outputs or leak one conversation into another.',
'R13':'GPU offload places model layers on device memory. CPU offload can enable capacity-limited models at the cost of PCIe and CPU latency.',
'R14':'Memory-mapped weights use the operating-system page cache. Warm load, cold file reads and explicit prefault costs must be measured separately.',
'R15':'Memory locking can prevent host weight pages from being swapped. It consumes host resources and does not itself accelerate a GPU-resident decode kernel.',
'R16':'NUMA placement can affect host memory and PCIe locality only when the actual platform exposes useful multiple-node topology.',
'R17':'CPU affinity controls which cores run inference-related host work. It requires the real topology and a fixed competing-load policy.',
'R18':'Streaming changes when generated output reaches the caller. Visible first-token latency must not be confused with buffered JSON or native decoder timing.',
'R19':'Context capacity reserves attention KV storage and affects recurrent-state planning. Successful long-document tasks must be checked beyond token throughput.',
'R20':'Prompt length changes arithmetic intensity and attention work. Fixed exact inputs are needed to attribute differences to an optimization.',
'R21':'Decode budgets change task completion, truncation and total time. Shorter output is useful only when correctness is retained.',
'R22':'Warm process, weights, graphs and prefix state are separate cache conditions. Prefix reuse is not a general decode acceleration.',
'K01':'Quantizing attention keys reduces KV storage but adds conversion and changes attention scores. It does not quantize the separate GDN recurrent state.',
'K02':'Quantizing attention values reduces KV storage but changes the attention value product. Its error behavior differs from key quantization.',
'K03':'Paired key/value formats create a joint attention kernel configuration. Individual key and value successes cannot be added to predict the pair.',
'K04':'Flash-attention format coverage determines which K/V pairs have a runnable implementation for the exact head dimensions and SM70 binary.',
'K05':'Multi-turn, rejection and restore operations must preserve GDN and attention state consistently. Primitive rollback tests do not qualify the full server scheduler.',
'K06':'Host-side KV offload trades device capacity for transfers and CPU work. It requires a real capacity problem and bounded host memory.',
'K07':'Compaction replaces retained history with a smaller representation. Information preservation, provenance and task success require independent evaluation.',
'C01':'Forcing quantized matrix multiplication changes routing across eligible shapes. A local small-batch benefit can coexist with severe prefill regressions.',
'C02':'Forcing cuBLAS changes the matrix path and conversion costs. This is routing, not a new Tensor Core instruction.',
'C03':'Compiling CUDA Graph support can reduce repeated launch overhead. Correct capture, replay and state lifecycle must be distinguished from graph optimization settings.',
'C04':'Graph optimization policy is distinct from enabling CUDA Graphs. A flag value alone does not prove optimized nodes or a replay-time improvement.',
'C05':'Compiling flash-attention kernels controls available operations. Runtime auto-selection logs alone do not identify an executed kernel.',
'C06':'Disabling virtual-memory management changes allocation behavior and memory overhead. Warm throughput does not establish cold-start or fragmentation effects.',
'C07':'The compiled flash-attention quantization set controls eligible KV kernels. Smaller binary size is not automatically faster inference.',
'C08':'cuBLAS operand precision determines conversion/storage and supported kernels. Operand format must not be mislabeled accumulator precision.',
'C09':'MMVQ warp configuration changes work distribution and register pressure. Shape-specific decode paths require actual dispatch evidence.',
'C10':'MMQ tile width changes reuse, occupancy and resource pressure. Comparisons with common forced routing do not represent stock routing.',
'C11':'Fused dequantization and matrix products avoid materialized intermediates. Existing fused defaults must not be presented as a newly achieved speedup.',
'C12':'RMSNorm, scaling and RoPE fusion reduces intermediate loads and launches. NORMAL/NEOX support does not imply support for hybrid interleaved multi-section RoPE.',
'C13':'GDN state-write fusion can remove copies when state type and layout match. F32-only cache fusion cannot silently be combined with F16 state storage.',
'C14':'Computation and output accumulation precision affect rounding and bandwidth. Coupled precision/output changes are not a pure isolated accumulation experiment.',
'C15':'Fatbinary compression affects distribution and loading. The effective NVCC flag must be present; a CMake cache entry or different ELF hash is insufficient.',
'C16':'Launch queue scaling changes driver queue capacity. It needs actual enqueue pressure to justify another sweep; it does not add independent GPU workers.',
'C17':'Device connection count changes host work-queue mapping. It differs from copy-connection settings and does not guarantee concurrent execution.',
'C18':'A selected upstream kernel port must identify an actual algorithm or launch-layout change. A newer revision number alone is not an optimization.',
'H01':'Pinning host work can reduce scheduling jitter when a host bottleneck exists. It does not change device arithmetic.',
'H02':'Host CPU isolation affects other services and needs an explicitly isolated environment. It cannot be justified by an unmeasured inference benefit.',
'H03':'Power limits trade clocks, latency and energy. Optimize integrated GPU joules per successful task rather than the lowest watt reading.',
'H04':'Application clocks are requests, not proof of actual fixed SM clocks. Capture actual load clocks and throttling alongside every comparison.',
'H05':'Cooling affects throttling and stability, but ambient conditions drift. Temperature is telemetry within hardware safety limits, not an arbitrary starting threshold.',
'H06':'PCIe and interconnect topology matters for transfers and offload. Multi-GPU NVLink gains do not transfer to a single-card setup.',
'H07':'Swap and hugepages affect host memory behavior. Global host changes require an isolated capacity hypothesis and do not prove GPU progress.',
'H08':'Model page-cache policy changes startup reads. Include private prefault/eviction preparation costs rather than reporting only the shortened load interval.',
'H09':'CUDA MPS changes multi-process resource sharing. It is outside a one-heavy-job research protocol unless separately admitted.',
'H10':'Unified memory can oversubscribe device capacity but introduces migration. It needs allocator support and measured host/device traffic.',
'Q01':'Weight quantization trades storage and dequantization costs against output quality. Compare tasks and wall time across tokenizers, not tokens/s alone.',
'Q02':'An importance matrix weights quantization errors using calibration activations. Calibration data must be separate from evaluation and exact source weights pinned.',
'Q03':'Mixed tensor quantization preserves sensitive operations at higher precision. Each tensor-policy change needs its own quality and memory test.',
'Q04':'AWQ uses activation-aware weight scaling/quantization. It needs matching weights, architecture support and an actual SM70 inference path.',
'Q05':'Selective outlier retention keeps sensitive weights in higher precision. It requires a concrete implemented tensor policy, not a renamed mixed-quantization result.',
'Q06':'A quantization format is useful only if supported by the loaded engine kernels. A readable file is not proof of accelerated device execution.',
'Q07':'QAT changes training to account for quantization. A pretrained deployment-compatible checkpoint and its training provenance are required.',
'Q08':'Attention KV and recurrent-state precision are different choices. State-storage compression must preserve repeated updates and rejection/restore behavior.',
'M01':'Reasoning-token budgets can improve complex tasks but raise latency, energy and truncation risk. Budgets need independent task-level evidence.',
'M02':'Sampling temperature changes the output distribution. A repeated greedy seed is not a stochastic quality estimate.',
'M03':'Top-k filters the candidate token set. In greedy decoding it can be effectively inactive, so configuration changes need proof of treatment.',
'M04':'Top-p filters cumulative probability mass. With deterministic argmax it may not change a single token decision.',
'M05':'Min-p removes tokens below a relative probability threshold. It requires an active stochastic profile and a quality hypothesis.',
'M06':'Repetition penalties and DRY alter token scores. They can suppress legitimate code or tool syntax and need functional checks.',
'M07':'Chat templates and instructions determine how native roles and tool syntax reach the model. Correct model-specific formatting precedes speed comparison.',
'M08':'Output grammars constrain valid syntax. Syntax validity does not guarantee correct tool selection or safe actions.',
'M09':'Function serialization and descriptions change token count and ambiguity. Faster compressed schemas can cause wrong tool selection.',
'M10':'Declared maximum context is model metadata, not demonstrated usable context. Position scaling needs architecture support and semantic tests.',
'M11':'System-instruction placement can change authority and prompt-injection behavior. Preserve native role semantics.',
'M12':'Stop tokens define generation termination. Removing an end token to obtain longer output can break native tool protocols.',
'M13':'Tool completion includes call parsing, argument typing, refusal and final-response behavior. Correct JSON alone is insufficient.',
'S01':'Prompt/ngram lookup proposes tokens from context. Acceptance and task success depend on the verifier and actual workload repetition.',
'S02':'Draft length trades proposed work against verification cost. The longest accepted span need not minimize total task time.',
'S03':'MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.',
'S04':'A separate draft model can reduce target steps at the cost of extra memory, startup and verification. Tokenizer and target compatibility are necessary.',
'E01':'Engine revisions change many behaviors. Pin commits, templates, builds and kernels; compare a whole configuration unless the patch is isolated.',
'E02':'A lab Ollama frontend adds model routing and protocol translation. Actual native tool messages and one owned GPU worker must be verified.',
'E03':'vLLM support on SM70 depends on source builds, PyTorch device support, model loaders and compatible kernels. Import success is insufficient.',
'E04':'TensorRT-LLM requires concrete model, toolchain and hardware support. Modern kernels cannot be assumed to support Volta.',
'E05':'ExLlama requires supported weight formats and device kernels. GGUF compatibility cannot be inferred from a model name.',
'E06':'An SM70 build must contain native compatible kernels. Merely setting an architecture variable is not proof of emitted binary coverage.',
'E07':'Compiler, discovered toolkit and loaded CUDA runtime are separate identities. Change only one admitted toolchain factor and retain A0.',
'E08':'Grammar parsing can change allowed token sequences and host overhead. Separate protocol correctness from GPU throughput.',
'E09':'Scheduling controls batching and conversation lifecycles. Reusing or erasing another slot state is not a safe parallelism fix.',
'A01':'Schema/prefix caching amortizes repeated agent context. Correct invalidation on schema, policy and conversation changes is mandatory.',
'A02':'Retrieval selects relevant history with provenance. It can save prefill while omitting facts required by later tool decisions.',
'A03':'Harness compression reduces context tokens but can alter tool semantics. Preserve structured data and evaluate complete tasks.',
'A04':'An independent tool gate checks authorization and arguments outside generation. A safe simulator result does not authorize production actions.',
'A05':'Planning/reflection loops trade extra generation for recovery. Evaluate additional successful tasks per second and joule, including failures.',
'A06':'Code execution and evaluation must use isolated tests and correct joint pass rules. Training loss or a syntax check is not coding success.',
'A07':'Idempotency, retry and rollback contracts prevent duplicate effects. Offline component replay does not qualify production recovery.',
'A08':'Context compression is a semantic policy, not just shorter text. Independent held-out task sequences must preserve facts and authorization.',
'T01':'LoRA/QLoRA train adapters with reduced optimizer state. The exact hybrid/MTP implementation and a real training step must fit the device.',
'T02':'Domain fine-tuning changes weights and task distribution. Split training, development and independent evaluation data.',
'T03':'Low-rank factorization reduces matrix parameters only when a compatible inference path realizes the saving. Rank choice changes model quality.',
'T04':'Pruning requires compact or sparse execution to reduce real work. Zero weights in an unchanged dense kernel do not establish a speedup.',
'T05':'Distillation transfers behavior to a different model or head. It needs trustworthy trajectories, resources and independent evaluation.',
'T06':'QAT retraining optimizes quantized behavior during training. It is not a runtime flag or free inference-only transformation.',
'T07':'Tensor smoothing redistributes activation/weight ranges. It changes tensor semantics and needs architecture-aware calibration and numerical checks.'}
HBM=['Effective bandwidth and roofline','Coalesced and vectorized accesses','SM70 MMVQ warp mapping','SM70 MMQ tiles and warps','Volta FP16 Tensor Core kernel','Dequantization and GEMV/GEMM fusion','L1/L2/shared-memory reuse','F16/Q8/Q4 attention KV cache','KIVI asymmetric KV quantization','KVQuant calibrated KV quantization','Paged attention and KV blocks','Asynchronous KV prefetch to L2','OasisKV sparse lookahead prefetch','Host/PCIe/HBM staging','VMM and allocator fragmentation','Attention and recurrent-state memory','Speculative decoding memory traffic','Volta-specific flash attention','Energy per correct task/token','StreamDQ custom HBM','FlashAccel high-bandwidth flash','QServe W4A8KV4','FlashInfer attention engine','Fork-specific experimental attention']
ALIASES={'HBM02':'HBM02','HBM03':'C09','HBM04':'C10','HBM05':'HBM05','HBM06':'C11','HBM07':'HBM07','HBM08':'K03','HBM14':'K06','HBM15':'C06','HBM16':'C13','HBM17':'S03','HBM18':'R06','HBM19':'H03'}
THEORY.update({'HBM01':'Roofline analysis compares actual arithmetic and memory traffic. Model bytes divided by time are an estimate, not a measured HBM transaction count.','HBM02':'Aligned vector loads can reduce instructions, but actual pointer alignment, tails, register pressure and fallback paths must be checked.','HBM05':'Volta supports FP16 Tensor Cores with architecture-specific MMA layouts and synchronization. New lane permutations need numerical and executed-path evidence.','HBM07':'Persistent conversion or shared/cache reuse can reduce redundant reads and dequantization. It consumes capacity and can change the workload that fits.','HBM09':'KIVI uses asymmetric key/value quantization. A generic symmetric Q4 cache is not a KIVI implementation.','HBM10':'KVQuant calibrates attention-cache compression with specific outlier/layout handling. Native cache dtype flags are not equivalent.','HBM11':'Paged KV allocation can reduce fragmentation in serving. It needs compatible attention kernels and a real multi-sequence capacity problem.','HBM12':'Prefetching can hide memory latency only if the executed KV access pattern and hardware instructions support it. Volta has no cp.async/TMA.','HBM13':'Sparse lookahead prefetch changes token selection and memory access. Dense attention quality and actual sparse execution must be independently checked.','HBM20':'Custom HBM hardware cannot be enabled by software on an existing V100. External architectural results require different physical equipment.','HBM21':'High-bandwidth flash systems require different storage hardware. They are not a drop-in HBM2 optimization.','HBM22':'QServe is a coordinated weight/activation/KV quantization stack. Independent GGUF Q4 and Q8 results cannot be combined into a QServe claim.','HBM23':'FlashInfer needs model-layout, dtype and architecture-compatible implementations. Modern GPU support does not imply SM70 compatibility.','HBM24':'Fork-specific attention architectures can require different trained weights and operators. Model changes are not retrofitted runtime flags.'})
BMT=['Minimal tool-schema descriptions','GDN/MTP rejection, prefix and slot-state correctness','Adaptive MTP draft length','Independent Q4/Q5/Q6 draft precision','MTP-head GGUF graft packaging','Agent harness and bounded recovery','Source-grounded retrieval','Hybrid attention KV precision','KV rotation and mean centering','DP4A/ternary inference kernels','Deployment-compatible QAD/QAT checkpoints','MoE residency and expert prefetch','DFlash/DSpark drafting','Verified trajectory distillation','Sensitivity-guided rank/pruning','Cold-load and specialist routing','SM70 graphs and GDN fusion','Independent tool authorization gates','Looped transformer weight sharing','LoopSplit, hyperconnections and depth attention','Task/scaffold/rollout co-evolution','Trajectory-level DPPO','Weakness-directed cross-model training data','Geometry-grounded OCR','Action-grounded GUI policies','Streaming cache-aware RNNT ASR','Confidence calibration and selective tool use','Stochastic recurrent-state rounding','Adaptive reasoning budgets','Learned ngram embeddings','Q4/Q6 conversion-cache transfer','GQA/MQA/MLA and sparse/local attention']
def title(f):
 if f['id'].startswith('HBM'):return HBM[int(f['id'][3:])-1]
 if f['id'].startswith('BMT'):return BMT[int(f['id'][3:])-1]
 return f['title']
def rationale(f):
 ident=f['id'];base=THEORY.get(ident,THEORY.get(ALIASES.get(ident),''))
 if not base:
  linked=f['linked_original_axes'];base='This research subcase investigates '+title(f).lower()+'. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference.'
  if linked:base+=' Related mechanisms: '+'; '.join(THEORY[x] for x in linked[:2] if x in THEORY)
 return base

def new_family_evidence(screening,history,experiments):
 """Exact verified links only; no name-based score transfer or best-run picking."""
 names={'Ministral-3-14B-Instruct-2512','gpt-oss-20b','Ministral-3-8B-Instruct-2512','Phi-4','Devstral-Small-2-24B-Instruct-2512','Mistral-Small-3.2-24B-Instruct-2506','GLM-4.7-Flash','Nemotron-3-Nano-30B-A3B'}
 result=[];artifacts=set();profiles={p['runtime_configuration_id']:p for p in history['profiles']}
 for row in screening['rows']:
  if row['model'] not in names:continue
  sha=row['configuration']['model_sha256'];artifacts.add(sha);points=[]
  for ref in row.get('full_benchmark_runs',[]):
   matches=[r for r in history['runs'] if all(r.get(k)==ref.get(k) for k in ('experiment_id','runtime_configuration_id','benchmark_identity_id','audit_hash')) and r.get('official_eligible') is True]
   assert matches,'Missing exact qualified screening/profile link'
   assert all(r.get('full_benchmark_score_claimed') is not False and r['benchmark_id'] in {'humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200'} and r['tasks']=={'humanevalplus-v0.1.10':164,'bfcl-v4-parallel-multiple-full200':200}[r['benchmark_id']] and type(r['solved']) is int and 0<=r['solved']<=r['tasks'] for r in matches),'Incomplete or unsupported official category'
   signatures={json.dumps({k:r[k] for k in ('benchmark_id','benchmark_revision','dataset_split_hash','scorer_version','model_artifact_id','solved','tasks','wall_s','peak_vram_mib')},sort_keys=True) for r in matches}
   assert len(signatures)==1,'Conflicting views of the same archived measurement'
   assert all(profiles[r['runtime_configuration_id']]['model']['artifact_sha256']==sha and profiles[r['runtime_configuration_id']]['model_artifact_id']==r['model_artifact_id'] for r in matches),'Linked weights differ'
   counters=[r['counter_energy'] for r in matches if r.get('counter_energy')]
   assert not counters or all(c==counters[0] for c in counters),'Conflicting energy supplements'
   r=matches[0];counter=counters[0] if counters else None
   if counter:assert counter['tasks']==r['tasks'] and counter['solved']==r['solved']
   point={k:r[k] for k in ('experiment_id','runtime_configuration_id','benchmark_identity_id','benchmark_id','solved','tasks','wall_s','peak_vram_mib','audit_hash')}
   point['counter_energy']=counter
   if point not in points:points.append(point)
  partials=[]
  for r in history['runs']:
   if r.get('status')!='PARTIAL' or profiles[r['runtime_configuration_id']]['model']['artifact_sha256']!=sha:continue
   p={k:r.get(k) for k in ('experiment_id','runtime_configuration_id','benchmark_id','solved','tasks','intended_tasks','termination_kind','audit_hash')}
   if p not in partials:partials.append(p)
  result.append({'model':row['model'],'model_sha256':sha,'quantization':row['configuration'].get('quantization'),'screening_experiment':row.get('experiment_id'),'screening_results':row.get('results'),'status':row['status'],'local_artifact_available':row['local_artifact_available'],'technical_blocker':row.get('technical_blocker'),'qualified_runs':points,'partial_runs':partials,'unscored_attempts':row.get('unscored_qualification_attempts',[])})
 agents=[]
 for exp in experiments:
  a=exp.get('aggregate_metrics',{}).get('native_validation33')
  if not a or a.get('model_sha256') not in artifacts:continue
  assert a['official_benchmark'] is False and a['tasks']==a['planned_tasks']==33
  agents.append({'experiment_id':exp['id'],**{k:a.get(k) for k in ('model_sha256','profile_sha256','solved','tasks','policy_gate_passes','task_phase_s','gpu_j_per_success_lower','gpu_j_per_success_upper','peak_device_vram_mib')}})
 return {'models':result,'agent_profiles':agents}

def new_family_section(screening,history,experiments):
 review=new_family_evidence(screening,history,experiments);rows=[];costs=[]
 link=lambda eid:'['+eid+'](experiments/'+eid+'.md)'
 for row in review['models']:
  g=row['screening_results']
  dev=lambda category:('NOT MEASURED' if not g else str(g[category]['successes'])+'/'+str(g[category]['completed']))
  scores={}
  for r in row['qualified_runs']:
   name='Coding' if r['benchmark_id']=='humanevalplus-v0.1.10' else 'Tools' if r['benchmark_id']=='bfcl-v4-parallel-multiple-full200' else r['benchmark_id']
   scores.setdefault(name,[]).append(str(r['solved'])+'/'+str(r['tasks'])+' '+link(r['experiment_id']))
   counter=r['counter_energy'];energy=(str(round(counter['j_per_success_lower'],1))+'–'+str(round(counter['j_per_success_upper'],1))) if counter and counter.get('j_per_success_lower') is not None and counter.get('j_per_success_upper') is not None else 'UNDEFINED (0 successes)' if counter and r['solved']==0 else 'NOT MEASURED'
   total_energy=(str(round(counter['lower_j'],1))+'–'+str(round(counter['upper_j'],1))) if counter else 'NOT MEASURED'
   costs.append([row['model'],name,link(r['experiment_id']),round(r['wall_s'],3) if r['wall_s'] is not None else None,total_energy,energy,r['peak_vram_mib'],'[Exact profile](configuration-profiles/'+r['runtime_configuration_id']+'.md)'])
  status=row['status']
  if row['technical_blocker']:status+=' · '+row['technical_blocker']['decision']+' '+link(row['technical_blocker']['experiment_id'])
  if row['local_artifact_available'] is False:status+=' · weight cache evicted; results retained'
  rows.append([row['model'],row['quantization'],dev('coding'),dev('tools'),' · '.join(scores.get('Coding',[])) or 'NOT MEASURED',' · '.join(scores.get('Tools',[])) or 'NOT MEASURED',status])
 text='## New-family evidence — current extension\n\nAll eight requested candidates remain visible. Development16+16 results are not official scores; complete categories below use exact verified profile/audit links. Missing categories are not zero, and small screening differences do not exclude a model.\n\n'
 text+='The regular total-parameter gate is30B. GLM4.7Flash and Nemotron3Nano have explicit owner-approved parameter-count exceptions; memory, runtime and hardware guards are unchanged.\n\n'
 text+=table(['Model','Quant','Dev coding /16','Dev mock tools /16','HumanEval+164 qualified','BFCL parallel200 qualified','Disposition'],rows)
 references={}
 for eid,bid in [('R516','humanevalplus-v0.1.10'),('R517','bfcl-v4-parallel-multiple-full200')]:
  matches=[r for r in history['runs'] if r['experiment_id']==eid and r['benchmark_id']==bid and r.get('official_eligible') is True]
  if matches:
   assert len({json.dumps({k:r[k] for k in ('runtime_configuration_id','benchmark_identity_id','solved','tasks','wall_s')},sort_keys=True) for r in matches})==1
   references[bid]=matches[0]
 if len(references)==2:
  comparable=[]
  for row in review['models']:
   points={bid:[p for p in row['qualified_runs'] if p['benchmark_id']==bid and p['benchmark_identity_id']==ref['benchmark_identity_id']] for bid,ref in references.items()}
   if all(len(v)==1 for v in points.values()):comparable.append((row,[v[0] for v in points.values()]))
  if comparable:
   text+='### Updated comparison decision\n\nThe unchanged OmniCoder bartowski Q6, MTP OFF reference has '+str(references['humanevalplus-v0.1.10']['solved'])+'/164 coding '+link('R516')+' and '+str(references['bfcl-v4-parallel-multiple-full200']['solved'])+'/200 tools '+link('R517')+'. '+str(len(comparable))+' new native profiles have complete results on both exact benchmark definitions.\n\n'
   if all(all(p['solved']<references[p['benchmark_id']]['solved'] for p in points) for row,points in comparable):
    text+='All these completed new coding/tool pairs have fewer observed successes in both categories. **Retain the established balanced reference; no new allround replacement is qualified.** This is a finite-benchmark comparison, not a population-superiority proof or permanent model exclusion.\n\n'
   faster=[row['model'] for row,points in comparable if all(p['wall_s'] is not None and references[p['benchmark_id']]['wall_s'] is not None and p['wall_s']<references[p['benchmark_id']]['wall_s'] for p in points)]
   if faster:text+='Lower observed response time on both categories: **'+', '.join(faster)+'**. Read the exact success counts and resource costs together: this is a whole-profile quality/latency tradeoff, not a quality-preserving optimization or causal speedup.\n\n'
   text+='Coding-only, tool-only, blocked and screening-only candidates remain under review in their measured scopes. A failed interface or small development score is not grounds for a general model rejection. Agent33 and policy behavior remain separate evidence below; official Terminal-Bench remains NOT MEASURED.\n\n'
 text+='??? note "Qualified-run resource measurements and exact profiles"\n\n'
 text+=''.join('    '+line+'\n' if line else '\n' for line in table(['Model','Category','Run','Response wall s','GPU J bounds','GPU J/success bounds','Peak VRAM MiB','Configuration'],costs).splitlines())
 text+='\nResponse wall excludes startup/warmup/CPU scoring; counter-energy groups include failed tasks and between-request setup. Bounds describe query timing, not confidence intervals or system energy. Different task coverage, output behavior and profiles prevent a causal speed ranking.\n\n'
 gaps=[]
 for row in review['models']:
  for p in row['partial_runs']:gaps.append([row['model'],link(p['experiment_id']),'PARTIAL',str(p['solved'])+'/'+str(p['tasks'])+' observed; '+str(p['intended_tasks'])+' planned',p['termination_kind']])
  for p in row['unscored_attempts']:gaps.append([row['model'],link(p['experiment_id']),'NOT MEASURED','No scorable benchmark result',p['decision']])
 if gaps:
  text+='??? note "Partial results and technical qualification gaps — separate recorded profiles"\n\n'
  text+=''.join('    '+line+'\n' if line else '\n' for line in table(['Model','Run','Status','Observed evidence','Limit / next diagnosis'],gaps).splitlines())
  text+='\nThese records do not enter complete-category scores. Incomplete tasks are unknown; technical failures do not measure zero quality. No automatic retry or cross-profile score transfer.\n\n'
 if review['agent_profiles']:
  text+='### Separate authored Agent33 profiles\n\nThese are independently replayed internal validation profiles, not Terminal-Bench or official ranking inputs. They are listed separately; shared weights alone do not prove identical inference settings.\n\n'
  text+=table(['Run','Verified success','Policy passes','TASK s','GPU J/success bounds','Peak VRAM MiB','Profile SHA256'],[[link(a['experiment_id']),str(a['solved'])+'/33',str(a['policy_gate_passes'])+'/33',a['task_phase_s'],str(a['gpu_j_per_success_lower'])+'–'+str(a['gpu_j_per_success_upper']),a['peak_device_vram_mib'],a['profile_sha256']] for a in review['agent_profiles']])
  reference=next((e.get('aggregate_metrics',{}).get('native_validation33') for e in experiments if e['id']=='R536'),None)
  if reference and all(a['solved']<reference['solved'] for a in review['agent_profiles']):text+='Every measured new agent profile has fewer observed successes on this authored set than the retained '+str(reference['solved'])+'/33 reference '+link('R536')+'. Grouped samples are small and exposed: this is not population inferiority, equivalence or safety certification. Tool authorization stays deterministic outside the model.\n\n'
 text+='The original core gate below remains a **dated baseline**; the current family comparison extends its evidence without rewriting its provenance or reference profiles. Further gates are retained in the [screening and qualification view](screening.md); Jarvis deployment remains deferred.\n\n'
 return text

def final_snapshot_page(register,experiments,profiles,refs,counts,pipeline,issues=None,screening=None,history=None):
 review=register.get('final_evidence_review');roles=register.get('role_comparison')
 if not review or not roles:return None
 es={e['id']:e for e in experiments}
 point=lambda kind,eid:next(p for p in roles['categories'][kind]['points'] if p['experiment_id']==eid)
 agent=lambda eid:next(p for p in roles['agents_development'] if p['experiment_id']==eid)
 score=lambda p:str(p['solved'])+'/'+str(p['tasks'])
 link=lambda eid:'['+eid+'](experiments/'+eid+'.md)'
 bart_c=point('coding','R516');bart_t=point('tools','R517');bart_a=agent('R536');gemma=point('coding','R464');q_c=point('coding','R548');q_t=point('tools','R549');q_a=agent('R550')
 release=register.get('final_research_gate')
 text=('# Best-of-V100 2026 — research decision' if release else '# Best-of-V100 2026 — evidence snapshot')+'\n\n'
 if (P/'data/frozen-baselines.json').exists():text+='**Newer decision:** [Three frozen Jarvis baselines — evidence through R585](final-selection.md). This page retains the dated earlier decision and its original scope.\n\n'
 if release:
  text+='**Reviewed research decision · evidence through R551 · actual review '+release['at_utc'][:10]+' · deadline31 October 2026.** The decision package is available ahead of the deadline. No future execution date, universal winner, production deployment or official 3/3 result is claimed.\n\n'
 else:
  text+='**Pre-freeze draft · evidence through R551 · review '+review['at_utc'][:10]+'. Final research freeze:31 October 2026.** No universal winner, production deployment or official 3/3 result is established.\n\n'
 if screening is not None and history is not None:text+=new_family_section(screening,history,experiments)
 scoped=next((x for x in issues or [] if x.get('completion_review_sha256')),None)
 if scoped:text+='**Eight-family review completed with explicit scope limits.** Source/decision review SHA256: `'+scoped['completion_review_sha256']+'`. [Candidate dispositions and source-only addendum](questions.md). This is not qualification of deferred profiles, a new universal Champion or production approval.\n\n'
 text+='## Dated core decision — evidence through R551\n\n'
 text+='- **Jarvis sandbox baseline: OmniCoder bartowski Q6, MTP OFF.** Coding '+score(bart_c)+', tools '+score(bart_t)+'; separately measured local Agent33 '+score(bart_a)+' with '+str(bart_a['policy_gate_passes'])+'/33 policy passes. Retain for isolated integration, not a safety certificate or general model-superiority claim. '+link('R516')+' · '+link('R517')+' · '+link('R536')+'\n'
 text+='- **Coding quality: Gemma4 nonthinking QAT profile.** '+score(gemma)+' is the highest observed coding score among the core profiles. Its tools and local agent results do not support the same allround recommendation. '+link('R464')+' · '+link('R472')+' · '+link('R534')+'\n'
 text+='- **Native-tool efficiency: OmniCoder bartowski Q6 + MTP3.** Retain only the tested tool scope. Its coding and Agent33 regressions remain disqualifying for those roles. '+link('R542')+' · '+link('R546')+' · '+link('R541')+' · '+link('R543')+'\n'
 text+='- **Larger alternative: Qwen3.8 27B integrated MTP3.** Coding '+score(q_c)+', tools '+score(q_t)+' and separate local agents '+score(q_a)+' / policy '+str(q_a['policy_gate_passes'])+'/33. Higher VRAM and per-task costs remain material. '+link('R548')+' · '+link('R549')+' · '+link('R550')+'\n'
 text+='- **Retain Qwen3.5, Nexus, canonical OmniCoder and Ornith** as documented quality/resource alternatives. Small differences on authored tasks do not justify automatic exclusion.\n\n'
 text+='The [single model/configuration comparison](configuration-comparison.md) contains complete locally qualified HumanEval+164 and BFCL parallel_multiple200 results, actual cost fields, exact parameters and audit links. Its user-defined arithmetic mean uses only available complete categories of the same verified inference configuration and shows coverage n/3. It is not an official overall score. The [role/Pareto detail](configurations.md) keeps configuration tradeoffs and local Agent33 evidence separate.\n\n'
 text+='## Measured optimization decisions\n\n**LOCAL MEASURED / LOKAL GEMESSEN**, within each linked scope:\n\n'
 arms=es['R546']['aggregate_metrics']['native_tools_confirmation']['arms'];aa,bb=arms
 reduction=100*(1-bb['response_wall_s']/aa['response_wall_s']);energy=100*es['R546']['aggregate_metrics']['native_tools_confirmation']['comparison']['GPU_j_per_success_reduction_conservative']
 text+='- **Tool MTP:** fresh matched full-category control retains '+str(aa['solved'])+'/'+str(aa['tasks'])+' on both arms; response wall falls '+f'{reduction:.2f}'+'%, conservative GPU J/success '+f'{energy:.2f}'+'%. This is confirmation of existing measurements, not another independent leaderboard score. '+link('R546')+'\n'
 fresh=es['R551']['mtp_confirmation'];c={**fresh['comparison'],'response_latency_reduction_percent':100*(1-fresh['arms'][1]['response_wall_s']/fresh['arms'][0]['response_wall_s'])}
 text+='- **Qwen27 integrated MTP:** fresh development control retains 16/16 coding and 13/16 mock tools in both arms, with '+f"{c['response_latency_reduction_percent']:.2f}"+'% lower response wall and '+f"{c['conservative_GPU_J_per_success_reduction_percent']:.2f}"+'% conservative GPU J/success reduction, at +'+str(int(c['additional_peak_device_vram_mib']))+' MiB peak VRAM. Exposed development data, not a new official score, lossless-token proof or population noninferiority. '+link('R551')+'\n'
 historical=[p for p in profiles if p.get('C') and refs[p['C']]['experiment_id']=='R90' and refs[p['C']]['aggregate_metrics'].get('metrics',{}).get('prefill2048',{}).get('unit')=='seconds']
 if len(historical)==1:
  p=historical[0];base=refs[p['A0']]['aggregate_metrics']['metrics'];cand=refs[p['C']]['aggregate_metrics']['metrics'];d=[100*(1-cand[k]['median']/base[k]['median']) for k in ('prefill2048','prefill4096')]
  text+='- **Historical HBM07:** fixed 2K/4K prefill token-event TTFT medians improve '+f'{d[0]:.2f}'+'% / '+f'{d[1]:.2f}'+'% against the matched stored A0. Higher VRAM and the exact historical engine/workload limits remain; no universal decode gain. '+link('R90')+'\n'
 text+='- **Historical prefix and energy/context profiles:** retain prefix reuse only for reused-prefix workloads, the independently qualified 32K profile, and the 175-W low-VRAM natural-SSE profile in their own scopes. They are not automatically transferable to current native-chat/MTP captures. '+link('R80')+' · '+link('R221')+' · '+link('R113')+'\n'
 text+='- **Negative evidence retained:** Omni MTP coding 131/164 versus 134/164 and Agent33 loss; Gemma Q8-key coding 151/164 versus 156/164; Gemma Thinking development tool regression and much higher costs. No synthetic-speed exception overrides these quality gates. '+link('R541')+' · '+link('R543')+' · '+link('R544')+' · '+link('R545')+'\n\n'
 text+='These gains are not added together. Existing scoped reference/Champion profiles remain in the [reference archive](configurations.md); no new combination or universal Champion is inferred here.\n\n'
 text+='## Integrity and bounded stability\n\n'
 text+=str(review['experiment_count'])+' original experiments / '+str(review['capture_count'])+' capture windows were source-hash checked and recomputed from retained telemetry against the original guard limits: **'+format(review['sample_count'],',')+' retained samples**, **'+str(review['sampled_guard_violations'])+' observed guard violations**, **'+str(review['incomplete_captures'])+' captures with missing required telemetry**. All selected original contracts address the same device. No new inference or scoring was performed. [Review audit](audits/'+review['audit_id']+'.md).\n\n'
 sessions=[s for r in review['rows'] for s in r['sessions']];temps=[s['temperature_range_c'][1] for s in sessions if s['temperature_range_c']];gaps=[s['max_sample_gap_s'] for s in sessions if s['max_sample_gap_s'] is not None]
 text+='Maximum observed temperature: '+str(max(temps))+' °C; largest recorded sample gap: '+f'{max(gaps):.6f}'+' s. Temperature is telemetry, not a 42-°C start criterion. Uncorrected ECC, thermal/VRAM/power-setting limits, hardware-throttle mask, compute mode and concurrent-process observations are separate checks. Idle and software-power-cap bits are not treated as hardware faults. **Corrected ECC and continuous 24-hour stability: NOT MEASURED.** Windows include startup/idle/load; faults between samples cannot be ruled out.\n\n'
 text+='Historical R90/R113 bounded soaks retain their original 440-request/220-cycle evidence and zero reported process-VRAM growth, in their original profile scopes. Shared audit views are not independent new repetitions. '+link('R90')+' · '+link('R113')+'\n\n'
 text+='??? note "Original capture-level hardware evidence"\n\n'
 rows=[]
 for row in review['rows']:
  for s in row['sessions']:rows.append([link(row['experiment_id']),s['sample_count'],s['status'],s['temperature_range_c'],s['peak_vram_mib'],s['sampled_guard_violations']])
 text+=''.join(('    '+line if line else '')+'\n' for line in table(['Original experiment','Samples','Observed status','Temperature range °C','Peak device VRAM MiB','Guard violations'],rows).splitlines())
 text+='\n## Limits that remain explicit\n\n'
 text+='- **Terminal-Bench2.1: NOT MEASURED / TECHNICALLY BLOCKED.** The archived 89-task source gate is NO-GO for this local freeze campaign; reviewed container/evaluator/gateway admission and official-protocol execution are missing. No short test substitutes for it. [Gate and prerequisites](pipeline-methods.md).\n'
 diagnostics=agent('R534').get('quality_diagnostics')
 if diagnostics:
  text+='- **Agent safety versus format:** Gemma Agent33 has '+str(diagnostics['policy_violation_cases'])+' policy-violation cases and '+str(diagnostics['rejected_tool_call_events'])+' rejected tool-call events, with '+str(diagnostics['final_contract_failure_cases'])+' case failing the final-output contract. Repeated blocked calls are not independent failed cases or production writes. [Separate per-profile policy, parser, contract and semantic counts](configurations.md) retain the original replay and scores; zero recorded parser failures is not proof of valid arguments or safe decisions. '+link('R534')+'\n'
 text+='- **External evidence / EXTERN BELEGT:** published model cards, papers, source implementations and community measurements remain [source evidence](benchmark-register.md), never local score replacements or proof of a speedup cause.\n'
 text+='- **Unverified / NICHT VERIFIZIERT:** unattended production stability; global model superiority; automatic multi-model routing/switch costs; a heavier multi-agent harness; independently rebuilt binary equivalence; and exact public reproduction of private Agent33 inputs. R537 has only five paired role cases. '+link('R537')+'\n'
 text+='- Model-specific native templates, context/output, sampler, quantization, engine and harness settings remain part of every result. The shared HumanEval/32 canonical-reference anomaly is retained and disclosed; all 164 official tasks remain. These are declared local protocols, not publisher-protocol reproductions.\n'
 text+='- GPU counter energy covers declared request groups, including failures, not CPU/system energy. Counter brackets reflect query timing, not calibration confidence. Server generation timing is not TTFT; unavailable TTFT, prefill/decode or hardware values are not extrapolated.\n'
 text+='- R538 remains 167/199 PARTIAL at its original task limit. Historical budget conditions and old audits remain unchanged. No qualification is inferred from a build, CPU test, source release or experiment number.\n\n'
 text+='## Reproduction and release status\n\n[Export exact configuration packets and inspect the original main-engine source assets](reproduce.md). The controlled deployment proposal keeps the existing broker, one heavy GPU job, 1,200-second total TASK budget and 14,336-MiB device-memory guard. Original weights, production services and safety rules remain protected. **Proposal only: no production change or release approval is implied.** Independent source rebuilds and other forks retain their documented boundaries.\n\n'
 text+='The earlier console value 15,600 comes from the historical R118 `maximum_process_vram_mib` field, not the current broker device allowance. The active device guard remains 14,336 MiB; neither historical values nor present limits were rewritten. '+link('R118')+'\n\n'
 if issues:
  progress='#10/#11 retain broader issue histories; the current mission decision package has been reviewed with declared limits' if release else '#10/#11 remain finalization work'
  text+='Open GitHub snapshot: **'+str(sum(x.get('github_state')=='OPEN' for x in issues))+' open / '+str(sum(x.get('github_state')=='CLOSED' for x in issues))+' closed**. '+progress+'; #13 has completed parser checks but an unresolved causal explanation. #2/#3/#4/#8 retain technical source/model gates. Issue16 new-family qualification is active; issues17/18 begin with retained evidence and CPU analysis, not automatic GPU authorization. [All dispositions and evidence](questions.md). Workflow closure is not experimental qualification.\n\n'
 first_priority='Preserve the completed eight-family comparison and its explicit gates; no automatic new model or optimization campaign.' if scoped and scoped.get('status')=='EIGHT_FAMILY_COMPARISON_COMPLETE_WITH_EXPLICIT_GATES' else 'Complete the current admitted new-family comparisons and append a new evidence review; preserve this core baseline and all negative/partial results.'
 text+='## Remaining research priorities\n\n1. '+first_priority+'\n2. Official agent evaluator/container/gateway admission and a defensible full Terminal-Bench protocol/budget decision.\n3. Independent agent/security validation and measured recovery/switch/routing costs before widening Jarvis permissions or orchestration. Minimal-versus-complex harness work remains separately admitted; current CPU evidence does not establish a general winner.\n4. Remaining concrete matrix subcases or source/reproduction gaps only when their prerequisites and expected practical information gain justify a new isolated experiment.\n\n'
 hold=pipeline.get('publication_lock_observation',{}).get('observed_hold_window_s');events=pipeline.get('verified_capacity_events')
 text+='## Pipeline and freeze readiness\n\nMeasured publication-lock hold: '+str(hold)+' s (corrected). Verified capacity events: '+str(events)+'. Capacity-only wait remains **NOT MEASURED**; clock gaps are not relabeled GPU idle or cloud wait. [Original timing evidence](pipeline-performance.md).\n\n'
 text+='Research map: 130 original axes + 32 techniques; '+str(counts['experimentally_covered'])+' experimentally covered, '+str(counts['scientific_status']['QUALIFIED'])+' scoped qualified factors. Reviewed factors, GPU captures, category qualifications and reference pointers are different inventories. No 100% experimental-coverage claim.\n\n'
 if release:
  text+='The seven requested deliverables are available: role decisions; the complete comparison; positive/negative optimization evidence; exact configuration/source material; explicit gaps; safety/production status; and the November backlog. The original mission sections were reviewed against '+str(release['original_evidence_files_verified'])+' retained evidence files, with no new inference or rescoring. [Final mission gate](audits/'+release['audit_id']+'.md). The evidence cut-off is the actual26-October review, not a claimed31-October execution.\n\n'
  if release.get('new_results_need_separate_review'):
   text+='**Additional records now exist beyond this dated release.** The current master table remains available; this gate applies only to its retained original scientific snapshot, not to new profiles or a newly inferred winner.\n\n'
  text+='??? note "Completion scope and retained limits"\n\n'
  text+=''.join(('    '+line if line else '')+'\n' for line in table(['Mission section','Reviewed scope','Decision'],[[r['section'],r['scope'],r['status']] for r in release['requirements']]).splitlines())
  text+='\nScientific recommendations remain role-specific and bounded by the declared protocols. No official agent result, production approval, continuous uptime or independent bit-identical rebuild is established. Future measurements require a new audited release; original results and this release’s provenance remain preserved.\n'
 else:
  text+='This snapshot prepares the seven freeze deliverables: role decisions; the existing complete comparison; positive/negative optimization evidence; exact configuration/source material; explicit gaps; release status; and a prioritized backlog. **Final 31-October freeze audit is still pending.** Any new result must append audited evidence and preserve this snapshot’s provenance; dates do not authorize weaker gates or budget resets.\n'
 return text

def final_qualification_review(screening,history,experiments,frozen=None):
 """Artifact inventory and exact-run frontier; never pool configurations or infer missing scores."""
 from leaderboard import role_comparison
 notes={
 'R497':('REVIEWED','Canonical OmniCoder remains an alternative; compare R471/R478/R530 with the separately quantized bartowski artifact. Shared family names are not weight identity.'),
 'R487':('REVIEWED','Nexus native OFF/T0 has complete coding/tools and separate Agent33. Retain as an efficiency candidate; the original Thinking profile is separate.'),
 'R498':('DEFERRED','Slopus OFF has full coding/tools; Nexus OFF has better observed scores, latency and energy in both categories at the same peak-memory class. Additional agent qualification is deferred for current selection, not inferred agent inferiority.'),
 'R499':('DEFERRED','Opus Distill OFF has full coding/tools; the Qwen3.5 reference has better observed scores and lower latency, energy and VRAM in both categories. Unmeasured agent capability is unknown; further work requires a concrete specialist hypothesis.'),
 'R500':('REVIEWED','Ornith OFF/T0 has complete categories and Agent33; retain the observed latency/quality tradeoff without transferring scores from its earlier Thinking profile.'),
 'R501':('REVIEWED','Qwen3.5 remains the lower-memory comparison with complete coding/tools and Agent33; not excluded by parameter count or screening.'),
 'R502':('REVIEWED','Qwen3.8 MTP3 has full coding/tools and Agent33 as a separately captured profile. Earlier OFF BFCL partials do not become full results. Higher memory and task cost are material.'),
 'R503':('REVIEWED','Gemma nonthinking QAT has complete 8K coding/tools. Agent33 at16K is a different context profile and cannot fill the missing 8K agent cell. Retain coding-specialist evidence; no population safety claim.'),
 'R504':('DEFERRED','MiMo has full coding/tools. Lower-memory alternatives have stronger observed category quality and lower task cost. Missing Agent33 is unknown; restoring an evicted cache is not justified without an additional role-specific hypothesis.'),
 'R505':('DEFERRED','LFM8 has complete coding/tools but lower observed success than the efficient references in both categories. No inference about unmeasured agent quality; further qualification is deferred for this selection.'),
 'R506':('DEFERRED','LFM24 has a full6/200 parallel-tool result. Archived source/response analysis found214 calls, not a parser loss of extra calls. Coding remains NOT MEASURED; defer additional qualification for the current parallel-tool Jarvis role, not a coding incapability claim.'),
 'R507':('DEFERRED','Qwen3.6 BFCL R492 is137/157 PARTIAL, not a full200 score. The original budget and negative/partial evidence remain intact; no identical retry or restoration of an evicted artifact without a new justified hypothesis.'),
 'R508':('DEFERRED','Bonsai historical coding151/164 used2519.7547 seconds and is outside the current1200-second TASK envelope. Parallel tools R475 is145/171 partial. Simple400 is a different category. No transfer or automatic budget extension.'),
 'R514':('REVIEWED','Qwen0.8 now has full17/164 coding and79/200 tools. The low memory footprint is measured; weak16-case development scores were not used as a hard exclusion. Agent33 is NOT MEASURED.'),
 'R515':('REVIEWED','OmniCoder bartowski Q6 MTP OFF has full coding/tools and separately measured Agent33. MTP3 tool efficiency does not erase its coding/agent quality regressions.'),
 'R552':('REVIEWED','Ministral14 has full135/164 coding,163/200 tools and16/33 Agent33. Evaluate response-time/resource tradeoffs without claiming a general quality-preserving speedup.'),
 'R553':('DEFERRED_TOOLS','gpt-oss parser-compatible R583 coding150/164 is a separate build from R570 tools0/200. CPU/source diagnosis retains the singleton parallel-call grammar limitation. Final-code extraction was fixed; parallel tools were not. No score transfer or identical200-task retry.'),
 'R554':('REVIEWED','Ministral8 has full128/164 coding,153/200 tools and17/33 Agent33; all results retained. Compare lower task cost against measured quality and policy failures.'),
 'R555':('DEFERRED_TOOLS','Phi4 full coding134/164 retained. R569 tools3/32 is partial:1163.880 seconds response wall,12 length stops and raw repeated calls. CPU raw/structured review matches all32 replies; a new justified bridge/profile is needed before another full attempt.'),
 'R556':('REVIEWED','Devstral24 has full122/164 coding,175/200 tools and22/33 Agent33. Larger memory/task cost must buy role-specific quality; no general model rejection.'),
 'R557':('REVIEWED','Mistral Small3.2 has full129/164 coding and147/200 tools. The evicted weight cache does not invalidate results or establish a quality failure. Agent33 is NOT MEASURED.'),
 'R558':('REVIEWED_WITH_LIMIT','GLM default Thinking has full168/200 tools but coding36/44 partial after wrapper stop. R578/R581 nonthinking is separate; no profile merging or automatic repeat. Further default-profile coding is deferred under the current budget.'),
 'R577':('REVIEWED_WITH_LIMIT','GLM native nonthinking has full109/164 coding and154/200 tools. R581 includes recorded background relocation; observed resource costs are not a clean causal efficiency gain. Agent33 is NOT MEASURED.'),
 None:('TECHNICALLY_BLOCKED','Nemotron R562 reached the180-second startup gate before any task. No OOM was proven. The proposed startup extension is not authorized; keep the current guard and do not retry.')}
 profiles={p['runtime_configuration_id']:p for p in history['profiles']};rows=[]
 for item in screening['rows']:
  eid=item.get('experiment_id')
  if eid not in notes:raise ValueError('Candidate has no explicit qualification disposition')
  if eid is None and item['model']!='Nemotron-3-Nano-30B-A3B':raise ValueError('Unidentified candidate cannot inherit the Nemotron startup decision')
  status,reason=notes[eid];sha=item['configuration']['model_sha256'];seen=set();links=[]
  for r in history['runs']:
   if not r.get('official_eligible') or r['benchmark_id'] not in {'humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200'}:continue
   if profiles[r['runtime_configuration_id']]['model']['artifact_sha256']!=sha:continue
   key=(r['experiment_id'],r['runtime_configuration_id'],r['benchmark_identity_id'])
   if key in seen:continue
   seen.add(key);links.append('['+r['experiment_id']+': '+str(r['solved'])+'/'+str(r['tasks'])+'](configuration-profiles/'+r['runtime_configuration_id']+'.md)')
  reason=re.sub(r'\bR[1-9][0-9]{1,3}\b',lambda m:'['+m[0]+'](experiments/'+m[0]+'.md)',reason)
  rows.append([item['model'],sha[:12],status,'; '.join(links) or 'NOT MEASURED',reason])
 stage='Top-3 selection frozen; see [selected baselines](final-selection.md).' if frozen else 'Top-3 selection pending.'
 text='# Final model qualification — candidate review\n\n**Evidence through R585; '+stage+'** No production approval, exhaustive tuning campaign or new GPU run. Every inventory profile is shown; artifact-associated results below link to their exact original configurations and must not be pooled into one score. Duplicate GLM artifacts represent different Thinking profiles.\n\n'
 text+=table(['Inventory profile','Weight SHA256 prefix','Disposition','Complete official evidence — exact profiles','Decision / remaining limit'],rows)
 selection={'coding':[],'tools':[],'agents_development':[]}
 for role,bid in [('coding','humanevalplus-v0.1.10'),('tools','bfcl-v4-parallel-multiple-full200')]:
  selection[role]=sorted({r['experiment_id'] for r in history['runs'] if r.get('official_eligible') and r['benchmark_id']==bid},key=lambda e:int(e[1:]))
 selection['agents_development']=[e['id'] for e in experiments if e.get('aggregate_metrics',{}).get('native_validation33')]
 review=role_comparison(history,experiments,selection)
 text+='\n## All-qualified-profile comparison\n\n'+review['method']+' Historical runs outside the current TASK envelope remain historical evidence, not a newly feasible baseline. Throughput is not inferred from task wall time. Missing metrics remain unknown.\n\n'
 for category,group in review['categories'].items():
  text+='### '+category.title()+'\n\n'
  text+=table(['Exact run/profile','Success','Response s/task','GPU J/success bounds','Peak MiB','Observed frontier','Dominated by'],[[ '['+r['experiment_id']+' — '+r['model']+'](configuration-profiles/'+r['runtime_configuration_id']+'.md)',str(r['solved'])+'/'+str(r['tasks']),r['seconds_per_task'],str(r['energy_lower'])+'–'+str(r['energy_upper']) if r['energy_lower'] is not None else 'NOT MEASURED',r['peak_vram_mib'],r['pareto_status'],', '.join(r['dominated_by']) or '—'] for r in group['points']])
 text+='\n## Agent and safety limits\n\n'+str(len(review['agents_development']))+' authored Agent33 profiles are preserved separately in [qualified configurations](configurations.md). They are not Terminal-Bench, population safety rates or independent repetitions of33 unrelated tasks. Policy failures prohibit a production-safety claim. Official Terminal-Bench remains technically blocked by its retained execution-prerequisite gate.\n\n'
 text+='## Handoff\n\n'+('The three exact baseline packets are frozen in the [selection report](final-selection.md). ' if frozen else 'Finalize exactly three immutable baseline profiles only after reviewing these dispositions and configuration identities. ')+'Then address [Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17) and [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18): retained-trace/CPU analysis first, separately admitted harness experiments later. Harness changes must not contaminate this model-selection baseline. Community derivatives and source-only leads retain the versioned feasibility review in [open questions](questions.md); publisher claims are not local results.\n'
 return text

def render_final_selection(frozen,history):
 from leaderboard import validate_final_baselines
 validate_final_baselines(frozen,history)
 text='# Jarvis — three frozen model baselines\n\n**Dated research selection through R585; not production approval or a universal model ranking.** Three concrete configurations are retained for the next controlled harness phase. Official Agent benchmarks remain NOT MEASURED.\n\n'
 text+=frozen['selection_method']+'\n\n'
 rows=[]
 for s in frozen['selected']:
  p=s['baseline_packet']['profile'];c,t=s['benchmark_captures'];a=s['authored_agent_context'];m=a['result']
  mean=(100*c['solved']/c['tasks']+100*t['solved']/t['tasks'])/2
  rows.append(['['+p['model']['name']+'](configuration-profiles/'+s['baseline_runtime_configuration_id']+'.md)',s['role'],str(c['solved'])+'/'+str(c['tasks']),str(t['solved'])+'/'+str(t['tasks']),f'{mean:.2f}% ·2/3',str(m['solved'])+'/33; policy '+str(m['policy_gate_passes'])+'/33 ['+a['experiment_id']+'](experiments/'+a['experiment_id']+'.md)' if m else 'NOT MEASURED at selected8K'])
 text+=table(['Frozen model/configuration','Intended role','HumanEval+164','BFCL parallel200','User mean / official coverage','Separate authored Agent33'],rows)
 text+='The arithmetic mean is user-defined and unofficial; only the two complete official categories enter it. Agent33 is not the missing third official category. Original coding/tool capture IDs remain separate and preserve their adapters and audit hashes.\n\n'
 for s in frozen['selected']:
  text+='## '+s['role']+'\n\n'+s['rationale']+'\n\n'
  p=s['baseline_packet']['profile'];text+='Frozen runtime ID: `'+s['baseline_runtime_configuration_id']+'`. Weight SHA256: `'+p['model']['artifact_sha256']+'`.\n\n'
  text+=table(['Category','Original capture','Exact profile'],[[r['experiment_id'],'['+r['experiment_id']+'](experiments/'+r['experiment_id']+'.md)','['+r['runtime_configuration_id'][:16]+'…](configuration-profiles/'+r['runtime_configuration_id']+'.md)'] for r in s['benchmark_captures']])
  text+='Requested/native controls are preserved verbatim in the packet. In Nexus, the engine reasoning flag is recorded ON while native `enable_thinking=false` selects the OFF template; neither field is silently rewritten. Cache/graph flags are requests, not proof of executed kernels. Unknown metadata stays unknown.\n\n' if s['selection_id']=='efficient-worker' else ''
 text+='## Why the alternatives were not selected\n\nThese are role/resource decisions for this dated selection, not permanent bans. All exact runs, including losing variants, remain in the [candidate matrix and complete Pareto comparison](final-qualification.md).\n\n'
 alternatives=[
  ['Canonical OmniCoder','The bartowski artifact has134 vs132 coding,178 vs177 tools and28 vs26 authored agent successes. Canonical remains a lower-cost alternative; this is not a causal quantizer comparison.'],
  ['Qwen3.5 9B','Strong lower-VRAM alternative:135 coding,176 tools,23 local agents. Retained for resource-sensitive use; three role slots favor Omni for observed agent/tool outcomes and Nexus for worker latency/tool count. No global dominance claimed.'],
  ['Qwen3.8 27B','MTP3 has151 coding,169 tools and26 agents/policy31. Gemma has higher observed coding, Omni has higher tool/agent counts, and the27B profile uses substantially more VRAM. Its better observed policy count is retained, not called a proven safety advantage.'],
  ['Ornith1.5','Fast measured responses remain useful;117 coding,170 tools and18 agents are below the selected worker counts130/178/25. Tiny latency differences do not prove a population speed ranking.'],
  ['Slopus / Opus Distill','Complete OFF coding/tools remain archived. See the explicit observed category-quality/resource tradeoffs and deferred agent questions in the candidate matrix; screening was not the exclusion basis.'],
  ['MiMo / LFM8','Full categories are retained. Their observed quality/resource tradeoffs do not improve the selected role set; unmeasured Agent33 capabilities remain unknown.'],
  ['LFM24 / Qwen3.6 / Bonsai','Current parallel-tool result6/200, budget-limited partial suites, historical over-budget coding or missing applicable qualifications prevent replacing the measured role baselines. Exact technical reasons and reopening conditions remain in the candidate matrix.'],
  ['Qwen0.8','Full17/164 and79/200 confirm the low-memory/quality tradeoff. Lowest memory alone does not meet the selected coding/agent roles; no rejection from its small development screen.'],
  ['Ministral14 / Ministral8','Full categories and authored agents measured:135/163/16 and128/153/17. Useful low task-time/energy alternatives, but weaker observed tool/agent outcomes than the balanced profile. No quality-preserving speedup is inferred.'],
  ['Devstral24 / Mistral Small3.2','Full122/175 and129/147 coding/tools respectively; Devstral22/33 local agents. Current resource/quality tradeoffs do not improve the three roles. Missing Mistral agent quality remains unknown.'],
  ['GLM Flash','Default-thinking tools168/200, coding partial; native-off109/164 and154/200 is separate. High memory and the documented R581 resource confound limit an efficiency claim; no retry or profile pooling.'],
  ['Phi4','Coding134/164 is valid; current tool bridge produced repetition, length stops and3/32 partial within the task budget. Defer until a justified bridge/profile fix; no general model incapability claim.'],
  ['gpt-oss20B','Parser-fixed150/164 coding is retained. Gemma has better observed coding, time, energy and memory on the compatible full protocol. Parallel-tool grammar remains limited; old0/200 and new coding have different builds.'],
  ['Nemotron3 Nano','Startup180 gate was reached before tasks; no authorized extension, no proven OOM or quality score. Technically blocked rather than quality-rejected.'],
  ['Other quantizations, MTP and engine variants','Every exact profile remains visible. Tool-scoped OmniMTP3 wins do not erase its coding/agent regression gates; GemmaQ8-key coding regression is retained. Historical or partial variants cannot borrow missing categories from another build or context.'],
  ['Source-only derivatives / OxCoder','The pinned Issue16 feasibility/source review remains linked in open questions. No verified local advantage or unreviewed download is promoted. OxCoder stays stopped by owner instruction after weight-identity concerns; that is not a measured model-quality rejection.']]
 text+=table(['Alternative','Decision / scope'],alternatives)
 text+='## Architecture and handoff to Issues17/18\n\n'+frozen['architecture_decision']+'\n\n'
 text+='Begin with retained traces and CPU contract tests from [Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17), then the separately admitted lean-harness comparisons in [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18). Keep these frozen model baselines untouched; each harness or inference change gets its own profile and evidence. No exhaustive engine/MTP/quantization/kernel campaign is started by this selection.\n\n'
 text+='## Frozen data and limits\n\n[Download the three frozen baseline packets](https://raw.githubusercontent.com/Maxxxel/v100-volta-ai-optimization-lab/main/data/frozen-baselines.json). They contain ordered redacted launch arguments, environment, native sampling/template controls, model/build/library hashes and original benchmark references. They grant no execution authority; asset mapping and the existing broker are mandatory.\n\nSelection SHA256: `'+frozen['selection_content_sha256']+'`; frozen at `'+frozen['frozen_at_utc']+'`. New measurements append history and must not regenerate this dated freeze.\n\n'
 text+='\n'.join('- '+v for v in frozen['remaining_limits'])+'\n'
 return text

def reserved_harness_report(experiments):
 rows=[(e,e.get('aggregate_metrics',{}).get('native_lean_reserved_validation33')) for e in experiments]
 rows=[(e,r) for e,r in rows if r]
 if not rows:return ''
 fmt=lambda v,n=2:'NOT MEASURED' if v is None else format(v,'.'+str(n)+'f')
 value=lambda v:'NOT MEASURED' if v is None else str(v)
 text='## Reserved-fixture validation · retained minimal harness\n\n**33 reserved cases ·11 correlated authored families.** Each model retains its frozen8K profile. **Not an official leaderboard** or causal model/harness comparison; no population-equivalence claim.\n\n'
 data=[]
 for e,r in rows:
  assert r['dataset_id']=='jarvis-lean-holdout-20261027-v1' and r['official_benchmark'] is False and r['winner_qualified'] is False
  w=r['measured_work'];data.append(['['+e['id']+' · '+e['model']+'](experiments/'+e['id']+'.md)',str(r['solved'])+'/'+str(r['tasks']),str(r['tasks'])+'/'+str(r['planned_tasks'])+(' complete' if r.get('complete_capture') else ' PARTIAL'),str(r['policy_gate_passes'])+'/'+str(r['tasks']),value(w['input_tokens'])+' / '+value(w['output_tokens']),w['completed_model_calls'],fmt(r.get('case_wall_s')),fmt(r.get('gpu_j_per_success_lower'))+'–'+fmt(r.get('gpu_j_per_success_upper')),r.get('peak_device_vram_mib'),value(r.get('technical_preflight_cases'))+' / '+value(r.get('technical_request_errors'))])
 text+=table(['Frozen profile','Solved / observed','Case capture','Policy passes','Reported input / output tokens','Completed model calls','Task wall s','GPU J / success bounds','Peak MiB','Preflight / request errors'],data)
 text+='Policy failures are rejected proposals, not executed production actions. Failed cases remain in time/energy totals and available token usage. Token counts cover completed-response usage; unknown usage from failed requests is never estimated. Reasoning tokens: **NOT MEASURED** where response instrumentation is absent. NVML bounds are counter-query brackets, not statistical confidence intervals; model loading, warm-up and host CPU energy are excluded. Complete case capture does not mean every case reached inference: preflight failures are shown separately. No population-equivalence or optimized-harness adoption claim.\n\n'
 for e,r in rows:
  text+='<details markdown="1"><summary>'+e['id']+' · frozen configuration and evidence</summary>\n\n'
  text+='Context / output: '+str(r['context_tokens'])+' / '+str(r['max_output_tokens'])+' tokens. Captured cases: '+str(r['tasks'])+'/'+str(r['planned_tasks'])+'. Independent nonroot CPU replay verified retained replies and simulated effects.\n\n'
  for label,key in [('Model SHA256','model_sha256'),('Captured profile SHA256','profile_sha256'),('Frozen parent profile SHA256','parent_profile_sha256'),('Scorer SHA256','scorer_sha256')]:text+=label+': `'+r[key]+'`\n\n'
  for limit in r.get('preflight_limits',[]):text+='Context preflight: '+limit['reason']+' · '+str(limit['prompt_tokens'])+' observed prompt tokens + '+str(limit['max_output_tokens'])+' reserved output > '+str(limit['context_tokens'])+' frozen context (turn '+str(limit['turn'])+'). No context/output change or answer repair.\n\n'
  text+='Dataset: `'+r['dataset_id']+'`. Engine binary SHA256: `'+r['implementation']['engine_binary_sha256']+'`; template SHA256: `'+r['implementation']['template_sha256']+'`. Engine release version: **NOT RECORDED**; hashes are not version numbers. [Frozen sampling, thinking and model settings](final-selection.md).\n\n[Audit and original-capture hashes](experiments/'+e['id']+'.md).\n\n</details>\n\n'
 return text

def lean_harness_report(experiments,research=None):
 text='# Lean Jarvis harness\n\nMeasured harness trials and reserved validation. Frozen models and external tool permissions remain unchanged; all tools are offline simulators.\n\n'
 text+='**Keep the original minimal single-agent loop.** No tested rewrite qualified. No production deployment.\n\n'
 text+='<details markdown="1"><summary>Original architecture and candidate change point</summary>\n\nRejected candidates inserted a pure request rewrite before the frozen model. The selected reference uses no rewrite or additional agent role.\n\n```mermaid\nflowchart LR\n  B[Domain-scoped native request] --> M[Frozen local model]\n  M --> P[Deterministic external permission check]\n  P -->|allowed| T[Isolated tool simulator]\n  P -->|denied| H[Retained outcome and full history]\n  T --> H\n  H --> B\n```\n\n</details>\n\n'
 text+=reserved_harness_report(experiments)
 text+='## Controlled development ablations\n\nThese exposed development cases are **not official benchmarks or independent holdout validation**.\n\n'
 rows=[(e,(e.get('aggregate_metrics',{}).get('native_lean_harness_ablation') or e.get('aggregate_metrics',{}).get('native_lean_harness_screen'))) for e in experiments]
 for e,r in rows:
  if not r:continue
  assert not r['official_benchmark'] and not r['winner_qualified']
  screen=r.get('screen_only',False)
  tool_json=r['dataset_id']=='jarvis-lean-tool-json-ablation33-v1'
  toon=r['dataset_id']=='jarvis-original-caveman-toon-screen33-v1'
  node_shrink=r['dataset_id']=='jarvis-original-caveman-node-shrink-screen33-v1'
  display_arms=([r['stored_reference']['metrics']] if screen else [])+r['arms']
  fmt=lambda v,n=3:'NOT MEASURED' if v is None else format(v,'.'+str(n)+'f')
  text+='## '+r['experiment_id']+(' · original Caveman Node shrink · B-only screen' if node_shrink else ' · original Caveman TOON · B-only screen' if toon else ' · pre-action checklist · B-only screen' if screen else ' · compact tool-result JSON' if tool_json else ' · compact system instructions')+'\n\n'
  decision=r['comparison']['decision']
  text+=('**Decision: rejected — preregistered quality/policy gate failed.**' if decision=='REJECT_OBSERVED_QUALITY_OR_POLICY_REGRESSION' else '**Development result only — no promotion; independent confirmation required.**')+' Original tools, inference profile and scoring retained; '+('only tool descriptions in the exact ten reviewed catalogs change through the original Node compressor; messages, tool arguments, typed schemas and authoritative results remain unchanged, and unknown catalogs pass through unchanged.' if node_shrink else 'only tool-result representation changes through the original upstream stateless TOON codec, after exact structured roundtrip validation; unsupported outputs remain original.' if toon else 'a fixed checklist is added at public pre-action checkpoints.' if screen else 'only insignificant JSON whitespace outside tool-result strings changed.' if tool_json else 'only reviewed system prose changed.')+(' Current run:33 candidate cases; stored original-request control fromR587. **No new A0 run and no fresh paired GPU comparison.**' if screen else ' One model start, alternating AB/BA across33 paired cases /11 correlated task families.')+'\n\n'
  data=[]
  for a in display_arms:
   data.append([('reference · R587 stored' if screen and a['arm']=='reference' else a['arm']),str(a['solved'])+'/33',a['policy_violations'],a['total_tokens_reported'],fmt(a['case_wall_s']),fmt(a['GPU_j_per_success_lower'],2)+'–'+fmt(a['GPU_j_per_success_upper'],2),a['peak_sampled_device_vram_mib'],a['model_calls_attempted']])
  text+=table(['Arm','Solved','Policy violations','Input + output tokens','Task wall s','GPU J / success bounds','Peak MiB','Model calls'],data)
  if node_shrink and r.get('request_wrapper_source'):
   text+='[Exact request wrapper]('+r['request_wrapper_source']['file']+').\n\n'
  if node_shrink:
   overhead=r['codec_overhead'];text+='Original Node codec: '+str(overhead['catalog_visits'])+' catalog transformations; '+fmt(overhead['codec_wall_s'])+'s codec invocation wall, '+fmt(overhead['codec_parent_CPU_s'])+'s parent CPU, '+fmt(overhead['codec_children_CPU_s'])+'s child CPU. Already included in task wall; do not add twice. Host CPU energy: NOT MEASURED. Source `JuliusBrussee/caveman@9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4`, Apache-2.0; Node24.22.0. This is distinct from the rejected Go toolschema default.\n\n'
  c=r['comparison'];text+=('Case-matched historical-control outcomes: ' if screen else 'Paired outcomes: ')+str(c['paired_gained'])+' gained, '+str(c['paired_lost'])+' lost; '+str(c['new_policy_failure_cases'])+' new policy-failure cases. Token reduction '+fmt(c['token_reduction_percent'],2)+'%; task-wall reduction '+fmt(c['latency_reduction_percent'],2)+'%. These differences **do not qualify the candidate**.\n\n'
  text+='<details markdown="1"><summary>Measurement limits, hashes and exact source</summary>\n\n'
  text+='Reasoning tokens: **NOT MEASURED**. GPU-energy intervals bracket cumulative NVML counter readings, not confidence intervals or calibration error. Failed tasks remain in cost numerators; model loading, warm-up and host CPU energy excluded. No population-equivalence claim.\n\n'
  text+='Transformation CPU seconds (including preservation/audit): '+', '.join(a['arm']+' '+fmt(a['transform_cpu_s'],6) for a in display_arms)+'. Current run TASK phase: '+format(r['task_phase_s'],'.3f')+'s /1200s. Independent isolated CPU replay reproduced all'+str(r['case_executions'])+' outcomes without model inference.\n\n'
  if r.get('correction_audit_id'):text+='CPU postprocessing required a byte-identical readable plan binding and restored permissions on empty sandbox mountpoints. Failed CPU receipts remain preserved; no GPU rerun or scoring-rule change. [Correction evidence](audits/'+r['correction_audit_id']+'.md).\n\n'
  if r.get('implementation'):text+='Captured implementation: transform SHA256 `'+r['implementation']['transform_module_sha256']+'`; engine binary SHA256 `'+r['implementation']['engine_binary_sha256']+'`. Transport and simulator identities are retained in the [public experiment data](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/experiments.json). Source commit for the local transform: **not recorded at execution**; binary hashes are not version numbers. [Frozen model settings](final-selection.md).\n\n'
  if toon:text+='Original upstream commit `'+r['implementation']['upstream_commit']+'`; codec SHA256 `'+r['implementation']['codec_binary_sha256']+'`. Codec subprocess overhead is included in task wall time. Parent-only transformation CPU excludes child codec CPU; host CPU energy is **NOT MEASURED**. No byte-to-token estimates.\n\n'
  if toon:
   costs=r['codec_overhead'];text+='Measured codec subprocess wall '+fmt(costs['codec_wall_s'],6)+'s; parent CPU '+fmt(costs['codec_parent_CPU_s'],6)+'s; child CPU '+fmt(costs['codec_children_CPU_s'],6)+'s across '+str(costs['tool_result_visits'])+' tool-result visits. These component timings are already inside task wall; do not add them again.\n\n'
  if toon:text+='Warm-up separately: '+str(costs['warmup_model_calls'])+' calls, '+str(costs['warmup_input_tokens'])+' input / '+str(costs['warmup_output_tokens'])+' output tokens, '+fmt(costs['warmup_response_wall_s'],6)+'s response wall. Warm-up is outside TASK; no allocation to the reused historical reference.\n\n'
  if r.get('transform_source'):text+='[Exact measured request-transform source]('+r['transform_source']['file']+') · MIT; file SHA256 matches the captured module. Private fixtures and privileged runner code are not included.\n\n'
  text+='[Experiment and audit hashes](experiments/'+r['experiment_id']+'.md). Model SHA256: `'+r['model_sha256']+'`; captured profile SHA256: `'+r['profile_sha256']+'`; scorer SHA256: `'+r['scorer_sha256']+'`.\n\n'
  text+='</details>\n\n'
 for r in (research.get('screening32_runs') or ([research['screening32']] if research.get('screening32') else [])) if research else []:
  text+='## Frozen16 +16 development screen · '+r['experiment_id']+'\n\n'
  verdict='Rejected exact profile; not a qualified gain.' if r['decision'].startswith('REJECT') else 'Promising screen; not a qualified gain.'
  text+='**'+verdict+'** '+r['candidate_kind']+'. Stored R515 control: Coding '+str(r['categories']['coding']['reference_successes'])+'/16, Tools '+str(r['categories']['tools']['reference_successes'])+'/16; candidate: Coding '+str(r['categories']['coding']['candidate_successes'])+'/16, Tools '+str(r['categories']['tools']['candidate_successes'])+'/16.\n\n'
  fmt=lambda v:'NOT MEASURED' if v is None else format(v,'.3f')
  columns=['Profile','Input tokens','Completion tokens','TASK seconds','GPU J/success interval','Peak MiB']
  text+=table(columns,[[name,str(v['input_tokens']),str(v['completion_tokens']),fmt(v['task_wall_s']),fmt(v['GPU_j_per_success_lower'])+'–'+fmt(v['GPU_j_per_success_upper']),fmt(v['peak_device_vram_mib'])]for name,v in [('R515 original',r['reference']),(r['experiment_id']+' candidate',r['candidate'])]])
  change=lambda v:'NOT MEASURED' if v is None else format(-v,'+.3f')+'%'
  text+='Changes versus stored control: total tokens '+change(r['token_reduction_percent'])+'; TASK latency including captured rewrite '+change(r['task_latency_reduction_including_captured_transform_percent'])+'; conservative GPU J/success '+change(r['conservative_GPU_j_per_success_reduction_percent'])+'. A fresh controlled comparison and unseen confirmation are required before any promotion. [Audit](experiments/'+r['experiment_id']+'.md).\n\n'
  origin='This is a local prose rewrite, not upstream Caveman.' if r['experiment_id']=='R592' else 'This uses the original pinned Caveman instruction skill, not its model-assisted compressor or proxy. Rejection applies only to this exact tested profile.'
  text+='<details markdown="1"><summary>Scope and source hashes</summary>\n\n'+r['scope']+' Reasoning: NOT MEASURED. Captured transform CPU '+fmt(r['transform_cpu_s'])+'s; wall '+fmt(r['captured_host_transform_wall_s'])+'s. '+origin+' Comparison SHA256 `'+r['comparison_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('confirmation64'):
  r=research['confirmation64'];text+='## Fresh A/B confirmation · '+r['experiment_id']+'\n\n'
  verdict='Development-only latency advantage; unseen validation pending.' if r['decision'].startswith('CONFIRMED') else 'No qualified improvement; see audit.'
  if research.get('fresh_harness_validation_GPU'):verdict='Historical development candidate; subsequent R599 fresh validation rejected adoption.'
  quality=[]
  for arm,key in [('A','reference_successes'),('B','candidate_successes')]:quality.append(arm+': Coding '+str(r['categories']['coding'][key])+'/16, Tools '+str(r['categories']['tools'][key])+'/16')
  unchanged=all(v['gained']==v['lost']==0 for v in r['categories'].values())
  text+='**'+verdict+'** '+str(r['unique_tasks'])+' unique exposed tasks, '+str(r['requests'])+' requests, '+str(r['model_starts'])+' resident model. '+'; '.join(quality)+('; no changed task judgments.' if unchanged else '; per-case gains/losses retained in audit.')+'\n\n'
  fmt=lambda v:'NOT MEASURED' if v is None else format(v,'.3f')
  text+=table(['Arm','Reported tokens','Request E2E seconds','GPU J/success interval'],[[arm+' · '+label,str(v['total_tokens']),fmt(v['response_wall_s']),fmt(v['GPU_j_per_success_lower'])+'–'+fmt(v['GPU_j_per_success_upper'])]for arm,label,v in [('A','original',r['arms']['A']),('B','compact',r['arms']['B'])]])
  energy='**Energy saving NOT CONFIRMED**: counter timing brackets overlap.' if not r['energy_saving_confirmed_by_counter_bounds'] else 'Counter timing brackets support an energy reduction in this execution.'
  text+='Compact instruction variant: '+format(-r['request_latency_reduction_percent'],'+.3f')+'% summed request latency, '+format(-r['token_reduction_percent'],'+.3f')+'% input+completion tokens. '+energy+' Shared TASK '+fmt(r['shared_TASK_phase_s'])+'s /1200s; per-arm TASK time is not assigned. [R594 audit](experiments/R594.md).\n\n'
  text+='<details markdown="1"><summary>Fresh-control profile, timing scope and hashes</summary>\n\n'+r['scope']+' Reasoning tokens: NOT MEASURED. Native context '+str(r['context'])+'; requested output '+str(r['request_options']['max_tokens'])+'; temperature '+str(r['request_options']['temperature'])+'; seed '+str(r['request_options']['seed'])+'. Date '+r['at_utc']+'. Model SHA256 `'+r['model_sha256']+'`; profile `'+r['profile_sha256']+'`; comparison `'+r['comparison_sha256']+'`. Engine release version: NOT RECORDED; [frozen model/build reference](final-selection.md).\n\n</details>\n\n'
 if research and research.get('mini_swe_native_CPU'):
  c=research['mini_swe_native_CPU'];text+='<details markdown="1"><summary>Original mini-SWE core · native CPU compatibility</summary>\n\nOriginal version '+c['package_version']+' at `'+c['commit']+'`, native Python '+c['runtime']+': '+str(c['reference_cases'])+' archived reference cases and '+str(c['archived_callbacks'])+' request callbacks reproduced, with '+str(len(c['boundary_controls']))+' additional malformed-action/error/turn-limit controls. **Zero new GPU/model calls.** Original DefaultAgent manages native history; the frozen policy, simulator and scorer remain unchanged. This is not a stock-shell/provider benchmark. Single fixed-order CPU replay: reference '+format(c['baseline_CPU_seconds'],'.3f')+'s, controller '+format(c['controller_CPU_seconds'],'.3f')+'s; bootstrap '+format(c['bootstrap_CPU_seconds'],'.3f')+'s. No new token/call saving or GPU-efficiency claim. Evidence SHA256 `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('caveman_toon_pretask_failure'):
  c=research['caveman_toon_pretask_failure'];text+='## Original TOON integration · R597 failed before tasks\n\nModel loaded; **0 requests, no TASK phase**. Inner simulator rejected the candidate dataset ID; a separate CPU codec binding also used a CT path on the host. Lab integration defects, **no TOON quality or efficiency result**. Original failure retained; no retry of this job. Peak observed device memory '+str(c['peak_device_vram_mib'])+'MiB during loading. [Audit](experiments/R597.md), SHA256 `'+c['audit_sha256']+'`.\n\n'
 if research and research.get('caveman_proxy_record_GPU'):
  c=research['caveman_proxy_record_GPU'];text+='## Original Caveman record · native V100 comparison\n\n'
  text+=('Native compatibility confirmed on exposed development tasks.'if c['observed_task_judgments_unchanged']else'Task judgments changed; diagnosis required.')+' Pass-through control, no compression or qualified optimization. [R596 audit](experiments/R596.md).\n\n'
  fmt=lambda v:'NOT MEASURED'if v is None else format(v,'.3f')
  text+=table(['Arm','Coding','Tools','Reported tokens','Request E2E seconds','GPU J/success interval'],[[arm+' · '+label,str(c['categories']['coding'][key])+'/16',str(c['categories']['tools'][key])+'/16',str(c['arms'][arm]['total_tokens']),fmt(c['arms'][arm]['response_wall_s']),fmt(c['arms'][arm]['GPU_j_per_success_lower'])+'–'+fmt(c['arms'][arm]['GPU_j_per_success_upper'])]for arm,label,key in [('A','direct','reference_successes'),('B','record proxy','candidate_successes')]])
  text+='<details markdown="1"><summary>Record-mode profile and measurement limits</summary>\n\n32 exposed tasks,64 balanced requests, one unchanged resident model. Shared TASK '+fmt(c['shared_TASK_phase_s'])+'s /1200s; per-arm full TASK time not assigned. Run-wide peak VRAM '+fmt(c['run_peak_vram_mib'])+' MiB. Counter intervals are timing brackets, not confidence intervals. Reasoning tokens: NOT MEASURED. Date '+c['at_utc']+'. Model SHA256 `'+c['model_sha256']+'`; original proxy commit `'+c['proxy_commit']+'`; binary `'+c['proxy_binary_sha256']+'`; profile `'+c['profile_sha256']+'`; comparison `'+c['comparison_sha256']+'`. Engine release: NOT RECORDED; binary `'+str(c['engine_binary_sha256'])+'`; [frozen native model/build](final-selection.md). Context '+str(c['context'])+'; output '+str(c['request_options']['max_tokens'])+'; temperature '+str(c['request_options']['temperature'])+'; seed '+str(c['request_options']['seed'])+'. Shared warmup: '+str(c['warmup_requests'])+' requests, '+str(c['warmup_input_tokens'])+' native input tokens and '+str(c['warmup_completion_tokens'])+' output tokens, '+fmt(c['warmup_request_E2E_s'])+'s request E2E; never divided by arm. Remaining native non-TASK time is not assigned to task latency. No compressor, unseen validation, population-equivalence or cross-model qualification.\n\n</details>\n\n'
 if research and research.get('caveman_preinference_failure'):
  c=research['caveman_preinference_failure'];text+='<details markdown="1"><summary>R595 · preserved lab integration failure</summary>\n\nOne broker job attempt; zero model/GPU inference runs and no TASK phase. The lab adapter incorrectly read a host-only dataset path inside the restricted jail before model launch. This is not a Caveman/model quality result. [Original failure audit](experiments/R595.md), SHA256 `'+c['audit_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('caveman_proxy_record_CPU'):
  c=research['caveman_proxy_record_CPU'];text+='<details markdown="1"><summary>Original Caveman proxy · record-mode CPU compatibility</summary>\n\nThe full original proxy at `'+c['commit']+'` was built without source patches (CGO disabled) and executed unprivileged without external network or GPU devices. Six synthetic contracts passed: plain completion, tool arguments/schema, SSE streaming, upstream error, unauthorized request and unknown mount. Four forwarded request/response fixtures remained byte-identical; denied requests did not reach the fixture server. **Zero new GPU/model calls.** This verifies this local API fixture only; native engine, Harmony, compression and GPU efficiency remain unqualified. Binary SHA256 `'+c['binary_sha256']+'`; evidence `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('caveman_original_toon_CPU'):
  c=research['caveman_original_toon_CPU'];text+='<details markdown="1"><summary>Original Caveman TOON · upstream CPU tests</summary>\n\n'+str(len(c['tests_passed']))+' original tests passed: structural roundtrip, duplicate-key rejection, quoted strings, numeric lexical forms, deterministic encoding and unsupported-shape fallback. No fuzz campaign, model/GPU calls or local token-saving claim. Model interpretation and GPU efficiency remain unqualified. Evidence SHA256 `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
  if c.get('critical_data_contracts'):
   k=c['critical_data_contracts'];text+='<details markdown="1"><summary>TOON · critical-data CPU controls</summary>\n\n'+str(k['actually_transformed'])+' synthetic fixtures actually encoded and decoded with unchanged critical values; '+str(k['invalid_rejected'])+' ambiguous/invalid inputs rejected. Permissions, commands, numeric lexemes, provenance, errors and ordered data covered. This is structural preservation, not proof of LLM understanding. Evidence `'+k['evidence_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('fresh_harness_validation_GPU'):
  c=research['fresh_harness_validation_GPU'];fmt=lambda v:'NOT MEASURED'if v is None else format(v,'.3f')
  text+='## R599 · fresh preamble validation: rejected\n\nThe unchanged R594 candidate lost one coding case. Retain the minimal reference; the tied overall15/16 totals hide a category regression. [R599 audit](experiments/R599.md).\n\n'
  text+=table(['Arm','Coding','Tools','Input + output tokens','Request E2E seconds','GPU J/success bounds'],[[arm+' · '+label,str(c['categories']['coding'][key])+'/8',str(c['categories']['tools'][key])+'/8',str(c['arms'][arm]['total_tokens']),fmt(c['arms'][arm]['response_wall_s']),fmt(c['arms'][arm]['GPU_j_per_success_lower'])+'–'+fmt(c['arms'][arm]['GPU_j_per_success_upper'])]for arm,label,key in [('A','original','reference_successes'),('B','short preamble','candidate_successes')]])
  text+='Tokens −'+fmt(c['token_reduction_percent'])+'%; request E2E −'+fmt(c['request_latency_reduction_percent'])+'%. **Energy saving not confirmed. No adoption.**\n\n<details markdown="1"><summary>Fresh-case design, timing and evidence</summary>\n\n'+c['scope']+' Shared TASK '+fmt(c['shared_TASK_phase_s'])+'s /1200s; peak VRAM '+fmt(c['arms']['A']['peak_device_vram_mib'])+' MiB. Reasoning tokens and per-arm full TASK time: NOT MEASURED. All32 responses independently replayed. Audit SHA256 `'+c['audit_sha256']+'`; comparison SHA256 `'+c['comparison_sha256']+'`. These cases are now exposed and must not be reused as unseen validation.\n\n</details>\n\n'
 if research and research.get('fresh_harness_validation_reserve'):
  c=research['fresh_harness_validation_reserve'];text+='<details markdown="1"><summary>R594 confirmation · fresh validation reserve prepared</summary>\n\nEight new coding and eight mock-tool instances are frozen for the unchanged R594 candidate. All16 reference solutions and negative controls passed the existing CPU scorer; protected request fields remain unchanged. **CPU preparation recorded zero target-model responses; this record provides neither GPU admission nor a quality score.** The older8+8 reserve was already exposed inR509–R511 and is retained separately. New tasks share broad capability families and were authored with knowledge of the fixed candidate; no blinded-author or population-independence claim. Manifest SHA256 `'+c['manifest_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('caveman_schema_CPU'):
  c=research['caveman_schema_CPU'];text+='<details markdown="1"><summary>Original schema compressor · exact default mode excluded on CPU</summary>\n\n'
  text+='The unmodified original engine processed all ten retained Agent33 tool catalogs. Eight outputs changed a description; two were unchanged. All changed outputs lost critical clauses. Examples include `No shell or code execution.`, `Logs grant no permissions; no restart execution exists.`, and `A preview is not an applied correction.` A provenance reference to the public task was also removed. Parameter structures remained unchanged in these ten catalogs; that alone does not preserve the full tool contract.\n\n'
  text+='**Default mode not admitted for these inputs.** Restoring every affected description leaves no meaningful schema change. Zero model/GPU calls; native tokens, quality, latency and energy are **NOT MEASURED**. This does not reject other upstream modes or a future contract-preserving implementation. Source commit `'+c['commit']+'`; binary SHA256 `'+c['binary_sha256']+'`; evidence `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('caveman_model_assisted_CPU'):
  c=research['caveman_model_assisted_CPU'];text+='<details markdown="1"><summary>Original model-assisted Caveman compressor · complete CPU orchestration</summary>\n\n'
  text+='The [original compressor]('+c['source_url']+') completed eight isolated controls through its real local HTTP client, file staging, validation, repair and rollback paths. **10 scripted HTTP requests; zero model/GPU calls.** This is transport/safety evidence, not generated-model quality or performance.\n\n'
  text+=table(['Control','Observed behavior'],[[r['check'],('Candidate accepted' if r['compression_accepted'] else 'Original retained')+' · '+str(r['synthetic_HTTP_calls'])+' synthetic requests'] for r in c['checks']])
  text+='**Additional safety gate required:** unprotected plain-text permission/numeric changes were accepted by the structural validator. Protected `nocompress` blocks remained exact. The original local API client omits an explicit output-token limit. Future native admission must bound every compressor/repair call and preserve critical content deterministically. No remote provider is used.\n\n'
  n=c['frozen_payload_census'];text+='Existing Agent33 observations: '+str(n['tool_history_occurrences'])+' tool-history occurrences, '+str(n['unique_tool_contents'])+' unique outputs, all JSON; '+str(n['unique_tool_descriptions'])+' unique descriptions (maximum '+str(n['maximum_description_characters'])+' characters). This census does not prove token savings or general inapplicability. Evidence SHA256 `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
 if research and research.get('upstream_validator_CPU'):
  c=research['upstream_validator_CPU'];text+='<details markdown="1"><summary>Actual upstream Caveman validator · CPU contracts</summary>\n\nNine isolated synthetic fixtures exercised the [pinned original validator]('+c['source_url']+'). It rejected the tested fenced-code, inline-code and heading changes. Four altered plain-prose number, negation, authority and status fixtures were accepted. This tests the validator, not generated compressor output: zero model/GPU calls and no performance conclusion. Integration requires additional deterministic protection of critical fields. Upstream Caveman remains under evaluation. Evidence SHA256 `'+c['evidence_sha256']+'`.\n\n</details>\n\n'
 if research:
  text+='## Technique decisions\n\n**Retain the measured minimal reference.** No alternative has independently qualified against the quality/policy and efficiency gates. Technical reviews and deferred ideas are not GPU qualifications.\n\n<details markdown="1"><summary>Technique coverage, exclusions and source methods</summary>\n\n'
  text+=table(['Approach','Decision / scope'],[[r['technique'],r['status']+' — '+(r.get('evidence') or '')] for r in research['techniques']])
  text+='CPU checks reused160 prior one-shot requests: no tool-result history for JSON compression and no matching effect-tool pre-action trigger. The existing compact-system module rejects their distinct preambles; this is not a general rejection of new prompt hypotheses. Exact duplicate-read reuse found no eligible payload after state/error barriers across484 reference requests. These are applicability findings, not token or speedup measurements.\n\n'
  text+='The pinned default JSON-elision route found no eligible long array in the reviewed Omni histories (all136 arrays have1–4 elements). Original TOON was subsequently measured in R598 and rejected in that exact profile; original full proxy record-mode compatibility was measured in R596. Neither result qualifies compression or rejects every upstream mode.\n\n'
  for source in research['source_reviews']:
   text+='['+source['repository'].split('/')[-1]+' · pinned source]('+source['repository']+'/tree/'+source['commit']+') · `'+source['commit']+'`. '+source['status']+'. '+(source.get('scope') or '')+'\n\n'
  if research.get('frozen_reference'):
   ref=research['frozen_reference'];text+='Frozen next-goal reference: `'+ref['id']+'` · SHA256 `'+ref['reference_sha256']+'`. '+ref['next_goal_boundary']+'\n\n'
  text+='Original source-plan SHA256: `'+research['canonical_plan_sha256']+'`. Complete reviewed source identities and scoped decisions: [public snapshot](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/snapshot.json).\n\n</details>\n\n'
 text+='## Next gate\n\nRetain the original minimal reference: none of the tested alternatives passed the quality/policy and efficiency gates. No rejected components are combined. Reserved validation and model-specific technical limits are reported separately; no optimized harness has been adopted.\n\n[Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17) · [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18)\n'
 return text

def main():
 s=read('snapshot.json');fs=read('factors.json');es=read('experiments.json');audits={x['id']:x for x in read('audit-excerpts.json')};profiles=read('profiles.json');refs={x['id']:x for x in read('references.json')};models=read('models.json');counts=s['counts']
 put('lean-harness.md',lean_harness_report(es,s.get('lean_harness_review')))
 history=read('configuration-history.json');register=read('benchmark-register.json')
 categories=[('Coding','humanevalplus-v0.1.10',164),('Tools','bfcl-v4-parallel-multiple-full200',200),('Agents','terminal-bench-2.1',89)]
 cards=[]
 for label,bid,n in categories:
  runs=[r for r in history['runs'] if r['benchmark_id']==bid and r['official_eligible'] is True and r['tasks']==n and r['status']!='PARTIAL']
  latest=max(runs,key=lambda r:int(r['experiment_id'][1:])) if runs else None
  if latest:
   score=f"{latest['solved']}/{latest['tasks']}";name=latest['model_name'];target='configuration-profiles/'+latest['runtime_configuration_id']+'/';note='Latest complete result · '+latest['experiment_id']
  else:score='Not measured';name='Evaluator admission pending';target='configuration-comparison/';note='No local score claimed'
  cards.append(f'<a class="lab-result" href="{target}"><span>{label}</span><strong>{score}</strong><b>{html.escape(name)}</b><small>{note}</small></a>')
 status_html=''.join('<span><strong>'+str(counts['scientific_status'].get(k,0))+'</strong> '+label+'</span>' for k,label in [('QUALIFIED','Qualified'),('TESTED_NEGATIVE','Negative'),('PARTIAL','Partial'),('OPEN','Open'),('DEFERRED','Deferred'),('NOT_APPLICABLE','Not applicable')])
 issue16_active=any(x.get('status')=='ACTIVE_OWNER_AUTHORIZED_NEW_FAMILY_SCREENING' for x in read('research-issues.json'))
 phase_notice='**Current phase: new model-family screening.** The previous Best-of-V100 decision is a reference baseline. Jarvis integration is deferred while [issue16 candidates](questions.md) pass the existing [screening protocol](screening.md).' if issue16_active else ''
 if (P/'data/frozen-baselines.json').exists():phase_notice='**Model selection frozen through R585:** [OmniCoder allround · Gemma coding · Nexus worker](final-selection.md). [All candidate decisions](final-qualification.md). Next: separately scoped lean-harness research (#17/#18); no production deployment or exhaustive inference-tuning campaign.'
 overview=f'''# V100 Volta AI Optimization Lab

<p class="lab-eyebrow">Independent research · NVIDIA Volta / SM70</p>
<p class="lab-lead">Better local AI on one Tesla V100-SXM2 with 16 GB HBM2. We measure model quality, useful speed and GPU energy — with reproducible configurations and retained negative results.</p>

<div class="lab-actions"><a class="lab-button lab-primary" href="configuration-comparison/">Compare models</a><a class="lab-button" href="archive/">Explore the research</a></div>

<div class="lab-kpis"><div><strong>162</strong><span>Research factors</span><small>130 original + 32 techniques</small></div><div><strong>{counts['experimentally_covered']}</strong><span>Experimentally covered</span><small>Factors, not GPU run count</small></div><div><strong>{counts['scientific_status']['QUALIFIED']}</strong><span>Qualified factor scopes</span><small>Workload-specific evidence</small></div><div><strong>16 GB</strong><span>HBM2 on one V100</span><small>One GPU benchmark at a time</small></div></div>

## Research pipeline

{phase_notice}

[Best-of-V100 research decision](best-of-v100-2026.md) · [Screening](screening.md) → [Official qualification](configuration-comparison.md) → [Targeted optimization](configurations.md). Development screens stay outside official scores.

## Model comparison

<div class="lab-results">{''.join(cards)}</div>

Latest complete category measurements, not a ranking. [All configurations, costs and audits](configuration-comparison.md).

## Optimization findings

<div class="lab-links"><a href="configurations/"><strong>Prefix reuse</strong><span>Lower latency with repeated context; not a universal decode gain.</span></a><a href="configurations/"><strong>HBM conversion cache</strong><span>Qualified prefill profiles with additional VRAM cost.</span></a><a href="configurations/"><strong>Energy profiles</strong><span>Measured trade-offs between task latency, memory and GPU joules.</span></a></div>

## Research progress

<div class="lab-status">{status_html}</div>

Reviewed, experimentally covered and qualified are separate stages. [Matrix and evidence](matrix.md) · [Open questions](questions.md).

<details><summary>Snapshot and methodology</summary>

Revision **{s['matrix_revision']}** · {s['source_date'][:10]}. {counts['sprint_records']} sprint records, {counts['reference_records']} immutable references and {counts['qualified_profile_pointers']} scoped Champion pointers are separate inventories, not a count of independent GPU runs.

Benchmark task phase: **1,200 seconds total**, shared across all parts. Startup, wrapper and CPU evaluation limits are separate. Historical measurements retain their original conditions. [Methods](methodology.md) · [Hardware](hardware.md) · [Reproduce](reproduce.md).

</details>

Independent community project; no affiliation with NVIDIA, Ollama or model publishers. Local measurements, external evidence and unverified hypotheses remain distinct. No universal winner is claimed.
'''
 put('index.md',overview)
 readme=re.sub(r'href="([^":]+)"',lambda m:'href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/'+m.group(1)+'"',overview)
 readme=re.sub(r'\]\(([^):]+\.md)\)',lambda m:'](docs/'+m.group(1)+')',readme)
 readme+='\n## Documentation and collaboration\n\nBuild with `pip install -r requirements-docs.txt` and `mkdocs build --strict`. [Contribute](CONTRIBUTING.md) · [Reproduce](docs/reproduce.md) · [German overview](docs/de.md). Publishing never launches a GPU job.\n'
 (P/'README.md').write_text(readme)
 put('hardware.md','# Hardware & scope\n\nOne NVIDIA Tesla V100-SXM2 ·16 GB HBM2 ·Volta SM70. Serialized local inference with recorded model, engine and kernel identities.\n\n- CUDA12.8 compiler baseline; driver580.178.04 recorded per run. Compiler, toolkit and loaded runtime identities remain distinct.\n- FP16 Tensor Cores; native BF16/FP8 Tensor Cores, cp.async and TMA are not assumed.\n- Attention KV, recurrent state, graphs and caches share the device memory budget.\n- Temperature is telemetry; existing ECC, VRAM, power, thermal and restore guards remain mandatory.\n\n[Reproduce](reproduce.md) · [Safety and admission](broker-admission.md)\n')
 put('methodology.md','''# Research methodology

**Current task budget:1,200 seconds total per benchmark**, shared across all parts without resets. Startup, wrapper, cleanup and CPU evaluation limits are separate. Older900-second experiments keep their historical conditions.\n\nGolden Baseline A0 is immutable per reproducible workload identity. Current Champion C is the best independently qualified configuration in that same profile. New candidate B first runs a cheap screen against valid stored references; only promising or materially uncertain cases receive fresh controls. Balanced sequences are used when drift or small differences justify them.

Pre-register the primary metric, practical improvement threshold, quality/numerical gates, maximum time and early-stop rule. Reject on quality or correctness loss regardless of synthetic speed. Keep failures, incomplete screens and outliers under their original rules.

Separate GPU/engine throughput, numerical kernel correctness, coding, native tool calling, isolated agent tasks and hardware telemetry. Use exact input IDs within one tokenizer; across models use the same tasks with correct templates and successful tasks per second/joule.

Prefill, decode, streaming TTFT, total task latency, device/process VRAM and GPU-energy integrals are different quantities. Buffered output does not measure visible TTFT. GPU energy excludes CPU/host energy unless explicitly stated. HBM-internal electrical energy cannot be identified from board-level NVML alone.

The audited `task_phase_s` includes input/template/token preparation between requests. The sum of completed HTTP windows is separate. Recorded `startup_s` starts at the protected broker clock and can include asset checks, model loading and warmups; it is not a pure model cold-start measurement. An interrupted trailing request is excluded from completed-request energy and latency summaries unless an explicit whole-window measurement says otherwise.

The original twelve quality tasks remain unchanged. HumanEvalPlus uses joint base AND plus success; a larger auxiliary count is not the same score. Repeated observations within one process do not establish independent sessions or broad model superiority. Frozen development suites are not unseen holdouts.

Official percentage admission must match the recorded numerator and denominator. A complete BFCL v4 Simple Python category uses its own AST-accuracy metric over all 400 unique official tasks; it is separate from the BFCL overall leaderboard and the historical static100 pilot. The metric adapter alone admits no model result: pinned scorer/configuration identities, complete coverage, controls and independent audit evidence are still mandatory. Missing results remain NOT MEASURED.

Native broker campaigns use their frozen data contracts and captured launch/profile receipts; no preflight plan is invented retrospectively. Full coding result export verifies all 164 unique tasks, every bounded part and scorer output, unchanged model/runtime configuration, and measured task costs. A complete local result still requires a separate official-API qualification before entering the official local highscore view. Partial campaigns retain actually scored task subsets in the research archive, with their original denominators and PARTIAL status; the central comparison admits only complete qualified category results. Unfinished or uncollected tasks are not zero; no full-suite official admission is implied.

## Status semantics

'''+table(['Status','Meaning'],[['QUALIFIED','Independently confirmed only within the named scope'],['TESTED_NEGATIVE','Valid test without sufficient benefit or with quality loss'],['PARTIAL','Only specified variants/components tested'],['OPEN','Insufficient technical or experimental evidence'],['DEFERRED','Specific documented prerequisite/cost blocks execution'],['NOT_APPLICABLE','Architecture, hardware or task mismatch']])+'''\nExperimental coverage is an independent boolean. A status decision, review, build or download is not a GPU intervention. Component coverage does not imply OmniCoder2 model coverage.\n''')
 rows=[]
 for f in fs:
  ident=f['id'];rows.append([f'[{ident}](factors/{ident}.md)',title(f),f['status'],'YES' if f['experimentally_covered'] else 'NO',f['priority']])
  sources=f['primary_sources'] or ['https://docs.nvidia.com/cuda/volta-tuning-guide/index.html','https://github.com/ggml-org/llama.cpp']
  details='# '+ident+' — '+title(f)+'\n\n'+table(['Scientific status','Experimental coverage','OmniCoder2 coverage','Priority'],[[f['status'],f['experimentally_covered'],f['omnicoder2_experimentally_covered'],f['priority']]])
  details+='\n## Theory and Volta implications\n\n'+rationale(f)+'\n\nOn SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.\n'
  details+='\n## Scientific background\n\n'+('\n'.join('- '+u for u in sources))+'\n\nThese are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.\n'
  details+='\n## Implementation and evidence\n\n'+(f['coverage_scope'] or 'See the exact original audit scope; no universal model/engine compatibility claim.')+'\n\n'
  for aid in f['evidence_ids']:details+=f'- [Original audit hash and public excerpt](../audits/{aid}.md)\n'
  if f['variants']:
   details+='\n'+table(['Original variant','Signed historical state','Reviewed scoped status','Hardware coverage in this variant'],[[v['value'],', '.join(v['historical_signed_states']),v['scope_status'] or 'See linked original evidence',v['experimental_coverage'] if v['experimental_coverage'] is not None else 'Not separately reconciled'] for v in f['variants']])
  details+='\n### Recorded model-specific variant coverage\n\n'+pretty(f.get('per_model_original_coverage',[]))+'\nHistorical states and window signatures are evidence links, not qualification of every model/variant.\n'
  details+='\n## Available results\n\nValues, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.\n\n'
  for v in f['variants']:
   if v.get('aggregate_metrics'):details+='\n### Variant '+v['value']+'\n\n'+pretty(v['aggregate_metrics'])
  details+='\n## Decision and remaining research\n\n'+(f['decision'] or 'No conclusive decision recorded.')+'\n\n**Remaining scope:** '+(f['remaining_scope'] or 'No additional concrete treatment identified; not proof that every imaginable variant is exhausted.')+'\n\n**Reopening condition:** '+(f['reopening_conditions'] or 'A distinct compatible intervention and independent evaluation contract are required.')+'\n\n**Next action:** '+(f['next_action'] or 'No new GPU job admitted.')+'\n\nThese canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.\n'
  if f.get('scope_reassessment'):
   details+='\n## Deferral scope reassessment — 2026-10-22\n\nThis is a source/evidence review, not a new GPU experiment.\n\n'+table(['Field','Assessment'],[[k.replace('_',' '),v] for k,v in f['scope_reassessment'].items()])
  if f['experiment_ids']:details+='\n## Related sprint records\n\n'+', '.join(f'[{e}](../experiments/{e}.md)' for e in f['experiment_ids'])+'\n'
  put('factors/'+ident+'.md',details)
 put('matrix.md','# Optimization matrix\n\n130 original factors plus 32 additional technique subcases; model candidates, research sources and signed test windows are separate inventories. Each row links to theory, evidence, variants, decisions and reopening conditions.\n\n'+table(['ID','Technique','Status','Experimentally covered','Priority'],rows))
 for aid,a in audits.items():
  put('audits/'+aid+'.md','# Public audit excerpt\n\nOriginal SHA256: `'+a['original_sha256']+'`\n\nOriginal file: `'+a['original_filename']+'`; '+str(a['original_bytes'])+' bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.\n\n'+pretty(a['statements'])+'\n## Selected aggregate measurements\n\n'+(pretty(a['aggregate_metrics']) if a['aggregate_metrics'] else 'NOT MEASURED / not included in the approved public schema.\n'))
 put('archive.md','''# Research archive

All original experiments, failures, configurations and audit identities remain available. Structured evidence opens on demand.

<div class="lab-links"><a href="../matrix/"><strong>Optimization matrix</strong><span>130 original factors +32 research techniques; scope, status and next questions.</span></a><a href="../results/"><strong>Experiment history</strong><span>Measured results, partial runs and original audit references.</span></a><a href="../configurations/"><strong>Qualified configurations</strong><span>Scoped winners with performance, quality and memory limits.</span></a><a href="../rejected/"><strong>Negative results</strong><span>What failed, why, and what could justify revisiting it.</span></a><a href="../configuration-archive/"><strong>Configuration history</strong><span>All profiles, historical subsets and attempts outside the complete-only comparison.</span></a><a href="../sources/"><strong>Papers and sources</strong><span>Pinned publications, implementations and evidence classifications.</span></a></div>

[Model research](models.md) · [OmniCoder derivatives](omnicoder-derivatives.md) · [Weight identity](weight-integrity-same-quantizer.md) · [Compatibility](compatibility.md) · [Open questions](questions.md) · [Roadmap](roadmap.md)
''')
 erows=[]
 registered_runs=read('configuration-history.json')['runs']
 for e in es:
  erows.append([f"[{e['id']}](experiments/{e['id']}.md)",', '.join(e['factor_ids']),e['evidence_status'],e.get('model')])
  text='# '+e['id']+'\n\n'+table(['Date','Factors','Model','Evidence state'],[[e.get('date'),', '.join(e['factor_ids']),e.get('model'),e['evidence_status']]])+'\n## Research question, decision and limits\n\n'+pretty(e['statements'])+'\n## Available aggregate results\n\n'+(pretty(e['aggregate_metrics']) if e['aggregate_metrics'] else 'NOT MEASURED / not recorded in this public projection.\n')
  measured=[r for r in registered_runs if r['experiment_id']==e['id']]
  if measured:
   text+='\n## Registered benchmark results\n\nThese are immutable historical measurement/admission views, not additional GPU runs. Partial denominators are not extrapolated to full benchmarks; missing costs stay unknown.\n\n'+table(['Benchmark / protocol identity','Status','Solved / evaluated','Configuration','Audit'],[[r['benchmark_id']+' / '+r['benchmark_identity_id'],r['status'],str(r['solved'])+'/'+str(r['tasks']),f"[Exact profile](../configuration-profiles/{r['runtime_configuration_id']}.md)",', '.join(f"[Proof](../audits/{aid}.md)" for aid in r['audit_ids'])] for r in measured])
  if e.get('independent_review'):
   review=e['independent_review'];text+='\n## Independent review and scope correction\n\n'+pretty(review.get('statements',{}))+'\n\n[Independent review audit excerpt](../audits/'+review['audit_id']+'.md)\n'
  confirmation=e.get('aggregate_metrics',{}).get('native_tools_confirmation')
  if confirmation:
   text+='\n## Fresh tool-specific MTP confirmation\n\n'+confirmation['decision']+'\n\nOne shared1,200s task budget includes both startups and warmups. Complete/partial counts are per arm; there is no pooled400-task BFCL score or global Champion.\n\n'
   text+=table(['Arm','MTP','Original tool tasks','AST solved','Protocol valid','Response seconds','Completion tokens','GPU J / success, bounds'],[[v['arm'],v.get('MTP','NOT MEASURED'),v['tasks'],v['solved'] if v['solved'] is not None else 'NOT MEASURED',v.get('protocol_valid','NOT MEASURED'),round(v['response_wall_s'],3) if 'response_wall_s' in v else 'NOT MEASURED',v.get('completion_tokens','NOT MEASURED'),str(round(v['GPU_j_per_success_lower'],2))+'–'+str(round(v['GPU_j_per_success_upper'],2)) if v.get('GPU_j_per_success_lower') is not None else 'NOT MEASURED'] for v in confirmation['arms']])
   text+='\n'+confirmation['scope']+'\n\nMeasured comparisons and immutable identities remain in the collapsed evidence above.\n'
  retrospective=e.get('aggregate_metrics',{}).get('native_role_comparison_development',{}).get('retrospective')
  if retrospective:
   text+='\n## Retrospective harness costs\n\nExisting R537 measurements: five paired exposed development cases, not an H0/H1 ablation or official benchmark. Input tokens include recurrent history; separate preamble/reasoning costs and compaction events remain **NOT MEASURED**.\n\n'
   text+='<details class="lab-evidence"><summary>Per-case costs: 15 executions / 5 paired cases</summary>\n<div class="screening-wrap"><table id="harness-retrospective"><thead><tr>'+''.join('<th>'+c+'</th>' for c in ['Case','Arm','Success','Policy','Calls','Input tokens','Output tokens','Seconds','GPU J, bounds','Simulator callbacks'])+'</tr></thead><tbody>'
   for row in retrospective['rows']:
    values=[row['case'],row['arm'],'PASS' if row['success'] else 'FAIL','PASS' if row['policy_pass'] else 'FAIL',row['model_calls'],row['reported_prompt_tokens'],row['completion_tokens'],round(row['case_seconds'],3),str(round(row['GPU_j_lower'],2))+'–'+str(round(row['GPU_j_upper'],2)),row['simulator_callbacks']]
    text+='<tr>'+''.join('<td>'+html.escape(str(v) if v is not None else 'NOT MEASURED')+'</td>' for v in values)+'</tr>'
   text+='</tbody></table></div>\n</details>\n\n'+retrospective['scope']+' Source identities and stable case hashes remain in the aggregate evidence above.\n'
  if e.get('qualification_review'):
   decision=e['qualification_review']
   text+='\n## Qualification decision\n\n**'+str(decision['decision'])+'**\n\n'+decision['scope']+'\n\n[Qualification evidence](../audits/'+decision['audit_id']+'.md)\n\n'+'<details class="lab-evidence"><summary>Predeclared gates and measured comparisons</summary>\n<pre><code>'+html.escape(json.dumps(decision,ensure_ascii=False,indent=2))+'</code></pre>\n</details>\n'
  if e.get('coding_mtp_comparison') or e.get('tools_mtp_comparison'):
   dev=e.get('coding_mtp_comparison') or e['tools_mtp_comparison'];tools=bool(e.get('tools_mtp_comparison'));label='tool' if tools else 'coding'
   text+='\n## '+('Tool' if tools else 'Coding')+' quality versus speed\n\n**The official benchmark score is valid. It does not qualify an optimization winner.**\n\n'
   text+=table(['Profile','BFCL parallel_multiple200' if tools else 'HumanEval+','Response seconds','Task seconds','Peak VRAM MiB','GPU J/success, bounds'],[[p['experiment_id'],str(p['solved'])+'/'+str(p['tasks']),round(p['response_wall_s'],3),round(p['task_phase_s'],3),p['peak_device_vram_mib'],str(round(p['GPU_j_per_success_lower'],2))+'–'+str(round(p['GPU_j_per_success_upper'],2))] for p in dev['profiles']])
   text+='\nPredeclared '+label+' nonregression gate: **'+('passed' if dev['quality_gate_passed'] else 'failed')+'**. '+dev['scope']+'\n\n[Paired comparison audit](../audits/'+dev['audit_id']+'.md)\n'
  if e.get('mtp_confirmation'):
   dev=e['mtp_confirmation']
   text+='\n## Fresh controlled MTP confirmation\n\n**Development evidence. Not an official benchmark score or Champion.** Same32 tasks per arm; one task clock including both startups/warmups: '+str(round(dev['single_task_clock_s'],3))+' seconds.\n\n'
   text+=table(['Arm','Coding /16','Mock tools /16','Response seconds','Arm incl. setup seconds','Peak VRAM MiB','Response GPU J/success, bounds'],[[p['arm'],p['coding_successes'],p['tool_successes'],round(p['response_wall_s'],3),round(p['arm_including_setup_s'],3),p['peak_device_vram_mib'],str(round(p['GPU_j_per_success_lower'],2))+'–'+str(round(p['GPU_j_per_success_upper'],2))] for p in dev['arms']])
   text+='\n'+dev['scope']+'\n\nNext: '+dev['next_action']+'\n\n[Comparison audit](../audits/'+dev['audit_id']+'.md)\n\n<details><summary>Draft counters, identities and metrics</summary>\n\n'+pretty(dev)+'\n</details>\n'
  if e.get('mtp_development_comparison'):
   dev=e['mtp_development_comparison']
   text+='\n## MTP development comparison\n\n**Locally measured development evidence; fresh confirmation pending. No official score or Champion.**\n\n'
   text+=table(['Profile','Coding /16','Mock tools /16','Task seconds','Peak VRAM MiB','GPU counter J, bounds'],[[p['experiment_id'],p['coding_solved'],p['tools_solved'],round(p['task_phase_s'],3),p['peak_device_vram_mib'],str(p['counter_lower_j'])+'–'+str(p['counter_upper_j'])] for p in dev['profiles']])
   text+='\n'+dev['scope']+'\n\nNext: '+dev['next_action']+'\n\n[Comparison evidence](../audits/'+dev['audit_id']+'.md)\n'
  if e.get('development_comparison'):
   text=text.replace('\n## Available aggregate results\n\nNOT MEASURED / not recorded in this public projection.\n','')
   dev=e['development_comparison']
   text+='\n## Controlled development comparison\n\n**Development evidence only; excluded from official benchmark rankings and averages.** '+str(dev['completed_requests'])+'/'+str(dev['planned_requests'])+' requests; '+str(dev['matched_base_tasks'])+' complete A/B/C task triples.\n\n'
   rows=[]
   for arm in dev['arms']:
    code,tools=arm['coding'],arm['tools']
    rows.append([arm['arm'],'On' if arm['thinking_requested'] else 'Off',arm['temperature'],str(code['successes'])+'/'+str(code['completed']),str(tools['successes'])+'/'+str(tools['completed']),round(code['completed_request_wall_s']+tools['completed_request_wall_s'],3),code['completion_tokens']+tools['completion_tokens'] if code['completion_tokens'] is not None and tools['completion_tokens'] is not None else None])
   text+=table(['Arm','Thinking requested','Temperature','Coding','Mock tools','Completed HTTP seconds','Completion tokens'],rows)
   text+='\nA→B changes only Thinking; B→C changes only temperature. Output cap '+str(dev['arms'][0]['max_output_tokens'])+', context '+str(dev['context'])+'. Actual task phase '+str(round(dev['task_phase_s'],3))+' s; shared cap '+str(dev['task_limit_s'])+' s. Peak VRAM '+str(dev['peak_device_vram_mib'])+' MiB. HTTP duration includes inference request costs; it is not a decode-only or TTFT measurement.\n\nFaster responses alone do not qualify an optimization. Small development counts cannot establish population quality or noninferiority; independent official confirmation remains necessary.\n\n<details><summary>Energy, output completion and immutable identities</summary>\n\n'+pretty(dev)+'\n</details>\n'
  if e.get('factor_mapping_correction'):
   text+='\n## Scientific mapping correction\n\nThe original audit and its hash remain unchanged. The current tested-factor assignment corrects earlier metadata; related cache settings are not separate isolated interventions.\n\n'+pretty(e['factor_mapping_correction'])
  if e.get('source_package'):
   text+='\n## Library source identity\n\nOnly metadata and checksums are public. Proprietary library binaries and license files remain outside this repository.\n\n'+pretty(e['source_package'])
  if e.get('audit_id'):text+='\n[Original audit SHA and selected excerpt](../audits/'+e['audit_id']+'.md)\n'
  related=[x for x in e.get('related_audit_ids',[]) if x!=e.get('audit_id') and (not e.get('independent_review') or x!=e['independent_review'].get('audit_id'))]
  if related:text+='\nRelated scoped evidence: '+', '.join('[audit excerpt](../audits/'+x+'.md)' for x in related)+'\n'
  if e.get('reference_A0'):text+='\nA0 reference ID: `'+e['reference_A0']+'`.\n'
  text+='\nDo not infer a new hardware intervention, successful quality gate or champion from an experiment number. Exact inputs and private task outputs are withheld; missing configuration fields remain unverified publicly.\n'
  put('experiments/'+e['id']+'.md',text)
 put('results.md','# Experiment results\n\nEvery scientifically catalogued sprint and signed historical window is preserved as metadata. Ledger events are available in the public dataset; payloads and private logs are omitted. Missing old sprint records are not invented.\n\n'+table(['Sprint','Factors','Audit verification','Model'],erows)+'\n## Historical signed windows\n\n'+table(['Window','Factor','Result','Audit excerpt'],[[w['id'],w.get('factor_id'),w.get('status'),f"[Evidence](audits/{w['audit_id']}.md)" if w.get('audit_id') else 'Not publicly linked'] for w in read('signed-windows.json')]))
 cr=[]
 for profile in profiles:
  if not profile['C']:continue
  a=refs[profile['C']];cr.append([f"[{profile['id']}](#profile-{profile['C'][:12]})",a['experiment_id'],a['qualification']])
 text='# Qualified configurations\n\nScoped reference pointers do not mean universally superior models. Native tools, coding, agent throughput, energy, low-VRAM, streaming and long-context profiles have different denominators and validity limits. No production deployment is implied.\n\n'+table(['Profile','Measurement sprint','Qualification scope'],cr)
 roles=read('benchmark-register.json').get('role_comparison')
 if roles:
  intro='## Jarvis role selection — provisional\n\n**Locally measured, role-specific recommendations; no overall Champion or production deployment.** Official Agents: **NOT MEASURED**. Complete coding/tools scores remain in the [master table](configuration-comparison.md); local Agent33 stays separate.\n\n'
  for d in roles['decisions']:
   intro+='- **'+d['role']+' — '+esc(d['profile'])+'**: '+esc(d['decision'])+' '+', '.join('['+e+'](experiments/'+e+'.md)' for e in d['evidence'])+'\n'
  intro+='\n<details><summary>Observed Pareto tradeoffs: coding and tools</summary>\n\n'+roles['method']+' Missing metrics prevent dominance assessment. A frontier is relative to this scope-frozen core shortlist and its already measured variants, not every possible model or configuration. **Frontier membership is not an optimization-quality pass.** R541 and R544 remain rejected for their predeclared coding-quality gates even if their cost tradeoffs appear on this frontier.\n\n'
  for kind,category in roles['categories'].items():
   rows=[]
   for v in category['points']:
    energy='NOT MEASURED' if v['energy_lower'] is None else f"{v['energy_lower']:.2f}–{v['energy_upper']:.2f}"
    profile='['+esc(v['model'])+'](configuration-profiles/'+v['runtime_configuration_id']+'.md)'
    rows.append([profile,'['+v['experiment_id']+'](experiments/'+v['experiment_id']+'.md)',str(v['solved'])+'/'+str(v['tasks']),round(v['seconds_per_task'],3) if v['seconds_per_task'] is not None else None,energy,v['peak_vram_mib'],v['pareto_status'],', '.join(v['dominated_by']) or '—'])
   intro+='### '+kind.title()+'\n\n'+table(['Exact profile','Evidence','Solved','Response s/task','GPU J/success bounds','Peak VRAM MiB','Observed status','Dominated by'],rows)
   if category['missing_complete_experiments']:intro+='Incomplete/missing qualified runs in selected scope: '+', '.join(category['missing_complete_experiments'])+'. No score imputed.\n'
  intro+='\n</details>\n\n<details><summary>Separate local Agent33 evidence</summary>\n\n33 authored cases in11 families; not Terminal-Bench, a population safety rate or an unseen holdout for later tuning. No joint official mean. Policy counts are independently replayed simulated case outcomes, not population safety guarantees. Missing counts remain NOT MEASURED; original security audits remain linked. Different model templates, context limits and request counts are disclosed per profile.\n\n'
  intro+=table(['Profile','Evidence','Solved /33','Policy passes /33','Case wall s','GPU J/success bounds','Peak VRAM MiB'],[[v['model'],'['+v['experiment_id']+'](experiments/'+v['experiment_id']+'.md)',str(v['solved'])+'/33',str(v['policy_gate_passes'])+'/33' if v['policy_gate_passes'] is not None else None,round(v['case_wall_s'],3),f"{v['energy_lower']:.2f}–{v['energy_upper']:.2f}",v['peak_vram_mib']] for v in roles['agents_development']])
  intro+='\n</details>\n\n<details><summary>Agent33 safety and output diagnostics</summary>\n\nRecounted from the same independently replayed original case results. Rejected tool calls are simulated proposals blocked by the deterministic harness, not executed production writes. Rejected-call and invalid-action events are distinct from affected cases. Final-contract failures combine missing/invalid final contracts without double counting; wrong status/reason/facts are separate semantic checks. Categories overlap and must not be summed into a score. Parser success alone does not establish correct arguments or safe behavior. Missing observations remain NOT MEASURED. No tasks, model outputs or scores were changed.\n\n'
  intro+=agent_diagnostics_table(roles['agents_development'])
  intro+='\n</details>\n\n## Existing scoped reference profiles\n\n'
  intro=re.sub(r'(?s)<details><summary>(.*?)</summary>\n\n(.*?)\n</details>',lambda m:'??? note \"'+m.group(1)+'\"\n\n'+''.join(('    '+line if line else '')+'\n' for line in m.group(2).splitlines()),intro)
  text=text.replace('# Qualified configurations\n\n','# Qualified configurations\n\n'+intro,1)
 for x in profiles:
  if not x['C']:continue
  a=refs[x['C']];text+='\n## Profile '+x['C'][:12]+'\n\n`'+x['id']+'`\n\nA0: `'+x['A0']+'`\n\nC: `'+x['C']+'`\n\n'+pretty(a)+'\n'
 put('configurations.md',text)
 final_page=final_snapshot_page(read('benchmark-register.json'),es,profiles,refs,counts,read('pipeline-performance.json'),read('research-issues.json'),read('screening.json'),history)
 if final_page:put('best-of-v100-2026.md',final_page)
 put('rejected.md','# Rejected optimizations and limits\n\nNegative results are retained. PARTIAL factors can contain rejected variants alongside valid narrower results. These are not equivalent to globally rejected factors.\n\n'+table(['Factor','Scope','Decision'],[[f"[{f['id']}](factors/{f['id']}.md)",f['status'],f['decision']] for f in fs if f['status'] in {'TESTED_NEGATIVE','PARTIAL'}])+'''\n## Interpretation corrections

- C11 forced unfused versus forced fused is not an improvement over the existing stock fused dispatch.
- C15 cached compression-mode names did not prove effective NVCC compression. R356 reopened its hardware-coverage claim.
- Q08's failed repeated-state numerical gate remains failed after a diagnostic found no tested conversion/copy bug. A diagnostic is not a tolerance waiver.
- Smaller context or shorter generation can save memory/time while failing quality; retain the actual early-stop denominator.
''')
 stage_rows=[['OmniCoder2','YES','YES: R181/R183/R220','YES: original12','YES: R181','YES: R183','YES: R220','YES: R90/R220/R226','YES: scoped profile records'],['Qwen3.5','YES','YES: R227/R228/R255','YES: recorded native suite','YES: R255','YES: R227','YES: R228','YES: R122–R127','Not an allround champion'],['Qwen3.8','YES','YES: R117/R118/R260','YES: recorded native suite','YES: R117/R118','See exact audits','YES: R260/R261','YES: MTP comparison','Not an allround champion']]
 for x in models:
  stage=['UNVERIFIED']*7
  if x['id']=='BMC01':stage=['YES: pinned Q6','YES: R253','YES: R259','YES: R254/R258','UNVERIFIED full100','YES: R253','YES: reasoning profile']
  elif x['id']=='BMC04':stage=['YES: PQ2 track','YES: R267+','YES: archived native suite','YES: recorded 164','YES: recorded 100','YES: recorded 18','YES: kernel/recipe variants']
  elif x['id']=='BMC03':stage=['YES: R287','YES: R288','YES: R288','UNVERIFIED','UNVERIFIED','PARTIAL: R289 early stop','UNVERIFIED']
  elif x['id']=='BMC02':stage=['YES: R290','YES: R409','PARTIAL: audited output-budget profile','NOT MEASURED','Control only; no100-case score','NOT MEASURED','NOT MEASURED']
  stage_rows.append([x['name']]+stage+['UNVERIFIED / no comparable-profile qualification'])
 stage_table=table(['Model','Local weights','GPU load','Basic quality','Coding','Tools','Agents','Own optimization','Comparable profile qualified'],stage_rows)
 from comparison import render as render_comparison
 render_comparison(read('comparison.json'),D,model_registry=read('models.json'),experiments=es)
 from leaderboard import render as render_leaderboard
 render_leaderboard(read('benchmark-register.json'),read('configuration-history.json'),read('comparison.json'),D,model_registry=read('models.json'))
 # Current development evidence is separate from the frozen retrospective snapshot.
 development=[e for e in es if e.get('development_comparison')]
 methods=D/'pipeline-methods.md'
 if development and methods.exists():
  rows=[]
  for e in development:
   d=e['development_comparison']
   rows.append([f"[{e['id']}](experiments/{e['id']}.md)",e.get('model'),d['matched_base_tasks'],str(d['completed_requests'])+'/'+str(d['planned_requests'])])
  section='## Executed independent development comparisons\n\n'+table(['Experiment','Model','Matched development tasks','Completed requests'],rows)
  section+='\nThese are actual independent development-task runs, separate from the retrospective resampling above. This list does not establish screening validity across models. A model absent here has no recorded result on this development set; its official benchmark answers must not be substituted as a development reference. No candidate-selection or cross-model screening claim follows from Nexus-only A/B/C evidence.\n\n'
  text=methods.read_text();anchor='## Nexus: first controlled development comparison'
  assert anchor in text
  put('pipeline-methods.md',text.replace(anchor,section+anchor,1))
 from derivatives import render as render_derivatives
 registry=read('benchmark-register.json')
 render_derivatives(registry.get('candidate_research',[]),D,registry.get('model_family_labels',{}))
 put('models.md','# Model benchmarks and transfer\n\n[View Model Comparison & Benchmarks with audited charts](benchmarks.md).\n\nModels are compared within the same tasks using correct model-specific tokenizers/templates. A higher coding score is not general assistant superiority. Base-versus-plus joint coding scores, task success, VRAM and energy remain separate.\n\n'+table(['Track','Candidate','Status','Evidence','Latest recorded sprint'],[[x['id'],x['name'],x['status'],x['evidence_class'],x['current_experiment']] for x in models])+'\n## Evidence stages (not a ranking)\n\n'+stage_table+'\nYES indicates an observed stage, not a passed quality gate. Old source-admission records are historical and may precede later GPU work. Bonsai PQ2 and the separate PTQ port must not be conflated.\n\n## Existing OmniCoder2 / Qwen / challenger measurements\n\n'+pretty(read('model-benchmarks.json'))+'\n## Candidate admission records\n\n'+''.join('\n### '+x['id']+' — '+x['name']+'\n\n'+pretty(x) for x in models)+'\n## Stage semantics\n\nResearched, locally available weights, GPU-load success, measured basic quality, coding, tool calling, agents and qualified comparable profile are separate stages. Missing stage evidence is **UNVERIFIED**, not NO and not YES. A model file or source-only architecture review does not prove any downstream stage. See the linked experiments rather than infer completion from a track status.\n')
 comp=[]
 for f in fs:
  comp.append([f"[{f['id']}](factors/{f['id']}.md)",'Local evidence in stated scope' if f['omnicoder2_experimentally_covered'] else 'Unverified / architecture-specific', 'Requires model-specific audit','Requires model-specific audit','No automatic transfer'])
 put('compatibility.md','# Optimization compatibility matrix\n\nThe table deliberately distinguishes demonstrated OmniCoder2 scope from conditional transfer. Qwen3.5 and Qwen3.8 stages must be read from the exact model-specific experiments. No cross-model gain is inferred. vLLM/FP8 and dense/MoE applicability differ from GGUF.\n\n'+table(['Factor','OmniCoder2 / llama.cpp GGUF','Qwen3.5','Qwen3.8','Other engines/models'],comp))
 sources=read('sources.json');put('sources.md','# Research papers & sources\n\nOriginal sources are cited rather than republished. Source revisions refer to the reviewed snapshot, not an assertion that upstream is unchanged. Secondary/community claims are discovery leads rather than local causal evidence.\n\n'+''.join('\n## '+x['id']+'\n\n'+pretty(x) for x in sources)+'\n## Factor-specific bibliography\n\n'+ '\n'.join('- ['+f['id']+'](factors/'+f['id']+'.md): '+', '.join(f['primary_sources']) for f in fs if f['primary_sources']))
 put('background.md', '''# Scientific background

Volta optimization balances arithmetic intensity, HBM traffic, launch overhead and data reuse. Higher occupancy alone is not a target; register spilling can erase the benefit of a larger tile or more warps. Shared-memory banks and register banks are different mechanisms.

FP16 Tensor Core use depends on layout and instruction eligibility. Quantized GEMV, quantized GEMM, dequantized cuBLAS and recurrent GDN operations have different bottlenecks. Native FP8 Tensor Core results from newer hardware cannot be applied to SM70. W8A16 uses compressed storage plus supported arithmetic and has distinct format/loader requirements.

Hybrid models combine attention KV with recurrent states. A rollback of accepted attention tokens without equivalent recurrent-state restoration can be functionally wrong even if a primitive or synthetic throughput test passes. Token decisions, tools and policy outcomes must be checked.

The data-pattern HBM2 power paper studies separately instrumented memory. Board-level GPU energy cannot identify internal DRAM bus switching or memory-rail current. Actual DRAM-byte counters require compatible profiling, permission and an explicit hypothesis; weight bytes/time are not a traffic measurement.

See the [pinned source registry](sources.md) and [factor details](matrix.md). Published benchmarks, proven implementations and causal hypotheses are reported separately.
''')
 proposals=read('research-subcases.json');issue_registry=read('research-issues.json')
 open_issues=[x for x in issue_registry if x.get('github_state')=='OPEN'];closed_issues=[x for x in issue_registry if x.get('github_state')=='CLOSED']
 def issue_rows(items):
  return [[x['subcase'],'['+x['title']+']('+x['url']+')',x['status'],x.get('freeze_priority'),x.get('next_action','')+' '+', '.join('[evidence]('+u+')' for u in x.get('evidence_urls',[]))] for x in items]
 priority='Current P0: owner-authorized new-family model qualification (#16); the dated Best-of-V100 decision remains a baseline.' if issue16_active else 'Current P0: final research/model decision (#10/#11).'
 questions='# Open questions & research proposals\n\nGitHub snapshot: '+max(x.get('github_checked_at_utc','') for x in issue_registry)+'. **'+str(len(open_issues))+' open / '+str(len(closed_issues))+' closed**. This is not a live issue monitor. Workflow closure, scientific disposition and optimization qualification are separate.\n\n'+priority+' Source/kernel gates remain conditional. Harness CPU reviews (#17/#18) do not authorize new GPU ablations. No factor count or GPU coverage is increased by this registry.\n\n'
 questions+=table(['Subcase','Open GitHub issue','Research disposition','Freeze priority','Next step / evidence'],issue_rows(open_issues))
 for issue in issue_registry:
  if issue.get('candidate_decisions'):
   questions+='\n??? note "Eight-family technical dispositions · measured scope and next gate"\n\n'
   matrix=table(['Candidate / pinned artifact source','Disposition','Measured scope / reopen condition','License'],[['['+r['model']+'](https://huggingface.co/'+r['hf_repository']+'/tree/'+r['hf_revision']+')',r['decision'],r['reason'],r['license']] for r in issue['candidate_decisions']])
   questions+=''.join(('    '+line if line else '')+'\n' for line in matrix.splitlines())
   questions+='\nADMIT identifies reviewed execution scope, not an allround Champion. DEFER and technical blocks do not measure zero quality. Completion review SHA256: `'+issue['completion_review_sha256']+'`.\n\n'
  if issue.get('source_addendum_review'):questions+=issue16_source_section(issue['source_addendum_review'])
 prefix_review=next((x for x in issue_registry if x.get('prefix_recurrence')),None)
 if prefix_review:
  recurrence=prefix_review['prefix_recurrence']
  questions+='\n<details class="lab-evidence"><summary>Harness token recurrence · R537 · 96 archived requests</summary>\n\n'
  questions+=table(['Arm','Requests','Recorded input tokens','Repeated within-case prefix tokens after first call'],[[arm,v['requests'],v['input_tokens'],v['repeated_within_case_prefix_tokens_after_first']] for arm,v in recurrence['arms'].items()])
  questions+='\nExact token IDs and request hashes match all96 original usage records; `cache_prompt=false` throughout. Five paired development cases, not an independent harness ablation. Prefixes include task/history content; isolated system/tool preamble tokens remain **NOT MEASURED**. No prompt was shortened, cache correctness tested, or latency/energy saving measured.\n\nAudit SHA256: `'+prefix_review['prefix_recurrence_audit_sha256']+'`. [CPU reproduction script](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/scripts/harness_prefix.py), SHA256 `'+recurrence['analysis_code_sha256']+'`.\n\n</details>\n'
 questions+='\n??? note "Closed scoped workflow records — not additional qualified optimizations"\n\n'
 questions+=''.join(('    '+line if line else '')+'\n' for line in table(['Subcase','Closed GitHub issue','Recorded scope','Priority','Evidence / boundary'],issue_rows(closed_issues)).splitlines())
 questions+='\n## Retained research proposals\n\nHypotheses and admission prerequisites remain distinct from measured gains. Existing safety and single-factor gates still apply.\n'+''.join('\n## '+x['id']+'\n\n'+pretty(x) for x in proposals)
 put('questions.md',questions)
 put('roadmap.md',f'''# Changelog & roadmap

Snapshot revision **{s['matrix_revision']}**; latest canonical assessment **{s['source_date']}**.

1. Finish technically meaningful remaining single-factor variants; preserve valid negative evidence.
2. Compare the remaining models, then reassess optimization applicability for each architecture, weight format, quantization, engine/kernel path, context and VRAM budget. A new model may enable a treatment that was unavailable on OmniCoder2.
3. Run promising model-specific single-factor tests before combining anything.
4. Test compatible interactions only after model-specific transfer; use fresh controls and independently qualify the combined profile.
5. Target final quality, latency and energy qualification with a reproducible recommendation by 31 October 2026. A deadline cannot turn an unverified claim into a qualification.

The present sprint is an active research snapshot, not the final result. Historical phase labels can be superseded by a reopened research gate; the current gate controls new work.

Publication commits record successive audited snapshots. Original negative results must not be removed silently; corrections require a new entry, reason and previous-audit reference.
''')
 reproduction='''# Reproducing the results

## Export an exact measured configuration

```sh
python scripts/leaderboard.py --export-profile @PROFILE_ID@ > profile.json
```

The JSON packet preserves the original immutable profile, ordered arguments, environment, request settings, model/quantization, weight and template hashes, engine build/binary/CUDA-library identities, recorded source/patch lineage and exact-profile benchmark audit views. Unknown fields stay `null`. Multiple views of one original measurement audit are grouped; their count is not a count of GPU jobs or independent generations. Different coding/tool configuration IDs are not silently merged.

**This is a specification, not a runnable launch or broker approval.** Replace redacted artifact/session placeholders only after verifying the corresponding assets. Requested flags do not prove an executed kernel/cache mode. No downloads, installations, model processes, broker submissions or production changes occur during export.

### Reproduction boundaries

- Obtain weights from the recorded publisher/revision under its license; no weights are distributed here.
- Exact template bytes, external draft artifacts and original engine dependencies must be supplied separately. The matched main-engine source package below supplies the archived patches and build identities; external dependencies and original build paths are not bundled. A bit-identical independent rebuild is **not established** by this packet.
- Locally retained original launch/configuration receipts remain authoritative. Redacted public bytes are not the hash of a private original launch.
- Full official tests require the exact registered dataset, task set, scorer and evaluation settings. Different templates, output limits, engines, quantization or sampling form another profile.
- Private development/Agent33 inputs are not redistributed. Exact public reproduction of those suites remains incomplete. A substitute must use a new experiment identity.
- A coding packet is not an Agent33 or tool-runtime qualification. Those original captures retain separate profile IDs/hashes and harness settings.

## Controlled Jarvis deployment proposal

**PROPOSAL ONLY — no production changes performed or implied.** [Role decisions and observed tradeoffs](configurations.md) are provisional. Official Terminal-Bench remains **NOT MEASURED**.

1. **Sandbox baseline:** retain the measured OmniCoder bartowski Q6 / MTP-OFF option for single-agent validation. Its local 28/33 result is not a safety certificate. Keep canonical OmniCoder, Nexus and Ornith as documented alternatives.
2. **Separate specialists:** Gemma4's existing nonthinking profile is a coding-quality option. OmniCoder MTP3 is a native-tool-specific option; its coding/Agent33 regression forbids promoting it to an allround profile. Qwen27 integrated MTP3 remains a larger alternative with measured VRAM/latency/energy tradeoffs.
3. **Stage exact assets and settings:** use the original matching role-specific capture. Verify weights, template, server, CUDA library and dependencies; retain measured context/output/batching/power. The packet alone does not admit a new binary or executable. Unknown or altered inputs require the existing source/build/execution review.
4. **Use the existing broker:** one GPU-heavy job; unchanged ECC, temperature, throttling, power and 14,336-MiB device-memory guards. Any research benchmark shares one 1,200-second TASK budget across all parts; startup and cleanup are separate. Existing research authorization remains valid within its policy.
5. **Shadow/simulated tools first:** enforce permissions deterministically outside the LLM. No productive Home Assistant, Proxmox or other real write actions. Record task completion, policy violations, recovery, end-to-end cost and failures. Do not retune on final official tests or repeat valid benchmarks without a distinct hypothesis.
6. **Release gate:** compare against the unchanged baseline, retain rollback artifacts, and obtain explicit production approval before changing a productive service or privileges. This proposal performs neither action.

Single-Agent remains the comparison baseline. R537's five paired cases do not justify Planner/Worker/Reviewer by default. Automatic specialist routing, real model-switch overhead and cold-start costs are **NOT QUALIFIED**; separate role recommendations do not prove that a routed system wins.

## Public documentation and data

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/validate.py
python -m unittest discover -s scripts
python scripts/render.py
mkdocs build --strict
```

The public byte manifest validates exported files; each audit separately identifies its retained original. Documentation regeneration must leave no unexplained changes. The role-comparison tests recompute the published assessment from public immutable history; no model inference is needed.

## A comparable GPU reproduction

Use one V100 SM70 with 16 GB, exact artifact and engine identities, role-specific native template/sampler/context/KV/state/batch/offload/threads, frozen tasks and scorer. Preserve warm/cold conditions and record actual power/clocks. Measure task success, response latency, prefill/decode, TTFT, memory, GPU energy and stability separately; unmeasured values remain missing.

Some historical runs lack complete public build recipes, uncertainty estimates or task-level data. Follow linked original audits and factor-specific prerequisites. No repository workflow starts GPU jobs.
'''
 reproduction_history=read('configuration-history.json')
 example=next(r['runtime_configuration_id'] for r in reproduction_history['runs'] if r['experiment_id']=='R548' and r['official_eligible'])
 reproduction=reproduction.replace('@PROFILE_ID@',example)
 for review in read('benchmark-register.json').get('engine_source_reviews',[]):
  package=review.get('reproduction_package')
  if not package:continue
  reproduction+='\n## Pinned main-engine source package\n\n**Source evidence, not a new optimization or GPU qualification.** Base commit `'+package['source_base_commit']+'`; `'+package['comparison_upstream_commit_not_build_base']+'` is the separate historical comparison revision, not this build base. Original server SHA256 `'+package['server_sha256']+'`.\n\n'
  reproduction+=table(['Exact source asset','Bytes','SHA256'],[['['+a['name']+']('+a['url']+')',a['bytes'],a['sha256']] for a in package['source_assets']])
  reproduction+='\nUse a separate source checkout at the stated build-base commit, without model weights. Apply `main-protocol.patch`, place the supplied header at `include/llama-grammar-prefill.h`, and apply `numeric-fixtures.patch` for the recorded backend-test target. Verify the five resulting source hashes listed below before configuring. These steps are instructions for a new isolated tree; archived and productive trees must remain untouched.\n\nOriginal upstream MIT copyright/permission notice is included. The protocol/header patch changes grammar-prefill handling; the separate numerical patch defines backend-test shapes, not a newly measured speedup. All bytes are bound to archived build/source receipts. No model weights, compiled binaries or NVIDIA libraries are redistributed.\n\n'
  reproduction+='Read-only checks match the retained patched sources. An independent fresh checkout/build and bit-identical rebuild have **not** been performed here. Compiler paths are explicitly remapped; external CUDA/system dependencies and CPU-native build conditions still matter. A rebuilt binary has a new identity and needs the existing source/build/admission review before research execution.\n\n'
  reproduction+='??? note "Recorded toolchain, configure arguments and runtime-library identities"\n\n'
  detail='Recorded compiler jobs: '+str(package['compiler_jobs'])+'. Configure in a separate unprivileged build directory against the pinned source; do not patch a productive or archived tree. Obtain the listed toolchain separately and map compiler paths explicitly. Build targets recorded in the original recipe: `llama-server` and `test-backend-ops`. These are reproduction instructions, not commands executed by this publication.\n\n'
  detail+=table(['Tool','Recorded version'],list(package['toolchain_versions'].items()))+'\n```json\n'+json.dumps({'cmake_flags':package['cmake_flags'],'remapped_compiler_paths':package['remapped_compiler_paths'],'expected_runtime_libraries_sha256':package['libraries_sha256'],'patched_sources_sha256':package['named_patched_sources_sha256']},indent=2)+'\n```\n'
  reproduction+=''.join(('    '+line if line else '')+'\n' for line in detail.splitlines())
  reproduction+='\n[Original reproduction receipt](audits/'+review['reproduction_audit_id']+'.md). Local library/file hashes identify the measured build; they do not assert identical output from another compiler or host.\n'
 reproduction+='\n??? note \"Selected exact benchmark-profile pointers\"\n\n'
 selected_rows=[]
 for eid in ('R471','R516','R488','R464','R465','R466','R495','R542','R548'):
  run=next(r for r in reproduction_history['runs'] if r['experiment_id']==eid and r['official_eligible'])
  selected_rows.append([run['model_name'],'['+eid+'](experiments/'+eid+'.md)','['+run['runtime_configuration_id']+'](configuration-profiles/'+run['runtime_configuration_id']+'.md)'])
 reproduction+=''.join(('    '+line if line else '')+'\n' for line in table(['Profile','Original benchmark capture','Exact export ID'],selected_rows).splitlines())
 put('reproduce.md',reproduction)
 put('publication.md','''# Public export and update policy

Only projected research metadata is publishable. The exporter uses explicitly selected keys, numeric aggregate branches and public HTTPS source domains. Explicit source-code exceptions export four named, SHA-bound main-engine reproduction files with their original MIT notice and three exact lab-owned pure request transforms under the project MIT license. These contain no private fixtures, model outputs or privileged runners. It never copies arbitrary source files, models, logs, prompts, responses, system dumps, authentication files or network configuration. Local audit locations remain in a private receipt outside this repository.

Publication validates all 162 unique factors, original/additional counters, scientific statuses, reference pointers, evidence links, forbidden content, file paths/sizes and the byte manifest. Selected original audit hashes are checked locally before export. CI only validates the public snapshot and builds static documentation; it cannot independently access the retained originals.

A local serialized synchronization job checks canonical state after audited work, regenerates data and pages, validates, commits and pushes. It skips while the canonical experiment lock is held. Failed authentication/push is recorded locally and retried in bounded later runs; it never blocks GPU work. Publishing requires an authenticated GitHub account and a configured HTTPS origin. It never force-pushes or rewrites history.

No publication is claimed until the repository exists, push succeeds and Pages deployment is verified. Proposed GitHub issues are first retained as public research proposals; remote issues are created only once an authenticated repository is available.

New script/documentation copyright is licensed under MIT. Referenced third-party software, papers, models and benchmark datasets retain their own licenses. No permission to redistribute their weights, code, test data or full papers is implied.
''')
 put('de.md',f'''# Deutsche Übersicht

Unabhängiges Community-Forschungsprojekt zur besten praktisch nutzbaren lokalen KI auf einer einzelnen Tesla V100-SXM2 mit 16 GB HBM2. Keine Verbindung zu NVIDIA, Ollama oder Modellherstellern.

Aktueller Stand: Revision {s['matrix_revision']}, 130 Originalachsen + 32 Zusatztechniken, {counts['experimentally_covered']} experimentell abgedeckt, {counts['scientific_status']['QUALIFIED']} Achsen im angegebenen Umfang qualifiziert. 11 Modell-Challenger werden getrennt geführt. Bewertung, GPU-Eingriff und unabhängige Qualifikation sind verschiedene Dinge.

Die englischen Hauptseiten enthalten Methodik, Faktoren, Originalaudit-Hashes, qualifizierte Profile und Negativbefunde. Einige genaue Begründungen bleiben in ihrer ursprünglichen deutschen Sprache. Fehlende Messwerte heißen NOT MEASURED. Private Aufgaben, Logs, Infrastruktur und Gewichte werden nicht veröffentlicht; exakte öffentliche Reproduzierbarkeit ist deshalb bei privaten Suites begrenzt.

Es gibt noch keinen endgültigen universellen Modellgewinner. Aktuell gilt: gemeinsames Entwicklungsscreening → offizielle Qualifikation → gezielte Optimierung → Bestätigung. Kleine Screeningunterschiede führen zu keiner automatischen Qualitätsaussortierung. Die bestehenden Schutzmechanismen bleiben verbindlich.
''')
 changelog=P/'CHANGELOG.md'
 entry='## Audited research checkpoint '+max((e['id'] for e in es),key=lambda x:int(x[1:]))+' / '+read('comparison.json')['measurement_fingerprint'][:12]
 if not changelog.exists():changelog.write_text('# Changelog\n\n')
 previous=changelog.read_text()
 if entry not in previous:
  changelog.write_text(previous+'\n'+entry+'\n\nAudited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.\n')
 # Content-addressed asset URLs prevent mixed old/new table code or datasets.
 # Unrelated matrix changes do not invalidate unchanged benchmark assets.
 config=P/'mkdocs.yml';configuration=config.read_text()
 for asset in ['stylesheets/lab.css','assets/benchmarks/leaderboard-data.js','javascripts/master-table.js','javascripts/leaderboard.js','javascripts/screening.js']:
  version=hashlib.sha256((D/asset).read_bytes()).hexdigest()[:16]
  configuration=re.sub(r'(?m)^(\s*-\s+)'+re.escape(asset)+r'(?:\?v=\S+)?$',lambda m:m.group(1)+asset+'?v='+version,configuration)
 config.write_text(configuration)
 from screening import render as render_screening
 put('screening.md',render_screening(read('screening.json')))
 from screening import render_validation,render_qualification
 methods=D/'pipeline-methods.md'
 from screening import render_native_agent_development
 methods.write_text(methods.read_text()+render_qualification(read('screening.json'))+render_validation(read('screening.json'))+render_native_agent_development(es))
 frozen=read('frozen-baselines.json') if (P/'data/frozen-baselines.json').exists() else None
 put('final-qualification.md',final_qualification_review(read('screening.json'),read('configuration-history.json'),es,frozen))
 if frozen:put('final-selection.md',render_final_selection(frozen,read('configuration-history.json')))
 print('Rendered',len(fs),'factors,',len(es),'sprints,',len(audits),'audit excerpts')
 if (P/'data/pipeline-performance.json').is_file():
  from pipeline import render as render_pipeline
  put('pipeline-performance.md',render_pipeline(read('pipeline-performance.json')))
if __name__=='__main__':main()
