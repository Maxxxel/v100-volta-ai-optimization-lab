# HBM06 — Dequantization and GEMV/GEMM fusion

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Fused dequantization and matrix products avoid materialized intermediates. Existing fused defaults must not be presented as a newly achieved speedup.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu
- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-68f29d4a2beebd20e166.md)
- [Original audit hash and public excerpt](../audits/audit-dd2d040919ab3ed21d7e.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | ALREADY_ACTIVE | PARTIAL | False |
| fused_variant | BLOCKED | TESTED_NEGATIVE | True |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "ALREADY_ACTIVE"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "fused_variant"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "ALREADY_ACTIVE"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "fused_variant"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "ALREADY_ACTIVE"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "fused_variant"
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
      "A": {
        "QA_GPU_j": 8980.715877693412,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 40.400321383,
        "peak_device_VRAM_mib": 9192.5
      },
      "B": {
        "QA_GPU_j": 2761.7564968004135,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.568496107,
        "peak_device_VRAM_mib": 7244.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": -81.20681277952097,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -76.78236020295357,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 443.71390417312256,
        "ttft_change_pct": -57.97259263888368
      },
      "prefill": {
        "e2e_change_pct": 17.26189911776217,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 33.07045386536773,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -14.76937969213582,
        "ttft_change_pct": 17.26812702767728
      },
      "prefill2048": {
        "e2e_change_pct": 43.959514171010206,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 55.67691859880814,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -30.56372581269877,
        "ttft_change_pct": 43.97517110043889
      },
      "prefill4096": {
        "e2e_change_pct": 49.951848834836454,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 60.06915292600665,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -33.3374361449835,
        "ttft_change_pct": 49.96299014012149
      }
    }
  }
]
```

</details>

### Variant fused_variant

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "metrics": {
      "A": {
        "QA_GPU_j": 8980.715877693412,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 40.400321383,
        "peak_device_VRAM_mib": 9192.5
      },
      "B": {
        "QA_GPU_j": 2761.7564968004135,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.568496107,
        "peak_device_VRAM_mib": 7244.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": -81.20681277952097,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -76.78236020295357,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 443.71390417312256,
        "ttft_change_pct": -57.97259263888368
      },
      "prefill": {
        "e2e_change_pct": 17.26189911776217,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 33.07045386536773,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -14.76937969213582,
        "ttft_change_pct": 17.26812702767728
      },
      "prefill2048": {
        "e2e_change_pct": 43.959514171010206,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 55.67691859880814,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -30.56372581269877,
        "ttft_change_pct": 43.97517110043889
      },
      "prefill4096": {
        "e2e_change_pct": 49.951848834836454,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 60.06915292600665,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -33.3374361449835,
        "ttft_change_pct": 49.96299014012149
      }
    }
  }
]
```

</details>

## Decision and remaining research

Identischer C11-Beleg wiederverwendet, kein zusätzlicher GPU-Lauf. Neue Fusion benötigt einen nachweislich noch entfuzten aktuellen Hotspot; HBM07-Cache ist ein anderes Verfahren.

**Remaining scope:** A genuinely new fusion must identify an unfused current hot path and provide a numerically equivalent implemented kernel; same fused operation under another flag is insufficient.

**Reopening condition:** A genuinely new fusion must identify an unfused current hot path and provide a numerically equivalent implemented kernel; same fused operation under another flag is insufficient.

**Next action:** Need an actually unfused current hot path plus a distinct semantically equivalent implemented fusion. Existing MMVQ/MMQ and HBM07 conversion reuse are not a new fusion.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R357](../experiments/R357.md)
