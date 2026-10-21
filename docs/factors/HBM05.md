# HBM05 — Volta FP16 Tensor Core kernel

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| TESTED_NEGATIVE | True | True | P3 |


## Theory and Volta implications

Volta supports FP16 Tensor Cores with architecture-specific MMA layouts and synchronization. New lane permutations need numerical and executed-path evidence.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-083ec3e6b24d6e01589b.md)
- [Original audit hash and public excerpt](../audits/audit-68f29d4a2beebd20e166.md)
- [Original audit hash and public excerpt](../audits/audit-d798c15e0eb73ae5a51c.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | PARTIAL | False |
| volta_fp16_patch | BLOCKED | TESTED_NEGATIVE | True |


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
        "value": "volta_fp16_patch"
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
        "value": "volta_fp16_patch"
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
        "value": "volta_fp16_patch"
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

R81 unverändert wiederverwendet: kein praktisch relevanter Gewinn, Antworten/Token identisch. Geprüfte Permutationsvariante verworfen; unabhängiges Kernel-Numerikorakel fehlt. Keine neue Messung oder Neubau.

**Remaining scope:** None identified beyond already reviewed evidence; do not automatically repeat.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** R81 scope is tested negative. No repeat build/benchmark or generic oracle run absent a materially new eligible MMA implementation.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R357](../experiments/R357.md), [R81](../experiments/R81.md)
