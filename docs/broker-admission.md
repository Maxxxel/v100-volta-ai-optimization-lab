# Safe research admission

Risk classes replace per-factor GPU approvals. Canonical factor IDs are provenance labels; the model/adapter operation schema and risk envelope determine eligibility. A negative optimization result is scientific evidence about its tested configuration; it is not a ban on a distinct model or matrix-shape hypothesis.

| Class | Automatically allowed scope | Excluded |
|---|---|---|
| AUTO_CPU | Asset validation; immutable source snapshots; isolated CMake/GGML or vendored Go/Ollama builds and CPU smoke checks | Supplied root commands, network installers, GPU device access during builds |
| AUTO_GPU_NUMERICS | Fixed-vector operator checks through a reviewed numerical adapter | Arbitrary programs, relaxed tolerances, inferred model quality |
| AUTO_GPU_MODEL_BENCH | Bounded native benchmark or isolated native HTTP adapter, reviewed weights and frozen engine artifacts | Production services, external networking, automatic winner/deployment claims |
| REVIEW_REQUIRED | Interfaces or privileges outside existing bounded adapters | Admission based solely on a self-generated checksum |

## New engines and kernels

New source commits, custom CUDA kernels and experimental engine builds are eligible automatically; a new hash is not itself a rejection reason. Source manifests and declared provenance are recorded. They establish byte identity, not authenticity or execution trust.

The fixed build adapter runs source-controlled build instructions as **UID 65534** in fresh mount, network, PID, IPC and UTS namespaces. Source and system trees are read-only. Build output uses a bounded 512 MiB temporary filesystem, with 4 GiB memory, six CPU workers, a task limit and a bounded deadline. A privileged supervisor only sets up isolation and collects bounded regular-file data; it never executes the resulting binary as root.

Successful builds receive ELF dependency and CPU-smoke evidence. Outputs are frozen before a GPU screen. Compatible GGML CUDA backends can use the original CPU/core numerical oracle rather than defining their own CPU correctness reference. Other supported native engine interfaces begin with a single bounded load/benchmark screen. These are execution admissions, not quality qualifications.

New candidate binaries run as UID 65534 in a separate GPU namespace sandbox with read-only engine/model mounts, bounded writable storage, CPU-memory/task limits and an independent privileged GPU monitor. The native HTTP adapter uses private loopback only. Custom kernels can enter through the engine-fork adapter; a different calling interface needs a compatible isolated adapter, not a manual exception for each binary identity.

Ollama source builds require an available or vendored pinned toolchain and offline dependencies. The adapter is implemented; a complete new Ollama build and GPU benchmark through this migration are **NOT VERIFIED** locally. Missing dependencies, unsupported interfaces or resource ceilings remain explicit technical deferrals. They are never silently converted into successes.

## GPU envelope and immutable evidence

### New model data with an executed engine

A first complete standard benchmark can admit a new model without inventing a previous execution of that model. The root-owned review binds the exact published repository revision, independently verified weight hash, GGUF tensor structure, native template, license, memory budget and inference recipe. Engine assets must match an independently executed, unprivileged parent capture exactly. A new executable requires the separate source/build admission path above.

This path passed **156 CPU regression controls**: 141 existing checks and 15 new tests covering source tampering, missing prerequisites, changed binaries, model identities, task subsets, budget resets and resource limits. All previous profiles and 46 historical clock files were preserved. The first admitted model is the official LFM2.5-24B-A2B QAD-Q4_0 artifact. Admission establishes permission for the bounded experiment; it establishes neither model quality nor measured VRAM fit.

The standard-suite contract retains one model session, a maximum of **1,200 seconds of pure task work**, the existing startup/cleanup wall envelope, immutable benchmark inputs and all GPU safeguards. No preliminary custom-answer quality filter is required. Runtime memory allocation remains independently monitored; an analytical memory budget is not presented as a measured peak.

