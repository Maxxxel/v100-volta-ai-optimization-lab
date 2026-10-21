# HBM18 — Volta-specific flash attention

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Flash attention fuses attention operations to reduce intermediate memory traffic. Actual support depends on head dimensions, KV formats and compiled SM70 kernels.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md
- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2d48a4fdae7ce747ef64.md)
- [Original audit hash and public excerpt](../audits/audit-4a63c493e0301a646d00.md)
- [Original audit hash and public excerpt](../audits/audit-6924d1fa43aaa9766b96.md)
- [Original audit hash and public excerpt](../audits/audit-9de95af06dcc3290e44f.md)
- [Original audit hash and public excerpt](../audits/audit-a200c5c240a36583e62e.md)
- [Original audit hash and public excerpt](../audits/audit-b8a83b89fd187aadf424.md)
- [Original audit hash and public excerpt](../audits/audit-e950bd432e12a6880a36.md)
- [Original audit hash and public excerpt](../audits/audit-f2e1299acd91cad7c2df.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | READY_LINKED | See linked original evidence | Not separately reconciled |
| on | READY_LINKED | See linked original evidence | Not separately reconciled |
| volta_fork_port | IMPLEMENTED_QUEUED | See linked original evidence | Not separately reconciled |


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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "IMPLEMENTED_QUEUED"
        ],
        "signed_window_signatures": [
          "074f9b8f5ed37d6d90aea4a2fb0740183eae381ce69424317ff1916b692aaf4a",
          "2f1977a5bc7e15ef49e9df3f1021dda4613baadc4d0cbf2263b38cd1e2b1269e",
          "e6b4a6c04ff44953d91ed4ce71fdb2f1b0aa477663d01b5e3bdca230eb653007"
        ],
        "value": "volta_fork_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "volta_fork_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "volta_fork_port"
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

Qualified Volta attention fork/numerical evidence remains valid in its own scope; failed early instrumentation does not erase later evidence.

**Remaining scope:** A new attention kernel needs an implemented D256/SM70 path and numerical/state/quality equivalence; Ampere-only FlashAttention cannot be treated as a ready Volta variant.

**Reopening condition:** A new attention kernel needs an implemented D256/SM70 path and numerical/state/quality equivalence; Ampere-only FlashAttention cannot be treated as a ready Volta variant.

**Next action:** Reuse qualified fork evidence; no repeat or new label for identical attention path.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
