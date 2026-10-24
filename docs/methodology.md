# Research methodology

**Current task budget:1,200 seconds total per benchmark**, shared across all parts without resets. Startup, wrapper, cleanup and CPU evaluation limits are separate. Older900-second experiments keep their historical conditions.

Golden Baseline A0 is immutable per reproducible workload identity. Current Champion C is the best independently qualified configuration in that same profile. New candidate B first runs a cheap screen against valid stored references; only promising or materially uncertain cases receive fresh controls. Balanced sequences are used when drift or small differences justify them.

Pre-register the primary metric, practical improvement threshold, quality/numerical gates, maximum time and early-stop rule. Reject on quality or correctness loss regardless of synthetic speed. Keep failures, incomplete screens and outliers under their original rules.

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
