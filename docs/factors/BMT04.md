# BMT04 — Independent Q4/Q5/Q6 draft precision

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| TESTED_NEGATIVE | True | True | P0 |


## Theory and Volta implications

This research subcase investigates independent q4/q5/q6 draft precision. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.; A separate draft model can reduce target steps at the cost of extra memory, startup and verification. Tokenizer and target compatibility are necessary.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2211.17192

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-4074703750eba42f8b7f.md)
- [Original audit hash and public excerpt](../audits/audit-4ed8d00dfd5d86541176.md)
- [Original audit hash and public excerpt](../audits/audit-f342d89e541599ff11aa.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

PublishedQ4/Q5/Q6 heads source/hash/tokenizer admitted with originalQ6target fixed; R197/R199/R210 native plusR211/R212actualagent tests resolve practical shortlist. None met preregistered practical qualification gates. Other bitallocations remain unmeasured, not universally disproven.

**Remaining scope:** Getestete negative Behandlung nicht wiederholen; keine pauschale Ablehnung aller Varianten.

**Reopening condition:** Anderer tatsächlich verfügbarer kompatibler Kopf oder neue Kosten-/Akzeptanzhypothese; vorhandene Q4/Q5/Q6-Piloten gültig negativ, keine Wiederholung.

**Next action:** Anderer tatsächlich verfügbarer kompatibler Kopf oder neue Kosten-/Akzeptanzhypothese; vorhandene Q4/Q5/Q6-Piloten gültig negativ, keine Wiederholung.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R210](../experiments/R210.md), [R211](../experiments/R211.md), [R212](../experiments/R212.md)
