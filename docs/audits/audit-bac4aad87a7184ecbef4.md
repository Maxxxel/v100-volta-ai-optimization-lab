# Public audit excerpt

Original SHA256: `bac4aad87a7184ecbef4830e4077ed6c659a031b8ecd06f8e1e1775e107c8802`

Original file: `RESULTS.json`; 39807 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

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
              "e2e_s": 1.7641045435,
              "format_passes": 2,
              "gpu_energy_j": 475.7104048948868,
              "semantic_passes": 2,
              "tokens_per_s": 35.38364258413024,
              "ttft_s": 0.5205821985000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.780518435,
              "format_passes": 0,
              "gpu_energy_j": 1067.8285603475906,
              "semantic_passes": 0,
              "tokens_per_s": 35.408714424426854,
              "ttft_s": 0.1940693715
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.58142145,
              "format_passes": 2,
              "gpu_energy_j": 146.1643814480276,
              "semantic_passes": 2,
              "tokens_per_s": 35.01209023376761,
              "ttft_s": 0.2100746255
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9258942800000001,
              "format_passes": 0,
              "gpu_energy_j": 246.01037351083485,
              "semantic_passes": 0,
              "tokens_per_s": 34.93122123372242,
              "ttft_s": 0.525083882
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.467794309,
              "format_passes": 2,
              "gpu_energy_j": 108.23917694742401,
              "semantic_passes": 2,
              "tokens_per_s": 34.202490928859035,
              "ttft_s": 0.20463288400000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989576083,
              "format_passes": 0,
              "gpu_energy_j": 260.60466430498707,
              "semantic_passes": 0,
              "tokens_per_s": 35.24486372096394,
              "ttft_s": 0.22340011850000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.146218219,
              "format_passes": 0,
              "gpu_energy_j": 293.3337618606913,
              "semantic_passes": 2,
              "tokens_per_s": 35.26860484403935,
              "ttft_s": 0.35229000450000003
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7935590725,
              "format_passes": 2,
              "gpu_energy_j": 1016.6482152311535,
              "semantic_passes": 2,
              "tokens_per_s": 34.38370400192071,
              "ttft_s": 3.2118825475
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574639153,
              "format_passes": 2,
              "gpu_energy_j": 142.11665625587688,
              "semantic_passes": 2,
              "tokens_per_s": 34.78530355671796,
              "ttft_s": 0.200906958
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7248183365,
              "format_passes": 0,
              "gpu_energy_j": 188.4069916988704,
              "semantic_passes": 0,
              "tokens_per_s": 697.6931760035301,
              "ttft_s": 0.7246924825
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7507154629999997,
              "format_passes": 0,
              "gpu_energy_j": 736.5903596065757,
              "semantic_passes": 0,
              "tokens_per_s": 745.0468554678662,
              "ttft_s": 2.7504627299999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.46559766,
              "format_passes": 0,
              "gpu_energy_j": 1472.7983558368965,
              "semantic_passes": 0,
              "tokens_per_s": 749.6582664586708,
              "ttft_s": 5.465178788999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846573174,
              "format_passes": 0,
              "gpu_energy_j": 227.2682252674792,
              "semantic_passes": 2,
              "tokens_per_s": 35.22182778547082,
              "ttft_s": 0.2219296095
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9853152485000001,
              "format_passes": 0,
              "gpu_energy_j": 261.59335813656435,
              "semantic_passes": 2,
              "tokens_per_s": 35.11760758884869,
              "ttft_s": 0.2164655885
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015109029,
              "format_passes": 0,
              "gpu_energy_j": 275.47168096494465,
              "semantic_passes": 2,
              "tokens_per_s": 35.277027118125105,
              "ttft_s": 0.2213450045
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.705128068,
              "format_passes": 0,
              "gpu_energy_j": 461.8891594774169,
              "semantic_passes": 0,
              "tokens_per_s": 35.06395318525797,
              "ttft_s": 1.0281194089999999
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7779234535000001,
              "format_passes": 0,
              "gpu_energy_j": 468.9009276039268,
              "semantic_passes": 0,
              "tokens_per_s": 35.05918688991774,
              "ttft_s": 1.093032835
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
              "e2e_s": 1.7642107765000001,
              "format_passes": 2,
              "gpu_energy_j": 480.6373552196459,
              "semantic_passes": 2,
              "tokens_per_s": 35.365772693816695,
              "ttft_s": 0.520048751
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.785630126,
              "format_passes": 0,
              "gpu_energy_j": 1070.4558965112835,
              "semantic_passes": 0,
              "tokens_per_s": 35.373469406023446,
              "ttft_s": 0.194908258
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581841425,
              "format_passes": 2,
              "gpu_energy_j": 149.1394023492777,
              "semantic_passes": 2,
              "tokens_per_s": 34.972091850808226,
              "ttft_s": 0.2100641495
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9245854099999999,
              "format_passes": 0,
              "gpu_energy_j": 245.78346062303063,
              "semantic_passes": 0,
              "tokens_per_s": 35.005302691767184,
              "ttft_s": 0.524559292
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4657667915,
              "format_passes": 2,
              "gpu_energy_j": 109.87028200709769,
              "semantic_passes": 2,
              "tokens_per_s": 34.12967743272996,
              "ttft_s": 0.202022076
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989789818,
              "format_passes": 0,
              "gpu_energy_j": 265.50637526895434,
              "semantic_passes": 0,
              "tokens_per_s": 35.283725204184485,
              "ttft_s": 0.224590187
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1494206065,
              "format_passes": 0,
              "gpu_energy_j": 295.9702444882301,
              "semantic_passes": 2,
              "tokens_per_s": 35.23178141050524,
              "ttft_s": 0.354555925
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7978753535000003,
              "format_passes": 2,
              "gpu_energy_j": 1021.7312694695166,
              "semantic_passes": 2,
              "tokens_per_s": 34.45463035695278,
              "ttft_s": 3.217336091
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5731108300000001,
              "format_passes": 2,
              "gpu_energy_j": 142.9977246042256,
              "semantic_passes": 2,
              "tokens_per_s": 34.97731269868339,
              "ttft_s": 0.201458368
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.72799766,
              "format_passes": 0,
              "gpu_energy_j": 186.47779513300634,
              "semantic_passes": 0,
              "tokens_per_s": 694.6816893872298,
              "ttft_s": 0.7278343015
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7508171675,
              "format_passes": 0,
              "gpu_energy_j": 736.2557137498668,
              "semantic_passes": 0,
              "tokens_per_s": 744.8480086744805,
              "ttft_s": 2.7505886664999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4744221930000005,
              "format_passes": 0,
              "gpu_energy_j": 1480.5889494224027,
              "semantic_passes": 0,
              "tokens_per_s": 748.4345574616511,
              "ttft_s": 5.4741045325
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.85426611,
              "format_passes": 0,
              "gpu_energy_j": 223.89170041605573,
              "semantic_passes": 2,
              "tokens_per_s": 34.9994370430329,
              "ttft_s": 0.22565259
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9857894185,
              "format_passes": 0,
              "gpu_energy_j": 262.37599345567685,
              "semantic_passes": 2,
              "tokens_per_s": 35.057822050065845,
              "ttft_s": 0.21560516950000003
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0181790035,
              "format_passes": 0,
              "gpu_energy_j": 273.7085813342004,
              "semantic_passes": 2,
              "tokens_per_s": 35.08218199448564,
              "ttft_s": 0.2200189545
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.707458098,
              "format_passes": 0,
              "gpu_energy_j": 467.57255427085056,
              "semantic_passes": 0,
              "tokens_per_s": 35.03858400629923,
              "ttft_s": 1.02910072
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7801853959999998,
              "format_passes": 0,
              "gpu_energy_j": 468.4092209117108,
              "semantic_passes": 0,
              "tokens_per_s": 35.04619166315161,
              "ttft_s": 1.095530266
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
            "e2e_change_pct": 0.006021922022236836,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0357037126080382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05050325237447861,
            "ttft_change_pct": -0.10247132951091142
          },
          "decode": {
            "e2e_change_pct": 0.13521137610852385,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2460447548656708,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09953769566707349,
            "ttft_change_pct": 0.43226115152332767
          },
          "energy": {
            "e2e_change_pct": 0.0722324571960753,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0353938981419573,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11424163108321173,
            "ttft_change_pct": -0.004986799321948787
          },
          "filtering": {
            "e2e_change_pct": -0.14136279144095765,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09223712177902632,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21207806491818637,
            "ttft_change_pct": -0.09990594226619853
          },
          "german": {
            "e2e_change_pct": -0.43342072808330023,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.506945179808561,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2128894538135362,
            "ttft_change_pct": -1.2758496821068221
          },
          "ha_sim": {
            "e2e_change_pct": 0.021598642456277517,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8808991684932996,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11026140866428058,
            "ttft_change_pct": 0.5327071928119764
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.2793872446726464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8987995827056894,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10440853472074574,
            "ttft_change_pct": 0.6431974995191769
          },
          "long_context": {
            "e2e_change_pct": 0.11377919567114869,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.49998162217865794,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20627898328842154,
            "ttft_change_pct": 0.16979274364328223
          },
          "math": {
            "e2e_change_pct": -0.2659622115933291,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6199613553828476,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5519835169825571,
            "ttft_change_pct": 0.2744603798142231
          },
          "prefill": {
            "e2e_change_pct": 0.4386372888070422,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0239516848437824,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4316348102400114,
            "ttft_change_pct": 0.4335382353024553
          },
          "prefill2048": {
            "e2e_change_pct": 0.003697383512335506,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.045431745385271505,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.026689166181470547,
            "ttft_change_pct": 0.0045787386473650216
          },
          "prefill4096": {
            "e2e_change_pct": 0.16145595685870262,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5289653912656123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1632355770317062,
            "ttft_change_pct": 0.1633202470515016
          },
          "pve_sim": {
            "e2e_change_pct": 0.9087148324877115,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4857003646020273,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6314003458095963,
            "ttft_change_pct": 1.677550151323981
          },
          "sorting": {
            "e2e_change_pct": 0.04812368434587988,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2991801185961096,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1702437691166403,
            "ttft_change_pct": -0.39748534903966126
          },
          "time": {
            "e2e_change_pct": 0.3024280557354819,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6400293578520788,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5523286386549198,
            "ttft_change_pct": -0.5990873853220391
          },
          "tool-call": {
            "e2e_change_pct": 0.13664838692926118,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2304672402062566,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07235116595297741,
            "ttft_change_pct": 0.09544718166099031
          },
          "tool-final": {
            "e2e_change_pct": 0.12722384057348712,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1048636637868472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.037066537814844924,
            "ttft_change_pct": 0.2284863656451641
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
