# Public audit excerpt

Original SHA256: `83a557bfdd78d028d5f043c24c525f723378d949af496877799210e6f3ea9458`

Original file: `RESULTS.json`; 39890 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7638815714999998,
              "format_passes": 2,
              "gpu_energy_j": 484.4252715830198,
              "semantic_passes": 2,
              "tokens_per_s": 35.37653746410634,
              "ttft_s": 0.5201032225
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7848737615,
              "format_passes": 0,
              "gpu_energy_j": 1068.206626632113,
              "semantic_passes": 0,
              "tokens_per_s": 35.384599485538075,
              "ttft_s": 0.1960228355
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5816721094999999,
              "format_passes": 2,
              "gpu_energy_j": 147.70331561722656,
              "semantic_passes": 2,
              "tokens_per_s": 34.95137742628047,
              "ttft_s": 0.20964043100000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.925206108,
              "format_passes": 0,
              "gpu_energy_j": 241.9946442727801,
              "semantic_passes": 0,
              "tokens_per_s": 34.99167547723799,
              "ttft_s": 0.52510179
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4653388355,
              "format_passes": 2,
              "gpu_energy_j": 108.54216204128699,
              "semantic_passes": 2,
              "tokens_per_s": 34.202456412545445,
              "ttft_s": 0.2021718455
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989818546,
              "format_passes": 0,
              "gpu_energy_j": 268.9654680555989,
              "semantic_passes": 0,
              "tokens_per_s": 35.28957509988927,
              "ttft_s": 0.2246888515
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1480223055,
              "format_passes": 0,
              "gpu_energy_j": 302.5147670674356,
              "semantic_passes": 2,
              "tokens_per_s": 35.21928676201533,
              "ttft_s": 0.352947386
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7931742245,
              "format_passes": 2,
              "gpu_energy_j": 1016.8281384710052,
              "semantic_passes": 2,
              "tokens_per_s": 34.40809714426332,
              "ttft_s": 3.2118313645
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5739568975,
              "format_passes": 2,
              "gpu_energy_j": 144.39690760051764,
              "semantic_passes": 2,
              "tokens_per_s": 35.00690248157881,
              "ttft_s": 0.2025280915
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7236359035,
              "format_passes": 0,
              "gpu_energy_j": 190.68376387232985,
              "semantic_passes": 0,
              "tokens_per_s": 698.962906439802,
              "ttft_s": 0.7235082214999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7517300125000004,
              "format_passes": 0,
              "gpu_energy_j": 730.9121819827437,
              "semantic_passes": 0,
              "tokens_per_s": 744.5912619898677,
              "ttft_s": 2.7515008045
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4705964845,
              "format_passes": 0,
              "gpu_energy_j": 1472.3248971789853,
              "semantic_passes": 0,
              "tokens_per_s": 748.969537454543,
              "ttft_s": 5.4702001209999995
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8483967575,
              "format_passes": 0,
              "gpu_energy_j": 225.23395248153875,
              "semantic_passes": 2,
              "tokens_per_s": 35.19285052816848,
              "ttft_s": 0.2232079385
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986515542,
              "format_passes": 0,
              "gpu_energy_j": 262.18826037698705,
              "semantic_passes": 2,
              "tokens_per_s": 35.09700017447061,
              "ttft_s": 0.21717413400000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0180070595,
              "format_passes": 0,
              "gpu_energy_j": 274.9620674704635,
              "semantic_passes": 2,
              "tokens_per_s": 35.1004621544638,
              "ttft_s": 0.2202877615
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.708539792,
              "format_passes": 0,
              "gpu_energy_j": 464.39987626864666,
              "semantic_passes": 0,
              "tokens_per_s": 34.977414273932865,
              "ttft_s": 1.0291327695
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7792272935,
              "format_passes": 0,
              "gpu_energy_j": 469.02221081050743,
              "semantic_passes": 0,
              "tokens_per_s": 35.066035552673554,
              "ttft_s": 1.0945004575
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
              "e2e_s": 1.7645822085,
              "format_passes": 2,
              "gpu_energy_j": 490.07124615488715,
              "semantic_passes": 2,
              "tokens_per_s": 35.382600518381324,
              "ttft_s": 0.520966295
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.791016817,
              "format_passes": 0,
              "gpu_energy_j": 1071.3752961622272,
              "semantic_passes": 0,
              "tokens_per_s": 35.324115074993344,
              "ttft_s": 0.1944607815
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.58063299,
              "format_passes": 2,
              "gpu_energy_j": 150.3994672797391,
              "semantic_passes": 2,
              "tokens_per_s": 34.91594125514996,
              "ttft_s": 0.20828656099999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.925296927,
              "format_passes": 0,
              "gpu_energy_j": 247.09336930583635,
              "semantic_passes": 0,
              "tokens_per_s": 34.93272654643947,
              "ttft_s": 0.5245225155
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4670801195,
              "format_passes": 2,
              "gpu_energy_j": 109.61478086841835,
              "semantic_passes": 2,
              "tokens_per_s": 34.27653365233367,
              "ttft_s": 0.2044260285
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9899729415,
              "format_passes": 0,
              "gpu_energy_j": 266.99097995926616,
              "semantic_passes": 0,
              "tokens_per_s": 35.250169818857785,
              "ttft_s": 0.2239860245
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1495258945,
              "format_passes": 0,
              "gpu_energy_j": 296.7496424953064,
              "semantic_passes": 2,
              "tokens_per_s": 35.26089609824392,
              "ttft_s": 0.35531406600000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8014551255,
              "format_passes": 2,
              "gpu_energy_j": 1030.917230294234,
              "semantic_passes": 2,
              "tokens_per_s": 34.360657123961296,
              "ttft_s": 3.2193623689999997
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5741158565,
              "format_passes": 2,
              "gpu_energy_j": 144.74526140177858,
              "semantic_passes": 2,
              "tokens_per_s": 34.92328789765993,
              "ttft_s": 0.2017872195
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.725120718,
              "format_passes": 0,
              "gpu_energy_j": 185.5316484271233,
              "semantic_passes": 0,
              "tokens_per_s": 697.5232194468251,
              "ttft_s": 0.724911557
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7515175925,
              "format_passes": 0,
              "gpu_energy_j": 739.6786847389167,
              "semantic_passes": 0,
              "tokens_per_s": 744.6349893100104,
              "ttft_s": 2.7512933415
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4778535365,
              "format_passes": 0,
              "gpu_energy_j": 1479.9134722170365,
              "semantic_passes": 0,
              "tokens_per_s": 747.9746071081279,
              "ttft_s": 5.477512642
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8491069410000001,
              "format_passes": 0,
              "gpu_energy_j": 228.26226985964746,
              "semantic_passes": 2,
              "tokens_per_s": 35.10349953140191,
              "ttft_s": 0.222348499
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9851233365000001,
              "format_passes": 0,
              "gpu_energy_j": 262.6736394535908,
              "semantic_passes": 2,
              "tokens_per_s": 35.06889333935662,
              "ttft_s": 0.215193832
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015775005,
              "format_passes": 0,
              "gpu_energy_j": 278.7379439797096,
              "semantic_passes": 2,
              "tokens_per_s": 35.23918903108506,
              "ttft_s": 0.2211829165
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.70835197,
              "format_passes": 0,
              "gpu_energy_j": 461.67095873254596,
              "semantic_passes": 0,
              "tokens_per_s": 35.01840882223396,
              "ttft_s": 1.0295946225
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.780116472,
              "format_passes": 0,
              "gpu_energy_j": 468.95110783661414,
              "semantic_passes": 0,
              "tokens_per_s": 35.056047964291736,
              "ttft_s": 1.095085675
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
            "e2e_change_pct": 0.03972131753746666,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1654995936560608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.017138631165170004,
            "ttft_change_pct": 0.16594254037718414
          },
          "decode": {
            "e2e_change_pct": 0.16230542647122093,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.29663451350272485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17093428051786486,
            "ttft_change_pct": -0.7968734846711123
          },
          "energy": {
            "e2e_change_pct": -0.17864351462426598,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.825383303851913,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1013870517843074,
            "ttft_change_pct": -0.645805770166552
          },
          "filtering": {
            "e2e_change_pct": 0.009816083055946834,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1069577999870415,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1684655850128336,
            "ttft_change_pct": -0.11031661118505731
          },
          "german": {
            "e2e_change_pct": 0.37419700810679135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9882047740336741,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2165845601693528,
            "ttft_change_pct": 1.1149836390052625
          },
          "ha_sim": {
            "e2e_change_pct": 0.015598364025803946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7341046828823972,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11166266785571644,
            "ttft_change_pct": -0.3128001212823972
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.13097210679586802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9057332731278187,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1181436083863785,
            "ttft_change_pct": 0.6705475359435109
          },
          "long_context": {
            "e2e_change_pct": 0.21831058922929802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3855922441735835,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1378745825528327,
            "ttft_change_pct": 0.2344769586360984
          },
          "math": {
            "e2e_change_pct": 0.027695285254414337,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.24124741107660608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23885170635384867,
            "ttft_change_pct": -0.36581196934846183
          },
          "prefill": {
            "e2e_change_pct": 0.20518806388938327,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.701916167679652,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2059747348124752,
            "ttft_change_pct": 0.193962619677035
          },
          "prefill2048": {
            "e2e_change_pct": -0.0077195073294067384,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1993920709314265,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005872660931549589,
            "ttft_change_pct": -0.007539994161032126
          },
          "prefill4096": {
            "e2e_change_pct": 0.13265558921338183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.515414434177619,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1328398949036691,
            "ttft_change_pct": 0.1336792226654948
          },
          "pve_sim": {
            "e2e_change_pct": 0.08370888899820184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3445208170188794,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.25388962651675673,
            "ttft_change_pct": -0.3850398448082104
          },
          "sorting": {
            "e2e_change_pct": -0.14112352423536478,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.18512616694044137,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08008329764442879,
            "ttft_change_pct": -0.91184984303887
          },
          "time": {
            "e2e_change_pct": -0.21925727127041217,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3732354226103194,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.39522806284082446,
            "ttft_change_pct": 0.4063571184820258
          },
          "tool-call": {
            "e2e_change_pct": -0.010993129974468108,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5876223650245094,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11720291265682192,
            "ttft_change_pct": 0.04487788297948825
          },
          "tool-final": {
            "e2e_change_pct": 0.04997554293644235,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.015159830868227697,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02848222852799287,
            "ttft_change_pct": 0.05346891323707581
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
