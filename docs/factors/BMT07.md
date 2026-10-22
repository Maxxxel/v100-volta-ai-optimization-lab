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

- [Original audit hash and public excerpt](../audits/audit-3065546a54fc26cd63ec.md)
- [Original audit hash and public excerpt](../audits/audit-5350f59ad47a9a208e94.md)
- [Original audit hash and public excerpt](../audits/audit-c6037cf66712e2203c95.md)
- [Original audit hash and public excerpt](../audits/audit-d8153ea70260b2285397.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R404 BMT07 GPU screen: candidate B correctly abstained on all 4 negative/ambiguous cases while A0 made 4 unsupported calls; all 8 positive calculations failed in both arms. Aggregate request latency was 69.98% lower, but this is a single synthetic screen and not a qualified agent/retrieval winner.

**Remaining scope:** Fresh balanced independent confirmation; report positive calculation quality separately from safe negative abstention. Vector retrieval and generated summaries remain separate untested scopes.

**Reopening condition:** Fresh independent balanced confirmation with new task IDs; no rerun or tuning of R404 tasks.

**Next action:** Run fresh balanced A/B on new task IDs. Keep model, engine, policy contract, tool schema and sampler fixed; vary only full-history versus provenance-selected source context. Qualification requires positive-case task quality and no candidate false calls on negatives; do not promote from R404 screen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R188](../experiments/R188.md), [R404](../experiments/R404.md), [R405](../experiments/R405.md)
