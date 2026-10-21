# Public audit excerpt

Original SHA256: `1ba196656dca95fc603fe5df7c08730489c8158efc53c16630e340147fca2f8b`

Original file: `RESULTS.json`; 42693 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6661799825,
              "format_passes": 2,
              "gpu_energy_j": 179.35468415805434,
              "semantic_passes": 2,
              "tokens_per_s": 79.28263294627604,
              "ttft_s": 0.1237736985
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658558589,
              "format_passes": 0,
              "gpu_energy_j": 456.7423952607521,
              "semantic_passes": 0,
              "tokens_per_s": 79.60311303452357,
              "ttft_s": 0.063164758
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2380333895,
              "format_passes": 2,
              "gpu_energy_j": 60.1122136489432,
              "semantic_passes": 2,
              "tokens_per_s": 78.249860826978,
              "ttft_s": 0.07185831749999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2414330945,
              "format_passes": 0,
              "gpu_energy_j": 60.15967310318214,
              "semantic_passes": 0,
              "tokens_per_s": 77.62941776759308,
              "ttft_s": 0.1254719355
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.181991661,
              "format_passes": 2,
              "gpu_energy_j": 42.77270975808614,
              "semantic_passes": 2,
              "tokens_per_s": 77.46233111112942,
              "ttft_s": 0.0657944835
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3575382915,
              "format_passes": 0,
              "gpu_energy_j": 90.16898593497274,
              "semantic_passes": 0,
              "tokens_per_s": 78.90185421000076,
              "ttft_s": 0.0786766625
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4694142995,
              "format_passes": 0,
              "gpu_energy_j": 116.82362356743677,
              "semantic_passes": 2,
              "tokens_per_s": 78.94214891821923,
              "ttft_s": 0.114659115
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0818971524999998,
              "format_passes": 2,
              "gpu_energy_j": 288.77633287904484,
              "semantic_passes": 2,
              "tokens_per_s": 77.72949080091685,
              "ttft_s": 0.8245669185
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23400943400000002,
              "format_passes": 0,
              "gpu_energy_j": 58.00744844822911,
              "semantic_passes": 0,
              "tokens_per_s": 78.13065293676499,
              "ttft_s": 0.0675893365
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1989930505,
              "format_passes": 0,
              "gpu_energy_j": 48.2409511745451,
              "semantic_passes": 0,
              "tokens_per_s": 2551.588911761717,
              "ttft_s": 0.1988398985
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.718342424,
              "format_passes": 0,
              "gpu_energy_j": 189.73655410373334,
              "semantic_passes": 0,
              "tokens_per_s": 2855.7405237181274,
              "ttft_s": 0.718111076
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4206916015000002,
              "format_passes": 0,
              "gpu_energy_j": 382.95171915778826,
              "semantic_passes": 0,
              "tokens_per_s": 2886.433800260408,
              "ttft_s": 1.420380979
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2956523385,
              "format_passes": 2,
              "gpu_energy_j": 72.68450315867403,
              "semantic_passes": 2,
              "tokens_per_s": 78.55360229645922,
              "ttft_s": 0.079196349
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3527337535,
              "format_passes": 2,
              "gpu_energy_j": 84.05255168250085,
              "semantic_passes": 2,
              "tokens_per_s": 78.85304933413812,
              "ttft_s": 0.0736877455
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36952293,
              "format_passes": 2,
              "gpu_energy_j": 92.71864294620313,
              "semantic_passes": 2,
              "tokens_per_s": 78.71460668280906,
              "ttft_s": 0.0772902045
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196088049999999,
              "format_passes": 0,
              "gpu_energy_j": 162.9877823013293,
              "semantic_passes": 0,
              "tokens_per_s": 79.06475974655368,
              "ttft_s": 0.31860208300000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5618493865,
              "format_passes": 0,
              "gpu_energy_j": 146.91599934099588,
              "semantic_passes": 0,
              "tokens_per_s": 78.74739882515533,
              "ttft_s": 0.25694392450000003
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
              "e2e_s": 0.666288106,
              "format_passes": 2,
              "gpu_energy_j": 179.21062313821005,
              "semantic_passes": 2,
              "tokens_per_s": 79.2869432080402,
              "ttft_s": 0.123917869
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6579813415,
              "format_passes": 0,
              "gpu_energy_j": 458.92664409954455,
              "semantic_passes": 0,
              "tokens_per_s": 79.61104679194653,
              "ttft_s": 0.06266395150000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238078133,
              "format_passes": 2,
              "gpu_energy_j": 56.57549129085761,
              "semantic_passes": 2,
              "tokens_per_s": 78.18128696031796,
              "ttft_s": 0.07178785700000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24142892449999998,
              "format_passes": 0,
              "gpu_energy_j": 59.52516182415659,
              "semantic_passes": 0,
              "tokens_per_s": 77.56281221268415,
              "ttft_s": 0.1253548175
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182184278,
              "format_passes": 2,
              "gpu_energy_j": 40.11335089267759,
              "semantic_passes": 2,
              "tokens_per_s": 77.4180076436122,
              "ttft_s": 0.06590106949999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357792879,
              "format_passes": 0,
              "gpu_energy_j": 91.51614423945381,
              "semantic_passes": 0,
              "tokens_per_s": 78.74807733495606,
              "ttft_s": 0.07840955
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46906828300000003,
              "format_passes": 0,
              "gpu_energy_j": 118.27353882189135,
              "semantic_passes": 2,
              "tokens_per_s": 78.99998006391742,
              "ttft_s": 0.1145991875
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0813293515,
              "format_passes": 2,
              "gpu_energy_j": 289.207461697442,
              "semantic_passes": 2,
              "tokens_per_s": 77.90422240795628,
              "ttft_s": 0.8245679845
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23329206,
              "format_passes": 0,
              "gpu_energy_j": 57.69598287270328,
              "semantic_passes": 0,
              "tokens_per_s": 78.31469084983019,
              "ttft_s": 0.06723812500000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2001120965,
              "format_passes": 0,
              "gpu_energy_j": 49.55338720591425,
              "semantic_passes": 0,
              "tokens_per_s": 2536.707594655292,
              "ttft_s": 0.1999710925
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.718770727,
              "format_passes": 0,
              "gpu_energy_j": 190.89761400094193,
              "semantic_passes": 0,
              "tokens_per_s": 2854.2620134917192,
              "ttft_s": 0.7185293429999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.417367392,
              "format_passes": 0,
              "gpu_energy_j": 384.66545303977375,
              "semantic_passes": 0,
              "tokens_per_s": 2893.360554648828,
              "ttft_s": 1.4170434345
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295154343,
              "format_passes": 2,
              "gpu_energy_j": 73.80261654175982,
              "semantic_passes": 2,
              "tokens_per_s": 78.66875769175641,
              "ttft_s": 0.07898136
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353414987,
              "format_passes": 2,
              "gpu_energy_j": 90.34680076961936,
              "semantic_passes": 2,
              "tokens_per_s": 78.82126459246618,
              "ttft_s": 0.074277911
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3694950685,
              "format_passes": 2,
              "gpu_energy_j": 94.02214026249916,
              "semantic_passes": 2,
              "tokens_per_s": 78.83948919462608,
              "ttft_s": 0.0777151655
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6213184645000001,
              "format_passes": 0,
              "gpu_energy_j": 162.5626479123281,
              "semantic_passes": 0,
              "tokens_per_s": 78.88070105257268,
              "ttft_s": 0.319818011
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5604829520000001,
              "format_passes": 0,
              "gpu_energy_j": 147.1256069481598,
              "semantic_passes": 0,
              "tokens_per_s": 78.7646130781796,
              "ttft_s": 0.2560412815
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.016230373598769,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.08032186085384918,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005436577474760007,
            "ttft_change_pct": 0.11647910803924688
          },
          "decode": {
            "e2e_change_pct": -0.03480416693317778,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.47822336210883165,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.009966642158221184,
            "ttft_change_pct": -0.7928574665005295
          },
          "energy": {
            "e2e_change_pct": 0.018797152825489327,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.8835337170248465,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08763449025380732,
            "ttft_change_pct": -0.09805475893585047
          },
          "filtering": {
            "e2e_change_pct": -0.0017271865767498618,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0547119794638515,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0857993745468244,
            "ttft_change_pct": -0.09334198881469913
          },
          "german": {
            "e2e_change_pct": 0.10583836585786877,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.217419659519708,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05721938248105518,
            "ttft_change_pct": 0.1619983839526551
          },
          "ha_sim": {
            "e2e_change_pct": 0.07120565993978811,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4940373239337612,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1948964020990096,
            "ttft_change_pct": -0.3395066484931264
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.07371239017825992,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2411147764284314,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0732576278840602,
            "ttft_change_pct": -0.05226579674890708
          },
          "long_context": {
            "e2e_change_pct": -0.052481975637685974,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1492950665654913,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2247944830707338,
            "ttft_change_pct": 0.00012927998640499538
          },
          "math": {
            "e2e_change_pct": -0.30655772621543953,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5369406582394487,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.23555148478555665,
            "ttft_change_pct": -0.5196256069180283
          },
          "prefill": {
            "e2e_change_pct": 0.5623543119662955,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.7205848960574874,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5832176585275461,
            "ttft_change_pct": 0.5688968906811143
          },
          "prefill2048": {
            "e2e_change_pct": 0.05962379301156506,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6119326361191391,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.051773269109312015,
            "ttft_change_pct": 0.058245446140414714
          },
          "prefill4096": {
            "e2e_change_pct": -0.2339852995886238,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.447506512245055,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.23997620828146715,
            "ttft_change_pct": -0.23497530235512265
          },
          "pve_sim": {
            "e2e_change_pct": -0.1684395606429523,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5383105538258723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1465946715754729,
            "ttft_change_pct": -0.27146327162127504
          },
          "sorting": {
            "e2e_change_pct": 0.19312966032891676,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.488468774742674,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04030883008373509,
            "ttft_change_pct": 0.8009004699431443
          },
          "time": {
            "e2e_change_pct": -0.007539856863547634,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4058632383697978,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15865227189695297,
            "ttft_change_pct": 0.5498251722183101
          },
          "tool-call": {
            "e2e_change_pct": 0.2759256302047097,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.26083819473979863,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23279485648348697,
            "ttft_change_pct": 0.38164471134358724
          },
          "tool-final": {
            "e2e_change_pct": -0.24320298870700308,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1426717363011143,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02186009097580044,
            "ttft_change_pct": -0.3512996081758035
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 341149478275303,
          "end_ns": 341150084631932,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 341194864801793,
          "end_ns": 341195269170983,
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
