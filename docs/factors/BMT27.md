# BMT27 — Confidence calibration and selective tool use

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P1 |


## Theory and Volta implications

This research subcase investigates confidence calibration and selective tool use. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: An independent tool gate checks authorization and arguments outside generation. A safe simulator result does not authorize production actions.; Output grammars constrain valid syntax. Syntax validity does not guarantee correct tool selection or safe actions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/6
- https://huggingface.co/datasets/LocalLLaMA/typed-decisions
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b
- https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b/blob/14c9d90137962d300f3de95633f7b6535e80c5ce/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Actual Omni inference with pre-sampling probability extraction on three neutral acquisition inputs; no action confidence calibration or broad model quality.

- [Original audit hash and public excerpt](../audits/audit-18678122920b3bae4bfa.md)
- [Original audit hash and public excerpt](../audits/audit-b4763d4fa78c55d3de3e.md)
- [Original audit hash and public excerpt](../audits/audit-bc43e8b613cc983bfb4a.md)
- [Original audit hash and public excerpt](../audits/audit-ca7d5f9ffc11eb4fcafa.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

R391 BMT27 acquisition gate: one actual stock Omni Q6K/8K/F16/300W model start,14requests,6matchedpairs on3newneutralinputs. All6nativeoutputIDarrays identical;360selected-token logprob entries and top5lists independently verified against returnedtokenIDs and nativepre-sampling settings. Paired E2E overhead 11.14–12.82%, median 11.83%; summed paired boardenergy change +4.12%, descriptive only. Metadata acquisition works in this exact greedy profile, but incurs cost. Zero calibration fits, original12/task-success or tool-safety qualification. BMT27 PARTIAL; no Champion or confidence correctness claim.

**Remaining scope:** Independentaction-calibration andholdout data nowfrozen(self-authored80/120family-disjoint); byte-alignedscoreobservable/API, modelacquisition, thresholdfit andheldoutselective-risk/fullcostevidence remainunmeasured. R391neutralacquisition isnotactionconfidencequalification.

**Reopening condition:** Independent acquisition controls, disjoint calibration/evaluation partitions, prespecified coverage/false-accept and full-cost criteria.

**Next action:** BMT27 action-level abstention study: frozen200self-authoredpolicycases,80calibration/120family-disjointholdout; pin selected-labelbyte/logprob parser and CPUoracle/no-leakage checks, then controlled stockruntime admission. Onefrozen threshold only,>=95%correctallowretention, zero calibration unsafeallow; if no baselineunsafeallow or no feasiblethreshold, stopbeforeholdout. No originalbenchmark tuning, no calibratedprobability/deployment claim; single-factor gate remains active.

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

[R390](../experiments/R390.md), [R391](../experiments/R391.md)
