# Public audit excerpt

Original SHA256: `97028b7aef1a9bf6fd1b066495639c8e2cb3eb32d1f9e8825af33375edcf0b61`

Original file: `RESULTS.json`; 40433 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.764131519,
              "format_passes": 2,
              "gpu_energy_j": 477.17326849728624,
              "semantic_passes": 2,
              "tokens_per_s": 35.39104411869228,
              "ttft_s": 0.5207902215
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7818086305,
              "format_passes": 0,
              "gpu_energy_j": 1067.186587987671,
              "semantic_passes": 0,
              "tokens_per_s": 35.404433780577826,
              "ttft_s": 0.195103978
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5828439384999999,
              "format_passes": 2,
              "gpu_energy_j": 144.34632273175066,
              "semantic_passes": 2,
              "tokens_per_s": 35.00495756288197,
              "ttft_s": 0.2114160905
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9245856475,
              "format_passes": 0,
              "gpu_energy_j": 240.698546567662,
              "semantic_passes": 0,
              "tokens_per_s": 34.958385728047105,
              "ttft_s": 0.5240931980000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46457450899999997,
              "format_passes": 2,
              "gpu_energy_j": 109.99181351771969,
              "semantic_passes": 2,
              "tokens_per_s": 34.258046918442474,
              "ttft_s": 0.2017912595
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9907342665000001,
              "format_passes": 0,
              "gpu_energy_j": 264.34053078659724,
              "semantic_passes": 0,
              "tokens_per_s": 35.24461079795504,
              "ttft_s": 0.22458787000000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.148466463,
              "format_passes": 0,
              "gpu_energy_j": 293.9406127969897,
              "semantic_passes": 2,
              "tokens_per_s": 35.17109586163973,
              "ttft_s": 0.35229533150000003
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7919533455,
              "format_passes": 2,
              "gpu_energy_j": 1020.4515989653707,
              "semantic_passes": 2,
              "tokens_per_s": 34.356136715993124,
              "ttft_s": 3.2097773309999997
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5755530915,
              "format_passes": 2,
              "gpu_energy_j": 142.60755607711874,
              "semantic_passes": 2,
              "tokens_per_s": 35.01167162279596,
              "ttft_s": 0.2041828785
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7235183345,
              "format_passes": 0,
              "gpu_energy_j": 190.72179726473624,
              "semantic_passes": 0,
              "tokens_per_s": 699.0164033785097,
              "ttft_s": 0.7233907735
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.75151962,
              "format_passes": 0,
              "gpu_energy_j": 729.6679167558934,
              "semantic_passes": 0,
              "tokens_per_s": 744.6517631760868,
              "ttft_s": 2.7513139129999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4642246015,
              "format_passes": 0,
              "gpu_energy_j": 1471.5181105394652,
              "semantic_passes": 0,
              "tokens_per_s": 749.8434162743179,
              "ttft_s": 5.463874451
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846808562,
              "format_passes": 0,
              "gpu_energy_j": 223.98923138857165,
              "semantic_passes": 2,
              "tokens_per_s": 35.24318461683062,
              "ttft_s": 0.222521401
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9877349195,
              "format_passes": 0,
              "gpu_energy_j": 260.3699213002823,
              "semantic_passes": 2,
              "tokens_per_s": 35.071542388444755,
              "ttft_s": 0.21780516
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0145235655,
              "format_passes": 0,
              "gpu_energy_j": 275.54524904920345,
              "semantic_passes": 2,
              "tokens_per_s": 35.273462517251076,
              "ttft_s": 0.22070952649999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.708296791,
              "format_passes": 0,
              "gpu_energy_j": 457.5097280713803,
              "semantic_passes": 0,
              "tokens_per_s": 35.01982095633028,
              "ttft_s": 1.03022409
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7784606715,
              "format_passes": 0,
              "gpu_energy_j": 465.210563200077,
              "semantic_passes": 0,
              "tokens_per_s": 35.11960482480406,
              "ttft_s": 1.094185228
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
              "e2e_s": 1.7923233015,
              "format_passes": 2,
              "gpu_energy_j": 488.325727650991,
              "semantic_passes": 2,
              "tokens_per_s": 34.64207360476028,
              "ttft_s": 0.5221197235
            },
            "decode": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.849521083,
              "format_passes": 0,
              "gpu_energy_j": 1082.4893294993965,
              "semantic_passes": 0,
              "tokens_per_s": 34.78220141275945,
              "ttft_s": 0.198133357
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.734356864,
              "format_passes": 0,
              "gpu_energy_j": 187.77412008904957,
              "semantic_passes": 2,
              "tokens_per_s": 34.435426975670936,
              "ttft_s": 0.211549708
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9343436805,
              "format_passes": 0,
              "gpu_energy_j": 249.73195644861528,
              "semantic_passes": 0,
              "tokens_per_s": 34.26732195871935,
              "ttft_s": 0.5257649824999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47489400849999996,
              "format_passes": 2,
              "gpu_energy_j": 112.51226850509984,
              "semantic_passes": 2,
              "tokens_per_s": 33.55880449299532,
              "ttft_s": 0.2066857825
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0093514135000001,
              "format_passes": 0,
              "gpu_energy_j": 271.3566902871221,
              "semantic_passes": 0,
              "tokens_per_s": 34.552627730858845,
              "ttft_s": 0.227903827
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.173105022,
              "format_passes": 0,
              "gpu_energy_j": 299.9802744653931,
              "semantic_passes": 2,
              "tokens_per_s": 34.40423165461082,
              "ttft_s": 0.3591853425
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8225283589999997,
              "format_passes": 2,
              "gpu_energy_j": 1028.625594668054,
              "semantic_passes": 2,
              "tokens_per_s": 33.767584816143874,
              "ttft_s": 3.2302094045
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.58636385,
              "format_passes": 2,
              "gpu_energy_j": 142.6453629440982,
              "semantic_passes": 2,
              "tokens_per_s": 34.249376646889814,
              "ttft_s": 0.2068119845
            },
            "prefill": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7193497715,
              "format_passes": 0,
              "gpu_energy_j": 186.49061165986882,
              "semantic_passes": 0,
              "tokens_per_s": 703.0818015880295,
              "ttft_s": 0.71915755
            },
            "prefill2048": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.758660731,
              "format_passes": 0,
              "gpu_energy_j": 736.4009489733382,
              "semantic_passes": 0,
              "tokens_per_s": 742.7195450617533,
              "ttft_s": 2.758431626
            },
            "prefill4096": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 5.494657607500001,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 745.6859674214415
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8647016359999999,
              "format_passes": 0,
              "gpu_energy_j": 232.39303937515714,
              "semantic_passes": 2,
              "tokens_per_s": 34.493295274661605,
              "ttft_s": 0.2268275695
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0058075,
              "format_passes": 0,
              "gpu_energy_j": 267.33187339174793,
              "semantic_passes": 2,
              "tokens_per_s": 34.396383809879225,
              "ttft_s": 0.22079861750000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.036328034,
              "format_passes": 0,
              "gpu_energy_j": 276.1910245296098,
              "semantic_passes": 2,
              "tokens_per_s": 34.56868313201396,
              "ttft_s": 0.22628387849999998
            },
            "tool-call": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.732643255,
              "format_passes": 0,
              "gpu_energy_j": 463.7007259277483,
              "semantic_passes": 0,
              "tokens_per_s": 34.359971521754616,
              "ttft_s": 1.0411386605000001
            },
            "tool-final": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.79433723,
              "format_passes": 0,
              "gpu_energy_j": 472.4488632775308,
              "semantic_passes": 0,
              "tokens_per_s": 34.44485717002488,
              "ttft_s": 1.0975669954999998
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
            "e2e_change_pct": 1.598054464554921,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.337192774613306,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.116271312652296,
            "ttft_change_pct": 0.25528551518705367
          },
          "decode": {
            "e2e_change_pct": 1.7904780256172703,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.433933080116856,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.7574984299274954,
            "ttft_change_pct": 1.5526997609448978
          },
          "energy": {
            "e2e_change_pct": 25.99545358401287,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 30.085835603864997,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.6269997933519686,
            "ttft_change_pct": 0.06320119707257099
          },
          "filtering": {
            "e2e_change_pct": 1.0553952493622232,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7529972697254887,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.976818308213002,
            "ttft_change_pct": 0.31898610903167146
          },
          "german": {
            "e2e_change_pct": 2.2212797517050076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2914932546085343,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.041104173602848,
            "ttft_change_pct": 2.4255376630919034
          },
          "ha_sim": {
            "e2e_change_pct": 1.8791261824191663,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.65421253397915,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9633727013275593,
            "ttft_change_pct": 1.4764630876992424
          },
          "jarvis_memory": {
            "e2e_change_pct": 2.1453442302215464,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.054721738154197,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.1803818966736,
            "ttft_change_pct": 1.9557485961178456
          },
          "long_context": {
            "e2e_change_pct": 0.8063130190218093,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8010174819629734,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.7130910402253452,
            "ttft_change_pct": 0.6365573494045096
          },
          "math": {
            "e2e_change_pct": 1.8783251553432079,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.02651112466929284,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.1772595839434805,
            "ttft_change_pct": 1.2876231441707242
          },
          "prefill": {
            "e2e_change_pct": -0.576151674564096,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.218511814354507,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5815883847461567,
            "ttft_change_pct": -0.5851918015926993
          },
          "prefill2048": {
            "e2e_change_pct": 0.25953334833934694,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9227529486810715,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2594794251331911,
            "ttft_change_pct": 0.2587023227836438
          },
          "prefill4096": {
            "e2e_change_pct": 0.5569501296057044,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5544422692317696
          },
          "pve_sim": {
            "e2e_change_pct": 2.1130010728446003,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7518803625013364,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.1277570410333957,
            "ttft_change_pct": 1.935170496252625
          },
          "sorting": {
            "e2e_change_pct": 1.8296994611822104,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.6738695686113756,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9250894958870668,
            "ttft_change_pct": 1.3743740047297504
          },
          "time": {
            "e2e_change_pct": 2.1492323334307173,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.23436277077346634,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9980442376260399,
            "ttft_change_pct": 2.5256508354658758
          },
          "tool-call": {
            "e2e_change_pct": 1.4251893539967364,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.353194801445201,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.8842170421102256,
            "ttft_change_pct": 1.0594365445288911
          },
          "tool-final": {
            "e2e_change_pct": 0.8927134996248975,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.555919114919324,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.9212848724955434,
            "ttft_change_pct": 0.3090671865659589
          }
        }
      },
      "complete": false,
      "failed_starts": [
        {
          "index": 1,
          "model": "qwen38"
        },
        {
          "index": 2,
          "model": "qwen38"
        }
      ]
    }
  }
}
```
