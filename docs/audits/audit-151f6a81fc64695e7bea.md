# Public audit excerpt

Original SHA256: `151f6a81fc64695e7beac655861477d9ba86be18bde27f1288a9a2252342624a`

Original file: `RESULTS.json`; 42559 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6611137679999999,
              "format_passes": 0,
              "gpu_energy_j": 462.1304985864357,
              "semantic_passes": 0,
              "tokens_per_s": 79.48163391651747,
              "ttft_s": 0.0632472405
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200728648,
              "format_passes": 0,
              "gpu_energy_j": 48.154668172884996,
              "semantic_passes": 0,
              "tokens_per_s": 2532.8325961578826,
              "ttft_s": 0.2005350735
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7222026404999999,
              "format_passes": 0,
              "gpu_energy_j": 191.04214935821827,
              "semantic_passes": 0,
              "tokens_per_s": 2841.4142323960014,
              "ttft_s": 0.7218820324999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4281364490000001,
              "format_passes": 0,
              "gpu_energy_j": 382.0469163434678,
              "semantic_passes": 0,
              "tokens_per_s": 2871.7905115242315,
              "ttft_s": 1.4277965975
            },
            "thinking-quality-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6665573140000001,
              "format_passes": 2,
              "gpu_energy_j": 181.8307273838724,
              "semantic_passes": 2,
              "tokens_per_s": 79.28907590584953
            },
            "thinking-quality-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23872886399999999,
              "format_passes": 2,
              "gpu_energy_j": 59.66476372006012,
              "semantic_passes": 2,
              "tokens_per_s": 78.39046669310426
            },
            "thinking-quality-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24174111650000002,
              "format_passes": 0,
              "gpu_energy_j": 57.017283714688595,
              "semantic_passes": 0,
              "tokens_per_s": 77.68659234421672
            },
            "thinking-quality-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.184764135,
              "format_passes": 2,
              "gpu_energy_j": 43.382528521684826,
              "semantic_passes": 2,
              "tokens_per_s": 76.95063077638954
            },
            "thinking-quality-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35801819700000004,
              "format_passes": 0,
              "gpu_energy_j": 94.70034559386481,
              "semantic_passes": 0,
              "tokens_per_s": 78.82562373214085
            },
            "thinking-quality-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4691237935,
              "format_passes": 0,
              "gpu_energy_j": 122.85727542318557,
              "semantic_passes": 2,
              "tokens_per_s": 78.92372280474763
            },
            "thinking-quality-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.088660363,
              "format_passes": 2,
              "gpu_energy_j": 291.95307514451235,
              "semantic_passes": 2,
              "tokens_per_s": 77.74872475959543
            },
            "thinking-quality-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234924302,
              "format_passes": 0,
              "gpu_energy_j": 59.24753877162472,
              "semantic_passes": 0,
              "tokens_per_s": 78.32961598344812
            },
            "thinking-quality-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295499745,
              "format_passes": 2,
              "gpu_energy_j": 76.4513165039585,
              "semantic_passes": 2,
              "tokens_per_s": 78.7006176192914
            },
            "thinking-quality-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3588998325,
              "format_passes": 2,
              "gpu_energy_j": 90.32397765826744,
              "semantic_passes": 2,
              "tokens_per_s": 77.95784708655955
            },
            "thinking-quality-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691002725,
              "format_passes": 2,
              "gpu_energy_j": 98.14975644371566,
              "semantic_passes": 2,
              "tokens_per_s": 78.99301094852498
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6213399390000001,
              "format_passes": 0,
              "gpu_energy_j": 165.05370042127586,
              "semantic_passes": 0,
              "tokens_per_s": 78.8214163957621,
              "ttft_s": 0.3193247735
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5623271125,
              "format_passes": 0,
              "gpu_energy_j": 144.9830443854978,
              "semantic_passes": 0,
              "tokens_per_s": 78.57251994549028,
              "ttft_s": 0.256714569
            }
          }
        },
        "B": {
          "format_passes": 20,
          "quality_attempts": 24,
          "quality_passes": 22,
          "tasks": {
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.66338846,
              "format_passes": 0,
              "gpu_energy_j": 466.26876630286563,
              "semantic_passes": 0,
              "tokens_per_s": 79.37357879405187,
              "ttft_s": 0.0632756105
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19957892449999998,
              "format_passes": 0,
              "gpu_energy_j": 48.64055396173671,
              "semantic_passes": 0,
              "tokens_per_s": 2546.7746283749584,
              "ttft_s": 0.19942245600000003
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7216022980000001,
              "format_passes": 0,
              "gpu_energy_j": 192.41300669484298,
              "semantic_passes": 0,
              "tokens_per_s": 2843.76652669821,
              "ttft_s": 0.7212702344999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4268882244999999,
              "format_passes": 0,
              "gpu_energy_j": 383.24502564679767,
              "semantic_passes": 0,
              "tokens_per_s": 2874.343686770901,
              "ttft_s": 1.4265386405
            },
            "thinking-quality-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 7.1447845095,
              "format_passes": 2,
              "gpu_energy_j": 2046.6208898070283,
              "semantic_passes": 2,
              "tokens_per_s": 79.4884879099072
            },
            "thinking-quality-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.710527129,
              "format_passes": 2,
              "gpu_energy_j": 1935.7568587359829,
              "semantic_passes": 2,
              "tokens_per_s": 79.39577032237008
            },
            "thinking-quality-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.6843032305,
              "format_passes": 2,
              "gpu_energy_j": 1930.6012891114385,
              "semantic_passes": 2,
              "tokens_per_s": 79.45410610729141
            },
            "thinking-quality-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.647191296,
              "format_passes": 2,
              "gpu_energy_j": 1895.5825649487865,
              "semantic_passes": 2,
              "tokens_per_s": 79.49322730545396
            },
            "thinking-quality-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.8198583465,
              "format_passes": 0,
              "gpu_energy_j": 1953.7902799453097,
              "semantic_passes": 0,
              "tokens_per_s": 79.52429726354612
            },
            "thinking-quality-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.796609364,
              "format_passes": 2,
              "gpu_energy_j": 1957.5865847983523,
              "semantic_passes": 2,
              "tokens_per_s": 79.4772262356242
            },
            "thinking-quality-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 7.5396944315,
              "format_passes": 2,
              "gpu_energy_j": 2156.7443035130964,
              "semantic_passes": 2,
              "tokens_per_s": 78.89674251887917
            },
            "thinking-quality-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.693265899,
              "format_passes": 2,
              "gpu_energy_j": 1915.2554714999865,
              "semantic_passes": 2,
              "tokens_per_s": 79.5571973191647
            },
            "thinking-quality-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.7667555695,
              "format_passes": 2,
              "gpu_energy_j": 1943.3441451045535,
              "semantic_passes": 2,
              "tokens_per_s": 79.41341322213023
            },
            "thinking-quality-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 5.447484232000001,
              "format_passes": 0,
              "gpu_energy_j": 1567.5237915675707,
              "semantic_passes": 2,
              "tokens_per_s": 79.48826890197638
            },
            "thinking-quality-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 6.8299226725,
              "format_passes": 2,
              "gpu_energy_j": 1968.116629566016,
              "semantic_passes": 2,
              "tokens_per_s": 79.47448617385616
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6226912155,
              "format_passes": 0,
              "gpu_energy_j": 164.6842857261572,
              "semantic_passes": 0,
              "tokens_per_s": 78.74919537568708,
              "ttft_s": 0.3205364075
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5635846520000001,
              "format_passes": 0,
              "gpu_energy_j": 148.78677803699378,
              "semantic_passes": 0,
              "tokens_per_s": 78.51746494804607,
              "ttft_s": 0.257378204
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 4,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 4,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "decode": {
            "e2e_change_pct": 0.1369377609059752,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8954760027931608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.13594980015018132,
            "ttft_change_pct": 0.04485571192627269
          },
          "prefill": {
            "e2e_change_pct": -0.5727749932336712,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0090107715149843,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5504521790435257,
            "ttft_change_pct": -0.5548243908564787
          },
          "prefill2048": {
            "e2e_change_pct": -0.08312659997812277,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7175680033070897,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0827860392683677,
            "ttft_change_pct": -0.08475041245745718
          },
          "prefill4096": {
            "e2e_change_pct": -0.0874023277589675,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31360266293911643,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.08890534446799325,
            "ttft_change_pct": -0.08810477642281489
          },
          "thinking-quality-code": {
            "e2e_change_pct": 971.8934980435904,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1025.563824801899,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-energy": {
            "e2e_change_pct": 2710.9408374682334,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3144.3887112640227,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-filtering": {
            "e2e_change_pct": 2665.0667487919873,
            "format_pass_change": 2,
            "gpu_energy_change_pct": 3285.9930942555293,
            "same_token_counts": false,
            "semantic_pass_change": 2,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-german": {
            "e2e_change_pct": 3497.663202330907,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4269.460770368137,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-ha_sim": {
            "e2e_change_pct": 1804.8915400520827,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1963.1289861648472,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-jarvis_memory": {
            "e2e_change_pct": 1348.7880295502428,
            "format_pass_change": 2,
            "gpu_energy_change_pct": 1493.3827101857719,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-long_context": {
            "e2e_change_pct": 592.5662665556237,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 638.7297778745918,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-math": {
            "e2e_change_pct": 2749.1160097178877,
            "format_pass_change": 2,
            "gpu_energy_change_pct": 3132.6329687424163,
            "same_token_counts": false,
            "semantic_pass_change": 2,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-pve_sim": {
            "e2e_change_pct": 2189.9361789635386,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2441.9367958221246,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-sorting": {
            "e2e_change_pct": 1417.8285802069859,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 1635.44592721343,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "thinking-quality-time": {
            "e2e_change_pct": 1750.4247169039952,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1905.2180472751754,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false
          },
          "tool-call": {
            "e2e_change_pct": 0.21747781128871324,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22381485187897843,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09162613839923672,
            "ttft_change_pct": 0.37943626694532107
          },
          "tool-final": {
            "e2e_change_pct": 0.2236313121039668,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.6235713752721157,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.07006902347336252,
            "ttft_change_pct": 0.2585108443923234
          }
        }
      },
      "complete": true,
      "thinking": {
        "arms": {
          "A": {
            "empty_final": 0,
            "final_tokens": 508,
            "forced_cap_requests": 0,
            "format_passes": 16,
            "length_stops": 0,
            "median_e2e_s": 0.35801819700000004,
            "questions": 24,
            "reasoning_tokens": 0,
            "semantic_passes": 18,
            "starts": 2
          },
          "B": {
            "empty_final": 0,
            "final_tokens": 508,
            "forced_cap_requests": 22,
            "format_passes": 20,
            "length_stops": 0,
            "median_e2e_s": 6.7829097775000005,
            "questions": 24,
            "reasoning_tokens": 12060,
            "semantic_passes": 22,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Same12 unchanged questions; final-only semantic/format scoring. Original off questions preserved before candidate. Both candidate arms share expanded total cap, format and buffered API. Raw token counts include separately reported delimiters/EOS. Kernel probes remain fixed thinking-off; thinking latency is full chat E2E, no buffered TTFT invented. Cap is per thinking block, original engine may re-arm for additional blocks.",
        "original_quality": {
          "A": {
            "attempts": 24,
            "passes": 18
          },
          "B": {
            "attempts": 24,
            "passes": 18
          }
        }
      }
    }
  }
}
```

</details>
