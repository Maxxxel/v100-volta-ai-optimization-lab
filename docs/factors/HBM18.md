# HBM18 — Volta-specific flash attention

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Flash attention fuses attention operations to reduce intermediate memory traffic. Actual support depends on head dimensions, KV formats and compiled SM70 kernels.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/docs/FA_V100_AUDIT.md
- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fa_v100_prefill.py

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2d48a4fdae7ce747ef64.md)
- [Original audit hash and public excerpt](../audits/audit-4a63c493e0301a646d00.md)
- [Original audit hash and public excerpt](../audits/audit-6924d1fa43aaa9766b96.md)
- [Original audit hash and public excerpt](../audits/audit-9de95af06dcc3290e44f.md)
- [Original audit hash and public excerpt](../audits/audit-a200c5c240a36583e62e.md)
- [Original audit hash and public excerpt](../audits/audit-b8a83b89fd187aadf424.md)
- [Original audit hash and public excerpt](../audits/audit-e950bd432e12a6880a36.md)
- [Original audit hash and public excerpt](../audits/audit-f2e1299acd91cad7c2df.md)
- [Original audit hash and public excerpt](../audits/audit-fe73faa6d74ccb07bdc1.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | READY_LINKED | PARTIAL | True |
| on | READY_LINKED | PARTIAL | False |
| volta_fork_port | IMPLEMENTED_QUEUED | PARTIAL | True |


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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "IMPLEMENTED_QUEUED"
        ],
        "signed_window_signatures": [
          "074f9b8f5ed37d6d90aea4a2fb0740183eae381ce69424317ff1916b692aaf4a",
          "2f1977a5bc7e15ef49e9df3f1021dda4613baadc4d0cbf2263b38cd1e2b1269e",
          "e6b4a6c04ff44953d91ed4ce71fdb2f1b0aa477663d01b5e3bdca230eb653007"
        ],
        "value": "volta_fork_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "volta_fork_port"
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
        "value": "off"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "on"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "volta_fork_port"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant off

