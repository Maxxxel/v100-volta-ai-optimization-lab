# BMT15 — Sensitivity-guided rank/pruning

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates sensitivity-guided rank/pruning. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Low-rank factorization reduces matrix parameters only when a compatible inference path realizes the saving. Rank choice changes model quality.; Pruning requires compact or sparse execution to reduce real work. Zero weights in an unchanged dense kernel do not establish a speedup.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2306.00978
- https://arxiv.org/abs/2403.07378

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)
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

SVD/pruning changes weights and needs calibrated ranks, independent quality and compatible kernel/engine. Current originalGGUF is preserved, no compatible compressed checkpoint admitted. Cost outweighs unmeasured gain before finalist evaluation.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Konkrete Ränge/Pruningstruktur, veränderte Gewichte, kompatible CUDA-Operatoren und unabhängige Qualität; keine CPU-SVD als GPU-Gewinn.

**Next action:** Named tensor/rank policy, compatible factorized operators, numerical checks and independent tasks.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_EXECUTABLE_COMPRESSION_DEFERRED |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Sensitivity analysis may be offline, but actual rank/pruning benefit requires compressed weights and an execution graph that avoids reconstructing dense work. |
| new GPU execution | False |
| next action | Named tensor/rank policy, compatible factorized operators, numerical checks and independent tasks. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R249](../experiments/R249.md), [R390](../experiments/R390.md)
