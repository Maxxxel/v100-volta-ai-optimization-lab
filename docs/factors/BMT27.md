# BMT27 — Confidence calibration and selective tool use

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| OPEN | False | False | P1 |


## Theory and Volta implications

This research subcase investigates confidence calibration and selective tool use. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: An independent tool gate checks authorization and arguments outside generation. A safe simulator result does not authorize production actions.; Output grammars constrain valid syntax. Syntax validity does not guarantee correct tool selection or safe actions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/datasets/LocalLLaMA/typed-decisions
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-bc43e8b613cc983bfb4a.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Head-free post-hoc calibration is a distinct unresolved transfer, not excluded by the unavailable checkpoint-specific decision head. Native probability extraction is source-visible; calibrated quality, safety and acquisition cost remain unmeasured.

**Remaining scope:** OPEN head-free acquisition/calibration/abstention; DEFERRED checkpoint-specific trained noncausal head. No new experimental coverage.

**Reopening condition:** Independent acquisition controls, disjoint calibration/evaluation partitions, prespecified coverage/false-accept and full-cost criteria.

**Next action:** Pin an unmodified native probability observable, verify acquisition cost/output invariance on independent inputs, then separate calibration/test data and false-accept versus coverage limits. No confidence claim from raw token probability.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | OPEN |
| decision | REOPEN_HEAD_FREE_CALIBRATION_ONLY |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | The trained noncausal decision head is checkpoint-specific. A head-free post-hoc calibration/abstention wrapper is separately possible on frozen Omni; existing native pre-sampling probability extraction is source-visible. |
| new GPU execution | False |
| next action | Pin an unmodified native probability observable, verify acquisition cost/output invariance on independent inputs, then separate calibration/test data and false-accept versus coverage limits. No confidence claim from raw token probability. |
| previous status | DEFERRED |
| priority | P1 |


## Related sprint records

[R390](../experiments/R390.md)
