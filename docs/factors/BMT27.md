# BMT27 — Confidence calibration and selective tool use

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P1 |


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


### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Publishedpplx255x5120 noncausalconfidencehead is checkpoint-specific, not a generic scalar confidence output. No trained Omnihead/calibration; implementing threshold on uncalibrated scores is not reproduction.

**Remaining scope:** Nur mit unabhängigem Kalibrations-/Testsplit, festem Merkmal und False-accept/Coverage-Vertrag zulassen; vorhandene R192/R241-Antworten nicht auf eigene Freigaben hin nachoptimieren.

**Reopening condition:** Unabhängige Kalibrations-/Testpartition, festes Konfidenzmerkmal und Coverage/False-accept-Grenzen; veröffentlichten fremden Konfidenzkopf nicht in Omni hineininterpretieren.

**Next action:** Unabhängige Kalibrations-/Testpartition, festes Konfidenzmerkmal und Coverage/False-accept-Grenzen; veröffentlichten fremden Konfidenzkopf nicht in Omni hineininterpretieren.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