The automatic path currently uses one V100, one monitored GPU process, baseline 300 W, at most 14 GiB device/process memory, temperature below 90 °C, unchanged zero-uncorrected-ECC and forbidden-throttling checks, bounded execution and existing leases/guardian checks. It does not add a room-temperature start threshold. Previously qualified separate power profiles remain preserved.

The root-owned broker accepts closed JSON data contracts, not shell commands, script paths or custom environments. It snapshots reviewed controller code and plans, verifies model/engine/input identities, checks idle occupancy and serializes admission/start. Experimental code cannot write broker policy or production files. On a guard violation, only the owned candidate unit is terminated; the lease remains held until tagged processes have ended. Baseline power restoration remains mandatory.

Registration validates a separate complete candidate registry before atomic activation. Failed registration leaves the active registry unchanged. Consumed terminal registrations may move out of the bounded active roster only with verified completion evidence; the prior registry, marker, program and audit evidence remain archived. Historical pinned experiments remain usable without accepting new arbitrary root controllers.

## Local verification

| Verification | Result | Scope |
|---|---|---|
| Broker regression suite | 30 tests passed | Policy boundaries, bad identities/hashes, compatibility, hardware faults, parallel starts, invalid-registration rollback, source links and scoped termination |
| Isolated source/build probes | Passed | UID 65534, read-only source/system, no GPU devices or protected host files, output quotas and ELF dependency capture |
| [R446](experiments/R446.md) | 12/12 new PQ2 boundary cases passed | Fixed native CPU/CUDA comparison, NMSE bound 5e-4; 806.5 MiB peak device memory |
| Candidate namespace GPU regression | One case passed | Reviewed original binaries through the new unprivileged namespace path; not an additional optimization factor |

Three submitted infrastructure failures occurred before native GPU execution during migration. Their logs and one-shot markers remain intact. Fixes addressed the LXC lock-file mount, private file transfer and the distinction between raw reserved NVML bytes and the existing idle rule. No valid benchmark was rerun to repair those startup failures.

R446 does **not** qualify a routing change, speedup, whole-model numerical equivalence or a Champion. Historical negative FORCE_MMQ results and all existing model/reference profiles remain unchanged.

## Historical whole-benchmark deadline and model lifetime

R451 used one sequential model session for the declared full task set. Its historical 900-second wall budget covered the complete benchmark across all jobs and evaluation stages; partitioning, changing a factor label or renaming an otherwise identical profile cannot renew it. Startup/preflight and cleanup reserves reduce the time available for inference. Unknown/stopping service states and residual processes fail closed.

A genuinely new execution protocol requires a root-owned source/resource review bound to one exact immutable contract and complete ordered task set. The reviewed single-session change keeps model weights, engine, template, sampling, context, output cap, hardware limits and isolation unchanged. It does not authorize new model derivatives or reset a predecessor campaign. Fresh responses are required; incomplete earlier campaigns remain preserved.

The single-session executor passed **87 CPU regression tests**, including existing admission, deadline, ECC, occupancy, numerical-adapter and rollback controls. An actual SIGTERM probe in a private CPU-only PID namespace preserved partial response files without producing a successful completion. These checks qualify the executor safeguards, not model quality or a performance improvement.

Historical one-session coding runs remain valid within their recorded scopes. Small multi-session campaigns are explicitly distinguished when comparing whole-campaign latency and energy. Completion-HTTP metrics exclude model startup and must not be presented as full workflow costs.

## Current timing policy: 20 minutes of task work

The user explicitly replaced the earlier whole-run limit with **1,200 seconds of pure benchmark task work**. For admitted single-session native comparisons, the fixed unprivileged adapter marks the phase after load and warmup and before the first benchmark task. The privileged monitor validates and stores one-shot boot-clock/wall-clock markers and enforces the task limit. Loading, warmup, CPU scoring and cleanup are excluded from task time and remain independently bounded: 180 seconds startup, 1,440 seconds GPU-wrapper ceiling with cleanup reserve, and 120 seconds per CPU evaluation pass. Socket clients cannot reset or fabricate a timer phase; factor/profile/task aliases cannot renew an exact admitted run.

