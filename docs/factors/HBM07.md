# HBM07 — L1/L2/shared-memory reuse

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| QUALIFIED | True | True | P0 |


## Theory and Volta implications

Persistent conversion or shared/cache reuse can reduce redundant reads and dequantization. It consumes capacity and can change the workload that fits.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-01288096354b4d254f2a.md)
- [Original audit hash and public excerpt](../audits/audit-056d794ebc3542e436de.md)
- [Original audit hash and public excerpt](../audits/audit-14791a89af65ec81443c.md)
- [Original audit hash and public excerpt](../audits/audit-1bcbaa3ce104e67fe6d6.md)
- [Original audit hash and public excerpt](../audits/audit-1f940596d115e34ae02f.md)
- [Original audit hash and public excerpt](../audits/audit-22786f761eb0e7bce306.md)
- [Original audit hash and public excerpt](../audits/audit-22d741ba21637e69bc9a.md)
- [Original audit hash and public excerpt](../audits/audit-2680061ad08d56e324f6.md)
- [Original audit hash and public excerpt](../audits/audit-273b2160c856596f102f.md)
- [Original audit hash and public excerpt](../audits/audit-34aef30f35e398a2b566.md)
- [Original audit hash and public excerpt](../audits/audit-3c1799daa595eea43052.md)
- [Original audit hash and public excerpt](../audits/audit-68adf78e010910f8aecd.md)
- [Original audit hash and public excerpt](../audits/audit-72561777b6d13a0a47fe.md)
- [Original audit hash and public excerpt](../audits/audit-74211c6727a78a62efe6.md)
- [Original audit hash and public excerpt](../audits/audit-7a9b64a68a7800dd100d.md)
- [Original audit hash and public excerpt](../audits/audit-7be4a096b60529fdd3d1.md)
- [Original audit hash and public excerpt](../audits/audit-7c91d45dc1aa187fe880.md)
- [Original audit hash and public excerpt](../audits/audit-81a482bba6bcc81336a6.md)
- [Original audit hash and public excerpt](../audits/audit-90c23d1af2a59b1df673.md)
- [Original audit hash and public excerpt](../audits/audit-97b2bd9c2d3316dd4eab.md)
- [Original audit hash and public excerpt](../audits/audit-9a720eae0135df096db9.md)
- [Original audit hash and public excerpt](../audits/audit-b4e2008571fcb429d31e.md)
- [Original audit hash and public excerpt](../audits/audit-c915993a806f0b95c0f6.md)
- [Original audit hash and public excerpt](../audits/audit-cad113d219a201e0f5e0.md)
- [Original audit hash and public excerpt](../audits/audit-cc4a0b8610c091844255.md)
- [Original audit hash and public excerpt](../audits/audit-d3d48f461ddbab44a526.md)
- [Original audit hash and public excerpt](../audits/audit-dbac47e8b176d1ba982a.md)
- [Original audit hash and public excerpt](../audits/audit-dc120944347a4f5cf410.md)
- [Original audit hash and public excerpt](../audits/audit-e5c8f2e9455ada3d921a.md)
- [Original audit hash and public excerpt](../audits/audit-ec82b4c9401ad086f524.md)
- [Original audit hash and public excerpt](../audits/audit-ef37383ee044d72312b7.md)
- [Original audit hash and public excerpt](../audits/audit-f01e69f875f6c1042276.md)
- [Original audit hash and public excerpt](../audits/audit-fe2e5fbb2e31d1cf8f9f.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | PARTIAL | False |
| shared_reuse_patch | BLOCKED | QUALIFIED | True |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
      }
    ],
    "model": "qwen38"
  }
]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant reference

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "metrics": {
      "gpu_energy_j": 41893.38831143596,
      "gpu_j_per_success": 3222.5683316489203,
      "mean_task_gpu_power_w": 257.6306285206843,
      "solved": 13,
      "successes_per_second": 0.08001717934864089,
      "tasks": 18,
      "total_wall_s": 162.46511194
    }
  },
  {
    "metrics": {
      "gpu_energy_j": 37114.11910535685,
      "gpu_j_per_success": 2854.9322388736036,
      "mean_task_gpu_power_w": 203.41011406579594,
      "solved": 13,
      "successes_per_second": 0.07151602353227142,
      "tasks": 18,
      "total_wall_s": 181.777444521
    }
  },
  {
    "metrics": {
      "custom_long_context16": {
        "all_request_wall_s": 76.244765779,
        "gpu_j_per_success": 687.2227446680172,
        "gross_gpu_energy_j": 10995.563914688275,
        "pass_fraction": 1.0,
        "solved": 16,
        "successes_per_request_wall_s": 0.20985047086874073,
        "tasks": 16,
        "truncated": 0
      },
      "full_standard164": {
        "all_request_wall_s": 576.769096475,
        "gpu_j_per_success": 639.3673005695108,
        "gross_gpu_energy_j": 83117.7490740364,
        "pass_fraction": 0.7926829268292683,
        "solved": 130,
        "successes_per_request_wall_s": 0.2253934907305403,
        "tasks": 164,
        "truncated": 4
      },
      "validated_standard163": {
        "all_request_wall_s": 561.253597062,
        "gpu_j_per_success": 622.1833211466443,
        "gross_gpu_energy_j": 80883.83174906376,
        "pass_fraction": 0.7975460122699386,
        "solved": 130,
        "successes_per_request_wall_s": 0.23162435070440943,
        "tasks": 163,
        "truncated": 3
      }
    }
  },
  {
    "metrics": {
      "context4096": {
        "all_request_wall_s": 80.653046237,
        "gpu_j_per_success": 781.8759265291908,
        "gross_gpu_energy_j": 11728.138897937863,
        "median_ttft_s": 1.574552953,
        "solved": 15,
        "successes_per_request_wall_s": 0.18598181593689977,
        "tasks": 16,
        "truncated": 0
      },
      "context6144": {
        "all_request_wall_s": 97.87749229399999,
        "gpu_j_per_success": 945.8989160376854,
        "gross_gpu_energy_j": 14188.48374056528,
        "median_ttft_s": 2.3503545055,
        "solved": 15,
        "successes_per_request_wall_s": 0.15325280254364995,
        "tasks": 16,
        "truncated": 0
      }
    }
  },
  {
    "metrics": {
      "decode": {
        "mad": 0.02904679275687272,
        "median": 79.64844387312178,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill": {
        "mad": 12.666329924800038,
        "median": 2829.1481898484326,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill2048": {
        "mad": 16.5246516733348,
        "median": 3157.212650190627,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill4096": {
        "mad": 15.572489472006282,
        "median": 3188.8400080869606,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      }
    }
  },
  {
    "metrics": {
      "decode": {
        "mad": 0.0007371735000000004,
        "median": 0.08524525,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      },
      "prefill2048": {
        "mad": 0.003421156500000022,
        "median": 0.6719578005,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      },
      "prefill4096": {
        "mad": 0.007726428999999979,
        "median": 1.306233777,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      }
    }
  }
]
```

</details>

### Variant shared_reuse_patch

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "metrics": {
      "gpu_energy_j": 41893.38831143596,
      "gpu_j_per_success": 3222.5683316489203,
      "mean_task_gpu_power_w": 257.6306285206843,
      "solved": 13,
      "successes_per_second": 0.08001717934864089,
      "tasks": 18,
      "total_wall_s": 162.46511194
    }
  },
  {
    "metrics": {
      "gpu_energy_j": 37114.11910535685,
      "gpu_j_per_success": 2854.9322388736036,
      "mean_task_gpu_power_w": 203.41011406579594,
      "solved": 13,
      "successes_per_second": 0.07151602353227142,
      "tasks": 18,
      "total_wall_s": 181.777444521
    }
  },
  {
    "metrics": {
      "custom_long_context16": {
        "all_request_wall_s": 76.244765779,
        "gpu_j_per_success": 687.2227446680172,
        "gross_gpu_energy_j": 10995.563914688275,
        "pass_fraction": 1.0,
        "solved": 16,
        "successes_per_request_wall_s": 0.20985047086874073,
        "tasks": 16,
        "truncated": 0
      },
      "full_standard164": {
        "all_request_wall_s": 576.769096475,
        "gpu_j_per_success": 639.3673005695108,
        "gross_gpu_energy_j": 83117.7490740364,
        "pass_fraction": 0.7926829268292683,
        "solved": 130,
        "successes_per_request_wall_s": 0.2253934907305403,
        "tasks": 164,
        "truncated": 4
      },
      "validated_standard163": {
        "all_request_wall_s": 561.253597062,
        "gpu_j_per_success": 622.1833211466443,
        "gross_gpu_energy_j": 80883.83174906376,
        "pass_fraction": 0.7975460122699386,
        "solved": 130,
        "successes_per_request_wall_s": 0.23162435070440943,
        "tasks": 163,
        "truncated": 3
      }
    }
  },
  {
    "metrics": {
      "context4096": {
        "all_request_wall_s": 80.653046237,
        "gpu_j_per_success": 781.8759265291908,
        "gross_gpu_energy_j": 11728.138897937863,
        "median_ttft_s": 1.574552953,
        "solved": 15,
        "successes_per_request_wall_s": 0.18598181593689977,
        "tasks": 16,
        "truncated": 0
      },
      "context6144": {
        "all_request_wall_s": 97.87749229399999,
        "gpu_j_per_success": 945.8989160376854,
        "gross_gpu_energy_j": 14188.48374056528,
        "median_ttft_s": 2.3503545055,
        "solved": 15,
        "successes_per_request_wall_s": 0.15325280254364995,
        "tasks": 16,
        "truncated": 0
      }
    }
  },
  {
    "metrics": {
      "decode": {
        "mad": 0.02904679275687272,
        "median": 79.64844387312178,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill": {
        "mad": 12.666329924800038,
        "median": 2829.1481898484326,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill2048": {
        "mad": 16.5246516733348,
        "median": 3157.212650190627,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      },
      "prefill4096": {
        "mad": 15.572489472006282,
        "median": 3188.8400080869606,
        "outlier_rule": "retain_all_complete_requests; exclude_rep_negative_warmup",
        "sessions": 2,
        "unit": "tokens/s"
      }
    }
  },
  {
    "metrics": {
      "decode": {
        "mad": 0.0007371735000000004,
        "median": 0.08524525,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      },
      "prefill2048": {
        "mad": 0.003421156500000022,
        "median": 0.6719578005,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      },
      "prefill4096": {
        "mad": 0.007726428999999979,
        "median": 1.306233777,
        "outlier_rule": "Retain all complete observations; use within-session medians then paired block comparisons; no independence or confidence-interval claim from within-session repetitions.",
        "primary": "token_event_ttft_s",
        "sessions": 2,
        "unit": "seconds"
      }
    }
  }
]
```

