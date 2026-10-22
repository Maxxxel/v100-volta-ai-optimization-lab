# BMT16 — Cold-load and specialist routing

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P1 |


## Theory and Volta implications

This research subcase investigates cold-load and specialist routing. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: A lab Ollama frontend adds model routing and protocol translation. Actual native tool messages and one owned GPU worker must be verified.; Scheduling controls batching and conversation lifecycles. Reusing or erasing another slot state is not a safe parallelism fix.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://github.com/NVlabs/ToolOrchestra
- https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- https://huggingface.co/google/gemma-4-12B-it
- https://huggingface.co/nvidia/Nemotron-Orchestrator-8B
- https://huggingface.co/nvidia/Nemotron-Orchestrator-8B/blob/26df4b9aad5abdc5b7871ee4c71063ce888feb26/README.md
- https://huggingface.co/ornith-ai/Ornith-1.5-9B

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

Cold loads/switches/multi-model routing require admitted multiplemodels and a distinct load/cache workload. Not single-factor Omni warm-runtime benefit; preserve H08 and R11 outstanding workload scopes.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Bewusst spätere Routingphase mit mehreren qualifizierten Modellen; echte Lade-/Wechselkosten samt Cachebedingungen, nicht erneuter Omni-Warmtest.

**Next action:** After the single-factor gate, use preserved artifacts with frozen task-only routing and include all cold loads, switch costs and energy; no test-label oracle.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | LATER_ROUTING_PHASE_NOT_OMNI_SINGLE_GAP |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Existing Omni and Bonsai scoped results provide routing leads; not all routing prerequisites require new models. Switching cost and selection quality remain unmeasured. |
| new GPU execution | False |
| next action | After the single-factor gate, use preserved artifacts with frozen task-only routing and include all cold loads, switch costs and energy; no test-label oracle. |
| previous status | DEFERRED |
| priority | P1 |


## Related sprint records

[R390](../experiments/R390.md)
