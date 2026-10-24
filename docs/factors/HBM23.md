# HBM23 — FlashInfer attention engine

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

FlashInfer needs model-layout, dtype and architecture-compatible implementations. Modern GPU support does not imply SM70 compatibility.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-060728369fad84f595c1.md)
- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| local_reference | BLOCKED | PARTIAL | False |
| flashinfer_port | BLOCKED | DEFERRED | False |


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
        "value": "local_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "flashinfer_port"
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
        "value": "local_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "flashinfer_port"
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
        "value": "local_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "flashinfer_port"
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

EXTERN_BELEGT / CPU source admission only: FlashInfer commit 0179e5b312d6aa0c790e8e571b9037bb277f4dbd README declares SM75+; unchanged check_cuda_arch AST rejects {(7,0)} and accepts SM75/SM80 controls without importing torch or initializing CUDA. Current upstream integration DEFERRED on V100SM70; not a GPU negative or universal rejection of historical forks/algorithm ports. Installing this package or deleting its architecture check does not establish a compatible kernel. Reopening needs a pinned executable SM70 operator plus correct GGUF/hybrid attention/KV/state adapter and numerics.

**Remaining scope:** Historical versions, unofficial forks and isolated kernel ports are not universally ruled out; require exact supported SM70 operator, generated code, Qwen35/GDN-attention state/cache adapter and numerics before any installation/GPU trial.

**Reopening condition:** A real pinned SM70-compatible operator implementation, not merely removal of the version check.; Correct integration with OmniCoder2 GGUF attention/KV and recurrent-state boundaries, with numerical reference tests.; A workload with measurable expected latency/VRAM/energy benefit beyond existing native attention.

**Next action:** Require a real pinned SM70 implementation and cache/state adapter before reopening; no architecture-check deletion trial.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_CURRENT_FLASHINFER_UPSTREAM_SM75_DEFERRED |
| expected benefit | Unverified; no local performance forecast. |
| new GPU execution | False |
| next action | Pinned executable SM70 operator with model-compatible attention/KV/state adapter, numerics, plus a distinct practical workload. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R394](../experiments/R394.md)
