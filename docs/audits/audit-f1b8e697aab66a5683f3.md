# Public audit excerpt

Original SHA256: `f1b8e697aab66a5683f3b5a93daedcdf7b09cd53ad76fc0ee779b065fd40f351`

Original file: `RESULTS.json`; 47426 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
    "omnicoder2": {
      "arms": {
        "A": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6663664275,
              "format_passes": 2,
              "gpu_energy_j": 180.56914849690963,
              "semantic_passes": 2,
              "tokens_per_s": 79.26311285609088,
              "ttft_s": 0.123861443
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659761472,
              "format_passes": 0,
              "gpu_energy_j": 463.8316299746367,
              "semantic_passes": 0,
              "tokens_per_s": 79.5447652588745,
              "ttft_s": 0.06295532849999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238255415,
              "format_passes": 2,
              "gpu_energy_j": 57.94942597610468,
              "semantic_passes": 2,
              "tokens_per_s": 78.14981677456413,
              "ttft_s": 0.07186822000000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24186823149999997,
              "format_passes": 0,
              "gpu_energy_j": 59.89431232133468,
              "semantic_passes": 0,
              "tokens_per_s": 77.59932461012522,
              "ttft_s": 0.125887519
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1824618465,
              "format_passes": 2,
              "gpu_energy_j": 38.448557289303025,
              "semantic_passes": 2,
              "tokens_per_s": 77.32757110182561,
              "ttft_s": 0.066052017
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358001348,
              "format_passes": 0,
              "gpu_energy_j": 89.35265178748494,
              "semantic_passes": 0,
              "tokens_per_s": 78.74114594653079,
              "ttft_s": 0.0785641125
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46960654150000003,
              "format_passes": 0,
              "gpu_energy_j": 118.45811043961598,
              "semantic_passes": 2,
              "tokens_per_s": 79.02384778951892,
              "ttft_s": 0.11517742349999999
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.663263351,
              "format_passes": 0,
              "gpu_energy_j": 465.04232086671766,
              "semantic_passes": 0,
              "tokens_per_s": 79.50104480919893,
              "ttft_s": 0.0655237195
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0840443535,
              "format_passes": 2,
              "gpu_energy_j": 287.13864214227465,
              "semantic_passes": 2,
              "tokens_per_s": 77.79566881166485,
              "ttft_s": 0.826939119
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23332381600000002,
              "format_passes": 0,
              "gpu_energy_j": 57.694988017334566,
              "semantic_passes": 0,
              "tokens_per_s": 78.26000062873527,
              "ttft_s": 0.06713717699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1990955795,
              "format_passes": 0,
              "gpu_energy_j": 47.99063581585001,
              "semantic_passes": 0,
              "tokens_per_s": 2550.80682130596,
              "ttft_s": 0.198913103
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.720049681,
              "format_passes": 0,
              "gpu_energy_j": 189.81297537422375,
              "semantic_passes": 0,
              "tokens_per_s": 2849.506398199157,
              "ttft_s": 0.7197071495
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.419833924,
              "format_passes": 0,
              "gpu_energy_j": 384.5152316310738,
              "semantic_passes": 0,
              "tokens_per_s": 2888.4547916800784,
              "ttft_s": 1.419449543
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29537060800000003,
              "format_passes": 2,
              "gpu_energy_j": 73.06045284386632,
              "semantic_passes": 2,
              "tokens_per_s": 78.56677183886768,
              "ttft_s": 0.0789534765
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3531962455,
              "format_passes": 2,
              "gpu_energy_j": 90.73219571312836,
              "semantic_passes": 2,
              "tokens_per_s": 78.8247687152619,
              "ttft_s": 0.074062846
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369348552,
              "format_passes": 2,
              "gpu_energy_j": 94.62802436962528,
              "semantic_passes": 2,
              "tokens_per_s": 78.76793681904832,
              "ttft_s": 0.077258294
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6195790175,
              "format_passes": 0,
              "gpu_energy_j": 164.9345277036163,
              "semantic_passes": 0,
              "tokens_per_s": 78.94189508957756,
              "ttft_s": 0.3182177215
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5601370880000001,
              "format_passes": 0,
              "gpu_energy_j": 146.9148390974853,
              "semantic_passes": 0,
              "tokens_per_s": 78.68271659959515,
              "ttft_s": 0.2551464095
            }
          }
        },
        "B": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.667456932,
              "format_passes": 2,
              "gpu_energy_j": 178.98124562423422,
              "semantic_passes": 2,
              "tokens_per_s": 79.10115990408809,
              "ttft_s": 0.12381650450000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658603599,
              "format_passes": 0,
              "gpu_energy_j": 464.2643638967511,
              "semantic_passes": 0,
              "tokens_per_s": 79.59779952442275,
              "ttft_s": 0.063057262
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23817954800000002,
              "format_passes": 2,
              "gpu_energy_j": 59.679200463861775,
              "semantic_passes": 2,
              "tokens_per_s": 78.22728665218615,
              "ttft_s": 0.0719958185
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2417529175,
              "format_passes": 0,
              "gpu_energy_j": 63.05494164321051,
              "semantic_passes": 0,
              "tokens_per_s": 77.70295078844089,
              "ttft_s": 0.1259069215
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1836609105,
              "format_passes": 2,
              "gpu_energy_j": 44.65610178260003,
              "semantic_passes": 2,
              "tokens_per_s": 76.80729634493792,
              "ttft_s": 0.0664638605
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3598223995,
              "format_passes": 0,
              "gpu_energy_j": 91.56909373512303,
              "semantic_passes": 0,
              "tokens_per_s": 78.40384143461668,
              "ttft_s": 0.0792025265
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4696632515,
              "format_passes": 0,
              "gpu_energy_j": 118.31151818297089,
              "semantic_passes": 2,
              "tokens_per_s": 79.12735309538334,
              "ttft_s": 0.115783473
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 12.936411647,
              "format_passes": 0,
              "gpu_energy_j": 3699.559275056547,
              "semantic_passes": 0,
              "tokens_per_s": 79.48320532691902,
              "ttft_s": 0.0656314115
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.084160068,
              "format_passes": 2,
              "gpu_energy_j": 289.18527186920454,
              "semantic_passes": 2,
              "tokens_per_s": 77.80819112910184,
              "ttft_s": 0.8270650945
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23464702399999998,
              "format_passes": 0,
              "gpu_energy_j": 58.16620409309689,
              "semantic_passes": 0,
              "tokens_per_s": 77.90126566213404,
              "ttft_s": 0.067779596
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19980633949999999,
              "format_passes": 0,
              "gpu_energy_j": 47.786240991992955,
              "semantic_passes": 0,
              "tokens_per_s": 2541.284002489917,
              "ttft_s": 0.19961135000000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721996938,
              "format_passes": 0,
              "gpu_energy_j": 190.76053857033773,
              "semantic_passes": 0,
              "tokens_per_s": 2841.5784045823157,
              "ttft_s": 0.7217365435
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.419026546,
              "format_passes": 0,
              "gpu_energy_j": 384.30098364919127,
              "semantic_passes": 0,
              "tokens_per_s": 2889.958487416276,
              "ttft_s": 1.418672381
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.296311942,
              "format_passes": 2,
              "gpu_energy_j": 72.18318637217294,
              "semantic_passes": 2,
              "tokens_per_s": 78.49943986944768,
              "ttft_s": 0.079717759
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353540558,
              "format_passes": 2,
              "gpu_energy_j": 91.30867654638942,
              "semantic_passes": 2,
              "tokens_per_s": 78.68031657939687,
              "ttft_s": 0.0738767495
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369200026,
              "format_passes": 2,
              "gpu_energy_j": 93.07353559011601,
              "semantic_passes": 2,
              "tokens_per_s": 78.83315699290347,
              "ttft_s": 0.077442877
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6203688304999999,
              "format_passes": 0,
              "gpu_energy_j": 164.4227600810843,
              "semantic_passes": 0,
              "tokens_per_s": 78.98516112444551,
              "ttft_s": 0.31941881949999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5616356650000001,
              "format_passes": 0,
              "gpu_energy_j": 146.8294325829739,
              "semantic_passes": 0,
              "tokens_per_s": 78.77802557112638,
              "ttft_s": 0.2568840685
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.16364937592838746,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8793876949043655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.20432322951640103,
            "ttft_change_pct": -0.03628126631787243
          },
          "decode": {
            "e2e_change_pct": -0.06976140966837852,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.09329547494163482,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.06667222585376997,
            "ttft_change_pct": 0.16191401495111446
          },
          "energy": {
            "e2e_change_pct": -0.03184271803433614,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.984972600885416,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.09912995425886972,
            "ttft_change_pct": 0.1775450957321567
          },
          "filtering": {
            "e2e_change_pct": -0.04767637290967741,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.2770107867988525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1335400518449159,
            "ttft_change_pct": 0.015412568421480088
          },
          "german": {
            "e2e_change_pct": 0.6571587556525094,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 16.14506481111593,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6728192150282197,
            "ttft_change_pct": 0.6235138890611003
          },
          "ha_sim": {
            "e2e_change_pct": 0.5086716880183362,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4805553089903176,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4283713525621735,
            "ttft_change_pct": 0.8126025734714215
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.012076066874788793,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.12375029122199122,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.13097983553029824,
            "ttft_change_pct": 0.5261877558843109
          },
          "length-decode": {
            "e2e_change_pct": 677.7729028432132,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 695.5317417480484,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 0.1643557490658143
          },
          "long_context": {
            "e2e_change_pct": 0.010674332616233961,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7127670841028166,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.016096419798516948,
            "ttft_change_pct": 0.015233950977244781
          },
          "math": {
            "e2e_change_pct": 0.5671122745566359,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8167365865831222,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4583886579595964,
            "ttft_change_pct": 0.956875204925578
          },
          "prefill": {
            "e2e_change_pct": 0.35699436511094085,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4259056384278037,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3733257546789659,
            "ttft_change_pct": 0.3510311736477201
          },
          "prefill2048": {
            "e2e_change_pct": 0.2704337008101465,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.49920886295882205,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.27822340114245225,
            "ttft_change_pct": 0.2819749673752536
          },
          "prefill4096": {
            "e2e_change_pct": -0.056864256188882134,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.055718984388131165,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.052058828842627136,
            "ttft_change_pct": -0.05475094228130084
          },
          "pve_sim": {
            "e2e_change_pct": 0.31869589407487187,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2007405341000754,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.08570031305102921,
            "ttft_change_pct": 0.9680162722156993
          },
          "sorting": {
            "e2e_change_pct": 0.09748475653035271,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6353652402326215,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1832572911020236,
            "ttft_change_pct": -0.25126836200703995
          },
          "time": {
            "e2e_change_pct": -0.04021296393222906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6427361660191764,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0828004090102974,
            "ttft_change_pct": 0.23891674335960733
          },
          "tool-call": {
            "e2e_change_pct": 0.1274757500967061,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3102853172451847,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0548074439039814,
            "ttft_change_pct": 0.37744535230102016
          },
          "tool-final": {
            "e2e_change_pct": 0.26753754252386575,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.05813334788783431,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12113075863438016,
            "ttft_change_pct": 0.6810438772801852
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
