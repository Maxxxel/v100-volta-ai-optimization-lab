# Public audit excerpt

Original SHA256: `d5be5aa0652c2a6fc19e1921be71a5e6d6bac859e0714707048e9aba5f14e8a1`

Original file: `RESULTS.json`; 48564 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6665651085,
              "format_passes": 2,
              "gpu_energy_j": 177.7049115185835,
              "semantic_passes": 2,
              "tokens_per_s": 79.26203869577165,
              "ttft_s": 0.12405164199999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6589872410000002,
              "format_passes": 0,
              "gpu_energy_j": 458.26853189193776,
              "semantic_passes": 0,
              "tokens_per_s": 79.60209041108824,
              "ttft_s": 0.06305107700000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23888419049999998,
              "format_passes": 2,
              "gpu_energy_j": 54.522280557214074,
              "semantic_passes": 2,
              "tokens_per_s": 77.94149034556722,
              "ttft_s": 0.072015619
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24136065950000002,
              "format_passes": 0,
              "gpu_energy_j": 56.900129082929524,
              "semantic_passes": 0,
              "tokens_per_s": 77.58157728082146,
              "ttft_s": 0.12528067050000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18232499349999998,
              "format_passes": 2,
              "gpu_energy_j": 40.273985032366056,
              "semantic_passes": 2,
              "tokens_per_s": 77.37613711349962,
              "ttft_s": 0.065969526
            },
            "grammar-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.664542905,
              "format_passes": 0,
              "gpu_energy_j": 179.7871719886706,
              "semantic_passes": 0,
              "tokens_per_s": 79.56368884825153
            },
            "grammar-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23843905450000002,
              "format_passes": 0,
              "gpu_energy_j": 59.31758635551617,
              "semantic_passes": 0,
              "tokens_per_s": 78.27045860572247
            },
            "grammar-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241763132,
              "format_passes": 0,
              "gpu_energy_j": 59.802044906704225,
              "semantic_passes": 0,
              "tokens_per_s": 77.58456266509992
            },
            "grammar-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18317739449999998,
              "format_passes": 0,
              "gpu_energy_j": 41.641763978482004,
              "semantic_passes": 0,
              "tokens_per_s": 77.57107818623396
            },
            "grammar-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3572862655,
              "format_passes": 0,
              "gpu_energy_j": 91.72934359524177,
              "semantic_passes": 0,
              "tokens_per_s": 79.00864629374314
            },
            "grammar-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4679678805,
              "format_passes": 0,
              "gpu_energy_j": 121.85530667970366,
              "semantic_passes": 0,
              "tokens_per_s": 79.09829138779617
            },
            "grammar-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.084976788,
              "format_passes": 0,
              "gpu_energy_j": 289.1298877606463,
              "semantic_passes": 0,
              "tokens_per_s": 78.12936746596591
            },
            "grammar-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233467744,
              "format_passes": 0,
              "gpu_energy_j": 52.747491915150675,
              "semantic_passes": 0,
              "tokens_per_s": 78.50102797522015
            },
            "grammar-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954364015,
              "format_passes": 0,
              "gpu_energy_j": 76.4874237970336,
              "semantic_passes": 0,
              "tokens_per_s": 78.81615873661087
            },
            "grammar-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351764199,
              "format_passes": 0,
              "gpu_energy_j": 91.45000413316039,
              "semantic_passes": 0,
              "tokens_per_s": 79.15804980283008
            },
            "grammar-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.368105464,
              "format_passes": 0,
              "gpu_energy_j": 95.63363048157015,
              "semantic_passes": 0,
              "tokens_per_s": 79.17302077230663
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.359025512,
              "format_passes": 0,
              "gpu_energy_j": 90.81604002827939,
              "semantic_passes": 0,
              "tokens_per_s": 78.48239126242046,
              "ttft_s": 0.078619999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4710328155,
              "format_passes": 0,
              "gpu_energy_j": 120.04444903825245,
              "semantic_passes": 2,
              "tokens_per_s": 78.74851874337172,
              "ttft_s": 0.115439994
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.082291807,
              "format_passes": 2,
              "gpu_energy_j": 290.1070022918162,
              "semantic_passes": 2,
              "tokens_per_s": 77.67821318686502,
              "ttft_s": 0.8247374315
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233510317,
              "format_passes": 0,
              "gpu_energy_j": 55.218157427775225,
              "semantic_passes": 0,
              "tokens_per_s": 78.22560971909772,
              "ttft_s": 0.06724033600000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1981201175,
              "format_passes": 0,
              "gpu_energy_j": 48.83366245962917,
              "semantic_passes": 0,
              "tokens_per_s": 2562.807977656126,
              "ttft_s": 0.1979254615
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7186871665,
              "format_passes": 0,
              "gpu_energy_j": 189.45084006012792,
              "semantic_passes": 0,
              "tokens_per_s": 2854.730451948488,
              "ttft_s": 0.718397371
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4237666139999998,
              "format_passes": 0,
              "gpu_energy_j": 382.667424838954,
              "semantic_passes": 0,
              "tokens_per_s": 2880.3637912726226,
              "ttft_s": 1.4234463415
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.297552372,
              "format_passes": 2,
              "gpu_energy_j": 74.34536687486207,
              "semantic_passes": 2,
              "tokens_per_s": 77.96874898672286,
              "ttft_s": 0.0794495465
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35495679950000003,
              "format_passes": 2,
              "gpu_energy_j": 87.69152801969655,
              "semantic_passes": 2,
              "tokens_per_s": 78.47927583939034,
              "ttft_s": 0.07459752950000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691623135,
              "format_passes": 2,
              "gpu_energy_j": 96.34434013545112,
              "semantic_passes": 2,
              "tokens_per_s": 78.98991211352876,
              "ttft_s": 0.077964588
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6211160005,
              "format_passes": 0,
              "gpu_energy_j": 163.54819602547445,
              "semantic_passes": 0,
              "tokens_per_s": 78.94324944158046,
              "ttft_s": 0.319225608
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561372723,
              "format_passes": 0,
              "gpu_energy_j": 146.27320664258593,
              "semantic_passes": 0,
              "tokens_per_s": 78.73318357223586,
              "ttft_s": 0.2559556865
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
              "e2e_s": 0.6666287485,
              "format_passes": 2,
              "gpu_energy_j": 179.51799442218424,
              "semantic_passes": 2,
              "tokens_per_s": 79.2485079383699,
              "ttft_s": 0.124006237
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659263074,
              "format_passes": 0,
              "gpu_energy_j": 459.31871371985835,
              "semantic_passes": 0,
              "tokens_per_s": 79.57650276340391,
              "ttft_s": 0.06293201300000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237844764,
              "format_passes": 2,
              "gpu_energy_j": 61.07334141698627,
              "semantic_passes": 2,
              "tokens_per_s": 78.28260908862339,
              "ttft_s": 0.071720036
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24185452000000002,
              "format_passes": 0,
              "gpu_energy_j": 62.57658685887361,
              "semantic_passes": 0,
              "tokens_per_s": 77.48334122524282,
              "ttft_s": 0.1256718175
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.181834411,
              "format_passes": 2,
              "gpu_energy_j": 42.01104580384498,
              "semantic_passes": 2,
              "tokens_per_s": 77.67761705313649,
              "ttft_s": 0.0658942165
            },
            "grammar-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.690846064,
              "format_passes": 0,
              "gpu_energy_j": 183.8080407951233,
              "semantic_passes": 0,
              "tokens_per_s": 75.90552716447993
            },
            "grammar-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.434752013,
              "format_passes": 0,
              "gpu_energy_j": 78.3261635520102,
              "semantic_passes": 0,
              "tokens_per_s": 35.89208701352104
            },
            "grammar-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4285085635,
              "format_passes": 0,
              "gpu_energy_j": 84.00669854947387,
              "semantic_passes": 0,
              "tokens_per_s": 43.03272424192302
            },
            "grammar-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2592724235,
              "format_passes": 0,
              "gpu_energy_j": 54.8978828816322,
              "semantic_passes": 0,
              "tokens_per_s": 62.73116156102164
            },
            "grammar-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5335335050000001,
              "format_passes": 0,
              "gpu_energy_j": 108.3804521452092,
              "semantic_passes": 0,
              "tokens_per_s": 55.07038101732501
            },
            "grammar-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9021315249999999,
              "format_passes": 0,
              "gpu_energy_j": 218.72059724674943,
              "semantic_passes": 0,
              "tokens_per_s": 70.94154150306586
            },
            "grammar-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.173239713,
              "format_passes": 0,
              "gpu_energy_j": 302.65682146146264,
              "semantic_passes": 0,
              "tokens_per_s": 60.9372449052502
            },
            "grammar-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4373875575,
              "format_passes": 0,
              "gpu_energy_j": 91.23922668902594,
              "semantic_passes": 0,
              "tokens_per_s": 56.95226834344955
            },
            "grammar-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3970247365,
              "format_passes": 0,
              "gpu_energy_j": 73.43036664809293,
              "semantic_passes": 0,
              "tokens_per_s": 44.15863305553601
            },
            "grammar-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.931895973,
              "format_passes": 0,
              "gpu_energy_j": 239.99602431479718,
              "semantic_passes": 0,
              "tokens_per_s": 72.32512253489176
            },
            "grammar-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8571162655,
              "format_passes": 0,
              "gpu_energy_j": 218.73254654141306,
              "semantic_passes": 0,
              "tokens_per_s": 71.74012929644466
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3574978955,
              "format_passes": 0,
              "gpu_energy_j": 88.85479653584248,
              "semantic_passes": 0,
              "tokens_per_s": 78.86401243584437,
              "ttft_s": 0.07848108
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46866221750000003,
              "format_passes": 0,
              "gpu_energy_j": 121.45565800861766,
              "semantic_passes": 2,
              "tokens_per_s": 79.05127260200214,
              "ttft_s": 0.1144756265
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0822753415,
              "format_passes": 2,
              "gpu_energy_j": 287.930324838165,
              "semantic_passes": 2,
              "tokens_per_s": 77.9187955311406,
              "ttft_s": 0.8255687654999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234676642,
              "format_passes": 0,
              "gpu_energy_j": 56.67829593097806,
              "semantic_passes": 0,
              "tokens_per_s": 77.78479539413485,
              "ttft_s": 0.067532414
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19895641149999999,
              "format_passes": 0,
              "gpu_energy_j": 48.85984181055797,
              "semantic_passes": 0,
              "tokens_per_s": 2552.1744986791155,
              "ttft_s": 0.198755926
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7188552539999999,
              "format_passes": 0,
              "gpu_energy_j": 190.25758111968395,
              "semantic_passes": 0,
              "tokens_per_s": 2853.9712566317435,
              "ttft_s": 0.7185968835000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.421568475,
              "format_passes": 0,
              "gpu_energy_j": 384.5015919229497,
              "semantic_passes": 0,
              "tokens_per_s": 2885.000154247571,
              "ttft_s": 1.4211453825
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2950508845,
              "format_passes": 2,
              "gpu_energy_j": 76.26282437539143,
              "semantic_passes": 2,
              "tokens_per_s": 78.56821240327665,
              "ttft_s": 0.0785939605
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352842993,
              "format_passes": 2,
              "gpu_energy_j": 91.62875462641694,
              "semantic_passes": 2,
              "tokens_per_s": 78.80137650587592,
              "ttft_s": 0.0736563675
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3694058565,
              "format_passes": 2,
              "gpu_energy_j": 95.16119248663549,
              "semantic_passes": 2,
              "tokens_per_s": 78.80308327470637,
              "ttft_s": 0.077510935
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6197854119999999,
              "format_passes": 0,
              "gpu_energy_j": 164.43009767239386,
              "semantic_passes": 0,
              "tokens_per_s": 79.0004831355871,
              "ttft_s": 0.3187553715
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560444572,
              "format_passes": 0,
              "gpu_energy_j": 145.73709443256405,
              "semantic_passes": 0,
              "tokens_per_s": 78.78060755828962,
              "ttft_s": 0.255732777
            }
          }
        }
      },
      "change_exercised": false,
      "complete": true,
      "grammar": {
        "arms": {
          "A": {
            "grammar_format_passes": 24,
            "length_stops": 0,
            "median_pipeline_e2e_s": 0.35927871499999997,
            "original_format_passes": 16,
            "questions": 24,
            "semantic_passes": 18,
            "starts": 2
          },
          "B": {
            "grammar_format_passes": 24,
            "length_stops": 0,
            "median_pipeline_e2e_s": 0.6191517915,
            "original_format_passes": 0,
            "questions": 24,
            "semantic_passes": 0,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Same12 questions and matched cap: original12 first, diagnostic12, timed production12. Timed requests omit verbose/raw-token serialization; generation parameters match the preceding diagnostic. Diagnostic/output differences are separate stability findings. Full production request+container-parse latency; render/tokenize/diagnostic calls excluded. At most58requests/start. Different output lengths: no direct candidate token/s percentage or common-kernel speed gain. Semantic answer quality, original answer-format compliance and JSON/schema compliance remain separate.",
        "original_quality": {
          "A": {
            "attempts": 24,
            "passes": 18
          },
          "B": {
            "attempts": 24,
            "passes": 18
          }
        },
        "paired_e2e_change_pct": 60.05138669754495,
        "per_question_pipeline_e2e_s": {
          "code": {
            "A": 0.671916507,
            "B": 0.6991763105
          },
          "energy": {
            "A": 0.245459467,
            "B": 0.418949511
          },
          "filtering": {
            "A": 0.24744718300000001,
            "B": 0.4408537015
          },
          "german": {
            "A": 0.1872026665,
            "B": 0.25133977750000003
          },
          "ha_sim": {
            "A": 0.364168269,
            "B": 0.541547838
          },
          "jarvis_memory": {
            "A": 0.4736307695,
            "B": 0.8962193734999999
          },
          "long_context": {
            "A": 1.0860501715000002,
            "B": 1.1765311865
          },
          "math": {
            "A": 0.23929604999999998,
            "B": 0.43971642499999997
          },
          "pve_sim": {
            "A": 0.30024330450000003,
            "B": 0.406100862
          },
          "sorting": {
            "A": 0.3543958905,
            "B": 0.9307143179999999
          },
          "time": {
            "A": 0.375071245,
            "B": 0.8629190215
          }
        }
      }
    }
  }
}
```

</details>
