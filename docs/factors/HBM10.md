# HBM10 — KVQuant calibrated KV quantization

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| OPEN | False | False | P2 |


## Theory and Volta implications

KVQuant calibrates attention-cache compression with specific outlier/layout handling. Native cache dtype flags are not equivalent.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2e96ee859dddd9c15699.md)
- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| f16_reference | BLOCKED | PARTIAL | False |
| kvquant_port | BLOCKED | DEFERRED | False |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "kvquant_port"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "kvquant_port"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "kvquant_port"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

EXTERN_BELEGT/source+CPUequation review: KVQuant commit 57a238357f0ffe50084670fcd5781c9848f80ea2. Published Fisher route uses squared K/V activation gradients and backward, unlike R187inputsecondmoments; currentnativeGDNbackward missing. Crucially, code also contains fisher=None unweightedNUQ KMeans, so no blanketgradient/training exclusion. Directfull-headRoPE sparsekernel conflicts with actualOmniD256/n_rot64: nonrotatedchannel128,position1,unitbasis targetdot1 versuscos(1)=0.540302. This is a source-equation counterexample, not a GPU/modelquality result. Source has nativeKcur_normed(preRoPE)/Vcur callbacks and cb_eval/tensorget pattern; forward-only calibration is a distinct stillOPEN route.

**Remaining scope:** Directweighted/full-head deployment is not a compatible readyOmniport. UpstreamunweightedNUQ and nativeforwardobserver remain concretely implementable candidates; no modelKVquantization has run.

**Reopening condition:** A concrete numerically validated port and relevant capacity workload before GPU admission.

**Next action:** HBM10 next: bounded privateCPU helper for nativeforward Kcur_normed/Vcur capture, reusing pinnedR187Pythonstdlib calibrationcorpus, never originalQA/HumanEval/BFCL/agentdata. Freeze atmostone model,4x512tokens,256MiBrawcap and exactcontrol-logit/shape/stride checks before GPUadmission. No CUDArebuild, backward, quantizerfit, targetweightchange, fullcacheport, combinations or newmodels at this step. Keep directfull-headRoPE/Fisher routes separatelydeferred and unweightedNUQ OPEN.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R395](../experiments/R395.md)
