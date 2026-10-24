# BMT32 — GQA/MQA/MLA and sparse/local attention

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P2 |


## Theory and Volta implications

This research subcase investigates gqa/mqa/mla and sparse/local attention. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Flash attention fuses attention operations to reduce intermediate memory traffic. Actual support depends on head dimensions, KV formats and compiled SM70 kernels.; Quantizing attention keys reduces KV storage but adds conversion and changes attention scores. It does not quantize the separate GDN recurrent state.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/f0e1c1e04d40177e4673a22097036854f536e9c0/README.md
- https://huggingface.co/XiaomiMiMo/MiMo-V2.5/blob/63651580ca774f8504f676040460aed3e1244ac1/README.md
- https://huggingface.co/moonshotai/Kimi-K2.6/blob/7eb5002f6aadc958aed6a9177b7ed26bb94011bb/README.md
- https://huggingface.co/stepfun-ai/Step-3.5-Flash/blob/ab446a3de5e171ea341227e24bb1f090e1b771f7/README.md

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

MLA/MQA/SWA/MSA/gelernte Sinks nur als kompatible Modellarchitektur vergleichen. Kein laufzeitneutraler Umbau bestehender Omni-Gewichte zugelassen; aktuelle GQA-/GDN-Struktur bewahren. Kernel-/Cachepfade getrennt behandeln.

**Remaining scope:** MLA/MQA/SWA/MSA/gelernte Sinks nur als kompatible Modellarchitektur vergleichen. Kein laufzeitneutraler Umbau bestehender Omni-Gewichte zugelassen; aktuelle GQA-/GDN-Struktur bewahren. Kernel-/Cachepfade getrennt behandeln.

**Reopening condition:** GQA/GDN sind bereits Teil der Omni-Architektur. MQA/MLA/gelernte lokale Muster benötigen passende Gewichte; laufzeitseitige Sink-/Sparse-KV-Policies separat mit state-sicherem Cachepfad und unabhängiger Qualität prüfen.

**Next action:** For a runtime policy require actual KV-pressure benefit and state-safe eviction including recurrent layers; freeze independent retention/quality tasks before any port or GPU test.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | SPLIT_LEARNED_ARCHITECTURE_AND_RUNTIME_CACHE |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | GQA/GDN already exist in Omni. Learned MLA/MQA/SWA/sink architectures need matching weights; a runtime sink/window/sparse-cache policy is a separate implementable but approximate treatment. |
| new GPU execution | False |
| next action | For a runtime policy require actual KV-pressure benefit and state-safe eviction including recurrent layers; freeze independent retention/quality tasks before any port or GPU test. |
| previous status | DEFERRED |
| priority | P2 |


## Related sprint records

[R390](../experiments/R390.md)
