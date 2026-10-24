# BMT24 — Geometry-grounded OCR

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates geometry-grounded ocr. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Context compression is a semantic policy, not just shorter text. Independent held-out task sequences must preserve facts and authorization.; Output grammars constrain valid syntax. Syntax validity does not guarantee correct tool selection or safe actions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6-GGUF
- https://huggingface.co/lightonai/LightOnOCR-3-0.8B
- https://huggingface.co/lightonai/LightOnOCR-3-0.8B/blob/36d8636925327c671bd8e479c517a004f7566bd9/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

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

GeometricOCR typedblocks/bboxes require matching visionmodel/component and documentdataset. Not a technique present in/retrofit to current textonlyOmniGGUF.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Passende Vision-/OCR-Komponente und Dokumentaufgaben; kein Bounding-Box-Ausgabemodus in textonlyOmni ohne Visiongewichte.

**Next action:** Licensed small OCR model and independent document set with complete component cost; no artificial Omni vision claim.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_COMPONENT_PHASE_DEFERRED |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Geometric OCR needs a vision/OCR component and document evaluation, not just JSON bounding boxes from the current text-only target. |
| new GPU execution | False |
| next action | Licensed small OCR model and independent document set with complete component cost; no artificial Omni vision claim. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R390](../experiments/R390.md)
