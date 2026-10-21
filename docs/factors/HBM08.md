# HBM08 — F16/Q8/Q4 attention KV cache

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Paired key/value formats create a joint attention kernel configuration. Individual key and value successes cannot be added to predict the pair.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-052735eb2d4adf83b1bd.md)
- [Original audit hash and public excerpt](../audits/audit-0b65111832a0e7ae153b.md)
- [Original audit hash and public excerpt](../audits/audit-15357beaac0b3905a2ce.md)
- [Original audit hash and public excerpt](../audits/audit-1962b7915d289ed667aa.md)
- [Original audit hash and public excerpt](../audits/audit-22d1d0a5e108bf464b15.md)
- [Original audit hash and public excerpt](../audits/audit-27819b91177b325e92d4.md)
- [Original audit hash and public excerpt](../audits/audit-386203c8d6cf777f3bb9.md)
- [Original audit hash and public excerpt](../audits/audit-62cb102a05278610565d.md)
- [Original audit hash and public excerpt](../audits/audit-652eef515a970abc8d51.md)
- [Original audit hash and public excerpt](../audits/audit-76bd28c3368e61d7c96d.md)
- [Original audit hash and public excerpt](../audits/audit-a2270317169dec422f24.md)
- [Original audit hash and public excerpt](../audits/audit-b4f0a807daebe43f2edf.md)
- [Original audit hash and public excerpt](../audits/audit-f818d211483856d94cf3.md)
- [Original audit hash and public excerpt](../audits/audit-fae4b1903a527efdd0b8.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| f16_f16 | READY_LINKED | See linked original evidence | Not separately reconciled |
| q8_0_q8_0 | READY_LINKED | See linked original evidence | Not separately reconciled |
| q8_0_q4_0 | BLOCKED | See linked original evidence | Not separately reconciled |
| q4_0_q4_0 | BLOCKED | See linked original evidence | Not separately reconciled |


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
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
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
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
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
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
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

Attention K/V storage tests remain distinct from recurrent GDN F32 state; F16/Q8/Q4 evidence is retained by exact side,context and quality scope.

**Remaining scope:** A different KV format or mixed policy needs actual SM70 attention support and independent state/quality tests. Existing negative quantizations must not be silently rescued by combinations.

**Reopening condition:** A different KV format or mixed policy needs actual SM70 attention support and independent state/quality tests. Existing negative quantizations must not be silently rescued by combinations.

**Next action:** Reuse K01/K02/K03 and existing memory screens; isolate new cache policies only when implemented.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R233](../experiments/R233.md), [R234](../experiments/R234.md), [R270](../experiments/R270.md), [R82](../experiments/R82.md), [R83](../experiments/R83.md)
