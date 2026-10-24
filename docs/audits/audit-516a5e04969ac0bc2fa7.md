# Public audit excerpt

Original SHA256: `516a5e04969ac0bc2fa7161c5ac0d58004a70170bedba154840f71e2aa2f7cb4`

Original file: `RESULTS.json`; 39579 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5267605335,
              "format_passes": 2,
              "gpu_energy_j": 132.30681265328982,
              "semantic_passes": 2,
              "tokens_per_s": 96.52119298719609,
              "ttft_s": 0.133001712
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3666715520000001,
              "format_passes": 0,
              "gpu_energy_j": 356.3330041078433,
              "semantic_passes": 0,
              "tokens_per_s": 97.05154552175055,
              "ttft_s": 0.058040818499999994
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20526612449999998,
              "format_passes": 2,
              "gpu_energy_j": 46.3867575416639,
              "semantic_passes": 2,
              "tokens_per_s": 94.86441880159023,
              "ttft_s": 0.068156567
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2297845255,
              "format_passes": 0,
              "gpu_energy_j": 52.873487168555236,
              "semantic_passes": 0,
              "tokens_per_s": 93.97264410134136,
              "ttft_s": 0.133989256
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1567111865,
              "format_passes": 2,
              "gpu_energy_j": 33.28201077412903,
              "semantic_passes": 2,
              "tokens_per_s": 94.04080496496067,
              "ttft_s": 0.0609496825
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3065482465,
              "format_passes": 0,
              "gpu_energy_j": 72.95400567513545,
              "semantic_passes": 0,
              "tokens_per_s": 95.87772292543036,
              "ttft_s": 0.0770734575
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3982550675,
              "format_passes": 0,
              "gpu_energy_j": 92.76419167694377,
              "semantic_passes": 2,
              "tokens_per_s": 96.21576354181389,
              "ttft_s": 0.10720597
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0317887940000001,
              "format_passes": 2,
              "gpu_energy_j": 276.3424475780391,
              "semantic_passes": 2,
              "tokens_per_s": 94.24829741935602,
              "ttft_s": 0.8725782915
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14921200350000002,
              "format_passes": 0,
              "gpu_energy_j": 31.215111656076928,
              "semantic_passes": 0,
              "tokens_per_s": 93.33826017055077,
              "ttft_s": 0.06349112400000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2061916875,
              "format_passes": 0,
              "gpu_energy_j": 51.256004163873385,
              "semantic_passes": 0,
              "tokens_per_s": 2462.5301828705683,
              "ttft_s": 0.20598538300000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7561524215,
              "format_passes": 0,
              "gpu_energy_j": 198.39494675060163,
              "semantic_passes": 0,
              "tokens_per_s": 2712.9421147561175,
              "ttft_s": 0.755890435
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5001669625,
              "format_passes": 0,
              "gpu_energy_j": 405.8189752095495,
              "semantic_passes": 0,
              "tokens_per_s": 2733.524657047397,
              "ttft_s": 1.499764135
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254308946,
              "format_passes": 2,
              "gpu_energy_j": 58.83657118797066,
              "semantic_passes": 2,
              "tokens_per_s": 95.5962217515765,
              "ttft_s": 0.076455123
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351371439,
              "format_passes": 0,
              "gpu_energy_j": 82.51325511655824,
              "semantic_passes": 2,
              "tokens_per_s": 95.96949298643483,
              "ttft_s": 0.0699872735
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314610944,
              "format_passes": 0,
              "gpu_energy_j": 75.63326869301578,
              "semantic_passes": 0,
              "tokens_per_s": 95.91746103353312,
              "ttft_s": 0.074789475
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.551506627,
              "format_passes": 0,
              "gpu_energy_j": 141.86157009776673,
              "semantic_passes": 0,
              "tokens_per_s": 96.02793551648097,
              "ttft_s": 0.304809397
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524828018,
              "format_passes": 0,
              "gpu_energy_j": 133.0648417789215,
              "semantic_passes": 0,
              "tokens_per_s": 95.70910784747996,
              "ttft_s": 0.274444691
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5285907400000001,
              "format_passes": 2,
              "gpu_energy_j": 135.3178638956295,
              "semantic_passes": 2,
              "tokens_per_s": 95.90517573229911,
              "ttft_s": 0.1323425505
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.36709479,
              "format_passes": 0,
              "gpu_energy_j": 353.7454511261881,
              "semantic_passes": 0,
              "tokens_per_s": 97.00684302008713,
              "ttft_s": 0.058191864499999996
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20492076250000002,
              "format_passes": 2,
              "gpu_energy_j": 46.23422165580102,
              "semantic_passes": 2,
              "tokens_per_s": 94.90181315392653,
              "ttft_s": 0.0679151425
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2295144575,
              "format_passes": 0,
              "gpu_energy_j": 55.95740721730529,
              "semantic_passes": 0,
              "tokens_per_s": 94.06611519252631,
              "ttft_s": 0.133844295
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1568623975,
              "format_passes": 2,
              "gpu_energy_j": 32.870836571947635,
              "semantic_passes": 2,
              "tokens_per_s": 93.74295575528222,
              "ttft_s": 0.0608481665
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30941673199999997,
              "format_passes": 0,
              "gpu_energy_j": 72.22900052526171,
              "semantic_passes": 0,
              "tokens_per_s": 95.08203602330522,
              "ttft_s": 0.078040323
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39802724,
              "format_passes": 0,
              "gpu_energy_j": 97.36624014624542,
              "semantic_passes": 2,
              "tokens_per_s": 96.27583731588362,
              "ttft_s": 0.107165944
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.03287859,
              "format_passes": 2,
              "gpu_energy_j": 275.0710132973216,
              "semantic_passes": 2,
              "tokens_per_s": 94.12768898006149,
              "ttft_s": 0.8735053100000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1484885645,
              "format_passes": 0,
              "gpu_energy_j": 30.700026791201005,
              "semantic_passes": 0,
              "tokens_per_s": 93.78983068768338,
              "ttft_s": 0.06318325
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206003,
              "format_passes": 0,
              "gpu_energy_j": 49.126092486594274,
              "semantic_passes": 0,
              "tokens_per_s": 2464.3404230733745,
              "ttft_s": 0.20581403599999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7565695505,
              "format_passes": 0,
              "gpu_energy_j": 204.54075369058327,
              "semantic_passes": 0,
              "tokens_per_s": 2711.4479589341463,
              "ttft_s": 0.756341808
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5012457345,
              "format_passes": 0,
              "gpu_energy_j": 405.56227973504417,
              "semantic_passes": 0,
              "tokens_per_s": 2731.572664331513,
              "ttft_s": 1.500874563
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254106068,
              "format_passes": 2,
              "gpu_energy_j": 59.23622440524908,
              "semantic_passes": 2,
              "tokens_per_s": 95.60769347504794,
              "ttft_s": 0.07625596400000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3516939865,
              "format_passes": 0,
              "gpu_energy_j": 83.09287790686393,
              "semantic_passes": 2,
              "tokens_per_s": 96.00135591157526,
              "ttft_s": 0.0704336905
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3152013365,
              "format_passes": 0,
              "gpu_energy_j": 75.24492150859638,
              "semantic_passes": 0,
              "tokens_per_s": 95.87368177464609,
              "ttft_s": 0.0752425725
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550629013,
              "format_passes": 0,
              "gpu_energy_j": 137.8326885090425,
              "semantic_passes": 0,
              "tokens_per_s": 96.17880725054917,
              "ttft_s": 0.303811314
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524235421,
              "format_passes": 0,
              "gpu_energy_j": 130.07857537919182,
              "semantic_passes": 0,
              "tokens_per_s": 95.9037155040038,
              "ttft_s": 0.27380446449999996
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
            "e2e_change_pct": 0.3474456386926894,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.275809674464857,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6382196860938993,
            "ttft_change_pct": -0.49560377087477514
          },
          "decode": {
            "e2e_change_pct": 0.03096852344517398,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7261614702611441,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04606057680287545,
            "ttft_change_pct": 0.260240988848226
          },
          "energy": {
            "e2e_change_pct": -0.16825085037349696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3288349821085723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03941873339730062,
            "ttft_change_pct": -0.35422045244738465
          },
          "filtering": {
            "e2e_change_pct": -0.11753097795090817,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.832639785832239,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09946627774370942,
            "ttft_change_pct": -0.10818852520533273
          },
          "german": {
            "e2e_change_pct": 0.09649024002509332,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.235424761357895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3167233732095598,
            "ttft_change_pct": -0.16655706122832292
          },
          "ha_sim": {
            "e2e_change_pct": 0.9357370439240009,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9937838822753453,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8298975797996322,
            "ttft_change_pct": 1.254472721688904
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.05720642839026624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.961018240021464,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06243651960795571,
            "ttft_change_pct": -0.03733560733604202
          },
          "long_context": {
            "e2e_change_pct": 0.10562200387687071,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4600937322010501,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1279688255352629,
            "ttft_change_pct": 0.10623900560333688
          },
          "math": {
            "e2e_change_pct": -0.48483967980499365,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6501137992106063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4838000154572031,
            "ttft_change_pct": -0.48490872519443284
          },
          "prefill": {
            "e2e_change_pct": -0.09151072106143854,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.155438395996402,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07351139147038221,
            "ttft_change_pct": -0.08318405777367754
          },
          "prefill2048": {
            "e2e_change_pct": 0.055164671584662095,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.097763849654611,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05507510882167832,
            "ttft_change_pct": 0.05971407747737967
          },
          "prefill4096": {
            "e2e_change_pct": 0.07191012913672079,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.0632536894985658,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07140936924975305,
            "ttft_change_pct": 0.07404017565735277
          },
          "pve_sim": {
            "e2e_change_pct": -0.0797761947391229,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.679259870534632,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.012000185008620434,
            "ttft_change_pct": -0.2604913734819192
          },
          "sorting": {
            "e2e_change_pct": 0.09179673251700216,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7024602162245541,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03320109771229873,
            "ttft_change_pct": 0.637854537939675
          },
          "time": {
            "e2e_change_pct": 0.18765796653277267,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5134607972526517,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.045642637341836156,
            "ttft_change_pct": 0.6058305663998897
          },
          "tool-call": {
            "e2e_change_pct": -0.15913027278998682,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8400091624163237,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15711233742217168,
            "ttft_change_pct": -0.3274449573482108
          },
          "tool-final": {
            "e2e_change_pct": -0.11291260749726195,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.244218953561883,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2033324318872154,
            "ttft_change_pct": -0.23328070135635315
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
