# Public audit excerpt

Original SHA256: `0addd2dae251fd75a1760deb03c46fd8080361d621531856bba3c90a58d51255`

Original file: `RESULTS.json`; 39562 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 0.5259399220000001,
              "format_passes": 2,
              "gpu_energy_j": 133.17910111701582,
              "semantic_passes": 2,
              "tokens_per_s": 96.51693004533513,
              "ttft_s": 0.132179135
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3666446360000002,
              "format_passes": 0,
              "gpu_energy_j": 351.60186691863794,
              "semantic_passes": 0,
              "tokens_per_s": 97.03916030562584,
              "ttft_s": 0.057803996499999996
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204923185,
              "format_passes": 2,
              "gpu_energy_j": 46.90036323505564,
              "semantic_passes": 2,
              "tokens_per_s": 95.16489220977685,
              "ttft_s": 0.06828042200000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.232589013,
              "format_passes": 0,
              "gpu_energy_j": 55.18384805589195,
              "semantic_passes": 0,
              "tokens_per_s": 92.19280897988355,
              "ttft_s": 0.134893737
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157373389,
              "format_passes": 2,
              "gpu_energy_j": 33.559553834538946,
              "semantic_passes": 2,
              "tokens_per_s": 93.95888379486647,
              "ttft_s": 0.061582124
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30656277249999997,
              "format_passes": 0,
              "gpu_energy_j": 72.21645617496509,
              "semantic_passes": 0,
              "tokens_per_s": 95.97911130578325,
              "ttft_s": 0.07731112500000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39803171299999995,
              "format_passes": 0,
              "gpu_energy_j": 97.315707566257,
              "semantic_passes": 2,
              "tokens_per_s": 96.33419261999127,
              "ttft_s": 0.107339024
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0317103300000001,
              "format_passes": 2,
              "gpu_energy_j": 268.6953263460987,
              "semantic_passes": 2,
              "tokens_per_s": 94.15605250144088,
              "ttft_s": 0.8723928355
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14870451299999998,
              "format_passes": 0,
              "gpu_energy_j": 30.242720986063794,
              "semantic_passes": 0,
              "tokens_per_s": 93.86995831695828,
              "ttft_s": 0.06346558
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20572500700000002,
              "format_passes": 0,
              "gpu_energy_j": 50.90295898568738,
              "semantic_passes": 0,
              "tokens_per_s": 2467.6169072842195,
              "ttft_s": 0.2055781895
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7539562035,
              "format_passes": 0,
              "gpu_energy_j": 198.83795725153092,
              "semantic_passes": 0,
              "tokens_per_s": 2720.846319815102,
              "ttft_s": 0.7537067845000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4955961675,
              "format_passes": 0,
              "gpu_energy_j": 405.0581732554929,
              "semantic_passes": 0,
              "tokens_per_s": 2741.8546288330554,
              "ttft_s": 1.495297512
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25414164650000004,
              "format_passes": 2,
              "gpu_energy_j": 57.458538915026125,
              "semantic_passes": 2,
              "tokens_per_s": 95.68438667272275,
              "ttft_s": 0.076453879
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35219586049999996,
              "format_passes": 0,
              "gpu_energy_j": 85.41730226729308,
              "semantic_passes": 2,
              "tokens_per_s": 95.77196262999831,
              "ttft_s": 0.0701911665
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314648519,
              "format_passes": 0,
              "gpu_energy_j": 72.32316658756335,
              "semantic_passes": 0,
              "tokens_per_s": 95.93615156144378,
              "ttft_s": 0.0748600165
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5505087735,
              "format_passes": 0,
              "gpu_energy_j": 138.62994413621772,
              "semantic_passes": 0,
              "tokens_per_s": 96.22675183066353,
              "ttft_s": 0.303573014
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524500312,
              "format_passes": 0,
              "gpu_energy_j": 131.02264021264844,
              "semantic_passes": 0,
              "tokens_per_s": 95.87844535011409,
              "ttft_s": 0.2740270325
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
              "e2e_s": 0.5265237785,
              "format_passes": 2,
              "gpu_energy_j": 131.52567363614543,
              "semantic_passes": 2,
              "tokens_per_s": 96.41859379013783,
              "ttft_s": 0.1323875125
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3663734650000001,
              "format_passes": 0,
              "gpu_energy_j": 352.5173719509386,
              "semantic_passes": 0,
              "tokens_per_s": 97.07368734019124,
              "ttft_s": 0.058090461999999995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2046409215,
              "format_passes": 2,
              "gpu_energy_j": 44.43230701426444,
              "semantic_passes": 2,
              "tokens_per_s": 95.16724890084393,
              "ttft_s": 0.0679821375
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229567565,
              "format_passes": 0,
              "gpu_energy_j": 53.6866715607738,
              "semantic_passes": 0,
              "tokens_per_s": 94.18467927370718,
              "ttft_s": 0.1339989695
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156962977,
              "format_passes": 2,
              "gpu_energy_j": 31.56300392863654,
              "semantic_passes": 2,
              "tokens_per_s": 93.98686747334338,
              "ttft_s": 0.061159683500000006
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30684131950000004,
              "format_passes": 0,
              "gpu_energy_j": 71.45741064019103,
              "semantic_passes": 0,
              "tokens_per_s": 95.91197659551548,
              "ttft_s": 0.077421247
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3981567525,
              "format_passes": 0,
              "gpu_energy_j": 88.5362204124855,
              "semantic_passes": 2,
              "tokens_per_s": 96.31397862620145,
              "ttft_s": 0.1073833315
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0311662985,
              "format_passes": 2,
              "gpu_energy_j": 274.61909256048176,
              "semantic_passes": 2,
              "tokens_per_s": 94.1269594030164,
              "ttft_s": 0.871737524
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149792627,
              "format_passes": 0,
              "gpu_energy_j": 32.582370985377665,
              "semantic_passes": 0,
              "tokens_per_s": 92.99145804337232,
              "ttft_s": 0.0637350615
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20616345200000002,
              "format_passes": 0,
              "gpu_energy_j": 50.79757451895304,
              "semantic_passes": 0,
              "tokens_per_s": 2461.79613226081,
              "ttft_s": 0.2059900895
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.75523976,
              "format_passes": 0,
              "gpu_energy_j": 197.79048249807266,
              "semantic_passes": 0,
              "tokens_per_s": 2716.1327228802347,
              "ttft_s": 0.755013655
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.493063904,
              "format_passes": 0,
              "gpu_energy_j": 402.6917319308136,
              "semantic_passes": 0,
              "tokens_per_s": 2746.537627972295,
              "ttft_s": 1.4927390095000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25439030949999997,
              "format_passes": 2,
              "gpu_energy_j": 56.73958721862188,
              "semantic_passes": 2,
              "tokens_per_s": 95.52926762468165,
              "ttft_s": 0.0764186945
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35164226200000004,
              "format_passes": 0,
              "gpu_energy_j": 82.16648621291533,
              "semantic_passes": 2,
              "tokens_per_s": 96.2412503743355,
              "ttft_s": 0.0710498315
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31483567749999997,
              "format_passes": 0,
              "gpu_energy_j": 73.70777770201312,
              "semantic_passes": 0,
              "tokens_per_s": 95.96691419877826,
              "ttft_s": 0.075156907
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5499018010000001,
              "format_passes": 0,
              "gpu_energy_j": 137.7908034623105,
              "semantic_passes": 0,
              "tokens_per_s": 96.21007358872166,
              "ttft_s": 0.302704264
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5247827890000001,
              "format_passes": 0,
              "gpu_energy_j": 131.70220564281402,
              "semantic_passes": 0,
              "tokens_per_s": 95.85603251215275,
              "ttft_s": 0.2744005895
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
            "e2e_change_pct": 0.1110120140299875,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2415067131423485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10188498033568694,
            "ttft_change_pct": 0.1576478012206728
          },
          "decode": {
            "e2e_change_pct": -0.019842100342470914,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2603811635939035,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.035580516625088876,
            "ttft_change_pct": 0.49558078566418473
          },
          "energy": {
            "e2e_change_pct": -0.1377411248024596,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.262339245480419,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0024764290825762814,
            "ttft_change_pct": -0.436852162395851
          },
          "filtering": {
            "e2e_change_pct": -1.2990501834237556,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.713070124435246,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.1605484374147332,
            "ttft_change_pct": -0.6633128564004442
          },
          "german": {
            "e2e_change_pct": -0.26078869026580076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.949274283401196,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.029782897951413645,
            "ttft_change_pct": -0.6859791000388249
          },
          "ha_sim": {
            "e2e_change_pct": 0.09086132596223262,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0510700399574469,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06994720971512658,
            "ttft_change_pct": 0.14244004339607486
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.031414456666678525,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.021654749613795,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.020983197388246833,
            "ttft_change_pct": 0.041278090995122696
          },
          "long_context": {
            "e2e_change_pct": -0.052731031587138766,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2046405849102335,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.030898808575308134,
            "ttft_change_pct": -0.07511656140830603
          },
          "math": {
            "e2e_change_pct": 0.731728969113421,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.73624172372589,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9358694616861785,
            "ttft_change_pct": 0.4246104738978129
          },
          "prefill": {
            "e2e_change_pct": 0.21312187876119104,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.20703013898262235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23588649462674693,
            "ttft_change_pct": 0.20036172173798494
          },
          "prefill2048": {
            "e2e_change_pct": 0.1702428462079686,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5267981867934757,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1732401018219809,
            "ttft_change_pct": 0.173392428843111
          },
          "prefill4096": {
            "e2e_change_pct": -0.16931465558867043,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5842225835513859,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17079676982119096,
            "ttft_change_pct": -0.17110324062385995
          },
          "pve_sim": {
            "e2e_change_pct": 0.09784425473922109,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2512530077861572,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16211531832426296,
            "ttft_change_pct": -0.04602055573924568
          },
          "sorting": {
            "e2e_change_pct": -0.15718484005291522,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.805805109841909,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.49000535381134025,
            "ttft_change_pct": 1.2233234505370394
          },
          "time": {
            "e2e_change_pct": 0.05948176733669985,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9144780016972618,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03206574042609045,
            "ttft_change_pct": 0.3965942219635865
          },
          "tool-call": {
            "e2e_change_pct": -0.11025664425672321,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6053098261964873,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01733222999278361,
            "ttft_change_pct": -0.2861749760141641
          },
          "tool-final": {
            "e2e_change_pct": 0.05385640266313274,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5186625983590654,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.023376305153355315,
            "ttft_change_pct": 0.13632122225022414
          }
        }
      },
      "complete": true
    }
  }
}
```