The trusted task client uses a non-dumpable process so another process with the same unprivileged UID cannot write to its protected event stream; the engine has its own log stream. **90 CPU regression controls** passed, with separate actual stop/copy and protected-descriptor probes. Historical 900-second clocks and audits remain unchanged; the new limit applies only through an explicitly reviewed immutable contract.

[R452](experiments/R452.md) collected all164 fresh answers with one model start. Its root-recorded task phase took **902.585 seconds**, excluding about55.5 seconds startup. Independent official-API scoring confirmed **116/164** with zero changed judgments. This qualifies the stated local HumanEval+ result, not an optimization speedup, tool/agent quality or a Champion. Earlier [R450](experiments/R450.md) and [R451](experiments/R451.md) partial results remain visible with their actual denominators.

## Complete native tool-category admission

R453 extends the same closed task-time policy to the pinned **400-task BFCL `simple_python` category**, using the existing reviewed model, native template and engine. The broker requires every ordered category ID, an exact contract, a protected prior GPU execution snapshot and successful native tool-wire evidence. The model/engine/sampler and hardware constraints remain bound to the review; a task-list subset, alias or an unreviewed checker is not a full-category admission. **97 CPU broker controls passed** before transactional activation; previous profiles and all seven historical clock files were preserved. The GPU runner, task adapter and thermal/ECC/VRAM/power protections are unchanged.

The public export independently verifies complete original inputs, both CPU scoring receipts, the reviewed official AST sources and category aggregation. Additional practical protocol checks remain separate. Two identical CPU score passes replay one answer set; they are not two independent model runs. Only the full category can be admitted locally; no full-BFCL or production-tool qualification follows.

## Archived model evidence and unchanged engine binaries

The October24 extension admits a data-only archived Qwen3.5-family model profile to an **already executed, independently admitted engine tuple**. It cross-checks the original model identity, explicit publisher template, native sampler, launch arguments, warmups and CUDA mappings. The engine reference must match its protected historical registration, original contract, trusted-runner start marker, completed GPU audit and captured profile. A newly invented receipt or another profile carrying an admission flag cannot establish trust in a new binary.

Older research captures do not always record the execution UID. That field remains unknown; it is never backfilled as65534. Every new run still uses the existing adapter that enforces UID65534, private namespaces, read-only model/engine assets, one heavy GPU job and the original power, memory, ECC, thermal and timeout protections. Shared research-folder payloads are treated as untrusted data and verified against the protected contract and pinned capture; their original ownership is unchanged.

**119 CPU controls passed**, including the previous admission/deadline/hardware tests, substituted engine receipts, altered registered runners, unsupported model identity, sampler/environment changes and the real shared-folder ownership case. The real proposed catalog and source chain were also checked before active policy replacement. The first attempted activation rolled back before any GPU start; its evidence is preserved. Final activation preserved all prior profiles, runner/adapter bytes and19 historical clock files. Admission does not qualify benchmark quality, performance, tool safety or a Champion. The current native tool campaigns allow120 seconds total for both isolated CPU scoring passes.

The following Gemma4 data-format extension passed **126 CPU controls**. It verifies the original QAT GGUF admission and download provenance, an explicit native-template hash and every archived native BFCL request's sampler. The template uses Gemma's own tool-call delimiter. The two archived completion warmups use buffered transport in the fixed client; the two legacy chat warmups are omitted and the changed warmup condition is declared. No engine or GPU-runner binary changed. Activation preserved22 prior clock files and all existing profiles. R458 defines a new full-category4096-token output profile; the earlier1024-token pilot remains separate and supplies no silently pooled scores. Existing research-weight ownership was mapped to LXC root with identical before/after full-file hashes and unchanged permission bits; the private Gemma mapping remains read-only. This is data admission, not a performance or quality qualification.

