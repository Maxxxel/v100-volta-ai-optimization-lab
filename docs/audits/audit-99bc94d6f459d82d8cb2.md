# Public audit excerpt

Original SHA256: `99bc94d6f459d82d8cb2e82b3d385ea2ae3db98271bb5a702356dde171b5f465`

Original file: `RESULTS.json`; 43281 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7624188955,
              "format_passes": 2,
              "gpu_energy_j": 479.89429440259096,
              "semantic_passes": 2,
              "tokens_per_s": 35.41293422366616,
              "ttft_s": 0.5198985165000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7858057494999997,
              "format_passes": 0,
              "gpu_energy_j": 1068.4132045064462,
              "semantic_passes": 0,
              "tokens_per_s": 35.372489877596465,
              "ttft_s": 0.196178009
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.583752913,
              "format_passes": 2,
              "gpu_energy_j": 146.6122771922866,
              "semantic_passes": 2,
              "tokens_per_s": 34.9234591202367,
              "ttft_s": 0.211485438
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9245555525,
              "format_passes": 0,
              "gpu_energy_j": 247.6465122557599,
              "semantic_passes": 0,
              "tokens_per_s": 35.00527934741133,
              "ttft_s": 0.524562722
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4680482805,
              "format_passes": 2,
              "gpu_energy_j": 110.50698463472659,
              "semantic_passes": 2,
              "tokens_per_s": 34.160419879689215,
              "ttft_s": 0.2045543025
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9903077364999999,
              "format_passes": 0,
              "gpu_energy_j": 263.5974399514917,
              "semantic_passes": 0,
              "tokens_per_s": 35.26604943565188,
              "ttft_s": 0.224669073
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.149839853,
              "format_passes": 0,
              "gpu_energy_j": 296.59651495975436,
              "semantic_passes": 2,
              "tokens_per_s": 35.26508501489235,
              "ttft_s": 0.35582242799999997
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7990279335,
              "format_passes": 2,
              "gpu_energy_j": 1025.0254989202435,
              "semantic_passes": 2,
              "tokens_per_s": 34.335488348815396,
              "ttft_s": 3.2164377594999998
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574753428,
              "format_passes": 2,
              "gpu_energy_j": 144.48752062821748,
              "semantic_passes": 2,
              "tokens_per_s": 34.89420039333305,
              "ttft_s": 0.2021411775
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7243840104999999,
              "format_passes": 0,
              "gpu_energy_j": 186.76678979509097,
              "semantic_passes": 0,
              "tokens_per_s": 698.2063282169637,
              "ttft_s": 0.7241841554999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.753562615,
              "format_passes": 0,
              "gpu_energy_j": 738.3392674166059,
              "semantic_passes": 0,
              "tokens_per_s": 744.095026224895,
              "ttft_s": 2.7533364765000004
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4706171105,
              "format_passes": 0,
              "gpu_energy_j": 1478.7938226605806,
              "semantic_passes": 0,
              "tokens_per_s": 748.9667751813897,
              "ttft_s": 5.4702486685
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8480419835,
              "format_passes": 0,
              "gpu_energy_j": 222.8942807636053,
              "semantic_passes": 2,
              "tokens_per_s": 35.176969423152826,
              "ttft_s": 0.222607941
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9886529694999999,
              "format_passes": 0,
              "gpu_energy_j": 259.6873096906688,
              "semantic_passes": 2,
              "tokens_per_s": 34.97159078144293,
              "ttft_s": 0.2165409685
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.016210478,
              "format_passes": 0,
              "gpu_energy_j": 277.17860674811095,
              "semantic_passes": 2,
              "tokens_per_s": 35.26229586559943,
              "ttft_s": 0.222124246
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7088626109999998,
              "format_passes": 0,
              "gpu_energy_j": 457.6595249570039,
              "semantic_passes": 0,
              "tokens_per_s": 34.9790651463982,
              "ttft_s": 1.02934903
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7803549975,
              "format_passes": 0,
              "gpu_energy_j": 470.7219697284806,
              "semantic_passes": 0,
              "tokens_per_s": 35.082889702703184,
              "ttft_s": 1.095385599
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
              "e2e_s": 2.2260627865,
              "format_passes": 2,
              "gpu_energy_j": 605.5033139863737,
              "semantic_passes": 2,
              "tokens_per_s": 35.372503579535675,
              "ttft_s": 0.982117506
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7988897325,
              "format_passes": 0,
              "gpu_energy_j": 1073.7399729042552,
              "semantic_passes": 0,
              "tokens_per_s": 35.25266036276035,
              "ttft_s": 0.196444613
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7248115665,
              "format_passes": 0,
              "gpu_energy_j": 190.4759520335121,
              "semantic_passes": 2,
              "tokens_per_s": 34.995141787790914,
              "ttft_s": 0.2104154165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.393062791,
              "format_passes": 0,
              "gpu_energy_j": 369.6141621452267,
              "semantic_passes": 0,
              "tokens_per_s": 34.72113923357166,
              "ttft_s": 0.9897824095000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46699440299999995,
              "format_passes": 2,
              "gpu_energy_j": 111.31820302361916,
              "semantic_passes": 2,
              "tokens_per_s": 34.26164347658113,
              "ttft_s": 0.20426135
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9932669384999999,
              "format_passes": 0,
              "gpu_energy_j": 268.44248580274666,
              "semantic_passes": 0,
              "tokens_per_s": 35.192160354071106,
              "ttft_s": 0.22603439250000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.151695798,
              "format_passes": 0,
              "gpu_energy_j": 297.05705365435784,
              "semantic_passes": 2,
              "tokens_per_s": 35.23543202171358,
              "ttft_s": 0.3570214215
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 11.3466075005,
              "format_passes": 2,
              "gpu_energy_j": 3235.829888336054,
              "semantic_passes": 2,
              "tokens_per_s": 34.324673086113336,
              "ttft_s": 10.763834582000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.577063631,
              "format_passes": 2,
              "gpu_energy_j": 144.2883480466049,
              "semantic_passes": 2,
              "tokens_per_s": 34.90101027351124,
              "ttft_s": 0.2045281715
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.4139463765,
              "format_passes": 0,
              "gpu_energy_j": 684.4179522385398,
              "semantic_passes": 0,
              "tokens_per_s": 209.29730855205693,
              "ttft_s": 2.4137396855
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 9.534760755499999,
              "format_passes": 0,
              "gpu_energy_j": 2730.3693489605075,
              "semantic_passes": 0,
              "tokens_per_s": 214.82147748154253,
              "ttft_s": 9.53452408
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 19.043599178,
              "format_passes": 0,
              "gpu_energy_j": 5465.803036176541,
              "semantic_passes": 0,
              "tokens_per_s": 215.10502686578698,
              "ttft_s": 19.043257029
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.849778369,
              "format_passes": 0,
              "gpu_energy_j": 226.1268251183584,
              "semantic_passes": 2,
              "tokens_per_s": 35.15076271177301,
              "ttft_s": 0.2238648375
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989896482,
              "format_passes": 0,
              "gpu_energy_j": 263.7824749077602,
              "semantic_passes": 2,
              "tokens_per_s": 34.99695660283204,
              "ttft_s": 0.21841408550000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0178419725,
              "format_passes": 0,
              "gpu_energy_j": 273.25358420969246,
              "semantic_passes": 2,
              "tokens_per_s": 35.18728140610129,
              "ttft_s": 0.22205764449999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.95488655,
              "format_passes": 0,
              "gpu_energy_j": 822.1673929881463,
              "semantic_passes": 0,
              "tokens_per_s": 34.92174501926353,
              "ttft_s": 2.2736225855
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5395143715,
              "format_passes": 0,
              "gpu_energy_j": 979.5510565907264,
              "semantic_passes": 0,
              "tokens_per_s": 34.9875153728503,
              "ttft_s": 2.8535052194999997
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
            "e2e_change_pct": 26.30724694247355,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 26.174309852995936,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11416914473997286,
            "ttft_change_pct": 88.90561808325528
          },
          "decode": {
            "e2e_change_pct": 0.34560629535016485,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.49856819209470604,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3387647158873297,
            "ttft_change_pct": 0.13589902423771782
          },
          "energy": {
            "e2e_change_pct": 24.164102715149973,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 29.918145793272764,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.205256493371464,
            "ttft_change_pct": -0.5059551665207329
          },
          "filtering": {
            "e2e_change_pct": 50.673779118318585,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 49.25070366567621,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8117064601019464,
            "ttft_change_pct": 88.6871422594151
          },
          "german": {
            "e2e_change_pct": -0.22516427127438066,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7340878873620449,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2963183627379795,
            "ttft_change_pct": -0.14321502721752477
          },
          "ha_sim": {
            "e2e_change_pct": 0.2988164073582489,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8380473847342982,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20951902116395082,
            "ttft_change_pct": 0.6077024673529552
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.16140899927565844,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.15527447942738082,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08408598239943998,
            "ttft_change_pct": 0.3369640038541899
          },
          "long_context": {
            "e2e_change_pct": 198.67133643438368,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 215.68286757204186,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03149878805330797,
            "ttft_change_pct": 234.65079652818326
          },
          "math": {
            "e2e_change_pct": 0.40194679795804156,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.13784760147215191,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0195157937463053,
            "ttft_change_pct": 1.1808549002837454
          },
          "prefill": {
            "e2e_change_pct": 233.24125622731432,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 266.45591702327863,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -70.0235732485342,
            "ttft_change_pct": 233.304680469497
          },
          "prefill2048": {
            "e2e_change_pct": 246.2699814254995,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 269.79874557042945,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -71.12983289628723,
            "ttft_change_pct": 246.2898255036429
          },
          "prefill4096": {
            "e2e_change_pct": 248.10696477822893,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 269.6122442777526,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -71.2797638034489,
            "ttft_change_pct": 248.1241563781023
          },
          "pve_sim": {
            "e2e_change_pct": 0.20475230398779853,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4502589943891087,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07449962805086141,
            "ttft_change_pct": 0.5646233887047103
          },
          "sorting": {
            "e2e_change_pct": 0.12577846204506749,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5769600840215947,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07253264956588179,
            "ttft_change_pct": 0.8650173742988709
          },
          "time": {
            "e2e_change_pct": 0.16054690788180892,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4160625830641371,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21273277209189478,
            "ttft_change_pct": -0.029983894689289414
          },
          "tool-call": {
            "e2e_change_pct": 72.9153959469478,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 79.64607926938419,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1638698086834589,
            "ttft_change_pct": 120.87965493103927
          },
          "tool-final": {
            "e2e_change_pct": 98.80947206990949,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 108.09546177667167,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.271854259045079,
            "ttft_change_pct": 160.50234931927378
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 351210301983988,
          "end_ns": 351211114121550,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 351312106359722,
          "end_ns": 351312614602621,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```

</details>
