# Public audit excerpt

Original SHA256: `7d4ff4b9c907940cedab784f1c0305595f3d26c5c12e385770d8e92cc82cc6e8`

Original file: `RESULTS.json`; 56743 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.66754592,
              "format_passes": 2,
              "gpu_energy_j": 179.79189544437043,
              "semantic_passes": 2,
              "tokens_per_s": 79.1269074141266,
              "ttft_s": 0.12412139650000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6595385805,
              "format_passes": 0,
              "gpu_energy_j": 461.99237057356436,
              "semantic_passes": 0,
              "tokens_per_s": 79.58071643922848,
              "ttft_s": 0.063518657
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237986458,
              "format_passes": 2,
              "gpu_energy_j": 57.225106153943514,
              "semantic_passes": 2,
              "tokens_per_s": 78.30007952375996,
              "ttft_s": 0.07189719
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241715348,
              "format_passes": 0,
              "gpu_energy_j": 57.34606595106992,
              "semantic_passes": 0,
              "tokens_per_s": 77.63212568732588,
              "ttft_s": 0.1257429625
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1824664305,
              "format_passes": 2,
              "gpu_energy_j": 40.35428309865493,
              "semantic_passes": 2,
              "tokens_per_s": 77.5354495109077,
              "ttft_s": 0.0663559135
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3585077345,
              "format_passes": 0,
              "gpu_energy_j": 91.55175630479505,
              "semantic_passes": 0,
              "tokens_per_s": 78.81253241645925,
              "ttft_s": 0.07934344
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4693140655,
              "format_passes": 0,
              "gpu_energy_j": 120.96232788114722,
              "semantic_passes": 2,
              "tokens_per_s": 79.06701179274049,
              "ttft_s": 0.1151450395
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.086574551,
              "format_passes": 2,
              "gpu_energy_j": 288.6419090931041,
              "semantic_passes": 2,
              "tokens_per_s": 77.78121485844594,
              "ttft_s": 0.829437287
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23358862,
              "format_passes": 0,
              "gpu_energy_j": 54.60171459881534,
              "semantic_passes": 0,
              "tokens_per_s": 78.24514300010763,
              "ttft_s": 0.06741519600000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199790414,
              "format_passes": 0,
              "gpu_energy_j": 48.006654753161236,
              "semantic_passes": 0,
              "tokens_per_s": 2541.7653420387887,
              "ttft_s": 0.1996140205
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7214171355000001,
              "format_passes": 0,
              "gpu_energy_j": 192.14960014102058,
              "semantic_passes": 0,
              "tokens_per_s": 2843.720889179661,
              "ttft_s": 0.721156066
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4263960835,
              "format_passes": 0,
              "gpu_energy_j": 384.82037063078326,
              "semantic_passes": 0,
              "tokens_per_s": 2875.0164547328695,
              "ttft_s": 1.426081829
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2958345995,
              "format_passes": 2,
              "gpu_energy_j": 73.40831145651143,
              "semantic_passes": 2,
              "tokens_per_s": 78.47426447895043,
              "ttft_s": 0.07913658200000001
            },
            "serialization-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0351284995,
              "format_passes": 0,
              "gpu_energy_j": 284.88554455457836,
              "semantic_passes": 0,
              "tokens_per_s": 79.32156257202433
            },
            "serialization-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.602262979,
              "format_passes": 0,
              "gpu_energy_j": 158.97626436979084,
              "semantic_passes": 0,
              "tokens_per_s": 79.04272254522367
            },
            "serialization-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7196102685,
              "format_passes": 0,
              "gpu_energy_j": 192.29443774799904,
              "semantic_passes": 0,
              "tokens_per_s": 79.20588044158123
            },
            "serialization-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7240877370000001,
              "format_passes": 0,
              "gpu_energy_j": 195.45134449874922,
              "semantic_passes": 0,
              "tokens_per_s": 79.19209491658957
            },
            "serialization-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8307546475,
              "format_passes": 0,
              "gpu_energy_j": 214.8419178470874,
              "semantic_passes": 0,
              "tokens_per_s": 73.779266195991
            },
            "serialization-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.220807382,
              "format_passes": 0,
              "gpu_energy_j": 319.8773816833519,
              "semantic_passes": 0,
              "tokens_per_s": 76.57900758522837
            },
            "serialization-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.796308095,
              "format_passes": 0,
              "gpu_energy_j": 492.32892981655203,
              "semantic_passes": 0,
              "tokens_per_s": 75.21249880234689
            },
            "serialization-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.598865005,
              "format_passes": 0,
              "gpu_energy_j": 160.41878751037603,
              "semantic_passes": 0,
              "tokens_per_s": 79.12152404531663
            },
            "serialization-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.036243981,
              "format_passes": 0,
              "gpu_energy_j": 267.3537342428054,
              "semantic_passes": 0,
              "tokens_per_s": 72.318014358184
            },
            "serialization-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7285602275,
              "format_passes": 0,
              "gpu_energy_j": 195.6996823641785,
              "semantic_passes": 0,
              "tokens_per_s": 79.14394984799979
            },
            "serialization-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.826197442,
              "format_passes": 0,
              "gpu_energy_j": 219.28139375736387,
              "semantic_passes": 0,
              "tokens_per_s": 75.67164792948836
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354003236,
              "format_passes": 2,
              "gpu_energy_j": 90.92759259730634,
              "semantic_passes": 2,
              "tokens_per_s": 78.72424496877503,
              "ttft_s": 0.074544643
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691920195,
              "format_passes": 2,
              "gpu_energy_j": 96.6969888445426,
              "semantic_passes": 2,
              "tokens_per_s": 78.92605678880425,
              "ttft_s": 0.0777447915
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.622264922,
              "format_passes": 0,
              "gpu_energy_j": 165.67040241996426,
              "semantic_passes": 0,
              "tokens_per_s": 78.92131364433052,
              "ttft_s": 0.32046744
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5626562405,
              "format_passes": 0,
              "gpu_energy_j": 143.28796551434948,
              "semantic_passes": 0,
              "tokens_per_s": 78.77570673929118,
              "ttft_s": 0.2579331585
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
              "e2e_s": 0.6674201559999999,
              "format_passes": 2,
              "gpu_energy_j": 179.48682131781158,
              "semantic_passes": 2,
              "tokens_per_s": 79.19867752630253,
              "ttft_s": 0.1244383065
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.66027821,
              "format_passes": 0,
              "gpu_energy_j": 463.0100964131489,
              "semantic_passes": 0,
              "tokens_per_s": 79.53374558733267,
              "ttft_s": 0.063380389
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2380939365,
              "format_passes": 2,
              "gpu_energy_j": 55.47670209431085,
              "semantic_passes": 2,
              "tokens_per_s": 78.25668209817877,
              "ttft_s": 0.07190536850000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242116425,
              "format_passes": 0,
              "gpu_energy_j": 58.45075769166294,
              "semantic_passes": 0,
              "tokens_per_s": 77.45942034496554,
              "ttft_s": 0.1259212395
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182283541,
              "format_passes": 2,
              "gpu_energy_j": 41.119758615411484,
              "semantic_passes": 2,
              "tokens_per_s": 77.55279395236212,
              "ttft_s": 0.0662054675
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357848823,
              "format_passes": 0,
              "gpu_energy_j": 92.7897524809641,
              "semantic_passes": 0,
              "tokens_per_s": 78.89377492281287,
              "ttft_s": 0.078952979
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4706168615,
              "format_passes": 0,
              "gpu_energy_j": 117.83076563995246,
              "semantic_passes": 2,
              "tokens_per_s": 78.8304225826436,
              "ttft_s": 0.1153927615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0837629670000002,
              "format_passes": 2,
              "gpu_energy_j": 289.88246167150817,
              "semantic_passes": 2,
              "tokens_per_s": 77.83500943381047,
              "ttft_s": 0.8267664145
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23397899900000002,
              "format_passes": 0,
              "gpu_energy_j": 57.43106327096096,
              "semantic_passes": 0,
              "tokens_per_s": 78.254108954857,
              "ttft_s": 0.067767577
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20052900499999998,
              "format_passes": 0,
              "gpu_energy_j": 48.04333133091965,
              "semantic_passes": 0,
              "tokens_per_s": 2531.3411557666054,
              "ttft_s": 0.20039090199999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721930742,
              "format_passes": 0,
              "gpu_energy_j": 189.8906937429174,
              "semantic_passes": 0,
              "tokens_per_s": 2841.704087577613,
              "ttft_s": 0.7216837255
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4295582165,
              "format_passes": 0,
              "gpu_energy_j": 381.8177138276481,
              "semantic_passes": 0,
              "tokens_per_s": 2868.649982498413,
              "ttft_s": 1.4292393725
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295488553,
              "format_passes": 2,
              "gpu_energy_j": 70.2269520178958,
              "semantic_passes": 2,
              "tokens_per_s": 78.58921742804819,
              "ttft_s": 0.0791115685
            },
            "serialization-diagnostic-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0300578935,
              "format_passes": 0,
              "gpu_energy_j": 288.7807015645642,
              "semantic_passes": 0,
              "tokens_per_s": 79.59601829196845
            },
            "serialization-diagnostic-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.601762578,
              "format_passes": 0,
              "gpu_energy_j": 159.51375853721777,
              "semantic_passes": 0,
              "tokens_per_s": 78.99028047003021
            },
            "serialization-diagnostic-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.719679614,
              "format_passes": 0,
              "gpu_energy_j": 195.06084689906342,
              "semantic_passes": 0,
              "tokens_per_s": 79.15997148828441
            },
            "serialization-diagnostic-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7250176095,
              "format_passes": 0,
              "gpu_energy_j": 194.1515764196658,
              "semantic_passes": 0,
              "tokens_per_s": 79.09018881394084
            },
            "serialization-diagnostic-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8296518065,
              "format_passes": 0,
              "gpu_energy_j": 216.7420405086244,
              "semantic_passes": 0,
              "tokens_per_s": 73.99575994630402
            },
            "serialization-diagnostic-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.223223359,
              "format_passes": 0,
              "gpu_energy_j": 326.45083304445825,
              "semantic_passes": 0,
              "tokens_per_s": 76.30926522356094
            },
            "serialization-diagnostic-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.794690497,
              "format_passes": 0,
              "gpu_energy_j": 485.48732465766375,
              "semantic_passes": 0,
              "tokens_per_s": 75.34038023733933
            },
            "serialization-diagnostic-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5980657335,
              "format_passes": 0,
              "gpu_energy_j": 157.750366173261,
              "semantic_passes": 0,
              "tokens_per_s": 79.14321464362354
            },
            "serialization-diagnostic-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.038709758,
              "format_passes": 0,
              "gpu_energy_j": 269.76603149212855,
              "semantic_passes": 0,
              "tokens_per_s": 72.13485550107383
            },
            "serialization-diagnostic-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7279126975000001,
              "format_passes": 0,
              "gpu_energy_j": 201.1904433711956,
              "semantic_passes": 0,
              "tokens_per_s": 79.21844477060026
            },
            "serialization-diagnostic-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8246843079999999,
              "format_passes": 0,
              "gpu_energy_j": 217.18000454236778,
              "semantic_passes": 0,
              "tokens_per_s": 75.8547703893923
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353206199,
              "format_passes": 2,
              "gpu_energy_j": 92.45609358387023,
              "semantic_passes": 2,
              "tokens_per_s": 78.86055809047707,
              "ttft_s": 0.07422442600000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3688494405,
              "format_passes": 2,
              "gpu_energy_j": 95.85648534043023,
              "semantic_passes": 2,
              "tokens_per_s": 78.97389768004135,
              "ttft_s": 0.0775975935
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6214875695,
              "format_passes": 0,
              "gpu_energy_j": 164.0858050456053,
              "semantic_passes": 0,
              "tokens_per_s": 78.96758392943877,
              "ttft_s": 0.31929854599999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5617323635,
              "format_passes": 0,
              "gpu_energy_j": 146.62792403734562,
              "semantic_passes": 0,
              "tokens_per_s": 78.77957385187852,
              "ttft_s": 0.25700272
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
            "median_consumer_us": 31.2515,
            "median_pipeline_e2e_s": 0.8189344519999999,
            "median_serialization_us": 31.0925,
            "questions": 24,
            "starts": 2,
            "wire_bytes": 4116
          },
          "B": {
            "accepted_correct": 18,
            "argument_format_passes": 18,
            "argument_semantic_passes": 18,
            "consumer_accepts": 24,
            "median_consumer_us": 23.628999999999998,
            "median_pipeline_e2e_s": 0.819501909,
            "median_serialization_us": 49.6235,
            "questions": 24,
            "starts": 2,
            "wire_bytes": 4116
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
        "paired_pipeline_e2e_change_pct": 0.011405481292547925,
        "pipeline_speed_gain_eligible": true
      }
    }
  }
}
```
