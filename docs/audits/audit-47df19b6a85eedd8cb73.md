# Public audit excerpt

Original SHA256: `47df19b6a85eedd8cb733433f41aa4c96dddc6e65cf776a636850647360686fa`

Original file: `RESULTS.json`; 44293 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.478447895,
              "format_passes": 2,
              "gpu_energy_j": 116.46944848945267,
              "semantic_passes": 2,
              "tokens_per_s": 96.44498704036243,
              "ttft_s": 0.084451973
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3673966590000002,
              "format_passes": 0,
              "gpu_energy_j": 359.91842899341793,
              "semantic_passes": 0,
              "tokens_per_s": 96.97584288087864,
              "ttft_s": 0.0577345145
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2049319695,
              "format_passes": 2,
              "gpu_energy_j": 42.36322995484343,
              "semantic_passes": 2,
              "tokens_per_s": 94.91071533993684,
              "ttft_s": 0.067910887
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.188520285,
              "format_passes": 0,
              "gpu_energy_j": 39.28449366906909,
              "semantic_passes": 0,
              "tokens_per_s": 93.86431411146657,
              "ttft_s": 0.0925745895
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15681529649999998,
              "format_passes": 2,
              "gpu_energy_j": 33.80124192442249,
              "semantic_passes": 2,
              "tokens_per_s": 93.94574191068617,
              "ttft_s": 0.060984013
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.305988138,
              "format_passes": 0,
              "gpu_energy_j": 71.1276876607033,
              "semantic_passes": 0,
              "tokens_per_s": 95.78135189640403,
              "ttft_s": 0.076243645
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398935905,
              "format_passes": 0,
              "gpu_energy_j": 92.16714467572535,
              "semantic_passes": 2,
              "tokens_per_s": 96.08901666635887,
              "ttft_s": 0.10749405949999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.412278153,
              "format_passes": 2,
              "gpu_energy_j": 372.30158781306284,
              "semantic_passes": 2,
              "tokens_per_s": 94.28786401135334,
              "ttft_s": 1.25315784
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149179112,
              "format_passes": 0,
              "gpu_energy_j": 30.068483576589006,
              "semantic_passes": 0,
              "tokens_per_s": 93.31461667675435,
              "ttft_s": 0.0634200895
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.305320406,
              "format_passes": 0,
              "gpu_energy_j": 77.69397013465769,
              "semantic_passes": 0,
              "tokens_per_s": 1659.8391014064227,
              "ttft_s": 0.30518906749999997
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1489958310000001,
              "format_passes": 0,
              "gpu_energy_j": 311.62239374834314,
              "semantic_passes": 0,
              "tokens_per_s": 1784.395698355267,
              "ttft_s": 1.1487409720000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.282970411,
              "format_passes": 0,
              "gpu_energy_j": 623.7279685506206,
              "semantic_passes": 0,
              "tokens_per_s": 1795.5489592508643,
              "ttft_s": 2.2826092115
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.253855066,
              "format_passes": 2,
              "gpu_energy_j": 57.23686258772079,
              "semantic_passes": 2,
              "tokens_per_s": 95.68224115362078,
              "ttft_s": 0.07613603099999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351678879,
              "format_passes": 0,
              "gpu_energy_j": 84.77226082988295,
              "semantic_passes": 2,
              "tokens_per_s": 96.02168648411057,
              "ttft_s": 0.07047313799999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3153637545,
              "format_passes": 0,
              "gpu_energy_j": 75.38160300867585,
              "semantic_passes": 0,
              "tokens_per_s": 95.69721365090533,
              "ttft_s": 0.07498262850000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.582479052,
              "format_passes": 0,
              "gpu_energy_j": 144.9364448626942,
              "semantic_passes": 0,
              "tokens_per_s": 96.31493633708354,
              "ttft_s": 0.3356024225
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.544176369,
              "format_passes": 0,
              "gpu_energy_j": 133.44293731483435,
              "semantic_passes": 0,
              "tokens_per_s": 95.96641648218532,
              "ttft_s": 0.2940354465
            }
          }
        },
        "B": {
          "format_passes": 8,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4801251595,
              "format_passes": 2,
              "gpu_energy_j": 119.34316614731739,
              "semantic_passes": 2,
              "tokens_per_s": 96.5919800311014,
              "ttft_s": 0.0866603635
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3655912905,
              "format_passes": 0,
              "gpu_energy_j": 361.43886387954046,
              "semantic_passes": 0,
              "tokens_per_s": 97.07914406243654,
              "ttft_s": 0.057417169000000004
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204983123,
              "format_passes": 2,
              "gpu_energy_j": 43.75160789220821,
              "semantic_passes": 2,
              "tokens_per_s": 95.05520469088165,
              "ttft_s": 0.0681670565
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.19062129449999998,
              "format_passes": 0,
              "gpu_energy_j": 42.6879278676805,
              "semantic_passes": 0,
              "tokens_per_s": 94.30502735451535,
              "ttft_s": 0.09514355199999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1567456585,
              "format_passes": 2,
              "gpu_energy_j": 32.765198713179494,
              "semantic_passes": 2,
              "tokens_per_s": 93.70412411403234,
              "ttft_s": 0.060665603
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3055538815,
              "format_passes": 0,
              "gpu_energy_j": 69.81581021639828,
              "semantic_passes": 0,
              "tokens_per_s": 95.89002680000644,
              "ttft_s": 0.07608132349999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.399104007,
              "format_passes": 0,
              "gpu_energy_j": 94.6438849341992,
              "semantic_passes": 2,
              "tokens_per_s": 96.25102326878212,
              "ttft_s": 0.108167892
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.6097876580000001,
              "format_passes": 0,
              "gpu_energy_j": 430.49505293175184,
              "semantic_passes": 2,
              "tokens_per_s": 95.15604353185088,
              "ttft_s": 1.34698578
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14930701,
              "format_passes": 0,
              "gpu_energy_j": 30.03784420375915,
              "semantic_passes": 0,
              "tokens_per_s": 93.56499928892987,
              "ttft_s": 0.0637762325
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.32492508750000004,
              "format_passes": 0,
              "gpu_energy_j": 83.81267933449911,
              "semantic_passes": 0,
              "tokens_per_s": 1559.226688886788,
              "ttft_s": 0.32473569150000003
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.225342222,
              "format_passes": 0,
              "gpu_energy_j": 343.7492193987514,
              "semantic_passes": 0,
              "tokens_per_s": 1673.102147207243,
              "ttft_s": 1.225099087
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.436207938,
              "format_passes": 0,
              "gpu_energy_j": 680.394486066923,
              "semantic_passes": 0,
              "tokens_per_s": 1682.5003714306786,
              "ttft_s": 2.435851285
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25473300050000003,
              "format_passes": 2,
              "gpu_energy_j": 60.42462985097286,
              "semantic_passes": 2,
              "tokens_per_s": 95.44237103701943,
              "ttft_s": 0.07658980700000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35068818749999997,
              "format_passes": 0,
              "gpu_energy_j": 84.49713445415713,
              "semantic_passes": 2,
              "tokens_per_s": 96.14103743365126,
              "ttft_s": 0.069834212
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31469545600000004,
              "format_passes": 0,
              "gpu_energy_j": 76.44588180436632,
              "semantic_passes": 0,
              "tokens_per_s": 95.92253277710827,
              "ttft_s": 0.074906334
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.59562885,
              "format_passes": 0,
              "gpu_energy_j": 152.41462329111715,
              "semantic_passes": 0,
              "tokens_per_s": 96.38456404555619,
              "ttft_s": 0.34890786949999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5522985205,
              "format_passes": 0,
              "gpu_energy_j": 139.53487247323437,
              "semantic_passes": 0,
              "tokens_per_s": 95.93764105832534,
              "ttft_s": 0.302076953
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": -2,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.35056367005230626,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.46735748742295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1524112297069946,
            "ttft_change_pct": 2.6149661417620207
          },
          "decode": {
            "e2e_change_pct": -0.13202961175292627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.42243874268252934,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10652259211068049,
            "ttft_change_pct": -0.549663408012202
          },
          "energy": {
            "e2e_change_pct": 0.024961210359131236,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.277318417043995,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15223713194796318,
            "ttft_change_pct": 0.3772141865854284
          },
          "filtering": {
            "e2e_change_pct": 1.1144739676157256,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.663556229798441,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.46952161449282936,
            "ttft_change_pct": 2.7750190563901933
          },
          "german": {
            "e2e_change_pct": -0.044407657641987175,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0651039791955825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2571886620295505,
            "ttft_change_pct": -0.5221204449107009
          },
          "ha_sim": {
            "e2e_change_pct": -0.1419193903523186,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.844397712692425,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11346144259891666,
            "ttft_change_pct": -0.2128983995977718
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.04213759601308098,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.687226849858315,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1686005415018066,
            "ttft_change_pct": 0.6268555705629675
          },
          "long_context": {
            "e2e_change_pct": 13.985170313683959,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 15.63073245551363,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9207754673422386,
            "ttft_change_pct": 7.487320192642288
          },
          "math": {
            "e2e_change_pct": 0.08573452294045047,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.10189863001176525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2683208923665692,
            "ttft_change_pct": 0.5615618060583305
          },
          "prefill": {
            "e2e_change_pct": 6.421019072010559,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.875397780853,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -6.0615762355750835,
            "ttft_change_pct": 6.404758912276587
          },
          "prefill2048": {
            "e2e_change_pct": 6.644618626122756,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.309536893023452,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -6.237044353480947,
            "ttft_change_pct": 6.647113392939885
          },
          "prefill4096": {
            "e2e_change_pct": 6.712199433757782,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.085133323102458,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -6.296045966206998,
            "ttft_change_pct": 6.713460750440858
          },
          "pve_sim": {
            "e2e_change_pct": 0.3458408429005022,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.569430466889269,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2506945005774197,
            "ttft_change_pct": 0.5960069024349535
          },
          "sorting": {
            "e2e_change_pct": -0.28170344002945713,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.32454764451538276,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12429582723527677,
            "ttft_change_pct": -0.9066234570113574
          },
          "time": {
            "e2e_change_pct": -0.21191354125634776,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4118548202908032,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.235450038310292,
            "ttft_change_pct": -0.10174956723476569
          },
          "tool-call": {
            "e2e_change_pct": 2.2575572382987463,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.159625955712799,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07229170377995864,
            "ttft_change_pct": 3.964645696203206
          },
          "tool-final": {
            "e2e_change_pct": 1.4925586561073123,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.565198639196022,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.029984889417355998,
            "ttft_change_pct": 2.7348765584968238
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 345541638816800,
          "end_ns": 345542346507835,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 345586800294527,
          "end_ns": 345587459712565,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
