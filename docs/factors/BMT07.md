# BMT07 — Source-grounded retrieval

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P0 |


## Theory and Volta implications

This research subcase investigates source-grounded retrieval. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Retrieval selects relevant history with provenance. It can save prefill while omitting facts required by later tool decisions.; Context compression is a semantic policy, not just shorter text. Independent held-out task sequences must preserve facts and authorization.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2309.06180
- https://huggingface.co/datasets/hkust-nlp/Toolathlon

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-d8153ea70260b2285397.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R151source-selection12/12vs8/12 scoped; R188newdata5/12vs3/12 fails absolutequality gate. Source selection alone does not fix arithmetic/policy errors. New independent policy/fixtures required; no tuning known evaluation answers or repeating negative retrieval treatments.

**Remaining scope:** R151/R188 gemessen; neue Retrieval-Politik bis zu unabhängig eingefrorenem Selektions-/Rechen-/Policy-Vertrag zurückgestellt. Keine bekannten Fehlantworten nachoptimieren.

**Reopening condition:** Unabhängige Selektions-/Provenienz-/Rechenregel vor einer neuen Retrieval-Policy; keine Reparatur bekannter R151/R188-Antworten.

**Next action:** Unabhängige Selektions-/Provenienz-/Rechenregel vor einer neuen Retrieval-Policy; keine Reparatur bekannter R151/R188-Antworten.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R188](../experiments/R188.md)
