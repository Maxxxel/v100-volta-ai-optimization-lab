# BMT10 — DP4A/ternary inference kernels

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| DEFERRED | True | False | P1 |


## Theory and Volta implications

This research subcase investigates dp4a/ternary inference kernels. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Weight quantization trades storage and dequantization costs against output quality. Compare tasks and wall time across tokenizers, not tokens/s alone.; A quantization format is useful only if supported by the loaded engine kernels. A readable file is not proof of accelerated device execution.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/PrismML-Eng/Bonsai-demo/blob/db871ea96bffff5ce5609873c412b75d7cd5ba3c/community-benchmarks/bonsai2/cuda-tesla-v100-windows.md
- https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Bonsai PQ2 CUDA-/CPU-Komponente lokal gemessen; PTQ1-Gegenvergleich und Omni-Transfer nicht gemessen.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Ternary Bonsai PTQ1/PQ2 packing and DP4A kernels require matching trained/quantized weights. Not an OmniQ6 runtime flag. Assess as separate model candidate; no currentOmniGPUtrial.

**Remaining scope:** Voraussetzung vor Ausführung belegen; kein GPU-Gewinn behauptet.

**Reopening condition:** PQ2-Pfad auf Bonsai lokal gemessen, PTQ1-Gegenvergleich und Omni-Ternärgewichte fehlen. Kompatibles Omni-Artefakt oder spätere Bonsai-Quantisierungsphase nötig.

**Next action:** PQ2-Pfad auf Bonsai lokal gemessen, PTQ1-Gegenvergleich und Omni-Ternärgewichte fehlen. Kompatibles Omni-Artefakt oder spätere Bonsai-Quantisierungsphase nötig.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md)
