# Public audit excerpt

Original SHA256: `18dc1be39488dec98ef84689a0285e21d6f852feacb875aa9c9b1ae9000d5710`

Original file: `RESULTS.json`; 40926 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen38": {
      "arms": {
        "A": {
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.8323644285,
              "format_passes": 2,
              "gpu_energy_j": 490.9468272030614,
              "semantic_passes": 2,
              "tokens_per_s": 33.55382399989303,
              "ttft_s": 0.5209820185
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.981020903,
              "format_passes": 0,
              "gpu_energy_j": 1094.6015355454742,
              "semantic_passes": 0,
              "tokens_per_s": 33.580693805880905,
              "ttft_s": 0.198064549
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6032462245,
              "format_passes": 2,
              "gpu_energy_j": 145.26421361283437,
              "semantic_passes": 2,
              "tokens_per_s": 33.102796249462855,
              "ttft_s": 0.21051533649999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9484839119999999,
              "format_passes": 0,
              "gpu_energy_j": 245.0053561034681,
              "semantic_passes": 0,
              "tokens_per_s": 33.15317011131806,
              "ttft_s": 0.526136582
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.484024272,
              "format_passes": 2,
              "gpu_energy_j": 111.16292151757338,
              "semantic_passes": 2,
              "tokens_per_s": 32.46665418534656,
              "ttft_s": 0.20678131500000002
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8870747800000001,
              "format_passes": 0,
              "gpu_energy_j": 234.20133058338013,
              "semantic_passes": 0,
              "tokens_per_s": 33.34138454879648,
              "ttft_s": 0.227236886
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1934709505,
              "format_passes": 0,
              "gpu_energy_j": 299.790264939973,
              "semantic_passes": 2,
              "tokens_per_s": 33.45159098205445,
              "ttft_s": 0.356373748
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.826019723,
              "format_passes": 2,
              "gpu_energy_j": 1020.2805260985168,
              "semantic_passes": 2,
              "tokens_per_s": 32.708189345570226,
              "ttft_s": 3.214515011
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5967288584999999,
              "format_passes": 2,
              "gpu_energy_j": 146.4966048532242,
              "semantic_passes": 2,
              "tokens_per_s": 33.13189298722102,
              "ttft_s": 0.20426704950000002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.728720898,
              "format_passes": 0,
              "gpu_energy_j": 189.23382356923668,
              "semantic_passes": 0,
              "tokens_per_s": 693.9963823228738,
              "ttft_s": 0.728583545
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.753515523,
              "format_passes": 0,
              "gpu_energy_j": 732.8228208265359,
              "semantic_passes": 0,
              "tokens_per_s": 744.1755114454504,
              "ttft_s": 2.7532680999999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.468656184,
              "format_passes": 0,
              "gpu_energy_j": 1482.5358969549447,
              "semantic_passes": 0,
              "tokens_per_s": 749.2352627983701,
              "ttft_s": 5.468358974999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7352785115,
              "format_passes": 2,
              "gpu_energy_j": 186.67564757618425,
              "semantic_passes": 2,
              "tokens_per_s": 33.27717162631226,
              "ttft_s": 0.224393585
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.029640767,
              "format_passes": 0,
              "gpu_energy_j": 262.1113347274194,
              "semantic_passes": 2,
              "tokens_per_s": 33.177711524569176,
              "ttft_s": 0.21579967849999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.060316915,
              "format_passes": 0,
              "gpu_energy_j": 279.00462795540363,
              "semantic_passes": 2,
              "tokens_per_s": 33.40640940404755,
              "ttft_s": 0.22207551650000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7614349,
              "format_passes": 0,
              "gpu_energy_j": 465.1531695513751,
              "semantic_passes": 0,
              "tokens_per_s": 33.25175017220478,
              "ttft_s": 1.0468981935000001
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8183246675,
              "format_passes": 0,
              "gpu_energy_j": 470.92473337004503,
              "semantic_passes": 0,
              "tokens_per_s": 33.26210338861159,
              "ttft_s": 1.0976699355
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
              "e2e_s": 1.8607291825,
              "format_passes": 2,
              "gpu_energy_j": 499.21569433761545,
              "semantic_passes": 2,
              "tokens_per_s": 32.88094754948314,
              "ttft_s": 0.5224842085
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 4.0341146755,
              "format_passes": 0,
              "gpu_energy_j": 1104.0180386947827,
              "semantic_passes": 0,
              "tokens_per_s": 33.09265612174687,
              "ttft_s": 0.195745766
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.61106775,
              "format_passes": 2,
              "gpu_energy_j": 149.55906827850805,
              "semantic_passes": 2,
              "tokens_per_s": 32.57806709392265,
              "ttft_s": 0.21201738399999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0456380324999999,
              "format_passes": 0,
              "gpu_energy_j": 274.2861589168073,
              "semantic_passes": 0,
              "tokens_per_s": 32.759637765864284,
              "ttft_s": 0.5266749799999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.486838198,
              "format_passes": 2,
              "gpu_energy_j": 112.399376947355,
              "semantic_passes": 2,
              "tokens_per_s": 32.04119485953005,
              "ttft_s": 0.2059139685
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0441050765000002,
              "format_passes": 0,
              "gpu_energy_j": 277.127880724537,
              "semantic_passes": 0,
              "tokens_per_s": 33.009797513707184,
              "ttft_s": 0.226090495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2028748425,
              "format_passes": 0,
              "gpu_energy_j": 309.1504617133402,
              "semantic_passes": 2,
              "tokens_per_s": 33.032233844243294,
              "ttft_s": 0.355172289
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8470580905,
              "format_passes": 2,
              "gpu_energy_j": 1030.7745399725802,
              "semantic_passes": 2,
              "tokens_per_s": 32.0792752957435,
              "ttft_s": 3.2235877085
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6030404005,
              "format_passes": 2,
              "gpu_energy_j": 151.22886591515862,
              "semantic_passes": 2,
              "tokens_per_s": 32.680734035738226,
              "ttft_s": 0.20517353
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7288025895,
              "format_passes": 0,
              "gpu_energy_j": 187.73003488548747,
              "semantic_passes": 0,
              "tokens_per_s": 693.8912041960044,
              "ttft_s": 0.7286629410000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7574268269999997,
              "format_passes": 0,
              "gpu_energy_j": 738.2835857117244,
              "semantic_passes": 0,
              "tokens_per_s": 743.0791326025267,
              "ttft_s": 2.757186461
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.480142832,
              "format_passes": 0,
              "gpu_energy_j": 1480.222304578202,
              "semantic_passes": 0,
              "tokens_per_s": 747.6813439979004,
              "ttft_s": 5.4797900765000005
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.893705467,
              "format_passes": 0,
              "gpu_energy_j": 234.13963581795457,
              "semantic_passes": 2,
              "tokens_per_s": 32.86236752030432,
              "ttft_s": 0.22417175649999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.039268067,
              "format_passes": 0,
              "gpu_energy_j": 268.2401257564966,
              "semantic_passes": 2,
              "tokens_per_s": 32.84645761736081,
              "ttft_s": 0.217206869
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0713633470000001,
              "format_passes": 0,
              "gpu_energy_j": 282.32434710826345,
              "semantic_passes": 2,
              "tokens_per_s": 32.96639085713058,
              "ttft_s": 0.22194001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.77577219,
              "format_passes": 0,
              "gpu_energy_j": 469.9200783541412,
              "semantic_passes": 0,
              "tokens_per_s": 32.77127483280088,
              "ttft_s": 1.0514361765
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8290042095,
              "format_passes": 0,
              "gpu_energy_j": 474.72850383899925,
              "semantic_passes": 0,
              "tokens_per_s": 32.80292929203151,
              "ttft_s": 1.0970741725
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": -2,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 1.5479865008741545,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6842693905696482,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.00536442705318,
            "ttft_change_pct": 0.28833816651197
          },
          "decode": {
            "e2e_change_pct": 1.333672286422538,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8602676721640057,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4533281740848558,
            "ttft_change_pct": -1.1707208643380262
          },
          "energy": {
            "e2e_change_pct": 1.2965726402155209,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9565813622345782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.5851505461527915,
            "ttft_change_pct": 0.713509773194132
          },
          "filtering": {
            "e2e_change_pct": 10.243096300404076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.951086816638279,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 0.10233046292908998
          },
          "german": {
            "e2e_change_pct": 0.5813605149123546,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.112291232455731,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.3104501726221573,
            "ttft_change_pct": -0.4194510998249634
          },
          "ha_sim": {
            "e2e_change_pct": 17.702035954623806,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 18.32890958997957,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -0.5044915991323728
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.7879447753680324,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1222484076463886,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2536238950073386,
            "ttft_change_pct": -0.3371345411222637
          },
          "long_context": {
            "e2e_change_pct": 0.5498760859367291,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0285420142430723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.9228030117536932,
            "ttft_change_pct": 0.2822415658024102
          },
          "math": {
            "e2e_change_pct": 1.0576900899121,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2302871910756537,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.3617059298628331,
            "ttft_change_pct": 0.4437722590201476
          },
          "prefill": {
            "e2e_change_pct": 0.011210258992733202,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7946722501218195,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.015155428695090567,
            "ttft_change_pct": 0.010897308969570751
          },
          "prefill2048": {
            "e2e_change_pct": 0.1420476466295062,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7451685086757198,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.14732799266589103,
            "ttft_change_pct": 0.14231672534905648
          },
          "prefill4096": {
            "e2e_change_pct": 0.2100451667377934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.15605641532826509,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.20740064938559177,
            "ttft_change_pct": 0.20904080277577286
          },
          "pve_sim": {
            "e2e_change_pct": 21.546523259166396,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 25.425913266163857,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -0.0988568813141466
          },
          "sorting": {
            "e2e_change_pct": 0.9350154256275722,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3382396016756735,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9984230134831962,
            "ttft_change_pct": 0.6520818333842104
          },
          "time": {
            "e2e_change_pct": 1.041804751365305,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.189843758932363,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.317168036812899,
            "ttft_change_pct": -0.06101820774107036
          },
          "tool-call": {
            "e2e_change_pct": 0.8139551453193006,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0248041107327355,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4449625566041124,
            "ttft_change_pct": 0.4334693696268932
          },
          "tool-final": {
            "e2e_change_pct": 0.5873286652753551,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8077236550591671,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.380472218534734,
            "ttft_change_pct": -0.054275240737877706
          }
        }
      },
      "complete": true
    }
  }
}
```
