# Public audit excerpt

Original SHA256: `2c9fad9d997cda90aff610e7718dc68d1af96ec700d32a074f18476634d15236`

Original file: `RESULTS.json`; 39546 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.527087927,
              "format_passes": 2,
              "gpu_energy_j": 132.68344821425967,
              "semantic_passes": 2,
              "tokens_per_s": 96.34951373164304,
              "ttft_s": 0.13266712749999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.367796772,
              "format_passes": 0,
              "gpu_energy_j": 357.4336581412239,
              "semantic_passes": 0,
              "tokens_per_s": 97.01214092269733,
              "ttft_s": 0.058334753
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2049148615,
              "format_passes": 2,
              "gpu_energy_j": 46.60712506498465,
              "semantic_passes": 2,
              "tokens_per_s": 94.91547563164438,
              "ttft_s": 0.067906045
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2298049255,
              "format_passes": 0,
              "gpu_energy_j": 55.94147293270257,
              "semantic_passes": 0,
              "tokens_per_s": 93.96857875655336,
              "ttft_s": 0.1340557715
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1569968865,
              "format_passes": 2,
              "gpu_energy_j": 33.382786672636236,
              "semantic_passes": 2,
              "tokens_per_s": 93.77300834655935,
              "ttft_s": 0.060998319
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30667491550000003,
              "format_passes": 0,
              "gpu_energy_j": 73.02167454335977,
              "semantic_passes": 0,
              "tokens_per_s": 95.89672415808946,
              "ttft_s": 0.077221896
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398501075,
              "format_passes": 0,
              "gpu_energy_j": 90.66531669937675,
              "semantic_passes": 2,
              "tokens_per_s": 96.25086657247219,
              "ttft_s": 0.1075686605
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.031482967,
              "format_passes": 2,
              "gpu_energy_j": 279.31793821452015,
              "semantic_passes": 2,
              "tokens_per_s": 94.17333925333372,
              "ttft_s": 0.8722229195
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148488646,
              "format_passes": 0,
              "gpu_energy_j": 28.96005423132175,
              "semantic_passes": 0,
              "tokens_per_s": 93.89737533369727,
              "ttft_s": 0.063248044
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2066842265,
              "format_passes": 0,
              "gpu_energy_j": 50.64757522764732,
              "semantic_passes": 0,
              "tokens_per_s": 2456.036131411969,
              "ttft_s": 0.206514432
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7570559215,
              "format_passes": 0,
              "gpu_energy_j": 202.17908833012547,
              "semantic_passes": 0,
              "tokens_per_s": 2709.7977364941107,
              "ttft_s": 0.756831553
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4982994855,
              "format_passes": 0,
              "gpu_energy_j": 403.72092377633237,
              "semantic_passes": 0,
              "tokens_per_s": 2736.822701799272,
              "ttft_s": 1.4979629115000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2551291645,
              "format_passes": 2,
              "gpu_energy_j": 57.13345325177399,
              "semantic_passes": 2,
              "tokens_per_s": 95.20204718353719,
              "ttft_s": 0.0765635265
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351115544,
              "format_passes": 0,
              "gpu_energy_j": 84.37520189499196,
              "semantic_passes": 2,
              "tokens_per_s": 96.16001748871875,
              "ttft_s": 0.07027351849999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3147541775,
              "format_passes": 0,
              "gpu_energy_j": 74.93598283026327,
              "semantic_passes": 0,
              "tokens_per_s": 95.93366775469947,
              "ttft_s": 0.0749687
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5510275570000001,
              "format_passes": 0,
              "gpu_energy_j": 140.34043200602693,
              "semantic_passes": 0,
              "tokens_per_s": 96.1226060502911,
              "ttft_s": 0.303964679
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5248119645,
              "format_passes": 0,
              "gpu_energy_j": 133.06075621932806,
              "semantic_passes": 0,
              "tokens_per_s": 95.95222159739888,
              "ttft_s": 0.274722431
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
              "e2e_s": 0.526643452,
              "format_passes": 2,
              "gpu_energy_j": 131.39565846687827,
              "semantic_passes": 2,
              "tokens_per_s": 96.44904146820929,
              "ttft_s": 0.132618699
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3672301365,
              "format_passes": 0,
              "gpu_energy_j": 357.2727980548085,
              "semantic_passes": 0,
              "tokens_per_s": 97.03500833711458,
              "ttft_s": 0.0580542305
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2064788985,
              "format_passes": 2,
              "gpu_energy_j": 44.44418830586673,
              "semantic_passes": 2,
              "tokens_per_s": 94.00254147222935,
              "ttft_s": 0.0681658565
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229920799,
              "format_passes": 0,
              "gpu_energy_j": 54.93063456228879,
              "semantic_passes": 0,
              "tokens_per_s": 93.7924517030868,
              "ttft_s": 0.13394396349999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1573821325,
              "format_passes": 2,
              "gpu_energy_j": 32.67724604273088,
              "semantic_passes": 2,
              "tokens_per_s": 94.13391419080679,
              "ttft_s": 0.061745279
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3115401665,
              "format_passes": 0,
              "gpu_energy_j": 71.68611851607515,
              "semantic_passes": 0,
              "tokens_per_s": 94.41047326103734,
              "ttft_s": 0.0784894125
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3988740555,
              "format_passes": 0,
              "gpu_energy_j": 91.1370528494795,
              "semantic_passes": 2,
              "tokens_per_s": 96.06021320057454,
              "ttft_s": 0.107361191
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0317213255,
              "format_passes": 2,
              "gpu_energy_j": 273.7528648004876,
              "semantic_passes": 2,
              "tokens_per_s": 94.0002807878291,
              "ttft_s": 0.8721210625
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1487642295,
              "format_passes": 0,
              "gpu_energy_j": 30.051858213371887,
              "semantic_passes": 0,
              "tokens_per_s": 93.89679640000564,
              "ttft_s": 0.0635335595
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20604865449999998,
              "format_passes": 0,
              "gpu_energy_j": 51.09599633511203,
              "semantic_passes": 0,
              "tokens_per_s": 2463.529140769975,
              "ttft_s": 0.205900418
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.756002557,
              "format_passes": 0,
              "gpu_energy_j": 201.37747140848037,
              "semantic_passes": 0,
              "tokens_per_s": 2713.51787623942,
              "ttft_s": 0.7557697164999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4971840015,
              "format_passes": 0,
              "gpu_energy_j": 405.3850659670137,
              "semantic_passes": 0,
              "tokens_per_s": 2738.92181836467,
              "ttft_s": 1.496867054
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254183406,
              "format_passes": 2,
              "gpu_energy_j": 55.413699717952824,
              "semantic_passes": 2,
              "tokens_per_s": 95.6922396288353,
              "ttft_s": 0.0764499005
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35063357149999996,
              "format_passes": 0,
              "gpu_energy_j": 84.22289618447778,
              "semantic_passes": 2,
              "tokens_per_s": 96.21982539276749,
              "ttft_s": 0.0700059405
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3147265855,
              "format_passes": 0,
              "gpu_energy_j": 75.05591950032519,
              "semantic_passes": 0,
              "tokens_per_s": 95.99978467629785,
              "ttft_s": 0.0751142595
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5500946215,
              "format_passes": 0,
              "gpu_energy_j": 139.75285658115254,
              "semantic_passes": 0,
              "tokens_per_s": 96.21356084508513,
              "ttft_s": 0.303172594
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5250518005,
              "format_passes": 0,
              "gpu_energy_j": 134.5313404025407,
              "semantic_passes": 0,
              "tokens_per_s": 95.88129899818941,
              "ttft_s": 0.2748263685
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
            "e2e_change_pct": -0.08432653779982813,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9705730177451022,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10329863920586213,
            "ttft_change_pct": -0.03650376767219132
          },
          "decode": {
            "e2e_change_pct": -0.041426877998218536,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04500417986708083,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.023571703706104508,
            "ttft_change_pct": -0.48088401094285027
          },
          "energy": {
            "e2e_change_pct": 0.7632618681490788,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.640785622589084,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9618391029909801,
            "ttft_change_pct": 0.38260437638504285
          },
          "filtering": {
            "e2e_change_pct": 0.05042254849321193,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8069570167196236,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1874318583905077,
            "ttft_change_pct": -0.08340409275107152
          },
          "german": {
            "e2e_change_pct": 0.2453844841056707,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.113486321031688,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.384871777722684,
            "ttft_change_pct": 1.2245583357797019
          },
          "ha_sim": {
            "e2e_change_pct": 1.586452218326273,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.828985757498025,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.549845325896615,
            "ttft_change_pct": 1.6413952073903948
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.09359585792836356,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5203049713783159,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1980796419677966,
            "ttft_change_pct": -0.19287169612007826
          },
          "long_context": {
            "e2e_change_pct": 0.0231083311722724,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9923795262152155,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18376587989418214,
            "ttft_change_pct": -0.011677863275871836
          },
          "math": {
            "e2e_change_pct": 0.18559230447829922,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.770034314608761,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.000616560036492686,
            "ttft_change_pct": 0.4514218653149271
          },
          "prefill": {
            "e2e_change_pct": -0.30750871063691676,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.885375273049438,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.30508546931262703,
            "ttft_change_pct": -0.2973225619408493
          },
          "prefill2048": {
            "e2e_change_pct": -0.13913958930708015,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.39648854303674375,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13728477573098363,
            "ttft_change_pct": -0.14030024194831014
          },
          "prefill4096": {
            "e2e_change_pct": -0.07445000220551723,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.41220112525137687,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07669903366476216,
            "ttft_change_pct": -0.07315651753372343
          },
          "pve_sim": {
            "e2e_change_pct": -0.37069791760322435,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0100640446895643,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5148969584163332,
            "ttft_change_pct": -0.14840747963719148
          },
          "sorting": {
            "e2e_change_pct": -0.13726891567068522,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.18051003979075997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06219622833965044,
            "ttft_change_pct": -0.38076647606593017
          },
          "time": {
            "e2e_change_pct": -0.008766206129229293,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1600521745789063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06891941395115175,
            "ttft_change_pct": 0.194160362924789
          },
          "tool-call": {
            "e2e_change_pct": -0.16930832009188768,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.41867864910745123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09462372955892917,
            "ttft_change_pct": -0.2605845529835338
          },
          "tool-final": {
            "e2e_change_pct": 0.045699415452249426,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.105197524045809,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07391449413964857,
            "ttft_change_pct": 0.03783364162206482
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
