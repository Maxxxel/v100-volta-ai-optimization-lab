# HBM15 — VMM and allocator fragmentation

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Disabling virtual-memory management changes allocation behavior and memory overhead. Warm throughput does not establish cold-start or fragmentation effects.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-ccaadd14ebc9e9edc4d9.md)
- [Original audit hash and public excerpt](../audits/audit-fe73faa6d74ccb07bdc1.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | READY_LINKED | PARTIAL | False |
| no_vmm_build | READY_LINKED | PARTIAL | True |


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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
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
        "value": "reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "no_vmm_build"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant reference

```json
[
  {
    "archive_sha256": "513276f0488967fd00079bfbd187f94ccba0f065fa6fad239fecb77ce3b4b30f",
    "metrics": {
      "A": {
        "QA_GPU_j": 2549.346625170113,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.112131582,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2541.6155632785653,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.108141614,
        "peak_device_VRAM_mib": 7424.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": -0.02530076586645391,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.08247140732459135,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.028087400164400478,
        "ttft_change_pct": 0.07183530173475727
      },
      "prefill": {
        "e2e_change_pct": -0.11303024342359524,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.2662754357735118,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.19983330117991915,
        "ttft_change_pct": -0.09777227615743733
      },
      "prefill2048": {
        "e2e_change_pct": 0.19226635578188933,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6531036172679583,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.18479819396499675,
        "ttft_change_pct": 0.18573653277658142
      },
      "prefill4096": {
        "e2e_change_pct": 0.18636765447024306,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.7354737339708706,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.19100633273293477,
        "ttft_change_pct": 0.19024017629458712
      }
    },
    "plan": {
      "sha256": "b2d60995bcb478abf8ae2ddb950b17529ac7c591b3774c66fd4204124c61b697"
    },
    "raw_members": [
      {
        "sha256": "2e0378d06c3fa28179ed6324bbf86396f32021e3868bc3838e7f1532213247b4"
      },
      {
        "sha256": "5ed480736e233078858fda5882fd039191726cd117f8830f4a0f2dcd77d4905b"
      },
      {
        "sha256": "2ff6dd294ac9a5c8ad3754f0cfa9a66eb2bd001b970ab0736bfe17e74749bea7"
      },
      {
        "sha256": "f942ed9b68da76bd5035764195c1c30b798e17708a07286612070c99d12a9aaf"
      },
      {
        "sha256": "dbe0bce8ba8d8ef496c773f92bd572473278242ad1a3a209b171df43c0672201"
      },
      {
        "sha256": "1d72c625fab5cc364acee8e37d4c1af6276534876da8e57eaf03f2c47052221a"
      },
      {
        "sha256": "e3dae91b493dd0b5ebdbaa5e013486d1581feb23bc7f302ca499fc73347f9f18"
      },
      {
        "sha256": "dbe0bce8ba8d8ef496c773f92bd572473278242ad1a3a209b171df43c0672201"
      },
      {
        "sha256": "c34db82498dda513782d5380ef43419182c7aa61ce4e709316d5886f7e1b974d"
      },
      {
        "sha256": "70aec4aeba881d6631d76d5cba42f95dc07dea6fdd7d1ffd15646487b0726818"
      },
      {
        "sha256": "5ed480736e233078858fda5882fd039191726cd117f8830f4a0f2dcd77d4905b"
      },
      {
        "sha256": "7379b1937e84a206627a84202da6d679eb9fa5410ebbde99d3046cf0b970b945"
      },
      {
        "sha256": "46f6a649e88ca66fc1291307117ae0ea17036aef78f934f1fd6c2989eea342bf"
      }
    ],
    "results": {
      "sha256": "ccaadd14ebc9e9edc4d96d603c8d9f869b43bfd9dcf1ab1cc8234acdc03a2a8d"
    },
    "runs": [
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      }
    ]
  }
]
```

### Variant no_vmm_build

```json
[
  {
    "archive_sha256": "513276f0488967fd00079bfbd187f94ccba0f065fa6fad239fecb77ce3b4b30f",
    "metrics": {
      "A": {
        "QA_GPU_j": 2549.346625170113,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.112131582,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_GPU_j": 2541.6155632785653,
        "QA_unique_tasks": 12,
        "QA_wall_sum_s": 10.108141614,
        "peak_device_VRAM_mib": 7424.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": -0.02530076586645391,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.08247140732459135,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.028087400164400478,
        "ttft_change_pct": 0.07183530173475727
      },
      "prefill": {
        "e2e_change_pct": -0.11303024342359524,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.2662754357735118,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.19983330117991915,
        "ttft_change_pct": -0.09777227615743733
      },
      "prefill2048": {
        "e2e_change_pct": 0.19226635578188933,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.6531036172679583,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.18479819396499675,
        "ttft_change_pct": 0.18573653277658142
      },
      "prefill4096": {
        "e2e_change_pct": 0.18636765447024306,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.7354737339708706,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.19100633273293477,
        "ttft_change_pct": 0.19024017629458712
      }
    },
    "plan": {
      "sha256": "b2d60995bcb478abf8ae2ddb950b17529ac7c591b3774c66fd4204124c61b697"
    },
    "raw_members": [
      {
        "sha256": "2e0378d06c3fa28179ed6324bbf86396f32021e3868bc3838e7f1532213247b4"
      },
      {
        "sha256": "5ed480736e233078858fda5882fd039191726cd117f8830f4a0f2dcd77d4905b"
      },
      {
        "sha256": "2ff6dd294ac9a5c8ad3754f0cfa9a66eb2bd001b970ab0736bfe17e74749bea7"
      },
      {
        "sha256": "f942ed9b68da76bd5035764195c1c30b798e17708a07286612070c99d12a9aaf"
      },
      {
        "sha256": "dbe0bce8ba8d8ef496c773f92bd572473278242ad1a3a209b171df43c0672201"
      },
      {
        "sha256": "1d72c625fab5cc364acee8e37d4c1af6276534876da8e57eaf03f2c47052221a"
      },
      {
        "sha256": "e3dae91b493dd0b5ebdbaa5e013486d1581feb23bc7f302ca499fc73347f9f18"
      },
      {
        "sha256": "dbe0bce8ba8d8ef496c773f92bd572473278242ad1a3a209b171df43c0672201"
      },
      {
        "sha256": "c34db82498dda513782d5380ef43419182c7aa61ce4e709316d5886f7e1b974d"
      },
      {
        "sha256": "70aec4aeba881d6631d76d5cba42f95dc07dea6fdd7d1ffd15646487b0726818"
      },
      {
        "sha256": "5ed480736e233078858fda5882fd039191726cd117f8830f4a0f2dcd77d4905b"
      },
      {
        "sha256": "7379b1937e84a206627a84202da6d679eb9fa5410ebbde99d3046cf0b970b945"
      },
      {
        "sha256": "46f6a649e88ca66fc1291307117ae0ea17036aef78f934f1fd6c2989eea342bf"
      }
    ],
    "results": {
      "sha256": "ccaadd14ebc9e9edc4d96d603c8d9f869b43bfd9dcf1ab1cc8234acdc03a2a8d"
    },
    "runs": [
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      },
      {
        "actual_CUDA_device_and_library_mapped": true,
        "profiler_present": false
      }
    ]
  }
]
```

## Decision and remaining research

C06 no-VMM ist realer vorhandener Allocatorvergleich: Gerätepeak7356,5→7424,5MiB. Kein qualifizierter praktischer Gewinner und kein Nachweis allgemeiner Fragmentierungsbehebung.

**Remaining scope:** Nur bei reproduzierbarer neuer Allokations-/Lebensdauerfragmentierung einen konkreten Allocatorfix testen; no-VMM nicht erneut blind bauen.

**Reopening condition:** Nur bei reproduzierbarer neuer Allokations-/Lebensdauerfragmentierung einen konkreten Allocatorfix testen; no-VMM nicht erneut blind bauen.

**Next action:** Nur bei reproduzierbarer neuer Allokations-/Lebensdauerfragmentierung einen konkreten Allocatorfix testen; no-VMM nicht erneut blind bauen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R374](../experiments/R374.md)
