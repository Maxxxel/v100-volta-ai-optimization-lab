# HBM01 — Effective bandwidth and roofline

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Roofline analysis compares actual arithmetic and memory traffic. Model bytes divided by time are an estimate, not a measured HBM transaction count.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-d7fc97756655a4112227.md)
- [Original audit hash and public excerpt](../audits/audit-e2e30ac7c1edebb0842f.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| baseline | PARTIALLY_IMPLEMENTED | See linked original evidence | Not separately reconciled |
| measured_roofline | PARTIALLY_IMPLEMENTED | See linked original evidence | Not separately reconciled |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Physical model HBM roofline is not established by copy/WMMA diagnostics or summed kernel durations.

**Remaining scope:** A model-specific eligible CUPTI metric set, bytes-count convention, profiling-overhead control and pinned workload must be admitted before treating a bandwidth counter as optimization evidence.

**Reopening condition:** A model-specific eligible CUPTI metric set, bytes-count convention, profiling-overhead control and pinned workload must be admitted before treating a bandwidth counter as optimization evidence.

**Next action:** Keep diagnostics. Profile actual dominant memory kernels only to decide a concrete patch; no diagnostic-only GPU run counted as a new gain.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R87](../experiments/R87.md)
