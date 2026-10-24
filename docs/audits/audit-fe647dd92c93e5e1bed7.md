# Public audit excerpt

Original SHA256: `fe647dd92c93e5e1bed7c5c2d8a4abf6e967ad086c6fe530606e6e9691f1c609`

Original file: `RESULTS.json`; 39522 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5266590935,
              "format_passes": 2,
              "gpu_energy_j": 132.24224482211872,
              "semantic_passes": 2,
              "tokens_per_s": 96.47473872750719,
              "ttft_s": 0.132739889
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.367118133,
              "format_passes": 0,
              "gpu_energy_j": 351.1364356448458,
              "semantic_passes": 0,
              "tokens_per_s": 97.00247304155226,
              "ttft_s": 0.0578073765
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20485188399999998,
              "format_passes": 2,
              "gpu_energy_j": 42.87484051198655,
              "semantic_passes": 2,
              "tokens_per_s": 95.0115325837154,
              "ttft_s": 0.06793624549999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2301100805,
              "format_passes": 0,
              "gpu_energy_j": 53.87246524998176,
              "semantic_passes": 0,
              "tokens_per_s": 93.99870507079159,
              "ttft_s": 0.1343356365
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157007495,
              "format_passes": 2,
              "gpu_energy_j": 33.27785396457713,
              "semantic_passes": 2,
              "tokens_per_s": 94.25223881306809,
              "ttft_s": 0.061481877
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30708092649999996,
              "format_passes": 0,
              "gpu_energy_j": 72.33490516881079,
              "semantic_passes": 0,
              "tokens_per_s": 95.90377108587026,
              "ttft_s": 0.077656116
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39843511,
              "format_passes": 0,
              "gpu_energy_j": 93.89816026344802,
              "semantic_passes": 2,
              "tokens_per_s": 96.07370894131171,
              "ttft_s": 0.10696747549999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0318722385,
              "format_passes": 2,
              "gpu_energy_j": 273.28900502889,
              "semantic_passes": 2,
              "tokens_per_s": 94.40522322766404,
              "ttft_s": 0.8729169485
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1483892235,
              "format_passes": 0,
              "gpu_energy_j": 30.056018952628236,
              "semantic_passes": 0,
              "tokens_per_s": 93.76250558118755,
              "ttft_s": 0.063061458
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2058827295,
              "format_passes": 0,
              "gpu_energy_j": 49.497608404440655,
              "semantic_passes": 0,
              "tokens_per_s": 2464.851589162152,
              "ttft_s": 0.205745109
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7547054115,
              "format_passes": 0,
              "gpu_energy_j": 203.1857892958266,
              "semantic_passes": 0,
              "tokens_per_s": 2718.251840967173,
              "ttft_s": 0.7544536614999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.498246464,
              "format_passes": 0,
              "gpu_energy_j": 405.1977621593765,
              "semantic_passes": 0,
              "tokens_per_s": 2736.981008663149,
              "ttft_s": 1.4979361025
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254082202,
              "format_passes": 2,
              "gpu_energy_j": 56.67447446450532,
              "semantic_passes": 2,
              "tokens_per_s": 95.7084675949478,
              "ttft_s": 0.076372827
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3511219285,
              "format_passes": 0,
              "gpu_energy_j": 84.2686868769086,
              "semantic_passes": 2,
              "tokens_per_s": 96.07796687075279,
              "ttft_s": 0.0700571455
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31513957800000003,
              "format_passes": 0,
              "gpu_energy_j": 76.23875677986024,
              "semantic_passes": 0,
              "tokens_per_s": 95.84819644662075,
              "ttft_s": 0.075165627
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5506576935,
              "format_passes": 0,
              "gpu_energy_j": 136.729711163224,
              "semantic_passes": 0,
              "tokens_per_s": 96.1406804667443,
              "ttft_s": 0.3034156895
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524322289,
              "format_passes": 0,
              "gpu_energy_j": 133.61244473626138,
              "semantic_passes": 0,
              "tokens_per_s": 95.86333982131306,
              "ttft_s": 0.273738371
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
              "e2e_s": 0.4780834055,
              "format_passes": 2,
              "gpu_energy_j": 117.19508366864721,
              "semantic_passes": 2,
              "tokens_per_s": 96.56336575066317,
              "ttft_s": 0.0844992245
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3671314395,
              "format_passes": 0,
              "gpu_energy_j": 350.3444813827973,
              "semantic_passes": 0,
              "tokens_per_s": 97.0329333166541,
              "ttft_s": 0.058023387499999995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20591478000000002,
              "format_passes": 2,
              "gpu_energy_j": 46.63838748077415,
              "semantic_passes": 2,
              "tokens_per_s": 94.54783438615837,
              "ttft_s": 0.068405879
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18906217,
              "format_passes": 0,
              "gpu_energy_j": 40.83449161839306,
              "semantic_passes": 0,
              "tokens_per_s": 93.88074823620623,
              "ttft_s": 0.093111583
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1570226025,
              "format_passes": 2,
              "gpu_energy_j": 33.018361557156815,
              "semantic_passes": 2,
              "tokens_per_s": 93.84061658516782,
              "ttft_s": 0.0610911325
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3060968615,
              "format_passes": 0,
              "gpu_energy_j": 70.09195841390851,
              "semantic_passes": 0,
              "tokens_per_s": 95.85542467663421,
              "ttft_s": 0.0765607235
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4032180715,
              "format_passes": 0,
              "gpu_energy_j": 93.71748531650604,
              "semantic_passes": 2,
              "tokens_per_s": 95.65522349191392,
              "ttft_s": 0.1104918175
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.4124168375,
              "format_passes": 2,
              "gpu_energy_j": 369.3668572219483,
              "semantic_passes": 2,
              "tokens_per_s": 94.38438077429856,
              "ttft_s": 1.2534834165
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149575652,
              "format_passes": 0,
              "gpu_energy_j": 26.800056639801227,
              "semantic_passes": 0,
              "tokens_per_s": 93.50345188726652,
              "ttft_s": 0.0640243865
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.305524308,
              "format_passes": 0,
              "gpu_energy_j": 76.29664787732202,
              "semantic_passes": 0,
              "tokens_per_s": 1658.7100913060772,
              "ttft_s": 0.30533062450000004
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1492938015,
              "format_passes": 0,
              "gpu_energy_j": 303.3824619009128,
              "semantic_passes": 0,
              "tokens_per_s": 1783.8509244947268,
              "ttft_s": 1.149087768
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.2835258245,
              "format_passes": 0,
              "gpu_energy_j": 613.4334452151106,
              "semantic_passes": 0,
              "tokens_per_s": 1795.0783948454969,
              "ttft_s": 2.2831275389999997
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254303281,
              "format_passes": 2,
              "gpu_energy_j": 57.11195447323874,
              "semantic_passes": 2,
              "tokens_per_s": 95.6884072031504,
              "ttft_s": 0.0766196355
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351178488,
              "format_passes": 0,
              "gpu_energy_j": 82.66991390728049,
              "semantic_passes": 2,
              "tokens_per_s": 96.11037791614007,
              "ttft_s": 0.070230185
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314796509,
              "format_passes": 0,
              "gpu_energy_j": 73.28745692855797,
              "semantic_passes": 0,
              "tokens_per_s": 95.87388606346201,
              "ttft_s": 0.074886302
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5820961255,
              "format_passes": 0,
              "gpu_energy_j": 143.2767386699444,
              "semantic_passes": 0,
              "tokens_per_s": 96.28309402637353,
              "ttft_s": 0.33504212099999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5446610510000001,
              "format_passes": 0,
              "gpu_energy_j": 131.759582559833,
              "semantic_passes": 0,
              "tokens_per_s": 95.87395870878669,
              "ttft_s": 0.29412664499999996
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
            "e2e_change_pct": -9.22336452546223,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -11.378482854485494,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09186552285600502,
            "ttft_change_pct": -36.342251649765956
          },
          "decode": {
            "e2e_change_pct": 0.0009733248121701621,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22554032611116215,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03140154487482061,
            "ttft_change_pct": 0.37367376462758006
          },
          "energy": {
            "e2e_change_pct": 0.5188607394013722,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.777984766463277,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4880441194319851,
            "ttft_change_pct": 0.6912856260212541
          },
          "filtering": {
            "e2e_change_pct": -17.83837996614842,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -24.201553745664373,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12548772293886623,
            "ttft_change_pct": -30.687354877720775
          },
          "german": {
            "e2e_change_pct": 0.00962215211446349,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7797750651124757,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4367240853733412,
            "ttft_change_pct": -0.6355441945924967
          },
          "ha_sim": {
            "e2e_change_pct": -0.3204578712250217,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.1007806669101523,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05041137453579703,
            "ttft_change_pct": -1.4105682287793075
          },
          "jarvis_memory": {
            "e2e_change_pct": 1.2004367536786686,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.19241585397952177,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4355878980933592,
            "ttft_change_pct": 3.294779075159182
          },
          "long_context": {
            "e2e_change_pct": 36.879042269146176,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 35.15613523599372,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0220776485165608,
            "ttft_change_pct": 43.597099203304104
          },
          "math": {
            "e2e_change_pct": 0.7995381820971703,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.832979304274403,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.27628708545626157,
            "ttft_change_pct": 1.526968342533408
          },
          "prefill": {
            "e2e_change_pct": 48.397249610001914,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 54.142089560992005,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -32.7054781472704,
            "ttft_change_pct": 48.40237320052163
          },
          "prefill2048": {
            "e2e_change_pct": 52.283763172672046,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 49.3128347963379,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -34.37506791644367,
            "ttft_change_pct": 52.30726903961087
          },
          "prefill4096": {
            "e2e_change_pct": 52.4132296900919,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 51.39112366909586,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -34.4139258122845,
            "ttft_change_pct": 52.41821965500024
          },
          "pve_sim": {
            "e2e_change_pct": 0.08701081707407354,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7719171864706054,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0209598923705423,
            "ttft_change_pct": 0.323162713356151
          },
          "sorting": {
            "e2e_change_pct": 0.016108222075916778,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8972325651204769,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.033734108290284226,
            "ttft_change_pct": 0.24699764565772053
          },
          "time": {
            "e2e_change_pct": -0.10886255613378193,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.8711279878607674,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.026802399829795043,
            "ttft_change_pct": -0.3716126787580709
          },
          "tool-call": {
            "e2e_change_pct": 5.709251386315173,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.788299083660563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1481303844926396,
            "ttft_change_pct": 10.423466087768007
          },
          "tool-final": {
            "e2e_change_pct": 3.879057294854027,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3867437124481574,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.011077109866430845,
            "ttft_change_pct": 7.448087721688079
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
