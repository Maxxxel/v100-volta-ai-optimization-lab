# HBM20 — StreamDQ custom HBM

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| NOT_APPLICABLE | False | False | P3 |


## Theory and Volta implications

Custom HBM hardware cannot be enabled by software on an existing V100. External architectural results require different physical equipment.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)
- [Original audit hash and public excerpt](../audits/audit-bc43e8b613cc983bfb4a.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| stock_hbm2 | NOT_APPLICABLE | PARTIAL | False |
| custom_hbm_streamdq | NOT_APPLICABLE | NOT_APPLICABLE | False |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "stock_hbm2"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "custom_hbm_streamdq"
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
        "value": "stock_hbm2"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "custom_hbm_streamdq"
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
        "value": "stock_hbm2"
      },
      {
        "historical_states": [
          "NOT_APPLICABLE"
        ],
        "signed_window_signatures": [],
        "value": "custom_hbm_streamdq"
      }
    ],
    "model": "qwen38"
  }
]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Custom HBM hardware is not retrofittable through a CUDA flag on this V100; excluded from local software sprint.

**Remaining scope:** None identified beyond already reviewed evidence; do not automatically repeat.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** A different physical memory architecture; software caches are separate factors.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | NOT_APPLICABLE |
| decision | KEEP_PHYSICAL_HARDWARE_NOT_APPLICABLE |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Custom HBM hardware is not a software modification to the installed V100. |
| new GPU execution | False |
| next action | A different physical memory architecture; software caches are separate factors. |
| previous status | NOT_APPLICABLE |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R390](../experiments/R390.md)
