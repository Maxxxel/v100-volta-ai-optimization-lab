# Public audit excerpt

Original SHA256: `a8b0b3b540e2b38a864a1003bf2695fb5cb2c972cd8e1d2ad09f01655e15b434`

Original file: `RESULTS.json`; 39872 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666252192,
              "format_passes": 2,
              "gpu_energy_j": 176.16946540705206,
              "semantic_passes": 2,
              "tokens_per_s": 79.25222847668313,
              "ttft_s": 0.12366858650000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658529953,
              "format_passes": 0,
              "gpu_energy_j": 451.85835336553237,
              "semantic_passes": 0,
              "tokens_per_s": 79.60862644748502,
              "ttft_s": 0.06318004299999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23836035,
              "format_passes": 2,
              "gpu_energy_j": 51.950177592767545,
              "semantic_passes": 2,
              "tokens_per_s": 78.26806313542396,
              "ttft_s": 0.0722588925
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241453097,
              "format_passes": 0,
              "gpu_energy_j": 58.714170925187226,
              "semantic_passes": 0,
              "tokens_per_s": 77.67896102515228,
              "ttft_s": 0.125578237
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1820520675,
              "format_passes": 2,
              "gpu_energy_j": 41.96904904311289,
              "semantic_passes": 2,
              "tokens_per_s": 77.56892735645596,
              "ttft_s": 0.065997047
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3576281565,
              "format_passes": 0,
              "gpu_energy_j": 91.97272505849105,
              "semantic_passes": 0,
              "tokens_per_s": 78.90183904764623,
              "ttft_s": 0.07876491399999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469163953,
              "format_passes": 0,
              "gpu_energy_j": 119.21428763587838,
              "semantic_passes": 2,
              "tokens_per_s": 79.0615421482299,
              "ttft_s": 0.1149748125
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0792410825,
              "format_passes": 2,
              "gpu_energy_j": 291.2112245118859,
              "semantic_passes": 2,
              "tokens_per_s": 78.11220274599822,
              "ttft_s": 0.8231359389999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23460599,
              "format_passes": 0,
              "gpu_energy_j": 54.821686699501626,
              "semantic_passes": 0,
              "tokens_per_s": 77.99491060771213,
              "ttft_s": 0.06789013599999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19938182399999999,
              "format_passes": 0,
              "gpu_energy_j": 48.3431594292459,
              "semantic_passes": 0,
              "tokens_per_s": 2546.571518050608,
              "ttft_s": 0.199247156
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7164900235,
              "format_passes": 0,
              "gpu_energy_j": 187.9298352552933,
              "semantic_passes": 0,
              "tokens_per_s": 2863.5035355548125,
              "ttft_s": 0.7162480360000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4169580805000002,
              "format_passes": 0,
              "gpu_energy_j": 380.56244713378203,
              "semantic_passes": 0,
              "tokens_per_s": 2894.2401747779786,
              "ttft_s": 1.4165965905000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29509182749999996,
              "format_passes": 2,
              "gpu_energy_j": 73.59903538629955,
              "semantic_passes": 2,
              "tokens_per_s": 78.63824192040266,
              "ttft_s": 0.07891039899999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353047188,
              "format_passes": 2,
              "gpu_energy_j": 86.20850188502112,
              "semantic_passes": 2,
              "tokens_per_s": 78.81824709202118,
              "ttft_s": 0.0738773755
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3690420035,
              "format_passes": 2,
              "gpu_energy_j": 94.92286511053823,
              "semantic_passes": 2,
              "tokens_per_s": 78.90503722376005,
              "ttft_s": 0.0775060125
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194996399999999,
              "format_passes": 0,
              "gpu_energy_j": 160.8581524912724,
              "semantic_passes": 0,
              "tokens_per_s": 79.00569985275867,
              "ttft_s": 0.3185095645
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5602352625,
              "format_passes": 0,
              "gpu_energy_j": 146.35657143834342,
              "semantic_passes": 0,
              "tokens_per_s": 78.83909553227224,
              "ttft_s": 0.25592854
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
              "e2e_s": 0.6666870574999999,
              "format_passes": 2,
              "gpu_energy_j": 177.21011015485567,
              "semantic_passes": 2,
              "tokens_per_s": 79.22022908261009,
              "ttft_s": 0.12381375650000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658879866,
              "format_passes": 0,
              "gpu_energy_j": 453.75954010685155,
              "semantic_passes": 0,
              "tokens_per_s": 79.60565864337208,
              "ttft_s": 0.063116184
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238461667,
              "format_passes": 2,
              "gpu_energy_j": 59.79353935056626,
              "semantic_passes": 2,
              "tokens_per_s": 77.97686955065163,
              "ttft_s": 0.071689945
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2422824765,
              "format_passes": 0,
              "gpu_energy_j": 62.62675838857879,
              "semantic_passes": 0,
              "tokens_per_s": 77.02250157533807,
              "ttft_s": 0.12539291749999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18227368100000002,
              "format_passes": 2,
              "gpu_energy_j": 40.891158917726706,
              "semantic_passes": 2,
              "tokens_per_s": 77.46509564514363,
              "ttft_s": 0.06605883500000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357451794,
              "format_passes": 0,
              "gpu_energy_j": 89.30687500715135,
              "semantic_passes": 0,
              "tokens_per_s": 78.99111121033565,
              "ttft_s": 0.07891638849999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468710049,
              "format_passes": 0,
              "gpu_energy_j": 119.5072585705617,
              "semantic_passes": 2,
              "tokens_per_s": 79.11095862715712,
              "ttft_s": 0.114756313
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.080649356,
              "format_passes": 2,
              "gpu_energy_j": 290.42231956154245,
              "semantic_passes": 2,
              "tokens_per_s": 78.09953588511772,
              "ttft_s": 0.824560957
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2335347605,
              "format_passes": 0,
              "gpu_energy_j": 56.68024434498432,
              "semantic_passes": 0,
              "tokens_per_s": 78.30533319261116,
              "ttft_s": 0.06749360900000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1986799775,
              "format_passes": 0,
              "gpu_energy_j": 48.02295925280948,
              "semantic_passes": 0,
              "tokens_per_s": 2555.2805087221323,
              "ttft_s": 0.1984936275
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7163260005000001,
              "format_passes": 0,
              "gpu_energy_j": 191.00644469686836,
              "semantic_passes": 0,
              "tokens_per_s": 2863.857684319736,
              "ttft_s": 0.7160808045
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4172262299999998,
              "format_passes": 0,
              "gpu_energy_j": 384.8123358697426,
              "semantic_passes": 0,
              "tokens_per_s": 2893.6536997080193,
              "ttft_s": 1.416894599
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29578178899999996,
              "format_passes": 2,
              "gpu_energy_j": 74.12998486821733,
              "semantic_passes": 2,
              "tokens_per_s": 78.37563176112806,
              "ttft_s": 0.07884919
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353105756,
              "format_passes": 2,
              "gpu_energy_j": 88.21472714817888,
              "semantic_passes": 2,
              "tokens_per_s": 78.79275216744456,
              "ttft_s": 0.0738708805
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36902148,
              "format_passes": 2,
              "gpu_energy_j": 94.5059079768517,
              "semantic_passes": 2,
              "tokens_per_s": 78.95572988340547,
              "ttft_s": 0.077631756
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619882025,
              "format_passes": 0,
              "gpu_energy_j": 160.79299162691905,
              "semantic_passes": 0,
              "tokens_per_s": 79.01060259648396,
              "ttft_s": 0.3183273125
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5607734209999999,
              "format_passes": 0,
              "gpu_energy_j": 146.75088673507474,
              "semantic_passes": 0,
              "tokens_per_s": 78.83443342000666,
              "ttft_s": 0.2561877655
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
            "e2e_change_pct": 0.06527040439363585,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5907066502127023,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.040376648944895344,
            "ttft_change_pct": 0.11738631782616249
          },
          "decode": {
            "e2e_change_pct": 0.02109777995671358,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4207483887724406,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0037279931150435708,
            "ttft_change_pct": -0.1010746383948935
          },
          "energy": {
            "e2e_change_pct": 0.04250581105456064,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 15.097853599812638,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.37204649394285694,
            "ttft_change_pct": -0.7873736786098706
          },
          "filtering": {
            "e2e_change_pct": 0.34349507639572785,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.6637872965573,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8450929841886667,
            "ttft_change_pct": -0.1475729429136874
          },
          "german": {
            "e2e_change_pct": 0.12173083395496942,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.5682977097692072,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13385735094051388,
            "ttft_change_pct": 0.09362237071002255
          },
          "ha_sim": {
            "e2e_change_pct": -0.04931448958773732,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8985224148184385,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11314332310492503,
            "ttft_change_pct": 0.19231215055983686
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.09674741571631396,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.24575152902659436,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0625038135918965,
            "ttft_change_pct": -0.19004118836897232
          },
          "long_context": {
            "e2e_change_pct": 0.1304873881132984,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.27090471930324433,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01621623822553042,
            "ttft_change_pct": 0.17312061501424392
          },
          "math": {
            "e2e_change_pct": -0.45660790672906737,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3901869084586034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.39800364213551376,
            "ttft_change_pct": -0.5840715947306063
          },
          "prefill": {
            "e2e_change_pct": -0.3520112746084547,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6623484691873793,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3419888508841451,
            "ttft_change_pct": -0.37818783220173735
          },
          "prefill2048": {
            "e2e_change_pct": -0.02289257276726353,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6371053789280499,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01236767339471978,
            "ttft_change_pct": -0.023348266465628154
          },
          "prefill4096": {
            "e2e_change_pct": 0.018924307196521717,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1167388605914041,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.020263524605534933,
            "ttft_change_pct": 0.02103693472073065
          },
          "pve_sim": {
            "e2e_change_pct": 0.23381247316989207,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7214082075002626,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3339471392816873,
            "ttft_change_pct": -0.07756772336177109
          },
          "sorting": {
            "e2e_change_pct": 0.01658928380983138,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3271779688661454,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03234647498168153,
            "ttft_change_pct": -0.008791595472956715
          },
          "time": {
            "e2e_change_pct": -0.005561291074007713,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4392589005830949,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06424515015646115,
            "ttft_change_pct": 0.16223709096117034
          },
          "tool-call": {
            "e2e_change_pct": 0.061724813915975396,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.040508275983641706,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.006205556984406613,
            "ttft_change_pct": -0.05722025970745781
          },
          "tool-final": {
            "e2e_change_pct": 0.09605937648380358,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2694209715738305,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0059134522461201655,
            "ttft_change_pct": 0.10128823459860659
          }
        }
      },
      "complete": true
    }
  }
}
```
