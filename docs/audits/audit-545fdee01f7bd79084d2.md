# Public audit excerpt

Original SHA256: `545fdee01f7bd79084d23d2769e1fdb58103b63f36007ec371aa938cbd14c71a`

Original file: `RESULTS.json`; 40703 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6356473205,
              "format_passes": 2,
              "gpu_energy_j": 149.42625261524762,
              "semantic_passes": 2,
              "tokens_per_s": 83.67944505287029,
              "ttft_s": 0.1337109745
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.56399011,
              "format_passes": 0,
              "gpu_energy_j": 370.3979092774653,
              "semantic_passes": 0,
              "tokens_per_s": 84.42614067884594,
              "ttft_s": 0.059569084499999994
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.226348267,
              "format_passes": 2,
              "gpu_energy_j": 46.01651903380355,
              "semantic_passes": 2,
              "tokens_per_s": 82.84641011198465,
              "ttft_s": 0.069390809
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.245078662,
              "format_passes": 0,
              "gpu_energy_j": 53.95305020575549,
              "semantic_passes": 0,
              "tokens_per_s": 81.94671827300272,
              "ttft_s": 0.135223752
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.17227028300000002,
              "format_passes": 2,
              "gpu_energy_j": 34.65251949555941,
              "semantic_passes": 2,
              "tokens_per_s": 81.95892448722502,
              "ttft_s": 0.06239941
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3420152245,
              "format_passes": 0,
              "gpu_energy_j": 73.41483792525199,
              "semantic_passes": 0,
              "tokens_per_s": 83.72490000437718,
              "ttft_s": 0.0792198525
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.442520037,
              "format_passes": 0,
              "gpu_energy_j": 98.47359736411534,
              "semantic_passes": 2,
              "tokens_per_s": 83.9420452789015,
              "ttft_s": 0.1088983205
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0604187995,
              "format_passes": 2,
              "gpu_energy_j": 280.10594399669384,
              "semantic_passes": 2,
              "tokens_per_s": 82.19700838871051,
              "ttft_s": 0.877868625
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.16247505550000002,
              "format_passes": 0,
              "gpu_energy_j": 30.75786555863023,
              "semantic_passes": 0,
              "tokens_per_s": 81.9727891702853,
              "ttft_s": 0.06484006
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.207890505,
              "format_passes": 0,
              "gpu_energy_j": 50.879721472402345,
              "semantic_passes": 0,
              "tokens_per_s": 2442.014297106969,
              "ttft_s": 0.2077070805
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7578978155,
              "format_passes": 0,
              "gpu_energy_j": 198.74590283433707,
              "semantic_passes": 0,
              "tokens_per_s": 2707.370649723151,
              "ttft_s": 0.7575756825
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.502380772,
              "format_passes": 0,
              "gpu_energy_j": 406.85700077740177,
              "semantic_passes": 0,
              "tokens_per_s": 2729.708252642851,
              "ttft_s": 1.5020232595
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2824409155,
              "format_passes": 2,
              "gpu_energy_j": 59.276329950765714,
              "semantic_passes": 2,
              "tokens_per_s": 83.12806269086659,
              "ttft_s": 0.07789367950000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3345910635,
              "format_passes": 2,
              "gpu_energy_j": 69.7790724174377,
              "semantic_passes": 2,
              "tokens_per_s": 83.56599776865173,
              "ttft_s": 0.0712539885
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3512269805,
              "format_passes": 0,
              "gpu_energy_j": 78.77777260162098,
              "semantic_passes": 0,
              "tokens_per_s": 83.73456260001038,
              "ttft_s": 0.0764792105
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.602468367,
              "format_passes": 0,
              "gpu_energy_j": 141.80510262918662,
              "semantic_passes": 0,
              "tokens_per_s": 83.89660138838008,
              "ttft_s": 0.3192515
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5623685555,
              "format_passes": 0,
              "gpu_energy_j": 137.20112180521022,
              "semantic_passes": 0,
              "tokens_per_s": 83.64411102417077,
              "ttft_s": 0.275209783
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.575865563,
              "format_passes": 2,
              "gpu_energy_j": 143.87388113589714,
              "semantic_passes": 2,
              "tokens_per_s": 94.73544000027589,
              "ttft_s": 0.132464236
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3939640045,
              "format_passes": 0,
              "gpu_energy_j": 359.0496070195652,
              "semantic_passes": 0,
              "tokens_per_s": 95.04871618197643,
              "ttft_s": 0.0578440715
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2080221635,
              "format_passes": 2,
              "gpu_energy_j": 46.2201053102289,
              "semantic_passes": 2,
              "tokens_per_s": 93.18746476748575,
              "ttft_s": 0.06847585149999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.231662382,
              "format_passes": 0,
              "gpu_energy_j": 53.163039693340785,
              "semantic_passes": 0,
              "tokens_per_s": 92.03585864261233,
              "ttft_s": 0.13385869150000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.158588444,
              "format_passes": 2,
              "gpu_energy_j": 32.270210169663294,
              "semantic_passes": 2,
              "tokens_per_s": 92.2197603323778,
              "ttft_s": 0.060941839
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3111152275,
              "format_passes": 0,
              "gpu_energy_j": 71.05166770911983,
              "semantic_passes": 0,
              "tokens_per_s": 94.15701917310761,
              "ttft_s": 0.077475856
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.40554699699999996,
              "format_passes": 0,
              "gpu_energy_j": 93.8974862936814,
              "semantic_passes": 2,
              "tokens_per_s": 93.92583680011523,
              "ttft_s": 0.10738162849999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.035322018,
              "format_passes": 2,
              "gpu_energy_j": 277.9267667152132,
              "semantic_passes": 2,
              "tokens_per_s": 92.10752904549031,
              "ttft_s": 0.8724102174999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1509630325,
              "format_passes": 0,
              "gpu_energy_j": 30.373690313486655,
              "semantic_passes": 0,
              "tokens_per_s": 91.41873362895622,
              "ttft_s": 0.063409554
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205881402,
              "format_passes": 0,
              "gpu_energy_j": 50.34254587960252,
              "semantic_passes": 0,
              "tokens_per_s": 2465.9771161288263,
              "ttft_s": 0.2057071715
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7580192219999999,
              "format_passes": 0,
              "gpu_energy_j": 200.0024784822141,
              "semantic_passes": 0,
              "tokens_per_s": 2706.51910484544,
              "ttft_s": 0.7577548924999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4999787585,
              "format_passes": 0,
              "gpu_energy_j": 406.98400553130864,
              "semantic_passes": 0,
              "tokens_per_s": 2734.1426734841107,
              "ttft_s": 1.499649853
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2590967715,
              "format_passes": 2,
              "gpu_energy_j": 58.80450374294337,
              "semantic_passes": 2,
              "tokens_per_s": 93.46162699975231,
              "ttft_s": 0.0771611605
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30443773350000003,
              "format_passes": 2,
              "gpu_energy_j": 70.3682822049565,
              "semantic_passes": 2,
              "tokens_per_s": 93.88465282162494,
              "ttft_s": 0.070013295
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3202532605,
              "format_passes": 0,
              "gpu_energy_j": 72.68334410328579,
              "semantic_passes": 0,
              "tokens_per_s": 93.90726545655237,
              "ttft_s": 0.0752328535
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.558228747,
              "format_passes": 0,
              "gpu_energy_j": 140.33594310105423,
              "semantic_passes": 0,
              "tokens_per_s": 94.23552989790944,
              "ttft_s": 0.3059259265
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5297251119999999,
              "format_passes": 0,
              "gpu_energy_j": 129.7905227723488,
              "semantic_passes": 0,
              "tokens_per_s": 93.98128296202583,
              "ttft_s": 0.27440787850000004
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
            "e2e_change_pct": -9.404862660787373,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.7157938328595375,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 13.21231867685093,
            "ttft_change_pct": -0.9324129935198266
          },
          "decode": {
            "e2e_change_pct": -10.871303112012654,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.063813799607351,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.582092960447389,
            "ttft_change_pct": -2.8958192231408164
          },
          "energy": {
            "e2e_change_pct": -8.096418736883903,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44241998460552434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.482200063373838,
            "ttft_change_pct": -1.3185571881717206
          },
          "filtering": {
            "e2e_change_pct": -5.474275030928643,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4642555136399449,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.311829664731633,
            "ttft_change_pct": -1.009482786722249
          },
          "german": {
            "e2e_change_pct": -7.942077276322824,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.874851700758445,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.51948571720478,
            "ttft_change_pct": -2.3358730475176004
          },
          "ha_sim": {
            "e2e_change_pct": -9.034684653343561,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.218927239937852,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.459995972745318,
            "ttft_change_pct": -2.2014639575351325
          },
          "jarvis_memory": {
            "e2e_change_pct": -8.355110934784637,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.647043667464834,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.893671982904518,
            "ttft_change_pct": -1.3927597717175222
          },
          "long_context": {
            "e2e_change_pct": -2.3666858331664375,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7779832339103621,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.057033280229422,
            "ttft_change_pct": -0.6217795401903148
          },
          "math": {
            "e2e_change_pct": -7.085409489212335,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2490309004415945,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.523268336091984,
            "ttft_change_pct": -2.20620708864242
          },
          "prefill": {
            "e2e_change_pct": -0.9664236469097087,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0557754194688296,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.9812726751946554,
            "ttft_change_pct": -0.9628506621852995
          },
          "prefill2048": {
            "e2e_change_pct": 0.016018848123988683,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6322523533601743,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03145283700989321,
            "ttft_change_pct": 0.02365572234428459
          },
          "prefill4096": {
            "e2e_change_pct": -0.15988047402939465,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03121606698770485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.16245035845738887,
            "ttft_change_pct": -0.15801396449680594
          },
          "pve_sim": {
            "e2e_change_pct": -8.265142448881491,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7959774301382061,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.430897550582621,
            "ttft_change_pct": -0.9404087786095694
          },
          "sorting": {
            "e2e_change_pct": -9.01199502598191,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8443932644933705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.347911026611435,
            "ttft_change_pct": -1.7412267384863678
          },
          "time": {
            "e2e_change_pct": -8.818718868324515,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -7.736228503380904,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.148750218157488,
            "ttft_change_pct": -1.629667712116356
          },
          "tool-call": {
            "e2e_change_pct": -7.343061050705746,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.036041370086782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.323417562134221,
            "ttft_change_pct": -4.174004977267143
          },
          "tool-final": {
            "e2e_change_pct": -5.80463526645384,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.401267085397842,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.358517307773065,
            "ttft_change_pct": -0.29137935841472284
          }
        }
      },
      "complete": true
    }
  }
}
```
