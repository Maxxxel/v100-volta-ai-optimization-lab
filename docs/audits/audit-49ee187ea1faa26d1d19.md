# Public audit excerpt

Original SHA256: `49ee187ea1faa26d1d19bb015f1ee6b42c32b7a7e72f391e605edc5ba99dd5cf`

Original file: `RESULTS.json`; 42811 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7644855289999999,
              "format_passes": 2,
              "gpu_energy_j": 478.10730122386263,
              "semantic_passes": 2,
              "tokens_per_s": 35.34194626656378,
              "ttft_s": 0.5194602269999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7884795655000003,
              "format_passes": 0,
              "gpu_energy_j": 1071.9979292596604,
              "semantic_passes": 0,
              "tokens_per_s": 35.34021542177231,
              "ttft_s": 0.1947686395
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.583173217,
              "format_passes": 2,
              "gpu_energy_j": 147.70610963834713,
              "semantic_passes": 2,
              "tokens_per_s": 34.924127005955036,
              "ttft_s": 0.210947202
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9260470945,
              "format_passes": 0,
              "gpu_energy_j": 244.61029316808646,
              "semantic_passes": 0,
              "tokens_per_s": 34.92894954736799,
              "ttft_s": 0.525198834
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4653547715,
              "format_passes": 2,
              "gpu_energy_j": 107.750072331072,
              "semantic_passes": 2,
              "tokens_per_s": 34.21930380296913,
              "ttft_s": 0.2023176985
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9910160325,
              "format_passes": 0,
              "gpu_energy_j": 264.43771125762055,
              "semantic_passes": 0,
              "tokens_per_s": 35.313529116327544,
              "ttft_s": 0.22634515300000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1470668050000001,
              "format_passes": 0,
              "gpu_energy_j": 294.1348804524471,
              "semantic_passes": 2,
              "tokens_per_s": 35.2944448035093,
              "ttft_s": 0.3536970145
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7974394365,
              "format_passes": 2,
              "gpu_energy_j": 1017.5053788555631,
              "semantic_passes": 2,
              "tokens_per_s": 34.41283391834867,
              "ttft_s": 3.216206349
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.572629551,
              "format_passes": 2,
              "gpu_energy_j": 142.09268321873813,
              "semantic_passes": 2,
              "tokens_per_s": 35.05460581192778,
              "ttft_s": 0.20176563250000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7265717389999999,
              "format_passes": 0,
              "gpu_energy_j": 187.25269110913143,
              "semantic_passes": 0,
              "tokens_per_s": 696.1066964290592,
              "ttft_s": 0.7264164325
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7501072425,
              "format_passes": 0,
              "gpu_energy_j": 732.4826043000817,
              "semantic_passes": 0,
              "tokens_per_s": 745.0343711306741,
              "ttft_s": 2.749869588
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.474481023499999,
              "format_passes": 0,
              "gpu_energy_j": 1477.290522631818,
              "semantic_passes": 0,
              "tokens_per_s": 748.4375891060877,
              "ttft_s": 5.4741236465
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8471996935,
              "format_passes": 0,
              "gpu_energy_j": 222.55426431507408,
              "semantic_passes": 2,
              "tokens_per_s": 35.18959558506858,
              "ttft_s": 0.2219700845
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9871350395,
              "format_passes": 0,
              "gpu_energy_j": 262.9120832032283,
              "semantic_passes": 2,
              "tokens_per_s": 34.99733181548294,
              "ttft_s": 0.2155892685
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.016674599,
              "format_passes": 0,
              "gpu_energy_j": 271.1440534772395,
              "semantic_passes": 2,
              "tokens_per_s": 35.19564691988334,
              "ttft_s": 0.2210512835
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7072538874999998,
              "format_passes": 0,
              "gpu_energy_j": 458.06048968278435,
              "semantic_passes": 0,
              "tokens_per_s": 35.022986260897284,
              "ttft_s": 1.0290632445
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779832929,
              "format_passes": 0,
              "gpu_energy_j": 466.33977721483495,
              "semantic_passes": 0,
              "tokens_per_s": 35.075097034786346,
              "ttft_s": 1.0955021145
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
              "e2e_s": 1.764604534,
              "format_passes": 2,
              "gpu_energy_j": 484.53585351069546,
              "semantic_passes": 2,
              "tokens_per_s": 35.366551101589025,
              "ttft_s": 0.520500374
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7889827635,
              "format_passes": 0,
              "gpu_energy_j": 1068.2389908959774,
              "semantic_passes": 0,
              "tokens_per_s": 35.332086905647614,
              "ttft_s": 0.19418176199999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581278353,
              "format_passes": 2,
              "gpu_energy_j": 149.61972795596984,
              "semantic_passes": 2,
              "tokens_per_s": 34.939770312313144,
              "ttft_s": 0.209192245
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9248590624999999,
              "format_passes": 0,
              "gpu_energy_j": 247.65510267360975,
              "semantic_passes": 0,
              "tokens_per_s": 34.911422951933886,
              "ttft_s": 0.5238153569999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465900831,
              "format_passes": 2,
              "gpu_energy_j": 112.66375292969602,
              "semantic_passes": 2,
              "tokens_per_s": 34.229890933217746,
              "ttft_s": 0.2029517425
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989735158,
              "format_passes": 0,
              "gpu_energy_j": 270.63587599357163,
              "semantic_passes": 0,
              "tokens_per_s": 35.28628579734685,
              "ttft_s": 0.224515404
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1439016894999998,
              "format_passes": 0,
              "gpu_energy_j": 302.67181945602204,
              "semantic_passes": 2,
              "tokens_per_s": 35.28235361669264,
              "ttft_s": 0.35026559599999996
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8032878195,
              "format_passes": 2,
              "gpu_energy_j": 1017.8154423142496,
              "semantic_passes": 2,
              "tokens_per_s": 34.29720282892592,
              "ttft_s": 3.2200894425
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5775053265,
              "format_passes": 2,
              "gpu_energy_j": 143.6041341130617,
              "semantic_passes": 2,
              "tokens_per_s": 34.664980995697725,
              "ttft_s": 0.2024305755
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7249476244999999,
              "format_passes": 0,
              "gpu_energy_j": 188.242764130772,
              "semantic_passes": 0,
              "tokens_per_s": 697.5990995077793,
              "ttft_s": 0.7247791889999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.75545445,
              "format_passes": 0,
              "gpu_energy_j": 740.1998612675059,
              "semantic_passes": 0,
              "tokens_per_s": 743.5772059976496,
              "ttft_s": 2.7552284384999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4709212415,
              "format_passes": 0,
              "gpu_energy_j": 1476.184590460491,
              "semantic_passes": 0,
              "tokens_per_s": 748.923312138773,
              "ttft_s": 5.470592797
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8471660535000001,
              "format_passes": 0,
              "gpu_energy_j": 232.4683988819973,
              "semantic_passes": 2,
              "tokens_per_s": 35.21506362875782,
              "ttft_s": 0.22240959500000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.987775898,
              "format_passes": 0,
              "gpu_energy_j": 259.24150337978074,
              "semantic_passes": 2,
              "tokens_per_s": 35.027771501515076,
              "ttft_s": 0.21695182899999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0161016305000001,
              "format_passes": 0,
              "gpu_energy_j": 272.8459684359263,
              "semantic_passes": 2,
              "tokens_per_s": 35.22748188359112,
              "ttft_s": 0.221296411
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.70855843,
              "format_passes": 0,
              "gpu_energy_j": 459.94368001028283,
              "semantic_passes": 0,
              "tokens_per_s": 34.9655907862262,
              "ttft_s": 1.0295843105
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.781193918,
              "format_passes": 0,
              "gpu_energy_j": 467.7748104638236,
              "semantic_passes": 0,
              "tokens_per_s": 35.04281732177991,
              "ttft_s": 1.095611935
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.006744458826335453,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3445835841404241,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06961935497173943,
            "ttft_change_pct": 0.20023611932855623
          },
          "decode": {
            "e2e_change_pct": 0.01328232055366474,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.35064791275100093,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.023000754318225347,
            "ttft_change_pct": -0.3013203262633213
          },
          "energy": {
            "e2e_change_pct": -0.32492301511165556,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2955579984525567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04479226168041528,
            "ttft_change_pct": -0.8319413499497386
          },
          "filtering": {
            "e2e_change_pct": -0.1282906676189577,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2447593541907942,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.050177848636234756,
            "ttft_change_pct": -0.26341966326606236
          },
          "german": {
            "e2e_change_pct": 0.11734262404570206,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.560257355119246,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.030939057993628616,
            "ttft_change_pct": 0.31339027910106676
          },
          "ha_sim": {
            "e2e_change_pct": -0.12924861535981158,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.343903487317922,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0771469735889374,
            "ttft_change_pct": -0.8083888591155386
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.27593122616780263,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.902389199962685,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03425804509455954,
            "ttft_change_pct": -0.9701576092890796
          },
          "long_context": {
            "e2e_change_pct": 0.15400859178389403,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.030472906102496644,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.33601152900428755,
            "ttft_change_pct": 0.1207352103265169
          },
          "math": {
            "e2e_change_pct": 0.8514711634223682,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0637077575604836,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.111479667808668,
            "ttft_change_pct": 0.3295620724703907
          },
          "prefill": {
            "e2e_change_pct": -0.22353119627737117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5287363379272048,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21439286338946761,
            "ttft_change_pct": -0.22538635233861903
          },
          "prefill2048": {
            "e2e_change_pct": 0.19443632660445243,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0535754599658276,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19558361190948892,
            "ttft_change_pct": 0.19487653245029435
          },
          "prefill4096": {
            "e2e_change_pct": -0.06502501305087893,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.07486219903155567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0648982680393484,
            "ttft_change_pct": -0.06450072610721946
          },
          "pve_sim": {
            "e2e_change_pct": -0.003970728537561197,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.454704382966845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07237378908679926,
            "ttft_change_pct": 0.19800438468546844
          },
          "sorting": {
            "e2e_change_pct": 0.06492105683175708,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3961244301617826,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08697716212375806,
            "ttft_change_pct": 0.6320168482783162
          },
          "time": {
            "e2e_change_pct": -0.05635711766216467,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6276792490415684,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09045142366681524,
            "ttft_change_pct": 0.1108916881724431
          },
          "tool-call": {
            "e2e_change_pct": 0.07641174576036303,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.41112262897911034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16387944261384568,
            "ttft_change_pct": 0.05063498310573511
          },
          "tool-final": {
            "e2e_change_pct": 0.0764672334029104,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.30772267756338234,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.092030288538969,
            "ttft_change_pct": 0.010024672572184201
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 354273832231220,
          "end_ns": 354274389147603,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 354375498728418,
          "end_ns": 354375753043261,
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
