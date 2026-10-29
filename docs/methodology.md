# Research methodology

**Current task budget:1,200 seconds total per benchmark**, shared across all parts without resets. Startup, wrapper, cleanup and CPU evaluation limits are separate. Older900-second experiments keep their historical conditions.

Golden Baseline A0 is immutable per reproducible workload identity. Current Champion C is the best independently qualified configuration in that same profile. New candidate B first runs a cheap screen against valid stored references; only promising or materially uncertain cases receive fresh controls. For drift-sensitive or small effects, preregister a balanced ABBA or BAAB order; otherwise use a simpler paired A/B when it can resolve the decision. Keep the same task IDs, tokenized inputs, seed policy and execution budget across arms.

For every A/A or A/B repeat, record whether each request uses a fresh process, fresh slot, reset state, or intentional prefix/cache reuse. Do not call a state “reset” unless the engine operation and logs verify it. Compare paired task outcomes and first token/state divergence; preserve run order and session identity. If cache state is the treatment, change only that state and report both the request-level path and whole-task outcome. Repeated requests within one session are correlated observations, not independent quality samples. ABBA/BAAB controls order drift; it does not by itself establish statistical independence or causality.

Pre-register the primary metric, practical improvement threshold, quality/numerical gates, maximum time and early-stop rule. An observed quality or safety loss blocks promotion regardless of speed; a bounded investigation must distinguish a reproducible effect from baseline variability before attributing its cause. Preserve the original gate decision, failures, incomplete screens and outliers.

## Reproducibility and uncertainty

Check the request and server-reported sampler settings against the frozen profile. A fixed seed and temperature zero do not guarantee identical GPU outputs. Characterize baseline A/A repeatability with matched prompt bytes and token IDs, engine, checkpoint, seed, cache/slot lifecycle and resource limits. For stochastic profiles, repeat prespecified seeds and compare distinct seeds without treating correlated repeats as independent quality samples.

When a potentially useful candidate changes a task or policy outcome, retain the failed gate and investigate baseline variation and the earliest token/state divergence. Use a fresh balanced paired A/B order when feasible; compare task-level outcomes and disclose uncertainty and correlated task families. No observed difference does not establish equivalence or noninferiority. Any new policy violation blocks promotion and requires investigation; authorization is enforced outside the model.

Separate fixed-token prefill/decode measurements from complete agent latency, output length, tool calls and GPU joules per successful task. Fewer generated tokens alone do not demonstrate higher kernel throughput. Record actual cache hits, state resets and missing logits or token identities explicitly.

Separate GPU/engine throughput, numerical kernel correctness, coding, native tool calling, isolated agent tasks and hardware telemetry. Use exact input IDs within one tokenizer; across models use the same tasks with correct templates and successful tasks per second/joule.

Prefill, decode, streaming TTFT, total task latency, device/process VRAM and GPU-energy integrals are different quantities. Buffered output does not measure visible TTFT. GPU energy excludes CPU/host energy unless explicitly stated. HBM-internal electrical energy cannot be identified from board-level NVML alone.

The audited `task_phase_s` includes input/template/token preparation between requests. The sum of completed HTTP windows is separate. Recorded `startup_s` starts at the protected broker clock and can include asset checks, model loading and warmups; it is not a pure model cold-start measurement. An interrupted trailing request is excluded from completed-request energy and latency summaries unless an explicit whole-window measurement says otherwise.

The original twelve quality tasks remain unchanged. HumanEvalPlus uses joint base AND plus success; a larger auxiliary count is not the same score. Repeated observations within one process do not establish independent sessions or broad model superiority. Frozen development suites are not unseen holdouts.

Official percentage admission must match the recorded numerator and denominator. A complete BFCL v4 Simple Python category uses its own AST-accuracy metric over all 400 unique official tasks; it is separate from the BFCL overall leaderboard and the historical static100 pilot. The metric adapter alone admits no model result: pinned scorer/configuration identities, complete coverage, controls and independent audit evidence are still mandatory. Missing results remain NOT MEASURED.

Native broker campaigns use their frozen data contracts and captured launch/profile receipts; no preflight plan is invented retrospectively. Full coding result export verifies all 164 unique tasks, every bounded part and scorer output, unchanged model/runtime configuration, and measured task costs. A complete local result still requires a separate official-API qualification before entering the official local highscore view. Partial campaigns retain actually scored task subsets in the research archive, with their original denominators and PARTIAL status; the central comparison admits only complete qualified category results. Unfinished or uncollected tasks are not zero; no full-suite official admission is implied.

## Status semantics

| Status | Meaning |
|---|---|
| QUALIFIED | Independently confirmed only within the named scope |
| TESTED_NEGATIVE | Valid test without sufficient benefit or with quality loss |
| PARTIAL | Only specified variants/components tested |
| OPEN | Insufficient technical or experimental evidence |
| DEFERRED | Specific documented prerequisite/cost blocks execution |
| NOT_APPLICABLE | Architecture, hardware or task mismatch |


Experimental coverage is an independent boolean. A status decision, review, build or download is not a GPU intervention. Component coverage does not imply OmniCoder2 model coverage.

## Pipeline decision

[Retrospective screening evidence and Nexus/Jarvis development plan](pipeline-methods.md). CPU-only study; official results and GPU admission policy remain unchanged.
