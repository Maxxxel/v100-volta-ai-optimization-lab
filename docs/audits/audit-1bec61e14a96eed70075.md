# Public audit excerpt

Original SHA256: `1bec61e14a96eed70075930c9a78b9ef15e0217da86bdf6552b05f23724b0301`

Original file: `RESULTS.json`; 40412 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7901108675000001,
              "format_passes": 2,
              "gpu_energy_j": 479.55757353852584,
              "semantic_passes": 2,
              "tokens_per_s": 35.4151760224901,
              "ttft_s": 0.5441445985
            },
            "decode": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7762957029999997,
              "format_passes": 0,
              "gpu_energy_j": 1056.5009679751838,
              "semantic_passes": 0,
              "tokens_per_s": 35.52219703434238,
              "ttft_s": 0.2009407895
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5959948065,
              "format_passes": 2,
              "gpu_energy_j": 150.60457023465503,
              "semantic_passes": 2,
              "tokens_per_s": 34.8190923897599,
              "ttft_s": 0.22020596650000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9442051845,
              "format_passes": 0,
              "gpu_energy_j": 240.9090532494289,
              "semantic_passes": 0,
              "tokens_per_s": 34.95704724966008,
              "ttft_s": 0.54030139
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.48598551,
              "format_passes": 2,
              "gpu_energy_j": 110.75919688655743,
              "semantic_passes": 2,
              "tokens_per_s": 33.8378019602947,
              "ttft_s": 0.218614111
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.014091896,
              "format_passes": 0,
              "gpu_energy_j": 261.4560255379862,
              "semantic_passes": 0,
              "tokens_per_s": 35.18278913245764,
              "ttft_s": 0.24295347900000003
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1621639455000001,
              "format_passes": 0,
              "gpu_energy_j": 295.00221789822297,
              "semantic_passes": 2,
              "tokens_per_s": 35.28175847318168,
              "ttft_s": 0.3664476285
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 5.03695742,
              "format_passes": 2,
              "gpu_energy_j": 1374.5720082082446,
              "semantic_passes": 2,
              "tokens_per_s": 34.37235848072189,
              "ttft_s": 4.453680032
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.586675206,
              "format_passes": 2,
              "gpu_energy_j": 144.64181354293444,
              "semantic_passes": 2,
              "tokens_per_s": 34.92367385816018,
              "ttft_s": 0.21251273250000002
            },
            "prefill": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0548155875,
              "format_passes": 0,
              "gpu_energy_j": 284.7306769416068,
              "semantic_passes": 0,
              "tokens_per_s": 479.29877228216185,
              "ttft_s": 1.0546237775
            },
            "prefill2048": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.9729185865,
              "format_passes": 0,
              "gpu_energy_j": 1082.5863561423052,
              "semantic_passes": 0,
              "tokens_per_s": 515.8552117105835,
              "ttft_s": 3.9711136995
            },
            "prefill4096": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 7.904093007,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 518.3264960345199
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.871158952,
              "format_passes": 0,
              "gpu_energy_j": 229.7527065532509,
              "semantic_passes": 2,
              "tokens_per_s": 34.97019651549249,
              "ttft_s": 0.23934965000000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.998182462,
              "format_passes": 0,
              "gpu_energy_j": 259.17864900754927,
              "semantic_passes": 2,
              "tokens_per_s": 34.91633391123412,
              "ttft_s": 0.2232573465
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.02492366,
              "format_passes": 0,
              "gpu_energy_j": 270.46091915521316,
              "semantic_passes": 2,
              "tokens_per_s": 35.343005155313776,
              "ttft_s": 0.23092946250000002
            },
            "tool-call": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.8257997365,
              "format_passes": 0,
              "gpu_energy_j": 484.62920812296363,
              "semantic_passes": 0,
              "tokens_per_s": 35.10097399759496,
              "ttft_s": 1.149080654
            },
            "tool-final": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.186809809,
              "format_passes": 0,
              "gpu_energy_j": 553.1635017464375,
              "semantic_passes": 0,
              "tokens_per_s": 35.20129516125505,
              "ttft_s": 1.504977655
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
              "e2e_s": 1.7603532925,
              "format_passes": 2,
              "gpu_energy_j": 476.28420805224556,
              "semantic_passes": 2,
              "tokens_per_s": 35.489560595164775,
              "ttft_s": 0.520529249
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7861576045,
              "format_passes": 0,
              "gpu_energy_j": 1069.6330068293664,
              "semantic_passes": 0,
              "tokens_per_s": 35.426603977080276,
              "ttft_s": 0.20221851349999997
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5808119254999999,
              "format_passes": 2,
              "gpu_energy_j": 150.36853267110678,
              "semantic_passes": 2,
              "tokens_per_s": 35.079248153789166,
              "ttft_s": 0.21015577000000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9225202115,
              "format_passes": 0,
              "gpu_energy_j": 243.74544056632269,
              "semantic_passes": 0,
              "tokens_per_s": 35.09937847069824,
              "ttft_s": 0.5235917914999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.466101742,
              "format_passes": 2,
              "gpu_energy_j": 110.79094903715793,
              "semantic_passes": 2,
              "tokens_per_s": 34.32743398019083,
              "ttft_s": 0.20387117700000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986472317,
              "format_passes": 0,
              "gpu_energy_j": 265.6958501912489,
              "semantic_passes": 0,
              "tokens_per_s": 35.38792672503888,
              "ttft_s": 0.223479231
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.143853864,
              "format_passes": 0,
              "gpu_energy_j": 295.3445675882555,
              "semantic_passes": 2,
              "tokens_per_s": 35.39046068507399,
              "ttft_s": 0.3526498905
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 5.020574252,
              "format_passes": 2,
              "gpu_energy_j": 1375.6254386541066,
              "semantic_passes": 2,
              "tokens_per_s": 34.53068483073329,
              "ttft_s": 4.441306367
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5746184485,
              "format_passes": 2,
              "gpu_energy_j": 141.4881450226215,
              "semantic_passes": 2,
              "tokens_per_s": 35.04712784182526,
              "ttft_s": 0.2036430075
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.062099322,
              "format_passes": 0,
              "gpu_energy_j": 276.56633362366864,
              "semantic_passes": 0,
              "tokens_per_s": 475.963153634737,
              "ttft_s": 1.06195965
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.9735423005,
              "format_passes": 0,
              "gpu_energy_j": 1087.3512634826425,
              "semantic_passes": 0,
              "tokens_per_s": 515.5712700984457,
              "ttft_s": 3.9732556245
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 7.907219120000001,
              "format_passes": 0,
              "gpu_energy_j": 2184.6323682795405,
              "semantic_passes": 0,
              "tokens_per_s": 518.1231470259764,
              "ttft_s": 7.906850635
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846641102,
              "format_passes": 0,
              "gpu_energy_j": 224.36910599869822,
              "semantic_passes": 2,
              "tokens_per_s": 35.32475532268707,
              "ttft_s": 0.22378985899999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9842449495000001,
              "format_passes": 0,
              "gpu_energy_j": 261.4295646378249,
              "semantic_passes": 2,
              "tokens_per_s": 35.16216511988196,
              "ttft_s": 0.21635838699999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0141806965,
              "format_passes": 0,
              "gpu_energy_j": 273.5374119394929,
              "semantic_passes": 2,
              "tokens_per_s": 35.35101393088334,
              "ttft_s": 0.2221138775
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8297235795,
              "format_passes": 0,
              "gpu_energy_j": 482.55579265288884,
              "semantic_passes": 0,
              "tokens_per_s": 35.0798121408683,
              "ttft_s": 1.152002146
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.185022796,
              "format_passes": 0,
              "gpu_energy_j": 563.0725265336791,
              "semantic_passes": 0,
              "tokens_per_s": 35.08467118903672,
              "ttft_s": 1.501738877
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
            "e2e_change_pct": -1.662331397471395,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.682580292106949,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21003586888128645,
            "ttft_change_pct": -4.339903320753081
          },
          "decode": {
            "e2e_change_pct": 0.2611527876952513,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2429746164218436,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2691079528940432,
            "ttft_change_pct": 0.6358708966851978
          },
          "energy": {
            "e2e_change_pct": -2.5474854536337466,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.15672669373876236,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7471641165057274,
            "ttft_change_pct": -4.56399826932028
          },
          "filtering": {
            "e2e_change_pct": -2.296637781276667,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1773685042699933,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4071603073956709,
            "ttft_change_pct": -3.0926439963443575
          },
          "german": {
            "e2e_change_pct": -4.091432273361406,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.02866773278702439,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4469971201754417,
            "ttft_change_pct": -6.74381627634274
          },
          "ha_sim": {
            "e2e_change_pct": -2.7235775287173802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.621620555326131,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5830623371243515,
            "ttft_change_pct": -8.015628374681572
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.5755162230680408,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11604986988626997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.30809748889055744,
            "ttft_change_pct": -3.7652687388042394
          },
          "long_context": {
            "e2e_change_pct": -0.3252592117405695,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.0766369778790299,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.46062114154954426,
            "ttft_change_pct": -0.27783012949054164
          },
          "math": {
            "e2e_change_pct": -2.055099205948041,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.180329769839917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.35349655413252634,
            "ttft_change_pct": -4.17373815472446
          },
          "prefill": {
            "e2e_change_pct": 0.6905220766847853,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8673915314058496,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6959372400522579,
            "ttft_change_pct": 0.6955914190925672
          },
          "prefill2048": {
            "e2e_change_pct": 0.015699138716795957,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44014108558660947,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.055042889107637105,
            "ttft_change_pct": 0.05393763971728305
          },
          "prefill4096": {
            "e2e_change_pct": 0.039550559402989904,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03923183748065773
          },
          "pve_sim": {
            "e2e_change_pct": -2.8143945423176997,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.343215292353873,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.0138885180056123,
            "ttft_change_pct": -6.500862232303262
          },
          "sorting": {
            "e2e_change_pct": -1.3962890584226617,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8684803470096369,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.704057903881905,
            "ttft_change_pct": -3.090137730361331
          },
          "time": {
            "e2e_change_pct": -1.048172065810249,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1374999367336436,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0226601431722262,
            "ttft_change_pct": -3.817436244195138
          },
          "tool-call": {
            "e2e_change_pct": 0.214910919393696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4278354328055123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.060288517145179465,
            "ttft_change_pct": 0.25424603484796027
          },
          "tool-final": {
            "e2e_change_pct": -0.08171780612311608,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7913374175911878,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3313059127059925,
            "ttft_change_pct": -0.21520439119078194
          }
        }
      },
      "complete": false,
      "failed_starts": [
        {
          "index": 0,
          "model": "qwen38"
        },
        {
          "index": 3,
          "model": "qwen38"
        }
      ]
    }
  }
}
```

</details>
