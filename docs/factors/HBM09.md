# HBM09 — KIVI asymmetric KV quantization

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

KIVI uses asymmetric key/value quantization. A generic symmetric Q4 cache is not a KIVI implementation.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevant OmniD256/GQA4 quantizedKV CUDA numerical component only; no loaded Omni model or fullcacheintegration.

- [Original audit hash and public excerpt](../audits/audit-562eaeb901f0c1b39e99.md)
- [Original audit hash and public excerpt](../audits/audit-67337bdf704104b2d015.md)
- [Original audit hash and public excerpt](../audits/audit-a3984fe0de4957ec6661.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| f16_reference | BLOCKED | PARTIAL | False |
| kivi_2bit | BLOCKED | DEFERRED | False |


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
        "value": "kivi_2bit"
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
        "value": "kivi_2bit"
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
        "value": "kivi_2bit"
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

R395 KIVI actualupstream2bitCUDA component: unchanged kernel/helper from commit 876b4d2d08e3b1d5f70d0969c299d8c7c42ddfb6 compiled/nativebinarySM70 and executed onV100; four QKperchannelK/AVpertokenV cases atD256/GQA4,M1,contexts512/8192,group64. All147456outputelements independently checked against savedFP64reconstruction;4/4pass, NMSE4.15e-8–4.37e-8 below1e-6. Oneoperatorprocess,zero models. Peak550.5MiB. SyntheticcachequantizationNMSE~0.101 againstoriginalF16 is separate substantialquantizationloss, not measuredmodelquality. Packed/scalebytes exclude residualwindow and state. No throughput, wholemodelVRAMsaving, agentquality, MTPverification, energyper-success or Champion claim.

**Remaining scope:** FullGGUF cachelayout/quantizer/scale+residual memory/lifetime, serial andM>1/MTP correctness, original12/tool/agentquality and E2E/VRAM/energy remain untested.

**Reopening condition:** Justify measured KV pressure, then independent numerics and quality before a kernel port.

**Next action:** Continue remaining originalsingles with HBM10/KVQuant exact calibration/codebook/SM70 operator admission. Retain R395as componentonly proof: KIVI is not inherently excluded by Volta. FullKIVI port needs an admitted quantizer/cachelayout/residuallifetime and correct hybridGDN/reset/rollback plusM>1/MTP handling; only then modelquality and E2E/memory tests. No extra synthetickernel timing grid, combinations or newmodels yet.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R249](../experiments/R249.md), [R382](../experiments/R382.md), [R395](../experiments/R395.md)
