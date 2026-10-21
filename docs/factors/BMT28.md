# BMT28 — Stochastic recurrent-state rounding

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P2 |


## Theory and Volta implications

This research subcase investigates stochastic recurrent-state rounding. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Multi-turn, rejection and restore operations must preserve GDN and attention state consistently. Primitive rollback tests do not qualify the full server scheduler.; Attention KV and recurrent-state precision are different choices. State-storage compression must preserve repeated updates and rejection/restore behavior.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/blob/a9904d24bcc1d289a1950fa9d2b978c47cf903b9/README.md

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

PublishedstochasticMamba-rounding H100/vLLM is not a GDNstorage/kernel implementation. CurrentrecurrentF32 hardcoded; needs newCPUoracle+realactivationdrift/rollbackproof thenSM70port. Not attentionKVquantization.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Tatsächlich anderer GDN-State-Speicherpfad, stochastische Rundungsregel und CPU-/GPU-Orakel inklusive Rollback; Mamba/H100-Quelle ist kein SM70-GDN-Port.

**Next action:** Tatsächlich anderer GDN-State-Speicherpfad, stochastische Rundungsregel und CPU-/GPU-Orakel inklusive Rollback; Mamba/H100-Quelle ist kein SM70-GDN-Port.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.
