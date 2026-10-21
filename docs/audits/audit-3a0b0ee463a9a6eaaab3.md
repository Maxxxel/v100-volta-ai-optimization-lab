# Public audit excerpt

Original SHA256: `3a0b0ee463a9a6eaaab393f708e2288aa07cb7efee787b59dd330c9b81ef2d20`

Original file: `RESULTS.json`; 43125 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6669825359999999,
              "format_passes": 2,
              "gpu_energy_j": 177.35239585205403,
              "semantic_passes": 2,
              "tokens_per_s": 79.25224251726908,
              "ttft_s": 0.12440368299999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6648834845,
              "format_passes": 0,
              "gpu_energy_j": 457.64371641434866,
              "semantic_passes": 0,
              "tokens_per_s": 79.43274682353723,
              "ttft_s": 0.0636844175
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23852070749999998,
              "format_passes": 2,
              "gpu_energy_j": 55.15770454756691,
              "semantic_passes": 2,
              "tokens_per_s": 78.19108304230673,
              "ttft_s": 0.072169446
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2422101415,
              "format_passes": 0,
              "gpu_energy_j": 58.77242551022495,
              "semantic_passes": 0,
              "tokens_per_s": 77.31130351140598,
              "ttft_s": 0.1257561765
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182719957,
              "format_passes": 2,
              "gpu_energy_j": 41.91615780418255,
              "semantic_passes": 2,
              "tokens_per_s": 77.54008405949298,
              "ttft_s": 0.066613229
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35785108899999996,
              "format_passes": 0,
              "gpu_energy_j": 90.0470319462282,
              "semantic_passes": 0,
              "tokens_per_s": 78.85011510906017,
              "ttft_s": 0.07880179600000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4695960335,
              "format_passes": 0,
              "gpu_energy_j": 117.30786287005748,
              "semantic_passes": 2,
              "tokens_per_s": 78.9559796580901,
              "ttft_s": 0.114968501
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0821626485,
              "format_passes": 2,
              "gpu_energy_j": 290.81273168263954,
              "semantic_passes": 2,
              "tokens_per_s": 77.66231475593347,
              "ttft_s": 0.8246945045
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2346313875,
              "format_passes": 0,
              "gpu_energy_j": 54.91969319002598,
              "semantic_passes": 0,
              "tokens_per_s": 77.81711419832149,
              "ttft_s": 0.0675435195
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199749668,
              "format_passes": 0,
              "gpu_energy_j": 48.886287297040134,
              "semantic_passes": 0,
              "tokens_per_s": 2546.058601896839,
              "ttft_s": 0.1995035645
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7196153955,
              "format_passes": 0,
              "gpu_energy_j": 188.25633656867126,
              "semantic_passes": 0,
              "tokens_per_s": 2851.3423161851692,
              "ttft_s": 0.7193756065
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4194343360000001,
              "format_passes": 0,
              "gpu_energy_j": 383.43626322938246,
              "semantic_passes": 0,
              "tokens_per_s": 2889.5531927803295,
              "ttft_s": 1.4190490875
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2955088865,
              "format_passes": 2,
              "gpu_energy_j": 74.19035825609159,
              "semantic_passes": 2,
              "tokens_per_s": 78.50761900566619,
              "ttft_s": 0.0789673295
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353909164,
              "format_passes": 2,
              "gpu_energy_j": 89.83166923760993,
              "semantic_passes": 2,
              "tokens_per_s": 78.63230201755654,
              "ttft_s": 0.074120606
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.371409585,
              "format_passes": 2,
              "gpu_energy_j": 95.04519753151,
              "semantic_passes": 2,
              "tokens_per_s": 78.55701169965403,
              "ttft_s": 0.078606443
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6222324775,
              "format_passes": 0,
              "gpu_energy_j": 162.56654295464872,
              "semantic_passes": 0,
              "tokens_per_s": 78.79243809661499,
              "ttft_s": 0.3193388955
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5614256885,
              "format_passes": 0,
              "gpu_energy_j": 144.8559181194372,
              "semantic_passes": 0,
              "tokens_per_s": 78.71213998440552,
              "ttft_s": 0.2565382045
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
              "e2e_s": 2.034539131,
              "format_passes": 2,
              "gpu_energy_j": 259.2390891337456,
              "semantic_passes": 2,
              "tokens_per_s": 23.990468057169082,
              "ttft_s": 0.2418969795
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 6.1462571645,
              "format_passes": 0,
              "gpu_energy_j": 707.4826041100337,
              "semantic_passes": 0,
              "tokens_per_s": 21.654806150772117,
              "ttft_s": 0.27059737
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7340588175,
              "format_passes": 2,
              "gpu_energy_j": 87.15885112922865,
              "semantic_passes": 2,
              "tokens_per_s": 24.21239123804026,
              "ttft_s": 0.19685223200000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.616516323,
              "format_passes": 0,
              "gpu_energy_j": 81.14812709528286,
              "semantic_passes": 0,
              "tokens_per_s": 24.754274198555876,
              "ttft_s": 0.252694693
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.849332482,
              "format_passes": 2,
              "gpu_energy_j": 86.42540721932906,
              "semantic_passes": 2,
              "tokens_per_s": 24.09180481868932,
              "ttft_s": 0.47493768150000004
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.585986069,
              "format_passes": 0,
              "gpu_energy_j": 170.14017909495652,
              "semantic_passes": 0,
              "tokens_per_s": 17.871782726821912,
              "ttft_s": 0.341262466
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.6030366864999999,
              "format_passes": 0,
              "gpu_energy_j": 185.88029612876556,
              "semantic_passes": 2,
              "tokens_per_s": 23.358633616524735,
              "ttft_s": 0.4037145505
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.4681124015,
              "format_passes": 2,
              "gpu_energy_j": 377.9965378351559,
              "semantic_passes": 2,
              "tokens_per_s": 18.972234130083105,
              "ttft_s": 1.387237813
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7255351565,
              "format_passes": 0,
              "gpu_energy_j": 89.40460948386485,
              "semantic_passes": 0,
              "tokens_per_s": 24.38699303961348,
              "ttft_s": 0.1923085795
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.33290294249999997,
              "format_passes": 0,
              "gpu_energy_j": 59.775210857718285,
              "semantic_passes": 0,
              "tokens_per_s": 1522.7557102229953,
              "ttft_s": 0.332758437
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1741413710000002,
              "format_passes": 0,
              "gpu_energy_j": 227.2254135705528,
              "semantic_passes": 0,
              "tokens_per_s": 1746.9047016880172,
              "ttft_s": 1.1738189074999998
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.3587445865000003,
              "format_passes": 0,
              "gpu_energy_j": 456.50373681658164,
              "semantic_passes": 0,
              "tokens_per_s": 1737.8526830218964,
              "ttft_s": 2.358436655
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0449551625,
              "format_passes": 2,
              "gpu_energy_j": 120.68591663769396,
              "semantic_passes": 2,
              "tokens_per_s": 20.67057915079482,
              "ttft_s": 0.1982699295
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1351013195,
              "format_passes": 2,
              "gpu_energy_j": 136.52240786524857,
              "semantic_passes": 2,
              "tokens_per_s": 23.616548894630792,
              "ttft_s": 0.2033914705
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1509635665,
              "format_passes": 2,
              "gpu_energy_j": 140.11511236399934,
              "semantic_passes": 2,
              "tokens_per_s": 24.205728056609594,
              "ttft_s": 0.199953397
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.0068946385,
              "format_passes": 0,
              "gpu_energy_j": 243.2138048475038,
              "semantic_passes": 0,
              "tokens_per_s": 23.517586602456657,
              "ttft_s": 0.792075027
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.467813316,
              "format_passes": 0,
              "gpu_energy_j": 205.73911391357797,
              "semantic_passes": 0,
              "tokens_per_s": 24.29570680767251,
              "ttft_s": 0.4717440615
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
            "e2e_change_pct": 205.0363422109151,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 46.17174348746933,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -69.72897258782102,
            "ttft_change_pct": 94.44519138553159
          },
          "decode": {
            "e2e_change_pct": 269.17040872357813,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 54.59244358322663,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -72.73818794296632,
            "ttft_change_pct": 324.903580220389
          },
          "energy": {
            "e2e_change_pct": 207.7547543749425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 58.0175459514719,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -69.03433192639153,
            "ttft_change_pct": 172.76395055048647
          },
          "filtering": {
            "e2e_change_pct": 154.5377824322026,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 38.07176816475797,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -67.98104148521593,
            "ttft_change_pct": 100.9401844369847
          },
          "german": {
            "e2e_change_pct": 364.8274309740561,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 106.18637715574492,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -68.92987012987403,
            "ttft_change_pct": 612.9780204769838
          },
          "ha_sim": {
            "e2e_change_pct": 343.1972174325283,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 88.9459046207721,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -77.3344874613019,
            "ttft_change_pct": 333.0643250821338
          },
          "jarvis_memory": {
            "e2e_change_pct": 241.36503976667422,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 58.45510401520666,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -70.41562435463831,
            "ttft_change_pct": 251.15231301484914
          },
          "long_context": {
            "e2e_change_pct": 128.0722223152946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 29.97936357465223,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -75.57086189137362,
            "ttft_change_pct": 68.21232655613021
          },
          "math": {
            "e2e_change_pct": 209.22340111039065,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 62.79153121726051,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -68.66114441424568,
            "ttft_change_pct": 184.7180320533934
          },
          "prefill": {
            "e2e_change_pct": 66.66007299696737,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 22.27398348848928,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -40.191647235121486,
            "ttft_change_pct": 66.79322889992775
          },
          "prefill2048": {
            "e2e_change_pct": 63.16234732362673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 20.700008144303062,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -38.733953767248366,
            "ttft_change_pct": 63.17190865158977
          },
          "prefill4096": {
            "e2e_change_pct": 66.1749703157808,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 19.05596329669219,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -39.85739084630819,
            "ttft_change_pct": 66.19838424017874
          },
          "pve_sim": {
            "e2e_change_pct": 253.61209433544394,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 62.67062118922271,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -73.67060749950531,
            "ttft_change_pct": 151.07842794658515
          },
          "sorting": {
            "e2e_change_pct": 220.7323898230564,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 51.97581100729516,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -69.9658431857205,
            "ttft_change_pct": 174.40610847137435
          },
          "time": {
            "e2e_change_pct": 209.8906471409455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 47.41945516768218,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -69.18705595732813,
            "ttft_change_pct": 154.37278341166004
          },
          "tool-call": {
            "e2e_change_pct": 222.53132246701153,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 49.60876969337613,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -70.15248268670213,
            "ttft_change_pct": 148.03587604316743
          },
          "tool-final": {
            "e2e_change_pct": 161.44391788014883,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 42.030174938341894,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -69.13346935747651,
            "ttft_change_pct": 83.8884241118948
          }
        }
      },
      "complete": true,
      "residency": {
        "arms": {
          "A": {
            "gpu_owned_peak_bytes": 7459569664,
            "memory_limit_bytes": 8589934592,
            "rss_peak_bytes": 7728553984,
            "starts": 2,
            "swap_peak_bytes": 0,
            "verified_starts": 2
          },
          "B": {
            "gpu_owned_peak_bytes": 6740246528,
            "memory_limit_bytes": 8589934592,
            "rss_peak_bytes": 7728476160,
            "starts": 2,
            "swap_peak_bytes": 0,
            "verified_starts": 2
          }
        },
        "change_exercised": true,
        "note": "Both arms same original engine, verbosity5 for actual layer assignment evidence, six threads and unchanged frozen quality/speed probes. Output stays on GPU, first4repeating layers move to CPU. Paired A/B isolates offload; original-baseline comparison also includes the shared diagnostic verbosity difference."
      }
    }
  }
}
```
