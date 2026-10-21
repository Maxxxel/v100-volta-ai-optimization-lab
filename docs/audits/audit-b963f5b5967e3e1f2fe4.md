# Public audit excerpt

Original SHA256: `b963f5b5967e3e1f2fe4505aa7a908b47433928c5d43f774e48c7bc21adc7e4e`

Original file: `RESULTS.json`; 46091 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 0.6674967015,
              "format_passes": 2,
              "gpu_energy_j": 180.59540303047135,
              "semantic_passes": 2,
              "tokens_per_s": 79.05899275399211,
              "ttft_s": 0.1236148735
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 4.2216542455,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 79.46273317472146,
              "ttft_s": 2.6218979195000003
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.8984440840000001,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 78.45272874621017,
              "ttft_s": 0.755186463
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6584059660000001,
              "format_passes": 0,
              "gpu_energy_j": 459.47556048801425,
              "semantic_passes": 0,
              "tokens_per_s": 79.6238800522483,
              "ttft_s": 0.0630855465
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2376028795,
              "format_passes": 2,
              "gpu_energy_j": 56.15928301589451,
              "semantic_passes": 2,
              "tokens_per_s": 78.37653813842508,
              "ttft_s": 0.071706246
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2414567495,
              "format_passes": 0,
              "gpu_energy_j": 60.52042962820801,
              "semantic_passes": 0,
              "tokens_per_s": 77.47401378282456,
              "ttft_s": 0.125266002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18289029,
              "format_passes": 2,
              "gpu_energy_j": 42.86187148586161,
              "semantic_passes": 2,
              "tokens_per_s": 77.4352142152645,
              "ttft_s": 0.0666176765
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35780545750000003,
              "format_passes": 0,
              "gpu_energy_j": 89.00291075934646,
              "semantic_passes": 0,
              "tokens_per_s": 78.80617013765027,
              "ttft_s": 0.07863497850000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469450126,
              "format_passes": 0,
              "gpu_energy_j": 120.54705518948944,
              "semantic_passes": 2,
              "tokens_per_s": 79.08498812732294,
              "ttft_s": 0.11534574950000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0819856625,
              "format_passes": 2,
              "gpu_energy_j": 288.09259760501425,
              "semantic_passes": 2,
              "tokens_per_s": 77.75628421905236,
              "ttft_s": 0.824799413
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233266784,
              "format_passes": 0,
              "gpu_energy_j": 54.646955706429196,
              "semantic_passes": 0,
              "tokens_per_s": 78.31690341654772,
              "ttft_s": 0.0672056435
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198903848,
              "format_passes": 0,
              "gpu_energy_j": 48.31681380218724,
              "semantic_passes": 0,
              "tokens_per_s": 2553.071521144598,
              "ttft_s": 0.19876759100000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7195901865000001,
              "format_passes": 0,
              "gpu_energy_j": 190.50350547285166,
              "semantic_passes": 0,
              "tokens_per_s": 2851.240051823501,
              "ttft_s": 0.7193405595
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4212190305,
              "format_passes": 0,
              "gpu_energy_j": 383.8310381469465,
              "semantic_passes": 0,
              "tokens_per_s": 2885.707755485794,
              "ttft_s": 1.4208495499999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294832179,
              "format_passes": 2,
              "gpu_energy_j": 71.89549946727583,
              "semantic_passes": 2,
              "tokens_per_s": 78.68788688973778,
              "ttft_s": 0.07871306950000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3531698995,
              "format_passes": 2,
              "gpu_energy_j": 87.09884424764097,
              "semantic_passes": 2,
              "tokens_per_s": 78.69228322228855,
              "ttft_s": 0.0735748825
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3687121495,
              "format_passes": 2,
              "gpu_energy_j": 95.55439979556618,
              "semantic_passes": 2,
              "tokens_per_s": 78.932223056189,
              "ttft_s": 0.07727530399999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620425353,
              "format_passes": 0,
              "gpu_energy_j": 164.02878769079172,
              "semantic_passes": 0,
              "tokens_per_s": 78.92928794761139,
              "ttft_s": 0.319391907
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560263144,
              "format_passes": 0,
              "gpu_energy_j": 146.0385627545241,
              "semantic_passes": 0,
              "tokens_per_s": 78.8521756603836,
              "ttft_s": 0.2558784115
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
              "e2e_s": 0.6671095225,
              "format_passes": 2,
              "gpu_energy_j": 180.51545841188414,
              "semantic_passes": 2,
              "tokens_per_s": 79.1856311869939,
              "ttft_s": 0.1240881435
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 3.1619058745,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 65.95859169933223,
              "ttft_s": 1.2354000294999998
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.870313502,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 55.578214896329264,
              "ttft_s": 0.4106171795
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6865353365,
              "format_passes": 0,
              "gpu_energy_j": 469.2676281276673,
              "semantic_passes": 0,
              "tokens_per_s": 78.45145485377807,
              "ttft_s": 0.067306225
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2379221425,
              "format_passes": 2,
              "gpu_energy_j": 60.474648324579604,
              "semantic_passes": 2,
              "tokens_per_s": 78.14801831098083,
              "ttft_s": 0.0715012095
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24554871550000001,
              "format_passes": 0,
              "gpu_energy_j": 64.5059089258378,
              "semantic_passes": 0,
              "tokens_per_s": 77.07164701111749,
              "ttft_s": 0.12873809749999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.180914781,
              "format_passes": 2,
              "gpu_energy_j": 41.022710103509766,
              "semantic_passes": 2,
              "tokens_per_s": 77.0187344835206,
              "ttft_s": 0.06402484650000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3574618075,
              "format_passes": 0,
              "gpu_energy_j": 91.40357039112462,
              "semantic_passes": 0,
              "tokens_per_s": 78.89532311703005,
              "ttft_s": 0.07852165750000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46939449850000003,
              "format_passes": 0,
              "gpu_energy_j": 119.74451536747745,
              "semantic_passes": 2,
              "tokens_per_s": 79.01596874664247,
              "ttft_s": 0.1149836365
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0837971265,
              "format_passes": 2,
              "gpu_energy_j": 291.1733359566499,
              "semantic_passes": 2,
              "tokens_per_s": 77.89093376371366,
              "ttft_s": 0.8269479805
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23673073849999998,
              "format_passes": 0,
              "gpu_energy_j": 56.99107808336153,
              "semantic_passes": 0,
              "tokens_per_s": 78.03734849848124,
              "ttft_s": 0.070101894
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2128096415,
              "format_passes": 0,
              "gpu_energy_j": 51.60908053707308,
              "semantic_passes": 0,
              "tokens_per_s": 2384.8373160984584,
              "ttft_s": 0.212671313
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7274019025,
              "format_passes": 0,
              "gpu_energy_j": 192.06541994366637,
              "semantic_passes": 0,
              "tokens_per_s": 2820.4144494024463,
              "ttft_s": 0.7271546579999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4394411004999998,
              "format_passes": 0,
              "gpu_energy_j": 386.995412911289,
              "semantic_passes": 0,
              "tokens_per_s": 2849.235815944612,
              "ttft_s": 1.439081409
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295365348,
              "format_passes": 2,
              "gpu_energy_j": 74.65737535390744,
              "semantic_passes": 2,
              "tokens_per_s": 78.60526911873956,
              "ttft_s": 0.07907341300000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3563796335,
              "format_passes": 2,
              "gpu_energy_j": 88.78096052951426,
              "semantic_passes": 2,
              "tokens_per_s": 78.10547221908625,
              "ttft_s": 0.0747219695
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36914711899999997,
              "format_passes": 2,
              "gpu_energy_j": 96.8359181216903,
              "semantic_passes": 2,
              "tokens_per_s": 78.7893867331666,
              "ttft_s": 0.0772234825
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6213589775,
              "format_passes": 0,
              "gpu_energy_j": 165.02890235213778,
              "semantic_passes": 0,
              "tokens_per_s": 78.92160340071035,
              "ttft_s": 0.319982528
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5617467654999999,
              "format_passes": 0,
              "gpu_energy_j": 147.92431792611964,
              "semantic_passes": 0,
              "tokens_per_s": 78.79755597401932,
              "ttft_s": 0.25714266350000003
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.05800463120340105,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04426725002170118,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.16018219887501406,
            "ttft_change_pct": 0.38285845918046846
          },
          "concurrent-decode": {
            "e2e_change_pct": -25.102680356393957,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -16.994307816843566,
            "ttft_change_pct": -52.88145963609474
          },
          "concurrent-quality": {
            "e2e_change_pct": -3.1310331383961887,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -29.157065936965143,
            "ttft_change_pct": -45.62704714424947
          },
          "decode": {
            "e2e_change_pct": 1.6961691574136406,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1311400391465396,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4724542407389518,
            "ttft_change_pct": 6.690404909149827
          },
          "energy": {
            "e2e_change_pct": 0.134368321070788,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.684153138963223,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.29156662551316215,
            "ttft_change_pct": -0.2859395261048836
          },
          "filtering": {
            "e2e_change_pct": 1.694699364782104,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.58534534885753,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5193570747928256,
            "ttft_change_pct": 2.7717780120419144
          },
          "german": {
            "e2e_change_pct": -1.0801606799355046,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.290903123440404,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5378428095854537,
            "ttft_change_pct": -3.892105123180012
          },
          "ha_sim": {
            "e2e_change_pct": -0.09604381174092014,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.69728215773668,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.11312944052992435,
            "ttft_change_pct": -0.14411016847928337
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.011849501559191289,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6657481767186058,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.08727241707282563,
            "ttft_change_pct": -0.31393701247743877
          },
          "long_context": {
            "e2e_change_pct": 0.16742033307672877,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0693569974538075,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.17316869757044717,
            "ttft_change_pct": 0.26049576007638464
          },
          "math": {
            "e2e_change_pct": 1.4849754605439136,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.2895754148232434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3569534875243918,
            "ttft_change_pct": 4.309534659838499
          },
          "prefill": {
            "e2e_change_pct": 6.991213915579952,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.813915231175294,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.589482654630707,
            "ttft_change_pct": 6.994964284695682
          },
          "prefill2048": {
            "e2e_change_pct": 1.0855784509784971,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8198875222468205,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.081129679044046,
            "ttft_change_pct": 1.086286376710266
          },
          "prefill4096": {
            "e2e_change_pct": 1.2821436815118492,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8244186764101658,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2638819531135215,
            "ttft_change_pct": 1.283166046679618
          },
          "pve_sim": {
            "e2e_change_pct": 0.1808381302910611,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.8415142910144473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.104994268195302,
            "ttft_change_pct": 0.4577937339872218
          },
          "sorting": {
            "e2e_change_pct": 0.9088356636690165,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.931272792886518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7457033640067223,
            "ttft_change_pct": 1.5590741854055956
          },
          "time": {
            "e2e_change_pct": 0.11796993958290702,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3411400509718563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.18096072490030313,
            "ttft_change_pct": -0.067060881442782
          },
          "tool-call": {
            "e2e_change_pct": 0.15048135855273426,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6097189861765884,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.009735989137682477,
            "ttft_change_pct": 0.18492046512625926
          },
          "tool-final": {
            "e2e_change_pct": 0.2648079774456802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2912720695322788,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.0692684582344616,
            "ttft_change_pct": 0.49408310477963013
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 60.540375811286104,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 76.26481069861362,
            "exact_serial_matches": 24,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 16,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 18,
            "request_e2e_s": 4.2216542455,
            "wave_elapsed_s": 6.713453185500001,
            "waves": 6
          },
          "B": {
            "active_slots_max": 2,
            "aggregate_tokens_per_s": 122.43581370732024,
            "exact_serial_matches": 8,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 15,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 17,
            "request_e2e_s": 3.1619058745,
            "wave_elapsed_s": 4.181783812,
            "waves": 6
          }
        },
        "change_exercised": true,
        "note": "Aggregate four-request wall-clock throughput; per-request native throughput and correctness are reported separately. Two starts per arm give preliminary results."
      }
    }
  }
}
```
