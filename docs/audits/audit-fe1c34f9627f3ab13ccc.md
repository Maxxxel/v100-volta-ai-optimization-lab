# Public audit excerpt

Original SHA256: `fe1c34f9627f3ab13cccab624491d6ded8b04bf13c58ccc21d0d97ac41057f3e`

Original file: `RESULTS.json`; 47370 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6668515500000001,
              "format_passes": 2,
              "gpu_energy_j": 177.97325232168532,
              "semantic_passes": 2,
              "tokens_per_s": 79.18247313602774,
              "ttft_s": 0.123793162
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588624425,
              "format_passes": 0,
              "gpu_energy_j": 457.9421004539264,
              "semantic_passes": 0,
              "tokens_per_s": 79.59572891184968,
              "ttft_s": 0.0631328315
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2376160595,
              "format_passes": 2,
              "gpu_energy_j": 57.77044419436491,
              "semantic_passes": 2,
              "tokens_per_s": 78.29916229184985,
              "ttft_s": 0.0715291445
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24173558350000002,
              "format_passes": 0,
              "gpu_energy_j": 61.41186641113339,
              "semantic_passes": 0,
              "tokens_per_s": 77.3578222382493,
              "ttft_s": 0.1254274
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18197984150000002,
              "format_passes": 2,
              "gpu_energy_j": 43.35339538414652,
              "semantic_passes": 2,
              "tokens_per_s": 77.564141604387,
              "ttft_s": 0.0658954235
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.361717014,
              "format_passes": 0,
              "gpu_energy_j": 91.22216248754637,
              "semantic_passes": 0,
              "tokens_per_s": 77.74314185894036,
              "ttft_s": 0.07865918599999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469058844,
              "format_passes": 0,
              "gpu_energy_j": 116.71286559336382,
              "semantic_passes": 2,
              "tokens_per_s": 79.11620620791996,
              "ttft_s": 0.1150250715
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.663731978,
              "format_passes": 0,
              "gpu_energy_j": 463.9290040476028,
              "semantic_passes": 0,
              "tokens_per_s": 79.57757970802547,
              "ttft_s": 0.0659480385
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0811731834999998,
              "format_passes": 2,
              "gpu_energy_j": 287.92413932804743,
              "semantic_passes": 2,
              "tokens_per_s": 77.79413819541959,
              "ttft_s": 0.8240002065
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2341757815,
              "format_passes": 0,
              "gpu_energy_j": 58.23983662272495,
              "semantic_passes": 0,
              "tokens_per_s": 78.18438156583161,
              "ttft_s": 0.06792350999999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19918129350000002,
              "format_passes": 0,
              "gpu_energy_j": 49.4095248439948,
              "semantic_passes": 0,
              "tokens_per_s": 2548.3639740456624,
              "ttft_s": 0.19904584250000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7208519005,
              "format_passes": 0,
              "gpu_energy_j": 188.54915991694034,
              "semantic_passes": 0,
              "tokens_per_s": 2846.3659077801567,
              "ttft_s": 0.7205394620000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4223788050000001,
              "format_passes": 0,
              "gpu_energy_j": 382.06151173899696,
              "semantic_passes": 0,
              "tokens_per_s": 2883.4044680492498,
              "ttft_s": 1.4220151520000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294957315,
              "format_passes": 2,
              "gpu_energy_j": 69.05437346337007,
              "semantic_passes": 2,
              "tokens_per_s": 78.68913585718042,
              "ttft_s": 0.0788885295
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35336586449999996,
              "format_passes": 2,
              "gpu_energy_j": 83.33335648356375,
              "semantic_passes": 2,
              "tokens_per_s": 78.90907432904639,
              "ttft_s": 0.0745027095
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37136569399999997,
              "format_passes": 2,
              "gpu_energy_j": 92.97735999007463,
              "semantic_passes": 2,
              "tokens_per_s": 78.85386141051492,
              "ttft_s": 0.079623281
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620939699,
              "format_passes": 0,
              "gpu_energy_j": 164.64221501912436,
              "semantic_passes": 0,
              "tokens_per_s": 78.94859656788779,
              "ttft_s": 0.31898628399999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5601121375,
              "format_passes": 0,
              "gpu_energy_j": 143.75505035184588,
              "semantic_passes": 0,
              "tokens_per_s": 78.85366144399106,
              "ttft_s": 0.255517821
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
              "e2e_s": 0.665732341,
              "format_passes": 2,
              "gpu_energy_j": 172.06390392149223,
              "semantic_passes": 2,
              "tokens_per_s": 79.35255811099404,
              "ttft_s": 0.1237822715
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658703494,
              "format_passes": 0,
              "gpu_energy_j": 462.06623139006365,
              "semantic_passes": 0,
              "tokens_per_s": 79.61426590353557,
              "ttft_s": 0.063000306
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2386648145,
              "format_passes": 2,
              "gpu_energy_j": 58.28630770194735,
              "semantic_passes": 2,
              "tokens_per_s": 77.97642555701364,
              "ttft_s": 0.0718393135
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24252901500000001,
              "format_passes": 0,
              "gpu_energy_j": 59.06026737539774,
              "semantic_passes": 0,
              "tokens_per_s": 77.51828615355149,
              "ttft_s": 0.1263280225
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.181948924,
              "format_passes": 2,
              "gpu_energy_j": 39.448512032146695,
              "semantic_passes": 2,
              "tokens_per_s": 77.67527153091244,
              "ttft_s": 0.0660471625
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3603971935,
              "format_passes": 0,
              "gpu_energy_j": 91.78593230940648,
              "semantic_passes": 0,
              "tokens_per_s": 78.08199313640375,
              "ttft_s": 0.0785681045
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468875123,
              "format_passes": 0,
              "gpu_energy_j": 118.7554567944339,
              "semantic_passes": 2,
              "tokens_per_s": 79.1442375428145,
              "ttft_s": 0.1150773435
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.458098673,
              "format_passes": 0,
              "gpu_energy_j": 120.67863560563606,
              "semantic_passes": 0,
              "tokens_per_s": 78.93751992034726,
              "ttft_s": 0.0655324085
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0807173515,
              "format_passes": 2,
              "gpu_energy_j": 291.3168673161446,
              "semantic_passes": 2,
              "tokens_per_s": 77.95881499903733,
              "ttft_s": 0.824173074
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23338823,
              "format_passes": 0,
              "gpu_energy_j": 52.07081867863458,
              "semantic_passes": 0,
              "tokens_per_s": 78.34039437346755,
              "ttft_s": 0.067383885
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199063286,
              "format_passes": 0,
              "gpu_energy_j": 49.04685469772166,
              "semantic_passes": 0,
              "tokens_per_s": 2549.9518115968312,
              "ttft_s": 0.19892837400000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7184873220000001,
              "format_passes": 0,
              "gpu_energy_j": 188.6677532283124,
              "semantic_passes": 0,
              "tokens_per_s": 2855.304717269437,
              "ttft_s": 0.718249661
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.422611282,
              "format_passes": 0,
              "gpu_energy_j": 382.21034056099893,
              "semantic_passes": 0,
              "tokens_per_s": 2882.8459262036395,
              "ttft_s": 1.422254807
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30141095650000005,
              "format_passes": 2,
              "gpu_energy_j": 72.75545080927202,
              "semantic_passes": 2,
              "tokens_per_s": 77.03765738080281,
              "ttft_s": 0.080645143
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354777073,
              "format_passes": 2,
              "gpu_energy_j": 91.55965790100485,
              "semantic_passes": 2,
              "tokens_per_s": 78.33399422778113,
              "ttft_s": 0.0738976535
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691294865,
              "format_passes": 2,
              "gpu_energy_j": 95.52541872866632,
              "semantic_passes": 2,
              "tokens_per_s": 78.90388503730955,
              "ttft_s": 0.0776029015
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6216095269999999,
              "format_passes": 0,
              "gpu_energy_j": 162.7642840696972,
              "semantic_passes": 0,
              "tokens_per_s": 78.91462007585889,
              "ttft_s": 0.31961003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560903325,
              "format_passes": 0,
              "gpu_energy_j": 145.6749663549238,
              "semantic_passes": 0,
              "tokens_per_s": 78.77557413643767,
              "ttft_s": 0.256286492
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
            "e2e_change_pct": -0.16783480521265215,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3203575948098085,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.21480129153594874,
            "ttft_change_pct": -0.008797335671895112
          },
          "decode": {
            "e2e_change_pct": -0.0095817770013773,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9005791195108026,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.02328892760870005,
            "ttft_change_pct": -0.20991534333446582
          },
          "energy": {
            "e2e_change_pct": 0.4413653699193665,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.892954026537951,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4121841478115118,
            "ttft_change_pct": 0.43362604455585707
          },
          "filtering": {
            "e2e_change_pct": 0.3282228824206257,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.829225804655434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.207430755752136,
            "ttft_change_pct": 0.7180428678263295
          },
          "german": {
            "e2e_change_pct": -0.01698951913858826,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.007099253471084,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.14327487448033693,
            "ttft_change_pct": 0.23027244069537822
          },
          "ha_sim": {
            "e2e_change_pct": -0.3648765330126258,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6180184798152188,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.43586002489868214,
            "ttft_change_pct": -0.11579257888582051
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.039168006818346424,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7500994347843468,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.03543058525945497,
            "ttft_change_pct": 0.04544400565749118
          },
          "length-decode": {
            "e2e_change_pct": -72.46559667917857,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -73.98769325634716,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -0.6302386082339684
          },
          "long_context": {
            "e2e_change_pct": -0.04216086811589248,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1783409324466865,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.21168279183718663,
            "ttft_change_pct": 0.02097906027647145
          },
          "math": {
            "e2e_change_pct": -0.3363078346340531,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.592436898566515,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.19954472301424442,
            "ttft_change_pct": -0.7944598269435499
          },
          "prefill": {
            "e2e_change_pct": -0.05924627655859993,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7340085690324516,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.06230811482741405,
            "ttft_change_pct": -0.05901580184975996
          },
          "prefill2048": {
            "e2e_change_pct": -0.3280255623048012,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.06289782008273015,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3140428806025053,
            "ttft_change_pct": -0.317789811767466
          },
          "prefill4096": {
            "e2e_change_pct": 0.016344239606413957,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03895415199623997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.019370915589522752,
            "ttft_change_pct": 0.01685319594961765
          },
          "pve_sim": {
            "e2e_change_pct": 2.18799167601591,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.359656688312708,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.09873759368131,
            "ttft_change_pct": 2.226703313058964
          },
          "sorting": {
            "e2e_change_pct": 0.39936186309248445,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.871558958582959,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7287882998946449,
            "ttft_change_pct": -0.8121261683778136
          },
          "time": {
            "e2e_change_pct": -0.6021578018997054,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.740515259697296,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.06343839844975552,
            "ttft_change_pct": -2.537423068511835
          },
          "tool-call": {
            "e2e_change_pct": 0.10787327675758629,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1406132681153647,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.043036220409164994,
            "ttft_change_pct": 0.1955400690520026
          },
          "tool-final": {
            "e2e_change_pct": 0.14125519642036455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3355468196622367,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09902813150769463,
            "ttft_change_pct": 0.30082872380161607
          }
        }
      },
      "complete": true
    }
  }
}
```
