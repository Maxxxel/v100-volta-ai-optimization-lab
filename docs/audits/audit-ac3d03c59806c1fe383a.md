# Public audit excerpt

Original SHA256: `ac3d03c59806c1fe383a0c304714d150766cb3090737e7a4c3c7342b4a74dee9`

Original file: `RESULTS.json`; 48988 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.7244894205,
              "format_passes": 2,
              "gpu_energy_j": 183.35694376170835,
              "semantic_passes": 2,
              "tokens_per_s": 77.02214126404775,
              "ttft_s": 0.1595110575
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6591711304999999,
              "format_passes": 0,
              "gpu_energy_j": 449.64007992366135,
              "semantic_passes": 0,
              "tokens_per_s": 79.5699713571424,
              "ttft_s": 0.062871569
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.268463683,
              "format_passes": 2,
              "gpu_energy_j": 56.99212984025948,
              "semantic_passes": 2,
              "tokens_per_s": 76.70362475509222,
              "ttft_s": 0.093015768
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.275455032,
              "format_passes": 0,
              "gpu_energy_j": 61.18217571277341,
              "semantic_passes": 0,
              "tokens_per_s": 76.5026490919162,
              "ttft_s": 0.1513609835
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22061338549999998,
              "format_passes": 2,
              "gpu_energy_j": 44.97188828310376,
              "semantic_passes": 2,
              "tokens_per_s": 73.94216477795322,
              "ttft_s": 0.093924601
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.41071506599999996,
              "format_passes": 0,
              "gpu_energy_j": 93.80165676016901,
              "semantic_passes": 0,
              "tokens_per_s": 77.92027006018662,
              "ttft_s": 0.1168492015
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.508248552,
              "format_passes": 0,
              "gpu_energy_j": 120.69020600767654,
              "semantic_passes": 2,
              "tokens_per_s": 78.37539129453276,
              "ttft_s": 0.1443530575
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.10271941,
              "format_passes": 2,
              "gpu_energy_j": 286.07658275634395,
              "semantic_passes": 2,
              "tokens_per_s": 77.39028894933939,
              "ttft_s": 0.8408313985
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2581507265,
              "format_passes": 0,
              "gpu_energy_j": 54.767503877416345,
              "semantic_passes": 0,
              "tokens_per_s": 77.54596893541203,
              "ttft_s": 0.08815944649999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1971371995,
              "format_passes": 0,
              "gpu_energy_j": 47.28993421214539,
              "semantic_passes": 0,
              "tokens_per_s": 2576.0385962377527,
              "ttft_s": 0.197001476
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7143215585,
              "format_passes": 0,
              "gpu_energy_j": 189.01576197035672,
              "semantic_passes": 0,
              "tokens_per_s": 2876.5142080493615,
              "ttft_s": 0.713599702
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4091194224999999,
              "format_passes": 0,
              "gpu_energy_j": 381.1896593393785,
              "semantic_passes": 0,
              "tokens_per_s": 2910.453639954765,
              "ttft_s": 1.408773751
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.334708349,
              "format_passes": 2,
              "gpu_energy_j": 73.83149117574072,
              "semantic_passes": 2,
              "tokens_per_s": 77.77141978473213,
              "ttft_s": 0.11038128999999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37380897300000004,
              "format_passes": 2,
              "gpu_energy_j": 90.5732744057241,
              "semantic_passes": 2,
              "tokens_per_s": 78.35214930291508,
              "ttft_s": 0.089850461
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39815292599999996,
              "format_passes": 2,
              "gpu_energy_j": 96.2080774417498,
              "semantic_passes": 2,
              "tokens_per_s": 78.08625529105964,
              "ttft_s": 0.0982238195
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194539225,
              "format_passes": 0,
              "gpu_energy_j": 159.55427644896645,
              "semantic_passes": 0,
              "tokens_per_s": 78.9471929408021,
              "ttft_s": 0.3182200335
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560781481,
              "format_passes": 0,
              "gpu_energy_j": 142.0861662522851,
              "semantic_passes": 0,
              "tokens_per_s": 78.76444876408978,
              "ttft_s": 0.2563349625
            }
          }
        }
      }
    },
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
              "e2e_s": 0.5282137465000001,
              "format_passes": 2,
              "gpu_energy_j": 129.43352845174144,
              "semantic_passes": 2,
              "tokens_per_s": 96.55443499253005,
              "ttft_s": 0.13453628899999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3668466895,
              "format_passes": 0,
              "gpu_energy_j": 350.9198959322555,
              "semantic_passes": 0,
              "tokens_per_s": 97.02774692678442,
              "ttft_s": 0.057454311999999993
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.207175874,
              "format_passes": 2,
              "gpu_energy_j": 44.66853467898097,
              "semantic_passes": 2,
              "tokens_per_s": 93.69773565205884,
              "ttft_s": 0.06832195299999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2304910475,
              "format_passes": 0,
              "gpu_energy_j": 54.829892463845894,
              "semantic_passes": 0,
              "tokens_per_s": 94.01254794639209,
              "ttft_s": 0.13471572050000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1578094225,
              "format_passes": 2,
              "gpu_energy_j": 32.790957938742025,
              "semantic_passes": 2,
              "tokens_per_s": 93.62847917884139,
              "ttft_s": 0.061636192500000006
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.307272482,
              "format_passes": 0,
              "gpu_energy_j": 71.24150467069052,
              "semantic_passes": 0,
              "tokens_per_s": 95.93324603176971,
              "ttft_s": 0.077914489
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3987557805,
              "format_passes": 0,
              "gpu_energy_j": 94.13038498063901,
              "semantic_passes": 2,
              "tokens_per_s": 96.25472731006752,
              "ttft_s": 0.1078287705
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0336890415000002,
              "format_passes": 2,
              "gpu_energy_j": 273.07086830892035,
              "semantic_passes": 2,
              "tokens_per_s": 92.23858623681193,
              "ttft_s": 0.870976354
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148895152,
              "format_passes": 0,
              "gpu_energy_j": 32.20304495334048,
              "semantic_passes": 0,
              "tokens_per_s": 93.7043279222948,
              "ttft_s": 0.0634697875
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.204886182,
              "format_passes": 0,
              "gpu_energy_j": 50.83437755855745,
              "semantic_passes": 0,
              "tokens_per_s": 2478.3074360953333,
              "ttft_s": 0.204711534
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7518367625,
              "format_passes": 0,
              "gpu_energy_j": 198.53341229666387,
              "semantic_passes": 0,
              "tokens_per_s": 2728.730360565549,
              "ttft_s": 0.751605851
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4931248165,
              "format_passes": 0,
              "gpu_energy_j": 403.2543790567392,
              "semantic_passes": 0,
              "tokens_per_s": 2746.470542662081,
              "ttft_s": 1.4927911539999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.256077863,
              "format_passes": 2,
              "gpu_energy_j": 56.48610860605431,
              "semantic_passes": 2,
              "tokens_per_s": 94.82150670676816,
              "ttft_s": 0.076757222
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354197984,
              "format_passes": 0,
              "gpu_energy_j": 83.85759370394203,
              "semantic_passes": 2,
              "tokens_per_s": 95.63192896705128,
              "ttft_s": 0.07182522599999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3165573285,
              "format_passes": 0,
              "gpu_energy_j": 75.54726205581815,
              "semantic_passes": 0,
              "tokens_per_s": 95.0546013505074,
              "ttft_s": 0.07454408700000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5497258309999999,
              "format_passes": 0,
              "gpu_energy_j": 135.49752939472157,
              "semantic_passes": 0,
              "tokens_per_s": 96.16925807765853,
              "ttft_s": 0.302580147
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.523822022,
              "format_passes": 0,
              "gpu_energy_j": 131.50981800881038,
              "semantic_passes": 0,
              "tokens_per_s": 95.87786738097196,
              "ttft_s": 0.2733579715
            }
          }
        }
      }
    },
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
              "e2e_s": 1.7621439250000002,
              "format_passes": 2,
              "gpu_energy_j": 476.0543474988539,
              "semantic_passes": 2,
              "tokens_per_s": 35.4268926223042,
              "ttft_s": 0.5200555739999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7744183355,
              "format_passes": 0,
              "gpu_energy_j": 1054.7646905012903,
              "semantic_passes": 0,
              "tokens_per_s": 35.48910555069617,
              "ttft_s": 0.195900617
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5799409799999999,
              "format_passes": 2,
              "gpu_energy_j": 142.45239132204495,
              "semantic_passes": 2,
              "tokens_per_s": 35.027367947957224,
              "ttft_s": 0.20877469599999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9229597415,
              "format_passes": 0,
              "gpu_energy_j": 241.91720246547817,
              "semantic_passes": 0,
              "tokens_per_s": 35.046173505546356,
              "ttft_s": 0.5234749585
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465574049,
              "format_passes": 2,
              "gpu_energy_j": 107.55720101910828,
              "semantic_passes": 2,
              "tokens_per_s": 34.2622976175297,
              "ttft_s": 0.202869832
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9873103615,
              "format_passes": 0,
              "gpu_energy_j": 260.8056604059663,
              "semantic_passes": 0,
              "tokens_per_s": 35.338366537160155,
              "ttft_s": 0.2232645495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1455100905000002,
              "format_passes": 0,
              "gpu_energy_j": 294.31262423684075,
              "semantic_passes": 2,
              "tokens_per_s": 35.363358549798434,
              "ttft_s": 0.3536959355
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7794833005,
              "format_passes": 2,
              "gpu_energy_j": 1007.8370850490446,
              "semantic_passes": 2,
              "tokens_per_s": 34.41999441649442,
              "ttft_s": 3.1986421515
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5733588519999999,
              "format_passes": 2,
              "gpu_energy_j": 142.53369483701235,
              "semantic_passes": 2,
              "tokens_per_s": 35.03081071390858,
              "ttft_s": 0.2021579745
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.722186714,
              "format_passes": 0,
              "gpu_energy_j": 186.74106860139545,
              "semantic_passes": 0,
              "tokens_per_s": 700.3046250344378,
              "ttft_s": 0.721980282
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.736773177,
              "format_passes": 0,
              "gpu_energy_j": 732.3103252796329,
              "semantic_passes": 0,
              "tokens_per_s": 748.6666678011356,
              "ttft_s": 2.7365038655
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4347152325,
              "format_passes": 0,
              "gpu_energy_j": 1471.3419135843621,
              "semantic_passes": 0,
              "tokens_per_s": 753.9037151402888,
              "ttft_s": 5.434407209
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8480947155,
              "format_passes": 0,
              "gpu_energy_j": 220.7743285606533,
              "semantic_passes": 2,
              "tokens_per_s": 35.24650648788017,
              "ttft_s": 0.2238373645
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9841275055,
              "format_passes": 0,
              "gpu_energy_j": 256.5306638297256,
              "semantic_passes": 2,
              "tokens_per_s": 35.15005014672565,
              "ttft_s": 0.2159945565
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0136539765,
              "format_passes": 0,
              "gpu_energy_j": 269.4860494676492,
              "semantic_passes": 2,
              "tokens_per_s": 35.34781191606497,
              "ttft_s": 0.2214679695
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.702987203,
              "format_passes": 0,
              "gpu_energy_j": 456.32979857236796,
              "semantic_passes": 0,
              "tokens_per_s": 35.08848584356434,
              "ttft_s": 1.0267688345
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7737970485,
              "format_passes": 0,
              "gpu_energy_j": 463.47202489277686,
              "semantic_passes": 0,
              "tokens_per_s": 35.14679370701363,
              "ttft_s": 1.0909077795
            }
          }
        }
      }
    }
  }
}
```

</details>