The first ordinary coding suite for an already verified native model passed **131 CPU controls**. It retains the same model, engine, template, sampler, context and warmups, dropping only tool-dispatch options. R459 then exposed a submission timing defect: its systemd deadline condition rejected the wrapper before any model load or task execution. The failure, one-shot marker and original clock remain preserved. The corrected task-wrapper calculation reserves the existing30-second submission allowance **inside** the unchanged wall limit; the strict launch condition and1200-second task deadline are unchanged. **134 CPU controls passed**, including startup-delay reproduction, exhausted/wrong-phase rejection and the earlier admission/hardware cases. Activation preserved26 historical clock files, all prior profiles and the engine/runner bytes. R460 is the first actual inference attempt for that profile, not a renewal after generated tasks. Its eventual quality result is independent of this admission check.

[R460](experiments/R460.md) reached the task deadline with93 completed coding replies; isolated CPU scoring found85 passes. The controller collected the partial artifacts but did not emit its normal completion/hash manifest. The first CPU observer therefore failed. Post-stop recovery verified every completed reply against the original host-captured event stream and pinned the actual unprivileged launch before scoring. The derived integrity receipt is explicitly identified as post-stop evidence; no successful controller completion was fabricated, and no inference or clock was restarted. This remains a PARTIAL result, not a full164 score. Counter-energy bounds cover exactly the93 completed requests and intervening setup, excluding the unfinished trailing request. The original failed power integral remains unknown. An initial unpublished counter receipt was rejected because it replaced the fixed method's scope text; the corrected receipt restores that metadata without changing any numeric bounds. Both receipts and the original observer failure remain preserved.

The archived native-agent data format used for R462 passed **137 CPU controls**. Every original agent request/reply, exact warmup, sampler and original raw hash is checked against the protected source capture; unknown row kinds, missing replies and changed samplers fail closed. The engine still requires an independently completed broker execution with the actual unprivileged UID. No legacy UID, BFCL capture or new executable is invented. Activation preserved31 prior clock files and all existing profiles. The complete published27B artifact contains MTP tensors; R462 explicitly requests no speculative inference. Engine/runner/weight bytes and hardware limits were unchanged.


## Opt-in native HTTP response deadline after R470

[R470](experiments/R470.md) preserved **242/260** independently scored native-tool successes. The next response was still generating when the fixed **120-second HTTP client timeout** fired. This was a transport failure before the overall task deadline; it is not a full400 score, a model-quality rejection or permission to reset the campaign. The original controller/observer failure, completed replies and post-stop integrity review remain preserved. Counter costs cover the260 completed requests only and exclude the incomplete trailing request.

The reviewed client correction is explicitly enabled by a new root-owned profile using `REMAINING_TASK_TIME`. Legacy profiles retain their120-second timeout. An opted-in generation may wait only until the **remaining existing task deadline**, bounded by the original1200-second contract; startup/warmup and the independent signal/broker deadlines remain enforced. The experiment cannot supply arbitrary timeout values. Model weights, engine/kernel binaries, GPU-runner bytes, privilege separation, leases, power/VRAM/thermal/ECC guards and production services are unchanged.

**161 CPU regression controls passed** before atomic activation, including the previous156 admission/deadline/hardware controls and five opt-in timeout controls. Unknown policies, invalid budgets and expired/forged deadlines fail closed. Activation preserved every existing profile and all55 prior clock files, with original source/trust bytes retained for rollback. This qualifies the scoped client safeguards, not a GPU speedup or model winner. Any new model result still requires its own real execution and independent quality audit.

## Parallel/multiple tool-composition category

The next category uses all **200 original BFCL v4 `parallel_multiple` tasks**, pinned to the same upstream revision as the existing simple-call category. It has its own dataset hash, official AST category, scorer-wrapper identity and qualification. It is neither a subset of `simple_python400` nor a full-BFCL overall score. Model answers remain distinct from synthetic scorer controls.

