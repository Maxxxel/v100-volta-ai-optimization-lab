# BMT12 — MoE residency and expert prefetch

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| NOT_APPLICABLE | False | False | P3 |


## Theory and Volta implications

This research subcase investigates moe residency and expert prefetch. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Scheduling controls batching and conversation lifecycles. Reusing or erasing another slot state is not a safe parallelism fix.; Prefetching can hide memory latency only if the executed KV access pattern and hardware instructions support it. Volta has no cp.async/TMA.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2312.17238
- https://huggingface.co/LiquidAI/LFM2.5-24B-A2B

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

Omni9B is dense, not MoE. Expert residency/prefetch needs a compatible MoE target/modelcomparison and actual RAM/PCIe capacity; cannot retrofit experts into these weights.

**Remaining scope:** Keine Omni-Ausführung für diese Architektur; passende Modellkandidaten gesondert bewerten.

**Reopening condition:** Aktuelles Omni ist dicht; Experten-Residency benötigt ein tatsächlich anderes MoE-Modell und ist kein nachrüstbarer Omni-Flagtest.

**Next action:** Aktuelles Omni ist dicht; Experten-Residency benötigt ein tatsächlich anderes MoE-Modell und ist kein nachrüstbarer Omni-Flagtest.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md)
