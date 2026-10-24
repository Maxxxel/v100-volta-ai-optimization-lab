# Public audit excerpt

Original SHA256: `2378a3f8a79d525edbce569315b0e2c3cd86f33790283fb255a05a312c8d7e3c`

Original file: `RESULTS.json`; 39674 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6658436355,
              "format_passes": 2,
              "gpu_energy_j": 171.2191921376815,
              "semantic_passes": 2,
              "tokens_per_s": 79.35905535591789,
              "ttft_s": 0.123972003
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6591842765,
              "format_passes": 0,
              "gpu_energy_j": 445.74720511291616,
              "semantic_passes": 0,
              "tokens_per_s": 79.56680579715061,
              "ttft_s": 0.0629099545
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23792092050000002,
              "format_passes": 2,
              "gpu_energy_j": 55.67654020665047,
              "semantic_passes": 2,
              "tokens_per_s": 78.29320874645894,
              "ttft_s": 0.071842428
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241705639,
              "format_passes": 0,
              "gpu_energy_j": 55.86357013243661,
              "semantic_passes": 0,
              "tokens_per_s": 77.39052865436958,
              "ttft_s": 0.12541721249999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1824977135,
              "format_passes": 2,
              "gpu_energy_j": 38.57368553215947,
              "semantic_passes": 2,
              "tokens_per_s": 77.47038549906787,
              "ttft_s": 0.06628400000000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35883620250000003,
              "format_passes": 0,
              "gpu_energy_j": 88.38952743855776,
              "semantic_passes": 0,
              "tokens_per_s": 78.6697336174757,
              "ttft_s": 0.07914080849999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4691949555,
              "format_passes": 0,
              "gpu_energy_j": 117.35022872449328,
              "semantic_passes": 2,
              "tokens_per_s": 79.04716178956009,
              "ttft_s": 0.114958126
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.076110542,
              "format_passes": 2,
              "gpu_energy_j": 286.62758442002905,
              "semantic_passes": 2,
              "tokens_per_s": 78.01214154470198,
              "ttft_s": 0.8197127365
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234362808,
              "format_passes": 0,
              "gpu_energy_j": 51.04978303960483,
              "semantic_passes": 0,
              "tokens_per_s": 78.25156932073278,
              "ttft_s": 0.068173484
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1984825875,
              "format_passes": 0,
              "gpu_energy_j": 46.35846334321296,
              "semantic_passes": 0,
              "tokens_per_s": 2557.387276988344,
              "ttft_s": 0.1983281845
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.714484893,
              "format_passes": 0,
              "gpu_energy_j": 187.63177610454972,
              "semantic_passes": 0,
              "tokens_per_s": 2871.613286014345,
              "ttft_s": 0.714242134
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4083748895000001,
              "format_passes": 0,
              "gpu_energy_j": 377.0777312704276,
              "semantic_passes": 0,
              "tokens_per_s": 2911.812084788885,
              "ttft_s": 1.408067231
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29539813049999997,
              "format_passes": 2,
              "gpu_energy_j": 74.03523944942891,
              "semantic_passes": 2,
              "tokens_per_s": 78.63782739777811,
              "ttft_s": 0.079177155
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3531452585,
              "format_passes": 2,
              "gpu_energy_j": 88.13077215153392,
              "semantic_passes": 2,
              "tokens_per_s": 78.78290385612281,
              "ttft_s": 0.07389021800000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369817445,
              "format_passes": 2,
              "gpu_energy_j": 90.84395896811361,
              "semantic_passes": 2,
              "tokens_per_s": 78.78136804548951,
              "ttft_s": 0.07783699
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6193132105000001,
              "format_passes": 0,
              "gpu_energy_j": 157.0240957178815,
              "semantic_passes": 0,
              "tokens_per_s": 79.0046614959765,
              "ttft_s": 0.3178410365
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559173676,
              "format_passes": 0,
              "gpu_energy_j": 141.24026724598855,
              "semantic_passes": 0,
              "tokens_per_s": 78.77156562653894,
              "ttft_s": 0.254674742
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
              "e2e_s": 0.6624417705,
              "format_passes": 2,
              "gpu_energy_j": 174.08681905991227,
              "semantic_passes": 2,
              "tokens_per_s": 79.77270560090739,
              "ttft_s": 0.1233393275
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6494591829999998,
              "format_passes": 0,
              "gpu_energy_j": 442.2416626347373,
              "semantic_passes": 0,
              "tokens_per_s": 80.02268660928112,
              "ttft_s": 0.0622739725
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23549290350000002,
              "format_passes": 2,
              "gpu_energy_j": 57.354856866149944,
              "semantic_passes": 2,
              "tokens_per_s": 79.48865939437641,
              "ttft_s": 0.0719348005
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23843245400000002,
              "format_passes": 0,
              "gpu_energy_j": 59.31112756969593,
              "semantic_passes": 0,
              "tokens_per_s": 79.2560540333587,
              "ttft_s": 0.12484946250000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.17913333450000002,
              "format_passes": 2,
              "gpu_energy_j": 38.62540111902173,
              "semantic_passes": 2,
              "tokens_per_s": 79.59078238210077,
              "ttft_s": 0.0659851745
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35419021100000003,
              "format_passes": 0,
              "gpu_energy_j": 90.66065433893823,
              "semantic_passes": 0,
              "tokens_per_s": 79.7041771682677,
              "ttft_s": 0.07816076599999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4640209865,
              "format_passes": 0,
              "gpu_energy_j": 115.39916209390387,
              "semantic_passes": 2,
              "tokens_per_s": 79.83121914490143,
              "ttft_s": 0.1132218355
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0706857055,
              "format_passes": 2,
              "gpu_energy_j": 286.9949451078863,
              "semantic_passes": 2,
              "tokens_per_s": 79.1131986379216,
              "ttft_s": 0.817833998
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2300303485,
              "format_passes": 0,
              "gpu_energy_j": 53.31955155301617,
              "semantic_passes": 0,
              "tokens_per_s": 79.67889422045673,
              "ttft_s": 0.0668249485
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1984255875,
              "format_passes": 0,
              "gpu_energy_j": 48.86911604783777,
              "semantic_passes": 0,
              "tokens_per_s": 2558.9135090281566,
              "ttft_s": 0.1982933945
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.713250159,
              "format_passes": 0,
              "gpu_energy_j": 188.2049550651813,
              "semantic_passes": 0,
              "tokens_per_s": 2876.5300263910553,
              "ttft_s": 0.7129625625
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4034252055,
              "format_passes": 0,
              "gpu_energy_j": 380.5753467707276,
              "semantic_passes": 0,
              "tokens_per_s": 2922.1537886678793,
              "ttft_s": 1.4030599965000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2918044665,
              "format_passes": 2,
              "gpu_energy_j": 72.70296329856743,
              "semantic_passes": 2,
              "tokens_per_s": 79.78096613095646,
              "ttft_s": 0.078691968
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.349623624,
              "format_passes": 2,
              "gpu_energy_j": 86.01019238175775,
              "semantic_passes": 2,
              "tokens_per_s": 79.64468184942767,
              "ttft_s": 0.073352369
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3656516145,
              "format_passes": 2,
              "gpu_energy_j": 90.75974608950912,
              "semantic_passes": 2,
              "tokens_per_s": 79.74011876754528,
              "ttft_s": 0.0771632135
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.613678688,
              "format_passes": 0,
              "gpu_energy_j": 158.85475251973594,
              "semantic_passes": 0,
              "tokens_per_s": 79.78106143077883,
              "ttft_s": 0.313622562
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5548389254999999,
              "format_passes": 0,
              "gpu_energy_j": 142.4440503855514,
              "semantic_passes": 0,
              "tokens_per_s": 79.71820275736852,
              "ttft_s": 0.2537713275
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
            "e2e_change_pct": -0.51091049288855,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6748279713437952,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5212388720283068,
            "ttft_change_pct": -0.5103374025504759
          },
          "decode": {
            "e2e_change_pct": -0.5861370335858651,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7864418302501397,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5729535169386457,
            "ttft_change_pct": -1.0109401684593622
          },
          "energy": {
            "e2e_change_pct": -1.0205142931094202,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.014405444860957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.5268893267470496,
            "ttft_change_pct": 0.12857652862179325
          },
          "filtering": {
            "e2e_change_pct": -1.3542029939979994,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.171387594967781,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.410534481965687,
            "ttft_change_pct": -0.4526890597253419
          },
          "german": {
            "e2e_change_pct": -1.8435184394789528,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1340696024991983,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.737041863640144,
            "ttft_change_pct": -0.4508259911894519
          },
          "ha_sim": {
            "e2e_change_pct": -1.2947387882358385,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.56945247496565,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.3149193510961776,
            "ttft_change_pct": -1.238352903609774
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.1027332965433012,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.662601472358427,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9918855245285796,
            "ttft_change_pct": -1.5103677838311236
          },
          "long_context": {
            "e2e_change_pct": -0.5041151710973413,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1281665505434626,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4113919595306834,
            "ttft_change_pct": -0.2291947430293484
          },
          "math": {
            "e2e_change_pct": -1.848612216661949,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.446186405239816,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.8240207987059165,
            "ttft_change_pct": -1.9780938583100927
          },
          "prefill": {
            "e2e_change_pct": -0.02871788438368883,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.41573754513236,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0596793474944457,
            "ttft_change_pct": -0.017541631860196194
          },
          "prefill2048": {
            "e2e_change_pct": -0.1728145706224149,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.30548075199812175,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17121875012406917,
            "ttft_change_pct": -0.1791509404288405
          },
          "prefill4096": {
            "e2e_change_pct": -0.35144648182113825,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9275582221511813,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3551638491034126,
            "ttft_change_pct": -0.35561047013669134
          },
          "pve_sim": {
            "e2e_change_pct": -1.2165493376404268,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7995162314177748,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4536753760959753,
            "ttft_change_pct": -0.6127866049241093
          },
          "sorting": {
            "e2e_change_pct": -0.997219816842021,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.406174050228449,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.0938642156154588,
            "ttft_change_pct": -0.7279028463551218
          },
          "time": {
            "e2e_change_pct": -1.1264559193523205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.0927005819220672,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.216976482944765,
            "ttft_change_pct": -0.8656250710619706
          },
          "tool-call": {
            "e2e_change_pct": -0.9098017617694687,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1658445116242033,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9827267405504436,
            "ttft_change_pct": -1.3272277697219281
          },
          "tool-final": {
            "e2e_change_pct": -0.7752064673373638,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8522945779097846,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.2017497980396197,
            "ttft_change_pct": -0.3547326652440619
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
