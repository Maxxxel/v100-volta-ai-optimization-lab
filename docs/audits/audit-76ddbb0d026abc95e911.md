# Public audit excerpt

Original SHA256: `76ddbb0d026abc95e911532f5beba38d076897590f0e601163df641971e8dedc`

Original file: `RESULTS.json`; 43213 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7757847039999999,
              "format_passes": 2,
              "gpu_energy_j": 483.9689596889872,
              "semantic_passes": 2,
              "tokens_per_s": 35.062002209854484,
              "ttft_s": 0.5207930825
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.819262125,
              "format_passes": 0,
              "gpu_energy_j": 1080.0837256473396,
              "semantic_passes": 0,
              "tokens_per_s": 35.06314066398432,
              "ttft_s": 0.19652522249999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5864011545000001,
              "format_passes": 2,
              "gpu_energy_j": 148.72674880368794,
              "semantic_passes": 2,
              "tokens_per_s": 34.688025301435225,
              "ttft_s": 0.2115692615
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.932103301,
              "format_passes": 0,
              "gpu_energy_j": 247.3397007191794,
              "semantic_passes": 0,
              "tokens_per_s": 34.44213039039744,
              "ttft_s": 0.525508328
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47067667700000004,
              "format_passes": 2,
              "gpu_energy_j": 107.5241565256618,
              "semantic_passes": 2,
              "tokens_per_s": 33.76863611844135,
              "ttft_s": 0.2041561425
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9993314099999999,
              "format_passes": 0,
              "gpu_energy_j": 267.7021495636502,
              "semantic_passes": 0,
              "tokens_per_s": 34.951002175760564,
              "ttft_s": 0.2267522715
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1596180944999999,
              "format_passes": 0,
              "gpu_energy_j": 295.0251887252878,
              "semantic_passes": 2,
              "tokens_per_s": 34.926119198440695,
              "ttft_s": 0.357908125
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.809737924,
              "format_passes": 2,
              "gpu_energy_j": 1031.999939408548,
              "semantic_passes": 2,
              "tokens_per_s": 33.78365708435463,
              "ttft_s": 3.2177059075
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.577272643,
              "format_passes": 2,
              "gpu_energy_j": 146.01114655459526,
              "semantic_passes": 2,
              "tokens_per_s": 34.67188031787945,
              "ttft_s": 0.2023279045
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7283718685,
              "format_passes": 0,
              "gpu_energy_j": 188.79823526614203,
              "semantic_passes": 0,
              "tokens_per_s": 694.2803465021309,
              "ttft_s": 0.728220358
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7473629455,
              "format_passes": 0,
              "gpu_energy_j": 735.3802058173022,
              "semantic_passes": 0,
              "tokens_per_s": 745.7802455247954,
              "ttft_s": 2.747145366
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.480199057,
              "format_passes": 0,
              "gpu_energy_j": 1477.8005424025773,
              "semantic_passes": 0,
              "tokens_per_s": 747.6571274857777,
              "ttft_s": 5.4798672725
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8547898145,
              "format_passes": 0,
              "gpu_energy_j": 226.13336772943086,
              "semantic_passes": 2,
              "tokens_per_s": 34.8961932192989,
              "ttft_s": 0.224310787
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.997333805,
              "format_passes": 0,
              "gpu_energy_j": 257.92251836523786,
              "semantic_passes": 2,
              "tokens_per_s": 34.759393470141916,
              "ttft_s": 0.220502902
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.023547283,
              "format_passes": 0,
              "gpu_energy_j": 277.9226305567687,
              "semantic_passes": 2,
              "tokens_per_s": 34.90828270116235,
              "ttft_s": 0.221453823
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.717704479,
              "format_passes": 0,
              "gpu_energy_j": 463.01659820025213,
              "semantic_passes": 0,
              "tokens_per_s": 34.724195421772805,
              "ttft_s": 1.034072261
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.785928927,
              "format_passes": 0,
              "gpu_energy_j": 469.55977235448427,
              "semantic_passes": 0,
              "tokens_per_s": 34.756274379603795,
              "ttft_s": 1.094940565
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
              "e2e_s": 1.7674068125,
              "format_passes": 2,
              "gpu_energy_j": 486.87937920709294,
              "semantic_passes": 2,
              "tokens_per_s": 35.2797390578517,
              "ttft_s": 0.5202064925
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.785318128,
              "format_passes": 0,
              "gpu_energy_j": 1072.4585061299003,
              "semantic_passes": 0,
              "tokens_per_s": 35.36426315201141,
              "ttft_s": 0.19569326599999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581261802,
              "format_passes": 2,
              "gpu_energy_j": 145.94638719696724,
              "semantic_passes": 2,
              "tokens_per_s": 34.9502485637116,
              "ttft_s": 0.20923626950000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9256325525,
              "format_passes": 0,
              "gpu_energy_j": 248.34016210675924,
              "semantic_passes": 0,
              "tokens_per_s": 34.92713886815301,
              "ttft_s": 0.52476725
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46533715249999996,
              "format_passes": 2,
              "gpu_energy_j": 109.39794677006077,
              "semantic_passes": 2,
              "tokens_per_s": 34.21458222843735,
              "ttft_s": 0.202282058
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9910687595000001,
              "format_passes": 0,
              "gpu_energy_j": 268.47310849821133,
              "semantic_passes": 0,
              "tokens_per_s": 35.23798740418819,
              "ttft_s": 0.2248458325
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1477649460000001,
              "format_passes": 0,
              "gpu_energy_j": 302.9656736469715,
              "semantic_passes": 2,
              "tokens_per_s": 35.23932543987694,
              "ttft_s": 0.3531514225
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8037633925,
              "format_passes": 2,
              "gpu_energy_j": 1029.1562205148307,
              "semantic_passes": 2,
              "tokens_per_s": 34.30691117163589,
              "ttft_s": 3.220718909
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5747094035,
              "format_passes": 2,
              "gpu_energy_j": 143.15467243291667,
              "semantic_passes": 2,
              "tokens_per_s": 34.93696291809954,
              "ttft_s": 0.202575353
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7276496145,
              "format_passes": 0,
              "gpu_energy_j": 189.6887620268277,
              "semantic_passes": 0,
              "tokens_per_s": 694.9914580985945,
              "ttft_s": 0.7275232925
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.753665666,
              "format_passes": 0,
              "gpu_energy_j": 733.3992101496424,
              "semantic_passes": 0,
              "tokens_per_s": 744.0850026255865,
              "ttft_s": 2.7534284675
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4743754235,
              "format_passes": 0,
              "gpu_energy_j": 1471.6367470388814,
              "semantic_passes": 0,
              "tokens_per_s": 748.4513881527403,
              "ttft_s": 5.474017349
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846646703,
              "format_passes": 0,
              "gpu_energy_j": 227.42085354193472,
              "semantic_passes": 2,
              "tokens_per_s": 35.21580612029864,
              "ttft_s": 0.2218613415
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.984567077,
              "format_passes": 0,
              "gpu_energy_j": 263.9700920630703,
              "semantic_passes": 2,
              "tokens_per_s": 35.055257504058105,
              "ttft_s": 0.21432993150000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0156933795,
              "format_passes": 0,
              "gpu_energy_j": 276.7704275454248,
              "semantic_passes": 2,
              "tokens_per_s": 35.216960168008725,
              "ttft_s": 0.220562871
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7073533470000002,
              "format_passes": 0,
              "gpu_energy_j": 462.59919597897465,
              "semantic_passes": 0,
              "tokens_per_s": 35.01874300997332,
              "ttft_s": 1.0289445415
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779200274,
              "format_passes": 0,
              "gpu_energy_j": 467.211188379164,
              "semantic_passes": 0,
              "tokens_per_s": 35.03194668936055,
              "ttft_s": 1.094462557
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.4717853172813369,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.60136491397631,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6210051744735212,
            "ttft_change_pct": -0.1126339845345492
          },
          "decode": {
            "e2e_change_pct": -0.888757982276478,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7059841136731526,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8588006730851472,
            "ttft_change_pct": -0.4233331932749773
          },
          "energy": {
            "e2e_change_pct": -0.8764226435369449,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8694428736492075,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7559475063734,
            "ttft_change_pct": -1.1027083913132563
          },
          "filtering": {
            "e2e_change_pct": -0.6942093749757072,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.40448880008783217,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.4081837338691283,
            "ttft_change_pct": -0.14102117140948334
          },
          "german": {
            "e2e_change_pct": -1.1344357519546433,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7426690940391287,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.3205926008734048,
            "ttft_change_pct": -0.9179662571259684
          },
          "ha_sim": {
            "e2e_change_pct": -0.8268178521477543,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2879913126651257,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8211072946762599,
            "ttft_change_pct": -0.8407585015085428
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.0221596710346725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.691459992277956,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8967679450920363,
            "ttft_change_pct": -1.3290289232746666
          },
          "long_context": {
            "e2e_change_pct": -0.15682263765081084,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2755541725464772,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.54883790696414,
            "ttft_change_pct": 0.09363818778393984
          },
          "math": {
            "e2e_change_pct": -0.44402580497826527,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9563397652045178,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7645463637672822,
            "ttft_change_pct": 0.12230072792556168
          },
          "prefill": {
            "e2e_change_pct": -0.09916006249491849,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4716817185448363,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10242427285265254,
            "ttft_change_pct": -0.09572178151052713
          },
          "prefill2048": {
            "e2e_change_pct": 0.22940982407597676,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.26938387136191677,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.22731131715830744,
            "ttft_change_pct": 0.22871383428642034
          },
          "prefill4096": {
            "e2e_change_pct": -0.10626682424175193,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.41709250922827845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10623327696126506,
            "ttft_change_pct": -0.10675301442713003
          },
          "pve_sim": {
            "e2e_change_pct": -0.9526448913951158,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5693480026549347,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9158961809707655,
            "ttft_change_pct": -1.0919873862330176
          },
          "sorting": {
            "e2e_change_pct": -1.2800857582482172,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3447249725084607,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.851177205293685,
            "ttft_change_pct": -2.7994962624119935
          },
          "time": {
            "e2e_change_pct": -0.7673220016744531,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4145768946687278,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8842527989384452,
            "ttft_change_pct": -0.40231953909416474
          },
          "tool-call": {
            "e2e_change_pct": -0.6026142521341038,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.09014843590919863,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.848248849607125,
            "ttft_change_pct": -0.4958763225155205
          },
          "tool-final": {
            "e2e_change_pct": -0.37675928186587937,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5001672020462644,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7931583999651437,
            "ttft_change_pct": -0.04365606821772339
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 354752782158018,
          "end_ns": 354753288689367,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 354854847645712,
          "end_ns": 354855102276594,
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
