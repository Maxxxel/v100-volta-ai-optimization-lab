# HBM11 — Paged attention and KV blocks

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| OPEN | False | False | P3 |


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

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | See linked original evidence | Not separately reconciled |
| paged_port | BLOCKED | See linked original evidence | Not separately reconciled |


### Recorded model-specific variant coverage

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

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

PagedAttention erfordert echte Blockverwaltung/Operatoren; kein neuer zugelassener Pfad. Aktuelle qualifizierte Profile sind Einzelslot-Profile, R11 war ein Kontextdeckel.

**Remaining scope:** Nur mit begründetem Mehrsequenz-/Fragmentierungsworkload und kompatiblem Operator priorisieren; kein zusätzlicher Allocator ohne belegte Lücke.

**Reopening condition:** Qualify serial semantics and real multi-session pressure before a new allocator.

**Next action:** Qualify serial semantics and real multi-session pressure before a new allocator.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md)
