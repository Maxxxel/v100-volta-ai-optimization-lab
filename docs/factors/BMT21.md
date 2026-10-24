# BMT21 — Task/scaffold/rollout co-evolution

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates task/scaffold/rollout co-evolution. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Planning/reflection loops trade extra generation for recovery. Evaluate additional successful tasks per second and joule, including failures.; Domain fine-tuning changes weights and task distribution. Split training, development and independent evaluation data.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/ornith-ai/Ornith-1.5-9B
- https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-bc43e8b613cc983bfb4a.md)

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

Jointtask/scaffold evolution changes trainingdata/policy. Must have reproducible verifier and clean data splits; publisherrecipe is not a measured Omniinference gain. No uncontrolled rollout-trainingbranch.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Reproduzierbarer Trainings-/Scaffold-Verifier, saubere Datenpartitionen und zugelassener Trainer; MiMo-Inferenz misst nicht die kausale Wirksamkeit des Trainingsrezepts.

**Next action:** Separate static scaffold hypothesis from a bounded admitted training recipe; no evaluation-task recycling.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_TRAINING_EFFECT_DEFERRED |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Offline scaffold proposals are possible; joint policy/task evolution requires disjoint data, a verifier and actual training. Foreign model scores do not prove the training cause. |
| new GPU execution | False |
| next action | Separate static scaffold hypothesis from a bounded admitted training recipe; no evaluation-task recycling. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R390](../experiments/R390.md)
