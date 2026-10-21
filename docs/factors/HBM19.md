# HBM19 — Energy per correct task/token

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P0 |


## Theory and Volta implications

Power limits trade clocks, latency and energy. Optimize integrated GPU joules per successful task rather than the lowest watt reading.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-01890c2a82328f8c3796.md)
- [Original audit hash and public excerpt](../audits/audit-07e0c748aa3ce4016cab.md)
- [Original audit hash and public excerpt](../audits/audit-1bcbaa3ce104e67fe6d6.md)
- [Original audit hash and public excerpt](../audits/audit-22786f761eb0e7bce306.md)
- [Original audit hash and public excerpt](../audits/audit-261651f358a67acc29ea.md)
- [Original audit hash and public excerpt](../audits/audit-279bd808c8487b9d9681.md)
- [Original audit hash and public excerpt](../audits/audit-3727ed46efb9075e5bee.md)
- [Original audit hash and public excerpt](../audits/audit-3a5da87dc341e4331390.md)
- [Original audit hash and public excerpt](../audits/audit-46e12a310b5c14e20d97.md)
- [Original audit hash and public excerpt](../audits/audit-6e8fc40945c6d265d61b.md)
- [Original audit hash and public excerpt](../audits/audit-72561777b6d13a0a47fe.md)
- [Original audit hash and public excerpt](../audits/audit-7a099423089cce84e68f.md)
- [Original audit hash and public excerpt](../audits/audit-836a463ab5e93aea2a7d.md)
- [Original audit hash and public excerpt](../audits/audit-93f7fb61b86674e46b11.md)
- [Original audit hash and public excerpt](../audits/audit-aa3173b6909f83dad10b.md)
- [Original audit hash and public excerpt](../audits/audit-b1fac35bfe4735e7500b.md)
- [Original audit hash and public excerpt](../audits/audit-d3d48f461ddbab44a526.md)
- [Original audit hash and public excerpt](../audits/audit-db8ee1f15a2aba4eaeed.md)
- [Original audit hash and public excerpt](../audits/audit-ec82b4c9401ad086f524.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| baseline | READY_LINKED | See linked original evidence | Not separately reconciled |
| quality_adjusted_energy | READY_LINKED | See linked original evidence | Not separately reconciled |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "quality_adjusted_energy"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "quality_adjusted_energy"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "quality_adjusted_energy"
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

Energy per successful task includes failed attempts and whole task time; correct tokens alone are not a useful assistant objective. Existing power profiles remain scoped.

**Remaining scope:** New profile must retain quality, hardware comparability and actual GPU integration. Wall plug/whole-system Joules are unavailable from GPU-only NVML and must remain unmeasured.

**Reopening condition:** New profile must retain quality, hardware comparability and actual GPU integration. Wall plug/whole-system Joules are unavailable from GPU-only NVML and must remain unmeasured.

**Next action:** Reuse H03 energy profiles; actual interaction sweeps wait for singles gate, not a new metric-only GPU run.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R102](../experiments/R102.md), [R103](../experiments/R103.md), [R104](../experiments/R104.md), [R105](../experiments/R105.md), [R106](../experiments/R106.md), [R107](../experiments/R107.md), [R108](../experiments/R108.md), [R109](../experiments/R109.md), [R110](../experiments/R110.md), [R111](../experiments/R111.md), [R112](../experiments/R112.md), [R113](../experiments/R113.md), [R142](../experiments/R142.md), [R143](../experiments/R143.md), [R144](../experiments/R144.md), [R152](../experiments/R152.md), [R153](../experiments/R153.md), [R165](../experiments/R165.md), [R166](../experiments/R166.md)
