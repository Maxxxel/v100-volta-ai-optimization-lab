# Public audit excerpt

Original SHA256: `eafc50d2ff1739a11233ef09fcc3d4ad81ce30d39657029845e735e32cf24951`

Original file: `RESULTS.json`; 39664 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 0.665697078,
              "format_passes": 2,
              "gpu_energy_j": 179.28202348710454,
              "semantic_passes": 2,
              "tokens_per_s": 79.30792609585889,
              "ttft_s": 0.123475125
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6586392835,
              "format_passes": 0,
              "gpu_energy_j": 459.67073230333324,
              "semantic_passes": 0,
              "tokens_per_s": 79.59658080125867,
              "ttft_s": 0.0629006895
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2377188985,
              "format_passes": 2,
              "gpu_energy_j": 58.5862113266448,
              "semantic_passes": 2,
              "tokens_per_s": 78.26540010979788,
              "ttft_s": 0.07156602949999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242072407,
              "format_passes": 0,
              "gpu_energy_j": 60.32436955071745,
              "semantic_passes": 0,
              "tokens_per_s": 77.11360947762753,
              "ttft_s": 0.12542138549999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182100792,
              "format_passes": 2,
              "gpu_energy_j": 42.01622789836305,
              "semantic_passes": 2,
              "tokens_per_s": 77.49835316143194,
              "ttft_s": 0.06594503800000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357694114,
              "format_passes": 0,
              "gpu_energy_j": 92.63821575918216,
              "semantic_passes": 0,
              "tokens_per_s": 78.84109532516666,
              "ttft_s": 0.0786251765
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4697619595,
              "format_passes": 0,
              "gpu_energy_j": 119.50839273060686,
              "semantic_passes": 2,
              "tokens_per_s": 78.88658379040476,
              "ttft_s": 0.11485211000000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.080381455,
              "format_passes": 2,
              "gpu_energy_j": 289.7283390847605,
              "semantic_passes": 2,
              "tokens_per_s": 77.72163415370281,
              "ttft_s": 0.8229716575
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2340296885,
              "format_passes": 0,
              "gpu_energy_j": 54.88467439939219,
              "semantic_passes": 0,
              "tokens_per_s": 78.08939584556573,
              "ttft_s": 0.06750181699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1978088575,
              "format_passes": 0,
              "gpu_energy_j": 49.31750891436462,
              "semantic_passes": 0,
              "tokens_per_s": 2566.294417481856,
              "ttft_s": 0.197681357
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7170397959999999,
              "format_passes": 0,
              "gpu_energy_j": 188.96847123099323,
              "semantic_passes": 0,
              "tokens_per_s": 2861.123806941645,
              "ttft_s": 0.7167819019999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4176756105,
              "format_passes": 0,
              "gpu_energy_j": 382.9057963815435,
              "semantic_passes": 0,
              "tokens_per_s": 2892.870978123782,
              "ttft_s": 1.417263783
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2965367565,
              "format_passes": 2,
              "gpu_energy_j": 72.63794014316207,
              "semantic_passes": 2,
              "tokens_per_s": 78.52301133585934,
              "ttft_s": 0.07999797750000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3569690845,
              "format_passes": 2,
              "gpu_energy_j": 87.19360289767009,
              "semantic_passes": 2,
              "tokens_per_s": 77.6896707618408,
              "ttft_s": 0.07370677649999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36884799300000004,
              "format_passes": 2,
              "gpu_energy_j": 94.2319062536395,
              "semantic_passes": 2,
              "tokens_per_s": 78.99111460113787,
              "ttft_s": 0.0775983485
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6202145029999999,
              "format_passes": 0,
              "gpu_energy_j": 162.35301623739514,
              "semantic_passes": 0,
              "tokens_per_s": 78.91621731920736,
              "ttft_s": 0.3187243625
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560702386,
              "format_passes": 0,
              "gpu_energy_j": 143.52652372030872,
              "semantic_passes": 0,
              "tokens_per_s": 78.75398586091268,
              "ttft_s": 0.25631689550000003
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
              "e2e_s": 0.6931719025,
              "format_passes": 2,
              "gpu_energy_j": 185.05067319937524,
              "semantic_passes": 2,
              "tokens_per_s": 78.49828557980166,
              "ttft_s": 0.14532846649999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6605358780000001,
              "format_passes": 0,
              "gpu_energy_j": 463.46763538756204,
              "semantic_passes": 0,
              "tokens_per_s": 79.59610316444382,
              "ttft_s": 0.0645634585
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2409314565,
              "format_passes": 2,
              "gpu_energy_j": 57.72957566026045,
              "semantic_passes": 2,
              "tokens_per_s": 78.25847946507974,
              "ttft_s": 0.0747553205
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.261866667,
              "format_passes": 0,
              "gpu_energy_j": 62.32055180037843,
              "semantic_passes": 0,
              "tokens_per_s": 77.63807936051333,
              "ttft_s": 0.145905363
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1826612845,
              "format_passes": 2,
              "gpu_energy_j": 40.75713574815072,
              "semantic_passes": 2,
              "tokens_per_s": 77.44100209376063,
              "ttft_s": 0.066398769
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.360475009,
              "format_passes": 0,
              "gpu_energy_j": 91.83819237101221,
              "semantic_passes": 0,
              "tokens_per_s": 78.8370972816095,
              "ttft_s": 0.08139642899999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.499485664,
              "format_passes": 0,
              "gpu_energy_j": 123.98120580020596,
              "semantic_passes": 2,
              "tokens_per_s": 79.0456467857795,
              "ttft_s": 0.1452366675
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.0423863155,
              "format_passes": 2,
              "gpu_energy_j": 826.702393441648,
              "semantic_passes": 2,
              "tokens_per_s": 77.98995889671014,
              "ttft_s": 2.785865509
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2336029795,
              "format_passes": 0,
              "gpu_energy_j": 56.295947751280046,
              "semantic_passes": 0,
              "tokens_per_s": 78.37534282105699,
              "ttft_s": 0.06768956849999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6475838055,
              "format_passes": 0,
              "gpu_energy_j": 168.25579919842323,
              "semantic_passes": 0,
              "tokens_per_s": 781.0760329914577,
              "ttft_s": 0.6474564395
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.565512901,
              "format_passes": 0,
              "gpu_energy_j": 707.7577162455179,
              "semantic_passes": 0,
              "tokens_per_s": 798.677196007167,
              "ttft_s": 2.5652409179999998
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.143741074499999,
              "format_passes": 0,
              "gpu_energy_j": 1433.4355700230128,
              "semantic_passes": 0,
              "tokens_per_s": 796.5794549205425,
              "ttft_s": 5.143409817
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29567705349999995,
              "format_passes": 2,
              "gpu_energy_j": 72.54734512043461,
              "semantic_passes": 2,
              "tokens_per_s": 78.70989969426678,
              "ttft_s": 0.0796270595
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352849795,
              "format_passes": 2,
              "gpu_energy_j": 91.41802510930972,
              "semantic_passes": 2,
              "tokens_per_s": 78.85644780230821,
              "ttft_s": 0.073859372
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3719271365,
              "format_passes": 2,
              "gpu_energy_j": 92.74794308539194,
              "semantic_passes": 2,
              "tokens_per_s": 78.8316942879199,
              "ttft_s": 0.0801344615
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8255369065,
              "format_passes": 0,
              "gpu_energy_j": 214.04253931466425,
              "semantic_passes": 0,
              "tokens_per_s": 79.11459212535782,
              "ttft_s": 0.5239548629999999
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8297744225,
              "format_passes": 0,
              "gpu_energy_j": 218.45536545473425,
              "semantic_passes": 0,
              "tokens_per_s": 78.80523083379967,
              "ttft_s": 0.5239850945
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
            "e2e_change_pct": 4.127226242684512,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.217639783436299,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.0208822193618072,
            "ttft_change_pct": 17.698578154911736
          },
          "decode": {
            "e2e_change_pct": 0.11434641147520797,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.82600496777403,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0006000720257581804,
            "ttft_change_pct": 2.6434829462402165
          },
          "energy": {
            "e2e_change_pct": 1.3514104348754552,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4621796613681237,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.008842534131847657,
            "ttft_change_pct": 4.456431385508131
          },
          "filtering": {
            "e2e_change_pct": 8.176999702407217,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3090809974942292,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6801262273139486,
            "ttft_change_pct": 16.332125034609856
          },
          "german": {
            "e2e_change_pct": 0.30779245594934057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.9966805998340895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07400295016829483,
            "ttft_change_pct": 0.6880441861296438
          },
          "ha_sim": {
            "e2e_change_pct": 0.7774505900871587,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8635997375528559,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0050710147299071195,
            "ttft_change_pct": 3.524637556775456
          },
          "jarvis_memory": {
            "e2e_change_pct": 6.327397078221697,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.742676951301327,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20163504075338956,
            "ttft_change_pct": 26.455375961312335
          },
          "long_context": {
            "e2e_change_pct": 181.60297471044612,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 185.33708371544387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3452381642885749,
            "ttft_change_pct": 238.51293463286737
          },
          "math": {
            "e2e_change_pct": -0.18233114043563203,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.571343216173805,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3661790085516481,
            "ttft_change_pct": 0.27814288317602465
          },
          "prefill": {
            "e2e_change_pct": 227.37856822210304,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 241.16848742418063,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -69.56405205612072,
            "ttft_change_pct": 227.5252908649347
          },
          "prefill2048": {
            "e2e_change_pct": 257.7922613656439,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 274.53746206178585,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -72.08519274596156,
            "ttft_change_pct": 257.88304794559394
          },
          "prefill4096": {
            "e2e_change_pct": 262.8291998820417,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 274.3572397098625,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -72.46405176918132,
            "ttft_change_pct": 262.91125750159665
          },
          "pve_sim": {
            "e2e_change_pct": -0.28991448147847043,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.12472135436233378,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2380045737269132,
            "ttft_change_pct": -0.46365922188471576
          },
          "sorting": {
            "e2e_change_pct": -1.1539625359349492,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.844876311164015,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.5018432038979679,
            "ttft_change_pct": 0.20703048925225787
          },
          "time": {
            "e2e_change_pct": 0.8348001232041158,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5747990539990209,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20182056427858752,
            "ttft_change_pct": 3.2682564114106194
          },
          "tool-call": {
            "e2e_change_pct": 33.105063249383605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 31.837735001909586,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.25137394174388206,
            "ttft_change_pct": 64.39121844662876
          },
          "tool-final": {
            "e2e_change_pct": 47.98838799662251,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 52.20557134125254,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06506968799966373,
            "ttft_change_pct": 104.42862085929092
          }
        }
      },
      "complete": true
    }
  }
}
```