**178 CPU regression controls passed** before transactional activation: the161 preceding controls and17 new category/input checks. The broker requires a protected prior native-model execution, identical model/engine/template/sampler, the exact complete ordered200 inputs, reviewed source/scorer evidence and current executor identities. It rejects altered datasets, new executables, parameter changes, forged execution evidence and increased limits. Historical validation reports are preserved; their old hashes cannot approve changed executor software. Existing profiles and58 previous clock files were unchanged.

Before any generation, the isolated client applies the actual model template and tokenizer to every selected input and verifies context plus output budget under the existing startup limit. This is a technical input check, not a model-quality gate. Generation still has one1200-second task clock, with no partition resets or retries. Model weights, engine/kernel and GPU-runner binaries, privilege separation, one-job lease, power/VRAM/thermal/ECC protections and production services are unchanged. Full-category quality admission and any model comparison require the resulting original responses and independent CPU scoring; the admission tests themselves are not benchmark results.

[R472](experiments/R472.md) qualified **154/200** locally with identical CPU replay. Its frozen campaign plan retained an unused copied `new_count=400` description. The executed contract, native request cap, original ordered inputs, preregistered expected count, captured replies and scorer all used200. An append-only metadata correction preserves the original plan; no task, answer, clock or score was changed or rerun.


## Technical wrapper stop: R473 partial preservation

[R473](experiments/R473.md) retained **165/197** official AST successes, identically rescored on the CPU, after the actual outer systemd wrapper reached its admitted1310-second limit. The native1200-second task deadline was not itself observed as exhausted; three original tasks remain unknown. The first CPU observer rejected the unfamiliar stop signature. Recovery pins the original protected start marker and initial clock, exact root systemd unit/PID/UID timeout events and original response/telemetry hashes. It preserves the original failure and clocks and does not fabricate a controller-success receipt. **Five additional CPU negative controls** reject changed sources, unknown runners, unprotected markers, wrong contracts/policies, manual/incorrect-unit stops and mismatched timeout timestamps. GPU admission, source assets, guards and time limits were not changed, and no inference was repeated.

The public record remains **PARTIAL,165/197 of200 intended**, with no full-category admission or model rejection. Reported-counter energy is2011.080–2011.746GPU-J per165 successes for exactly the197 completed requests and intervening setup; the incomplete trailing request, startup, warmup and CPU/system energy are excluded. The failed power integral and missing task-end marker remain unknown.

An **exploratory common-prefix comparison**, selected solely by the197 original IDs completed by both profiles, finds Gemma151/197 and Qwen3.8 165/197. Qwen's complete-HTTP time is3.613 times Gemma's; its reported-counter joules per success are3.797–3.803 times as high. These are two different native whole profiles with different model sizes, quantization, templates and samplers, one generated answer set each. The wrapper-selected prefix is not a random holdout, a complete200-task ranking, causal optimization evidence or a Champion qualification. Full-session VRAM peaks retain their original coverage and are not relabelled as separate prefix measurements.

The reproducible comparison is retained with original source/audit hashes and ordered task IDs. Original analysis SHA256: `848c73aa5b0a3127691263f5b7c5fa92e0d03ed3332d6321d0a51731df4ec096`.

## R476 — existing LFM8 complex-tool baseline

The original LFM2.5-8B-A1B Q6_K native profile completes the full BFCL v4 `parallel_multiple` category: **170/200**, with an identical independent CPU replay. Pure task time is **641.971598066s**, completed-request time641.844368499s and peak device memory7442.5MiB. Reported counter bounds are **730.922–731.419 GPU-J per170 successes**, covering exactly200 completed requests including failed answers. One incomplete power integral remains unknown; counter energy does not fill it. This is a normal model-profile comparison, not a full-BFCL score or causal optimization test.

The registered trial string accidentally retains a copied descriptive `qwen35` component. The actual selected immutable LFM profile, source R453, weight hash, engine launch and configuration artifact identify LFM8 throughout. An append-only label correction binds the original contract; the contract, budget and original outputs were not renamed or restarted.

## Retrospective common171-task comparison

