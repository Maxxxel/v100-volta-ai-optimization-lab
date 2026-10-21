# Public audit excerpt

Original SHA256: `dfdff312bec0a06c732f6c8f035c40e67c2c3d13fe20a52729999a47de22d6a7`

Original file: `RESULTS.json`; 47211 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6918471715,
              "format_passes": 2,
              "gpu_energy_j": 179.5669991030739,
              "semantic_passes": 2,
              "tokens_per_s": 79.02758282162745,
              "ttft_s": 0.145651393
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658321472,
              "format_passes": 0,
              "gpu_energy_j": 455.7357978796607,
              "semantic_passes": 0,
              "tokens_per_s": 79.62482656415172,
              "ttft_s": 0.062918721
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25110894699999997,
              "format_passes": 2,
              "gpu_energy_j": 59.31450882278392,
              "semantic_passes": 2,
              "tokens_per_s": 77.68770757750514,
              "ttft_s": 0.0820830905
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2624295035,
              "format_passes": 0,
              "gpu_energy_j": 59.175654688751436,
              "semantic_passes": 0,
              "tokens_per_s": 76.55971937912307,
              "ttft_s": 0.142652163
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2044792225,
              "format_passes": 2,
              "gpu_energy_j": 44.475621637209294,
              "semantic_passes": 2,
              "tokens_per_s": 75.86268452600012,
              "ttft_s": 0.08416791
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.381991489,
              "format_passes": 0,
              "gpu_energy_j": 93.73378975355705,
              "semantic_passes": 0,
              "tokens_per_s": 78.42743444439142,
              "ttft_s": 0.096245185
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4834845955,
              "format_passes": 0,
              "gpu_energy_j": 121.24435780388475,
              "semantic_passes": 2,
              "tokens_per_s": 78.61862723789338,
              "ttft_s": 0.12374564900000001
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20040744900000002,
              "format_passes": 0,
              "gpu_energy_j": 48.76059120269474,
              "semantic_passes": 0,
              "tokens_per_s": 2567.0670942022343,
              "ttft_s": 0.2002163295
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.091835824,
              "format_passes": 2,
              "gpu_energy_j": 291.9414491216818,
              "semantic_passes": 2,
              "tokens_per_s": 77.87693117813211,
              "ttft_s": 0.833636782
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.249857816,
              "format_passes": 0,
              "gpu_energy_j": 55.909604360106314,
              "semantic_passes": 0,
              "tokens_per_s": 78.01182554562291,
              "ttft_s": 0.081431053
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19978843699999999,
              "format_passes": 0,
              "gpu_energy_j": 48.124981687883896,
              "semantic_passes": 0,
              "tokens_per_s": 2541.375229019559,
              "ttft_s": 0.1995940585
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7195329269999999,
              "format_passes": 0,
              "gpu_energy_j": 191.88069440577644,
              "semantic_passes": 0,
              "tokens_per_s": 2853.9682909725675,
              "ttft_s": 0.7188696185000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4191946055,
              "format_passes": 0,
              "gpu_energy_j": 386.30144181536303,
              "semantic_passes": 0,
              "tokens_per_s": 2889.6497467520403,
              "ttft_s": 1.4188628699999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.310782497,
              "format_passes": 2,
              "gpu_energy_j": 74.31406429452613,
              "semantic_passes": 2,
              "tokens_per_s": 78.10712313719654,
              "ttft_s": 0.09152432099999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36398159350000003,
              "format_passes": 2,
              "gpu_energy_j": 87.03671632939658,
              "semantic_passes": 2,
              "tokens_per_s": 78.65836288833464,
              "ttft_s": 0.0822944715
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3871070125,
              "format_passes": 2,
              "gpu_energy_j": 96.32321939828329,
              "semantic_passes": 2,
              "tokens_per_s": 77.64235116624783,
              "ttft_s": 0.088183816
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6219821335,
              "format_passes": 0,
              "gpu_energy_j": 163.44748926067876,
              "semantic_passes": 0,
              "tokens_per_s": 78.87591998680642,
              "ttft_s": 0.320255388
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5614961844999999,
              "format_passes": 0,
              "gpu_energy_j": 146.91116159973865,
              "semantic_passes": 0,
              "tokens_per_s": 78.82268464614401,
              "ttft_s": 0.25669461849999997
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
              "e2e_s": 0.6660306205,
              "format_passes": 2,
              "gpu_energy_j": 174.4622132554174,
              "semantic_passes": 2,
              "tokens_per_s": 79.31391801656613,
              "ttft_s": 0.1238411985
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6591616485,
              "format_passes": 0,
              "gpu_energy_j": 456.9540914143524,
              "semantic_passes": 0,
              "tokens_per_s": 79.60563311451719,
              "ttft_s": 0.0629873735
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237580958,
              "format_passes": 2,
              "gpu_energy_j": 59.13597992259474,
              "semantic_passes": 2,
              "tokens_per_s": 78.36755403270654,
              "ttft_s": 0.0716521215
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24146242,
              "format_passes": 0,
              "gpu_energy_j": 61.66781961198271,
              "semantic_passes": 0,
              "tokens_per_s": 77.50842250648424,
              "ttft_s": 0.1253122935
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18193939650000002,
              "format_passes": 2,
              "gpu_energy_j": 39.04609823509328,
              "semantic_passes": 2,
              "tokens_per_s": 77.65382852328915,
              "ttft_s": 0.0659791075
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357816645,
              "format_passes": 0,
              "gpu_energy_j": 91.05802383211362,
              "semantic_passes": 0,
              "tokens_per_s": 78.82564171077462,
              "ttft_s": 0.078676837
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46949429249999997,
              "format_passes": 0,
              "gpu_energy_j": 119.73552375463356,
              "semantic_passes": 2,
              "tokens_per_s": 79.03157238094387,
              "ttft_s": 0.1151399315
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7209473665,
              "format_passes": 0,
              "gpu_energy_j": 189.95700918682326,
              "semantic_passes": 0,
              "tokens_per_s": 2846.0051722007443,
              "ttft_s": 0.7206615704999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.08107285,
              "format_passes": 2,
              "gpu_energy_j": 288.9897053100759,
              "semantic_passes": 2,
              "tokens_per_s": 77.884232619317,
              "ttft_s": 0.8242536014999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23402023049999998,
              "format_passes": 0,
              "gpu_energy_j": 56.165721291510295,
              "semantic_passes": 0,
              "tokens_per_s": 77.97837165581787,
              "ttft_s": 0.067283604
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199263705,
              "format_passes": 0,
              "gpu_energy_j": 48.592200825518134,
              "semantic_passes": 0,
              "tokens_per_s": 2547.7324442897443,
              "ttft_s": 0.19911143
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.717979286,
              "format_passes": 0,
              "gpu_energy_j": 189.38836595973666,
              "semantic_passes": 0,
              "tokens_per_s": 2857.4066627099064,
              "ttft_s": 0.717749785
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.418802884,
              "format_passes": 0,
              "gpu_energy_j": 381.4569131650046,
              "semantic_passes": 0,
              "tokens_per_s": 2890.4844767522154,
              "ttft_s": 1.4184231975000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952474705,
              "format_passes": 2,
              "gpu_energy_j": 72.83666314173955,
              "semantic_passes": 2,
              "tokens_per_s": 78.59454462908104,
              "ttft_s": 0.0789167095
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353175102,
              "format_passes": 2,
              "gpu_energy_j": 89.7959918263505,
              "semantic_passes": 2,
              "tokens_per_s": 78.7954514256302,
              "ttft_s": 0.073923834
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36957359850000004,
              "format_passes": 2,
              "gpu_energy_j": 93.77601295137053,
              "semantic_passes": 2,
              "tokens_per_s": 78.87848765238184,
              "ttft_s": 0.077937649
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6209602505,
              "format_passes": 0,
              "gpu_energy_j": 164.4563886445918,
              "semantic_passes": 0,
              "tokens_per_s": 78.96030974342807,
              "ttft_s": 0.3191050905
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5619866255,
              "format_passes": 0,
              "gpu_energy_j": 147.10442110305667,
              "semantic_passes": 0,
              "tokens_per_s": 78.6047681534194,
              "ttft_s": 0.2569322465
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -3.731539574560505,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.842830739030333,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.36232310886310515,
            "ttft_change_pct": -14.974243672355403
          },
          "decode": {
            "e2e_change_pct": 0.050664271927125526,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2673245201188612,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.024104855812856485,
            "ttft_change_pct": 0.10911299357150295
          },
          "energy": {
            "e2e_change_pct": -5.3872986851400295,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3009868980329511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.87510170707914,
            "ttft_change_pct": -12.707817086882223
          },
          "filtering": {
            "e2e_change_pct": -7.989606054336029,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.211469964023906,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.2391674565357391,
            "ttft_change_pct": -12.15534986314929
          },
          "german": {
            "e2e_change_pct": -11.023039761411447,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -12.207863998855384,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.361034293052411,
            "ttft_change_pct": -21.610139184874622
          },
          "ha_sim": {
            "e2e_change_pct": -6.328634196349858,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8546439106735155,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5077397586753074,
            "ttft_change_pct": -18.253742252144868
          },
          "jarvis_memory": {
            "e2e_change_pct": -2.8936398657193663,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2444571249177305,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5252510220013829,
            "ttft_change_pct": -6.954359663991106
          },
          "length-prefill": {
            "e2e_change_pct": 259.74080309759347,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 289.57076709177664,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 259.9414554745395
          },
          "long_context": {
            "e2e_change_pct": -0.9857685343726108,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0110739055678164,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.00937561492786454,
            "ttft_change_pct": -1.1255717960870992
          },
          "math": {
            "e2e_change_pct": -6.338639212311059,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.45809111750167997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.042883100826140996,
            "ttft_change_pct": -17.373530709470263
          },
          "prefill": {
            "e2e_change_pct": -0.26264382858152135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9708453307357034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.2501486280968468,
            "ttft_change_pct": -0.24180504351034582
          },
          "prefill2048": {
            "e2e_change_pct": -0.21592354452458773,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2988948438810488,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12047687243810223,
            "ttft_change_pct": -0.15577699643737342
          },
          "prefill4096": {
            "e2e_change_pct": -0.02760167622409826,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2540798780331541,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.028886891953372462,
            "ttft_change_pct": -0.030987666905379907
          },
          "pve_sim": {
            "e2e_change_pct": -4.9986812803038845,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9880505349986755,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.6240423053712307,
            "ttft_change_pct": -13.775148902770873
          },
          "sorting": {
            "e2e_change_pct": -2.9689664787953096,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.170243103509618,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1742834865380738,
            "ttft_change_pct": -10.171567235837953
          },
          "time": {
            "e2e_change_pct": -4.529345486863267,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.644436578038789,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.5920904861409735,
            "ttft_change_pct": -11.619101400647036
          },
          "tool-call": {
            "e2e_change_pct": -0.1642945906258797,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6172620873386325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10699051958540373,
            "ttft_change_pct": -0.35918131063573666
          },
          "tool-final": {
            "e2e_change_pct": 0.08734538426771188,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.13154855030317325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.27646418502857983,
            "ttft_change_pct": 0.09257225624308418
          }
        }
      },
      "complete": true
    }
  }
}
```
