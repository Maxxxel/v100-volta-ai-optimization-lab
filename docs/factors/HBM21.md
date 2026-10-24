# HBM21 — FlashAccel high-bandwidth flash

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| NOT_APPLICABLE | False | False | P3 |


## Theory and Volta implications

High-bandwidth flash systems require different storage hardware. They are not a drop-in HBM2 optimization.

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
| hbf_flashaccel | NOT_APPLICABLE | NOT_APPLICABLE | False |


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
        "value": "hbf_flashaccel"
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
        "value": "hbf_flashaccel"
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
        "value": "hbf_flashaccel"
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

High-bandwidth flash requires hardware architecture changes; SSD PCIe is not equivalent; excluded.

**Remaining scope:** None identified beyond already reviewed evidence; do not automatically repeat.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** Actual supported hardware and its transfer path.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | NOT_APPLICABLE |
| decision | KEEP_PHYSICAL_HARDWARE_NOT_APPLICABLE |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | High-bandwidth flash hardware is not equivalent to the existing PCIe SSD or an HBM allocation flag. |
| new GPU execution | False |
| next action | Actual supported hardware and its transfer path. |
| previous status | NOT_APPLICABLE |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R390](../experiments/R390.md)
