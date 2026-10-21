# BMT29 — Adaptive reasoning budgets

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P1 |


## Theory and Volta implications

This research subcase investigates adaptive reasoning budgets. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Reasoning-token budgets can improve complex tasks but raise latency, energy and truncation risk. Budgets need independent task-level evidence.; Planning/reflection loops trade extra generation for recovery. Evaluate additional successful tasks per second and joule, including failures.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/ibm-granite/granite-4.2-8b
- https://huggingface.co/ibm-granite/granite-4.2-8b/blob/f8de16cdcdbc6c779ca517604e050d82cc119e44/README.md
- https://huggingface.co/meta-models/Muse-Glimmer-30B
- https://huggingface.co/meta-models/Muse-Glimmer-30B/blob/a4e59da52a7bc87ae7251dd5545c0dd437c44b68/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-1907ff8806b26b2738e7.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Sourcecards substantiate thinkingmodes, not causal superiority of our proposed confidence/cost router. Need verified effectiveOmni budgetpath, independent calibration and safe taskpolicy; no newflag-only adaptivegain admitted.

**Remaining scope:** Confidence-/Kosten-Router benötigt unabhängige Kalibration und eigenen eingefrorenen Policyvertrag.

**Reopening condition:** Effektiver Budgetpfad plus unabhängiger Confidence-/Kostenrouter mit eingefrorenem Policyvertrag; R257Fixed256-Codingpilot ist kein adaptiver Router.

**Next action:** Effektiver Budgetpfad plus unabhängiger Confidence-/Kostenrouter mit eingefrorenem Policyvertrag; R257Fixed256-Codingpilot ist kein adaptiver Router.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R257](../experiments/R257.md)
