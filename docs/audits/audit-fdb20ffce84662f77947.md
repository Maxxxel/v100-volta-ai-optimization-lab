# Public audit excerpt

Original SHA256: `fdb20ffce84662f77947616ad0eaea941ad7a31b26c8fb851c83b15e6c67c89b`

Original file: `RESULTS.json`; 39734 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6683158475,
              "format_passes": 2,
              "gpu_energy_j": 177.17980520719124,
              "semantic_passes": 2,
              "tokens_per_s": 79.0239598872765,
              "ttft_s": 0.124170923
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659367832,
              "format_passes": 0,
              "gpu_energy_j": 454.916662899298,
              "semantic_passes": 0,
              "tokens_per_s": 79.57087435350024,
              "ttft_s": 0.06323683699999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23778718650000003,
              "format_passes": 2,
              "gpu_energy_j": 55.32111538808129,
              "semantic_passes": 2,
              "tokens_per_s": 78.26893205336276,
              "ttft_s": 0.07163868400000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241585553,
              "format_passes": 0,
              "gpu_energy_j": 60.39706985006043,
              "semantic_passes": 0,
              "tokens_per_s": 77.47871530444152,
              "ttft_s": 0.125407614
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.187729747,
              "format_passes": 2,
              "gpu_energy_j": 41.92200084055806,
              "semantic_passes": 2,
              "tokens_per_s": 76.27952715541988,
              "ttft_s": 0.0696945245
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35786380650000005,
              "format_passes": 0,
              "gpu_energy_j": 88.53134159329431,
              "semantic_passes": 0,
              "tokens_per_s": 78.88798151121867,
              "ttft_s": 0.078915446
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469371153,
              "format_passes": 0,
              "gpu_energy_j": 117.86601667020183,
              "semantic_passes": 2,
              "tokens_per_s": 79.07334585309059,
              "ttft_s": 0.1152520955
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0784797584999999,
              "format_passes": 2,
              "gpu_energy_j": 289.1594516743147,
              "semantic_passes": 2,
              "tokens_per_s": 78.03766488162705,
              "ttft_s": 0.8221491780000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23434426600000002,
              "format_passes": 0,
              "gpu_energy_j": 54.87933133776601,
              "semantic_passes": 0,
              "tokens_per_s": 78.28054847498302,
              "ttft_s": 0.06822355199999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19798629950000002,
              "format_passes": 0,
              "gpu_energy_j": 49.26060923123057,
              "semantic_passes": 0,
              "tokens_per_s": 2564.240503302998,
              "ttft_s": 0.197855687
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.716867194,
              "format_passes": 0,
              "gpu_energy_j": 189.0618984027555,
              "semantic_passes": 0,
              "tokens_per_s": 2861.870089001178,
              "ttft_s": 0.7166463325
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4171849265,
              "format_passes": 0,
              "gpu_energy_j": 379.4885495317643,
              "semantic_passes": 0,
              "tokens_per_s": 2893.706907499858,
              "ttft_s": 1.4168372704999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2959607615,
              "format_passes": 2,
              "gpu_energy_j": 74.22475788939946,
              "semantic_passes": 2,
              "tokens_per_s": 78.35025807527703,
              "ttft_s": 0.078959835
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3539148915,
              "format_passes": 2,
              "gpu_energy_j": 87.30463459192887,
              "semantic_passes": 2,
              "tokens_per_s": 78.69595680504702,
              "ttft_s": 0.07436822700000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3689763735,
              "format_passes": 2,
              "gpu_energy_j": 93.96677287104234,
              "semantic_passes": 2,
              "tokens_per_s": 78.89641248454151,
              "ttft_s": 0.07741744349999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6192296785,
              "format_passes": 0,
              "gpu_energy_j": 159.8710526161607,
              "semantic_passes": 0,
              "tokens_per_s": 79.03689945984004,
              "ttft_s": 0.31800402250000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560491658,
              "format_passes": 0,
              "gpu_energy_j": 145.46587516865847,
              "semantic_passes": 0,
              "tokens_per_s": 78.76535309561169,
              "ttft_s": 0.25613637749999996
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
              "e2e_s": 0.665808438,
              "format_passes": 2,
              "gpu_energy_j": 178.28075761159926,
              "semantic_passes": 2,
              "tokens_per_s": 79.32386652830651,
              "ttft_s": 0.1236845845
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657966837,
              "format_passes": 0,
              "gpu_energy_j": 457.59344758642794,
              "semantic_passes": 0,
              "tokens_per_s": 79.61935812953774,
              "ttft_s": 0.062821282
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237686882,
              "format_passes": 2,
              "gpu_energy_j": 58.0949801038214,
              "semantic_passes": 2,
              "tokens_per_s": 78.24196727047381,
              "ttft_s": 0.07152583800000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24164553700000002,
              "format_passes": 0,
              "gpu_energy_j": 61.749413843449176,
              "semantic_passes": 0,
              "tokens_per_s": 77.5591439387304,
              "ttft_s": 0.125561773
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18279744599999997,
              "format_passes": 2,
              "gpu_energy_j": 41.7693747978101,
              "semantic_passes": 2,
              "tokens_per_s": 77.39938117131302,
              "ttft_s": 0.066532602
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3574661225,
              "format_passes": 0,
              "gpu_energy_j": 90.36455977810428,
              "semantic_passes": 0,
              "tokens_per_s": 78.89504489939395,
              "ttft_s": 0.078613827
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469136009,
              "format_passes": 0,
              "gpu_energy_j": 117.90791931350648,
              "semantic_passes": 2,
              "tokens_per_s": 79.08727337483668,
              "ttft_s": 0.1151102705
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.07912066,
              "format_passes": 2,
              "gpu_energy_j": 287.6681306062954,
              "semantic_passes": 2,
              "tokens_per_s": 78.05898623804595,
              "ttft_s": 0.8228944455
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23330372100000002,
              "format_passes": 0,
              "gpu_energy_j": 57.13325665553815,
              "semantic_passes": 0,
              "tokens_per_s": 78.27320347925448,
              "ttft_s": 0.067195845
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19865098949999999,
              "format_passes": 0,
              "gpu_energy_j": 48.28178883379849,
              "semantic_passes": 0,
              "tokens_per_s": 2555.2901929480468,
              "ttft_s": 0.198516935
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.716871271,
              "format_passes": 0,
              "gpu_energy_j": 190.9624350838142,
              "semantic_passes": 0,
              "tokens_per_s": 2861.7975785708654,
              "ttft_s": 0.716625466
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.414351582,
              "format_passes": 0,
              "gpu_energy_j": 381.8490397335809,
              "semantic_passes": 0,
              "tokens_per_s": 2899.537944979924,
              "ttft_s": 1.4140357165
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2957868365,
              "format_passes": 2,
              "gpu_energy_j": 70.11146131359098,
              "semantic_passes": 2,
              "tokens_per_s": 78.48321317839648,
              "ttft_s": 0.079158541
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3528898235,
              "format_passes": 2,
              "gpu_energy_j": 87.13075001392265,
              "semantic_passes": 2,
              "tokens_per_s": 78.86194115306274,
              "ttft_s": 0.073904888
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3696630285,
              "format_passes": 2,
              "gpu_energy_j": 94.43539951303578,
              "semantic_passes": 2,
              "tokens_per_s": 78.97408832787387,
              "ttft_s": 0.078384817
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196624935,
              "format_passes": 0,
              "gpu_energy_j": 163.01199152915984,
              "semantic_passes": 0,
              "tokens_per_s": 78.97109755036115,
              "ttft_s": 0.318017134
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5603738524999999,
              "format_passes": 0,
              "gpu_energy_j": 146.66254179869958,
              "semantic_passes": 0,
              "tokens_per_s": 78.78487709282955,
              "ttft_s": 0.255617108
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
            "e2e_change_pct": -0.3751833073208588,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6213757844019341,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.37951355697412037,
            "ttft_change_pct": -0.39166858733908905
          },
          "decode": {
            "e2e_change_pct": -0.08442944192255109,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5884120994975595,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06093156124200583,
            "ttft_change_pct": -0.6571407105639748
          },
          "energy": {
            "e2e_change_pct": -0.042182466379458994,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.014115670447472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03445145114612247,
            "ttft_change_pct": -0.15752103988956323
          },
          "filtering": {
            "e2e_change_pct": 0.024829299291750928,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2390887451096964,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10380739274373774,
            "ttft_change_pct": 0.122926347996688
          },
          "german": {
            "e2e_change_pct": -2.6273412066123103,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3640714653111221,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4680924982812593,
            "ttft_change_pct": -4.536830579854234
          },
          "ha_sim": {
            "e2e_change_pct": -0.11112719218228095,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0706996548540024,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.008953693629853987,
            "ttft_change_pct": -0.38220527829241346
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.05009766759141998,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03555108120936179,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.017613421559237175,
            "ttft_change_pct": -0.12305633089334522
          },
          "long_context": {
            "e2e_change_pct": 0.05942638189997407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.515743497016663,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0273218790583174,
            "ttft_change_pct": 0.09064869490145178
          },
          "math": {
            "e2e_change_pct": -0.4440240923155314,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.107056815069221,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.009382912960675949,
            "ttft_change_pct": -1.5063815498788324
          },
          "prefill": {
            "e2e_change_pct": 0.3357252505242103,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9870245470117398,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3490433266077231,
            "ttft_change_pct": 0.3342072244807426
          },
          "prefill2048": {
            "e2e_change_pct": 0.0005687245886232262,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0052457407414783,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.002533673019999849,
            "ttft_change_pct": -0.0029116872652057424
          },
          "prefill4096": {
            "e2e_change_pct": -0.1999276486095214,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6220188210498412,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2015075357131968,
            "ttft_change_pct": -0.197732940707529
          },
          "pve_sim": {
            "e2e_change_pct": -0.058766236145135764,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.541677322730509,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16969325486040354,
            "ttft_change_pct": 0.251654527900147
          },
          "sorting": {
            "e2e_change_pct": -0.28963686598647564,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.19916992817045065,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21091852079124784,
            "ttft_change_pct": -0.6230335436126611
          },
          "time": {
            "e2e_change_pct": 0.18609728137510828,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4987152667641048,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09845294720793873,
            "ttft_change_pct": 1.2495549533355632
          },
          "tool-call": {
            "e2e_change_pct": 0.06989571317841392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9646701898812902,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0832546695639591,
            "ttft_change_pct": 0.004123061053395993
          },
          "tool-final": {
            "e2e_change_pct": -0.021018243236736733,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.822644230926084,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02478754484114276,
            "ttft_change_pct": -0.20273164829933688
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
