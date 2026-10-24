# Public audit excerpt

Original SHA256: `6812b5bedd6abb3e53709e9b78e71cdc3e65cbcd6383ac2d0d52890f9b6a16a5`

Original file: `RESULTS.json`; 49539 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.668470547,
              "format_passes": 2,
              "gpu_energy_j": 178.94730544832834,
              "semantic_passes": 2,
              "tokens_per_s": 79.00152288551216,
              "ttft_s": 0.1241437645
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.9789726395000002,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 48.683658664143415,
              "ttft_s": 0.3722959675
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.9769172104999999,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 49.52712188582642,
              "ttft_s": 0.4824871475
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6987829235,
              "format_passes": 0,
              "gpu_energy_j": 460.8375911720167,
              "semantic_passes": 0,
              "tokens_per_s": 77.71286754335134,
              "ttft_s": 0.0644129135
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24751534549999998,
              "format_passes": 2,
              "gpu_energy_j": 54.83450614174585,
              "semantic_passes": 2,
              "tokens_per_s": 77.490762004494,
              "ttft_s": 0.079663541
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2448486365,
              "format_passes": 0,
              "gpu_energy_j": 61.827489936255716,
              "semantic_passes": 0,
              "tokens_per_s": 76.55972520840467,
              "ttft_s": 0.12730660700000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1797113185,
              "format_passes": 2,
              "gpu_energy_j": 41.60817631270281,
              "semantic_passes": 2,
              "tokens_per_s": 76.97746075062031,
              "ttft_s": 0.0627736385
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3688220045,
              "format_passes": 0,
              "gpu_energy_j": 89.64701299593105,
              "semantic_passes": 0,
              "tokens_per_s": 78.30536758796833,
              "ttft_s": 0.08783246650000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.474373066,
              "format_passes": 0,
              "gpu_energy_j": 120.76876761143816,
              "semantic_passes": 2,
              "tokens_per_s": 78.9038326297521,
              "ttft_s": 0.119462154
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0848657154999999,
              "format_passes": 2,
              "gpu_energy_j": 290.55316446426787,
              "semantic_passes": 2,
              "tokens_per_s": 77.77700870333501,
              "ttft_s": 0.827656932
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2426097505,
              "format_passes": 0,
              "gpu_energy_j": 58.167881833331634,
              "semantic_passes": 0,
              "tokens_per_s": 76.332551508833,
              "ttft_s": 0.072228913
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2128108405,
              "format_passes": 0,
              "gpu_energy_j": 51.34279673661212,
              "semantic_passes": 0,
              "tokens_per_s": 2385.1304761232072,
              "ttft_s": 0.21265292600000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7345620815,
              "format_passes": 0,
              "gpu_energy_j": 195.15070275296537,
              "semantic_passes": 0,
              "tokens_per_s": 2793.067237207856,
              "ttft_s": 0.7343283135
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4527573995,
              "format_passes": 0,
              "gpu_energy_j": 387.18488504357083,
              "semantic_passes": 0,
              "tokens_per_s": 2822.9443907879686,
              "ttft_s": 1.4524135025
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30296417649999996,
              "format_passes": 2,
              "gpu_energy_j": 72.99286408712338,
              "semantic_passes": 2,
              "tokens_per_s": 78.27257431201784,
              "ttft_s": 0.0857134065
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35929875850000004,
              "format_passes": 2,
              "gpu_energy_j": 89.27460271730328,
              "semantic_passes": 2,
              "tokens_per_s": 77.98842540112462,
              "ttft_s": 0.0771428245
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37606130699999996,
              "format_passes": 2,
              "gpu_energy_j": 97.34369416351268,
              "semantic_passes": 2,
              "tokens_per_s": 78.7295121078744,
              "ttft_s": 0.083872535
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6443714715,
              "format_passes": 0,
              "gpu_energy_j": 165.90401096767252,
              "semantic_passes": 0,
              "tokens_per_s": 77.20401034337837,
              "ttft_s": 0.336103655
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5790787465,
              "format_passes": 0,
              "gpu_energy_j": 152.0326109988572,
              "semantic_passes": 0,
              "tokens_per_s": 77.06869491632267,
              "ttft_s": 0.2675270395
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
              "e2e_s": 0.6676495665,
              "format_passes": 2,
              "gpu_energy_j": 178.2846005606063,
              "semantic_passes": 2,
              "tokens_per_s": 78.94327044633991,
              "ttft_s": 0.12292196899999999
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.771872602,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 52.86330778874912,
              "ttft_s": 0.3739605875
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.9772704305000001,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 51.97265717224862,
              "ttft_s": 0.4883229455
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.699488032,
              "format_passes": 0,
              "gpu_energy_j": 466.9623407388078,
              "semantic_passes": 0,
              "tokens_per_s": 77.62973834619604,
              "ttft_s": 0.063216154
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.247218876,
              "format_passes": 2,
              "gpu_energy_j": 57.555805647181714,
              "semantic_passes": 2,
              "tokens_per_s": 77.27492983564002,
              "ttft_s": 0.07894717200000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24317884350000002,
              "format_passes": 0,
              "gpu_energy_j": 58.56405845536173,
              "semantic_passes": 0,
              "tokens_per_s": 76.63651835140826,
              "ttft_s": 0.125686994
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.178171879,
              "format_passes": 2,
              "gpu_energy_j": 41.54141126201901,
              "semantic_passes": 2,
              "tokens_per_s": 76.9437931795676,
              "ttft_s": 0.061139966000000004
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.366975985,
              "format_passes": 0,
              "gpu_energy_j": 90.67000847173833,
              "semantic_passes": 0,
              "tokens_per_s": 78.4176892372619,
              "ttft_s": 0.0863740625
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47264869249999997,
              "format_passes": 0,
              "gpu_energy_j": 117.58751696775647,
              "semantic_passes": 2,
              "tokens_per_s": 78.91415495927177,
              "ttft_s": 0.117813713
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.083525332,
              "format_passes": 2,
              "gpu_energy_j": 290.86270961998406,
              "semantic_passes": 2,
              "tokens_per_s": 77.72515531053051,
              "ttft_s": 0.82620339
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23637536199999998,
              "format_passes": 0,
              "gpu_energy_j": 55.01590166984832,
              "semantic_passes": 0,
              "tokens_per_s": 77.8869625587032,
              "ttft_s": 0.0694480895
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.21182519300000002,
              "format_passes": 0,
              "gpu_energy_j": 52.37410349790481,
              "semantic_passes": 0,
              "tokens_per_s": 2395.9053202426685,
              "ttft_s": 0.2116895085
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.73313261,
              "format_passes": 0,
              "gpu_energy_j": 194.16922811250038,
              "semantic_passes": 0,
              "tokens_per_s": 2798.1511907176196,
              "ttft_s": 0.73288585
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4532563230000002,
              "format_passes": 0,
              "gpu_energy_j": 390.81306401075034,
              "semantic_passes": 0,
              "tokens_per_s": 2822.1828187443334,
              "ttft_s": 1.4529239205
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3017119965,
              "format_passes": 2,
              "gpu_energy_j": 76.10813628578777,
              "semantic_passes": 2,
              "tokens_per_s": 78.23665994187739,
              "ttft_s": 0.08440457900000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35759814700000003,
              "format_passes": 2,
              "gpu_energy_j": 90.85862332359685,
              "semantic_passes": 2,
              "tokens_per_s": 78.1139235766739,
              "ttft_s": 0.075894602
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37554825999999997,
              "format_passes": 2,
              "gpu_energy_j": 94.91500597297086,
              "semantic_passes": 2,
              "tokens_per_s": 78.70459105363946,
              "ttft_s": 0.0832507725
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6430255555,
              "format_passes": 0,
              "gpu_energy_j": 172.82929121451758,
              "semantic_passes": 0,
              "tokens_per_s": 77.30247754433327,
              "ttft_s": 0.33508375700000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5786919385,
              "format_passes": 0,
              "gpu_energy_j": 147.92885758218478,
              "semantic_passes": 0,
              "tokens_per_s": 77.10584029600128,
              "ttft_s": 0.26730123149999996
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
            "e2e_change_pct": -0.12281476030386873,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3703352146385952,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.07373584336680672,
            "ttft_change_pct": -0.984177904481065
          },
          "concurrent-decode": {
            "e2e_change_pct": -6.9520624242712215,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 8.585322548249863,
            "ttft_change_pct": 0.44712275858858064
          },
          "concurrent-quality": {
            "e2e_change_pct": 0.03615659507312241,
            "format_pass_change": 0,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 1.2095240319328848
          },
          "decode": {
            "e2e_change_pct": 0.0415066863603375,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3290473008537473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.10696966896625026,
            "ttft_change_pct": -1.8579496485592206
          },
          "energy": {
            "e2e_change_pct": -0.11977823007340849,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.962750094623591,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.27852632142326694,
            "ttft_change_pct": -0.8992432309781417
          },
          "filtering": {
            "e2e_change_pct": -0.6819694909756979,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.278285572095176,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10030488327190668,
            "ttft_change_pct": -1.2722144106786404
          },
          "german": {
            "e2e_change_pct": -0.8566179987155254,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.16046137226017887,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.04373692081345304,
            "ttft_change_pct": -2.6024817726632232
          },
          "ha_sim": {
            "e2e_change_pct": -0.5005177233127989,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.141137268961434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.14344054916461957,
            "ttft_change_pct": -1.6604383983683468
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.3635057771176342,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.634166686139461,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.013082164928679418,
            "ttft_change_pct": -1.3798855493598383
          },
          "long_context": {
            "e2e_change_pct": -0.12355294123955751,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.10653649437510904,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.06666930712427854,
            "ttft_change_pct": -0.17562131649010437
          },
          "math": {
            "e2e_change_pct": -2.5697188539007265,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.418763867858689,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.036367210508261,
            "ttft_change_pct": -3.850014328749485
          },
          "prefill": {
            "e2e_change_pct": -0.4631566219484795,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0086688432328303,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.45175072086516277,
            "ttft_change_pct": -0.45304690517167234
          },
          "prefill2048": {
            "e2e_change_pct": -0.19460186361389686,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5029316454511656,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.18202044841733045,
            "ttft_change_pct": -0.19643304956129537
          },
          "prefill4096": {
            "e2e_change_pct": 0.034343208313503126,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9370662717815614,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.026977932902982893,
            "ttft_change_pct": 0.035142746822547366
          },
          "pve_sim": {
            "e2e_change_pct": -0.4133095914064078,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.267913360607456,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.04588372166894894,
            "ttft_change_pct": -1.5269810796750938
          },
          "sorting": {
            "e2e_change_pct": -0.47331404848146574,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7743238928875638,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1609189759939289,
            "ttft_change_pct": -1.6180668883857052
          },
          "time": {
            "e2e_change_pct": -0.13642642581146447,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.494962012087032,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03165401838232107,
            "ttft_change_pct": -0.741318358864429
          },
          "tool-call": {
            "e2e_change_pct": -0.20887268594727004,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.174269329868396,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12754156230609937,
            "ttft_change_pct": -0.30344745879063995
          },
          "tool-final": {
            "e2e_change_pct": -0.06679713291809497,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.699258658856596,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.04819775360012102,
            "ttft_change_pct": -0.08440567369267793
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 7.382633557892171,
        "arms": {
          "A": {
            "active_slots_max": 4,
            "aggregate_tokens_per_s": 171.6426825641994,
            "exact_serial_matches": 0,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 15,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 17,
            "request_e2e_s": 2.9789726395000002,
            "wave_elapsed_s": 2.982942782,
            "waves": 6
          },
          "B": {
            "active_slots_max": 4,
            "aggregate_tokens_per_s": 184.3144328468503,
            "exact_serial_matches": 4,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 14,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 17,
            "request_e2e_s": 2.771872602,
            "wave_elapsed_s": 2.7778634115000003,
            "waves": 6
          }
        },
        "change_exercised": true,
        "note": "Aggregate four-request wall-clock throughput; per-request native throughput and correctness are reported separately. Two starts per arm give preliminary results."
      },
      "numerical_results": [
        {
          "begin_ns": 394771550905281,
          "end_ns": 394772209624578,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 394837937395905,
          "end_ns": 394838346199002,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```

</details>
