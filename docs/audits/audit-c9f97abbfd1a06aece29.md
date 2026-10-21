# Public audit excerpt

Original SHA256: `c9f97abbfd1a06aece29ca046780d656f05801945252997ba27dd0ac06a4aadf`

Original file: `RESULTS.json`; 39899 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.763495475,
              "format_passes": 2,
              "gpu_energy_j": 482.229088813839,
              "semantic_passes": 2,
              "tokens_per_s": 35.38596879639786,
              "ttft_s": 0.520056812
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7849572609999997,
              "format_passes": 0,
              "gpu_energy_j": 1069.0911223407181,
              "semantic_passes": 0,
              "tokens_per_s": 35.38269027325393,
              "ttft_s": 0.195908706
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5822195605,
              "format_passes": 2,
              "gpu_energy_j": 146.8162570635301,
              "semantic_passes": 2,
              "tokens_per_s": 34.92387218158116,
              "ttft_s": 0.20994165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9246695865000001,
              "format_passes": 0,
              "gpu_energy_j": 244.24563688988013,
              "semantic_passes": 0,
              "tokens_per_s": 35.0370862687667,
              "ttft_s": 0.52504101
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46574187899999997,
              "format_passes": 2,
              "gpu_energy_j": 107.42755077291646,
              "semantic_passes": 2,
              "tokens_per_s": 34.279581192288155,
              "ttft_s": 0.20320443049999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.990850819,
              "format_passes": 0,
              "gpu_energy_j": 265.2872012677957,
              "semantic_passes": 0,
              "tokens_per_s": 35.298878431606425,
              "ttft_s": 0.225906981
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1453300345,
              "format_passes": 0,
              "gpu_energy_j": 295.82352881274466,
              "semantic_passes": 2,
              "tokens_per_s": 35.346691592188535,
              "ttft_s": 0.353174398
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.795878589,
              "format_passes": 2,
              "gpu_energy_j": 1017.2586436008439,
              "semantic_passes": 2,
              "tokens_per_s": 34.36426106510673,
              "ttft_s": 3.2137765270000003
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5747591715,
              "format_passes": 2,
              "gpu_energy_j": 145.85248665818443,
              "semantic_passes": 2,
              "tokens_per_s": 34.965305928473626,
              "ttft_s": 0.202914213
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.725487232,
              "format_passes": 0,
              "gpu_energy_j": 187.77970961901553,
              "semantic_passes": 0,
              "tokens_per_s": 697.1359879440199,
              "ttft_s": 0.7253056635
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7526127215000002,
              "format_passes": 0,
              "gpu_energy_j": 732.4467462386834,
              "semantic_passes": 0,
              "tokens_per_s": 744.3665937393889,
              "ttft_s": 2.7523291445
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4714728515,
              "format_passes": 0,
              "gpu_energy_j": 1470.153484426685,
              "semantic_passes": 0,
              "tokens_per_s": 748.845352641001,
              "ttft_s": 5.4711131625
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8462768665,
              "format_passes": 0,
              "gpu_energy_j": 221.57145848704207,
              "semantic_passes": 2,
              "tokens_per_s": 35.28327838666242,
              "ttft_s": 0.22269040699999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9860708140000001,
              "format_passes": 0,
              "gpu_energy_j": 261.07492911333185,
              "semantic_passes": 2,
              "tokens_per_s": 35.09871838980145,
              "ttft_s": 0.216797652
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0152395865,
              "format_passes": 0,
              "gpu_energy_j": 272.3204206379075,
              "semantic_passes": 2,
              "tokens_per_s": 35.27778514921644,
              "ttft_s": 0.2214865525
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7100494585,
              "format_passes": 0,
              "gpu_energy_j": 459.64858216668995,
              "semantic_passes": 0,
              "tokens_per_s": 34.998818523012446,
              "ttft_s": 1.030748768
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7791143095000002,
              "format_passes": 0,
              "gpu_energy_j": 468.1092052618221,
              "semantic_passes": 0,
              "tokens_per_s": 35.07513050023317,
              "ttft_s": 1.0947841165
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
              "e2e_s": 1.764476915,
              "format_passes": 2,
              "gpu_energy_j": 483.6860130496202,
              "semantic_passes": 2,
              "tokens_per_s": 35.3529936164528,
              "ttft_s": 0.5198445045
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.785541463,
              "format_passes": 0,
              "gpu_energy_j": 1071.2233241070203,
              "semantic_passes": 0,
              "tokens_per_s": 35.3539017091631,
              "ttft_s": 0.1939296445
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5806419279999999,
              "format_passes": 2,
              "gpu_energy_j": 150.85982322630412,
              "semantic_passes": 2,
              "tokens_per_s": 34.96183505485139,
              "ttft_s": 0.2087859835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9262548239999999,
              "format_passes": 0,
              "gpu_energy_j": 245.01604291443613,
              "semantic_passes": 0,
              "tokens_per_s": 34.97917398430428,
              "ttft_s": 0.5259719885
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46730859599999997,
              "format_passes": 2,
              "gpu_energy_j": 110.48848931506726,
              "semantic_passes": 2,
              "tokens_per_s": 34.171485469234405,
              "ttft_s": 0.203849477
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9899322269999999,
              "format_passes": 0,
              "gpu_energy_j": 268.6218447093163,
              "semantic_passes": 0,
              "tokens_per_s": 35.24992761148173,
              "ttft_s": 0.2238843225
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.149275613,
              "format_passes": 0,
              "gpu_energy_j": 296.1753092233207,
              "semantic_passes": 2,
              "tokens_per_s": 35.320868038785335,
              "ttft_s": 0.35653718749999996
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.803533561,
              "format_passes": 2,
              "gpu_energy_j": 1032.136583471786,
              "semantic_passes": 2,
              "tokens_per_s": 34.28903453794172,
              "ttft_s": 3.220226798
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.576163651,
              "format_passes": 2,
              "gpu_energy_j": 146.65232663640847,
              "semantic_passes": 2,
              "tokens_per_s": 34.83622966796872,
              "ttft_s": 0.202948801
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.727588637,
              "format_passes": 0,
              "gpu_energy_j": 189.40954671715906,
              "semantic_passes": 0,
              "tokens_per_s": 695.1339205799238,
              "ttft_s": 0.72739793
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.754306217,
              "format_passes": 0,
              "gpu_energy_j": 736.4004858835646,
              "semantic_passes": 0,
              "tokens_per_s": 743.9030832341546,
              "ttft_s": 2.754076096
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.473349056,
              "format_passes": 0,
              "gpu_energy_j": 1481.1567386700103,
              "semantic_passes": 0,
              "tokens_per_s": 748.5878745722769,
              "ttft_s": 5.4730001375
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8478451665,
              "format_passes": 0,
              "gpu_energy_j": 227.25592922874534,
              "semantic_passes": 2,
              "tokens_per_s": 35.24560878627381,
              "ttft_s": 0.223630761
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986515958,
              "format_passes": 0,
              "gpu_energy_j": 270.89420342173406,
              "semantic_passes": 2,
              "tokens_per_s": 35.05694856911742,
              "ttft_s": 0.216334983
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0157235095,
              "format_passes": 0,
              "gpu_energy_j": 274.71352220714203,
              "semantic_passes": 2,
              "tokens_per_s": 35.22810211683251,
              "ttft_s": 0.22086122400000002
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.707815338,
              "format_passes": 0,
              "gpu_energy_j": 460.2312009668926,
              "semantic_passes": 0,
              "tokens_per_s": 34.98260410540339,
              "ttft_s": 1.0288943145
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7820665645,
              "format_passes": 0,
              "gpu_energy_j": 468.4828426815045,
              "semantic_passes": 0,
              "tokens_per_s": 35.01743178486745,
              "ttft_s": 1.096210202
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
            "e2e_change_pct": 0.05565310565935899,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.30212284359802943,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09318716165379604,
            "ttft_change_pct": -0.04082390521595869
          },
          "decode": {
            "e2e_change_pct": 0.015434837429206816,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1994406016237349,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08136341207665154,
            "ttft_change_pct": -1.0101957898695835
          },
          "energy": {
            "e2e_change_pct": -0.27096865289878425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.7541678582803764,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10870178734148084,
            "ttft_change_pct": -0.5504703330663552
          },
          "filtering": {
            "e2e_change_pct": 0.17143826542409535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.315422635329754,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16528852889814427,
            "ttft_change_pct": 0.17731538723042561
          },
          "german": {
            "e2e_change_pct": 0.3363916947653367,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8493049689097827,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3153356000687335,
            "ttft_change_pct": 0.3174372224133304
          },
          "ha_sim": {
            "e2e_change_pct": -0.09270739675294459,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2569937130719078,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1386752845973227,
            "ttft_change_pct": -0.895350152990626
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.34449271224450406,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11891562918875387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07305790793983302,
            "ttft_change_pct": 0.9521611756240445
          },
          "long_context": {
            "e2e_change_pct": 0.2016653541602631,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4625523178921185,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21890919470810566,
            "ttft_change_pct": 0.20070689252376095
          },
          "math": {
            "e2e_change_pct": 0.24435965003126725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5483896754523876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3691552442553925,
            "ttft_change_pct": 0.017045627060152668
          },
          "prefill": {
            "e2e_change_pct": 0.2896543050395106,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.86795165539999,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2871846237633702,
            "ttft_change_pct": 0.28846686373626973
          },
          "prefill2048": {
            "e2e_change_pct": 0.06152320254759758,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5397989226090028,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.062269117009383645,
            "ttft_change_pct": 0.06347175095284818
          },
          "prefill4096": {
            "e2e_change_pct": 0.03429066635112221,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7484425510589698,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03438334334533444,
            "ttft_change_pct": 0.03448978195028651
          },
          "pve_sim": {
            "e2e_change_pct": 0.18531760255791063,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.565524811055808,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10676332277230749,
            "ttft_change_pct": 0.42226964900200503
          },
          "sorting": {
            "e2e_change_pct": 0.045143208142861546,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7610943117941886,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11900668343539644,
            "ttft_change_pct": -0.21341052162318075
          },
          "time": {
            "e2e_change_pct": 0.04766589152302991,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8787815337640614,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14083376315656704,
            "ttft_change_pct": -0.28233249059216314
          },
          "tool-call": {
            "e2e_change_pct": -0.13064654293446498,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1267530941695183,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04632847134080631,
            "ttft_change_pct": -0.17991323953734373
          },
          "tool-final": {
            "e2e_change_pct": 0.16593959051622864,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07981843028987967,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16450035835317012,
            "ttft_change_pct": 0.13026180034096946
          }
        }
      },
      "complete": true
    }
  }
}
```
