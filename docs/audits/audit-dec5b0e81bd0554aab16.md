# Public audit excerpt

Original SHA256: `dec5b0e81bd0554aab16de0f913da983a9a5c869c90cf381109835a448d0a2a1`

Original file: `RESULTS.json`; 41292 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5372964305,
              "format_passes": 2,
              "gpu_energy_j": 133.53135443078025,
              "semantic_passes": 2,
              "tokens_per_s": 93.8309478435627,
              "ttft_s": 0.1322633695
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.40394272,
              "format_passes": 0,
              "gpu_energy_j": 356.21506001414247,
              "semantic_passes": 0,
              "tokens_per_s": 94.3847046742797,
              "ttft_s": 0.058033148
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2089122645,
              "format_passes": 2,
              "gpu_energy_j": 46.715078319552205,
              "semantic_passes": 2,
              "tokens_per_s": 92.48259663064849,
              "ttft_s": 0.068339461
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2323297045,
              "format_passes": 0,
              "gpu_energy_j": 54.60448019749184,
              "semantic_passes": 0,
              "tokens_per_s": 91.33069498234185,
              "ttft_s": 0.133751299
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.16051239150000002,
              "format_passes": 2,
              "gpu_energy_j": 34.13096477604668,
              "semantic_passes": 2,
              "tokens_per_s": 91.10961452635806,
              "ttft_s": 0.061700794
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3152107585,
              "format_passes": 0,
              "gpu_energy_j": 74.51562863234659,
              "semantic_passes": 0,
              "tokens_per_s": 92.61246873570393,
              "ttft_s": 0.077609031
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4062563515,
              "format_passes": 0,
              "gpu_energy_j": 92.91418656147066,
              "semantic_passes": 2,
              "tokens_per_s": 93.62532538549083,
              "ttft_s": 0.10712988949999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.034479536,
              "format_passes": 2,
              "gpu_energy_j": 270.7855373659103,
              "semantic_passes": 2,
              "tokens_per_s": 91.28347923196814,
              "ttft_s": 0.8701003279999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1512577815,
              "format_passes": 0,
              "gpu_energy_j": 30.297932010203798,
              "semantic_passes": 0,
              "tokens_per_s": 91.02858024185221,
              "ttft_s": 0.0633126505
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20599696950000002,
              "format_passes": 0,
              "gpu_energy_j": 50.53757613906522,
              "semantic_passes": 0,
              "tokens_per_s": 2464.1123494879234,
              "ttft_s": 0.2058485205
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7542149225,
              "format_passes": 0,
              "gpu_energy_j": 199.53848060759304,
              "semantic_passes": 0,
              "tokens_per_s": 2719.961039213992,
              "ttft_s": 0.753957189
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4968222945,
              "format_passes": 0,
              "gpu_energy_j": 405.3905910300398,
              "semantic_passes": 0,
              "tokens_per_s": 2739.5506960863686,
              "ttft_s": 1.496498616
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.260516391,
              "format_passes": 2,
              "gpu_energy_j": 57.61597431907484,
              "semantic_passes": 2,
              "tokens_per_s": 92.96435615764743,
              "ttft_s": 0.0776471275
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3070710645,
              "format_passes": 2,
              "gpu_energy_j": 69.10886844370211,
              "semantic_passes": 2,
              "tokens_per_s": 92.90708953053179,
              "ttft_s": 0.0702290475
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3226866395,
              "format_passes": 0,
              "gpu_energy_j": 76.13479643140334,
              "semantic_passes": 0,
              "tokens_per_s": 93.04994692213172,
              "ttft_s": 0.075476629
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560596613,
              "format_passes": 0,
              "gpu_energy_j": 136.91498310491113,
              "semantic_passes": 0,
              "tokens_per_s": 93.44603497552984,
              "ttft_s": 0.3059755915
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.53156448,
              "format_passes": 0,
              "gpu_energy_j": 130.82046629241938,
              "semantic_passes": 0,
              "tokens_per_s": 93.20050849936896,
              "ttft_s": 0.274363323
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5387667585,
              "format_passes": 2,
              "gpu_energy_j": 132.93417889917438,
              "semantic_passes": 2,
              "tokens_per_s": 93.51782841571462,
              "ttft_s": 0.132418378
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4071919965,
              "format_passes": 0,
              "gpu_energy_j": 354.5996145842501,
              "semantic_passes": 0,
              "tokens_per_s": 94.15504978486496,
              "ttft_s": 0.058184379999999994
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2092622555,
              "format_passes": 2,
              "gpu_energy_j": 47.14637211958502,
              "semantic_passes": 2,
              "tokens_per_s": 92.09003233007368,
              "ttft_s": 0.0680772165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23338349349999998,
              "format_passes": 0,
              "gpu_energy_j": 56.00141387554401,
              "semantic_passes": 0,
              "tokens_per_s": 91.23674150304961,
              "ttft_s": 0.134766614
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15996370599999998,
              "format_passes": 2,
              "gpu_energy_j": 32.86369876344413,
              "semantic_passes": 2,
              "tokens_per_s": 91.33037287946357,
              "ttft_s": 0.061439871
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31396507399999996,
              "format_passes": 0,
              "gpu_energy_j": 73.30141902086683,
              "semantic_passes": 0,
              "tokens_per_s": 93.03720901318474,
              "ttft_s": 0.07748716050000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.407666808,
              "format_passes": 0,
              "gpu_energy_j": 94.1859055300786,
              "semantic_passes": 2,
              "tokens_per_s": 93.51430016348783,
              "ttft_s": 0.108224741
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.86630932,
              "format_passes": 2,
              "gpu_energy_j": 227.03699897001076,
              "semantic_passes": 2,
              "tokens_per_s": 89.52724826363283,
              "ttft_s": 0.6987141845
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15160023350000001,
              "format_passes": 0,
              "gpu_energy_j": 31.333654993156017,
              "semantic_passes": 0,
              "tokens_per_s": 90.87734484191728,
              "ttft_s": 0.063560882
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20882764,
              "format_passes": 0,
              "gpu_energy_j": 49.37522034799343,
              "semantic_passes": 0,
              "tokens_per_s": 2431.1706135808204,
              "ttft_s": 0.208691398
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5714433665,
              "format_passes": 0,
              "gpu_energy_j": 151.95403701016065,
              "semantic_passes": 0,
              "tokens_per_s": 3591.571153513809,
              "ttft_s": 0.5712469965
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1515711105,
              "format_passes": 0,
              "gpu_energy_j": 302.1324916930125,
              "semantic_passes": 0,
              "tokens_per_s": 3562.3155243855617,
              "ttft_s": 1.151184898
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2598958485,
              "format_passes": 2,
              "gpu_energy_j": 57.84901194689108,
              "semantic_passes": 2,
              "tokens_per_s": 92.91892121639374,
              "ttft_s": 0.076908664
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3069599065,
              "format_passes": 2,
              "gpu_energy_j": 71.12343303425533,
              "semantic_passes": 2,
              "tokens_per_s": 92.99657010054571,
              "ttft_s": 0.070360408
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3230281055,
              "format_passes": 0,
              "gpu_energy_j": 75.70405944028036,
              "semantic_passes": 0,
              "tokens_per_s": 92.82145240738346,
              "ttft_s": 0.075227643
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561517234,
              "format_passes": 0,
              "gpu_energy_j": 137.34276185767845,
              "semantic_passes": 0,
              "tokens_per_s": 93.1922025737893,
              "ttft_s": 0.3066912095
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5331005345,
              "format_passes": 0,
              "gpu_energy_j": 133.48876861931353,
              "semantic_passes": 0,
              "tokens_per_s": 93.07286478711123,
              "ttft_s": 0.27470791699999997
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
            "e2e_change_pct": 0.2736530370454515,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.44721746001268325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3337059201087067,
            "ttft_change_pct": 0.11719684791486884
          },
          "decode": {
            "e2e_change_pct": 0.2314393923421587,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.45350284455357714,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.24331790856080282,
            "ttft_change_pct": 0.2605958925405716
          },
          "energy": {
            "e2e_change_pct": 0.16753013559909213,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9232432344061792,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4244737008656907,
            "ttft_change_pct": -0.3837380280186986
          },
          "filtering": {
            "e2e_change_pct": 0.4535748032167719,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5582766707050064,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10287174460941184,
            "ttft_change_pct": 0.7591066461343443
          },
          "german": {
            "e2e_change_pct": -0.34183373312959286,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.712951042895596,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.24229973340699207,
            "ttft_change_pct": -0.42288434732299374
          },
          "ha_sim": {
            "e2e_change_pct": -0.39519098457423407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.629469728384847,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.45862105100871187,
            "ttft_change_pct": -0.15703133827297266
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.34718386427492476,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3687026875778496,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11858460469521548,
            "ttft_change_pct": 1.0219850922183582
          },
          "long_context": {
            "e2e_change_pct": -16.256504855597264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -16.156157681635143,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.923930795705553,
            "ttft_change_pct": -19.69728524226001
          },
          "math": {
            "e2e_change_pct": 0.2264028974932497,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4184609781400477,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1661405676471217,
            "ttft_change_pct": 0.3920725132175562
          },
          "prefill": {
            "e2e_change_pct": 1.3741321082881175,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2999832597299874,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.336860144138674,
            "ttft_change_pct": 1.3810531613706711
          },
          "prefill2048": {
            "e2e_change_pct": -24.2333518666226,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -23.847251644163148,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 32.044948502339295,
            "ttft_change_pct": -24.23349696318102
          },
          "prefill4096": {
            "e2e_change_pct": -23.065609409253764,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -25.47126194386089,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 30.032838212286705,
            "ttft_change_pct": -23.07477696992405
          },
          "pve_sim": {
            "e2e_change_pct": -0.23819710445781572,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.40446704333365613,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04887350715002681,
            "ttft_change_pct": -0.9510506360972504
          },
          "sorting": {
            "e2e_change_pct": -0.03619943812712689,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9150594358151594,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09631188584862116,
            "ttft_change_pct": 0.1870458231688188
          },
          "time": {
            "e2e_change_pct": 0.10581968950715837,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5657557533644608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2455611446393169,
            "ttft_change_pct": -0.32988489721765824
          },
          "tool-call": {
            "e2e_change_pct": 0.16422164862419653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31244115367530245,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.27163528319528174,
            "ttft_change_pct": 0.2338807473144522
          },
          "tool-final": {
            "e2e_change_pct": 0.28896861204870117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0396673414462274,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13695602557640685,
            "ttft_change_pct": 0.12559769149609323
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 372547544077024,
          "end_ns": 372548253657530,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 372588095763768,
          "end_ns": 372588754521931,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
