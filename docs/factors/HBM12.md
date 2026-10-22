# HBM12 — Asynchronous KV prefetch to L2

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Prefetching can hide memory latency only if the executed KV access pattern and hardware instructions support it. Volta has no cp.async/TMA.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-07ce3c7d410cc80f1024.md)
- [Original audit hash and public excerpt](../audits/audit-1ebeea4faa1f402a49cc.md)
- [Original audit hash and public excerpt](../audits/audit-8a9c78673e8eca6afc99.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | BLOCKED | PARTIAL | False |
| sm70_prefetch_port | BLOCKED | TESTED_NEGATIVE | True |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant sm70_prefetch_port

```json
{
  "native_numerical_cases": 6,
  "passed_cases": 4,
  "peak_device_vram_mib": 812.5
}
```

## Decision and remaining research

R385: actual SM70 F16 D256 KV-prefetch component executed at Omni16-query/4KV/GQA4 shapes. 4/6 native CPU-reference cases pass unchanged NMSE5e-4; two32K cases fail at0.000724829/0.000741057. Actual long-KV launch grid_y40,nbatch64,next_stride2560; privatepatchedCUDA mapped. Candidate fails numerical admission, no model/performance screen or champion. Unpatched identical-input32K control not measured; patch-caused regression is not established. R242 remains weight-prefetch, not this KV treatment. R384 zero-case attempt remains separate and receives no coverage.

**Remaining scope:** One prefetch prototype numerically screened, not qualified; isolated causal baseline control and useful model speed remain unmeasured. Other KV-prefetch implementations require a genuinely new hypothesis and CPU/native oracle before any model run.

**Reopening condition:** Only after breadth priorities: isolated same-input numerical cause or materially different KV-prefetch mechanism. No tolerance waiver, distance grid or automatic16K model winner.

**Next action:** Numerical gate failed; preserve exact scope and continue another distinct single. No model screen/qualification of this candidate.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R242](../experiments/R242.md), [R250](../experiments/R250.md), [R382](../experiments/R382.md), [R384](../experiments/R384.md), [R385](../experiments/R385.md)
