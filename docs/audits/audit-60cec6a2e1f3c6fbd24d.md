# Public audit excerpt

Original SHA256: `60cec6a2e1f3c6fbd24d7cf6fb6bfbe361b9ab7fa0066e391bd17b2e252a8d0f`

Original file: `RESULTS.json`; 39870 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.795701034,
              "format_passes": 2,
              "gpu_energy_j": 483.12597921679003,
              "semantic_passes": 2,
              "tokens_per_s": 35.31176346565006,
              "ttft_s": 0.5451753815
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7839551765,
              "format_passes": 0,
              "gpu_energy_j": 1067.8938220025718,
              "semantic_passes": 0,
              "tokens_per_s": 35.4025052384625,
              "ttft_s": 0.1945062525
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6030824825000001,
              "format_passes": 2,
              "gpu_energy_j": 151.6754840441907,
              "semantic_passes": 2,
              "tokens_per_s": 34.790302892300346,
              "ttft_s": 0.22559074899999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9481628995,
              "format_passes": 0,
              "gpu_energy_j": 249.09359727614245,
              "semantic_passes": 0,
              "tokens_per_s": 34.75933030168927,
              "ttft_s": 0.5406532
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4942534785,
              "format_passes": 2,
              "gpu_energy_j": 109.29659337436517,
              "semantic_passes": 2,
              "tokens_per_s": 33.72991471560234,
              "ttft_s": 0.225695189
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.031526288,
              "format_passes": 0,
              "gpu_energy_j": 264.5259086100293,
              "semantic_passes": 0,
              "tokens_per_s": 34.92852871240491,
              "ttft_s": 0.256869597
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1690094439999998,
              "format_passes": 0,
              "gpu_energy_j": 297.15145613137577,
              "semantic_passes": 2,
              "tokens_per_s": 35.13249782386753,
              "ttft_s": 0.3679419605
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8091124185,
              "format_passes": 2,
              "gpu_energy_j": 1017.6426620982728,
              "semantic_passes": 2,
              "tokens_per_s": 34.208952629456505,
              "ttft_s": 3.2219625785000003
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.591625701,
              "format_passes": 2,
              "gpu_energy_j": 142.38681404907982,
              "semantic_passes": 2,
              "tokens_per_s": 34.87142929517137,
              "ttft_s": 0.2163793
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7258834285,
              "format_passes": 0,
              "gpu_energy_j": 187.58754270076588,
              "semantic_passes": 0,
              "tokens_per_s": 696.8035380302415,
              "ttft_s": 0.7257128475000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.748663392,
              "format_passes": 0,
              "gpu_energy_j": 733.0092550584075,
              "semantic_passes": 0,
              "tokens_per_s": 745.4178178435268,
              "ttft_s": 2.7484517145
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4497624515,
              "format_passes": 0,
              "gpu_energy_j": 1478.0324278907683,
              "semantic_passes": 0,
              "tokens_per_s": 751.831906172269,
              "ttft_s": 5.449430490499999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.883554907,
              "format_passes": 0,
              "gpu_energy_j": 228.7969806857668,
              "semantic_passes": 2,
              "tokens_per_s": 35.07606224594953,
              "ttft_s": 0.2335212295
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.995415137,
              "format_passes": 0,
              "gpu_energy_j": 260.4442213463858,
              "semantic_passes": 2,
              "tokens_per_s": 35.00508945386206,
              "ttft_s": 0.221959165
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0305328994999998,
              "format_passes": 0,
              "gpu_energy_j": 274.7274391360639,
              "semantic_passes": 2,
              "tokens_per_s": 35.20029581704685,
              "ttft_s": 0.233759476
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.706514117,
              "format_passes": 0,
              "gpu_energy_j": 463.79771054519824,
              "semantic_passes": 0,
              "tokens_per_s": 35.05700973510065,
              "ttft_s": 1.0291887915000002
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7786906729999998,
              "format_passes": 0,
              "gpu_energy_j": 466.33643640060177,
              "semantic_passes": 0,
              "tokens_per_s": 35.07206887379874,
              "ttft_s": 1.094024552
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.4794059339999999,
              "format_passes": 2,
              "gpu_energy_j": 409.6166511800121,
              "semantic_passes": 2,
              "tokens_per_s": 35.4030451692344,
              "ttft_s": 0.23653819599999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.786844383,
              "format_passes": 0,
              "gpu_energy_j": 1071.1395998980042,
              "semantic_passes": 0,
              "tokens_per_s": 35.3445468094302,
              "ttft_s": 0.193944686
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5810773305,
              "format_passes": 2,
              "gpu_energy_j": 149.48825843825549,
              "semantic_passes": 2,
              "tokens_per_s": 34.89476206667212,
              "ttft_s": 0.2085199485
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6584603019999999,
              "format_passes": 0,
              "gpu_energy_j": 177.0670682131414,
              "semantic_passes": 0,
              "tokens_per_s": 34.93768276602971,
              "ttft_s": 0.2576911125
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46737079400000003,
              "format_passes": 2,
              "gpu_energy_j": 108.73598057088554,
              "semantic_passes": 2,
              "tokens_per_s": 34.20719753440109,
              "ttft_s": 0.204260096
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9877066845,
              "format_passes": 0,
              "gpu_energy_j": 262.2583774146252,
              "semantic_passes": 0,
              "tokens_per_s": 35.3162471496703,
              "ttft_s": 0.2231513075
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.149959467,
              "format_passes": 0,
              "gpu_energy_j": 294.964382064737,
              "semantic_passes": 2,
              "tokens_per_s": 35.28293056962903,
              "ttft_s": 0.35639136849999997
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 4.5166777955,
              "format_passes": 0,
              "gpu_energy_j": 1273.0192878257221,
              "semantic_passes": 2,
              "tokens_per_s": 34.553408724540574,
              "ttft_s": 3.7930569255
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.573660991,
              "format_passes": 2,
              "gpu_energy_j": 145.9369750474121,
              "semantic_passes": 2,
              "tokens_per_s": 34.999431852944674,
              "ttft_s": 0.20221801
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.9238234845,
              "format_passes": 0,
              "gpu_energy_j": 248.4796128751544,
              "semantic_passes": 0,
              "tokens_per_s": 547.2976206495654,
              "ttft_s": 0.9236370295
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.504137963,
              "format_passes": 0,
              "gpu_energy_j": 983.3573775014027,
              "semantic_passes": 0,
              "tokens_per_s": 584.6690261898423,
              "ttft_s": 3.5038765715
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 6.9710398295000005,
              "format_passes": 0,
              "gpu_energy_j": 1977.3362840705383,
              "semantic_passes": 0,
              "tokens_per_s": 587.7152875236254,
              "ttft_s": 6.970730119
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8456606234999999,
              "format_passes": 0,
              "gpu_energy_j": 222.5193694054583,
              "semantic_passes": 2,
              "tokens_per_s": 35.24111226414638,
              "ttft_s": 0.2213977885
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9855202825,
              "format_passes": 0,
              "gpu_energy_j": 262.4456184784983,
              "semantic_passes": 2,
              "tokens_per_s": 35.05210279255441,
              "ttft_s": 0.2152025045
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.016535387,
              "format_passes": 0,
              "gpu_energy_j": 274.93573788471633,
              "semantic_passes": 2,
              "tokens_per_s": 35.222210778526275,
              "ttft_s": 0.22153670050000002
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6781191965,
              "format_passes": 0,
              "gpu_energy_j": 456.43809107511305,
              "semantic_passes": 0,
              "tokens_per_s": 34.9601130136614,
              "ttft_s": 0.997554667
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.528288094,
              "format_passes": 0,
              "gpu_energy_j": 417.4574956817086,
              "semantic_passes": 0,
              "tokens_per_s": 35.008807582587195,
              "ttft_s": 0.842719321
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": -2,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -17.61401781316789,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.215354006825732,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.25850225144699035,
            "ttft_change_pct": -56.61245829751393
          },
          "decode": {
            "e2e_change_pct": 0.07635414177058486,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.30394200514669567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16371278993367877,
            "ttft_change_pct": -0.2887138550983104
          },
          "energy": {
            "e2e_change_pct": -3.6487798333621924,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4420429377353883,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.30025370775055293,
            "ttft_change_pct": -7.567154493555927
          },
          "filtering": {
            "e2e_change_pct": -30.554095467431864,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -28.91544778774592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5131067336236139,
            "ttft_change_pct": -52.33707809368371
          },
          "german": {
            "e2e_change_pct": -5.439048113851563,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5129279753115501,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4150134170898943,
            "ttft_change_pct": -9.497363720943108
          },
          "ha_sim": {
            "e2e_change_pct": -4.248035557577568,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8572057108957698,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.1100336932534205,
            "ttft_change_pct": -13.126617510907678
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.6295828145593605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7360132422409627,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.42818687847268055,
            "ttft_change_pct": -3.139242935028075
          },
          "long_context": {
            "e2e_change_pct": 18.575597127654063,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 25.09492135489775,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.006917980843025,
            "ttft_change_pct": 17.725045933521532
          },
          "math": {
            "e2e_change_pct": -3.0364992544500646,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4933214652225866,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3670700064795751,
            "ttft_change_pct": -6.544660233210841
          },
          "prefill": {
            "e2e_change_pct": 27.26884899535904,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 32.46061508013982,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -21.455964159324846,
            "ttft_change_pct": 27.273071254260795
          },
          "prefill2048": {
            "e2e_change_pct": 27.48516144969997,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 34.15347360423806,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -21.564924771818085,
            "ttft_change_pct": 27.48546947412638
          },
          "prefill4096": {
            "e2e_change_pct": 27.914563094053424,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 33.781657747002434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -21.828897829595316,
            "ttft_change_pct": 27.916671864189937
          },
          "pve_sim": {
            "e2e_change_pct": -4.288843081486049,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.7437474312348,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4705488804288782,
            "ttft_change_pct": -5.1915798088070675
          },
          "sorting": {
            "e2e_change_pct": -0.9940430009755752,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.768455188510675,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13430429524914356,
            "ttft_change_pct": -3.0441007020368005
          },
          "time": {
            "e2e_change_pct": -1.358279052206024,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07582014716385199,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06225789008516003,
            "ttft_change_pct": -5.228782896484585
          },
          "tool-call": {
            "e2e_change_pct": -1.6639136012491562,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5868166881276569,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.27639756548384353,
            "ttft_change_pct": -3.073695007297428
          },
          "tool-final": {
            "e2e_change_pct": -14.077916008726932,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -10.481475798066132,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18037513395398053,
            "ttft_change_pct": -22.970712178313157
          }
        }
      },
      "complete": true
    }
  }
}
```
