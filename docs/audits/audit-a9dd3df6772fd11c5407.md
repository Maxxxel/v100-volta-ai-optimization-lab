# Public audit excerpt

Original SHA256: `a9dd3df6772fd11c540739098f8ae4458dccd0f31341b9ba3874cabe344c634f`

Original file: `RESULTS.json`; 56770 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6670927675,
              "format_passes": 2,
              "gpu_energy_j": 181.3851089225472,
              "semantic_passes": 2,
              "tokens_per_s": 79.2530309848913,
              "ttft_s": 0.124527649
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588669514999999,
              "format_passes": 0,
              "gpu_energy_j": 462.4042026019201,
              "semantic_passes": 0,
              "tokens_per_s": 79.60413562175638,
              "ttft_s": 0.06335959399999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2420803575,
              "format_passes": 2,
              "gpu_energy_j": 55.61500868754443,
              "semantic_passes": 2,
              "tokens_per_s": 77.18413418182885,
              "ttft_s": 0.0735716835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24506566600000002,
              "format_passes": 0,
              "gpu_energy_j": 60.03339323984507,
              "semantic_passes": 0,
              "tokens_per_s": 76.47288172437356,
              "ttft_s": 0.127284966
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1824819955,
              "format_passes": 2,
              "gpu_energy_j": 42.407373687995616,
              "semantic_passes": 2,
              "tokens_per_s": 77.44101070132591,
              "ttft_s": 0.06619680750000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.359052308,
              "format_passes": 0,
              "gpu_energy_j": 93.02244198497472,
              "semantic_passes": 0,
              "tokens_per_s": 78.57674568899748,
              "ttft_s": 0.0790630415
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46999413349999997,
              "format_passes": 0,
              "gpu_energy_j": 119.58404391628045,
              "semantic_passes": 2,
              "tokens_per_s": 79.01636525185003,
              "ttft_s": 0.11554845450000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0848110979999999,
              "format_passes": 2,
              "gpu_energy_j": 291.45317247186904,
              "semantic_passes": 2,
              "tokens_per_s": 77.82651068399821,
              "ttft_s": 0.8278503895
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23425543999999998,
              "format_passes": 0,
              "gpu_energy_j": 54.752349100082114,
              "semantic_passes": 0,
              "tokens_per_s": 78.03944819233732,
              "ttft_s": 0.067623891
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199647404,
              "format_passes": 0,
              "gpu_energy_j": 47.784876559629296,
              "semantic_passes": 0,
              "tokens_per_s": 2542.6857250775524,
              "ttft_s": 0.19950541249999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721309049,
              "format_passes": 0,
              "gpu_energy_j": 190.8041314143244,
              "semantic_passes": 0,
              "tokens_per_s": 2844.0359159246004,
              "ttft_s": 0.721092254
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4248169210000001,
              "format_passes": 0,
              "gpu_energy_j": 381.10918051397084,
              "semantic_passes": 0,
              "tokens_per_s": 2878.1940930219434,
              "ttft_s": 1.4244629115
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295074338,
              "format_passes": 2,
              "gpu_energy_j": 69.2345157767609,
              "semantic_passes": 2,
              "tokens_per_s": 78.66420211867427,
              "ttft_s": 0.078915078
            },
            "serialization-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.032909579,
              "format_passes": 0,
              "gpu_energy_j": 289.823925444974,
              "semantic_passes": 0,
              "tokens_per_s": 79.39152768920604
            },
            "serialization-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6019155650000001,
              "format_passes": 0,
              "gpu_energy_j": 160.36495943808322,
              "semantic_passes": 0,
              "tokens_per_s": 78.99350516459681
            },
            "serialization-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.719124645,
              "format_passes": 0,
              "gpu_energy_j": 198.5026266886738,
              "semantic_passes": 0,
              "tokens_per_s": 79.2912397410206
            },
            "serialization-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.722989772,
              "format_passes": 0,
              "gpu_energy_j": 192.9935160774195,
              "semantic_passes": 0,
              "tokens_per_s": 79.26181148548568
            },
            "serialization-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.828751248,
              "format_passes": 0,
              "gpu_energy_j": 210.76255239992582,
              "semantic_passes": 0,
              "tokens_per_s": 74.08542000315363
            },
            "serialization-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.219195952,
              "format_passes": 0,
              "gpu_energy_j": 329.15562075272504,
              "semantic_passes": 0,
              "tokens_per_s": 76.5995207299546
            },
            "serialization-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.793967781,
              "format_passes": 0,
              "gpu_energy_j": 484.26254128242056,
              "semantic_passes": 0,
              "tokens_per_s": 75.33473880117913
            },
            "serialization-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6010428225,
              "format_passes": 0,
              "gpu_energy_j": 157.43639456040336,
              "semantic_passes": 0,
              "tokens_per_s": 78.81575091300635
            },
            "serialization-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.039510599,
              "format_passes": 0,
              "gpu_energy_j": 265.2292857237116,
              "semantic_passes": 0,
              "tokens_per_s": 72.09275496752102
            },
            "serialization-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.727035124,
              "format_passes": 0,
              "gpu_energy_j": 196.40278610539912,
              "semantic_passes": 0,
              "tokens_per_s": 79.34165779615103
            },
            "serialization-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8246952535000001,
              "format_passes": 0,
              "gpu_energy_j": 220.137596057524,
              "semantic_passes": 0,
              "tokens_per_s": 75.75585983628622
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35657610250000005,
              "format_passes": 2,
              "gpu_energy_j": 90.72962239339583,
              "semantic_passes": 2,
              "tokens_per_s": 77.8882605242224,
              "ttft_s": 0.073986552
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3695615645,
              "format_passes": 2,
              "gpu_energy_j": 95.95312555828303,
              "semantic_passes": 2,
              "tokens_per_s": 78.94428047731259,
              "ttft_s": 0.07820993600000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.621637126,
              "format_passes": 0,
              "gpu_energy_j": 164.63581044242926,
              "semantic_passes": 0,
              "tokens_per_s": 78.89904756171599,
              "ttft_s": 0.320111993
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5619900369999999,
              "format_passes": 0,
              "gpu_energy_j": 147.38410256074275,
              "semantic_passes": 0,
              "tokens_per_s": 78.74804045270116,
              "ttft_s": 0.257128484
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
              "e2e_s": 0.6673487105,
              "format_passes": 2,
              "gpu_energy_j": 173.934550969908,
              "semantic_passes": 2,
              "tokens_per_s": 79.22777900759152,
              "ttft_s": 0.124556109
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658645996,
              "format_passes": 0,
              "gpu_energy_j": 466.53518954320725,
              "semantic_passes": 0,
              "tokens_per_s": 79.60760458370412,
              "ttft_s": 0.06309841599999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2431196165,
              "format_passes": 2,
              "gpu_energy_j": 60.587625089392546,
              "semantic_passes": 2,
              "tokens_per_s": 76.2676624210458,
              "ttft_s": 0.072535772
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24202481850000002,
              "format_passes": 0,
              "gpu_energy_j": 62.344132291154125,
              "semantic_passes": 0,
              "tokens_per_s": 77.27381714738058,
              "ttft_s": 0.1255025815
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1826765855,
              "format_passes": 2,
              "gpu_energy_j": 39.87527061149767,
              "semantic_passes": 2,
              "tokens_per_s": 77.47540274918336,
              "ttft_s": 0.066475645
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357869398,
              "format_passes": 0,
              "gpu_energy_j": 91.6343899399929,
              "semantic_passes": 0,
              "tokens_per_s": 78.81632368242745,
              "ttft_s": 0.07872928700000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46921230700000005,
              "format_passes": 0,
              "gpu_energy_j": 119.27561129932973,
              "semantic_passes": 2,
              "tokens_per_s": 79.05966877672648,
              "ttft_s": 0.1150431705
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.08421529,
              "format_passes": 2,
              "gpu_energy_j": 291.7596538814777,
              "semantic_passes": 2,
              "tokens_per_s": 77.81053104567377,
              "ttft_s": 0.8271473155
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2340492745,
              "format_passes": 0,
              "gpu_energy_j": 55.51054830711385,
              "semantic_passes": 0,
              "tokens_per_s": 78.0631424919014,
              "ttft_s": 0.0674936475
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200209372,
              "format_passes": 0,
              "gpu_energy_j": 49.28460524365208,
              "semantic_passes": 0,
              "tokens_per_s": 2535.6153644046353,
              "ttft_s": 0.2000745205
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7223190095,
              "format_passes": 0,
              "gpu_energy_j": 191.2601899989097,
              "semantic_passes": 0,
              "tokens_per_s": 2840.233771801491,
              "ttft_s": 0.7220426015
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4275850695,
              "format_passes": 0,
              "gpu_energy_j": 381.97345573276425,
              "semantic_passes": 0,
              "tokens_per_s": 2872.575738554426,
              "ttft_s": 1.4272865205
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295890216,
              "format_passes": 2,
              "gpu_energy_j": 73.94973219983675,
              "semantic_passes": 2,
              "tokens_per_s": 78.42965151315873,
              "ttft_s": 0.079082142
            },
            "serialization-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0318748795000001,
              "format_passes": 0,
              "gpu_energy_j": 281.4935742195494,
              "semantic_passes": 0,
              "tokens_per_s": 79.39850174921207
            },
            "serialization-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6020323670000001,
              "format_passes": 0,
              "gpu_energy_j": 160.07685278055112,
              "semantic_passes": 0,
              "tokens_per_s": 79.16655980269454
            },
            "serialization-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.723322758,
              "format_passes": 0,
              "gpu_energy_j": 197.40588100683837,
              "semantic_passes": 0,
              "tokens_per_s": 78.7172975507792
            },
            "serialization-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7235439260000001,
              "format_passes": 0,
              "gpu_energy_j": 192.9422937668826,
              "semantic_passes": 0,
              "tokens_per_s": 79.30727992538377
            },
            "serialization-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8311595865,
              "format_passes": 0,
              "gpu_energy_j": 215.9376557375018,
              "semantic_passes": 0,
              "tokens_per_s": 74.08312222533871
            },
            "serialization-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.219716612,
              "format_passes": 0,
              "gpu_energy_j": 322.2258500160839,
              "semantic_passes": 0,
              "tokens_per_s": 76.63801316510634
            },
            "serialization-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.797126542,
              "format_passes": 0,
              "gpu_energy_j": 482.1394273270856,
              "semantic_passes": 0,
              "tokens_per_s": 75.20938054547761
            },
            "serialization-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.601995402,
              "format_passes": 0,
              "gpu_energy_j": 160.62511583716196,
              "semantic_passes": 0,
              "tokens_per_s": 78.71038838584627
            },
            "serialization-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.04174491,
              "format_passes": 0,
              "gpu_energy_j": 270.44822954287247,
              "semantic_passes": 0,
              "tokens_per_s": 71.91833129185889
            },
            "serialization-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.728086875,
              "format_passes": 0,
              "gpu_energy_j": 199.09633097078213,
              "semantic_passes": 0,
              "tokens_per_s": 79.20835444393589
            },
            "serialization-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8256816155,
              "format_passes": 0,
              "gpu_energy_j": 221.22884415840213,
              "semantic_passes": 0,
              "tokens_per_s": 75.7073121202999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3533662195,
              "format_passes": 2,
              "gpu_energy_j": 90.62711400297799,
              "semantic_passes": 2,
              "tokens_per_s": 78.78569755142445,
              "ttft_s": 0.074133435
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.370186738,
              "format_passes": 2,
              "gpu_energy_j": 96.98489282885555,
              "semantic_passes": 2,
              "tokens_per_s": 78.76804687326253,
              "ttft_s": 0.07814270949999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6214245,
              "format_passes": 0,
              "gpu_energy_j": 164.04163032510496,
              "semantic_passes": 0,
              "tokens_per_s": 78.87975535641115,
              "ttft_s": 0.3198450215
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.563700292,
              "format_passes": 0,
              "gpu_energy_j": 147.38451494622126,
              "semantic_passes": 0,
              "tokens_per_s": 78.48626175482383,
              "ttft_s": 0.25783547
            }
          }
        }
      },
      "change_exercised": false,
      "complete": true,
      "serialization": {
        "arms": {
          "A": {
            "accepted_correct": 18,
            "argument_format_passes": 18,
            "argument_semantic_passes": 18,
            "consumer_accepts": 24,
            "median_consumer_us": 31.613500000000002,
            "median_pipeline_e2e_s": 0.8178305545,
            "median_serialization_us": 30.4045,
            "questions": 24,
            "starts": 2,
            "wire_bytes": 4116
          },
          "B": {
            "accepted_correct": 18,
            "argument_format_passes": 18,
            "argument_semantic_passes": 18,
            "consumer_accepts": 24,
            "median_consumer_us": 24.361,
            "median_pipeline_e2e_s": 0.82100785,
            "median_serialization_us": 62.765,
            "questions": 24,
            "starts": 2,
            "wire_bytes": 3914
          }
        },
        "change_exercised": true,
        "note": "Same12 frozen questions, identical tools/schema/native generation across modes. Strict is real typed canonical serialization, not an ignored strict request flag or a change to native constrained decoding. Validator checks before unchanged native delivery. Common kernel speed is excluded. Timed production request+local serialization/consumer; diagnostics, render/tokenizer and quality oracle excluded. Loaded service/cold KV after same diagnostic. Original raw answers and serialized acceptance separate. Server call IDs remain intact in delivery; input matching ignores their random characters but requires equal UTF-8 byte length. Mismatched native input or inactive path keeps quality visible without a percent gain. Two starts/arm; no significance claim.",
        "original_quality": {
          "A": {
            "attempts": 24,
            "passes": 18
          },
          "B": {
            "attempts": 24,
            "passes": 18
          }
        },
        "paired_pipeline_e2e_change_pct": 0.06179330170321684,
        "pipeline_speed_gain_eligible": true
      }
    }
  }
}
```

</details>
