# Public audit excerpt

Original SHA256: `80eef66d7e1c048abf399469ab9d98e29b7ab17fbe28bd1b68c41acb5f796795`

Original file: `RESULTS.json`; 39821 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7633170135,
              "format_passes": 2,
              "gpu_energy_j": 479.6405287980185,
              "semantic_passes": 2,
              "tokens_per_s": 35.38929373479514,
              "ttft_s": 0.5199345639999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7832679870000003,
              "format_passes": 0,
              "gpu_energy_j": 1067.1879824015705,
              "semantic_passes": 0,
              "tokens_per_s": 35.38487447884624,
              "ttft_s": 0.194053596
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5801532300000001,
              "format_passes": 2,
              "gpu_energy_j": 150.20973097825276,
              "semantic_passes": 2,
              "tokens_per_s": 35.02859534803984,
              "ttft_s": 0.20901402
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.92438587,
              "format_passes": 0,
              "gpu_energy_j": 241.21396149448782,
              "semantic_passes": 0,
              "tokens_per_s": 34.9815817627636,
              "ttft_s": 0.524153325
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.464243235,
              "format_passes": 2,
              "gpu_energy_j": 106.41898166132486,
              "semantic_passes": 2,
              "tokens_per_s": 34.26678819574407,
              "ttft_s": 0.2015429575
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.991498313,
              "format_passes": 0,
              "gpu_energy_j": 268.5363898898089,
              "semantic_passes": 0,
              "tokens_per_s": 35.34388510764923,
              "ttft_s": 0.227510879
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1497313574999999,
              "format_passes": 0,
              "gpu_energy_j": 298.2233941042766,
              "semantic_passes": 2,
              "tokens_per_s": 35.24467110964552,
              "ttft_s": 0.3552363295
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.796938678,
              "format_passes": 2,
              "gpu_energy_j": 1020.2890405124683,
              "semantic_passes": 2,
              "tokens_per_s": 34.367291678476,
              "ttft_s": 3.2149380305
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.573804528,
              "format_passes": 2,
              "gpu_energy_j": 142.1801539144953,
              "semantic_passes": 2,
              "tokens_per_s": 34.974250224507614,
              "ttft_s": 0.202029464
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7257333625,
              "format_passes": 0,
              "gpu_energy_j": 187.08121408432274,
              "semantic_passes": 0,
              "tokens_per_s": 696.8371642806808,
              "ttft_s": 0.7256098755
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7482664100000003,
              "format_passes": 0,
              "gpu_energy_j": 732.0202567862141,
              "semantic_passes": 0,
              "tokens_per_s": 745.5484635632938,
              "ttft_s": 2.748049235
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4654789305,
              "format_passes": 0,
              "gpu_energy_j": 1469.4462992323342,
              "semantic_passes": 0,
              "tokens_per_s": 749.6810655354825,
              "ttft_s": 5.465076403
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8486258555,
              "format_passes": 0,
              "gpu_energy_j": 227.95731467230513,
              "semantic_passes": 2,
              "tokens_per_s": 35.18703049922598,
              "ttft_s": 0.223371121
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.985611995,
              "format_passes": 0,
              "gpu_energy_j": 261.71293825269987,
              "semantic_passes": 2,
              "tokens_per_s": 35.11375468853154,
              "ttft_s": 0.2166364
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015190671,
              "format_passes": 0,
              "gpu_energy_j": 273.5585958372843,
              "semantic_passes": 2,
              "tokens_per_s": 35.24751122581132,
              "ttft_s": 0.22077192299999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7081357220000002,
              "format_passes": 0,
              "gpu_energy_j": 456.30590649488266,
              "semantic_passes": 0,
              "tokens_per_s": 35.00701056251378,
              "ttft_s": 1.0295234475
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.778180603,
              "format_passes": 0,
              "gpu_energy_j": 467.38991404763976,
              "semantic_passes": 0,
              "tokens_per_s": 35.075002513588295,
              "ttft_s": 1.0931465404999998
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
              "e2e_s": 1.7648960864999998,
              "format_passes": 2,
              "gpu_energy_j": 481.06310307253693,
              "semantic_passes": 2,
              "tokens_per_s": 35.353608233239996,
              "ttft_s": 0.5203006055
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7825692220000002,
              "format_passes": 0,
              "gpu_energy_j": 1069.1142981553583,
              "semantic_passes": 0,
              "tokens_per_s": 35.38909123861566,
              "ttft_s": 0.193945504
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.582329479,
              "format_passes": 2,
              "gpu_energy_j": 149.7464804192069,
              "semantic_passes": 2,
              "tokens_per_s": 34.99145241557186,
              "ttft_s": 0.2107735005
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924307838,
              "format_passes": 0,
              "gpu_energy_j": 248.65424771023226,
              "semantic_passes": 0,
              "tokens_per_s": 34.98780235204774,
              "ttft_s": 0.5241316275000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4654910705,
              "format_passes": 2,
              "gpu_energy_j": 111.4789842023653,
              "semantic_passes": 2,
              "tokens_per_s": 34.18961157950573,
              "ttft_s": 0.2022096805
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.98940812,
              "format_passes": 0,
              "gpu_energy_j": 267.9909127250154,
              "semantic_passes": 0,
              "tokens_per_s": 35.25140802711233,
              "ttft_s": 0.22346059299999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1452501169999998,
              "format_passes": 0,
              "gpu_energy_j": 299.75342905080254,
              "semantic_passes": 2,
              "tokens_per_s": 35.23741995368409,
              "ttft_s": 0.35063561200000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7968085785000003,
              "format_passes": 2,
              "gpu_energy_j": 1021.1766887161891,
              "semantic_passes": 2,
              "tokens_per_s": 34.41587022544334,
              "ttft_s": 3.215562088
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5737242145,
              "format_passes": 2,
              "gpu_energy_j": 144.57980027193042,
              "semantic_passes": 2,
              "tokens_per_s": 34.88664372523426,
              "ttft_s": 0.201036963
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.726282224,
              "format_passes": 0,
              "gpu_energy_j": 187.49276613837435,
              "semantic_passes": 0,
              "tokens_per_s": 696.3490884997059,
              "ttft_s": 0.726146706
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.751828645,
              "format_passes": 0,
              "gpu_energy_j": 739.3602382740343,
              "semantic_passes": 0,
              "tokens_per_s": 744.5683444902777,
              "ttft_s": 2.751594326
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4719923635,
              "format_passes": 0,
              "gpu_energy_j": 1473.833524000856,
              "semantic_passes": 0,
              "tokens_per_s": 748.7898989447001,
              "ttft_s": 5.4716055665
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8473659345,
              "format_passes": 0,
              "gpu_energy_j": 225.74895269112503,
              "semantic_passes": 2,
              "tokens_per_s": 35.15421414854893,
              "ttft_s": 0.2215043765
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986072933,
              "format_passes": 0,
              "gpu_energy_j": 261.6169362756875,
              "semantic_passes": 2,
              "tokens_per_s": 35.049429218946656,
              "ttft_s": 0.2157107405
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0143490695000001,
              "format_passes": 0,
              "gpu_energy_j": 274.47885113637005,
              "semantic_passes": 2,
              "tokens_per_s": 35.258978428317775,
              "ttft_s": 0.220217752
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7079150594999999,
              "format_passes": 0,
              "gpu_energy_j": 457.59873549441375,
              "semantic_passes": 0,
              "tokens_per_s": 35.00423764308438,
              "ttft_s": 1.0289508944999999
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.777433957,
              "format_passes": 0,
              "gpu_energy_j": 467.4008013116859,
              "semantic_passes": 0,
              "tokens_per_s": 35.10391179583209,
              "ttft_s": 1.0937196825
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
            "e2e_change_pct": 0.08955128249261701,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2965917575988408,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10083699839439353,
            "ttft_change_pct": 0.07040145536469922
          },
          "decode": {
            "e2e_change_pct": -0.018469878486038205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.18050388362254033,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.011916842525305782,
            "ttft_change_pct": -0.05570213705290428
          },
          "energy": {
            "e2e_change_pct": 0.375116242996687,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.308402495649851,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10603603170192821,
            "ttft_change_pct": 0.8418002294774185
          },
          "filtering": {
            "e2e_change_pct": -0.0084414964066859,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.0845172350914885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01778247000472355,
            "ttft_change_pct": -0.004139533026892295
          },
          "german": {
            "e2e_change_pct": 0.268789161784988,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.754793235236665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.22522278947615382,
            "ttft_change_pct": 0.33080937596143833
          },
          "ha_sim": {
            "e2e_change_pct": -0.2108115538467903,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.20312970060308855,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.26164944871009954,
            "ttft_change_pct": -1.78026036284622
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.38976413670618326,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5130499406733158,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.020573765432163604,
            "ttft_change_pct": -1.295114580897605
          },
          "long_context": {
            "e2e_change_pct": -0.0034264314236476245,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.08699968033323291,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14135110622570668,
            "ttft_change_pct": 0.019411182861994725
          },
          "math": {
            "e2e_change_pct": -0.013996665428894772,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6877505695191752,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2504885700507997,
            "ttft_change_pct": -0.4912654720501508
          },
          "prefill": {
            "e2e_change_pct": 0.07562853361313682,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.21998577252451135,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0700415830258927,
            "ttft_change_pct": 0.07398335085091468
          },
          "prefill2048": {
            "e2e_change_pct": 0.1296175286005008,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0027019634736511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13146282514374663,
            "ttft_change_pct": 0.12900391138734868
          },
          "prefill4096": {
            "e2e_change_pct": 0.11917405743990805,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.29856312345770686,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11887276226535404,
            "ttft_change_pct": 0.11947067192721317
          },
          "pve_sim": {
            "e2e_change_pct": -0.1484660161877538,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9687611842395527,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09326263174658234,
            "ttft_change_pct": -0.8357143446488857
          },
          "sorting": {
            "e2e_change_pct": 0.04676667921437172,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.03668216697779725,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18319165852661579,
            "ttft_change_pct": -0.42728715026653097
          },
          "time": {
            "e2e_change_pct": -0.08290083075437327,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.33640152899201414,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03253336791069206,
            "ttft_change_pct": -0.2510151619234624
          },
          "tool-call": {
            "e2e_change_pct": -0.012918323594446335,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2833250635438711,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.007921040342606656,
            "ttft_change_pct": -0.055613400684595415
          },
          "tool-final": {
            "e2e_change_pct": -0.041989323173385884,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.002329375050447169,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08242132622113818,
            "ttft_change_pct": 0.052430481986243116
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
