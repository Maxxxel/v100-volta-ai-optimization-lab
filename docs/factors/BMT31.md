# BMT31 — Q4/Q6 conversion-cache transfer

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| QUALIFIED | True | True | P0 |


## Theory and Volta implications

This research subcase investigates q4/q6 conversion-cache transfer. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Persistent conversion or shared/cache reuse can reduce redundant reads and dequantization. It consumes capacity and can change the workload that fits.; Fused dequantization and matrix products avoid materialized intermediates. Existing fused defaults must not be presented as a newly achieved speedup.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/Qwen/Qwen3.5-9B

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-056d794ebc3542e436de.md)
- [Original audit hash and public excerpt](../audits/audit-273b2160c856596f102f.md)
- [Original audit hash and public excerpt](../audits/audit-ef37383ee044d72312b7.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R88-R90Q6 andR133-R134Q4conversioncache actuallocaltransfer retained. No universaldecodeclaim; additionalrealapplication qualification belongs combinations/finalprofiles.

**Remaining scope:** Offenen Rest auf einen konkreten sinnvollen Einzelversuch prüfen; bestehende Messungen erhalten.

**Reopening condition:** Bestehende Q4/Q6-Konvertierungscache-Qualifikation wiederverwenden; neuer Datentyp benötigt tatsächlichen Dispatch und einen qualitätserhaltenden Zielcheckpoint, kein Alias.

**Next action:** Bestehende Q4/Q6-Konvertierungscache-Qualifikation wiederverwenden; neuer Datentyp benötigt tatsächlichen Dispatch und einen qualitätserhaltenden Zielcheckpoint, kein Alias.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R133](../experiments/R133.md), [R134](../experiments/R134.md), [R90](../experiments/R90.md)
