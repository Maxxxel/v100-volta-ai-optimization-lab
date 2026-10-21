# Public audit excerpt

Original SHA256: `c1e687f321b4bfb3a8b1b14b30852ef37436c746e327c364f173df0157982da3`

Original file: `RESULTS.json`; 39554 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5262365790000001,
              "format_passes": 2,
              "gpu_energy_j": 132.5939099281349,
              "semantic_passes": 2,
              "tokens_per_s": 96.47709703153699,
              "ttft_s": 0.13235150950000002
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3677734075,
              "format_passes": 0,
              "gpu_energy_j": 356.1806770936329,
              "semantic_passes": 0,
              "tokens_per_s": 96.94534402495695,
              "ttft_s": 0.0576432535
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20665026,
              "format_passes": 2,
              "gpu_energy_j": 45.175869853737616,
              "semantic_passes": 2,
              "tokens_per_s": 94.21554789606004,
              "ttft_s": 0.0686361645
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2331055635,
              "format_passes": 0,
              "gpu_energy_j": 55.450334201422955,
              "semantic_passes": 0,
              "tokens_per_s": 92.00963066394831,
              "ttft_s": 0.1352176155
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15754093949999998,
              "format_passes": 2,
              "gpu_energy_j": 34.479600326987565,
              "semantic_passes": 2,
              "tokens_per_s": 94.11300385612707,
              "ttft_s": 0.061898807
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30707072550000003,
              "format_passes": 0,
              "gpu_energy_j": 73.05269036236392,
              "semantic_passes": 0,
              "tokens_per_s": 95.70795385866094,
              "ttft_s": 0.077147187
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3983955695,
              "format_passes": 0,
              "gpu_energy_j": 92.35383890360725,
              "semantic_passes": 2,
              "tokens_per_s": 96.1185872747296,
              "ttft_s": 0.10712055100000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0298505285,
              "format_passes": 2,
              "gpu_energy_j": 271.6171935631738,
              "semantic_passes": 2,
              "tokens_per_s": 94.11483822904627,
              "ttft_s": 0.8704166945
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14946261700000002,
              "format_passes": 0,
              "gpu_energy_j": 30.754266168679727,
              "semantic_passes": 0,
              "tokens_per_s": 92.87114953284677,
              "ttft_s": 0.06333633150000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206251303,
              "format_passes": 0,
              "gpu_energy_j": 48.858679682111514,
              "semantic_passes": 0,
              "tokens_per_s": 2461.1353579024544,
              "ttft_s": 0.20610860949999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7546692635000001,
              "format_passes": 0,
              "gpu_energy_j": 199.7264756035453,
              "semantic_passes": 0,
              "tokens_per_s": 2718.202819762544,
              "ttft_s": 0.7544339975000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4979910250000001,
              "format_passes": 0,
              "gpu_energy_j": 405.0254047640684,
              "semantic_passes": 0,
              "tokens_per_s": 2737.3551128410368,
              "ttft_s": 1.4977004699999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2544326335,
              "format_passes": 2,
              "gpu_energy_j": 57.85278390457202,
              "semantic_passes": 2,
              "tokens_per_s": 95.50035931496977,
              "ttft_s": 0.076360256
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3505643635,
              "format_passes": 0,
              "gpu_energy_j": 84.93365273971935,
              "semantic_passes": 2,
              "tokens_per_s": 96.23788892631798,
              "ttft_s": 0.0699607085
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314844551,
              "format_passes": 0,
              "gpu_energy_j": 75.4616597435139,
              "semantic_passes": 0,
              "tokens_per_s": 95.83311978198637,
              "ttft_s": 0.0747706115
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5504093785,
              "format_passes": 0,
              "gpu_energy_j": 139.14534578854344,
              "semantic_passes": 0,
              "tokens_per_s": 96.12290818578526,
              "ttft_s": 0.302951415
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5247688755,
              "format_passes": 0,
              "gpu_energy_j": 133.54070703254703,
              "semantic_passes": 0,
              "tokens_per_s": 95.73558895377246,
              "ttft_s": 0.274248669
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5268146579999999,
              "format_passes": 2,
              "gpu_energy_j": 132.56245544211282,
              "semantic_passes": 2,
              "tokens_per_s": 96.57066946539888,
              "ttft_s": 0.13331993250000002
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3667929735,
              "format_passes": 0,
              "gpu_energy_j": 353.9080188181486,
              "semantic_passes": 0,
              "tokens_per_s": 97.03401605161847,
              "ttft_s": 0.05782036
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20469052799999998,
              "format_passes": 2,
              "gpu_energy_j": 46.82723240116287,
              "semantic_passes": 2,
              "tokens_per_s": 95.27833305090803,
              "ttft_s": 0.0681717835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22986233849999999,
              "format_passes": 0,
              "gpu_energy_j": 55.36349672435632,
              "semantic_passes": 0,
              "tokens_per_s": 93.86685079493492,
              "ttft_s": 0.1339778935
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15763637749999998,
              "format_passes": 2,
              "gpu_energy_j": 33.42993604553257,
              "semantic_passes": 2,
              "tokens_per_s": 93.6764829979087,
              "ttft_s": 0.061475858
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3074227855,
              "format_passes": 0,
              "gpu_energy_j": 70.82998572082887,
              "semantic_passes": 0,
              "tokens_per_s": 95.8230759932666,
              "ttft_s": 0.07778385199999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39828747249999996,
              "format_passes": 0,
              "gpu_energy_j": 95.04037684215679,
              "semantic_passes": 2,
              "tokens_per_s": 96.217298888724,
              "ttft_s": 0.10724001350000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0294282755,
              "format_passes": 2,
              "gpu_energy_j": 271.94541401553306,
              "semantic_passes": 2,
              "tokens_per_s": 94.18928776644343,
              "ttft_s": 0.870024483
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14865673950000002,
              "format_passes": 0,
              "gpu_energy_j": 30.43582872130664,
              "semantic_passes": 0,
              "tokens_per_s": 93.74026182824102,
              "ttft_s": 0.063276253
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20567361550000002,
              "format_passes": 0,
              "gpu_energy_j": 50.56745235697561,
              "semantic_passes": 0,
              "tokens_per_s": 2468.087912506626,
              "ttft_s": 0.2054893265
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7560553489999999,
              "format_passes": 0,
              "gpu_energy_j": 198.7607937192302,
              "semantic_passes": 0,
              "tokens_per_s": 2713.4129981345,
              "ttft_s": 0.755792748
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.495428733,
              "format_passes": 0,
              "gpu_energy_j": 403.757714499488,
              "semantic_passes": 0,
              "tokens_per_s": 2742.1199418545,
              "ttft_s": 1.495114794
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.255248571,
              "format_passes": 2,
              "gpu_energy_j": 56.66272084353362,
              "semantic_passes": 2,
              "tokens_per_s": 95.10895311527338,
              "ttft_s": 0.0765279985
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35201390850000003,
              "format_passes": 0,
              "gpu_energy_j": 82.50102007302286,
              "semantic_passes": 2,
              "tokens_per_s": 95.8521868556082,
              "ttft_s": 0.07028471
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3146235005,
              "format_passes": 0,
              "gpu_energy_j": 73.87686607797835,
              "semantic_passes": 0,
              "tokens_per_s": 95.98131575023407,
              "ttft_s": 0.074996703
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5512974225,
              "format_passes": 0,
              "gpu_energy_j": 137.0359963481423,
              "semantic_passes": 0,
              "tokens_per_s": 96.11535786897487,
              "ttft_s": 0.303839142
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.52519236,
              "format_passes": 0,
              "gpu_energy_j": 131.1941063367288,
              "semantic_passes": 0,
              "tokens_per_s": 95.79691337171236,
              "ttft_s": 0.27392815800000003
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
            "e2e_change_pct": 0.10985154264615549,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.023722421368477242,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09698927179713213,
            "ttft_change_pct": 0.7317052927152234
          },
          "decode": {
            "e2e_change_pct": -0.07168102513355201,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6380633261828583,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09146599824194634,
            "ttft_change_pct": 0.30724584274204325
          },
          "energy": {
            "e2e_change_pct": -0.9483327047350554,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.655408413322725,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.1280358482025354,
            "ttft_change_pct": -0.6765835523924069
          },
          "filtering": {
            "e2e_change_pct": -1.39131170929776,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.15660406437083552,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.0185062341678384,
            "ttft_change_pct": -0.9168346856404996
          },
          "german": {
            "e2e_change_pct": 0.06057980884390801,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0443052457119424,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4638262942766924,
            "ttft_change_pct": -0.683291036610767
          },
          "ha_sim": {
            "e2e_change_pct": 0.11465111154009833,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.04260476994036,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12028481433807858,
            "ttft_change_pct": 0.8252601614625155
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.027133082864272406,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.908961847653746,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10269773702795693,
            "ttft_change_pct": 0.11152155107940764
          },
          "long_context": {
            "e2e_change_pct": -0.0410013869308834,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.12083935043047944,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07910499427941087,
            "ttft_change_pct": -0.04506019961224572
          },
          "math": {
            "e2e_change_pct": -0.5391833196658147,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0354252825495402,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9358259263140267,
            "ttft_change_pct": -0.09485629902642456
          },
          "prefill": {
            "e2e_change_pct": -0.280089139606543,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.497377919300848,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2824937922186077,
            "ttft_change_pct": -0.3004644015125235
          },
          "prefill2048": {
            "e2e_change_pct": 0.1836679413139919,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4835021903815906,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17621281212792939,
            "ttft_change_pct": 0.1801019710806262
          },
          "prefill4096": {
            "e2e_change_pct": -0.17104855484698644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3129903086743102,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17406689366357142,
            "ttft_change_pct": -0.17264306527191575
          },
          "pve_sim": {
            "e2e_change_pct": 0.320689012559372,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.057054096137201,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4098478817294193,
            "ttft_change_pct": 0.21967252178933805
          },
          "sorting": {
            "e2e_change_pct": 0.41348897689654773,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.864156418835928,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.40077985397735105,
            "ttft_change_pct": 0.4631192378504956
          },
          "time": {
            "e2e_change_pct": -0.07020940946822485,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1001309418877123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15463961580801655,
            "ttft_change_pct": 0.30238016710615323
          },
          "tool-call": {
            "e2e_change_pct": 0.1613424543055686,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.515932443480128,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.007854856821232215,
            "ttft_change_pct": 0.293026193655499
          },
          "tool-final": {
            "e2e_change_pct": 0.08069924108906612,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7572175166380655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06405603037498153,
            "ttft_change_pct": -0.1168687531533541
          }
        }
      },
      "complete": true
    }
  }
}
```
