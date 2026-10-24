# BMT11 — Deployment-compatible QAD/QAT checkpoints

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P2 |


## Theory and Volta implications

This research subcase investigates deployment-compatible qad/qat checkpoints. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: AWQ uses activation-aware weight scaling/quantization. It needs matching weights, architecture support and an actual SM70 inference path.; QAT changes training to account for quantization. A pretrained deployment-compatible checkpoint and its training provenance are required.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2601.20088
- https://arxiv.org/abs/2608.13966
- https://huggingface.co/LiquidAI/LFM2.5-24B-A2B
- https://huggingface.co/QUASAR-QAT/Qwen3.8-27B-QUASAR-NVFP4
- https://huggingface.co/QUASAR-QAT/Qwen3.8-27B-QUASAR-NVFP4/blob/4a22293aa6d1026844bc93a8727f1837e48acd89/README.md
- https://huggingface.co/google/gemma-4-12B-it

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

QAT/QAD is a trained checkpoint property. NativeNVFP4 instructions are not SM70; a supported dequant path may exist but requires a compatible specific artifact. No admitted OmniQATcheckpoint, no generic FP16flag substitute.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** Passender Omni-QAT/QAD-Checkpoint oder zugelassener realer Trainingsschritt; Fremdmodell-QAT ist keine Omni-Inferenzintervention.

**Next action:** Later model-phase artifact/license/hash/SM70-load admission for the linked GGUF; no download or generic NVFP4 exclusion now.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | SPLIT_OMNI_AND_OTHER_MODEL_QAT |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Omni-specific QAT is unadmitted, but the archived QUASAR card explicitly links a Qwen3.5-4B Q4_0 GGUF. Native NVFP4 absence does not exclude supported dequantized QAT deployment. |
| new GPU execution | False |
| next action | Later model-phase artifact/license/hash/SM70-load admission for the linked GGUF; no download or generic NVFP4 exclusion now. |
| previous status | DEFERRED |
| priority | P2 |


## Related sprint records

[R390](../experiments/R390.md)
