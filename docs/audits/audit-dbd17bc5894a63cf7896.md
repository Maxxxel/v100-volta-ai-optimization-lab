# Public audit excerpt

Original SHA256: `dbd17bc5894a63cf78967912471e78c3cf60499dede7ff95069b7c32090dfe9b`

Original file: `RESULTS.json`; 40659 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.525602304,
              "format_passes": 2,
              "gpu_energy_j": 134.56096974097125,
              "semantic_passes": 2,
              "tokens_per_s": 96.66341581013722,
              "ttft_s": 0.1324343555
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3665429915,
              "format_passes": 0,
              "gpu_energy_j": 356.4517940480844,
              "semantic_passes": 0,
              "tokens_per_s": 97.04683725202312,
              "ttft_s": 0.0577087505
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20471533050000001,
              "format_passes": 2,
              "gpu_energy_j": 46.706084545596845,
              "semantic_passes": 2,
              "tokens_per_s": 95.03475353193146,
              "ttft_s": 0.0678834395
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22994605099999998,
              "format_passes": 0,
              "gpu_energy_j": 53.119198918033874,
              "semantic_passes": 0,
              "tokens_per_s": 93.96092515674297,
              "ttft_s": 0.13410029699999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156898405,
              "format_passes": 2,
              "gpu_energy_j": 32.81950158108896,
              "semantic_passes": 2,
              "tokens_per_s": 93.87993098785095,
              "ttft_s": 0.061038798
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30689377900000003,
              "format_passes": 0,
              "gpu_energy_j": 71.845388035027,
              "semantic_passes": 0,
              "tokens_per_s": 95.90423768983592,
              "ttft_s": 0.07747261750000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398119172,
              "format_passes": 0,
              "gpu_energy_j": 92.84169607845644,
              "semantic_passes": 2,
              "tokens_per_s": 96.21788467514682,
              "ttft_s": 0.1071030615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0319838375,
              "format_passes": 2,
              "gpu_energy_j": 273.57229081230366,
              "semantic_passes": 2,
              "tokens_per_s": 94.14630174317445,
              "ttft_s": 0.8726511699999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14868984,
              "format_passes": 0,
              "gpu_energy_j": 28.17036817559906,
              "semantic_passes": 0,
              "tokens_per_s": 93.70386442064071,
              "ttft_s": 0.0632708635
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2066628425,
              "format_passes": 0,
              "gpu_energy_j": 51.16744585747131,
              "semantic_passes": 0,
              "tokens_per_s": 2456.5961053470637,
              "ttft_s": 0.206527119
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7555504145,
              "format_passes": 0,
              "gpu_energy_j": 198.24699113461654,
              "semantic_passes": 0,
              "tokens_per_s": 2715.4446539453165,
              "ttft_s": 0.7552973135000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5013668175000001,
              "format_passes": 0,
              "gpu_energy_j": 401.73539685509115,
              "semantic_passes": 0,
              "tokens_per_s": 2731.4007543894368,
              "ttft_s": 1.5010470555
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2539854185,
              "format_passes": 2,
              "gpu_energy_j": 60.05824607118322,
              "semantic_passes": 2,
              "tokens_per_s": 95.61894471076134,
              "ttft_s": 0.076182785
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35109828499999995,
              "format_passes": 0,
              "gpu_energy_j": 85.2643964596098,
              "semantic_passes": 2,
              "tokens_per_s": 95.9851779027222,
              "ttft_s": 0.06977170299999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3209787665,
              "format_passes": 0,
              "gpu_energy_j": 73.4257845040238,
              "semantic_passes": 0,
              "tokens_per_s": 93.85335365897242,
              "ttft_s": 0.0756772135
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5507931685,
              "format_passes": 0,
              "gpu_energy_j": 138.90205598468987,
              "semantic_passes": 0,
              "tokens_per_s": 96.03059171832868,
              "ttft_s": 0.303370543
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5249813395,
              "format_passes": 0,
              "gpu_energy_j": 131.19268038531115,
              "semantic_passes": 0,
              "tokens_per_s": 95.8286593916406,
              "ttft_s": 0.274600383
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
              "e2e_s": 0.611593799,
              "format_passes": 2,
              "gpu_energy_j": 139.05905884457255,
              "semantic_passes": 2,
              "tokens_per_s": 89.95631744095994,
              "ttft_s": 0.189151777
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5673008915,
              "format_passes": 0,
              "gpu_energy_j": 369.14827848415695,
              "semantic_passes": 0,
              "tokens_per_s": 87.38130427424875,
              "ttft_s": 0.1143351725
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2650958715,
              "format_passes": 2,
              "gpu_energy_j": 52.07356411435663,
              "semantic_passes": 2,
              "tokens_per_s": 92.8998122748778,
              "ttft_s": 0.125087268
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2859990835,
              "format_passes": 0,
              "gpu_energy_j": 60.60211685638506,
              "semantic_passes": 0,
              "tokens_per_s": 93.93837817529158,
              "ttft_s": 0.190115739
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2132772605,
              "format_passes": 2,
              "gpu_energy_j": 37.52055803466376,
              "semantic_passes": 2,
              "tokens_per_s": 94.0792900642605,
              "ttft_s": 0.11756132150000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3722351865,
              "format_passes": 0,
              "gpu_energy_j": 76.9982274333024,
              "semantic_passes": 0,
              "tokens_per_s": 92.3517395654167,
              "ttft_s": 0.1339664955
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4644303575,
              "format_passes": 0,
              "gpu_energy_j": 98.40862400660174,
              "semantic_passes": 2,
              "tokens_per_s": 92.9457807450809,
              "ttft_s": 0.1631751695
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0947106645,
              "format_passes": 2,
              "gpu_energy_j": 281.52883446808954,
              "semantic_passes": 2,
              "tokens_per_s": 91.49280415088916,
              "ttft_s": 0.9307363065
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20670144750000002,
              "format_passes": 0,
              "gpu_energy_j": 33.39674325684895,
              "semantic_passes": 0,
              "tokens_per_s": 91.79418176653475,
              "ttft_s": 0.11948666399999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.26244099,
              "format_passes": 0,
              "gpu_energy_j": 53.94428085529764,
              "semantic_passes": 0,
              "tokens_per_s": 2466.192716941954,
              "ttft_s": 0.26225098449999995
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8146037335,
              "format_passes": 0,
              "gpu_energy_j": 204.19369821617312,
              "semantic_passes": 0,
              "tokens_per_s": 2707.72336038942,
              "ttft_s": 0.814357953
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5586351155,
              "format_passes": 0,
              "gpu_energy_j": 408.2983618217711,
              "semantic_passes": 0,
              "tokens_per_s": 2734.389151277477,
              "ttft_s": 1.558316002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.311235656,
              "format_passes": 2,
              "gpu_energy_j": 61.10326855486228,
              "semantic_passes": 2,
              "tokens_per_s": 95.04701730172752,
              "ttft_s": 0.132352639
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.424378767,
              "format_passes": 0,
              "gpu_energy_j": 90.00660417092658,
              "semantic_passes": 2,
              "tokens_per_s": 90.62729256941391,
              "ttft_s": 0.126454758
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37636915049999997,
              "format_passes": 0,
              "gpu_energy_j": 78.49295282295068,
              "semantic_passes": 0,
              "tokens_per_s": 93.9047864045092,
              "ttft_s": 0.1313663135
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6337523469999999,
              "format_passes": 0,
              "gpu_energy_j": 143.3689006232086,
              "semantic_passes": 0,
              "tokens_per_s": 89.01761624103825,
              "ttft_s": 0.36603500050000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5998279845,
              "format_passes": 0,
              "gpu_energy_j": 134.74291456752792,
              "semantic_passes": 0,
              "tokens_per_s": 88.94276200403819,
              "ttft_s": 0.329843095
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
            "e2e_change_pct": 16.360562795402057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.342788857913326,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.938610965653358,
            "ttft_change_pct": 42.82681883100945
          },
          "decode": {
            "e2e_change_pct": 14.690931880572311,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5619078506755386,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.959657884237627,
            "ttft_change_pct": 98.12449846752442
          },
          "energy": {
            "e2e_change_pct": 29.494879964546673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.492034969276377,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.24648476237308,
            "ttft_change_pct": 84.26772261591135
          },
          "filtering": {
            "e2e_change_pct": 24.376601492495297,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.087030849049098,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.023996125425318482,
            "ttft_change_pct": 41.771303459529285
          },
          "german": {
            "e2e_change_pct": 35.93335158505915,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.323972720791133,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.21235537170916086,
            "ttft_change_pct": 92.60097733248287
          },
          "ha_sim": {
            "e2e_change_pct": 21.2912127814751,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.172122719642382,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -3.7042139221296733,
            "ttft_change_pct": 72.92109111971077
          },
          "jarvis_memory": {
            "e2e_change_pct": 16.65611459173837,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.996150612587847,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -3.400723203501388,
            "ttft_change_pct": 52.35341288540103
          },
          "long_context": {
            "e2e_change_pct": 6.078276104784441,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9083879921321554,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.818483087656354,
            "ttft_change_pct": 6.6561689821604375
          },
          "math": {
            "e2e_change_pct": 39.015179181038896,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 18.552739703902542,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.037997755923193,
            "ttft_change_pct": 88.84942829964697
          },
          "prefill": {
            "e2e_change_pct": 26.98992563213196,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.4269564393761405,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3906466990647006,
            "ttft_change_pct": 26.981379380012527
          },
          "prefill2048": {
            "e2e_change_pct": 7.815933638138439,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9996455671392974,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.28434729997821595,
            "ttft_change_pct": 7.81952198748288
          },
          "prefill4096": {
            "e2e_change_pct": 3.814410797712986,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6336536481616593,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10940895008679785,
            "ttft_change_pct": 3.8152665694363375
          },
          "pve_sim": {
            "e2e_change_pct": 22.540757590774852,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7400149888501026,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5981318981963746,
            "ttft_change_pct": 73.7303762260726
          },
          "sorting": {
            "e2e_change_pct": 20.87178580208675,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.561767757968217,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -5.581992397553637,
            "ttft_change_pct": 81.24075027952237
          },
          "time": {
            "e2e_change_pct": 17.256712836174472,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.901074810646657,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.054801180279251405,
            "ttft_change_pct": 73.58767246365379
          },
          "tool-call": {
            "e2e_change_pct": 15.061766057470605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.215823269751361,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -7.3028556336094175,
            "ttft_change_pct": 20.656078497377408
          },
          "tool-final": {
            "e2e_change_pct": 14.257010557991446,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.706122149337742,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -7.185634685194275,
            "ttft_change_pct": 20.117492698471562
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
