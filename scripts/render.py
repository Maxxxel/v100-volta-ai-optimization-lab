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

def main():
 s=read('snapshot.json');fs=read('factors.json');es=read('experiments.json');audits={x['id']:x for x in read('audit-excerpts.json')};profiles=read('profiles.json');refs={x['id']:x for x in read('references.json')};models=read('models.json');counts=s['counts']
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
 overview=f'''# V100 Volta AI Optimization Lab

<p class="lab-eyebrow">Independent research · NVIDIA Volta / SM70</p>
<p class="lab-lead">Better local AI on one Tesla V100-SXM2 with 16 GB HBM2. We measure model quality, useful speed and GPU energy — with reproducible configurations and retained negative results.</p>

<div class="lab-actions"><a class="lab-button lab-primary" href="configuration-comparison/">Compare models</a><a class="lab-button" href="archive/">Explore the research</a></div>

<div class="lab-kpis"><div><strong>162</strong><span>Research factors</span><small>130 original + 32 techniques</small></div><div><strong>{counts['experimentally_covered']}</strong><span>Experimentally covered</span><small>Factors, not GPU run count</small></div><div><strong>{counts['scientific_status']['QUALIFIED']}</strong><span>Qualified factor scopes</span><small>Workload-specific evidence</small></div><div><strong>16 GB</strong><span>HBM2 on one V100</span><small>One GPU benchmark at a time</small></div></div>

## Research pipeline

[Screening](screening.md) → [Official qualification](configuration-comparison.md) → [Targeted optimization](configurations.md). Development screens stay outside official scores.

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
 text='# Qualified configurations\n\nTen profile pointers do not mean ten universally superior models. Native tools, coding, agent throughput, energy, low-VRAM, streaming and long-context profiles have different denominators and validity limits. No production deployment is implied.\n\n'+table(['Profile','Measurement sprint','Qualification scope'],cr)
 for x in profiles:
  if not x['C']:continue
  a=refs[x['C']];text+='\n## Profile '+x['C'][:12]+'\n\n`'+x['id']+'`\n\nA0: `'+x['A0']+'`\n\nC: `'+x['C']+'`\n\n'+pretty(a)+'\n'
 put('configurations.md',text)
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
 proposals=read('research-subcases.json');issue_registry=read('research-issues.json');put('questions.md','# Open questions & research proposals\n\nThese are hypotheses or admission plans, never claimed local improvements. They extend existing axes and do not increase the factor count. GPU execution remains behind the single-factor and safety gates.\n\n'+table(['Subcase','Public research issue','Status'],[[x['subcase'],'['+x['title']+']('+x['url']+')',x['status']] for x in issue_registry])+''.join('\n## '+x['id']+'\n\n'+pretty(x) for x in proposals))
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
 put('reproduce.md','''# Reproducing the results

## Public documentation and data

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/validate.py
mkdocs build --strict
```

All public pages are generated from `data/` by `python scripts/render.py`. Rerendering and validation must leave a clean worktree. `data/publication-manifest.json` verifies exported bytes; each audit receipt separately names the SHA256 of its unmodified retained original. Redacted bytes are not an original-audit hash proof.

## A comparable GPU reproduction

Use one V100 SM70 with 16 GB, the exact public weight repository and hash, pinned engine/build identities, context/KV/state/batch/offload/threads/sampler settings and frozen workload identity of the selected profile. Obtain weights from their licensed publisher; no weights are distributed here. Keep cold/warm conditions, power and actual clocks explicit. Reproduce the numerical oracle before an inference candidate and measure tasks, prefill, decode, TTFT, memory, energy and stability separately.

Use an isolated device and tool simulator. Do not apply example state or tool policies to production. No repository workflow starts a GPU job.

## Limits of this export

Private local task prompts, conversation outputs, simulator entities and infrastructure are intentionally withheld. Their retained hashes identify the original workload but do not provide its text. Thus exact independent task-level reproduction of those suites is **not yet fully public**. Public benchmark releases must be obtained under their own licenses, and any newly authored public substitute must receive a new profile identity; it cannot be passed off as the historical suite.

Some old measurements lack a complete public command/build recipe, confidence interval, numerical oracle or task-level data. Missing fields are not guessed. Follow the factor-specific prerequisites and open a Benchmark Reproduction issue when evidence is insufficient.
''')
 put('publication.md','''# Public export and update policy

Only projected research metadata is publishable. The exporter uses explicitly selected keys, numeric aggregate branches and public HTTPS source domains. It never copies a source file, model, log, prompt, response, system dump, authentication file or network configuration. Local audit locations remain in a private receipt outside this repository.

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
 print('Rendered',len(fs),'factors,',len(es),'sprints,',len(audits),'audit excerpts')
 if (P/'data/pipeline-performance.json').is_file():
  from pipeline import render as render_pipeline
  put('pipeline-performance.md',render_pipeline(read('pipeline-performance.json')))
if __name__=='__main__':main()
