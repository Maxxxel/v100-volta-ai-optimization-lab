# BMT20 — LoopSplit, hyperconnections and depth attention

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates loopsplit, hyperconnections and depth attention. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: GDN state-write fusion can remove copies when state type and layout match. F32-only cache fusion cannot silently be combined with F16 state storage.; Multi-turn, rejection and restore operations must preserve GDN and attention state consistently. Primitive rollback tests do not qualify the full server scheduler.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/b82e54bd609793562a75cbf9337970a93369eab5/README.md
- https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/configuration_nanbeige.py
- https://huggingface.co/Nanbeige/Nanbeige4.2-3B/blob/main/modeling_nanbeige.py
- https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/configuration_nanbeige.py
- https://huggingface.co/Nanbeige/Nanbeige4.2-3B/raw/b82e54bd609793562a75cbf9337970a93369eab5/modeling_nanbeige.py

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

LoopSplit/mHC/depth-attention sourceflags are not proof currentweights trainedfor them. Need matching checkpoint/layout and enginepath; no Omni flag-only treatment.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Passend trainierte mHC/Depth-Attention/LoopSplit-Gewichte und Enginepfad; Quellflags allein sind keine Interventionszulassung.

**Next action:** Per-technique primary implementation/checkpoint and supported graph; no compound source label as implementation evidence.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_DISTINCT_ARCHITECTURE_PREREQUISITES |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | LoopSplit, mHC and depth attention are separate model mechanisms; the shared source card alone does not establish all three in a runnable Omni graph. |
| new GPU execution | False |
| next action | Per-technique primary implementation/checkpoint and supported graph; no compound source label as implementation evidence. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R390](../experiments/R390.md)
