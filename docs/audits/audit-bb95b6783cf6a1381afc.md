# Public audit excerpt

Original SHA256: `bb95b6783cf6a1381afc17a6b8058ba3e7c92b62af4ca25bf81828f7b0f48fc0`

Original file: `RESULTS.json`; 45919 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5268823899999999,
              "format_passes": 2,
              "gpu_energy_j": 132.57445975577383,
              "semantic_passes": 2,
              "tokens_per_s": 96.3437717878708,
              "ttft_s": 0.132474706
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 3.4924535375,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 96.83923256414286,
              "ttft_s": 2.177372113
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.821184413,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 95.48514507513951,
              "ttft_s": 0.6323188995
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3673743225,
              "format_passes": 0,
              "gpu_energy_j": 357.39880050329094,
              "semantic_passes": 0,
              "tokens_per_s": 97.01240679485659,
              "ttft_s": 0.058055708
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2047794765,
              "format_passes": 2,
              "gpu_energy_j": 45.67244011405734,
              "semantic_passes": 2,
              "tokens_per_s": 95.03722761767062,
              "ttft_s": 0.06795926050000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23030668599999998,
              "format_passes": 0,
              "gpu_energy_j": 54.81771281754392,
              "semantic_passes": 0,
              "tokens_per_s": 93.79704271888377,
              "ttft_s": 0.1343650545
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156647855,
              "format_passes": 2,
              "gpu_energy_j": 32.99225476495971,
              "semantic_passes": 2,
              "tokens_per_s": 94.06850043851128,
              "ttft_s": 0.06093874
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3083930835,
              "format_passes": 0,
              "gpu_energy_j": 71.95959450431806,
              "semantic_passes": 0,
              "tokens_per_s": 95.46321491240118,
              "ttft_s": 0.0779231735
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3987567355,
              "format_passes": 0,
              "gpu_energy_j": 92.7537202492355,
              "semantic_passes": 2,
              "tokens_per_s": 96.21533635892283,
              "ttft_s": 0.10767330650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0348127295,
              "format_passes": 2,
              "gpu_energy_j": 275.08018462869927,
              "semantic_passes": 2,
              "tokens_per_s": 94.08935684371627,
              "ttft_s": 0.875364264
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1493633165,
              "format_passes": 0,
              "gpu_energy_j": 31.97444867385223,
              "semantic_passes": 0,
              "tokens_per_s": 93.05134704497925,
              "ttft_s": 0.06334680949999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206392927,
              "format_passes": 0,
              "gpu_energy_j": 50.387695334791445,
              "semantic_passes": 0,
              "tokens_per_s": 2459.287715822895,
              "ttft_s": 0.206230058
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.758293112,
              "format_passes": 0,
              "gpu_energy_j": 199.4335944236468,
              "semantic_passes": 0,
              "tokens_per_s": 2705.3342820528487,
              "ttft_s": 0.758027927
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.501801025,
              "format_passes": 0,
              "gpu_energy_j": 407.3339042556704,
              "semantic_passes": 0,
              "tokens_per_s": 2730.4828987252295,
              "ttft_s": 1.5014674664999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2545488285,
              "format_passes": 2,
              "gpu_energy_j": 59.90281487399232,
              "semantic_passes": 2,
              "tokens_per_s": 95.45044275626492,
              "ttft_s": 0.0764269145
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3512602795,
              "format_passes": 0,
              "gpu_energy_j": 81.23985183483484,
              "semantic_passes": 2,
              "tokens_per_s": 96.19255614076629,
              "ttft_s": 0.07050317049999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314375984,
              "format_passes": 0,
              "gpu_energy_j": 75.79079621794229,
              "semantic_passes": 0,
              "tokens_per_s": 96.02306269444095,
              "ttft_s": 0.0747862285
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.551896768,
              "format_passes": 0,
              "gpu_energy_j": 140.56477725170024,
              "semantic_passes": 0,
              "tokens_per_s": 96.14666173213837,
              "ttft_s": 0.304239627
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5253508259999999,
              "format_passes": 0,
              "gpu_energy_j": 128.9339645654689,
              "semantic_passes": 0,
              "tokens_per_s": 95.77920220098895,
              "ttft_s": 0.27481890350000004
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
              "e2e_s": 0.5268286099999999,
              "format_passes": 2,
              "gpu_energy_j": 134.27417665161676,
              "semantic_passes": 2,
              "tokens_per_s": 96.36290195435879,
              "ttft_s": 0.132449394
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.6647617415,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 78.96195523629373,
              "ttft_s": 1.056278688
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 0.989161882,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 65.88978944265656,
              "ttft_s": 0.630726591
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.396770342,
              "format_passes": 0,
              "gpu_energy_j": 363.60482110597866,
              "semantic_passes": 0,
              "tokens_per_s": 95.19408702141858,
              "ttft_s": 0.062094189499999994
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.205061343,
              "format_passes": 2,
              "gpu_energy_j": 45.44928659857808,
              "semantic_passes": 2,
              "tokens_per_s": 94.7088793652963,
              "ttft_s": 0.067736187
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23323427200000002,
              "format_passes": 0,
              "gpu_energy_j": 55.37556673496301,
              "semantic_passes": 0,
              "tokens_per_s": 93.02347941464916,
              "ttft_s": 0.136484417
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1550910715,
              "format_passes": 2,
              "gpu_energy_j": 32.84085467144339,
              "semantic_passes": 2,
              "tokens_per_s": 93.64075346916914,
              "ttft_s": 0.0589501105
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3076495205,
              "format_passes": 0,
              "gpu_energy_j": 71.69047253370964,
              "semantic_passes": 0,
              "tokens_per_s": 95.53962435305812,
              "ttft_s": 0.0773912735
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.399789352,
              "format_passes": 0,
              "gpu_energy_j": 97.45612547715638,
              "semantic_passes": 2,
              "tokens_per_s": 95.82521970307099,
              "ttft_s": 0.1076141635
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0319863329999999,
              "format_passes": 2,
              "gpu_energy_j": 274.34116225890625,
              "semantic_passes": 2,
              "tokens_per_s": 93.8611765668752,
              "ttft_s": 0.872080493
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1524528275,
              "format_passes": 0,
              "gpu_energy_j": 32.11613316472496,
              "semantic_passes": 0,
              "tokens_per_s": 92.95105649314655,
              "ttft_s": 0.0663257725
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.219712243,
              "format_passes": 0,
              "gpu_energy_j": 53.43034496007329,
              "semantic_passes": 0,
              "tokens_per_s": 2309.4968473248327,
              "ttft_s": 0.2195382405
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7610503335,
              "format_passes": 0,
              "gpu_energy_j": 201.86845422518297,
              "semantic_passes": 0,
              "tokens_per_s": 2695.6279840058764,
              "ttft_s": 0.7607836295
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.514004306,
              "format_passes": 0,
              "gpu_energy_j": 408.0560269977866,
              "semantic_passes": 0,
              "tokens_per_s": 2708.5603109255753,
              "ttft_s": 1.5136925854999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2542050645,
              "format_passes": 2,
              "gpu_energy_j": 58.328091719911214,
              "semantic_passes": 2,
              "tokens_per_s": 95.62284518483241,
              "ttft_s": 0.0763659965
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.355105112,
              "format_passes": 0,
              "gpu_energy_j": 86.592686486254,
              "semantic_passes": 2,
              "tokens_per_s": 95.06018489197675,
              "ttft_s": 0.0710364025
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3173643155,
              "format_passes": 0,
              "gpu_energy_j": 75.49533823588806,
              "semantic_passes": 0,
              "tokens_per_s": 95.70629010744022,
              "ttft_s": 0.077004566
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5529586479999999,
              "format_passes": 0,
              "gpu_energy_j": 138.3695927548119,
              "semantic_passes": 0,
              "tokens_per_s": 95.99315843272304,
              "ttft_s": 0.3048922395
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5258952575,
              "format_passes": 0,
              "gpu_energy_j": 133.6893061999875,
              "semantic_passes": 0,
              "tokens_per_s": 95.76117452279269,
              "ttft_s": 0.27516578
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
            "e2e_change_pct": -0.01020721151830939,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2820847235388344,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.019856152746555722,
            "ttft_change_pct": -0.019107043725008488
          },
          "concurrent-decode": {
            "e2e_change_pct": -23.69943614461041,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -18.460779639086724,
            "ttft_change_pct": -51.488370697250694
          },
          "concurrent-quality": {
            "e2e_change_pct": 20.455511130116875,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -30.99472238241212,
            "ttft_change_pct": -0.25182048192124995
          },
          "decode": {
            "e2e_change_pct": 2.1498150883991096,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7364413629671782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.8743167327896937,
            "ttft_change_pct": 6.956217810658671
          },
          "energy": {
            "e2e_change_pct": 0.13764392058108754,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4885955620544502,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.345494350587805,
            "ttft_change_pct": -0.3282459202156862
          },
          "filtering": {
            "e2e_change_pct": 1.2711684801022471,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0176526687201592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8247203555798999,
            "ttft_change_pct": 1.5773167419807166
          },
          "german": {
            "e2e_change_pct": -0.9938109270631212,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.45889586690850415,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.45471860117696217,
            "ttft_change_pct": -3.263325595507882
          },
          "ha_sim": {
            "e2e_change_pct": -0.24110884445305292,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3739903934454114,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.08004071592082607,
            "ttft_change_pct": -0.6825954027655179
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.25895901136445687,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.0697753311513605,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4054620298748923,
            "ttft_change_pct": -0.054928191510505986
          },
          "long_context": {
            "e2e_change_pct": -0.2731312071669101,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2686570720426662,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.24251443999142586,
            "ttft_change_pct": -0.37513194621342505
          },
          "math": {
            "e2e_change_pct": 2.0684536688096333,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4431178542527725,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.10777979579835728,
            "ttft_change_pct": 4.70262515746751
          },
          "prefill": {
            "e2e_change_pct": 6.453378123757125,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.0384774597558755,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.090823271076317,
            "ttft_change_pct": 6.45307605935892
          },
          "prefill2048": {
            "e2e_change_pct": 0.36360893384983495,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.220887488175082,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.35878368567476837,
            "ttft_change_pct": 0.3635357487297375
          },
          "prefill4096": {
            "e2e_change_pct": 0.812576419702471,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17728029377661603,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8028831753492782,
            "ttft_change_pct": 0.8142113813826013
          },
          "pve_sim": {
            "e2e_change_pct": -0.13504835281532568,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.628796588930904,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.180619831180584,
            "ttft_change_pct": -0.07970752240690215
          },
          "sorting": {
            "e2e_change_pct": 1.0945822014014617,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.588927146619827,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.177192180164599,
            "ttft_change_pct": 0.7563234337099933
          },
          "time": {
            "e2e_change_pct": 0.9505597285064837,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3898335903539274,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3298921926795262,
            "ttft_change_pct": 2.966237961846141
          },
          "tool-call": {
            "e2e_change_pct": 0.19240554784332176,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5616888809616758,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1596553605189066,
            "ttft_change_pct": 0.2145060807611232
          },
          "tool-final": {
            "e2e_change_pct": 0.10363198705620746,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.6881993433964144,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.018822121903283584,
            "ttft_change_pct": 0.1262200291109128
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 57.409167166054665,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 92.35439986015442,
            "exact_serial_matches": 24,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 10,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 14,
            "request_e2e_s": 3.4924535375,
            "wave_elapsed_s": 5.543862192000001,
            "waves": 6
          },
          "B": {
            "active_slots_max": 2,
            "aggregate_tokens_per_s": 145.37429166107702,
            "exact_serial_matches": 13,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 11,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 14,
            "request_e2e_s": 2.6647617415,
            "wave_elapsed_s": 3.521946986,
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
