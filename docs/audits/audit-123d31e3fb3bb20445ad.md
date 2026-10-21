# Public audit excerpt

Original SHA256: `123d31e3fb3bb20445ad202d5d3bdafcb8bcc0044fe977d782dea3f1fd9c16e0`

Original file: `RESULTS.json`; 39898 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7629555875,
              "format_passes": 2,
              "gpu_energy_j": 487.1150397170652,
              "semantic_passes": 2,
              "tokens_per_s": 35.403392555312884,
              "ttft_s": 0.520098146
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.788006942,
              "format_passes": 0,
              "gpu_energy_j": 1066.6831569949218,
              "semantic_passes": 0,
              "tokens_per_s": 35.346014470385164,
              "ttft_s": 0.1957192735
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.582511058,
              "format_passes": 2,
              "gpu_energy_j": 146.47409510340736,
              "semantic_passes": 2,
              "tokens_per_s": 34.9335770783556,
              "ttft_s": 0.2103673985
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9250604465,
              "format_passes": 0,
              "gpu_energy_j": 244.96269849711263,
              "semantic_passes": 0,
              "tokens_per_s": 34.94120412777773,
              "ttft_s": 0.524335446
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4650394875,
              "format_passes": 2,
              "gpu_energy_j": 109.94629879171868,
              "semantic_passes": 2,
              "tokens_per_s": 34.265091451437044,
              "ttft_s": 0.2023714775
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9887876369999999,
              "format_passes": 0,
              "gpu_energy_j": 269.6854196597915,
              "semantic_passes": 0,
              "tokens_per_s": 35.28471284177391,
              "ttft_s": 0.2235362985
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1467912409999999,
              "format_passes": 0,
              "gpu_energy_j": 292.2111363447448,
              "semantic_passes": 2,
              "tokens_per_s": 35.27147848320086,
              "ttft_s": 0.3529080455
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7938524145,
              "format_passes": 2,
              "gpu_energy_j": 1018.2593731214133,
              "semantic_passes": 2,
              "tokens_per_s": 34.38290912516985,
              "ttft_s": 3.2120734295
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574592088,
              "format_passes": 2,
              "gpu_energy_j": 144.1196211653944,
              "semantic_passes": 2,
              "tokens_per_s": 34.93724042691049,
              "ttft_s": 0.2024406305
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.725318158,
              "format_passes": 0,
              "gpu_energy_j": 190.45317042433567,
              "semantic_passes": 0,
              "tokens_per_s": 697.2614911822634,
              "ttft_s": 0.7251699275
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.750970062,
              "format_passes": 0,
              "gpu_energy_j": 734.5905094989612,
              "semantic_passes": 0,
              "tokens_per_s": 744.8048556563605,
              "ttft_s": 2.7507356255
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.468648863,
              "format_passes": 0,
              "gpu_energy_j": 1478.4596749670568,
              "semantic_passes": 0,
              "tokens_per_s": 749.2279178892334,
              "ttft_s": 5.468308024000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.848921676,
              "format_passes": 0,
              "gpu_energy_j": 226.14837143878634,
              "semantic_passes": 2,
              "tokens_per_s": 35.150832995116225,
              "ttft_s": 0.223072163
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9880751605,
              "format_passes": 0,
              "gpu_energy_j": 257.83761874922214,
              "semantic_passes": 2,
              "tokens_per_s": 35.04872947846813,
              "ttft_s": 0.217660982
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0155009045,
              "format_passes": 0,
              "gpu_energy_j": 278.39862131796326,
              "semantic_passes": 2,
              "tokens_per_s": 35.28702088135555,
              "ttft_s": 0.22194065400000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7088936305,
              "format_passes": 0,
              "gpu_energy_j": 459.3853697989201,
              "semantic_passes": 0,
              "tokens_per_s": 35.01780011512438,
              "ttft_s": 1.030277734
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7800818755,
              "format_passes": 0,
              "gpu_energy_j": 466.23831105592694,
              "semantic_passes": 0,
              "tokens_per_s": 35.05419524724905,
              "ttft_s": 1.0947529955
            }
          }
        },
        "B": {
          "format_passes": 8,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.772567028,
              "format_passes": 2,
              "gpu_energy_j": 489.8149537951035,
              "semantic_passes": 2,
              "tokens_per_s": 35.124494066428866,
              "ttft_s": 0.5198392304999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.8141433510000002,
              "format_passes": 0,
              "gpu_energy_j": 1081.8456814821702,
              "semantic_passes": 0,
              "tokens_per_s": 35.111398532694935,
              "ttft_s": 0.1974116345
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7275745954999999,
              "format_passes": 0,
              "gpu_energy_j": 193.85056088362376,
              "semantic_passes": 2,
              "tokens_per_s": 34.822579102125005,
              "ttft_s": 0.2106511475
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9275017805,
              "format_passes": 0,
              "gpu_energy_j": 244.4370822611155,
              "semantic_passes": 0,
              "tokens_per_s": 34.72187878067822,
              "ttft_s": 0.5242442475
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4653168875,
              "format_passes": 2,
              "gpu_energy_j": 112.66569867301497,
              "semantic_passes": 2,
              "tokens_per_s": 34.36051711239652,
              "ttft_s": 0.2033686785
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.999008022,
              "format_passes": 0,
              "gpu_energy_j": 269.70287274512907,
              "semantic_passes": 0,
              "tokens_per_s": 34.94820526379338,
              "ttft_s": 0.226421558
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1556090085,
              "format_passes": 0,
              "gpu_energy_j": 304.81938110346135,
              "semantic_passes": 2,
              "tokens_per_s": 34.99119019017307,
              "ttft_s": 0.35535058750000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 4.002564058,
              "format_passes": 0,
              "gpu_energy_j": 1087.207985042337,
              "semantic_passes": 2,
              "tokens_per_s": 33.298645335372264,
              "ttft_s": 3.2517241765
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5790820295,
              "format_passes": 2,
              "gpu_energy_j": 142.5859948396536,
              "semantic_passes": 2,
              "tokens_per_s": 34.652346897723774,
              "ttft_s": 0.203930213
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.730046079,
              "format_passes": 0,
              "gpu_energy_j": 190.81599872263132,
              "semantic_passes": 0,
              "tokens_per_s": 692.7855677383766,
              "ttft_s": 0.7298844545000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7827093785,
              "format_passes": 0,
              "gpu_energy_j": 750.3906907142789,
              "semantic_passes": 0,
              "tokens_per_s": 736.3130172336721,
              "ttft_s": 2.7824702035
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.581622382000001,
              "format_passes": 0,
              "gpu_energy_j": 1518.993851877118,
              "semantic_passes": 0,
              "tokens_per_s": 734.0651613944747,
              "ttft_s": 5.581309168
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.854975254,
              "format_passes": 0,
              "gpu_energy_j": 228.49854014380145,
              "semantic_passes": 2,
              "tokens_per_s": 34.877315380853986,
              "ttft_s": 0.2241396015
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.990867255,
              "format_passes": 0,
              "gpu_energy_j": 265.7099362831116,
              "semantic_passes": 2,
              "tokens_per_s": 34.98109473438559,
              "ttft_s": 0.2189890675
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0240517085,
              "format_passes": 0,
              "gpu_energy_j": 279.05789046094935,
              "semantic_passes": 2,
              "tokens_per_s": 34.947251810878925,
              "ttft_s": 0.22279257200000002
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7251679415,
              "format_passes": 0,
              "gpu_energy_j": 466.88850162221786,
              "semantic_passes": 0,
              "tokens_per_s": 34.49910815842796,
              "ttft_s": 1.0346174339999998
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.792560087,
              "format_passes": 0,
              "gpu_energy_j": 473.8792390091447,
              "semantic_passes": 0,
              "tokens_per_s": 34.44665608555965,
              "ttft_s": 1.096358984
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": -4,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.5451890318819652,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5542662118596331,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.7877733424791922,
            "ttft_change_pct": -0.049782046329405194
          },
          "decode": {
            "e2e_change_pct": 0.6899778537945433,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.421464695286323,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6637691440057658,
            "ttft_change_pct": 0.8646879633956717
          },
          "energy": {
            "e2e_change_pct": 24.90313883449058,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 32.344603833715226,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.31774008135961873,
            "ttft_change_pct": 0.13488259208567221
          },
          "filtering": {
            "e2e_change_pct": 0.2639107540741703,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2145699076724239,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6276983079846254,
            "ttft_change_pct": -0.017393159416512205
          },
          "german": {
            "e2e_change_pct": 0.05965084846693003,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.473389201075249,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.27849235743240275,
            "ttft_change_pct": 0.49275768123004937
          },
          "ha_sim": {
            "e2e_change_pct": 1.0336279113489777,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.006471645875261167,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9536922674970194,
            "ttft_change_pct": 1.290734220509604
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.768907817286002,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.314772159758351,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.7946598925851145,
            "ttft_change_pct": 0.6921185365835081
          },
          "long_context": {
            "e2e_change_pct": 5.501311614081494,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 6.7712229065533425,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.1534963660298843,
            "ttft_change_pct": 1.2344284111266868
          },
          "math": {
            "e2e_change_pct": 0.7814137357213369,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0641343026989825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8154437090780564,
            "ttft_change_pct": 0.7358120236639065
          },
          "prefill": {
            "e2e_change_pct": 0.6518409814855408,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.19050788048697864,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.6419289607257017,
            "ttft_change_pct": 0.6501272075985387
          },
          "prefill2048": {
            "e2e_change_pct": 1.1537499785412075,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.15088284030438,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.1401427311057089,
            "ttft_change_pct": 1.1536760459933904
          },
          "prefill4096": {
            "e2e_change_pct": 2.0658396951459324,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.741649136352975,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.0237842361074954,
            "ttft_change_pct": 2.066473642377953
          },
          "pve_sim": {
            "e2e_change_pct": 0.7130902851395726,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0392154009613241,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.778125554806175,
            "ttft_change_pct": 0.47851712452351425
          },
          "sorting": {
            "e2e_change_pct": 0.2825791611426709,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.053207507918465,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1929734546414541,
            "ttft_change_pct": 0.610162413031845
          },
          "time": {
            "e2e_change_pct": 0.8420282012658653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.23680761774791392,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9628726426609502,
            "ttft_change_pct": 0.3838494591441588
          },
          "tool-call": {
            "e2e_change_pct": 0.9523302509611753,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6332979490796484,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.4812237062041933,
            "ttft_change_pct": 0.42121651830242524
          },
          "tool-final": {
            "e2e_change_pct": 0.7009908741694826,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6388460090104529,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.7331425166209558,
            "ttft_change_pct": 0.14669870798267315
          }
        }
      },
      "complete": true
    }
  }
}
```
