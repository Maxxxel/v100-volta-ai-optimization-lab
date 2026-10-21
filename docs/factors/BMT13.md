# BMT13 — DFlash/DSpark drafting

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates dflash/dspark drafting. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Prompt/ngram lookup proposes tokens from context. Acceptance and task success depend on the verifier and actual workload repetition.; MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2602.06036
- https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

No admitted trained DFlash/DSpark/Medusa/EAGLE head matching this Omni target+tokenizer with a validated localSM70 verifier. Differenttarget/5090/Apple reports are not transferable speed evidence; largeport deferred.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Matching trainierter Draft/Head und SM70-Verifikationspfad; kein großer EAGLE/Medusa/DFlash-Port ohne beides.

**Next action:** Matching trainierter Draft/Head und SM70-Verifikationspfad; kein großer EAGLE/Medusa/DFlash-Port ohne beides.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md)
