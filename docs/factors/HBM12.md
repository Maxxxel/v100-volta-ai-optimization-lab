# HBM12 — Asynchronous KV prefetch to L2

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| OPEN | False | False | P3 |


## Theory and Volta implications

Prefetching can hide memory latency only if the executed KV access pattern and hardware instructions support it. Volta has no cp.async/TMA.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-1ebeea4faa1f402a49cc.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | BLOCKED | PARTIAL | False |
| sm70_prefetch_port | BLOCKED | DEFERRED | False |


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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "sm70_prefetch_port"
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

HBM12 bleibt ohne gemessenen KV-Eingriff: R242 verändert Q6-Gewichts-Prefetch inMMVQ, nicht Attention-KV-Prefetch. Sein gültiger Negativbefund bleibt separat erhalten. Kein lokal zugelassener KV-Prefetch-Patch/gezielter KV-Bottlenecknachweis; aufwändiger SM70-Pfad deshalb zurückgestellt.

**Remaining scope:** Erst mit KV-spezifischem Zugriffspfad, gemessenem Speicherlatenz-Engpass, isoliertem SM70-Patch und numerischem Attention-Orakel zulassen. Kein cp.async/TMA aufVolta voraussetzen; Gewichts-Prefetch nicht alsKV-Test zählen.

**Reopening condition:** Only reopen with actual KV addresses/instructions exercised; retain R250 scope correction.

**Next action:** Only reopen with actual KV addresses/instructions exercised; retain R250 scope correction.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R242](../experiments/R242.md), [R250](../experiments/R250.md), [R382](../experiments/R382.md)
