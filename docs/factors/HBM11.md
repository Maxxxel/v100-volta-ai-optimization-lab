# HBM11 — Paged attention and KV blocks

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

Paged KV allocation can reduce fragmentation in serving. It needs compatible attention kernels and a real multi-sequence capacity problem.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)
- [Original audit hash and public excerpt](../audits/audit-89b244b35fdb3b8b755e.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | PARTIAL | False |
| paged_port | BLOCKED | DEFERRED | False |


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
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "paged_port"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "paged_port"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "paged_port"
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

HBM11 current-engine admission: exact pinned get_k/get_v expose strided 4D views into preallocated KV buffers; hybrid preparation couples attention allocation with recurrent batches and trailing rollback snapshots. Sequence copy/remove and state serialization update both memory classes. A block-table allocator alone therefore is not a PagedAttention implementation. Existing R376 two-slot history-isolation gate remains failed (20/21 matching prefix responses), and R343 vLLM namespace mapping remains incomplete (379/427 names; GDN/norm/layout inversion required). These are retained independent findings, not fresh HBM11 quality/performance tests. No admitted exact-model paged operator plus hybrid lifecycle adapter currently exists. Defer the current-engine port pending a concrete adapter and a useful fragmentation/sharing workload; this does not exclude SM70 PagedAttention or future single-sequence/component tests. No GPU/model launch or speed/VRAM/energy claim.

**Remaining scope:** Current exact-model engine port deferred, not universal architectural exclusion; compatible component and future serving tests remain possible.

**Reopening condition:** A concrete exact-model operator/cache patch and bounded correctness oracle admit a component test without waiting for all serving work. Whole multi-session qualification additionally requires demonstrated preserved histories. Separate vLLM route requires its existing weight/graph/SM70/16GB admission, not a new installation now.

**Next action:** A concrete exact-model operator/cache patch and bounded correctness oracle admit a component test without waiting for all serving work. Whole multi-session qualification additionally requires demonstrated preserved histories. Separate vLLM route requires its existing weight/graph/SM70/16GB admission, not a new installation now.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_CURRENT_ENGINE_PAGED_PORT_DEFERRED |
| expected benefit | Unverified; no local performance forecast. |
| new GPU execution | False |
| next action | A concrete exact-model block-table-aware attention operator plus hybrid KV/GDN copy-on-write/reset/rollback contract and bounded correctness oracle. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R396](../experiments/R396.md)