```json
[
  {
    "archive": {
      "sha256": "d3d93621974bcfd2be7c2e75833a07dc98c289216c3b153b35b82f43896f19ac"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03844532078679519,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.035260940655268413,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.02520997458221874,
        "ttft_change_pct": -0.33056797697259555
      },
      "prefill": {
        "e2e_change_pct": 1.4710573859948006,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.4038656739217892,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.439751553284352,
        "ttft_change_pct": 1.4802534460955696
      },
      "prefill2048": {
        "e2e_change_pct": 1.5468451839961483,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.6275813413755076,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.547304624789192,
        "ttft_change_pct": 1.5468610296409002
      },
      "prefill4096": {
        "e2e_change_pct": 2.4680000603759744,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.567504033119806,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.4124958080922965,
        "ttft_change_pct": 2.4733440672718654
      }
    },
    "plan": {
      "sha256": "1f999f21d61313c6a2a1852c01fa6c0614d9f788a57ca084dfc5699ace70ef33"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "c49ae91886c5baf59d2027c0ae7e7b5ffba7a41618ab3854aacd22898795aa98"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "adfcf8aedf3b4aa16ff286bfcd85e76fdba92ecd15896391841b8b40db7b5b9f"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "f441d57baefbd4fe7139dc705d2971d7b5abdb54ebbe6866e30d9eb218554642"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "771452687b79b8ec7e3c3893c344e7026d46c89beadd3022cde9a9c10f9a11b4"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "e16c7d4b1adbaa35de5e1c283a2c12a67bcbce726330d8d8ebcd86afade43f32"
      }
    ],
    "results": {
      "sha256": "4a63c493e0301a646d009c4df1f921d8cc513154a92f10d0702aecee192dddff"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d3e137d887765bb9bb3d480760a67876cff67772e29febb65a80e17248164cc6"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.01872961166982101,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6199502826767178,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.01000078456289133,
        "ttft_change_pct": 1.0596644396206445
      },
      "prefill": {
        "e2e_change_pct": -0.21993978649137436,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.7969677712090784,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.20823820195625675,
        "ttft_change_pct": -0.17340640463117118
      },
      "prefill2048": {
        "e2e_change_pct": -0.08157444742422637,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.4910401590483504,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.07518313167673707,
        "ttft_change_pct": -0.08154730747818029
      },
      "prefill4096": {
        "e2e_change_pct": -0.11011789060569876,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.7751808979532093,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.08724369579711233,
        "ttft_change_pct": -0.10846497132217525
      }
    },
    "plan": {
      "sha256": "2def7efc4d736ccd0b9cfa60c060155c2fe8359c46b1127a22233e9ad3244e65"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "df265af3dc03e64b0cca45de8cabf98d2895a50fd6431fd5e012c197d0b057c3"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "a1ab66d55ac91834a54130d86b72c4721f2552c2d49f2d6bd666ed9d6c62dab6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "759171e9ed96ea7fb111df474034ddcc971809c68e2beae90fee55e55ea4f5b6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "5f01905b3624fe6eb277081dee2793786aed9c781bb364eb0551a910b2eed373"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "cc0e4a793ba24ba4103148c117881400797c823093d9b59c7ed66cee9574583c"
      }
    ],
    "results": {
      "sha256": "2d48a4fdae7ce747ef64980e98b6fc659cced31dd640ef070ffdbadc2fa3ba03"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d1a51db005f0974c9efecae4bf1fc37d652a5c209c47046f8e8a2d8ff2f445a5"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.7546207468939636,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.07939342716145603,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.7395577101842354,
        "ttft_change_pct": 0.9819498249429293
      },
      "prefill": {
        "e2e_change_pct": 0.6014253683975568,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5153322027265492,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.6525066614318176,
        "ttft_change_pct": 0.6209104980808622
      },
      "prefill2048": {
        "e2e_change_pct": 1.523029027381373,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.9667152435937751,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.5075865827430146,
        "ttft_change_pct": 1.5296689227545013
      },
      "prefill4096": {
        "e2e_change_pct": 2.240279897585973,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 4.2379725753622255,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.1912743541844693,
        "ttft_change_pct": 2.238612787069827
      }
    },
    "plan": {
      "sha256": "0bbf15f30c2046796bfb5da6e1e2de48d25715cbf98c3f61658a78fd23011b5d"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "3665ec1903ec5402bcb4e75af63617b80cf96828dc7fd838b454fbafd153f3a3"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "e8709b1fa08813aa1b097fb7c1a5da333e4c42d269fa928303c3c2b732acf24b"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "d21cec598cd7bb58f16f531b33cdcbd3f8c83effe34bb4dcae22ac8f1a2a1c09"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "7e7acd19fb427dad949fdcac8ce590415566f0c6666f473142feaacf51050810"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "cd26493eea40f14f0e61a8853caa16f7e0eb50d8d98fc8524fcb8b9433c2f976"
      }
    ],
    "results": {
      "sha256": "6924d1fa43aaa9766b9670f9d58a431e88292599fad2cd4595c6dd5c28c43d24"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "f734b356f3c833efaa8146f80325b15efe60b2c7b20277c2869180fc3943ad8f"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.12094202283677857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2856470069623529,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.11882657494497462,
        "ttft_change_pct": -0.28305017804981514
      },
      "prefill": {
        "e2e_change_pct": 0.0777428639953115,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5546811581639175,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.10236772686988971,
        "ttft_change_pct": 0.05896704382681861
      },
      "prefill2048": {
        "e2e_change_pct": -0.6585947020502081,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.1133234268202452,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.6722642854425809,
        "ttft_change_pct": -0.6546126659291995
      },
      "prefill4096": {
        "e2e_change_pct": -1.0945844952338857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5452301253211065,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.1063714542294933,
        "ttft_change_pct": -1.0952972692583884
      }
    },
    "numerical_results": [
      {
        "begin_ns": 419851260534344,
        "end_ns": 419852218338664,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      },
      {
        "begin_ns": 419896556077540,
        "end_ns": 419897212462880,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      }
    ],
    "plan": {
      "sha256": "ba39820e1e798c12fa493e65535d58603adf8bf8b6e42b82256897aefc3820a2"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "6894fb362340e3a4d8f28f2612804633905a92c4ed130a2c5d3a5645d3f67363"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "2978e3df7b4a69f71e42ba70fb7cc7c14fdaa8dfae3a8db43654216da8427d23"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "3d0fbd23eb44f859a966295268fb6f4348af2fb9bb918c85e101ea8314bce760"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "c5ab0ca6fa240685b494bed10a6db33e3d092e249b7b2663311b0d166a750420"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "7b0af48817cdd47263ca19d707b57ffa221c0421aa59ad06c9a5eac47f66a246"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "c4f6499ca9cb5cfb14f1707d5aecad276c5ab6a0867e6882673fd5c3bd8b2c3f"
      },
      {
        "sha256": "57b687c2591b91775455adf9ca1fbd042adb2eae6b41bf2ac795fed51280db91"
      }
    ],
    "results": {
      "sha256": "e950bd432e12a6880a36aa5abf80fa654f5eb655c9d9de54413c1292cf2e44b8"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "4a1a610e3bb140088015e839091e17b3d72a981ec4ac515fb3b03790f75e1900"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.02890953625340753,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.36050347029360497,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.005611639230274079,
        "ttft_change_pct": 0.0011794624995342673
      },
      "prefill": {
        "e2e_change_pct": 0.32741308559378623,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.8231634235959517,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.2896480127901224,
        "ttft_change_pct": 0.32520613652560204
      },
      "prefill2048": {
        "e2e_change_pct": -0.5936452279304949,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9047104540210515,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.5924174957517181,
        "ttft_change_pct": -0.5883653398635391
      },
      "prefill4096": {
        "e2e_change_pct": -1.3222520400019477,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6731597927917998,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.3396620744484222,
        "ttft_change_pct": -1.3238337476255357
      }
    },
    "numerical_results": [
      {
        "begin_ns": 422121923689996,
        "end_ns": 422123735022939,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      },
      {
        "begin_ns": 422168251279398,
        "end_ns": 422169812063566,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      }
    ],
    "plan": {
      "sha256": "ed2b2ef653fe0fdb46efccdd2128daf4c3b100c6e5136a8111922c5a7a203e91"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "843be0e25d5409335c4d0250ee0372ca59e12674b776014aead48a6685bd11ef"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "b82ac6982a30585dde08668a7e864c3d55f83217e4e21206c6c03147a537a487"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "c52d253cf8a5b51fdaf2d29a9c934ac01698e72fe31c0d0ef56491048c6705c8"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "64eedb2c1b91e366a6294be25247a86f2a28035ca8e41028f0ccd7fcd527f515"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "f333a211f5fe4d3177e45f2c683dadb7620853649d85a8a3a22fd340e1de08ee"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "e37313b4dcb005c16007f502b412528e60916399a650cc5a240d188ecb79e1d1"
      },
      {
        "sha256": "b2c594f7a94812d074d99c1b5657f82af00ad3c40f01e6dde2951221b438506f"
      }
    ],
    "results": {
      "sha256": "9de95af06dcc3290e44fd619da2eadc3fa738a4cd2237a361f0bc2ad8a875dcb"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "468d2dfd5258ff403340077a7d35623db3540eb7039c610fcfee6b3e5bcd0053"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03503157045112726,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2513145889854407,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.012265723416837737,
        "ttft_change_pct": -0.4501650513101474
      },
      "prefill": {
        "e2e_change_pct": -0.009999258488779805,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -5.956983196393962,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.014861421090606175,
        "ttft_change_pct": 0.010265633072203961
      },
      "prefill2048": {
        "e2e_change_pct": -0.25711078793596576,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9707387687063473,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.24877340370492718,
        "ttft_change_pct": -0.25277945019878123
      },
      "prefill4096": {
        "e2e_change_pct": -0.15154001546083817,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.3300460822200488,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.14205097060184801,
        "ttft_change_pct": -0.1468214065870166
      }
    },
    "plan": {
      "sha256": "6a37c4abc88444a34b033036ab93edebe2760bfbb9285014197e8f6e316b2839"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "0473cb2a053a4480fff31c9d11703fad0a6cac5a2ed46bf621d1410ad80bc415"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "fa019eb42d0beb6867e9117504d5968f70fab3094841da95a874e1871ce99489"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "19ab050677a7ccacefe87bc71037b8c557cc610f077890b487922fb7d0806f01"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "4629b0a9d0aa4a41e8efbab7800c3972e2289bc23999d5a58f572b64812483fd"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "f40f8304c1599872baf81de85305d52fccb2b0ed5baddab4d38f297600882624"
      }
    ],
    "results": {
      "sha256": "a200c5c240a36583e62e17eedfe4f741c7b69bbe5af0b190bd9e0a65b937e682"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  }
]
```

