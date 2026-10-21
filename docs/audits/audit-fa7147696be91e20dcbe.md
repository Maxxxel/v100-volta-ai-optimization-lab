# Public audit excerpt

Original SHA256: `fa7147696be91e20dcbeb0b079b956d4e033ab4e1b5642a858741e63a68283dd`

Original file: `RESULTS.json`; 39915 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen38": {
      "arms": {
        "A": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.763311099,
              "format_passes": 2,
              "gpu_energy_j": 479.9991121521691,
              "semantic_passes": 2,
              "tokens_per_s": 35.38682689209039,
              "ttft_s": 0.5198731155
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.784197056,
              "format_passes": 0,
              "gpu_energy_j": 1068.33278256571,
              "semantic_passes": 0,
              "tokens_per_s": 35.377657048938964,
              "ttft_s": 0.193955857
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.578829261,
              "format_passes": 2,
              "gpu_energy_j": 150.70001029696428,
              "semantic_passes": 2,
              "tokens_per_s": 35.016234308715326,
              "ttft_s": 0.207527097
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9232061060000001,
              "format_passes": 0,
              "gpu_energy_j": 242.72815681273732,
              "semantic_passes": 0,
              "tokens_per_s": 35.0671231581892,
              "ttft_s": 0.5239308935
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465152727,
              "format_passes": 2,
              "gpu_energy_j": 108.51464611348763,
              "semantic_passes": 2,
              "tokens_per_s": 34.28370194470385,
              "ttft_s": 0.2025404795
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.991104745,
              "format_passes": 0,
              "gpu_energy_j": 263.5167673640632,
              "semantic_passes": 0,
              "tokens_per_s": 35.22165496779827,
              "ttft_s": 0.22447537950000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1451542190000001,
              "format_passes": 0,
              "gpu_energy_j": 299.92234908946455,
              "semantic_passes": 2,
              "tokens_per_s": 35.2628314450524,
              "ttft_s": 0.35115493
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7951825594999997,
              "format_passes": 2,
              "gpu_energy_j": 1020.1963904170376,
              "semantic_passes": 2,
              "tokens_per_s": 34.44732965716409,
              "ttft_s": 3.214539171
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5743410915,
              "format_passes": 2,
              "gpu_energy_j": 144.83783215132786,
              "semantic_passes": 2,
              "tokens_per_s": 35.02330969978824,
              "ttft_s": 0.20309143699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.722908571,
              "format_passes": 0,
              "gpu_energy_j": 189.66620168702104,
              "semantic_passes": 0,
              "tokens_per_s": 699.5705853451128,
              "ttft_s": 0.722781892
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7484650000000004,
              "format_passes": 0,
              "gpu_energy_j": 732.2346727631461,
              "semantic_passes": 0,
              "tokens_per_s": 745.485868208925,
              "ttft_s": 2.748200592
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4695742535,
              "format_passes": 0,
              "gpu_energy_j": 1472.318108140495,
              "semantic_passes": 0,
              "tokens_per_s": 749.1073472838077,
              "ttft_s": 5.4692016205
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.845889806,
              "format_passes": 0,
              "gpu_energy_j": 224.69536613809254,
              "semantic_passes": 2,
              "tokens_per_s": 35.24659678332748,
              "ttft_s": 0.2216892975
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.985310599,
              "format_passes": 0,
              "gpu_energy_j": 257.0179328939744,
              "semantic_passes": 2,
              "tokens_per_s": 35.07722585905297,
              "ttft_s": 0.21553483750000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0133300900000002,
              "format_passes": 0,
              "gpu_energy_j": 269.8437880814413,
              "semantic_passes": 2,
              "tokens_per_s": 35.28573006327413,
              "ttft_s": 0.2197897605
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7079988265,
              "format_passes": 0,
              "gpu_energy_j": 459.6276907009119,
              "semantic_passes": 0,
              "tokens_per_s": 35.017815356811454,
              "ttft_s": 1.029425192
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.777648852,
              "format_passes": 0,
              "gpu_energy_j": 467.72245592641707,
              "semantic_passes": 0,
              "tokens_per_s": 35.12175628234223,
              "ttft_s": 1.0933153610000002
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.765958666,
              "format_passes": 2,
              "gpu_energy_j": 489.03540272786563,
              "semantic_passes": 2,
              "tokens_per_s": 35.362896960002864,
              "ttft_s": 0.521664946
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7860337735,
              "format_passes": 0,
              "gpu_energy_j": 1069.900431621126,
              "semantic_passes": 0,
              "tokens_per_s": 35.354036734787556,
              "ttft_s": 0.19408475549999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581040864,
              "format_passes": 2,
              "gpu_energy_j": 152.72162893491577,
              "semantic_passes": 2,
              "tokens_per_s": 34.98952028363793,
              "ttft_s": 0.209437715
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0090760025,
              "format_passes": 0,
              "gpu_energy_j": 270.59588978923887,
              "semantic_passes": 0,
              "tokens_per_s": 35.06272935428919,
              "ttft_s": 0.5241653735
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.464692261,
              "format_passes": 2,
              "gpu_energy_j": 110.49711562458191,
              "semantic_passes": 2,
              "tokens_per_s": 34.254327789803156,
              "ttft_s": 0.2019217575
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.988762444,
              "format_passes": 0,
              "gpu_energy_j": 265.9241843672347,
              "semantic_passes": 0,
              "tokens_per_s": 35.25126623938056,
              "ttft_s": 0.22277095600000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1453770104999998,
              "format_passes": 0,
              "gpu_energy_j": 299.96690757503075,
              "semantic_passes": 2,
              "tokens_per_s": 35.28452276329988,
              "ttft_s": 0.351763874
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.796737145,
              "format_passes": 2,
              "gpu_energy_j": 1027.7042035403877,
              "semantic_passes": 2,
              "tokens_per_s": 34.3918959733158,
              "ttft_s": 3.2150818755
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5728797595,
              "format_passes": 2,
              "gpu_energy_j": 147.44614212012772,
              "semantic_passes": 2,
              "tokens_per_s": 34.899305684574486,
              "ttft_s": 0.2002855785
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7269031914999999,
              "format_passes": 0,
              "gpu_energy_j": 188.66595458158102,
              "semantic_passes": 0,
              "tokens_per_s": 695.7149620960423,
              "ttft_s": 0.726776447
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7566516735000004,
              "format_passes": 0,
              "gpu_energy_j": 739.7521519495735,
              "semantic_passes": 0,
              "tokens_per_s": 743.2719447009208,
              "ttft_s": 2.7564016110000003
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.480681427,
              "format_passes": 0,
              "gpu_energy_j": 1476.2987814754783,
              "semantic_passes": 0,
              "tokens_per_s": 747.5877878522431,
              "ttft_s": 5.480364893
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8470784650000001,
              "format_passes": 0,
              "gpu_energy_j": 225.2667024741367,
              "semantic_passes": 2,
              "tokens_per_s": 35.11196265606469,
              "ttft_s": 0.22052825799999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986721061,
              "format_passes": 0,
              "gpu_energy_j": 260.1096128184287,
              "semantic_passes": 2,
              "tokens_per_s": 35.02817874430256,
              "ttft_s": 0.215855992
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0173823395000001,
              "format_passes": 0,
              "gpu_energy_j": 277.3569553735417,
              "semantic_passes": 2,
              "tokens_per_s": 35.234403048990536,
              "ttft_s": 0.2227009965
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7101471634999998,
              "format_passes": 0,
              "gpu_energy_j": 462.5688927150466,
              "semantic_passes": 0,
              "tokens_per_s": 34.958166351040866,
              "ttft_s": 1.029168425
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.780158875,
              "format_passes": 0,
              "gpu_energy_j": 467.6024544510723,
              "semantic_passes": 0,
              "tokens_per_s": 35.04240519036756,
              "ttft_s": 1.0949369395000002
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.15014746980843707,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8825640187500658,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06762384251206566,
            "ttft_change_pct": 0.34466689016543484
          },
          "decode": {
            "e2e_change_pct": 0.04853651839000772,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.14673789674890525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06676619121139815,
            "ttft_change_pct": 0.06645764762853723
          },
          "energy": {
            "e2e_change_pct": 0.38208210071812854,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3414854013398925,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0762903995954467,
            "ttft_change_pct": 0.9206595319935618
          },
          "filtering": {
            "e2e_change_pct": 9.301270425089658,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.481046674779162,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.012529695921126294,
            "ttft_change_pct": 0.04475399387764423
          },
          "german": {
            "e2e_change_pct": -0.09899243265104607,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8269142296432062,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0856796472798349,
            "ttft_change_pct": -0.30548066318764056
          },
          "ha_sim": {
            "e2e_change_pct": -0.2363323363969938,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9135726076381134,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08407121019544661,
            "ttft_change_pct": -0.7592919561140499
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.01945515252907981,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.01485667396960988,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.061513262998413865,
            "ttft_change_pct": 0.17341177582215206
          },
          "long_context": {
            "e2e_change_pct": 0.04096207430412946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7359184166767063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1609230219003721,
            "ttft_change_pct": 0.016882808736506938
          },
          "math": {
            "e2e_change_pct": -0.2544362612438955,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8008485283559583,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.354061384479909,
            "ttft_change_pct": -1.3815740050133085
          },
          "prefill": {
            "e2e_change_pct": 0.5525761707976695,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5273723502359107,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5511414187273855,
            "ttft_change_pct": 0.5526639563349756
          },
          "prefill2048": {
            "e2e_change_pct": 0.2978634801607427,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0266488963244003,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2969772603903631,
            "ttft_change_pct": 0.29841413410192086
          },
          "prefill4096": {
            "e2e_change_pct": 0.20307199400195763,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.270367749535505,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20284935624705902,
            "ttft_change_pct": 0.20411155548110127
          },
          "pve_sim": {
            "e2e_change_pct": 0.14052173126675171,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2542715258725181,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.38197766465351,
            "ttft_change_pct": -0.5237237490005597
          },
          "sorting": {
            "e2e_change_pct": 0.14314897266218818,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.202904361436019,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13982609385216893,
            "ttft_change_pct": 0.14900352245839077
          },
          "time": {
            "e2e_change_pct": 0.3998943226880769,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.784265424643717,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14546110904196663,
            "ttft_change_pct": 1.324554880708373
          },
          "tool-call": {
            "e2e_change_pct": 0.12578094122008832,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6399096646352076,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17033902647208832,
            "ttft_change_pct": -0.024942754655254973
          },
          "tool-final": {
            "e2e_change_pct": 0.1411990336098068,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.02565655632400521,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.22593144641392948,
            "ttft_change_pct": 0.14831754476740677
          }
        }
      },
      "complete": true
    }
  }
}
```
