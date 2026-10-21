# BMT22 — Trajectory-level DPPO

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates trajectory-level dppo. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Domain fine-tuning changes weights and task distribution. Split training, development and independent evaluation data.; Code execution and evaluation must use isolated tests and correct joint pass rules. Training loss or a syntax check is not coding success.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://github.com/hamishivi/tmax
- https://huggingface.co/allenai/tmax-9b
- https://huggingface.co/allenai/tmax-9b/blob/81ec54b29986d78191596d81900c0f8de2fa1b35/README.md

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

DPPOfullterminaltrajectory training needs objective/logprobs/rewards and admitted trainer. No equivalent inference switch; large training development outside coarse inference shortlist.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Differenzierbare Trajektorien-/Logprob-/Reward-Pipeline und echtes Training; bisherige MiMo-Agentenmessungen schließen Omni-DPPO nicht experimentell ab.

**Next action:** Differenzierbare Trajektorien-/Logprob-/Reward-Pipeline und echtes Training; bisherige MiMo-Agentenmessungen schließen Omni-DPPO nicht experimentell ab.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