### Variant on

```json
[
  {
    "archive": {
      "sha256": "d3d93621974bcfd2be7c2e75833a07dc98c289216c3b153b35b82f43896f19ac"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03844532078679519,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.035260940655268413,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.02520997458221874,
        "ttft_change_pct": -0.33056797697259555
      },
      "prefill": {
        "e2e_change_pct": 1.4710573859948006,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.4038656739217892,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.439751553284352,
        "ttft_change_pct": 1.4802534460955696
      },
      "prefill2048": {
        "e2e_change_pct": 1.5468451839961483,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.6275813413755076,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.547304624789192,
        "ttft_change_pct": 1.5468610296409002
      },
      "prefill4096": {
        "e2e_change_pct": 2.4680000603759744,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.567504033119806,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.4124958080922965,
        "ttft_change_pct": 2.4733440672718654
      }
    },
    "plan": {
      "sha256": "1f999f21d61313c6a2a1852c01fa6c0614d9f788a57ca084dfc5699ace70ef33"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "c49ae91886c5baf59d2027c0ae7e7b5ffba7a41618ab3854aacd22898795aa98"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "adfcf8aedf3b4aa16ff286bfcd85e76fdba92ecd15896391841b8b40db7b5b9f"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "f441d57baefbd4fe7139dc705d2971d7b5abdb54ebbe6866e30d9eb218554642"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "771452687b79b8ec7e3c3893c344e7026d46c89beadd3022cde9a9c10f9a11b4"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "e16c7d4b1adbaa35de5e1c283a2c12a67bcbce726330d8d8ebcd86afade43f32"
      }
    ],
    "results": {
      "sha256": "4a63c493e0301a646d009c4df1f921d8cc513154a92f10d0702aecee192dddff"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d3e137d887765bb9bb3d480760a67876cff67772e29febb65a80e17248164cc6"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.01872961166982101,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6199502826767178,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.01000078456289133,
        "ttft_change_pct": 1.0596644396206445
      },
      "prefill": {
        "e2e_change_pct": -0.21993978649137436,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.7969677712090784,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.20823820195625675,
        "ttft_change_pct": -0.17340640463117118
      },
      "prefill2048": {
        "e2e_change_pct": -0.08157444742422637,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.4910401590483504,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.07518313167673707,
        "ttft_change_pct": -0.08154730747818029
      },
      "prefill4096": {
        "e2e_change_pct": -0.11011789060569876,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.7751808979532093,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.08724369579711233,
        "ttft_change_pct": -0.10846497132217525
      }
    },
    "plan": {
      "sha256": "2def7efc4d736ccd0b9cfa60c060155c2fe8359c46b1127a22233e9ad3244e65"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "df265af3dc03e64b0cca45de8cabf98d2895a50fd6431fd5e012c197d0b057c3"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "a1ab66d55ac91834a54130d86b72c4721f2552c2d49f2d6bd666ed9d6c62dab6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "759171e9ed96ea7fb111df474034ddcc971809c68e2beae90fee55e55ea4f5b6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "5f01905b3624fe6eb277081dee2793786aed9c781bb364eb0551a910b2eed373"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "cc0e4a793ba24ba4103148c117881400797c823093d9b59c7ed66cee9574583c"
      }
    ],
    "results": {
      "sha256": "2d48a4fdae7ce747ef64980e98b6fc659cced31dd640ef070ffdbadc2fa3ba03"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d1a51db005f0974c9efecae4bf1fc37d652a5c209c47046f8e8a2d8ff2f445a5"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.7546207468939636,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.07939342716145603,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.7395577101842354,
        "ttft_change_pct": 0.9819498249429293
      },
      "prefill": {
        "e2e_change_pct": 0.6014253683975568,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5153322027265492,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.6525066614318176,
        "ttft_change_pct": 0.6209104980808622
      },
      "prefill2048": {
        "e2e_change_pct": 1.523029027381373,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.9667152435937751,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.5075865827430146,
        "ttft_change_pct": 1.5296689227545013
      },
      "prefill4096": {
        "e2e_change_pct": 2.240279897585973,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 4.2379725753622255,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.1912743541844693,
        "ttft_change_pct": 2.238612787069827
      }
    },
    "plan": {
      "sha256": "0bbf15f30c2046796bfb5da6e1e2de48d25715cbf98c3f61658a78fd23011b5d"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "3665ec1903ec5402bcb4e75af63617b80cf96828dc7fd838b454fbafd153f3a3"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "e8709b1fa08813aa1b097fb7c1a5da333e4c42d269fa928303c3c2b732acf24b"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "d21cec598cd7bb58f16f531b33cdcbd3f8c83effe34bb4dcae22ac8f1a2a1c09"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "7e7acd19fb427dad949fdcac8ce590415566f0c6666f473142feaacf51050810"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "cd26493eea40f14f0e61a8853caa16f7e0eb50d8d98fc8524fcb8b9433c2f976"
      }
    ],
    "results": {
      "sha256": "6924d1fa43aaa9766b9670f9d58a431e88292599fad2cd4595c6dd5c28c43d24"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "f734b356f3c833efaa8146f80325b15efe60b2c7b20277c2869180fc3943ad8f"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.12094202283677857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2856470069623529,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.11882657494497462,
        "ttft_change_pct": -0.28305017804981514
      },
      "prefill": {
        "e2e_change_pct": 0.0777428639953115,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5546811581639175,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.10236772686988971,
        "ttft_change_pct": 0.05896704382681861
      },
      "prefill2048": {
        "e2e_change_pct": -0.6585947020502081,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.1133234268202452,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.6722642854425809,
        "ttft_change_pct": -0.6546126659291995
      },
      "prefill4096": {
        "e2e_change_pct": -1.0945844952338857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5452301253211065,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.1063714542294933,
        "ttft_change_pct": -1.0952972692583884
      }
    },
    "numerical_results": [
      {
        "begin_ns": 419851260534344,
        "end_ns": 419852218338664,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      },
      {
        "begin_ns": 419896556077540,
        "end_ns": 419897212462880,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      }
    ],
    "plan": {
      "sha256": "ba39820e1e798c12fa493e65535d58603adf8bf8b6e42b82256897aefc3820a2"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "6894fb362340e3a4d8f28f2612804633905a92c4ed130a2c5d3a5645d3f67363"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "2978e3df7b4a69f71e42ba70fb7cc7c14fdaa8dfae3a8db43654216da8427d23"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "3d0fbd23eb44f859a966295268fb6f4348af2fb9bb918c85e101ea8314bce760"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "c5ab0ca6fa240685b494bed10a6db33e3d092e249b7b2663311b0d166a750420"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "7b0af48817cdd47263ca19d707b57ffa221c0421aa59ad06c9a5eac47f66a246"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "c4f6499ca9cb5cfb14f1707d5aecad276c5ab6a0867e6882673fd5c3bd8b2c3f"
      },
      {
        "sha256": "57b687c2591b91775455adf9ca1fbd042adb2eae6b41bf2ac795fed51280db91"
      }
    ],
    "results": {
      "sha256": "e950bd432e12a6880a36aa5abf80fa654f5eb655c9d9de54413c1292cf2e44b8"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "4a1a610e3bb140088015e839091e17b3d72a981ec4ac515fb3b03790f75e1900"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.02890953625340753,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.36050347029360497,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.005611639230274079,
        "ttft_change_pct": 0.0011794624995342673
      },
      "prefill": {
        "e2e_change_pct": 0.32741308559378623,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.8231634235959517,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.2896480127901224,
        "ttft_change_pct": 0.32520613652560204
      },
      "prefill2048": {
        "e2e_change_pct": -0.5936452279304949,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9047104540210515,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.5924174957517181,
        "ttft_change_pct": -0.5883653398635391
      },
      "prefill4096": {
        "e2e_change_pct": -1.3222520400019477,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6731597927917998,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.3396620744484222,
        "ttft_change_pct": -1.3238337476255357
      }
    },
    "numerical_results": [
      {
        "begin_ns": 422121923689996,
        "end_ns": 422123735022939,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      },
      {
        "begin_ns": 422168251279398,
        "end_ns": 422169812063566,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      }
    ],
    "plan": {
      "sha256": "ed2b2ef653fe0fdb46efccdd2128daf4c3b100c6e5136a8111922c5a7a203e91"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "843be0e25d5409335c4d0250ee0372ca59e12674b776014aead48a6685bd11ef"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "b82ac6982a30585dde08668a7e864c3d55f83217e4e21206c6c03147a537a487"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "c52d253cf8a5b51fdaf2d29a9c934ac01698e72fe31c0d0ef56491048c6705c8"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "64eedb2c1b91e366a6294be25247a86f2a28035ca8e41028f0ccd7fcd527f515"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "f333a211f5fe4d3177e45f2c683dadb7620853649d85a8a3a22fd340e1de08ee"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "e37313b4dcb005c16007f502b412528e60916399a650cc5a240d188ecb79e1d1"
      },
      {
        "sha256": "b2c594f7a94812d074d99c1b5657f82af00ad3c40f01e6dde2951221b438506f"
      }
    ],
    "results": {
      "sha256": "9de95af06dcc3290e44fd619da2eadc3fa738a4cd2237a361f0bc2ad8a875dcb"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "468d2dfd5258ff403340077a7d35623db3540eb7039c610fcfee6b3e5bcd0053"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03503157045112726,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2513145889854407,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.012265723416837737,
        "ttft_change_pct": -0.4501650513101474
      },
      "prefill": {
        "e2e_change_pct": -0.009999258488779805,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -5.956983196393962,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.014861421090606175,
        "ttft_change_pct": 0.010265633072203961
      },
      "prefill2048": {
        "e2e_change_pct": -0.25711078793596576,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9707387687063473,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.24877340370492718,
        "ttft_change_pct": -0.25277945019878123
      },
      "prefill4096": {
        "e2e_change_pct": -0.15154001546083817,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.3300460822200488,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.14205097060184801,
        "ttft_change_pct": -0.1468214065870166
      }
    },
    "plan": {
      "sha256": "6a37c4abc88444a34b033036ab93edebe2760bfbb9285014197e8f6e316b2839"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "0473cb2a053a4480fff31c9d11703fad0a6cac5a2ed46bf621d1410ad80bc415"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "fa019eb42d0beb6867e9117504d5968f70fab3094841da95a874e1871ce99489"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "19ab050677a7ccacefe87bc71037b8c557cc610f077890b487922fb7d0806f01"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "4629b0a9d0aa4a41e8efbab7800c3972e2289bc23999d5a58f572b64812483fd"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "f40f8304c1599872baf81de85305d52fccb2b0ed5baddab4d38f297600882624"
      }
    ],
    "results": {
      "sha256": "a200c5c240a36583e62e17eedfe4f741c7b69bbe5af0b190bd9e0a65b937e682"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  }
]
```

