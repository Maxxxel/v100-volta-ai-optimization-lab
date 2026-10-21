# HBM16 — Attention and recurrent-state memory

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

GDN state-write fusion can remove copies when state type and layout match. F32-only cache fusion cannot silently be combined with F16 state storage.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2da70f9a1f9f3bf94e45.md)
- [Original audit hash and public excerpt](../audits/audit-37fda1f10a4731b174fa.md)
- [Original audit hash and public excerpt](../audits/audit-3d840b4f87513c2af730.md)
- [Original audit hash and public excerpt](../audits/audit-7e7065168ccf20c177ee.md)
- [Original audit hash and public excerpt](../audits/audit-894272c69b792fd8736e.md)
- [Original audit hash and public excerpt](../audits/audit-8fb7e72fcd73c8402e82.md)
- [Original audit hash and public excerpt](../audits/audit-9907670c98fb135ab20f.md)
- [Original audit hash and public excerpt](../audits/audit-c16b8748920037f57079.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | See linked original evidence | Not separately reconciled |
| state_fusion_port | BLOCKED | See linked original evidence | Not separately reconciled |


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
        "value": "state_fusion_port"
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
        "value": "state_fusion_port"
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
        "value": "state_fusion_port"
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

C13 recurrent fusion and existing seeded state checks do not qualify reduced-precision state, speculative rollback or all long sessions.

**Remaining scope:** A recurrent-storage precision candidate needs concrete dispatch/storage support, CPU state oracle and long-sequence drift bounds before GPU quality qualification. Attention-KV flags do not implement GDN state compression.

**Reopening condition:** A recurrent-storage precision candidate needs concrete dispatch/storage support, CPU state oracle and long-sequence drift bounds before GPU quality qualification. Attention-KV flags do not implement GDN state compression.

**Next action:** Reuse C13 and K05/R291-R292 scopes. Do not infer a state bug merely from altered prompts or speculative outputs.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R237](../experiments/R237.md), [R238](../experiments/R238.md), [R291](../experiments/R291.md), [R292](../experiments/R292.md)
