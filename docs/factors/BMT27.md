# BMT27 — Confidence calibration and selective tool use

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


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
- [Original audit hash and public excerpt](../audits/audit-7051e3c06b9fd4ba2852.md)
- [Original audit hash and public excerpt](../audits/audit-77e97e00457c2d4494e8.md)
- [Original audit hash and public excerpt](../audits/audit-b4763d4fa78c55d3de3e.md)
- [Original audit hash and public excerpt](../audits/audit-bc43e8b613cc983bfb4a.md)
- [Original audit hash and public excerpt](../audits/audit-ca7d5f9ffc11eb4fcafa.md)
- [Original audit hash and public excerpt](../audits/audit-e547bc3b623ccc45230b.md)
- [Original audit hash and public excerpt](../audits/audit-ffbe3c06cb66ec62a08f.md)

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

R392 BMT27: one stock Omni Q6K/8K/F16/300W model start,80new self-authored calibration cases,65/80correct labels and15unsafeallows. Independent raw-byte/logprob/oracle replay confirms the chosen likelihood feature cannot eliminate all15unsafeallows while retaining95%ofcorrectallows. At zero observed unsafeallows, at most19/28correctallows could remain (67.86%). Preregistered early stop used: zero accepted thresholds, zero holdoutpairs;120holdoutcases untouched. Concrete mean-selected-decision-token-logprob cutoff rejected in this calibration scope. No source-head, broadagentsecurity, independentholdout, original12 or globalOmniqualityclaim; no knownfailureprompt/thresholdrepair.

**Remaining scope:** R391acquisition works but R392mean-selected-label-logprob threshold failed80casecalibration;120holdoutnotrun. Otherconfidencefeatures or trainedheads require a distinct independentlymotivated implementation/data contract, not retuningthese15failures.

**Reopening condition:** Independent acquisition controls, disjoint calibration/evaluation partitions, prespecified coverage/false-accept and full-cost criteria.

**Next action:** Keep this cutoff negative; do not weaken95%retention or force heldoutgeneration. No newthreshold/promptfeaturesearch on these calibrationfailures. Different confidence methods remain separate hypotheses.

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

[R390](../experiments/R390.md), [R391](../experiments/R391.md), [R392](../experiments/R392.md)