### Variant volta_fork_port

```json
[
  {
    "archive": {
      "sha256": "d3d93621974bcfd2be7c2e75833a07dc98c289216c3b153b35b82f43896f19ac"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03844532078679519,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.035260940655268413,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.02520997458221874,
        "ttft_change_pct": -0.33056797697259555
      },
      "prefill": {
        "e2e_change_pct": 1.4710573859948006,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.4038656739217892,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.439751553284352,
        "ttft_change_pct": 1.4802534460955696
      },
      "prefill2048": {
        "e2e_change_pct": 1.5468451839961483,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.6275813413755076,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.547304624789192,
        "ttft_change_pct": 1.5468610296409002
      },
      "prefill4096": {
        "e2e_change_pct": 2.4680000603759744,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 3.567504033119806,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.4124958080922965,
        "ttft_change_pct": 2.4733440672718654
      }
    },
    "plan": {
      "sha256": "1f999f21d61313c6a2a1852c01fa6c0614d9f788a57ca084dfc5699ace70ef33"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "c49ae91886c5baf59d2027c0ae7e7b5ffba7a41618ab3854aacd22898795aa98"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "adfcf8aedf3b4aa16ff286bfcd85e76fdba92ecd15896391841b8b40db7b5b9f"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "f441d57baefbd4fe7139dc705d2971d7b5abdb54ebbe6866e30d9eb218554642"
      },
      {
        "sha256": "9e536b98ae9cc6b453103add4cb0c679e485ce5e615d712f812685e8da241011"
      },
      {
        "sha256": "771452687b79b8ec7e3c3893c344e7026d46c89beadd3022cde9a9c10f9a11b4"
      },
      {
        "sha256": "1127dd7f462e0191ec579e5e6a21d12d2ea5c7a13e91f5ef47a672cde3ce649b"
      },
      {
        "sha256": "e16c7d4b1adbaa35de5e1c283a2c12a67bcbce726330d8d8ebcd86afade43f32"
      }
    ],
    "results": {
      "sha256": "4a63c493e0301a646d009c4df1f921d8cc513154a92f10d0702aecee192dddff"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d3e137d887765bb9bb3d480760a67876cff67772e29febb65a80e17248164cc6"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.01872961166982101,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6199502826767178,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.01000078456289133,
        "ttft_change_pct": 1.0596644396206445
      },
      "prefill": {
        "e2e_change_pct": -0.21993978649137436,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.7969677712090784,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.20823820195625675,
        "ttft_change_pct": -0.17340640463117118
      },
      "prefill2048": {
        "e2e_change_pct": -0.08157444742422637,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.4910401590483504,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.07518313167673707,
        "ttft_change_pct": -0.08154730747818029
      },
      "prefill4096": {
        "e2e_change_pct": -0.11011789060569876,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.7751808979532093,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.08724369579711233,
        "ttft_change_pct": -0.10846497132217525
      }
    },
    "plan": {
      "sha256": "2def7efc4d736ccd0b9cfa60c060155c2fe8359c46b1127a22233e9ad3244e65"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "df265af3dc03e64b0cca45de8cabf98d2895a50fd6431fd5e012c197d0b057c3"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "a1ab66d55ac91834a54130d86b72c4721f2552c2d49f2d6bd666ed9d6c62dab6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "759171e9ed96ea7fb111df474034ddcc971809c68e2beae90fee55e55ea4f5b6"
      },
      {
        "sha256": "444d7d2491f62ad52e3d460e77b256aaa6d7f311c0dad40f151309357510f074"
      },
      {
        "sha256": "5f01905b3624fe6eb277081dee2793786aed9c781bb364eb0551a910b2eed373"
      },
      {
        "sha256": "071e012edb5a6caf68483864e15f163e7a40c088c3c99fee6a418b05caff4e9d"
      },
      {
        "sha256": "cc0e4a793ba24ba4103148c117881400797c823093d9b59c7ed66cee9574583c"
      }
    ],
    "results": {
      "sha256": "2d48a4fdae7ce747ef64980e98b6fc659cced31dd640ef070ffdbadc2fa3ba03"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "d1a51db005f0974c9efecae4bf1fc37d652a5c209c47046f8e8a2d8ff2f445a5"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": 0.7546207468939636,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.07939342716145603,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.7395577101842354,
        "ttft_change_pct": 0.9819498249429293
      },
      "prefill": {
        "e2e_change_pct": 0.6014253683975568,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5153322027265492,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.6525066614318176,
        "ttft_change_pct": 0.6209104980808622
      },
      "prefill2048": {
        "e2e_change_pct": 1.523029027381373,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.9667152435937751,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -1.5075865827430146,
        "ttft_change_pct": 1.5296689227545013
      },
      "prefill4096": {
        "e2e_change_pct": 2.240279897585973,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 4.2379725753622255,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -2.1912743541844693,
        "ttft_change_pct": 2.238612787069827
      }
    },
    "plan": {
      "sha256": "0bbf15f30c2046796bfb5da6e1e2de48d25715cbf98c3f61658a78fd23011b5d"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "3665ec1903ec5402bcb4e75af63617b80cf96828dc7fd838b454fbafd153f3a3"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "e8709b1fa08813aa1b097fb7c1a5da333e4c42d269fa928303c3c2b732acf24b"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "d21cec598cd7bb58f16f531b33cdcbd3f8c83effe34bb4dcae22ac8f1a2a1c09"
      },
      {
        "sha256": "da0f73fd754788dcb3f4a30f4956da7076d9810c9cdbb93677efc1ce74b5fae9"
      },
      {
        "sha256": "7e7acd19fb427dad949fdcac8ce590415566f0c6666f473142feaacf51050810"
      },
      {
        "sha256": "818db237f38007aa9292e9185fe3880afd718a3c058cfaed03229f4f9cdbe537"
      },
      {
        "sha256": "cd26493eea40f14f0e61a8853caa16f7e0eb50d8d98fc8524fcb8b9433c2f976"
      }
    ],
    "results": {
      "sha256": "6924d1fa43aaa9766b9670f9d58a431e88292599fad2cd4595c6dd5c28c43d24"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "f734b356f3c833efaa8146f80325b15efe60b2c7b20277c2869180fc3943ad8f"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.12094202283677857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2856470069623529,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.11882657494497462,
        "ttft_change_pct": -0.28305017804981514
      },
      "prefill": {
        "e2e_change_pct": 0.0777428639953115,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5546811581639175,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.10236772686988971,
        "ttft_change_pct": 0.05896704382681861
      },
      "prefill2048": {
        "e2e_change_pct": -0.6585947020502081,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.1133234268202452,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.6722642854425809,
        "ttft_change_pct": -0.6546126659291995
      },
      "prefill4096": {
        "e2e_change_pct": -1.0945844952338857,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -1.5452301253211065,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.1063714542294933,
        "ttft_change_pct": -1.0952972692583884
      }
    },
    "numerical_results": [
      {
        "begin_ns": 419851260534344,
        "end_ns": 419852218338664,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      },
      {
        "begin_ns": 419896556077540,
        "end_ns": 419897212462880,
        "model": "omnicoder2",
        "passed": false,
        "reference": "existing CPU reference backend",
        "returncode": -6
      }
    ],
    "plan": {
      "sha256": "ba39820e1e798c12fa493e65535d58603adf8bf8b6e42b82256897aefc3820a2"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "6894fb362340e3a4d8f28f2612804633905a92c4ed130a2c5d3a5645d3f67363"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "2978e3df7b4a69f71e42ba70fb7cc7c14fdaa8dfae3a8db43654216da8427d23"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "3d0fbd23eb44f859a966295268fb6f4348af2fb9bb918c85e101ea8314bce760"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "8418b1f8e02a410dcc7164847ca321508051063de8d6464b3f37bffb7c1b442f"
      },
      {
        "sha256": "c5ab0ca6fa240685b494bed10a6db33e3d092e249b7b2663311b0d166a750420"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "0fae11a80cf5956eb7e2f552018ae8c6c914d4f5ea1abd31c72709b2f35a336a"
      },
      {
        "sha256": "7b0af48817cdd47263ca19d707b57ffa221c0421aa59ad06c9a5eac47f66a246"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "c4f6499ca9cb5cfb14f1707d5aecad276c5ab6a0867e6882673fd5c3bd8b2c3f"
      },
      {
        "sha256": "57b687c2591b91775455adf9ca1fbd042adb2eae6b41bf2ac795fed51280db91"
      }
    ],
    "results": {
      "sha256": "e950bd432e12a6880a36aa5abf80fa654f5eb655c9d9de54413c1292cf2e44b8"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "4a1a610e3bb140088015e839091e17b3d72a981ec4ac515fb3b03790f75e1900"
    },
    "arms": {
      "A": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 0,
          "O2_MMVQ_WARPS": 0
        }
      },
      "B": {
        "build": {
          "O2_FA_VOLTA_D256_ENABLED": 1,
          "O2_MMVQ_WARPS": 0
        }
      }
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.02890953625340753,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.36050347029360497,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.005611639230274079,
        "ttft_change_pct": 0.0011794624995342673
      },
      "prefill": {
        "e2e_change_pct": 0.32741308559378623,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.8231634235959517,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -0.2896480127901224,
        "ttft_change_pct": 0.32520613652560204
      },
      "prefill2048": {
        "e2e_change_pct": -0.5936452279304949,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9047104540210515,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 0.5924174957517181,
        "ttft_change_pct": -0.5883653398635391
      },
      "prefill4096": {
        "e2e_change_pct": -1.3222520400019477,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.6731597927917998,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": 1.3396620744484222,
        "ttft_change_pct": -1.3238337476255357
      }
    },
    "numerical_results": [
      {
        "begin_ns": 422121923689996,
        "end_ns": 422123735022939,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      },
      {
        "begin_ns": 422168251279398,
        "end_ns": 422169812063566,
        "model": "omnicoder2",
        "passed": true,
        "reference": "existing CPU reference backend",
        "returncode": 0
      }
    ],
    "plan": {
      "sha256": "ed2b2ef653fe0fdb46efccdd2128daf4c3b100c6e5136a8111922c5a7a203e91"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "843be0e25d5409335c4d0250ee0372ca59e12674b776014aead48a6685bd11ef"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "b82ac6982a30585dde08668a7e864c3d55f83217e4e21206c6c03147a537a487"
      },
      {
        "sha256": "1c435bee660746eb9e6b4005b6ae97e10356c31c725e024bbb6247f99d83dd02"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "c52d253cf8a5b51fdaf2d29a9c934ac01698e72fe31c0d0ef56491048c6705c8"
      },
      {
        "sha256": "27779e087021b6885aaf58cb9c9c8b3dbb2a04654ffd2fec9c892c3ec6a3944d"
      },
      {
        "sha256": "9f9676401d857d75c11a684a6155c465dcce89ff7e824d1cb5f2ea51a3c7bbce"
      },
      {
        "sha256": "64eedb2c1b91e366a6294be25247a86f2a28035ca8e41028f0ccd7fcd527f515"
      },
      {
        "sha256": "a54331d3739235898d166822b79f50683032b03808d9ff31700f8a5dd6360d4d"
      },
      {
        "sha256": "d76dddb4fefa5b209428834e2d1375ea2292612a45174a5f71c34fb2068436e1"
      },
      {
        "sha256": "f333a211f5fe4d3177e45f2c683dadb7620853649d85a8a3a22fd340e1de08ee"
      },
      {
        "sha256": "5aa351f971c18c4434c2cf360022de0790fa2039f04ee13e657fbd941a42d5a0"
      },
      {
        "sha256": "e37313b4dcb005c16007f502b412528e60916399a650cc5a240d188ecb79e1d1"
      },
      {
        "sha256": "b2c594f7a94812d074d99c1b5657f82af00ad3c40f01e6dde2951221b438506f"
      }
    ],
    "results": {
      "sha256": "9de95af06dcc3290e44fd619da2eadc3fa738a4cd2237a361f0bc2ad8a875dcb"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  },
  {
    "archive": {
      "sha256": "468d2dfd5258ff403340077a7d35623db3540eb7039c610fcfee6b3e5bcd0053"
    },
    "native_comparisons": {
      "decode": {
        "e2e_change_pct": -0.03503157045112726,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -0.2513145889854407,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.012265723416837737,
        "ttft_change_pct": -0.4501650513101474
      },
      "prefill": {
        "e2e_change_pct": -0.009999258488779805,
        "format_pass_change": 0,
        "gpu_energy_change_pct": -5.956983196393962,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -0.014861421090606175,
        "ttft_change_pct": 0.010265633072203961
      },
      "prefill2048": {
        "e2e_change_pct": -0.25711078793596576,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 0.9707387687063473,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.24877340370492718,
        "ttft_change_pct": -0.25277945019878123
      },
      "prefill4096": {
        "e2e_change_pct": -0.15154001546083817,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 1.3300460822200488,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": 0.14205097060184801,
        "ttft_change_pct": -0.1468214065870166
      }
    },
    "plan": {
      "sha256": "6a37c4abc88444a34b033036ab93edebe2760bfbb9285014197e8f6e316b2839"
    },
    "quality_arm_scores": {
      "A": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      },
      "B": {
        "format_passes": 16,
        "quality_attempts": 24,
        "quality_passes": 18
      }
    },
    "raw_members": [
      {
        "sha256": "0473cb2a053a4480fff31c9d11703fad0a6cac5a2ed46bf621d1410ad80bc415"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "fa019eb42d0beb6867e9117504d5968f70fab3094841da95a874e1871ce99489"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "19ab050677a7ccacefe87bc71037b8c557cc610f077890b487922fb7d0806f01"
      },
      {
        "sha256": "378c89a453961feeb78e84ede8aa1dc15bc886c30347644b76c6a7451cc19493"
      },
      {
        "sha256": "4629b0a9d0aa4a41e8efbab7800c3972e2289bc23999d5a58f572b64812483fd"
      },
      {
        "sha256": "421a74ada60ec4d4571db8edbf10d98bc801ebdcc855f5ba9db04bdf4c76ab4e"
      },
      {
        "sha256": "f40f8304c1599872baf81de85305d52fccb2b0ed5baddab4d38f297600882624"
      }
    ],
    "results": {
      "sha256": "a200c5c240a36583e62e17eedfe4f741c7b69bbe5af0b190bd9e0a65b937e682"
    },
    "runs": [
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      },
      {
        "CUDA_mapped": true,
        "requests": 34
      }
    ]
  }
]
```

## Decision and remaining research

Volta-D256-Pfad tatsächlich ausgeführt. Erster Numerik-Aufruf hatte0Fälle; später48/48 je Variante bestanden. Späterer Performancevergleich ist ganze Engine-Revision, kein isoliert qualifizierter Attention-Speedup. Vorhandene gültige Numerik/Dispatchbelege erhalten.

**Remaining scope:** Neue Attention-Einzelvariante nur bei konkretem SM70/D256-Quelldiff, gültiger Numerik und praktischer Hypothese. Bisherige Port-/Revisionsergebnisse nicht als isolierten Champion oder neue Achse zählen.

**Reopening condition:** Neue Attention-Einzelvariante nur bei konkretem SM70/D256-Quelldiff, gültiger Numerik und praktischer Hypothese. Bisherige Port-/Revisionsergebnisse nicht als isolierten Champion oder neue Achse zählen.

**Next action:** Neue Attention-Einzelvariante nur bei konkretem SM70/D256-Quelldiff, gültiger Numerik und praktischer Hypothese. Bisherige Port-/Revisionsergebnisse nicht als isolierten Champion oder neue Achse zählen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R374](../experiments/R374.md)
