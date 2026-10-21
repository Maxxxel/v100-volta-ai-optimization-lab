# Public audit excerpt

Original SHA256: `a5a921e0333f3c3df73b7431f51a0e3b85cb2b0174d76b538798c876685ef409`

Original file: `RESULTS.json`; 40867 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666581651,
              "format_passes": 2,
              "gpu_energy_j": 178.83791995477876,
              "semantic_passes": 2,
              "tokens_per_s": 79.23780949814747,
              "ttft_s": 0.123939194
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6597235205,
              "format_passes": 0,
              "gpu_energy_j": 458.1410618325147,
              "semantic_passes": 0,
              "tokens_per_s": 79.55372243142187,
              "ttft_s": 0.063411994
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23813659999999998,
              "format_passes": 2,
              "gpu_energy_j": 56.17208625916696,
              "semantic_passes": 2,
              "tokens_per_s": 78.119381424486,
              "ttft_s": 0.0717181815
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24181743449999998,
              "format_passes": 0,
              "gpu_energy_j": 59.82663558307334,
              "semantic_passes": 0,
              "tokens_per_s": 77.37740942922139,
              "ttft_s": 0.1254781475
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182266896,
              "format_passes": 2,
              "gpu_energy_j": 42.7414222862723,
              "semantic_passes": 2,
              "tokens_per_s": 77.71685258336058,
              "ttft_s": 0.06641032
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358275204,
              "format_passes": 0,
              "gpu_energy_j": 90.88679727679522,
              "semantic_passes": 0,
              "tokens_per_s": 78.7143149931251,
              "ttft_s": 0.0787591175
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4690135265,
              "format_passes": 0,
              "gpu_energy_j": 119.40534969415077,
              "semantic_passes": 2,
              "tokens_per_s": 79.10330750846566,
              "ttft_s": 0.114982946
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.08132829,
              "format_passes": 2,
              "gpu_energy_j": 290.494603388241,
              "semantic_passes": 2,
              "tokens_per_s": 77.95616897774454,
              "ttft_s": 0.8247677314999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2337105455,
              "format_passes": 0,
              "gpu_energy_j": 58.02904215231345,
              "semantic_passes": 0,
              "tokens_per_s": 78.17812021858762,
              "ttft_s": 0.067389483
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199159356,
              "format_passes": 0,
              "gpu_energy_j": 49.04064747341578,
              "semantic_passes": 0,
              "tokens_per_s": 2549.169691225801,
              "ttft_s": 0.1990235195
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7183704120000001,
              "format_passes": 0,
              "gpu_energy_j": 188.7747944504398,
              "semantic_passes": 0,
              "tokens_per_s": 2856.4353620996662,
              "ttft_s": 0.71810836
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.422037622,
              "format_passes": 0,
              "gpu_energy_j": 381.85629260811055,
              "semantic_passes": 0,
              "tokens_per_s": 2884.0973368653604,
              "ttft_s": 1.4217115045000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29528491599999995,
              "format_passes": 2,
              "gpu_energy_j": 71.30603880064913,
              "semantic_passes": 2,
              "tokens_per_s": 78.57767003727798,
              "ttft_s": 0.07887228800000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353032656,
              "format_passes": 2,
              "gpu_energy_j": 89.44332371873341,
              "semantic_passes": 2,
              "tokens_per_s": 78.83863524066467,
              "ttft_s": 0.07398447150000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3699704535,
              "format_passes": 2,
              "gpu_energy_j": 92.77823162448999,
              "semantic_passes": 2,
              "tokens_per_s": 78.71570144421943,
              "ttft_s": 0.0777279255
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6210106375,
              "format_passes": 0,
              "gpu_energy_j": 163.10555863600973,
              "semantic_passes": 0,
              "tokens_per_s": 78.95303518927258,
              "ttft_s": 0.319389576
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560662701,
              "format_passes": 0,
              "gpu_energy_j": 147.96630124799782,
              "semantic_passes": 0,
              "tokens_per_s": 78.72997457793679,
              "ttft_s": 0.255888508
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
              "e2e_s": 0.7516492775,
              "format_passes": 2,
              "gpu_energy_j": 184.69997975581356,
              "semantic_passes": 2,
              "tokens_per_s": 75.47257830263275,
              "ttft_s": 0.1818790435
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8596741314999998,
              "format_passes": 0,
              "gpu_energy_j": 469.34863089874375,
              "semantic_passes": 0,
              "tokens_per_s": 73.06747790189905,
              "ttft_s": 0.1220701545
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2972464205,
              "format_passes": 2,
              "gpu_energy_j": 63.04642785398128,
              "semantic_passes": 2,
              "tokens_per_s": 77.19533758661748,
              "ttft_s": 0.1288360895
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3009620535,
              "format_passes": 0,
              "gpu_energy_j": 66.48096221339999,
              "semantic_passes": 0,
              "tokens_per_s": 77.58286363782261,
              "ttft_s": 0.18487497
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23981591600000002,
              "format_passes": 2,
              "gpu_energy_j": 46.65706556804298,
              "semantic_passes": 2,
              "tokens_per_s": 77.37936253571948,
              "ttft_s": 0.12348759249999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4247013505,
              "format_passes": 0,
              "gpu_energy_j": 95.30541187122807,
              "semantic_passes": 0,
              "tokens_per_s": 76.40450373544218,
              "ttft_s": 0.13677499999999998
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5370382389999999,
              "format_passes": 0,
              "gpu_energy_j": 123.50766678980428,
              "semantic_passes": 2,
              "tokens_per_s": 76.97225336783899,
              "ttft_s": 0.173215999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1419394735,
              "format_passes": 2,
              "gpu_energy_j": 292.8471141621993,
              "semantic_passes": 2,
              "tokens_per_s": 76.67522163511182,
              "ttft_s": 0.88100626
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.293639435,
              "format_passes": 0,
              "gpu_energy_j": 62.82797531886385,
              "semantic_passes": 0,
              "tokens_per_s": 77.37588663995784,
              "ttft_s": 0.125567645
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.256490071,
              "format_passes": 0,
              "gpu_energy_j": 52.27797630444478,
              "semantic_passes": 0,
              "tokens_per_s": 2552.697478951525,
              "ttft_s": 0.256338336
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7770803534999999,
              "format_passes": 0,
              "gpu_energy_j": 195.3850052250314,
              "semantic_passes": 0,
              "tokens_per_s": 2855.5378039415004,
              "ttft_s": 0.7768098320000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4765916209999999,
              "format_passes": 0,
              "gpu_energy_j": 387.677786215099,
              "semantic_passes": 0,
              "tokens_per_s": 2891.8056100028302,
              "ttft_s": 1.4762659605000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35484355300000003,
              "format_passes": 2,
              "gpu_energy_j": 73.59753860533941,
              "semantic_passes": 2,
              "tokens_per_s": 78.10815457170638,
              "ttft_s": 0.1371612825
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.42837401750000004,
              "format_passes": 2,
              "gpu_energy_j": 95.40499193038568,
              "semantic_passes": 2,
              "tokens_per_s": 74.34995890866247,
              "ttft_s": 0.1324088005
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4311793445,
              "format_passes": 2,
              "gpu_energy_j": 95.67641221198396,
              "semantic_passes": 2,
              "tokens_per_s": 78.05309512713751,
              "ttft_s": 0.1364511955
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.705258122,
              "format_passes": 0,
              "gpu_energy_j": 167.9165004795464,
              "semantic_passes": 0,
              "tokens_per_s": 74.13731211341153,
              "ttft_s": 0.38349899750000005
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6405222795000001,
              "format_passes": 0,
              "gpu_energy_j": 152.092574892895,
              "semantic_passes": 0,
              "tokens_per_s": 73.98936668876702,
              "ttft_s": 0.316032891
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
            "e2e_change_pct": 12.76177140075523,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2778617658475895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -4.751811312505739,
            "ttft_change_pct": 46.74860924139945
          },
          "decode": {
            "e2e_change_pct": 12.047224042457593,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.446314028565788,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -8.153288534190462,
            "ttft_change_pct": 92.50325813756936
          },
          "energy": {
            "e2e_change_pct": 24.82181256472127,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.238002987992047,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.1828611812060186,
            "ttft_change_pct": 79.64215880180954
          },
          "filtering": {
            "e2e_change_pct": 24.45837667672386,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.122682339518608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.2655222113492339,
            "ttft_change_pct": 47.33638779613001
          },
          "german": {
            "e2e_change_pct": 31.574038546198757,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.161237676052526,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4342559386062317,
            "ttft_change_pct": 85.94638980809006
          },
          "ha_sim": {
            "e2e_change_pct": 18.54053692758486,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.861668280571041,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.93442337379759,
            "ttft_change_pct": 73.66243343191343
          },
          "jarvis_memory": {
            "e2e_change_pct": 14.50378478583174,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.435622529611382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.694013951816876,
            "ttft_change_pct": 50.644947816870165
          },
          "long_context": {
            "e2e_change_pct": 5.6052527304173205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8098294242024906,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.643163535907477,
            "ttft_change_pct": 6.818711056714055
          },
          "math": {
            "e2e_change_pct": 25.642355748983526,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.269881749821506,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0261612537967424,
            "ttft_change_pct": 86.331218774894
          },
          "prefill": {
            "e2e_change_pct": 28.786352874127587,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.601317474007473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1383896779357796,
            "ttft_change_pct": 28.79801173448748
          },
          "prefill2048": {
            "e2e_change_pct": 8.172655849862576,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5016384437526193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03142231643239457,
            "ttft_change_pct": 8.174458796162742
          },
          "prefill4096": {
            "e2e_change_pct": 3.8363259984129927,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5245247281973962,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.267268134086196,
            "ttft_change_pct": 3.837238133568177
          },
          "pve_sim": {
            "e2e_change_pct": 20.169888054830444,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2136125400215265,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5975176730855791,
            "ttft_change_pct": 73.90300950823183
          },
          "sorting": {
            "e2e_change_pct": 21.34118762656336,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.665302633877435,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -5.693498268076258,
            "ttft_change_pct": 78.96836703091132
          },
          "time": {
            "e2e_change_pct": 16.54426466247527,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.123772178827511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.841771469890884,
            "ttft_change_pct": 75.54977136241723
          },
          "tool-call": {
            "e2e_change_pct": 13.566190240984422,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9495879133542457,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.099478081262388,
            "ttft_change_pct": 20.072483987392253
          },
          "tool-final": {
            "e2e_change_pct": 14.243783001359311,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.788657694417429,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.021350717542684,
            "ttft_change_pct": 23.50413602786725
          }
        }
      },
      "complete": true
    }
  }
}
```
