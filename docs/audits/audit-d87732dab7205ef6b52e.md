# Public audit excerpt

Original SHA256: `d87732dab7205ef6b52e79b4d94e5e22f3fff642900c5e994adc87100bf99bed`

Original file: `RESULTS.json`; 48197 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.672281729,
              "format_passes": 2,
              "gpu_energy_j": 178.3793674807863,
              "semantic_passes": 2,
              "tokens_per_s": 78.52181653662655,
              "ttft_s": 0.1247325485
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.44231725099999997,
              "format_passes": 0,
              "gpu_energy_j": 90.21401591711547,
              "semantic_passes": 0,
              "tokens_per_s": 335.6596683818386,
              "ttft_s": 0.0630173515
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2392803725,
              "format_passes": 2,
              "gpu_energy_j": 55.088882834641694,
              "semantic_passes": 2,
              "tokens_per_s": 77.69357715853243,
              "ttft_s": 0.07193806450000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24303965,
              "format_passes": 0,
              "gpu_energy_j": 58.73144800670188,
              "semantic_passes": 0,
              "tokens_per_s": 76.8801241991812,
              "ttft_s": 0.125907216
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1863856795,
              "format_passes": 2,
              "gpu_energy_j": 42.30430720351036,
              "semantic_passes": 2,
              "tokens_per_s": 75.47560957891511,
              "ttft_s": 0.0671843375
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3609723465,
              "format_passes": 0,
              "gpu_energy_j": 91.14033019369387,
              "semantic_passes": 0,
              "tokens_per_s": 78.03080813316994,
              "ttft_s": 0.07899711200000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.475074787,
              "format_passes": 0,
              "gpu_energy_j": 120.3243147872873,
              "semantic_passes": 2,
              "tokens_per_s": 77.94984826834532,
              "ttft_s": 0.1158051045
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0847633575,
              "format_passes": 2,
              "gpu_energy_j": 288.74615462380075,
              "semantic_passes": 2,
              "tokens_per_s": 77.09817816969766,
              "ttft_s": 0.825308453
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2373048495,
              "format_passes": 0,
              "gpu_energy_j": 56.423352106099635,
              "semantic_passes": 0,
              "tokens_per_s": 76.75254230633882,
              "ttft_s": 0.0679187875
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1997245345,
              "format_passes": 0,
              "gpu_energy_j": 48.51050775593755,
              "semantic_passes": 0,
              "tokens_per_s": 2546.035392536062,
              "ttft_s": 0.1995387965
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7176381345,
              "format_passes": 0,
              "gpu_energy_j": 188.0262102351441,
              "semantic_passes": 0,
              "tokens_per_s": 2859.915872125486,
              "ttft_s": 0.7173519465
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.419814074,
              "format_passes": 0,
              "gpu_energy_j": 381.75769604735365,
              "semantic_passes": 0,
              "tokens_per_s": 2888.8456131671337,
              "ttft_s": 1.419399571
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29701907,
              "format_passes": 2,
              "gpu_energy_j": 73.09477087402584,
              "semantic_passes": 2,
              "tokens_per_s": 77.95502088881328,
              "ttft_s": 0.078976347
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3560281045,
              "format_passes": 2,
              "gpu_energy_j": 88.78949603685561,
              "semantic_passes": 2,
              "tokens_per_s": 78.02401158528814,
              "ttft_s": 0.07402674249999999
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.865776727,
              "format_passes": 0,
              "gpu_energy_j": 194.005085119952,
              "semantic_passes": 0,
              "tokens_per_s": 462.62488592849365
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.92870465,
              "format_passes": 0,
              "gpu_energy_j": 211.89318161556469,
              "semantic_passes": 0,
              "tokens_per_s": 462.02700013009456
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.754683703,
              "format_passes": 0,
              "gpu_energy_j": 166.22286660410282,
              "semantic_passes": 0,
              "tokens_per_s": 460.7937038713431
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.373723547,
              "format_passes": 2,
              "gpu_energy_j": 97.53636869401807,
              "semantic_passes": 2,
              "tokens_per_s": 77.8453355391959,
              "ttft_s": 0.0783268715
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.41203829150000004,
              "format_passes": 0,
              "gpu_energy_j": 91.11234018177996,
              "semantic_passes": 0,
              "tokens_per_s": 158.2789779637517,
              "ttft_s": 0.411322411
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.3886770055,
              "format_passes": 0,
              "gpu_energy_j": 91.57663705224007,
              "semantic_passes": 0,
              "tokens_per_s": 181.55447424773683,
              "ttft_s": 0.25654039250000005
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
              "e2e_s": 0.671446256,
              "format_passes": 2,
              "gpu_energy_j": 178.53267834497825,
              "semantic_passes": 2,
              "tokens_per_s": 78.55251470252045,
              "ttft_s": 0.124064372
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.45587453899999997,
              "format_passes": 0,
              "gpu_energy_j": 91.32652568158707,
              "semantic_passes": 0,
              "tokens_per_s": 323.51664975579934,
              "ttft_s": 0.063392452
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.239642743,
              "format_passes": 2,
              "gpu_energy_j": 58.51685220344777,
              "semantic_passes": 2,
              "tokens_per_s": 77.49238064619382,
              "ttft_s": 0.071869853
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24284550049999998,
              "format_passes": 0,
              "gpu_energy_j": 58.15711044634669,
              "semantic_passes": 0,
              "tokens_per_s": 76.8283441705808,
              "ttft_s": 0.1256868975
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.183943904,
              "format_passes": 2,
              "gpu_energy_j": 43.1114619661178,
              "semantic_passes": 2,
              "tokens_per_s": 76.6762940379835,
              "ttft_s": 0.0665344145
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.363630636,
              "format_passes": 0,
              "gpu_energy_j": 92.1449252183645,
              "semantic_passes": 0,
              "tokens_per_s": 77.39468111378947,
              "ttft_s": 0.079366156
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47624589549999996,
              "format_passes": 0,
              "gpu_energy_j": 118.43668976714591,
              "semantic_passes": 2,
              "tokens_per_s": 77.63857714959187,
              "ttft_s": 0.11560118
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0843845955,
              "format_passes": 2,
              "gpu_energy_j": 288.5582373419721,
              "semantic_passes": 2,
              "tokens_per_s": 77.34574260787696,
              "ttft_s": 0.8258029445
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.235647373,
              "format_passes": 0,
              "gpu_energy_j": 57.7042903546828,
              "semantic_passes": 0,
              "tokens_per_s": 77.41662235000183,
              "ttft_s": 0.067747207
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199435195,
              "format_passes": 0,
              "gpu_energy_j": 48.40671957201586,
              "semantic_passes": 0,
              "tokens_per_s": 2549.342967744136,
              "ttft_s": 0.199201864
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.719905039,
              "format_passes": 0,
              "gpu_energy_j": 187.81572960380228,
              "semantic_passes": 0,
              "tokens_per_s": 2850.1467173142737,
              "ttft_s": 0.7196328015
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.419135942,
              "format_passes": 0,
              "gpu_energy_j": 385.8110499490729,
              "semantic_passes": 0,
              "tokens_per_s": 2890.0521598767355,
              "ttft_s": 1.418795328
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29723423849999997,
              "format_passes": 2,
              "gpu_energy_j": 72.46828668672816,
              "semantic_passes": 2,
              "tokens_per_s": 77.93122761040166,
              "ttft_s": 0.079076582
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35590005599999996,
              "format_passes": 2,
              "gpu_energy_j": 91.74431706009929,
              "semantic_passes": 2,
              "tokens_per_s": 78.01643966738531,
              "ttft_s": 0.0739006655
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8500325725,
              "format_passes": 0,
              "gpu_energy_j": 178.32536484379443,
              "semantic_passes": 0,
              "tokens_per_s": 476.6368526022376
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9132584804999999,
              "format_passes": 0,
              "gpu_energy_j": 191.82440884978917,
              "semantic_passes": 0,
              "tokens_per_s": 474.9631166452334
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.736607581,
              "format_passes": 0,
              "gpu_energy_j": 147.60989749855918,
              "semantic_passes": 0,
              "tokens_per_s": 475.88459956476106
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.372687098,
              "format_passes": 2,
              "gpu_energy_j": 95.26151531755731,
              "semantic_passes": 2,
              "tokens_per_s": 78.02157035430768,
              "ttft_s": 0.07789204999999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2739244845,
              "format_passes": 0,
              "gpu_energy_j": 59.7557406070049,
              "semantic_passes": 0,
              "tokens_per_s": 463.7101652789046,
              "ttft_s": 0.27324303149999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.3899725275,
              "format_passes": 0,
              "gpu_energy_j": 92.48794922149821,
              "semantic_passes": 0,
              "tokens_per_s": 182.02677998776107,
              "ttft_s": 0.257528344
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.12427423860571496,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.08594652305202732,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.03909507860098138,
            "ttft_change_pct": -0.5356873631103487
          },
          "decode": {
            "e2e_change_pct": 3.065059743735832,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2331894918564679,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -3.6176579344723847,
            "ttft_change_pct": 0.5952336794097235
          },
          "energy": {
            "e2e_change_pct": 0.15144179867907503,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.222615512272567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.25896157661536856,
            "ttft_change_pct": -0.09481975985051738
          },
          "filtering": {
            "e2e_change_pct": -0.07988387902961858,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9779046487831344,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.06735164535666138,
            "ttft_change_pct": -0.17498480786040105
          },
          "german": {
            "e2e_change_pct": -1.3100660450686696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9079730078654045,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.590824460732554,
            "ttft_change_pct": -0.967372789826193
          },
          "ha_sim": {
            "e2e_change_pct": 0.7364246945160469,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1022508065700931,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8152254661964231,
            "ttft_change_pct": 0.4671613817983422
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.24651034574898478,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5687810260780588,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3993222894827064,
            "ttft_change_pct": -0.1760928422632757
          },
          "long_context": {
            "e2e_change_pct": -0.03491655552164685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.06508044481960962,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3211028380390335,
            "ttft_change_pct": 0.059915962111212195
          },
          "math": {
            "e2e_change_pct": -0.6984587561073008,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2702271325079293,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.8652222111581676,
            "ttft_change_pct": -0.25262597628085137
          },
          "prefill": {
            "e2e_change_pct": -0.14486928244661357,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.213949902243582,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12991081026487716,
            "ttft_change_pct": -0.1688556340470826
          },
          "prefill2048": {
            "e2e_change_pct": 0.3158840634325255,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.11194217608204715,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3415888875064055,
            "ttft_change_pct": 0.3179548074175198
          },
          "prefill4096": {
            "e2e_change_pct": -0.04776202831188181,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0617608875176376,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.04176570406193569,
            "ttft_change_pct": -0.042570324265645
          },
          "pve_sim": {
            "e2e_change_pct": 0.07244265494468216,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8570848226303163,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03052180365079593,
            "ttft_change_pct": 0.12691774665141153
          },
          "sorting": {
            "e2e_change_pct": -0.03596584044393003,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3278948018999444,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.009704599582838203,
            "ttft_change_pct": -0.17031277581880389
          },
          "spec-branch": {
            "e2e_change_pct": -1.8185005451180292,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.082118191109744,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 3.0287965693029495
          },
          "spec-code": {
            "e2e_change_pct": -1.6631950211512425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.471174396817572,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.7998615906638324
          },
          "spec-repeat": {
            "e2e_change_pct": -2.395191777448513,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -11.197598432636003,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 3.2749787088305116
          },
          "time": {
            "e2e_change_pct": -0.27733039791576486,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.3323129689164612,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.22639097627505933,
            "ttft_change_pct": -0.5551370706795233
          },
          "tool-call": {
            "e2e_change_pct": -33.51965335483875,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -34.41531576536714,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 192.97015386661224,
            "ttft_change_pct": -33.56962222513084
          },
          "tool-final": {
            "e2e_change_pct": 0.33331583337001813,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9951360943056597,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.2601454698272887,
            "ttft_change_pct": 0.38510563204972037
          }
        }
      },
      "complete": true,
      "speculation": {
        "arms": {
          "A": {
            "acceptance_pct": 91.03221083455344,
            "accepted_n": 4974,
            "checkpoint_events": 90,
            "draft_n": 5464,
            "median_e2e_s": 0.896064203,
            "restore_events": 20,
            "starts": 2
          },
          "B": {
            "acceptance_pct": 99.45291129347402,
            "accepted_n": 5090,
            "checkpoint_events": 166,
            "draft_n": 5118,
            "median_e2e_s": 0.8790314405,
            "restore_events": 2,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Token drift is reported separately from semantic quality and protocol validity. No draft is inactivity, not an optimization gain. Internal RAM checkpoint trace is not a new model checkpoint."
      }
    }
  }
}
```
