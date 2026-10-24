# BMT02 — GDN/MTP rejection, prefix and slot-state correctness

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P0 |


## Theory and Volta implications

This research subcase investigates gdn/mtp rejection, prefix and slot-state correctness. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.; Multi-turn, rejection and restore operations must preserve GDN and attention state consistently. Primitive rollback tests do not qualify the full server scheduler.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2211.17192
- https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2da70f9a1f9f3bf94e45.md)
- [Original audit hash and public excerpt](../audits/audit-3d840b4f87513c2af730.md)
- [Original audit hash and public excerpt](../audits/audit-dc8a8b9d5095ace488a2.md)
- [Original audit hash and public excerpt](../audits/audit-f6ede40a69a9cd5a74b3.md)

### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R292 K05/BMT02: echter Slot-Save/Erase/Restore für2 unveränderte Fälle (Gedächtnis, Langkontext). Beide Ausgaben tokenidentisch zur gültigen R291-Kaltreferenz;2/2Semantik und1/2Format unverändert.73/2198Tokens wiederverwendet, Slotroundtrip-SHAs identisch, Peak7354,5MiB. Kein MTP/kein Champion.

**Remaining scope:** MTP rollback, checkpoint/fork invariance, long-session/32K and multi-slot integration remain scoped separately; cold/warm token identity on QA12 is not proof all states invariant.

**Reopening condition:** Diese neue funktionale Aufgabenbasis unterscheidet sich von den bereits gemessenen synthetischen 2K-Ausgaben; kein neuer Kernelpatch.

**Next action:** K05-Screens R291/R292 wiederverwenden; MTP-Rollback/32K/Mehrslot bleiben partiell. Jetzt übrige Originalachsen und Benchmark-Techniken anhand konkreter Varianten und Rohmetriken einzeln neu bewerten; keine weiteren Modelle oder Kombinationen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R194](../experiments/R194.md), [R209](../experiments/R209.md), [R291](../experiments/R291.md), [R292](../experiments/R292.md)
