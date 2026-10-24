# BMT05 — MTP-head GGUF graft packaging

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| QUALIFIED | True | True | P1 |


## Theory and Volta implications

This research subcase investigates mtp-head gguf graft packaging. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.; A separate draft model can reduce target steps at the cost of extra memory, startup and verification. Tokenizer and target compatibility are necessary.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2211.17192
- https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-058f7fb472328b4ccdee.md)
- [Original audit hash and public excerpt](../audits/audit-1e481b9ad01b4b62af21.md)
- [Original audit hash and public excerpt](../audits/audit-21267142b49cd147290a.md)
- [Original audit hash and public excerpt](../audits/audit-4af664a242392bba07e2.md)
- [Original audit hash and public excerpt](../audits/audit-dffb404b82747d32d666.md)
- [Original audit hash and public excerpt](../audits/audit-fb076ec1a01a891d9edb.md)

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

R200/R201/R203/R205/R206/R207: ~1GiB saved,132/164+16coding,88/100tools,13/18agents without prior success loss; independent memory confirmation. No extra practical speed or Cpromotion.

**Remaining scope:** Qualifizierten Umfang wiederverwenden; neue Kombination nur mit eigener Messung.

**Reopening condition:** Qualifizierter Graft-Speicherumfang bleibt gültig; neue Interaktionen erst in der späteren Kombinationsphase, eigener Kopf erst nach Trainingszulassung.

**Next action:** Qualifizierter Graft-Speicherumfang bleibt gültig; neue Interaktionen erst in der späteren Kombinationsphase, eigener Kopf erst nach Trainingszulassung.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R200](../experiments/R200.md), [R201](../experiments/R201.md), [R203](../experiments/R203.md), [R205](../experiments/R205.md), [R206](../experiments/R206.md), [R207](../experiments/R207.md)
