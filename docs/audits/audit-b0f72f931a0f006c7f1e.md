# Public audit excerpt

Original SHA256: `b0f72f931a0f006c7f1ee3bd35cba37b02d10e789548d5769cfc0fcba3a70203`

Original file: `RESULTS.json`; 41600 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6233029915,
              "format_passes": 2,
              "gpu_energy_j": 162.84707356627894,
              "semantic_passes": 2,
              "tokens_per_s": 76.20636721684838,
              "ttft_s": 0.1246253165
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7252286905,
              "format_passes": 0,
              "gpu_energy_j": 452.6055633246499,
              "semantic_passes": 0,
              "tokens_per_s": 76.4323218069963,
              "ttft_s": 0.0636702535
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24513505400000002,
              "format_passes": 2,
              "gpu_energy_j": 55.529719844460175,
              "semantic_passes": 2,
              "tokens_per_s": 75.13409739354611,
              "ttft_s": 0.072088435
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2466519025,
              "format_passes": 0,
              "gpu_energy_j": 60.84458385549985,
              "semantic_passes": 0,
              "tokens_per_s": 74.69865896969768,
              "ttft_s": 0.126156611
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.187606887,
              "format_passes": 2,
              "gpu_energy_j": 40.743843106055465,
              "semantic_passes": 2,
              "tokens_per_s": 74.5721670628201,
              "ttft_s": 0.06692495700000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369543171,
              "format_passes": 0,
              "gpu_energy_j": 89.67279824214742,
              "semantic_passes": 0,
              "tokens_per_s": 75.7954050415276,
              "ttft_s": 0.079248656
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.484560765,
              "format_passes": 0,
              "gpu_energy_j": 118.06557280781445,
              "semantic_passes": 2,
              "tokens_per_s": 75.96692021387427,
              "ttft_s": 0.1159574615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.090648791,
              "format_passes": 2,
              "gpu_energy_j": 288.0287063237918,
              "semantic_passes": 2,
              "tokens_per_s": 74.9275696908133,
              "ttft_s": 0.8236248095
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24065626699999998,
              "format_passes": 0,
              "gpu_energy_j": 56.427049339187995,
              "semantic_passes": 0,
              "tokens_per_s": 75.35972146097862,
              "ttft_s": 0.068072359
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19965435999999998,
              "format_passes": 0,
              "gpu_energy_j": 48.81693822074496,
              "semantic_passes": 0,
              "tokens_per_s": 2542.7113869649747,
              "ttft_s": 0.199487596
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7174954259999999,
              "format_passes": 0,
              "gpu_energy_j": 190.3396750080874,
              "semantic_passes": 0,
              "tokens_per_s": 2859.308912399682,
              "ttft_s": 0.7172388285
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4155416785,
              "format_passes": 0,
              "gpu_energy_j": 383.7408459169351,
              "semantic_passes": 0,
              "tokens_per_s": 2897.0807962578483,
              "ttft_s": 1.4152072565
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.304561792,
              "format_passes": 2,
              "gpu_energy_j": 73.30519460096139,
              "semantic_passes": 2,
              "tokens_per_s": 75.56856757708834,
              "ttft_s": 0.0795431325
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3645461785,
              "format_passes": 2,
              "gpu_energy_j": 88.02170325111045,
              "semantic_passes": 2,
              "tokens_per_s": 75.77794771827179,
              "ttft_s": 0.07414865749999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.381336524,
              "format_passes": 2,
              "gpu_energy_j": 94.99199403575793,
              "semantic_passes": 2,
              "tokens_per_s": 75.81665920849446,
              "ttft_s": 0.077977864
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6376985415,
              "format_passes": 0,
              "gpu_energy_j": 160.17403269789673,
              "semantic_passes": 0,
              "tokens_per_s": 75.84948160998154,
              "ttft_s": 0.3240029035
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5731458524999999,
              "format_passes": 0,
              "gpu_energy_j": 143.83788110314555,
              "semantic_passes": 0,
              "tokens_per_s": 75.73522357887273,
              "ttft_s": 0.25636724050000004
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
              "e2e_s": 0.6239514115,
              "format_passes": 2,
              "gpu_energy_j": 161.43945653660077,
              "semantic_passes": 2,
              "tokens_per_s": 76.06427431186967,
              "ttft_s": 0.1243716685
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7244320210000001,
              "format_passes": 0,
              "gpu_energy_j": 455.9125506907212,
              "semantic_passes": 0,
              "tokens_per_s": 76.48055351815339,
              "ttft_s": 0.0639420795
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24533073900000002,
              "format_passes": 2,
              "gpu_energy_j": 57.47524996438676,
              "semantic_passes": 2,
              "tokens_per_s": 75.15332180243524,
              "ttft_s": 0.072335082
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.246785642,
              "format_passes": 0,
              "gpu_energy_j": 58.878171533589935,
              "semantic_passes": 0,
              "tokens_per_s": 74.6145017210501,
              "ttft_s": 0.126147932
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18796562449999998,
              "format_passes": 2,
              "gpu_energy_j": 42.866860320358924,
              "semantic_passes": 2,
              "tokens_per_s": 74.31298996479279,
              "ttft_s": 0.0668548625
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3704223555,
              "format_passes": 0,
              "gpu_energy_j": 90.89738545980214,
              "semantic_passes": 0,
              "tokens_per_s": 75.65207351510558,
              "ttft_s": 0.07963676750000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4850733585,
              "format_passes": 0,
              "gpu_energy_j": 120.1146409979886,
              "semantic_passes": 2,
              "tokens_per_s": 75.89026583244886,
              "ttft_s": 0.11610118150000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9562107425,
              "format_passes": 2,
              "gpu_energy_j": 242.8626655901886,
              "semantic_passes": 2,
              "tokens_per_s": 73.69224832219706,
              "ttft_s": 0.6847874075
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2413341215,
              "format_passes": 0,
              "gpu_energy_j": 55.500912085501014,
              "semantic_passes": 0,
              "tokens_per_s": 75.16733465628216,
              "ttft_s": 0.068361314
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20009063049999998,
              "format_passes": 0,
              "gpu_energy_j": 47.7064891747405,
              "semantic_passes": 0,
              "tokens_per_s": 2537.600583420503,
              "ttft_s": 0.1999389965
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5720111855,
              "format_passes": 0,
              "gpu_energy_j": 146.53037786437176,
              "semantic_passes": 0,
              "tokens_per_s": 3588.323991550498,
              "ttft_s": 0.571775071
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1451941749999999,
              "format_passes": 0,
              "gpu_energy_j": 295.08412253148595,
              "semantic_passes": 0,
              "tokens_per_s": 3582.1621285882984,
              "ttft_s": 1.144891963
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.304509488,
              "format_passes": 2,
              "gpu_energy_j": 74.96479903536485,
              "semantic_passes": 2,
              "tokens_per_s": 75.64283501479636,
              "ttft_s": 0.0797593995
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36533854450000003,
              "format_passes": 2,
              "gpu_energy_j": 89.60112291460177,
              "semantic_passes": 2,
              "tokens_per_s": 75.7053313243708,
              "ttft_s": 0.07467201400000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.38175218850000003,
              "format_passes": 2,
              "gpu_energy_j": 93.60911895338322,
              "semantic_passes": 2,
              "tokens_per_s": 75.8700416936021,
              "ttft_s": 0.07859350949999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6381352,
              "format_passes": 0,
              "gpu_energy_j": 160.8727090679955,
              "semantic_passes": 0,
              "tokens_per_s": 75.78541409351772,
              "ttft_s": 0.324002942
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5727421749999999,
              "format_passes": 0,
              "gpu_energy_j": 145.31790936924466,
              "semantic_passes": 0,
              "tokens_per_s": 75.77683091990966,
              "ttft_s": 0.255982539
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
            "e2e_change_pct": 0.10402966275511183,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8643796900072998,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18645804828142376,
            "ttft_change_pct": -0.20352847007614194
          },
          "decode": {
            "e2e_change_pct": -0.04617761716964042,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7306554832820833,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06310381526664077,
            "ttft_change_pct": 0.4269277803330862
          },
          "energy": {
            "e2e_change_pct": 0.079827424436818,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5035835321626907,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02558679688189347,
            "ttft_change_pct": 0.3421450333884968
          },
          "filtering": {
            "e2e_change_pct": 0.054221961657074935,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.2318609107097496,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11266232862588987,
            "ttft_change_pct": -0.00687954434668292
          },
          "german": {
            "e2e_change_pct": 0.19121766036231946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.21064546802148,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3475520535818344,
            "ttft_change_pct": -0.10473596568766341
          },
          "ha_sim": {
            "e2e_change_pct": 0.2379111749300833,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3656172681796974,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1891031868534565,
            "ttft_change_pct": 0.48973890484655946
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.10578518465067521,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7355340269340047,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10090494811373363,
            "ttft_change_pct": 0.12394200264551625
          },
          "long_context": {
            "e2e_change_pct": -12.326428966811187,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -15.681090024002376,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.6486873572888583,
            "ttft_change_pct": -16.856874683544852
          },
          "math": {
            "e2e_change_pct": 0.28166916592287095,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.641300164607029,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2552912895200543,
            "ttft_change_pct": 0.424482130845516
          },
          "prefill": {
            "e2e_change_pct": 0.21851288396608215,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2747207966692384,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2009981774051095,
            "ttft_change_pct": 0.2262799838442131
          },
          "prefill2048": {
            "e2e_change_pct": -20.2766784606652,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -23.016376980707886,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 25.496198609019416,
            "ttft_change_pct": -20.281076779434283
          },
          "prefill4096": {
            "e2e_change_pct": -19.098519500074197,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -23.10328033326946,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 23.64729810833608,
            "ttft_change_pct": -19.10075660356112
          },
          "pve_sim": {
            "e2e_change_pct": -0.017173526480962487,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.263965662239298,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09827821287238248,
            "ttft_change_pct": 0.27188645103961573
          },
          "sorting": {
            "e2e_change_pct": 0.21735682520671595,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7943525348350864,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09582787088793232,
            "ttft_change_pct": 0.7058206010001067
          },
          "time": {
            "e2e_change_pct": 0.10900201628734063,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4557806648991423,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07040996749916317,
            "ttft_change_pct": 0.7895131623507856
          },
          "tool-call": {
            "e2e_change_pct": 0.06847412555983645,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4361982765436867,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08446665040278134,
            "ttft_change_pct": 1.1882609562974267e-05
          },
          "tool-final": {
            "e2e_change_pct": -0.07043189761196667,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0289558319048098,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.054937899527818246,
            "ttft_change_pct": -0.1500587591650726
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 372109212199751,
          "end_ns": 372110023939369,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 372154067710487,
          "end_ns": 372154725521008,
          "model": "omnicoder2",
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
