# Public audit excerpt

Original SHA256: `6a3317baf08620ddb7ed4652e7dbd4c6b21a6d2931680e0878b1d88be7cab630`

Original file: `RESULTS.json`; 46030 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6660283565,
              "format_passes": 2,
              "gpu_energy_j": 178.44604793875186,
              "semantic_passes": 2,
              "tokens_per_s": 79.28101318348878,
              "ttft_s": 0.123606217
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 4.2226487715,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 79.46218685250219,
              "ttft_s": 2.622186502
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.9411506665,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 78.63488241306143,
              "ttft_s": 0.73752108
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659582269,
              "format_passes": 0,
              "gpu_energy_j": 462.20831966741036,
              "semantic_passes": 0,
              "tokens_per_s": 79.55618937832406,
              "ttft_s": 0.06298394600000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2377063585,
              "format_passes": 2,
              "gpu_energy_j": 59.484966449627095,
              "semantic_passes": 2,
              "tokens_per_s": 78.24188078008193,
              "ttft_s": 0.07149646400000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241483288,
              "format_passes": 0,
              "gpu_energy_j": 57.29375395697911,
              "semantic_passes": 0,
              "tokens_per_s": 77.60361640861407,
              "ttft_s": 0.1255111585
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182150444,
              "format_passes": 2,
              "gpu_energy_j": 43.309306850322145,
              "semantic_passes": 2,
              "tokens_per_s": 77.46148821704796,
              "ttft_s": 0.0659585375
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3577613525,
              "format_passes": 0,
              "gpu_energy_j": 89.75622251154914,
              "semantic_passes": 0,
              "tokens_per_s": 78.83464874937411,
              "ttft_s": 0.0786950285
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469065901,
              "format_passes": 0,
              "gpu_energy_j": 118.31919713691856,
              "semantic_passes": 2,
              "tokens_per_s": 79.11806117201526,
              "ttft_s": 0.1151047585
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081924141,
              "format_passes": 2,
              "gpu_energy_j": 290.489705491676,
              "semantic_passes": 2,
              "tokens_per_s": 77.83227482204371,
              "ttft_s": 0.8249035175
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2333610705,
              "format_passes": 0,
              "gpu_energy_j": 58.8820781392604,
              "semantic_passes": 0,
              "tokens_per_s": 78.28143704535887,
              "ttft_s": 0.06722214900000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198859641,
              "format_passes": 0,
              "gpu_energy_j": 49.56814892278771,
              "semantic_passes": 0,
              "tokens_per_s": 2552.8840539313233,
              "ttft_s": 0.19870743400000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7206006185,
              "format_passes": 0,
              "gpu_energy_j": 189.53575939806464,
              "semantic_passes": 0,
              "tokens_per_s": 2847.002858154141,
              "ttft_s": 0.7203707275
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4237655685,
              "format_passes": 0,
              "gpu_energy_j": 383.9107955086009,
              "semantic_passes": 0,
              "tokens_per_s": 2880.3067411332477,
              "ttft_s": 1.423458101
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29532727049999996,
              "format_passes": 2,
              "gpu_energy_j": 74.83404314910092,
              "semantic_passes": 2,
              "tokens_per_s": 78.62022888958082,
              "ttft_s": 0.07904823450000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35306537,
              "format_passes": 2,
              "gpu_energy_j": 88.15535761947172,
              "semantic_passes": 2,
              "tokens_per_s": 78.80037953474215,
              "ttft_s": 0.07386609250000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36931669300000003,
              "format_passes": 2,
              "gpu_energy_j": 95.55892591617864,
              "semantic_passes": 2,
              "tokens_per_s": 78.93935910876465,
              "ttft_s": 0.077951391
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6210629885000001,
              "format_passes": 0,
              "gpu_energy_j": 162.62088961802266,
              "semantic_passes": 0,
              "tokens_per_s": 78.9517127426209,
              "ttft_s": 0.31953551199999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56146106,
              "format_passes": 0,
              "gpu_energy_j": 148.04945066154175,
              "semantic_passes": 0,
              "tokens_per_s": 78.76962059537959,
              "ttft_s": 0.2567452405
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
              "e2e_s": 0.6687709305,
              "format_passes": 2,
              "gpu_energy_j": 178.12572551953093,
              "semantic_passes": 2,
              "tokens_per_s": 78.99976037729911,
              "ttft_s": 0.12444674550000001
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.9905281355,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 48.60690830953655,
              "ttft_s": 0.37772553649999996
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.9749450369999999,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 48.98557009692654,
              "ttft_s": 0.485379211
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6993378065,
              "format_passes": 0,
              "gpu_energy_j": 471.0002833212184,
              "semantic_passes": 0,
              "tokens_per_s": 77.69786727078366,
              "ttft_s": 0.06450900100000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2438566885,
              "format_passes": 2,
              "gpu_energy_j": 54.11916527762827,
              "semantic_passes": 2,
              "tokens_per_s": 77.2461179317172,
              "ttft_s": 0.0754839185
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2451338785,
              "format_passes": 0,
              "gpu_energy_j": 62.318674157217586,
              "semantic_passes": 0,
              "tokens_per_s": 76.46016736878539,
              "ttft_s": 0.1274106075
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.179818602,
              "format_passes": 2,
              "gpu_energy_j": 43.25236840634561,
              "semantic_passes": 2,
              "tokens_per_s": 76.91956420896157,
              "ttft_s": 0.06279211000000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.362935162,
              "format_passes": 0,
              "gpu_energy_j": 89.39798705235552,
              "semantic_passes": 0,
              "tokens_per_s": 78.5264244840549,
              "ttft_s": 0.0827267155
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469653263,
              "format_passes": 0,
              "gpu_energy_j": 119.10133801874638,
              "semantic_passes": 2,
              "tokens_per_s": 78.84407274604158,
              "ttft_s": 0.11450289699999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0879539285,
              "format_passes": 2,
              "gpu_energy_j": 293.08397171807894,
              "semantic_passes": 2,
              "tokens_per_s": 77.70049741608986,
              "ttft_s": 0.83049481
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2360239815,
              "format_passes": 0,
              "gpu_energy_j": 55.89564569609262,
              "semantic_passes": 0,
              "tokens_per_s": 77.54976817135177,
              "ttft_s": 0.0683967815
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2135422495,
              "format_passes": 0,
              "gpu_energy_j": 51.250175351936704,
              "semantic_passes": 0,
              "tokens_per_s": 2377.25303702929,
              "ttft_s": 0.2133284385
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7388468965,
              "format_passes": 0,
              "gpu_energy_j": 193.98515953834075,
              "semantic_passes": 0,
              "tokens_per_s": 2776.64795798018,
              "ttft_s": 0.738593887
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.456744016,
              "format_passes": 0,
              "gpu_energy_j": 395.3426974820003,
              "semantic_passes": 0,
              "tokens_per_s": 2815.0664107364482,
              "ttft_s": 1.456446371
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.296671016,
              "format_passes": 2,
              "gpu_energy_j": 75.7424331565139,
              "semantic_passes": 2,
              "tokens_per_s": 78.26965912707233,
              "ttft_s": 0.0794378915
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3552651735,
              "format_passes": 2,
              "gpu_energy_j": 91.22858696479145,
              "semantic_passes": 2,
              "tokens_per_s": 77.96959800070815,
              "ttft_s": 0.07307062950000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3702326145,
              "format_passes": 2,
              "gpu_energy_j": 96.95200587823854,
              "semantic_passes": 2,
              "tokens_per_s": 78.64216185977713,
              "ttft_s": 0.0777123935
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6429244350000001,
              "format_passes": 0,
              "gpu_energy_j": 167.43523682605382,
              "semantic_passes": 0,
              "tokens_per_s": 77.13313338142466,
              "ttft_s": 0.3349704695
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5802525065,
              "format_passes": 0,
              "gpu_energy_j": 150.67632899987373,
              "semantic_passes": 0,
              "tokens_per_s": 77.08466510366117,
              "ttft_s": 0.2684465855
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
            "e2e_change_pct": 0.41178036539049057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.17950659200414165,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3547543035792633,
            "ttft_change_pct": 0.6800050356690512
          },
          "concurrent-decode": {
            "e2e_change_pct": -29.178856747830284,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -38.83014017754035,
            "ttft_change_pct": -85.59501636470554
          },
          "concurrent-quality": {
            "e2e_change_pct": 3.5907503126652474,
            "format_pass_change": 0,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -34.18775080978025
          },
          "decode": {
            "e2e_change_pct": 2.395514717324332,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9021647338876235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.3358611342019886,
            "ttft_change_pct": 2.4213392409551338
          },
          "energy": {
            "e2e_change_pct": 2.587364527735181,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.020432375199672,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2726724337871809,
            "ttft_change_pct": 5.577135255248411
          },
          "filtering": {
            "e2e_change_pct": 1.5117362904218945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.77045027283707,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4734481364991558,
            "ttft_change_pct": 1.5133706219435439
          },
          "german": {
            "e2e_change_pct": -1.280173656892103,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.13146930329158701,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6996044364238174,
            "ttft_change_pct": -4.80063327662471
          },
          "ha_sim": {
            "e2e_change_pct": 1.44616221507603,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.39912047228539693,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3909756309044998,
            "ttft_change_pct": 5.123178778695037
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.1252195051372862,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6610430942349366,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3463032611200956,
            "ttft_change_pct": -0.5228815105849938
          },
          "long_context": {
            "e2e_change_pct": 0.5573207280897385,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8930664933588517,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1693094622444935,
            "ttft_change_pct": 0.6778116932929734
          },
          "math": {
            "e2e_change_pct": 1.1411119233788458,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.071886960417138,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9346645917896801,
            "ttft_change_pct": 1.747389093437035
          },
          "prefill": {
            "e2e_change_pct": 7.383402899736713,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.393361393763339,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.879709896404007,
            "ttft_change_pct": 7.35805611580691
          },
          "prefill2048": {
            "e2e_change_pct": 2.532093025118609,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3475254244405885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.471191764787195,
            "ttft_change_pct": 2.5296918384291267
          },
          "prefill4096": {
            "e2e_change_pct": 2.3162835392026127,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.977749546806696,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.265048005655501,
            "ttft_change_pct": 2.3174739022402635
          },
          "pve_sim": {
            "e2e_change_pct": 0.4550021735971299,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2138726830555946,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.44590274978828504,
            "ttft_change_pct": 0.49293574039277477
          },
          "sorting": {
            "e2e_change_pct": 0.6230584154996555,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4861515264738907,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0542862089486738,
            "ttft_change_pct": -1.0768987137095398
          },
          "time": {
            "e2e_change_pct": 0.24800435977043733,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.457822959711641,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3764880439148577,
            "ttft_change_pct": -0.30659812087251437
          },
          "tool-call": {
            "e2e_change_pct": 3.52000471849081,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9604728023192584,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.303407105460431,
            "ttft_change_pct": 4.830435716954051
          },
          "tool-final": {
            "e2e_change_pct": 3.3468833083455607,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7743249479103662,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.1390930652994133,
            "ttft_change_pct": 4.5575703671125956
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 124.3245943273596,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 76.25644108189354,
            "exact_serial_matches": 24,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 16,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 18,
            "request_e2e_s": 4.2226487715,
            "wave_elapsed_s": 6.7141869295,
            "waves": 6
          },
          "B": {
            "active_slots_max": 4,
            "aggregate_tokens_per_s": 171.06195210543967,
            "exact_serial_matches": 4,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 16,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 18,
            "request_e2e_s": 2.9905281355,
            "wave_elapsed_s": 2.993068085,
            "waves": 6
          }
        },
        "change_exercised": true,
        "note": "Aggregate four-request wall-clock throughput; per-request native throughput and correctness are reported separately. Two starts per arm give preliminary results."
      }
    }
  }
}
```