On the same original171 task IDs completed by all of R472–R475: Gemma scores127/171 in270.009 completed-HTTP seconds; Qwen3.8 scores143/171 in977.029s; Qwen3.5 scores148/171 in389.325s; Bonsai scores145/171 in1194.523s. The independent source/hash/counter review is pinned by SHA256 `77393c91f2fc2662bff16c3721c033326d3b8c3328225f0bc066db264bd47784`. This selection is determined retrospectively by Bonsai's runtime cap, **not** a random holdout or the complete200-task benchmark. Native samplers, templates, weights, engines and quantizations differ. Original full/partial results are unchanged; no new generation, leaderboard row, causal optimization result or Champion promotion is introduced.

## No-call safety category — CPU preparation only

The original official BFCL irrelevance oracle can credit empty output or decoding failures as no-call success; this is preserved as official scoring semantics and does not establish practical tool safety. A separately versioned practical adapter additionally requires a complete, nonempty final assistant response and no native tool call. Omitted, empty-list and nullable no-call representations are equivalent; truncated, malformed, thinking-only and API-error outputs cannot qualify. **4,560 synthetic CPU checks** cover240 original task schemas and19 response variants without any model query or tool execution. Historical scorers and scores remain unchanged. The category still requires its own official full240 wrapper, registered definition, closed root admission and negative policy controls before any GPU use; there are no model results for it yet.

## R477 — complete low-scoring LFM24 complex-tool profile

The existing LFM2.5-24B-A2B QAD Q4_0 native profile completes all200 original parallel/multiple tasks: **6/200 (3%)**, with identical independent official-AST replay. All200 response envelopes are protocol-valid and complete. Pure task time356.535669929s, complete-request time356.417828738s, peak13788.5MiB. Reported counter bounds are **9622.956–9632.822 GPU-J per6 successes**, covering all200 completed requests including194 unsuccessful answers. Missing integral energy remains unknown. Qualification here means this category measurement is verified; **it does not mean a successful optimization**.

A CPU-only shape review finds193 single-call replies, two with two calls, three with three calls and two with four calls. The captured template can render a call list and does not reference `parallel_tool_calls`; that request field was omitted. Absence alone does not prove parallel decoding disabled, and the same engine successfully handled the LFM8 complex profile. No isolated template, parser, sampling or model cause has been established. The source review is pinned by SHA256 `f59475be7fa8c0ad9a67c505f9189d8038208fe58d7526b7bf0741a36f5529fc`. Preserve this negative profile result alongside the valid simple400 score; do not extrapolate generic model incapability or silently retry with different settings. A future correction needs a distinct source-backed hypothesis and configuration, using development tasks before another full test. No model download, original-weight change, Champion promotion or additional optimization-axis credit.

## R478 — unchanged OmniCoder reference complex-tool baseline

The retained OmniCoder9B Q6_K reference artifact completes all200 original parallel/multiple cases: **177/200**, identical independent CPU replay. Task502.671012318s, completed-HTTP502.544043479s, peak7356.5MiB; reported counter bounds **797.789–798.373 GPU-J per177 successes**, covering all200 completed requests including unsuccessful answers/setup. Missing integral energy remains unknown. No MTP, cache, sampler, template or other inference optimization was introduced; this fills the missing normal reference-model category. Corrected V1/V2 display identity retains all original artifact and audit hashes; unknown HF provenance stays unknown.

The exact evidenced coding/complex-tool captures share one presentation row, with132/164 coding and177/200 tools linked to their own original experiments and protocols. Qwen3.5's176/200 differs by one task only; no repeat-based performance or general quality superiority is established. Its measured time, memory and reportedJ/success remain lower for this specific native-profile comparison. These are different model/quantization/template/sampler profiles, not a causal isolated optimization test or whole-BFCL score. No Champion pointer or162-factor status was changed.

## R479 and owner-selected comparison scope

