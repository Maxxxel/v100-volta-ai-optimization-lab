# BMT08 — Hybrid attention KV precision

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P1 |


## Theory and Volta implications

This research subcase investigates hybrid attention kv precision. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Quantizing attention keys reduces KV storage but adds conversion and changes attention scores. It does not quantize the separate GDN recurrent state.; Quantizing attention values reduces KV storage but changes the attention value product. Its error behavior differs from key quantization.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2401.18079
- https://arxiv.org/abs/2402.02750

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-658cb0df8d89b3225ae5.md)
- [Original audit hash and public excerpt](../audits/audit-7b8fd7f0f58f6b5a9c23.md)
- [Original audit hash and public excerpt](../audits/audit-b0139d46e7212cc90689.md)
- [Original audit hash and public excerpt](../audits/audit-d4a5784816404879edc5.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

K01/K02/K03 actualGPU Q8/Q4 attentioncache formats already protocol-audited; recurrentstate remains separatelyF32. No new equivalent KV flag. Longcontext/multislot quality and KVxMTP interactions remain explicit later-workload scopes; cannot infer GDNcompression or general quality from those sweeps.

**Remaining scope:** Beide32K-Q8-Negativscreens übernehmen; keine gemeinsame Key/Value-Variante daraus ableiten. Lange semantische Aufgaben/MTP bleiben getrennt unqualifiziert.

**Reopening condition:** Neue relevante Langkontextqualitätshypothese; native Key/Value-Q8-Negative und unqualifizierte State-Präzision getrennt halten.

**Next action:** Neue relevante Langkontextqualitätshypothese; native Key/Value-Q8-Negative und unqualifizierte State-Präzision getrennt halten.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
