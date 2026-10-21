# Public audit excerpt

Original SHA256: `221bbaebac83f3523c2c5aed765c160c31fa7fe3d73a84f5955716f79b6bd37d`

Original file: `RESULTS.json`; 40442 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.837711264,
              "format_passes": 2,
              "gpu_energy_j": 484.609040191036,
              "semantic_passes": 2,
              "tokens_per_s": 34.765753715836475,
              "ttft_s": 0.547366647
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7812726,
              "format_passes": 0,
              "gpu_energy_j": 1066.558448251616,
              "semantic_passes": 0,
              "tokens_per_s": 35.42660238232322,
              "ttft_s": 0.195231198
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6011608884999999,
              "format_passes": 2,
              "gpu_energy_j": 146.85410981295746,
              "semantic_passes": 2,
              "tokens_per_s": 34.85413342834784,
              "ttft_s": 0.225043761
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.942444835,
              "format_passes": 0,
              "gpu_energy_j": 246.01145441593226,
              "semantic_passes": 0,
              "tokens_per_s": 34.84603360570987,
              "ttft_s": 0.5371363725
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5056343505,
              "format_passes": 2,
              "gpu_energy_j": 108.28732918522564,
              "semantic_passes": 2,
              "tokens_per_s": 32.66917157807574,
              "ttft_s": 0.224863947
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.027459629,
              "format_passes": 0,
              "gpu_energy_j": 266.0330556775963,
              "semantic_passes": 0,
              "tokens_per_s": 35.11567747489016,
              "ttft_s": 0.2550784215
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1699415110000002,
              "format_passes": 0,
              "gpu_energy_j": 296.98416454459493,
              "semantic_passes": 2,
              "tokens_per_s": 35.13278570107211,
              "ttft_s": 0.369403131
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8092029280000004,
              "format_passes": 2,
              "gpu_energy_j": 1015.0767228469297,
              "semantic_passes": 2,
              "tokens_per_s": 34.196951618563595,
              "ttft_s": 3.2208861875
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5925040994999999,
              "format_passes": 2,
              "gpu_energy_j": 141.065948500346,
              "semantic_passes": 2,
              "tokens_per_s": 34.69779134257297,
              "ttft_s": 0.216699445
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7235614804999999,
              "format_passes": 0,
              "gpu_energy_j": 188.13709136281045,
              "semantic_passes": 0,
              "tokens_per_s": 699.0998937100073,
              "ttft_s": 0.7233129395
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.746384619,
              "format_passes": 0,
              "gpu_energy_j": 733.5806571318034,
              "semantic_passes": 0,
              "tokens_per_s": 746.051045144462,
              "ttft_s": 2.746147023
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4642311795,
              "format_passes": 0,
              "gpu_energy_j": 1477.1198009872596,
              "semantic_passes": 0,
              "tokens_per_s": 749.8410041912002,
              "ttft_s": 5.463913531499999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.872791929,
              "format_passes": 0,
              "gpu_energy_j": 227.95064970372292,
              "semantic_passes": 2,
              "tokens_per_s": 35.110890513313564,
              "ttft_s": 0.24396929550000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0007079755000001,
              "format_passes": 0,
              "gpu_energy_j": 260.78174581495193,
              "semantic_passes": 2,
              "tokens_per_s": 34.90734962505619,
              "ttft_s": 0.22546579249999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0520834225,
              "format_passes": 0,
              "gpu_energy_j": 276.5911787385745,
              "semantic_passes": 2,
              "tokens_per_s": 35.164871757532765,
              "ttft_s": 0.2324552405
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.710808372,
              "format_passes": 0,
              "gpu_energy_j": 457.6061446556258,
              "semantic_passes": 0,
              "tokens_per_s": 35.05091848134262,
              "ttft_s": 1.031675655
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7790034989999999,
              "format_passes": 0,
              "gpu_energy_j": 466.86246718171185,
              "semantic_passes": 0,
              "tokens_per_s": 35.09655675372437,
              "ttft_s": 1.0951102659999998
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
              "e2e_s": 1.7627092275,
              "format_passes": 2,
              "gpu_energy_j": 483.40959645894594,
              "semantic_passes": 2,
              "tokens_per_s": 35.41596657677942
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.780271838,
              "format_passes": 0,
              "gpu_energy_j": 1066.3067234690793,
              "semantic_passes": 0,
              "tokens_per_s": 35.43259207352142
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581544515,
              "format_passes": 2,
              "gpu_energy_j": 149.65225234682825,
              "semantic_passes": 2,
              "tokens_per_s": 35.00601854947072
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9278883415000001,
              "format_passes": 0,
              "gpu_energy_j": 246.04697843393524,
              "semantic_passes": 0,
              "tokens_per_s": 34.959395627714926
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.466421792,
              "format_passes": 2,
              "gpu_energy_j": 111.41389797167957,
              "semantic_passes": 2,
              "tokens_per_s": 34.324877456188375
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.991982087,
              "format_passes": 0,
              "gpu_energy_j": 263.78055418568715,
              "semantic_passes": 0,
              "tokens_per_s": 35.29555096857655
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1478695554999998,
              "format_passes": 0,
              "gpu_energy_j": 297.7676327675407,
              "semantic_passes": 2,
              "tokens_per_s": 35.34402348168148
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7960479425,
              "format_passes": 2,
              "gpu_energy_j": 1024.3751785019745,
              "semantic_passes": 2,
              "tokens_per_s": 34.43800025981258
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5731783965,
              "format_passes": 2,
              "gpu_energy_j": 145.61776499428763,
              "semantic_passes": 2,
              "tokens_per_s": 35.06545727958088
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.727029074,
              "format_passes": 0,
              "gpu_energy_j": 186.18035462654046,
              "semantic_passes": 0,
              "tokens_per_s": 695.7751106712055
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7465171909999997,
              "format_passes": 0,
              "gpu_energy_j": 735.589677507423,
              "semantic_passes": 0,
              "tokens_per_s": 746.0688424269701
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4714949845,
              "format_passes": 0,
              "gpu_energy_j": 1479.7470619827368,
              "semantic_passes": 0,
              "tokens_per_s": 748.8719393306801
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.845317162,
              "format_passes": 0,
              "gpu_energy_j": 225.00662858895538,
              "semantic_passes": 2,
              "tokens_per_s": 35.32070467576014
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9854299725,
              "format_passes": 0,
              "gpu_energy_j": 259.82682198127384,
              "semantic_passes": 2,
              "tokens_per_s": 35.162625455694624
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015913751,
              "format_passes": 0,
              "gpu_energy_j": 275.5012800671754,
              "semantic_passes": 2,
              "tokens_per_s": 35.31912010044422
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7100584964999999,
              "format_passes": 0,
              "gpu_energy_j": 464.7654450795393,
              "semantic_passes": 0,
              "tokens_per_s": 35.02253402974726
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7777801975,
              "format_passes": 0,
              "gpu_energy_j": 467.2065817123889,
              "semantic_passes": 0,
              "tokens_per_s": 35.12142905501142
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
            "e2e_change_pct": -4.0812742441785455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.24750750246368414,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.8702682710622698
          },
          "decode": {
            "e2e_change_pct": -0.02646627487263853,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.02360159285684782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.016907326120518817
          },
          "energy": {
            "e2e_change_pct": -3.2630821258093023,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9053893264782795,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.43577362620452753
          },
          "filtering": {
            "e2e_change_pct": -1.5445459468192535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.01443998536057034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3253225985136998
          },
          "german": {
            "e2e_change_pct": -7.755121553989442,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8872895933243825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 5.0680987552919055
          },
          "ha_sim": {
            "e2e_change_pct": -3.452937808809997,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8466998532088099,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5122313069853446
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.886586234651555,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2638080801874221,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.6012554267876613
          },
          "long_context": {
            "e2e_change_pct": -0.34534745847492054,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9160347632606536,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.7048834174977703
          },
          "math": {
            "e2e_change_pct": -3.261699457659184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2267294427403614,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.0596234595393383
          },
          "prefill": {
            "e2e_change_pct": 0.4792396490763906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0400589921402248,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.47558053844890535
          },
          "prefill2048": {
            "e2e_change_pct": 0.004827146171826335,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2738649603268639,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.002385531475890268
          },
          "prefill4096": {
            "e2e_change_pct": 0.13293370579288144,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17786377203266035,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.12923604538876976
          },
          "pve_sim": {
            "e2e_change_pct": -3.147917170989334,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.291516878146215,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.597575736129552
          },
          "sorting": {
            "e2e_change_pct": -1.5267194200552447,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3661774065872314,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.7312953672518274
          },
          "time": {
            "e2e_change_pct": -3.437909078925716,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.39404679367206485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.43864326870015624
          },
          "tool-call": {
            "e2e_change_pct": -0.043831647791359174,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5645114270266713,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.08098062140786677
          },
          "tool-final": {
            "e2e_change_pct": -0.06876329926768232,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07370790219105583,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.07086820927071358
          }
        }
      },
      "complete": true
    }
  }
}
```
