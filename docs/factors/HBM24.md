# HBM24 — Fork-specific experimental attention

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| NOT_APPLICABLE | False | False | P3 |


## Theory and Volta implications

Fork-specific attention architectures can require different trained weights and operators. Model changes are not retrofitted runtime flags.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| qwen35_reference | NOT_APPLICABLE | PARTIAL | False |
| qwen4exp_qsa | NOT_APPLICABLE | NOT_APPLICABLE | False |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen35_reference"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen4exp_qsa"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen35_reference"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen4exp_qsa"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen35_reference"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "qwen4exp_qsa"
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

Current artifacts are qwen35 architecture, not qwen4exp; unavailable model-specific path not executed.

**Remaining scope:** None identified beyond already reviewed evidence; do not automatically repeat.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** Omni-GGUF ist qwen35, nicht qwen4exp/QSA; passende andere Architektur ist spätere Modellphase.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md)
