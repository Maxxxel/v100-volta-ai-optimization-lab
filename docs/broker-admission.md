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
