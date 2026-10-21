# Research methodology

Golden Baseline A0 is immutable per reproducible workload identity. Current Champion C is the best independently qualified configuration in that same profile. New candidate B first runs a cheap screen against valid stored references; only promising or materially uncertain cases receive fresh controls. Balanced sequences are used when drift or small differences justify them.

Pre-register the primary metric, practical improvement threshold, quality/numerical gates, maximum time and early-stop rule. Reject on quality or correctness loss regardless of synthetic speed. Keep failures, incomplete screens and outliers under their original rules.

Separate GPU/engine throughput, numerical kernel correctness, coding, native tool calling, isolated agent tasks and hardware telemetry. Use exact input IDs within one tokenizer; across models use the same tasks with correct templates and successful tasks per second/joule.

Prefill, decode, streaming TTFT, total task latency, device/process VRAM and GPU-energy integrals are different quantities. Buffered output does not measure visible TTFT. GPU energy excludes CPU/host energy unless explicitly stated. HBM-internal electrical energy cannot be identified from board-level NVML alone.

The original twelve quality tasks remain unchanged. HumanEvalPlus uses joint base AND plus success; a larger auxiliary count is not the same score. Repeated observations within one process do not establish independent sessions or broad model superiority. Frozen development suites are not unseen holdouts.

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
