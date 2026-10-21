# HBM22 — QServe W4A8KV4

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| OPEN | False | False | P3 |


## Theory and Volta implications

QServe is a coordinated weight/activation/KV quantization stack. Independent GGUF Q4 and Q8 results cannot be combined into a QServe claim.

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
| gguf_reference | BLOCKED | See linked original evidence | Not separately reconciled |
| qserve_port | BLOCKED | See linked original evidence | Not separately reconciled |


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
        "value": "gguf_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "qserve_port"
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
        "value": "gguf_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "qserve_port"
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
        "value": "gguf_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "qserve_port"
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

W4A8KV4 benötigt passende Gewichte, Aktivierungs-/KV-Quantisierung und ausgeführte SM70-Operatoren. Kein lokal zugelassenes QServe-Gesamtprofil.

**Remaining scope:** Nicht aus einzelnen Q4-/MMQ-/KV-Ergebnissen einen QServe-Gewinn zusammensetzen; erst kompatible Implementierung belegen.

**Reopening condition:** First prove executable operator coverage; do not add independent Q4/MMQ percentages.

**Next action:** First prove executable operator coverage; do not add independent Q4/MMQ percentages.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md)
