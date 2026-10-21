# Public audit excerpt

Original SHA256: `fb080c78ceab56b04fad69b3ba369250099eeebc456479d1304bca6d1b6af056`

Original file: `RESULTS.json`; 39606 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5263122025,
              "format_passes": 2,
              "gpu_energy_j": 131.8210527623727,
              "semantic_passes": 2,
              "tokens_per_s": 96.51726693003562,
              "ttft_s": 0.1325343275
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.367685869,
              "format_passes": 0,
              "gpu_energy_j": 356.76816518206977,
              "semantic_passes": 0,
              "tokens_per_s": 96.98336339769487,
              "ttft_s": 0.0581441845
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2046652615,
              "format_passes": 2,
              "gpu_energy_j": 44.825047538088086,
              "semantic_passes": 2,
              "tokens_per_s": 95.22839463828277,
              "ttft_s": 0.0681210775
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2297552575,
              "format_passes": 0,
              "gpu_energy_j": 55.0121656300458,
              "semantic_passes": 0,
              "tokens_per_s": 93.9831146726138,
              "ttft_s": 0.133966021
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156824166,
              "format_passes": 2,
              "gpu_energy_j": 32.46853227545782,
              "semantic_passes": 2,
              "tokens_per_s": 94.17422384150137,
              "ttft_s": 0.061193774
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3066325365,
              "format_passes": 0,
              "gpu_energy_j": 71.52122337964548,
              "semantic_passes": 0,
              "tokens_per_s": 96.10634565819475,
              "ttft_s": 0.0776163665
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398537405,
              "format_passes": 0,
              "gpu_energy_j": 95.64862117183353,
              "semantic_passes": 2,
              "tokens_per_s": 96.04848467818803,
              "ttft_s": 0.1070392
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0321971375,
              "format_passes": 2,
              "gpu_energy_j": 271.0908110740047,
              "semantic_passes": 2,
              "tokens_per_s": 94.27755591259063,
              "ttft_s": 0.87309224
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1485332315,
              "format_passes": 0,
              "gpu_energy_j": 31.525028658180965,
              "semantic_passes": 0,
              "tokens_per_s": 93.60120026715133,
              "ttft_s": 0.06303310300000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2061348065,
              "format_passes": 0,
              "gpu_energy_j": 50.89361423976543,
              "semantic_passes": 0,
              "tokens_per_s": 2462.819955002711,
              "ttft_s": 0.2059616635
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.75589852,
              "format_passes": 0,
              "gpu_energy_j": 200.47268605348626,
              "semantic_passes": 0,
              "tokens_per_s": 2713.805613335796,
              "ttft_s": 0.7556505385
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5003937025,
              "format_passes": 0,
              "gpu_energy_j": 403.2097471809046,
              "semantic_passes": 0,
              "tokens_per_s": 2732.948344650229,
              "ttft_s": 1.5000855309999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.255137921,
              "format_passes": 2,
              "gpu_energy_j": 58.26080292999176,
              "semantic_passes": 2,
              "tokens_per_s": 95.26718294957888,
              "ttft_s": 0.0768375325
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3516711955,
              "format_passes": 0,
              "gpu_energy_j": 85.49088896858329,
              "semantic_passes": 2,
              "tokens_per_s": 95.88560211130716,
              "ttft_s": 0.070092674
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.315858357,
              "format_passes": 0,
              "gpu_energy_j": 75.1119476820117,
              "semantic_passes": 0,
              "tokens_per_s": 95.47318705953396,
              "ttft_s": 0.07487424649999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5508611505000001,
              "format_passes": 0,
              "gpu_energy_j": 140.4802211530411,
              "semantic_passes": 0,
              "tokens_per_s": 96.16019078150197,
              "ttft_s": 0.303713497
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5249108945000001,
              "format_passes": 0,
              "gpu_energy_j": 133.44656949666737,
              "semantic_passes": 0,
              "tokens_per_s": 95.79404281139668,
              "ttft_s": 0.27455754649999997
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
              "e2e_s": 0.5263933925,
              "format_passes": 2,
              "gpu_energy_j": 131.60097018341528,
              "semantic_passes": 2,
              "tokens_per_s": 96.40061399930556,
              "ttft_s": 0.132200301
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3648087785,
              "format_passes": 0,
              "gpu_energy_j": 356.7668566940074,
              "semantic_passes": 0,
              "tokens_per_s": 97.16726831853558,
              "ttft_s": 0.0577239015
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2041804515,
              "format_passes": 2,
              "gpu_energy_j": 47.1737261962092,
              "semantic_passes": 2,
              "tokens_per_s": 95.29021327325104,
              "ttft_s": 0.0677116905
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2296337705,
              "format_passes": 0,
              "gpu_energy_j": 54.02904262676455,
              "semantic_passes": 0,
              "tokens_per_s": 94.0690259205162,
              "ttft_s": 0.133911752
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1562353875,
              "format_passes": 2,
              "gpu_energy_j": 32.47609012055545,
              "semantic_passes": 2,
              "tokens_per_s": 94.2280249869891,
              "ttft_s": 0.0606982435
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30593410249999997,
              "format_passes": 0,
              "gpu_energy_j": 72.51565427544882,
              "semantic_passes": 0,
              "tokens_per_s": 96.04493149588808,
              "ttft_s": 0.07685185950000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.397620844,
              "format_passes": 0,
              "gpu_energy_j": 93.93507607675755,
              "semantic_passes": 2,
              "tokens_per_s": 96.3911844412672,
              "ttft_s": 0.10711977950000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0322374825,
              "format_passes": 2,
              "gpu_energy_j": 270.3617430838152,
              "semantic_passes": 2,
              "tokens_per_s": 94.44779786871655,
              "ttft_s": 0.8733592845
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1483918945,
              "format_passes": 0,
              "gpu_energy_j": 32.13560909169267,
              "semantic_passes": 0,
              "tokens_per_s": 93.80208535107965,
              "ttft_s": 0.06311723699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20620324,
              "format_passes": 0,
              "gpu_energy_j": 52.64882581429118,
              "semantic_passes": 0,
              "tokens_per_s": 2462.143460368956,
              "ttft_s": 0.20599022849999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7538665545000001,
              "format_passes": 0,
              "gpu_energy_j": 199.04185976536178,
              "semantic_passes": 0,
              "tokens_per_s": 2720.9718271580614,
              "ttft_s": 0.753663537
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4986829335,
              "format_passes": 0,
              "gpu_energy_j": 404.80901065632537,
              "semantic_passes": 0,
              "tokens_per_s": 2736.1593991145983,
              "ttft_s": 1.4983491025000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.253602329,
              "format_passes": 2,
              "gpu_energy_j": 56.92784872015395,
              "semantic_passes": 2,
              "tokens_per_s": 95.73668599810635,
              "ttft_s": 0.075980089
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35054593,
              "format_passes": 0,
              "gpu_energy_j": 83.24152796032746,
              "semantic_passes": 2,
              "tokens_per_s": 96.25926080186547,
              "ttft_s": 0.0700413275
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314190701,
              "format_passes": 0,
              "gpu_energy_j": 75.73308895464544,
              "semantic_passes": 0,
              "tokens_per_s": 96.23413000001739,
              "ttft_s": 0.07518775850000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5493097360000001,
              "format_passes": 0,
              "gpu_energy_j": 138.4935913884343,
              "semantic_passes": 0,
              "tokens_per_s": 96.35071299465045,
              "ttft_s": 0.302685961
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5238212685000001,
              "format_passes": 0,
              "gpu_energy_j": 134.30135449697036,
              "semantic_passes": 0,
              "tokens_per_s": 95.99738982879339,
              "ttft_s": 0.273698932
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
            "e2e_change_pct": 0.01542620513343973,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.16695556160830627,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12086223992916478,
            "ttft_change_pct": -0.25203017686116214
          },
          "decode": {
            "e2e_change_pct": -0.21036193801604597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.0003667614406399622,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1896252247785668,
            "ttft_change_pct": -0.7228289529110143
          },
          "energy": {
            "e2e_change_pct": -0.23687947649093655,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.239656814921245,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06491617883834788,
            "ttft_change_pct": -0.6009696484909455
          },
          "filtering": {
            "e2e_change_pct": -0.05287670076494777,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7871010748653382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0914113649049364,
            "ttft_change_pct": -0.04050952591926338
          },
          "german": {
            "e2e_change_pct": -0.37543862978361986,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.023277446093072918,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05712937499573467,
            "ttft_change_pct": -0.8097727392986087
          },
          "ha_sim": {
            "e2e_change_pct": -0.2277755674502724,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3903997286578207,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06390229686299431,
            "ttft_change_pct": -0.98498169197343
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.22998117328536516,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7915000489108768,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.35679871913376626,
            "ttft_change_pct": 0.07528036457673526
          },
          "long_context": {
            "e2e_change_pct": 0.003908652575579374,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2689386583414888,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.18057527529007356,
            "ttft_change_pct": 0.030586058123716064
          },
          "math": {
            "e2e_change_pct": -0.09515513705092848,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9368116683797343,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2146180640365314,
            "ttft_change_pct": 0.13347589757715106
          },
          "prefill": {
            "e2e_change_pct": 0.033198420568547604,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.448785472882232,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.027468294317700703,
            "ttft_change_pct": 0.0138690858844992
          },
          "prefill2048": {
            "e2e_change_pct": -0.26881458902709987,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7137263017180984,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.26406511162959667,
            "ttft_change_pct": -0.2629524361809188
          },
          "prefill4096": {
            "e2e_change_pct": -0.11402133967567396,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.39663313860893723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11749415134958419,
            "ttft_change_pct": -0.11575529955563102
          },
          "pve_sim": {
            "e2e_change_pct": -0.6018674111560096,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2879090963430992,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4928276810451715,
            "ttft_change_pct": -1.1159175367845164
          },
          "sorting": {
            "e2e_change_pct": -0.3199765901782503,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.631111964553834,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3896921772724049,
            "ttft_change_pct": -0.07325515930522997
          },
          "time": {
            "e2e_change_pct": -0.5279758990198169,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8269540223658556,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7970226656505375,
            "ttft_change_pct": 0.4187180701711757
          },
          "tool-call": {
            "e2e_change_pct": -0.28163440071817814,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4141704421453904,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19813002823736436,
            "ttft_change_pct": -0.33832411471657053
          },
          "tool-final": {
            "e2e_change_pct": -0.20758304150609863,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6405447539993503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21227522237168284,
            "ttft_change_pct": -0.3127266072069035
          }
        }
      },
      "complete": true
    }
  }
}
```
