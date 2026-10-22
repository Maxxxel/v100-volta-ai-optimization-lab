# BMT26 — Streaming cache-aware RNNT ASR

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | False | False | P3 |


## Theory and Volta implications

This research subcase investigates streaming cache-aware rnnt asr. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: vLLM support on SM70 depends on source builds, PyTorch device support, model loaders and compatible kernels. Import success is insufficient.; Grammar parsing can change allowed token sequences and host overhead. Separate protocol correctness from GPU throughput.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize
- https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize/blob/704aa4a9c304e8520be88901e0d1960158ef5b15/README.md
- https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b
- https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b/blob/ea30d66debe3740a08b573244286791d423d6b3e/README.md

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

StreamingRNNT is audioarchitecture/serving for ASR, not an Omnidecoderoptimization. Evaluate later as assistantcomponent; not an untested OmniGPUfactor.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** ASR/RNNT-Komponente und Audiotests in späterer Assistentenphase; keine Änderung des Omni-Textdecoders durch ASR-Servingparameter.

**Next action:** Later ASR engine/SM70 model/license and audio latency/quality test; no new Omni text benchmark.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Deferral scope reassessment — 2026-10-22

This is a source/evidence review, not a new GPU experiment.

| Field | Assessment |
|---|---|
| current status | DEFERRED |
| decision | KEEP_AUDIO_COMPONENT_DEFERRED |
| expected benefit | Unverified; no numerical performance forecast. |
| model engine compatibility | Streaming RNNT and transcript-state handling are ASR component methods, not modifications to text decoder KV/GDN state. |
| new GPU execution | False |
| next action | Later ASR engine/SM70 model/license and audio latency/quality test; no new Omni text benchmark. |
| previous status | DEFERRED |
| priority | P3 |


## Related sprint records

[R390](../experiments/R390.md)
