# Public audit excerpt

Original SHA256: `dc1ae21055fd77c4f30d490bd6b6c5ae6a31e1a5e355ce95b6b4640db15bc7dd`

Original file: `RESULTS.json`; 39708 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.527172643,
              "format_passes": 2,
              "gpu_energy_j": 132.20011472664817,
              "semantic_passes": 2,
              "tokens_per_s": 96.24969849467149,
              "ttft_s": 0.1323633115
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3671410334999998,
              "format_passes": 0,
              "gpu_energy_j": 358.7668657062753,
              "semantic_passes": 0,
              "tokens_per_s": 97.03037396451364,
              "ttft_s": 0.057782825999999995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204793188,
              "format_passes": 2,
              "gpu_energy_j": 42.41773724236701,
              "semantic_passes": 2,
              "tokens_per_s": 94.98933680929534,
              "ttft_s": 0.06787992200000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22991946200000002,
              "format_passes": 0,
              "gpu_energy_j": 54.81430562323759,
              "semantic_passes": 0,
              "tokens_per_s": 93.67374045831416,
              "ttft_s": 0.133820606
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156785909,
              "format_passes": 2,
              "gpu_energy_j": 30.812403566639226,
              "semantic_passes": 2,
              "tokens_per_s": 93.98929435605572,
              "ttft_s": 0.060980969499999996
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3066444655,
              "format_passes": 0,
              "gpu_energy_j": 71.89365820214951,
              "semantic_passes": 0,
              "tokens_per_s": 95.87915741884036,
              "ttft_s": 0.0771765365
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3986284075,
              "format_passes": 0,
              "gpu_energy_j": 94.37984394396528,
              "semantic_passes": 2,
              "tokens_per_s": 96.19504643118381,
              "ttft_s": 0.10755443049999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0325066155,
              "format_passes": 2,
              "gpu_energy_j": 268.7330240496313,
              "semantic_passes": 2,
              "tokens_per_s": 94.0619438307408,
              "ttft_s": 0.872969801
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14861044950000002,
              "format_passes": 0,
              "gpu_energy_j": 32.144286819021815,
              "semantic_passes": 0,
              "tokens_per_s": 93.69237838079476,
              "ttft_s": 0.06320276999999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205846628,
              "format_passes": 0,
              "gpu_energy_j": 50.8576343103822,
              "semantic_passes": 0,
              "tokens_per_s": 2466.5469716180733,
              "ttft_s": 0.20566575450000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.756904996,
              "format_passes": 0,
              "gpu_energy_j": 198.84073233145028,
              "semantic_passes": 0,
              "tokens_per_s": 2710.0085493703923,
              "ttft_s": 0.7566720245
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.499807002,
              "format_passes": 0,
              "gpu_energy_j": 404.09058518690136,
              "semantic_passes": 0,
              "tokens_per_s": 2734.2561128452962,
              "ttft_s": 1.4994881754999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2543170145,
              "format_passes": 2,
              "gpu_energy_j": 57.72285612882675,
              "semantic_passes": 2,
              "tokens_per_s": 95.64665200963788,
              "ttft_s": 0.0765364225
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35050439600000005,
              "format_passes": 0,
              "gpu_energy_j": 82.13306644765937,
              "semantic_passes": 2,
              "tokens_per_s": 96.21214656486242,
              "ttft_s": 0.069826745
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31437601699999995,
              "format_passes": 0,
              "gpu_energy_j": 76.59000217059787,
              "semantic_passes": 0,
              "tokens_per_s": 95.97290899782169,
              "ttft_s": 0.0746867325
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5503278155,
              "format_passes": 0,
              "gpu_energy_j": 140.1107232715019,
              "semantic_passes": 0,
              "tokens_per_s": 96.2316633039376,
              "ttft_s": 0.303889022
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5245937355,
              "format_passes": 0,
              "gpu_energy_j": 134.27075973458187,
              "semantic_passes": 0,
              "tokens_per_s": 95.9025700768562,
              "ttft_s": 0.27433951199999995
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
              "e2e_s": 0.5674392985,
              "format_passes": 2,
              "gpu_energy_j": 141.1889703968397,
              "semantic_passes": 2,
              "tokens_per_s": 96.48895105028839,
              "ttft_s": 0.132138875
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3670163149999999,
              "format_passes": 0,
              "gpu_energy_j": 355.7087680985747,
              "semantic_passes": 0,
              "tokens_per_s": 96.99629464622794,
              "ttft_s": 0.057683841
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.207262838,
              "format_passes": 2,
              "gpu_energy_j": 45.84459965848575,
              "semantic_passes": 2,
              "tokens_per_s": 93.66845469941528,
              "ttft_s": 0.068438345
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23289808499999998,
              "format_passes": 0,
              "gpu_energy_j": 55.60465935423127,
              "semantic_passes": 0,
              "tokens_per_s": 91.62627327125287,
              "ttft_s": 0.13468391899999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1564485105,
              "format_passes": 2,
              "gpu_energy_j": 31.897143669320087,
              "semantic_passes": 2,
              "tokens_per_s": 94.11298958379908,
              "ttft_s": 0.060783965499999995
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30656083050000005,
              "format_passes": 0,
              "gpu_energy_j": 73.06363572465357,
              "semantic_passes": 0,
              "tokens_per_s": 95.85701811111862,
              "ttft_s": 0.077017667
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4014587465,
              "format_passes": 0,
              "gpu_energy_j": 93.45184691804184,
              "semantic_passes": 2,
              "tokens_per_s": 95.75831352407573,
              "ttft_s": 0.109084716
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0327614755,
              "format_passes": 2,
              "gpu_energy_j": 276.90379923464855,
              "semantic_passes": 2,
              "tokens_per_s": 93.45014164441372,
              "ttft_s": 0.872209227
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14880219449999998,
              "format_passes": 0,
              "gpu_energy_j": 32.012699085544476,
              "semantic_passes": 0,
              "tokens_per_s": 93.546358014265,
              "ttft_s": 0.063279405
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20619440249999998,
              "format_passes": 0,
              "gpu_energy_j": 50.403443606975735,
              "semantic_passes": 0,
              "tokens_per_s": 2461.292148465876,
              "ttft_s": 0.20606247300000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7562803555,
              "format_passes": 0,
              "gpu_energy_j": 201.11956388446163,
              "semantic_passes": 0,
              "tokens_per_s": 2712.448212232521,
              "ttft_s": 0.7560523530000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5011175890000001,
              "format_passes": 0,
              "gpu_energy_j": 406.5041596961871,
              "semantic_passes": 0,
              "tokens_per_s": 2731.718897498138,
              "ttft_s": 1.5008002285
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2570579655,
              "format_passes": 2,
              "gpu_energy_j": 57.8236645945841,
              "semantic_passes": 2,
              "tokens_per_s": 94.11065587237039,
              "ttft_s": 0.0762894745
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3524658085,
              "format_passes": 0,
              "gpu_energy_j": 86.00160724585248,
              "semantic_passes": 2,
              "tokens_per_s": 95.79721420133592,
              "ttft_s": 0.07055990449999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314430509,
              "format_passes": 0,
              "gpu_energy_j": 74.57083484389027,
              "semantic_passes": 0,
              "tokens_per_s": 96.04336145813309,
              "ttft_s": 0.074887514
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5507281625,
              "format_passes": 0,
              "gpu_energy_j": 137.24765941827735,
              "semantic_passes": 0,
              "tokens_per_s": 95.99232898219755,
              "ttft_s": 0.3031812145
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5046542125,
              "format_passes": 0,
              "gpu_energy_j": 127.03813755784108,
              "semantic_passes": 0,
              "tokens_per_s": 95.68399934503765,
              "ttft_s": 0.27451247300000003
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
            "e2e_change_pct": 7.63822934188183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.799431066136297,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.24857486242426674,
            "ttft_change_pct": -0.16956095874044452
          },
          "decode": {
            "e2e_change_pct": -0.009122577476927685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8523913159261265,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03512231983994196,
            "ttft_change_pct": -0.17130522484309907
          },
          "energy": {
            "e2e_change_pct": 1.2059239001641187,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.078843047516383,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.3905583029092172,
            "ttft_change_pct": 0.8226629959886989
          },
          "filtering": {
            "e2e_change_pct": 1.2955071197930934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4418749302894218,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.1857429595996902,
            "ttft_change_pct": 0.6451271039678019
          },
          "german": {
            "e2e_change_pct": -0.21519695370073588,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5204657122410055,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13160565635781385,
            "ttft_change_pct": -0.3230581632520657
          },
          "ha_sim": {
            "e2e_change_pct": -0.02727425713149323,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6273723604581791,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02309084509892756,
            "ttft_change_pct": -0.20585207266978767
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.7100193931863785,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9832576397079129,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.45400768886837417,
            "ttft_change_pct": 1.4228009881936066
          },
          "long_context": {
            "e2e_change_pct": 0.02468361908525285,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.0404804969218047,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.650424774793068,
            "ttft_change_pct": -0.0871248924222523
          },
          "math": {
            "e2e_change_pct": 0.1290252473127529,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.40936585159969674,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15585084833292795,
            "ttft_change_pct": 0.12125259699853341
          },
          "prefill": {
            "e2e_change_pct": 0.16894835896945626,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8930629777912147,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21304370898520553,
            "ttft_change_pct": 0.192894777725372
          },
          "prefill2048": {
            "e2e_change_pct": -0.08252561461492558,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1460587206109984,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09002417585346478,
            "ttft_change_pct": -0.08189433201385432
          },
          "prefill4096": {
            "e2e_change_pct": 0.08738370992082967,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5972855091809226,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09279362438794347,
            "ttft_change_pct": 0.08750005644844183
          },
          "pve_sim": {
            "e2e_change_pct": 1.0777694152272366,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17464219984604235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.605906850887695,
            "ttft_change_pct": -0.32265422387623977
          },
          "sorting": {
            "e2e_change_pct": 0.55959711843383,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.7100893288312795,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.43126816970742166,
            "ttft_change_pct": 1.0499694637061907
          },
          "time": {
            "e2e_change_pct": 0.017333383290507598,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.6363327712278672,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07340869527356908,
            "ttft_change_pct": 0.26883154916437224
          },
          "tool-call": {
            "e2e_change_pct": 0.07274700437160941,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.043429500878824,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.24870641691407958,
            "ttft_change_pct": -0.23291644276639545
          },
          "tool-final": {
            "e2e_change_pct": -3.8009456939083086,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.386595109045178,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2279091495080765,
            "ttft_change_pct": 0.06304633216671629
          }
        }
      },
      "complete": true
    }
  }
}
```
