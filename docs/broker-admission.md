# Safe research admission

Risk classes replace per-factor GPU approvals. A negative optimization result is scientific evidence about its tested configuration; it is not a ban on a distinct model or matrix-shape hypothesis.

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
| Broker regression suite | 29 tests passed | Policy boundaries, bad identities/hashes, compatibility, hardware faults, parallel starts, invalid-registration rollback, source links and scoped termination |
| Isolated source/build probes | Passed | UID 65534, read-only source/system, no GPU devices or protected host files, output quotas and ELF dependency capture |
| [R446](experiments/R446.md) | 12/12 new PQ2 boundary cases passed | Fixed native CPU/CUDA comparison, NMSE bound 5e-4; 806.5 MiB peak device memory |
| Candidate namespace GPU regression | One case passed | Reviewed original binaries through the new unprivileged namespace path; not an additional optimization factor |

Three submitted infrastructure failures occurred before native GPU execution during migration. Their logs and one-shot markers remain intact. Fixes addressed the LXC lock-file mount, private file transfer and the distinction between raw reserved NVML bytes and the existing idle rule. No valid benchmark was rerun to repair those startup failures.

R446 does **not** qualify a routing change, speedup, whole-model numerical equivalence or a Champion. Historical negative FORCE_MMQ results and all existing model/reference profiles remain unchanged.
