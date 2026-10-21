# HBM15 — VMM and allocator fragmentation

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Disabling virtual-memory management changes allocation behavior and memory overhead. Warm throughput does not establish cold-start or fragmentation effects.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-ccaadd14ebc9e9edc4d9.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | READY_LINKED | See linked original evidence | Not separately reconciled |
| no_vmm_build | READY_LINKED | See linked original evidence | Not separately reconciled |


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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
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

Existing C06 no-VMM comparison covers that allocator toggle, not arbitrary fragmentation or VMM architecture.

**Remaining scope:** New allocator claim needs a reproducible allocation/lifetime fragmentation trace and an actual changed allocator; repeated no-VMM flag is not new evidence.

**Reopening condition:** New allocator claim needs a reproducible allocation/lifetime fragmentation trace and an actual changed allocator; repeated no-VMM flag is not new evidence.

**Next action:** Retain C06; only admit a measured allocation problem and a bounded fix.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
