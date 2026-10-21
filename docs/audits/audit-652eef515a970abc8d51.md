# Public audit excerpt

Original SHA256: `652eef515a970abc8d51bd7ae2f62df389ccab5c9e4337731f3b63ad1bc2d6ae`

Original file: `RESULTS.json`; 40921 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666322396,
              "format_passes": 2,
              "gpu_energy_j": 176.47853810917138,
              "semantic_passes": 2,
              "tokens_per_s": 79.22879073409952,
              "ttft_s": 0.1235421645
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659696354,
              "format_passes": 0,
              "gpu_energy_j": 456.16600680668824,
              "semantic_passes": 0,
              "tokens_per_s": 79.53000895940255,
              "ttft_s": 0.06268056350000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23792196300000001,
              "format_passes": 2,
              "gpu_energy_j": 57.697376376053086,
              "semantic_passes": 2,
              "tokens_per_s": 78.29136817015285,
              "ttft_s": 0.0718801865
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24161888650000002,
              "format_passes": 0,
              "gpu_energy_j": 60.00102288123249,
              "semantic_passes": 0,
              "tokens_per_s": 77.42773487275163,
              "ttft_s": 0.1253524735
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18228766200000002,
              "format_passes": 2,
              "gpu_energy_j": 42.89685649174031,
              "semantic_passes": 2,
              "tokens_per_s": 77.40570680874035,
              "ttft_s": 0.066003546
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357705361,
              "format_passes": 0,
              "gpu_energy_j": 88.62772114480211,
              "semantic_passes": 0,
              "tokens_per_s": 78.81071818268762,
              "ttft_s": 0.078527353
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4693735625,
              "format_passes": 0,
              "gpu_energy_j": 116.71917250634871,
              "semantic_passes": 2,
              "tokens_per_s": 78.99049798084624,
              "ttft_s": 0.114853758
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0795026965,
              "format_passes": 2,
              "gpu_energy_j": 289.78681557106677,
              "semantic_passes": 2,
              "tokens_per_s": 77.74939287523028,
              "ttft_s": 0.822273189
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2333285825,
              "format_passes": 0,
              "gpu_energy_j": 56.15975894472963,
              "semantic_passes": 0,
              "tokens_per_s": 78.30790874531542,
              "ttft_s": 0.06725445499999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19861061800000002,
              "format_passes": 0,
              "gpu_energy_j": 48.25643464587348,
              "semantic_passes": 0,
              "tokens_per_s": 2556.1947519547252,
              "ttft_s": 0.19847359850000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.71811589,
              "format_passes": 0,
              "gpu_energy_j": 187.5433978528466,
              "semantic_passes": 0,
              "tokens_per_s": 2856.884531935956,
              "ttft_s": 0.7178681885
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.422681694,
              "format_passes": 0,
              "gpu_energy_j": 380.8447188952689,
              "semantic_passes": 0,
              "tokens_per_s": 2882.6151389722063,
              "ttft_s": 1.4223684665
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952847395,
              "format_passes": 2,
              "gpu_energy_j": 74.17250155942686,
              "semantic_passes": 2,
              "tokens_per_s": 78.52072157534951,
              "ttft_s": 0.078708684
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353935508,
              "format_passes": 2,
              "gpu_energy_j": 90.3778895180044,
              "semantic_passes": 2,
              "tokens_per_s": 78.56095661598314,
              "ttft_s": 0.0739092415
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3694188245,
              "format_passes": 2,
              "gpu_energy_j": 94.47564727934719,
              "semantic_passes": 2,
              "tokens_per_s": 78.89763066255105,
              "ttft_s": 0.0778184445
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6210264885000001,
              "format_passes": 0,
              "gpu_energy_j": 164.61784005866087,
              "semantic_passes": 0,
              "tokens_per_s": 78.8644906942645,
              "ttft_s": 0.31931093499999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561403877,
              "format_passes": 0,
              "gpu_energy_j": 146.85405287968018,
              "semantic_passes": 0,
              "tokens_per_s": 78.67991086542023,
              "ttft_s": 0.256508128
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
              "e2e_s": 0.6728575575,
              "format_passes": 2,
              "gpu_energy_j": 177.58593205581883,
              "semantic_passes": 2,
              "tokens_per_s": 78.44409007863521,
              "ttft_s": 0.1246536435
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6777806535000002,
              "format_passes": 0,
              "gpu_energy_j": 464.28502336208624,
              "semantic_passes": 0,
              "tokens_per_s": 78.67206992864755,
              "ttft_s": 0.0634832085
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2402108835,
              "format_passes": 2,
              "gpu_energy_j": 57.20177809706924,
              "semantic_passes": 2,
              "tokens_per_s": 77.38385122037857,
              "ttft_s": 0.07217253900000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2435829565,
              "format_passes": 0,
              "gpu_energy_j": 61.5132201500286,
              "semantic_passes": 0,
              "tokens_per_s": 76.55275415152504,
              "ttft_s": 0.12599531949999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18363097350000002,
              "format_passes": 2,
              "gpu_energy_j": 40.98140839521416,
              "semantic_passes": 2,
              "tokens_per_s": 76.75826990977859,
              "ttft_s": 0.0662767465
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.361510235,
              "format_passes": 0,
              "gpu_energy_j": 91.9342473980509,
              "semantic_passes": 0,
              "tokens_per_s": 78.00460656842293,
              "ttft_s": 0.0794352045
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4755041325,
              "format_passes": 0,
              "gpu_energy_j": 117.30750490711526,
              "semantic_passes": 2,
              "tokens_per_s": 77.76469089564944,
              "ttft_s": 0.1154265805
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0878464955,
              "format_passes": 2,
              "gpu_energy_j": 290.0524734251781,
              "semantic_passes": 2,
              "tokens_per_s": 76.52151643947451,
              "ttft_s": 0.82642684
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.236726015,
              "format_passes": 0,
              "gpu_energy_j": 58.34002131696276,
              "semantic_passes": 0,
              "tokens_per_s": 77.32963918328116,
              "ttft_s": 0.06852414700000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199482783,
              "format_passes": 0,
              "gpu_energy_j": 48.32290735566653,
              "semantic_passes": 0,
              "tokens_per_s": 2544.9718501430407,
              "ttft_s": 0.19932825199999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.72027818,
              "format_passes": 0,
              "gpu_energy_j": 190.72753346496307,
              "semantic_passes": 0,
              "tokens_per_s": 2848.2231241754885,
              "ttft_s": 0.720044496
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.421871675,
              "format_passes": 0,
              "gpu_energy_j": 385.1546865555352,
              "semantic_passes": 0,
              "tokens_per_s": 2884.3242339379995,
              "ttft_s": 1.4214925125
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2982321295,
              "format_passes": 2,
              "gpu_energy_j": 71.34530210437042,
              "semantic_passes": 2,
              "tokens_per_s": 77.70015402998851,
              "ttft_s": 0.07938233
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3586067595,
              "format_passes": 2,
              "gpu_energy_j": 90.43111096027786,
              "semantic_passes": 2,
              "tokens_per_s": 77.79238531425881,
              "ttft_s": 0.07577223050000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.372682115,
              "format_passes": 2,
              "gpu_energy_j": 95.36697539157178,
              "semantic_passes": 2,
              "tokens_per_s": 78.10947987640351,
              "ttft_s": 0.07813790000000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6255698144999999,
              "format_passes": 0,
              "gpu_energy_j": 164.70521325022577,
              "semantic_passes": 0,
              "tokens_per_s": 78.06827327574005,
              "ttft_s": 0.3209080865
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5643083449999999,
              "format_passes": 0,
              "gpu_energy_j": 149.29341714554226,
              "semantic_passes": 0,
              "tokens_per_s": 77.87265201745645,
              "ttft_s": 0.25636699
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
            "e2e_change_pct": 0.9807807060412843,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6274949682337105,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9904236177197823,
            "ttft_change_pct": 0.8996758349656409
          },
          "decode": {
            "e2e_change_pct": 1.0896149441080416,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7798381366103566,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.078761390801497,
            "ttft_change_pct": 1.2805325210581309
          },
          "energy": {
            "e2e_change_pct": 0.9620467447135184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8589615509615123,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.159153264255064,
            "ttft_change_pct": 0.40672195529154465
          },
          "filtering": {
            "e2e_change_pct": 0.8128793359040598,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5202858154425023,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.1300611113893133,
            "ttft_change_pct": 0.5128307260725773
          },
          "german": {
            "e2e_change_pct": 0.7369184975338561,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.465241169583056,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8364201111960567,
            "ttft_change_pct": 0.4139179128345605
          },
          "ha_sim": {
            "e2e_change_pct": 1.0636893977107542,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7308036475929507,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0228451571727581,
            "ttft_change_pct": 1.156095889288422
          },
          "jarvis_memory": {
            "e2e_change_pct": 1.3061174488284033,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.504058063583801,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5518411917013641,
            "ttft_change_pct": 0.4987407551784173
          },
          "long_context": {
            "e2e_change_pct": 0.7729298895734482,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.09167354753107926,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.579274628840166,
            "ttft_change_pct": 0.5051424581958397
          },
          "math": {
            "e2e_change_pct": 1.456072146668963,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.882250232553286,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.249260231448568,
            "ttft_change_pct": 1.887892779742284
          },
          "prefill": {
            "e2e_change_pct": 0.43913311825050094,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.13774890391478056,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.43904721277995273,
            "ttft_change_pct": 0.4306131931194779
          },
          "prefill2048": {
            "e2e_change_pct": 0.30110599557962026,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6978126921934455,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3031766829791449,
            "ttft_change_pct": 0.3031625491787482
          },
          "prefill4096": {
            "e2e_change_pct": -0.05693606682479757,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.131686339978244,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.05928973808146942,
            "ttft_change_pct": -0.06158418304614832
          },
          "pve_sim": {
            "e2e_change_pct": 0.9981518194914996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.8116544482341586,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0450331185170914,
            "ttft_change_pct": 0.8558725235451758
          },
          "sorting": {
            "e2e_change_pct": 1.3198030133783512,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.05888767989306043,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9783120456147487,
            "ttft_change_pct": 2.5206441876419516
          },
          "time": {
            "e2e_change_pct": 0.8833579351070542,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9434474786810476,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9989536815351308,
            "ttft_change_pct": 0.41051385960304554
          },
          "tool-call": {
            "e2e_change_pct": 0.7315832873688866,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.05307638074569798,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0096019279591362,
            "ttft_change_pct": 0.5001869102917
          },
          "tool-final": {
            "e2e_change_pct": 0.5173580231616182,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6610806566303538,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0260037652363052,
            "ttft_change_pct": -0.05502281783444918
          }
        }
      },
      "complete": true
    }
  }
}
```
