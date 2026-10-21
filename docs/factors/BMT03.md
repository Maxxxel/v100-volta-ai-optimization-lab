# BMT03 — Adaptive MTP draft length

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| TESTED_NEGATIVE | True | True | P1 |


## Theory and Volta implications

This research subcase investigates adaptive mtp draft length. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Draft length trades proposed work against verification cost. The longest accepted span need not minimize total task time.; MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2211.17192
- https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-0ff1930c5d4878017f54.md)
- [Original audit hash and public excerpt](../audits/audit-642fa8e7d42cda1f1762.md)
- [Original audit hash and public excerpt](../audits/audit-f6ede40a69a9cd5a74b3.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R236 exercised real feedback1..3 across48 transitions on18 frozen workflows;13/18 preserved but only0.4685%tasks/s versusfixed3, below3%gate. No rule fitting on these tasks; other controllers untested.

**Remaining scope:** Gültigen Negativscreen übernehmen, keine weiteren A/B-Starts oder Regelanpassungen auf denselben18Aufgaben. Andere adaptive Verfahren bleiben ungetestet, nicht pauschal widerlegt.

**Reopening condition:** Ein sachlich anderer Controller samt unabhängiger Kalibration; R236Feedback1–3 und MAX5-Negative nicht auf denselben18Fällen optimieren.

**Next action:** Ein sachlich anderer Controller samt unabhängiger Kalibration; R236Feedback1–3 und MAX5-Negative nicht auf denselben18Fällen optimieren.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R204](../experiments/R204.md), [R208](../experiments/R208.md), [R209](../experiments/R209.md)
