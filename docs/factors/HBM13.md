# HBM13 — OasisKV sparse lookahead prefetch

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

Sparse lookahead prefetch changes token selection and memory access. Dense attention quality and actual sparse execution must be independently checked.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-18b8188a10fb7bf8b528.md)
- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| dense_reference | BLOCKED | PARTIAL | False |
| oasiskv_port | BLOCKED | DEFERRED | False |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "dense_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "oasiskv_port"
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
        "value": "dense_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "oasiskv_port"
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
        "value": "dense_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "oasiskv_port"
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

HBM13 OasisKV source admission: published v1 implements head-wise min/max key summaries, draft-query block prediction, capped replacement and asynchronous pinned-host KV gathering on a modified vLLM0.12 serving path; evaluation uses H100 and different models. No matching Omni/GDN SM70 implementation was established. The exact D256 CPU algebra control proves that a valid min/max block bound can rank the wrong block even with an exact query; this is not a measured task-quality regression or rejection of approximate selection. Local metadata imply 1GiB F16 attention-KV payload at32K for8attentionlayers/4KVheads/D256; this is analytical payload accounting, not observed VRAMsaving. ExistingR396data contain preRoPEK/V but no draft/target query sequence or attention importance labels, so they cannot validate this lookahead predictor. Defer full port until a compatible sparse operator, head-wise cache map, partialIMRoPE/GDN rollback and transfer/event lifecycle are concretely implemented. No newGPUrun, modelquality, speed or energymeasurement; coverageNEIN.

**Remaining scope:** Source-defined lookahead sparse KV port and meaningful exact-model selection/transfer tests remain unimplemented; not a universal hardware exclusion.

**Reopening condition:** A concrete source-pinned SM70 sparse operator and exact-model state/query oracle admit a bounded component test; whole OasisKV requires staged transfer and event ownership plus real quality/resource evidence. Future engine changes may reopen it.

**Next action:** A concrete source-pinned SM70 sparse operator and exact-model state/query oracle admit a bounded component test; whole OasisKV requires staged transfer and event ownership plus real quality/resource evidence. Future engine changes may reopen it.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_OMNI_SPARSE_LOOKAHEAD_PORT_DEFERRED |
| expected benefit | Unverified; no local performance forecast. |
| new GPU execution | False |
| next action | Pinned executable SM70 operator, exact-model query/attention oracle on non-benchmark calibration data, transfer/event ownership and a practical cost hypothesis. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R396](../experiments/R396.md)
