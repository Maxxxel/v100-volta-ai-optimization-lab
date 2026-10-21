# HBM08 — F16/Q8/Q4 attention KV cache

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P1 |


## Theory and Volta implications

Paired key/value formats create a joint attention kernel configuration. Individual key and value successes cannot be added to predict the pair.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-052735eb2d4adf83b1bd.md)
- [Original audit hash and public excerpt](../audits/audit-0b65111832a0e7ae153b.md)
- [Original audit hash and public excerpt](../audits/audit-15357beaac0b3905a2ce.md)
- [Original audit hash and public excerpt](../audits/audit-1962b7915d289ed667aa.md)
- [Original audit hash and public excerpt](../audits/audit-22d1d0a5e108bf464b15.md)
- [Original audit hash and public excerpt](../audits/audit-27819b91177b325e92d4.md)
- [Original audit hash and public excerpt](../audits/audit-386203c8d6cf777f3bb9.md)
- [Original audit hash and public excerpt](../audits/audit-62cb102a05278610565d.md)
- [Original audit hash and public excerpt](../audits/audit-652eef515a970abc8d51.md)
- [Original audit hash and public excerpt](../audits/audit-76bd28c3368e61d7c96d.md)
- [Original audit hash and public excerpt](../audits/audit-8caaa3cdf4c079c396fe.md)
- [Original audit hash and public excerpt](../audits/audit-8d0de00b1f8ea1c46cfb.md)
- [Original audit hash and public excerpt](../audits/audit-a2270317169dec422f24.md)
- [Original audit hash and public excerpt](../audits/audit-b4f0a807daebe43f2edf.md)
- [Original audit hash and public excerpt](../audits/audit-b939abaa6c68ac7fbb46.md)
- [Original audit hash and public excerpt](../audits/audit-d870ddde2a67de12a375.md)
- [Original audit hash and public excerpt](../audits/audit-f818d211483856d94cf3.md)
- [Original audit hash and public excerpt](../audits/audit-fae4b1903a527efdd0b8.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| f16_f16 | READY_LINKED | PARTIAL | False |
| q8_0_q8_0 | READY_LINKED | PARTIAL | True |
| q8_0_q4_0 | BLOCKED | PARTIAL | True |
| q4_0_q4_0 | BLOCKED | PARTIAL | True |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "f16_f16"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q8_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q8_0_q4_0"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "q4_0_q4_0"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant f16_f16

```json
[
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2594.443645763525,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.527936783,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2636.5099957165603,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.298508223,
        "peak_device_VRAM_mib": 7236.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.2696582541158916,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.561886463570783,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.236229004342205,
        "ttft_change_pct": 1.9281707637068601
      },
      "prefill": {
        "e2e_change_pct": 0.9080993850692831,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 2.6728422580919675,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.892371327204633,
        "ttft_change_pct": 0.8917386420676854
      },
      "prefill2048": {
        "e2e_change_pct": 0.4850796747903674,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6893905760388508,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.48780522627988043,
        "ttft_change_pct": 0.4846824275347661
      },
      "prefill4096": {
        "e2e_change_pct": 0.6079092720157941,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.06021958505744163,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.6058586524545162,
        "ttft_change_pct": 0.6090167311306294
      }
    }
  },
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2649.030992900021,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.66920848,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2653.4173859192642,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.467789167000001,
        "peak_device_VRAM_mib": 7204.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.5494949634889963,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6417283476910063,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -2.588320013493828,
        "ttft_change_pct": 0.38102260564694124
      },
      "prefill": {
        "e2e_change_pct": 0.7915046955718763,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.0679885088901386,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.774315035299189,
        "ttft_change_pct": 0.7565757098443315
      },
      "prefill2048": {
        "e2e_change_pct": 0.5960680888369652,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.541830699207213,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6092807043037274,
        "ttft_change_pct": 0.5942051029937279
      },
      "prefill4096": {
        "e2e_change_pct": 0.621654662565585,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6803077893213771,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6147332351422952,
        "ttft_change_pct": 0.6171983613609378
      }
    }
  },
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2599.013028498364,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.108073662,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2618.5108389778597,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.308949404,
        "peak_device_VRAM_mib": 7172.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.2891309825985973,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.345185255607162,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -2.2433133784325543,
        "ttft_change_pct": 1.1522841816442586
      },
      "prefill": {
        "e2e_change_pct": 0.3587627216725231,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.05777899097902939,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.36781070513044467,
        "ttft_change_pct": 0.36467714824366393
      },
      "prefill2048": {
        "e2e_change_pct": 0.6920839287919645,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.4614949876799788,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6818458242014769,
        "ttft_change_pct": 0.6944330832729717
      },
      "prefill4096": {
        "e2e_change_pct": 0.99135476498593,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.124780461844832,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.9832269534550853,
        "ttft_change_pct": 0.988037332534919
      }
    }
  }
]
```

### Variant q8_0_q8_0

```json
[
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2594.443645763525,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.527936783,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2636.5099957165603,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.298508223,
        "peak_device_VRAM_mib": 7236.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.2696582541158916,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.561886463570783,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.236229004342205,
        "ttft_change_pct": 1.9281707637068601
      },
      "prefill": {
        "e2e_change_pct": 0.9080993850692831,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 2.6728422580919675,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.892371327204633,
        "ttft_change_pct": 0.8917386420676854
      },
      "prefill2048": {
        "e2e_change_pct": 0.4850796747903674,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6893905760388508,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.48780522627988043,
        "ttft_change_pct": 0.4846824275347661
      },
      "prefill4096": {
        "e2e_change_pct": 0.6079092720157941,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.06021958505744163,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.6058586524545162,
        "ttft_change_pct": 0.6090167311306294
      }
    }
  }
]
```

### Variant q8_0_q4_0

```json
[
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2649.030992900021,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.66920848,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2653.4173859192642,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.467789167000001,
        "peak_device_VRAM_mib": 7204.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.5494949634889963,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6417283476910063,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -2.588320013493828,
        "ttft_change_pct": 0.38102260564694124
      },
      "prefill": {
        "e2e_change_pct": 0.7915046955718763,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.0679885088901386,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.774315035299189,
        "ttft_change_pct": 0.7565757098443315
      },
      "prefill2048": {
        "e2e_change_pct": 0.5960680888369652,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.541830699207213,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6092807043037274,
        "ttft_change_pct": 0.5942051029937279
      },
      "prefill4096": {
        "e2e_change_pct": 0.621654662565585,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6803077893213771,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6147332351422952,
        "ttft_change_pct": 0.6171983613609378
      }
    }
  }
]
```

### Variant q4_0_q4_0

```json
[
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 2599.013028498364,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.108073662,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2618.5108389778597,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.308949404,
        "peak_device_VRAM_mib": 7172.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 2.2891309825985973,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.345185255607162,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -2.2433133784325543,
        "ttft_change_pct": 1.1522841816442586
      },
      "prefill": {
        "e2e_change_pct": 0.3587627216725231,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.05777899097902939,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.36781070513044467,
        "ttft_change_pct": 0.36467714824366393
      },
      "prefill2048": {
        "e2e_change_pct": 0.6920839287919645,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.4614949876799788,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.6818458242014769,
        "ttft_change_pct": 0.6944330832729717
      },
      "prefill4096": {
        "e2e_change_pct": 0.99135476498593,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.124780461844832,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.9832269534550853,
        "ttft_change_pct": 0.988037332534919
      }
    }
  }
]
```

## Decision and remaining research

Attention K/V storage tests remain distinct from recurrent GDN F32 state; F16/Q8/Q4 evidence is retained by exact side,context and quality scope.

**Remaining scope:** R381 isolatedroute screen: longdecodephase improves9.439%, fullE2E0.961%, noenergywin. Independent relevanttaskquality/latency/stability and freshcontrols still needed before scopedqualification. Existing formatnegatives preserved.

**Reopening condition:** A different KV format or mixed policy needs actual SM70 attention support and independent state/quality tests. Existing negative quantizations must not be silently rescued by combinations.

**Next action:** R382: close the20remainingoriginalspecial-HBM variant scope reviews individually using retained implementation/hardware/model evidence (HBM09-13/HBM20-24); identify genuinely feasible missing singles. Preserve R381 as preliminary only. Any later route qualification needs fresh control, realtaskquality/energy and independent stability; do not open kernel tuning branches or combinations/models from this screen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R233](../experiments/R233.md), [R234](../experiments/R234.md), [R270](../experiments/R270.md), [R358](../experiments/R358.md), [R379](../experiments/R379.md), [R380](../experiments/R380.md), [R381](../experiments/R381.md), [R82](../experiments/R82.md), [R83](../experiments/R83.md)
