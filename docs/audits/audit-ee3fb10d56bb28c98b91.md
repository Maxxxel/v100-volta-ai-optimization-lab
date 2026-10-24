# Public audit excerpt

Original SHA256: `ee3fb10d56bb28c98b915030e56384f184c126f3e3dab84b94dcbef8a049b9a7`

Original file: `RESULTS.json`; 46235 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7887343205,
              "format_passes": 2,
              "gpu_energy_j": 487.2943151726711,
              "semantic_passes": 2,
              "tokens_per_s": 35.387653617847945,
              "ttft_s": 0.541380761
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 9.5286376675,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 35.28713879394596,
              "ttft_s": 5.924379716500001
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.5207193290000003,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 35.03646112199243,
              "ttft_s": 1.677734048
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7839600965,
              "format_passes": 0,
              "gpu_energy_j": 1067.2783827785,
              "semantic_passes": 0,
              "tokens_per_s": 35.38856858805635,
              "ttft_s": 0.19562454899999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5945300840000001,
              "format_passes": 2,
              "gpu_energy_j": 146.75298706290158,
              "semantic_passes": 2,
              "tokens_per_s": 34.828130350172124,
              "ttft_s": 0.218915838
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9400269935000001,
              "format_passes": 0,
              "gpu_energy_j": 242.88060478978102,
              "semantic_passes": 0,
              "tokens_per_s": 34.93968711133235,
              "ttft_s": 0.5380598185000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4909649545,
              "format_passes": 2,
              "gpu_energy_j": 110.70450710530689,
              "semantic_passes": 2,
              "tokens_per_s": 33.68758426888772,
              "ttft_s": 0.22054513
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0221611505,
              "format_passes": 0,
              "gpu_energy_j": 270.1457997307066,
              "semantic_passes": 0,
              "tokens_per_s": 35.12465931632326,
              "ttft_s": 0.2516480245
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.167671312,
              "format_passes": 0,
              "gpu_energy_j": 297.7992386992602,
              "semantic_passes": 2,
              "tokens_per_s": 35.11085301486246,
              "ttft_s": 0.3672900495
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8006530235,
              "format_passes": 2,
              "gpu_energy_j": 1020.0904811810453,
              "semantic_passes": 2,
              "tokens_per_s": 34.256307944018154,
              "ttft_s": 3.214443406
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5826705755,
              "format_passes": 2,
              "gpu_energy_j": 145.3657201578519,
              "semantic_passes": 2,
              "tokens_per_s": 34.95459942610487,
              "ttft_s": 0.209748435
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.722739051,
              "format_passes": 0,
              "gpu_energy_j": 189.58257985727556,
              "semantic_passes": 0,
              "tokens_per_s": 699.9662295993062,
              "ttft_s": 0.722555871
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7491683925,
              "format_passes": 0,
              "gpu_energy_j": 734.2472272671738,
              "semantic_passes": 0,
              "tokens_per_s": 745.299900249652,
              "ttft_s": 2.7489227475
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.457315555,
              "format_passes": 0,
              "gpu_energy_j": 1485.6923119356538,
              "semantic_passes": 0,
              "tokens_per_s": 750.8143204246445,
              "ttft_s": 5.4569682365
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.86473548,
              "format_passes": 0,
              "gpu_energy_j": 224.88988767232374,
              "semantic_passes": 2,
              "tokens_per_s": 35.23486609047343,
              "ttft_s": 0.23801940500000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9956632955,
              "format_passes": 0,
              "gpu_energy_j": 264.92580289855846,
              "semantic_passes": 2,
              "tokens_per_s": 34.99716065227524,
              "ttft_s": 0.2190574075
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0258766145,
              "format_passes": 0,
              "gpu_energy_j": 269.9149506348731,
              "semantic_passes": 2,
              "tokens_per_s": 35.25608706014072,
              "ttft_s": 0.230599433
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.707954062,
              "format_passes": 0,
              "gpu_energy_j": 461.286170398934,
              "semantic_passes": 0,
              "tokens_per_s": 35.04408977361287,
              "ttft_s": 1.0303203965
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.780430921,
              "format_passes": 0,
              "gpu_energy_j": 468.78115467127236,
              "semantic_passes": 0,
              "tokens_per_s": 35.05209173825912,
              "ttft_s": 1.09564303
            }
          }
        },
        "B": {
          "format_passes": 8,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.7760921905,
              "format_passes": 2,
              "gpu_energy_j": 487.0198100413423,
              "semantic_passes": 2,
              "tokens_per_s": 35.12610983595384,
              "ttft_s": 0.523406991
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 7.237725660000001,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 20.839762004416034,
              "ttft_s": 1.149678004
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.8784722699999996,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 20.68918751762334,
              "ttft_s": 1.6483763405
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.897968208,
              "format_passes": 0,
              "gpu_energy_j": 1108.2210135415967,
              "semantic_passes": 0,
              "tokens_per_s": 34.3270011359769,
              "ttft_s": 0.197756011
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7377796919999999,
              "format_passes": 0,
              "gpu_energy_j": 196.25241968526944,
              "semantic_passes": 2,
              "tokens_per_s": 34.658375193684535,
              "ttft_s": 0.2184050665
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9403119665,
              "format_passes": 0,
              "gpu_energy_j": 249.4567702513429,
              "semantic_passes": 0,
              "tokens_per_s": 34.389759399579205,
              "ttft_s": 0.5331894239999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4511250745,
              "format_passes": 2,
              "gpu_energy_j": 109.5642392018215,
              "semantic_passes": 2,
              "tokens_per_s": 34.52800571073935,
              "ttft_s": 0.1904386455
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.002861563,
              "format_passes": 0,
              "gpu_energy_j": 266.93490170842404,
              "semantic_passes": 0,
              "tokens_per_s": 35.06456160937566,
              "ttft_s": 0.2327808585
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1484445939999999,
              "format_passes": 0,
              "gpu_energy_j": 302.3740547213024,
              "semantic_passes": 2,
              "tokens_per_s": 35.22812370827723,
              "ttft_s": 0.3535763015
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.9526029995,
              "format_passes": 0,
              "gpu_energy_j": 1072.2224879390697,
              "semantic_passes": 2,
              "tokens_per_s": 34.49837261732537,
              "ttft_s": 3.2279242655
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5767640635,
              "format_passes": 2,
              "gpu_energy_j": 146.64623263323523,
              "semantic_passes": 2,
              "tokens_per_s": 34.77931916642871,
              "ttft_s": 0.20293929649999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.769364434,
              "format_passes": 0,
              "gpu_energy_j": 199.62015341951906,
              "semantic_passes": 0,
              "tokens_per_s": 657.2978922687342,
              "ttft_s": 0.7692277675
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.803317205,
              "format_passes": 0,
              "gpu_energy_j": 746.1141016011445,
              "semantic_passes": 0,
              "tokens_per_s": 730.9376658355526,
              "ttft_s": 2.8030369375
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.578395538500001,
              "format_passes": 0,
              "gpu_energy_j": 1508.3643851840357,
              "semantic_passes": 0,
              "tokens_per_s": 734.5014746903938
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.851957611,
              "format_passes": 0,
              "gpu_energy_j": 234.05380164917722,
              "semantic_passes": 2,
              "tokens_per_s": 34.97709825794152,
              "ttft_s": 0.222932727
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9874202489999999,
              "format_passes": 0,
              "gpu_energy_j": 268.5804858751211,
              "semantic_passes": 2,
              "tokens_per_s": 34.79882923294863,
              "ttft_s": 0.21149737000000002
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015827276,
              "format_passes": 0,
              "gpu_energy_j": 278.5315835275577,
              "semantic_passes": 2,
              "tokens_per_s": 35.195953555534125,
              "ttft_s": 0.220237762
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7810579055,
              "format_passes": 0,
              "gpu_energy_j": 481.1035256724167,
              "semantic_passes": 0,
              "tokens_per_s": 34.18417582751486,
              "ttft_s": 1.083249873
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8476338554999998,
              "format_passes": 0,
              "gpu_energy_j": 486.7090524251632,
              "semantic_passes": 0,
              "tokens_per_s": 34.093754814117844,
              "ttft_s": 1.1435997245
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": -4,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.7067639869774545,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.05633251256614846,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7390820106880303,
            "ttft_change_pct": -3.319986836399602
          },
          "concurrent-decode": {
            "e2e_change_pct": -24.04238766800605,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -40.94232993469164,
            "ttft_change_pct": -80.59412024522956
          },
          "concurrent-quality": {
            "e2e_change_pct": 14.192494058508466,
            "format_pass_change": 0,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -1.7498427438482733
          },
          "decode": {
            "e2e_change_pct": 3.012931124867113,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.8361716515337596,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.9997467951776158,
            "ttft_change_pct": 1.0895677515402324
          },
          "energy": {
            "e2e_change_pct": 24.094593672403608,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 33.72976156263947,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -0.23331866011448987
          },
          "filtering": {
            "e2e_change_pct": 0.030315406043701643,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.707571264182951,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5739342770896725,
            "ttft_change_pct": -0.9051771443513101
          },
          "german": {
            "e2e_change_pct": -8.11460769956035,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0300103702198138,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.4947512862411036,
            "ttft_change_pct": -13.650940512719556
          },
          "ha_sim": {
            "e2e_change_pct": -1.888115928741707,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.188579657904476,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.17109833409736375,
            "ttft_change_pct": -7.497442524131559
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.6465864839197208,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5362080984572923,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.33400126554923304,
            "ttft_change_pct": -3.733765186034521
          },
          "long_context": {
            "e2e_change_pct": 3.9979965300823483,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 5.1105277149205985,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 0.4193839429506463
          },
          "math": {
            "e2e_change_pct": -1.0136966320860696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8808902635317528,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5014512040016683,
            "ttft_change_pct": -3.2463357831490014
          },
          "prefill": {
            "e2e_change_pct": 6.451205720167996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.294565339178381,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.095770842401538,
            "ttft_change_pct": 6.459278565601756
          },
          "prefill2048": {
            "e2e_change_pct": 1.9696433527943702,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6161960022836652,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.9270409682449308,
            "ttft_change_pct": 1.9685598676504767
          },
          "prefill4096": {
            "e2e_change_pct": 2.218672940564459,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5260275001923729,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.172687079946012
          },
          "pve_sim": {
            "e2e_change_pct": -1.4776621632316966,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.074844837045655,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7315703481603597,
            "ttft_change_pct": -6.3384235415595676
          },
          "sorting": {
            "e2e_change_pct": -0.8278949859109375,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3795118997759648,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.566707171753722,
            "ttft_change_pct": -3.4511672471062127
          },
          "time": {
            "e2e_change_pct": -0.979585493806967,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.192351098898838,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.17056204933922903,
            "ttft_change_pct": -4.493363606839395
          },
          "tool-call": {
            "e2e_change_pct": 4.280199633378667,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.296108694597112,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.4538059103635046,
            "ttft_change_pct": 5.1371861296545696
          },
          "tool-final": {
            "e2e_change_pct": 3.7745319802834354,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.8243640076492724,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.7340363345428,
            "ttft_change_pct": 4.3770364239893
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 109.78207135471752,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 33.67259213173904,
            "exact_serial_matches": 24,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 12,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 20,
            "request_e2e_s": 9.5286376675,
            "wave_elapsed_s": 15.205247297500001,
            "waves": 6
          },
          "B": {
            "active_slots_max": 4,
            "aggregate_tokens_per_s": 70.63906125278778,
            "exact_serial_matches": 23,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 10,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 20,
            "request_e2e_s": 7.237725660000001,
            "wave_elapsed_s": 7.2481172975,
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

</details>
