# Public audit excerpt

Original SHA256: `9a376eecf4678c9215efd1a42cb637059a4e09dcb3761bac1fcb309505385f74`

Original file: `RESULTS.json`; 43319 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7632966135,
              "format_passes": 2,
              "gpu_energy_j": 485.23789906080015,
              "semantic_passes": 2,
              "tokens_per_s": 35.40872033860503,
              "ttft_s": 0.5206384079999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7872257344999998,
              "format_passes": 0,
              "gpu_energy_j": 1066.8490425075718,
              "semantic_passes": 0,
              "tokens_per_s": 35.35944342174737,
              "ttft_s": 0.1954592185
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5814253309999999,
              "format_passes": 2,
              "gpu_energy_j": 146.1721599281243,
              "semantic_passes": 2,
              "tokens_per_s": 34.93284762290932,
              "ttft_s": 0.209257689
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9241855434999999,
              "format_passes": 0,
              "gpu_energy_j": 247.59809687043844,
              "semantic_passes": 0,
              "tokens_per_s": 35.03109284377616,
              "ttft_s": 0.5244715875
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46662587499999997,
              "format_passes": 2,
              "gpu_energy_j": 110.04775743527267,
              "semantic_passes": 2,
              "tokens_per_s": 34.21541500323774,
              "ttft_s": 0.203530908
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9887023955,
              "format_passes": 0,
              "gpu_energy_j": 267.0667224367967,
              "semantic_passes": 0,
              "tokens_per_s": 35.33951188480963,
              "ttft_s": 0.22460827849999998
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1474891,
              "format_passes": 0,
              "gpu_energy_j": 299.44292159950237,
              "semantic_passes": 2,
              "tokens_per_s": 35.27306733742168,
              "ttft_s": 0.3536425975
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7923254555,
              "format_passes": 2,
              "gpu_energy_j": 1024.1556452220677,
              "semantic_passes": 2,
              "tokens_per_s": 34.43361513404578,
              "ttft_s": 3.2114470080000004
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.578176121,
              "format_passes": 2,
              "gpu_energy_j": 145.12897345318228,
              "semantic_passes": 2,
              "tokens_per_s": 34.903099126830256,
              "ttft_s": 0.2056658555
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7261976925,
              "format_passes": 0,
              "gpu_energy_j": 187.87330102791864,
              "semantic_passes": 0,
              "tokens_per_s": 696.4461822811261,
              "ttft_s": 0.7260647714999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7489245689999997,
              "format_passes": 0,
              "gpu_energy_j": 737.637288479903,
              "semantic_passes": 0,
              "tokens_per_s": 745.3536356863972,
              "ttft_s": 2.748703661
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4710511985,
              "format_passes": 0,
              "gpu_energy_j": 1471.0764597322868,
              "semantic_passes": 0,
              "tokens_per_s": 748.907053232642,
              "ttft_s": 5.47072613
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.85188055,
              "format_passes": 0,
              "gpu_energy_j": 224.10468553578482,
              "semantic_passes": 2,
              "tokens_per_s": 35.0439068264498,
              "ttft_s": 0.22409937800000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9903635245,
              "format_passes": 0,
              "gpu_energy_j": 268.9146629831595,
              "semantic_passes": 2,
              "tokens_per_s": 34.885445335552205,
              "ttft_s": 0.21636682499999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0159772230000002,
              "format_passes": 0,
              "gpu_energy_j": 275.39156170635795,
              "semantic_passes": 2,
              "tokens_per_s": 35.25920759036278,
              "ttft_s": 0.22182035049999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7089789935000002,
              "format_passes": 0,
              "gpu_energy_j": 463.0721576753682,
              "semantic_passes": 0,
              "tokens_per_s": 35.0193384772394,
              "ttft_s": 1.0303311370000001
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.782996255,
              "format_passes": 0,
              "gpu_energy_j": 467.403669366763,
              "semantic_passes": 0,
              "tokens_per_s": 35.01582258729144,
              "ttft_s": 1.096402292
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
              "e2e_s": 1.7671099510000001,
              "format_passes": 2,
              "gpu_energy_j": 483.7459964538424,
              "semantic_passes": 2,
              "tokens_per_s": 35.28789158449602,
              "ttft_s": 0.520203966
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7896187525,
              "format_passes": 0,
              "gpu_energy_j": 1071.020597850164,
              "semantic_passes": 0,
              "tokens_per_s": 35.350428397535154,
              "ttft_s": 0.19661470749999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7238733335,
              "format_passes": 0,
              "gpu_energy_j": 190.44513985356335,
              "semantic_passes": 2,
              "tokens_per_s": 35.06438706301536,
              "ttft_s": 0.210443724
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9254627485,
              "format_passes": 0,
              "gpu_energy_j": 246.2757866283548,
              "semantic_passes": 0,
              "tokens_per_s": 34.94917372333254,
              "ttft_s": 0.524761085
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46821698349999996,
              "format_passes": 2,
              "gpu_energy_j": 111.28192269118603,
              "semantic_passes": 2,
              "tokens_per_s": 34.10640883163013,
              "ttft_s": 0.2043411525
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9918305585,
              "format_passes": 0,
              "gpu_energy_j": 270.8851913927309,
              "semantic_passes": 0,
              "tokens_per_s": 35.26973974625527,
              "ttft_s": 0.2262629065
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1545377655,
              "format_passes": 0,
              "gpu_energy_j": 296.3715353450823,
              "semantic_passes": 2,
              "tokens_per_s": 35.22106447813795,
              "ttft_s": 0.3595175425
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.800919246,
              "format_passes": 2,
              "gpu_energy_j": 1026.955323482393,
              "semantic_passes": 2,
              "tokens_per_s": 34.31547521990095,
              "ttft_s": 3.2180307585
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5772619725,
              "format_passes": 2,
              "gpu_energy_j": 143.47515712702858,
              "semantic_passes": 2,
              "tokens_per_s": 34.96630328149342,
              "ttft_s": 0.2054386165
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7264815505,
              "format_passes": 0,
              "gpu_energy_j": 192.59064114620463,
              "semantic_passes": 0,
              "tokens_per_s": 696.2023281451288,
              "ttft_s": 0.7263366840000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.752042465,
              "format_passes": 0,
              "gpu_energy_j": 736.8550594070036,
              "semantic_passes": 0,
              "tokens_per_s": 744.5143817381967,
              "ttft_s": 2.7518176745
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4679921195,
              "format_passes": 0,
              "gpu_energy_j": 1477.9515731098277,
              "semantic_passes": 0,
              "tokens_per_s": 749.319268071577,
              "ttft_s": 5.467682087
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.709675483,
              "format_passes": 2,
              "gpu_energy_j": 185.80247876006388,
              "semantic_passes": 2,
              "tokens_per_s": 35.05071556145312,
              "ttft_s": 0.2246266765
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9881128365,
              "format_passes": 0,
              "gpu_energy_j": 263.31009651571287,
              "semantic_passes": 2,
              "tokens_per_s": 35.0276768191664,
              "ttft_s": 0.2172137885
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0189123155000002,
              "format_passes": 0,
              "gpu_energy_j": 278.10954414827836,
              "semantic_passes": 2,
              "tokens_per_s": 35.2246892251117,
              "ttft_s": 0.22401037750000002
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7109314045000001,
              "format_passes": 0,
              "gpu_energy_j": 462.9832101082731,
              "semantic_passes": 0,
              "tokens_per_s": 34.96588718741067,
              "ttft_s": 1.031268308
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7810734815,
              "format_passes": 0,
              "gpu_energy_j": 470.6083852107197,
              "semantic_passes": 0,
              "tokens_per_s": 35.00728953964031,
              "ttft_s": 1.0956110585
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
            "e2e_change_pct": 0.21626182860017273,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.30745797264504215,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3412401040013613,
            "ttft_change_pct": -0.08344409350605764
          },
          "decode": {
            "e2e_change_pct": 0.06318656894943597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3910164584098208,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.025495379281548214,
            "ttft_change_pct": 0.5911662846436627
          },
          "energy": {
            "e2e_change_pct": 24.499792992335266,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 30.288243634908962,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3765494342916842,
            "ttft_change_pct": 0.5667820406828561
          },
          "filtering": {
            "e2e_change_pct": 0.13819789856950315,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5340550912132258,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2338468879887312,
            "ttft_change_pct": 0.05519793767665426
          },
          "german": {
            "e2e_change_pct": 0.34098162687612454,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1214815137321255,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.31858789845833346,
            "ttft_change_pct": 0.3980940821037393
          },
          "ha_sim": {
            "e2e_change_pct": 0.3163907576473557,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4297808881216678,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19743379246942583,
            "ttft_change_pct": 0.7366727580346177
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.6142686235538042,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0257000693200458,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1474293652612424,
            "ttft_change_pct": 1.661266216663848
          },
          "long_context": {
            "e2e_change_pct": 0.2266100470764254,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2733645294429987,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.34309471626761123,
            "ttft_change_pct": 0.2050088475257006
          },
          "math": {
            "e2e_change_pct": -0.15810900291401975,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1395493861790507,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.18108464934156743,
            "ttft_change_pct": -0.11048941470986895
          },
          "prefill": {
            "e2e_change_pct": 0.039088254194630245,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.510915650321688,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03501406744718105,
            "ttft_change_pct": 0.03745017120695415
          },
          "prefill2048": {
            "e2e_change_pct": 0.11342239198417481,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.10604521830930302,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11259808874852784,
            "ttft_change_pct": 0.11329025912043544
          },
          "prefill4096": {
            "e2e_change_pct": -0.05591391652189914,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4673525520755062,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.055042189435328126,
            "ttft_change_pct": -0.05564239422088946
          },
          "pve_sim": {
            "e2e_change_pct": -16.693075924787802,
            "format_pass_change": 2,
            "gpu_energy_change_pct": -17.09121194148566,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01942915507975318,
            "ttft_change_pct": 0.23529672625863807
          },
          "sorting": {
            "e2e_change_pct": -0.22725877360398883,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.0841431275161026,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4077100987134319,
            "ttft_change_pct": 0.3914479495643608
          },
          "time": {
            "e2e_change_pct": 0.2888935335905618,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9869519694356121,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0978988684377291,
            "ttft_change_pct": 0.9872976014434931
          },
          "tool-call": {
            "e2e_change_pct": 0.11424429483486431,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.019208144048565856,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1526336365933023,
            "ttft_change_pct": 0.09095823336258135
          },
          "tool-final": {
            "e2e_change_pct": -0.10783945813728213,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6856419951299042,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.024369119502631875,
            "ttft_change_pct": -0.07216634859059656
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 350729406620287,
          "end_ns": 350730068133785,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 350831277514193,
          "end_ns": 350831934067322,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