</details>

## Decision and remaining research

R90 nativer Prefill-Champion und R219/R220-Agenten-Cacheprofil qualifiziert. R219 tatsächlicher Kandidat14106,5MiB/13Erfolge/162,465s; R220 Kontrollprofil7966,5MiB. Mehrspeicher6140MiB gegenüber Graft-Alternative, keine Addition einzelner Gewinne.

**Remaining scope:** ExistingconversioncacheChampionsremainqualified. Newpreferredcarveout hasno GPUtreatment. SelectedQ6decode resourceanalysis defersmore-L1 becausealready8KiBminimumshared. Otherkernels needdistinctresourcebottleneck, notanotherconversioncachetest.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** No selectedQ6decodecarveoutbuild/run. Reopen only a concrete differentresource-constrainedkernel/shape; preserve allscopedconversioncachewins.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R100](../experiments/R100.md), [R107](../experiments/R107.md), [R108](../experiments/R108.md), [R109](../experiments/R109.md), [R122](../experiments/R122.md), [R123](../experiments/R123.md), [R124](../experiments/R124.md), [R125](../experiments/R125.md), [R126](../experiments/R126.md), [R127](../experiments/R127.md), [R132](../experiments/R132.md), [R133](../experiments/R133.md), [R134](../experiments/R134.md), [R136](../experiments/R136.md), [R141](../experiments/R141.md), [R149](../experiments/R149.md), [R165](../experiments/R165.md), [R166](../experiments/R166.md), [R186](../experiments/R186.md), [R213](../experiments/R213.md), [R214](../experiments/R214.md), [R215](../experiments/R215.md), [R216](../experiments/R216.md), [R217](../experiments/R217.md), [R218](../experiments/R218.md), [R219](../experiments/R219.md), [R220](../experiments/R220.md), [R221](../experiments/R221.md), [R222](../experiments/R222.md), [R251](../experiments/R251.md), [R372](../experiments/R372.md), [R391](../experiments/R391.md), [R88](../experiments/R88.md), [R89](../experiments/R89.md), [R90](../experiments/R90.md), [R91](../experiments/R91.md), [R92](../experiments/R92.md), [R93](../experiments/R93.md), [R94](../experiments/R94.md), [R95](../experiments/R95.md), [R603](../experiments/R603.md)