The existing Ornith1.5 9B Q6_K native Thinking profile completes the selected parallel_multiple200 category at **171/200**, identical independent CPU replay. Task1045.35263573s, completed-HTTP1045.2234963s, peak7356.5MiB; reported counter1750.553–1751.025 GPU-J per171 successes across exactly200 complete requests including unsuccessful answers. Missing integral energy remains unknown. The existing coding85/93 prefix stays PARTIAL; it cannot enter a complete official coding/tool mean. Native sampling/template differences make this a whole-profile comparison, not a causal optimizer experiment or Champion change.

The owner now fixes exactly one displayed benchmark per decision category: HumanEval+164, BFCL parallel_multiple200 and Terminal-Bench2.1. All other historical suites remain archived, outside the central comparison, all presets, selectors, CSV, analysis and arithmetic mean. CPU preparation for irrelevance240 is retained without a new GPU campaign or displayed tool score. Terminal-Bench local results remain unmeasured and its evaluation definition still requires admission.


## First selected tool category from an executed coding profile

The normal Nexus coding run establishes actual execution of its pinned weights, template and known SM70 engine, even if the task deadline leaves its quality evaluation partial. A closed admission route now permits the selected **parallel_multiple200** category directly from that captured coding profile. It avoids running an unrelated400-task tool category solely to create a tool-profile parent.

The model artifact, complete engine/kernel asset tuple, template, sampler, context/output, inference flags, environment and warmup must match the executed coding capture. Only the fixed native-tools adapter and `tool_choice=auto`, `parallel_tool_calls=true` request envelope may differ. The original200 task identities/order/schema/scorer source review, technical context preflight and one1200-second pure-task clock remain mandatory. This proves eligibility to measure tools; a coding execution or CPU admission test does not prove tool quality.

**196 CPU regression controls** passed: the preceding178 controls plus18 coding-parent admission cases. They reject altered models, engines, runtime flags, sampler, warmup, task identities, hashes, source/parent evidence, executor proofs, resource limits and incorrect tool envelopes. Old policy functions, guard/lease/registration/budget logic and source checks remain structurally unchanged except one closed dispatcher branch. The extension was atomically activated after Nexus collection and independent CPU review were terminal; all old profiles, registry records, original proof hashes and85 existing clock files were preserved. GPU/engine/runner binaries and production services were unchanged. No GPU calls occurred in migration validation.

## Screened Gemma K-cache: bounded full-category confirmation

The closed K01 route now admits the already screened Gemma QAT Q4_0 candidate to the complete BFCL v4 `parallel_multiple200` category. Only K-cache storage changes from F16 to Q8; V remains F16. Model, engine, template, sampling, context, warmups and every other inference setting must match the captured reference. Admission additionally verifies the actual development capture and its identical independent CPU replay. The mixed Q8/F16 attention-vector specialization is absent from this build; the observed F16 conversion fallback remains unchanged.

**235 CPU regression controls passed**, including all preceding 228 and seven full-category admission controls. Untrusted raw captures cannot serve as root-owned evidence in place. The adapter, privileged runner, hardware guards, leases and budget enforcement remain unchanged. All 175 existing budget files and prior profile/review identities were preserved. Each full benchmark retains one 1,200-second task clock, with startup and CPU scoring separate; admission does not certify quality, safety or a Champion. Original source-review SHA256: `bfd8856677f4da956120c76b15546c03d11ed492b3512b1a2c4f280f02a956b7`.

R513 completed all 200 tasks in 354.546504386 task seconds: **158/200** official AST and practical protocol, with identical independent CPU replay. Peak VRAM was 7,986.5 MiB versus 8,118.5 MiB for stored F16 reference R472 (**132 MiB lower**). The reference scored 154/200 in 333.794263795s. Reported-counter energy was 530.062–530.560 GPU-J/success versus 528.354–528.988; failed completed requests are included. The predeclared tool-quality/memory gates pass, while coding/stability confirmation remains pending. No speed, population quality, energy or Champion superiority is claimed from one candidate and one stored reference. The failed initial CPU qualification-helper lookup was corrected without rerunning inference or modifying the original audit.
