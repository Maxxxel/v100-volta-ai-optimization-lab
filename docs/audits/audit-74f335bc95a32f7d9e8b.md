# Public audit excerpt

Original SHA256: `74f335bc95a32f7d9e8bc7aba46321f8d2e574d8f62e615012fae6c58d18d68f`

Original file: `RESULTS.json`; 39519 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5268645345,
              "format_passes": 2,
              "gpu_energy_j": 131.85855638796244,
              "semantic_passes": 2,
              "tokens_per_s": 96.38528509954173,
              "ttft_s": 0.132533181
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3665144525000001,
              "format_passes": 0,
              "gpu_energy_j": 356.1362139746026,
              "semantic_passes": 0,
              "tokens_per_s": 97.04423923448383,
              "ttft_s": 0.057638053
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20542198750000001,
              "format_passes": 2,
              "gpu_energy_j": 45.937771252391286,
              "semantic_passes": 2,
              "tokens_per_s": 94.90402358681848,
              "ttft_s": 0.068323394
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22966082999999998,
              "format_passes": 0,
              "gpu_energy_j": 54.763565582735126,
              "semantic_passes": 0,
              "tokens_per_s": 94.01460529163762,
              "ttft_s": 0.133915548
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15673670099999998,
              "format_passes": 2,
              "gpu_energy_j": 33.524251375866555,
              "semantic_passes": 2,
              "tokens_per_s": 93.65410019210151,
              "ttft_s": 0.0606256615
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.311230695,
              "format_passes": 0,
              "gpu_energy_j": 71.51758880250112,
              "semantic_passes": 0,
              "tokens_per_s": 94.79173242529131,
              "ttft_s": 0.07913875549999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39847638100000005,
              "format_passes": 0,
              "gpu_energy_j": 96.0116248084795,
              "semantic_passes": 2,
              "tokens_per_s": 96.17794311208117,
              "ttft_s": 0.1073289615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0306116175,
              "format_passes": 2,
              "gpu_energy_j": 272.6108938460919,
              "semantic_passes": 2,
              "tokens_per_s": 94.23815231910129,
              "ttft_s": 0.871379672
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14845385249999998,
              "format_passes": 0,
              "gpu_energy_j": 28.986038950496884,
              "semantic_passes": 0,
              "tokens_per_s": 93.65286469537196,
              "ttft_s": 0.06301820450000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20517866,
              "format_passes": 0,
              "gpu_energy_j": 49.32474010640058,
              "semantic_passes": 0,
              "tokens_per_s": 2474.658648345117,
              "ttft_s": 0.2050436765
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7540240975,
              "format_passes": 0,
              "gpu_energy_j": 199.7980841715842,
              "semantic_passes": 0,
              "tokens_per_s": 2720.645622594085,
              "ttft_s": 0.7537647160000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4948762885,
              "format_passes": 0,
              "gpu_energy_j": 406.26973763949115,
              "semantic_passes": 0,
              "tokens_per_s": 2743.4912399351415,
              "ttft_s": 1.494588642
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25458125249999997,
              "format_passes": 2,
              "gpu_energy_j": 59.524156105404444,
              "semantic_passes": 2,
              "tokens_per_s": 95.47701813839926,
              "ttft_s": 0.076503722
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35147557799999996,
              "format_passes": 0,
              "gpu_energy_j": 85.60219331776666,
              "semantic_passes": 2,
              "tokens_per_s": 95.87958855392961,
              "ttft_s": 0.069839921
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31538323,
              "format_passes": 0,
              "gpu_energy_j": 75.26112107158917,
              "semantic_passes": 0,
              "tokens_per_s": 95.83746553284323,
              "ttft_s": 0.075363501
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550216619,
              "format_passes": 0,
              "gpu_energy_j": 139.0437946358038,
              "semantic_passes": 0,
              "tokens_per_s": 96.17640992001948,
              "ttft_s": 0.30325980249999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5246634265000001,
              "format_passes": 0,
              "gpu_energy_j": 134.22621758911993,
              "semantic_passes": 0,
              "tokens_per_s": 95.75776792410699,
              "ttft_s": 0.273977225
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
              "e2e_s": 0.526741498,
              "format_passes": 2,
              "gpu_energy_j": 130.60808431005245,
              "semantic_passes": 2,
              "tokens_per_s": 96.33741110018913,
              "ttft_s": 0.132278906
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3683474105,
              "format_passes": 0,
              "gpu_energy_j": 357.52339461219606,
              "semantic_passes": 0,
              "tokens_per_s": 96.9069765347545,
              "ttft_s": 0.0576848995
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2048395475,
              "format_passes": 2,
              "gpu_energy_j": 43.02486195730482,
              "semantic_passes": 2,
              "tokens_per_s": 94.8877976484268,
              "ttft_s": 0.06778027
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22976197199999998,
              "format_passes": 0,
              "gpu_energy_j": 54.87172305347366,
              "semantic_passes": 0,
              "tokens_per_s": 94.07154857674382,
              "ttft_s": 0.1340967945
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1565115215,
              "format_passes": 2,
              "gpu_energy_j": 31.883216541412153,
              "semantic_passes": 2,
              "tokens_per_s": 93.89297785610307,
              "ttft_s": 0.060613362500000004
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.307275499,
              "format_passes": 0,
              "gpu_energy_j": 73.04841475890973,
              "semantic_passes": 0,
              "tokens_per_s": 95.5657563926645,
              "ttft_s": 0.0770668285
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398702432,
              "format_passes": 0,
              "gpu_energy_j": 91.65687674596617,
              "semantic_passes": 2,
              "tokens_per_s": 96.06642343605549,
              "ttft_s": 0.1072278085
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.028906344,
              "format_passes": 2,
              "gpu_energy_j": 272.10045974475713,
              "semantic_passes": 2,
              "tokens_per_s": 94.08636052407593,
              "ttft_s": 0.8694419085
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14905091799999998,
              "format_passes": 0,
              "gpu_energy_j": 31.77623371228751,
              "semantic_passes": 0,
              "tokens_per_s": 93.218747217039,
              "ttft_s": 0.0632061755
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20491188,
              "format_passes": 0,
              "gpu_energy_j": 51.38663366941891,
              "semantic_passes": 0,
              "tokens_per_s": 2476.9793744491726,
              "ttft_s": 0.204767044
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.753765754,
              "format_passes": 0,
              "gpu_energy_j": 198.4970383066513,
              "semantic_passes": 0,
              "tokens_per_s": 2721.7882871308725,
              "ttft_s": 0.75351013
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4973664064999999,
              "format_passes": 0,
              "gpu_energy_j": 403.60108046532633,
              "semantic_passes": 0,
              "tokens_per_s": 2738.642618231166,
              "ttft_s": 1.4970420610000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2553049035,
              "format_passes": 2,
              "gpu_energy_j": 57.72149893570848,
              "semantic_passes": 2,
              "tokens_per_s": 94.91511288540788,
              "ttft_s": 0.0761671155
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3518497975,
              "format_passes": 0,
              "gpu_energy_j": 81.55238650547804,
              "semantic_passes": 2,
              "tokens_per_s": 96.09567340802778,
              "ttft_s": 0.0708891225
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31483628249999995,
              "format_passes": 0,
              "gpu_energy_j": 74.52631924311737,
              "semantic_passes": 0,
              "tokens_per_s": 95.84220843653625,
              "ttft_s": 0.074824666
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5510043825,
              "format_passes": 0,
              "gpu_energy_j": 139.90635316989952,
              "semantic_passes": 0,
              "tokens_per_s": 96.05477389110743,
              "ttft_s": 0.3034205465
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524986025,
              "format_passes": 0,
              "gpu_energy_j": 135.15036166123434,
              "semantic_passes": 0,
              "tokens_per_s": 95.75391918549006,
              "ttft_s": 0.274296535
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
            "e2e_change_pct": -0.023352587229419353,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9483435221532166,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04966940680121157,
            "ttft_change_pct": -0.191857614886648
          },
          "decode": {
            "e2e_change_pct": 0.1341338173662443,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.38950844737524193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14144342911242003,
            "ttft_change_pct": 0.08127703411493492
          },
          "energy": {
            "e2e_change_pct": -0.2835334265276823,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.340989594559043,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.017097208082905713,
            "ttft_change_pct": -0.7949312354125659
          },
          "filtering": {
            "e2e_change_pct": 0.04403972588620242,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1974989568112262,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.060568552013329224,
            "ttft_change_pct": 0.13534388105556072
          },
          "german": {
            "e2e_change_pct": -0.14366737245540273,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.895067800487118,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.25506375429542594,
            "ttft_change_pct": -0.02028678895321656
          },
          "ha_sim": {
            "e2e_change_pct": -1.2708245245540484,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.140488769323645,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8165521903328532,
            "ttft_change_pct": -2.618093988096626
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.0567288328188198,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.535646669036186,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11595140467468568,
            "ttft_change_pct": -0.09424576422460973
          },
          "long_context": {
            "e2e_change_pct": -0.16546228191534063,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.18723906962535564,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16107255001284182,
            "ttft_change_pct": -0.22237878186351923
          },
          "math": {
            "e2e_change_pct": 0.4021892931340254,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.62599535091977,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4635389208274998,
            "ttft_change_pct": 0.29828047544577796
          },
          "prefill": {
            "e2e_change_pct": -0.1300232685017111,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.180242123061428,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09377964535057792,
            "ttft_change_pct": -0.13491393868954038
          },
          "prefill2048": {
            "e2e_change_pct": -0.03426196866340714,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6511803505661162,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04199975650256427,
            "ttft_change_pct": -0.033775260979451716
          },
          "prefill4096": {
            "e2e_change_pct": 0.1665768611861962,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6568683135668052,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17673180921438103,
            "ttft_change_pct": 0.16415346210023607
          },
          "pve_sim": {
            "e2e_change_pct": 0.28425148862838423,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.028446411745589,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5885240908726996,
            "ttft_change_pct": -0.4399870897784597
          },
          "sorting": {
            "e2e_change_pct": 0.10647098217448914,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.73096150381942,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22537106943949503,
            "ttft_change_pct": 1.502294797842052
          },
          "time": {
            "e2e_change_pct": -0.17342313984166635,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9763365440342731,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.004948903507262514,
            "ttft_change_pct": -0.7149813807084127
          },
          "tool-call": {
            "e2e_change_pct": 0.14317333806306287,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6203502546481943,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12647179179717805,
            "ttft_change_pct": 0.053005376470904864
          },
          "tool-final": {
            "e2e_change_pct": 0.06148675202157783,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.688497440152358,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.004019244287289947,
            "ttft_change_pct": 0.11654618372021197
          }
        }
      },
      "complete": true
    }
  }
}
```
