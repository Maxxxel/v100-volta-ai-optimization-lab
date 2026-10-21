# Public audit excerpt

Original SHA256: `e53af2194be20b8e11da6627b6986e47bc72b8111874bef781843b56d49df951`

Original file: `RESULTS.json`; 61407 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6660988219999999,
              "format_passes": 2,
              "gpu_energy_j": 180.82762251697608,
              "semantic_passes": 2,
              "tokens_per_s": 79.29236743803534,
              "ttft_s": 0.12377325
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6599580005,
              "format_passes": 0,
              "gpu_energy_j": 462.8990962820635,
              "semantic_passes": 0,
              "tokens_per_s": 79.54074419753661,
              "ttft_s": 0.062974765
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2376175635,
              "format_passes": 2,
              "gpu_energy_j": 59.90139061620586,
              "semantic_passes": 2,
              "tokens_per_s": 78.26374955973395,
              "ttft_s": 0.071477208
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24150212100000001,
              "format_passes": 0,
              "gpu_energy_j": 54.84901513602682,
              "semantic_passes": 0,
              "tokens_per_s": 77.57818488756308,
              "ttft_s": 0.125437881
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1820657145,
              "format_passes": 2,
              "gpu_energy_j": 41.71314794465698,
              "semantic_passes": 2,
              "tokens_per_s": 77.46948016560452,
              "ttft_s": 0.0658963365
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3576210305,
              "format_passes": 0,
              "gpu_energy_j": 92.42268031467866,
              "semantic_passes": 0,
              "tokens_per_s": 78.84612329964422,
              "ttft_s": 0.0785990565
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469838066,
              "format_passes": 0,
              "gpu_energy_j": 118.67439450532319,
              "semantic_passes": 2,
              "tokens_per_s": 78.89557632401784,
              "ttft_s": 0.11483789650000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0821914355,
              "format_passes": 2,
              "gpu_energy_j": 290.8024816321114,
              "semantic_passes": 2,
              "tokens_per_s": 77.95979232273717,
              "ttft_s": 0.8256056545
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2373168595,
              "format_passes": 0,
              "gpu_energy_j": 51.642275599921575,
              "semantic_passes": 0,
              "tokens_per_s": 77.02297432872692,
              "ttft_s": 0.0684472585
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200267233,
              "format_passes": 0,
              "gpu_energy_j": 48.00542605205438,
              "semantic_passes": 0,
              "tokens_per_s": 2535.1723837875506,
              "ttft_s": 0.200103383
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7241454764999999,
              "format_passes": 0,
              "gpu_energy_j": 189.75538973670984,
              "semantic_passes": 0,
              "tokens_per_s": 2833.13944937001,
              "ttft_s": 0.72393098
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4255222325,
              "format_passes": 0,
              "gpu_energy_j": 380.6348824462421,
              "semantic_passes": 0,
              "tokens_per_s": 2876.9175187226324,
              "ttft_s": 1.4251603485
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2951217265,
              "format_passes": 2,
              "gpu_energy_j": 75.45085919155625,
              "semantic_passes": 2,
              "tokens_per_s": 78.60750380847196,
              "ttft_s": 0.0787991525
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353306331,
              "format_passes": 2,
              "gpu_energy_j": 89.63573614992598,
              "semantic_passes": 2,
              "tokens_per_s": 78.88565404190898,
              "ttft_s": 0.0743889445
            },
            "state-prime": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 3.0919375615,
              "format_passes": 0,
              "gpu_energy_j": 849.4410489200231,
              "semantic_passes": 0,
              "tokens_per_s": 75.93571790746013,
              "ttft_s": 2.89368657
            },
            "state-quality-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6648808705,
              "format_passes": 0,
              "gpu_energy_j": 182.38813993677337,
              "semantic_passes": 0,
              "tokens_per_s": 79.25686675391952,
              "ttft_s": 0.122263253
            },
            "state-quality-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23583797499999998,
              "format_passes": 0,
              "gpu_energy_j": 56.9968735103406,
              "semantic_passes": 0,
              "tokens_per_s": 78.16494068331826,
              "ttft_s": 0.06948947899999999
            },
            "state-quality-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23955316,
              "format_passes": 0,
              "gpu_energy_j": 59.11662068622457,
              "semantic_passes": 0,
              "tokens_per_s": 77.30242480157833,
              "ttft_s": 0.1230877975
            },
            "state-quality-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1784966355,
              "format_passes": 0,
              "gpu_energy_j": 41.152383320683214,
              "semantic_passes": 0,
              "tokens_per_s": 77.32980697964669,
              "ttft_s": 0.062075596999999996
            },
            "state-quality-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.356675957,
              "format_passes": 0,
              "gpu_energy_j": 91.37505951889324,
              "semantic_passes": 0,
              "tokens_per_s": 78.57576112932082,
              "ttft_s": 0.07662604
            },
            "state-quality-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465640435,
              "format_passes": 0,
              "gpu_energy_j": 124.04139956039154,
              "semantic_passes": 0,
              "tokens_per_s": 79.06043799922199,
              "ttft_s": 0.111477357
            },
            "state-quality-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.084526673,
              "format_passes": 0,
              "gpu_energy_j": 291.1518514142984,
              "semantic_passes": 0,
              "tokens_per_s": 77.82525037142244,
              "ttft_s": 0.827495621
            },
            "state-quality-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.231688163,
              "format_passes": 0,
              "gpu_energy_j": 59.53064083927983,
              "semantic_passes": 0,
              "tokens_per_s": 78.08581709814534,
              "ttft_s": 0.065188726
            },
            "state-quality-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29322731150000003,
              "format_passes": 0,
              "gpu_energy_j": 71.93671372698194,
              "semantic_passes": 0,
              "tokens_per_s": 78.5212416037163,
              "ttft_s": 0.076697923
            },
            "state-quality-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.348581284,
              "format_passes": 0,
              "gpu_energy_j": 93.18984997200198,
              "semantic_passes": 0,
              "tokens_per_s": 78.69242648245083,
              "ttft_s": 0.069009742
            },
            "state-quality-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.366751238,
              "format_passes": 0,
              "gpu_energy_j": 97.92199492268365,
              "semantic_passes": 0,
              "tokens_per_s": 78.84223226963748,
              "ttft_s": 0.0749953365
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36898601,
              "format_passes": 2,
              "gpu_energy_j": 95.66438525649032,
              "semantic_passes": 2,
              "tokens_per_s": 78.97877830458671,
              "ttft_s": 0.077723441
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6213804345,
              "format_passes": 0,
              "gpu_energy_j": 163.9327359283422,
              "semantic_passes": 0,
              "tokens_per_s": 78.9862003082954,
              "ttft_s": 0.3198341105
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56182974,
              "format_passes": 0,
              "gpu_energy_j": 146.51178874237434,
              "semantic_passes": 0,
              "tokens_per_s": 78.67718744112312,
              "ttft_s": 0.256816
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
              "e2e_s": 0.665994246,
              "format_passes": 2,
              "gpu_energy_j": 179.92010251696848,
              "semantic_passes": 2,
              "tokens_per_s": 79.31260933641528,
              "ttft_s": 0.1238370515
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6586748125,
              "format_passes": 0,
              "gpu_energy_j": 463.32871856243634,
              "semantic_passes": 0,
              "tokens_per_s": 79.6067302960061,
              "ttft_s": 0.0634192475
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.237992242,
              "format_passes": 2,
              "gpu_energy_j": 54.52390368146203,
              "semantic_passes": 2,
              "tokens_per_s": 78.34256765203867,
              "ttft_s": 0.07199420349999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241573492,
              "format_passes": 0,
              "gpu_energy_j": 64.13817051942951,
              "semantic_passes": 0,
              "tokens_per_s": 77.52722829861472,
              "ttft_s": 0.12546000899999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1834479395,
              "format_passes": 2,
              "gpu_energy_j": 43.207119362447656,
              "semantic_passes": 2,
              "tokens_per_s": 77.48976646885951,
              "ttft_s": 0.06732196500000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3575413035,
              "format_passes": 0,
              "gpu_energy_j": 87.66817308901288,
              "semantic_passes": 0,
              "tokens_per_s": 78.84853113683623,
              "ttft_s": 0.07850035799999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46869805649999996,
              "format_passes": 0,
              "gpu_energy_j": 120.51413687901737,
              "semantic_passes": 2,
              "tokens_per_s": 79.0998438844921,
              "ttft_s": 0.1147162505
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0858839455,
              "format_passes": 2,
              "gpu_energy_j": 291.99897004913896,
              "semantic_passes": 2,
              "tokens_per_s": 77.91179345877325,
              "ttft_s": 0.829145217
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233398139,
              "format_passes": 0,
              "gpu_energy_j": 53.50881080588329,
              "semantic_passes": 0,
              "tokens_per_s": 78.27702192221597,
              "ttft_s": 0.0672827845
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2000703315,
              "format_passes": 0,
              "gpu_energy_j": 48.40967741266779,
              "semantic_passes": 0,
              "tokens_per_s": 2537.8244820618684,
              "ttft_s": 0.19992725900000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.723288538,
              "format_passes": 0,
              "gpu_energy_j": 191.78913513034365,
              "semantic_passes": 0,
              "tokens_per_s": 2836.441400260679,
              "ttft_s": 0.723056703
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4287311914999998,
              "format_passes": 0,
              "gpu_energy_j": 386.7863039410993,
              "semantic_passes": 0,
              "tokens_per_s": 2870.379521429105,
              "ttft_s": 1.4284005039999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29520449400000004,
              "format_passes": 2,
              "gpu_energy_j": 77.0872851021964,
              "semantic_passes": 2,
              "tokens_per_s": 78.64837189621007,
              "ttft_s": 0.079011995
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3533249385,
              "format_passes": 2,
              "gpu_energy_j": 91.38510535602,
              "semantic_passes": 2,
              "tokens_per_s": 78.71598950640448,
              "ttft_s": 0.073819628
            },
            "state-prime": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 3.0943785464999998,
              "format_passes": 0,
              "gpu_energy_j": 849.2434565202709,
              "semantic_passes": 0,
              "tokens_per_s": 75.86927253981078,
              "ttft_s": 2.8957163780000004
            },
            "state-quality-code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6633366115,
              "format_passes": 0,
              "gpu_energy_j": 184.96756293345072,
              "semantic_passes": 0,
              "tokens_per_s": 79.34634738658137,
              "ttft_s": 0.1213993355
            },
            "state-quality-energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.235570308,
              "format_passes": 0,
              "gpu_energy_j": 60.22498200034215,
              "semantic_passes": 0,
              "tokens_per_s": 78.18624987673473,
              "ttft_s": 0.0692745085
            },
            "state-quality-filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2412771765,
              "format_passes": 0,
              "gpu_energy_j": 59.241630024809595,
              "semantic_passes": 0,
              "tokens_per_s": 76.99405706927345,
              "ttft_s": 0.12440202049999999
            },
            "state-quality-german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.178943506,
              "format_passes": 0,
              "gpu_energy_j": 42.20413873246318,
              "semantic_passes": 0,
              "tokens_per_s": 76.76078526383415,
              "ttft_s": 0.061573825
            },
            "state-quality-ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3568442645,
              "format_passes": 0,
              "gpu_energy_j": 94.30654956783256,
              "semantic_passes": 0,
              "tokens_per_s": 78.45154179801139,
              "ttft_s": 0.076357852
            },
            "state-quality-jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.466166803,
              "format_passes": 0,
              "gpu_energy_j": 123.49704129293958,
              "semantic_passes": 0,
              "tokens_per_s": 78.98325981552448,
              "ttft_s": 0.111652637
            },
            "state-quality-long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0862757245,
              "format_passes": 0,
              "gpu_energy_j": 289.93855607921,
              "semantic_passes": 0,
              "tokens_per_s": 77.53450592927874,
              "ttft_s": 0.828326181
            },
            "state-quality-math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2324458325,
              "format_passes": 0,
              "gpu_energy_j": 58.86655441271822,
              "semantic_passes": 0,
              "tokens_per_s": 77.95887347138772,
              "ttft_s": 0.06570342
            },
            "state-quality-pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294621734,
              "format_passes": 0,
              "gpu_energy_j": 73.06778582729288,
              "semantic_passes": 0,
              "tokens_per_s": 78.15272385908321,
              "ttft_s": 0.077012682
            },
            "state-quality-sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.348540309,
              "format_passes": 0,
              "gpu_energy_j": 89.08155958589803,
              "semantic_passes": 0,
              "tokens_per_s": 78.68665181043036,
              "ttft_s": 0.0689410645
            },
            "state-quality-time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37560649199999996,
              "format_passes": 0,
              "gpu_energy_j": 96.12526475183896,
              "semantic_passes": 0,
              "tokens_per_s": 76.86498813943966,
              "ttft_s": 0.0764101375
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3687863065,
              "format_passes": 2,
              "gpu_energy_j": 95.74139484267553,
              "semantic_passes": 2,
              "tokens_per_s": 78.93161680611998,
              "ttft_s": 0.07731359
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6216742855,
              "format_passes": 0,
              "gpu_energy_j": 165.55078058658734,
              "semantic_passes": 0,
              "tokens_per_s": 78.92423931138293,
              "ttft_s": 0.3202558875
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5621861815,
              "format_passes": 0,
              "gpu_energy_j": 148.40156392254903,
              "semantic_passes": 0,
              "tokens_per_s": 78.6859451324923,
              "ttft_s": 0.256920594
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.015699772548150026,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5018702272228337,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.025528180118672417,
            "ttft_change_pct": 0.051547083073288924
          },
          "decode": {
            "e2e_change_pct": -0.07730243774924928,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.09281121605626552,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.08295886483740134,
            "ttft_change_pct": 0.7058104940923515
          },
          "energy": {
            "e2e_change_pct": 0.1576813155059531,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.977232213518915,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10070830077539838,
            "ttft_change_pct": 0.7233011955363411
          },
          "filtering": {
            "e2e_change_pct": 0.0295529495577318,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 16.935865412287466,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.06568417271197724,
            "ttft_change_pct": 0.01764060411701962
          },
          "german": {
            "e2e_change_pct": 0.7591901659222078,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5815360177870126,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0261861874013114,
            "ttft_change_pct": 2.1634412104230005
          },
          "ha_sim": {
            "e2e_change_pct": -0.022293711275456207,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.144307879275667,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0030538434754312505,
            "ttft_change_pct": -0.12557211803173596
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.24263881164537926,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5502437415946924,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.2589087626857056,
            "ttft_change_pct": -0.10592844671271084
          },
          "long_context": {
            "e2e_change_pct": 0.34120672913051653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.41144367486563027,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.061568742724738,
            "ttft_change_pct": 0.4287231416969295
          },
          "math": {
            "e2e_change_pct": -1.6512608957729769,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.6143550691336124,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.6281474513524907,
            "ttft_change_pct": -1.7012719362602402
          },
          "prefill": {
            "e2e_change_pct": -0.09831937908683086,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8420951418597111,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10461214753196835,
            "ttft_change_pct": -0.08801650294936181
          },
          "prefill2048": {
            "e2e_change_pct": -0.11833789311807008,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0717721359354782,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.11654741849729255,
            "ttft_change_pct": -0.12076800470673943
          },
          "prefill4096": {
            "e2e_change_pct": 0.2251076080638903,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6160950502811522,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.22725702947613557,
            "ttft_change_pct": 0.22735375029274696
          },
          "pve_sim": {
            "e2e_change_pct": 0.02804520730534943,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.168863188801562,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.05199005916494137,
            "ttft_change_pct": 0.2701076004592906
          },
          "sorting": {
            "e2e_change_pct": 0.005266676073256704,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9516425939404503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2150765402976318,
            "ttft_change_pct": -0.7653240731221866
          },
          "state-prime": {
            "e2e_change_pct": 0.07894677532931382,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.02326146116948813,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.08750212611451369,
            "ttft_change_pct": 0.07014609049385001
          },
          "state-quality-code": {
            "e2e_change_pct": -0.23226100622186774,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4142493023787228,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.11289953328545987,
            "ttft_change_pct": -0.7066043793223842
          },
          "state-quality-energy": {
            "e2e_change_pct": -0.11349614072965197,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.663658883703326,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.02726183021466433,
            "ttft_change_pct": -0.3093569027909915
          },
          "state-quality-filtering": {
            "e2e_change_pct": 0.7196801327939095,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.21146225398867013,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.39891081437147813,
            "ttft_change_pct": 1.0677118501531302
          },
          "state-quality-german": {
            "e2e_change_pct": 0.2503523378736272,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5557582013757907,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7358374966102144,
            "ttft_change_pct": -0.8083240826503801
          },
          "state-quality-ha_sim": {
            "e2e_change_pct": 0.047187789559921534,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2081949542623223,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15808861349111414,
            "ttft_change_pct": -0.3499959021763366
          },
          "state-quality-jarvis_memory": {
            "e2e_change_pct": 0.11304172929054168,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.43885208436955647,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09761922100440801,
            "ttft_change_pct": 0.15723372415439307
          },
          "state-quality-long_context": {
            "e2e_change_pct": 0.1612732580529297,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4167225209782077,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.37358625992993666,
            "ttft_change_pct": 0.10037031966361187
          },
          "state-quality-math": {
            "e2e_change_pct": 0.32702123845662623,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1155371707731176,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.16256937748128086,
            "ttft_change_pct": 0.7895444988447853
          },
          "state-quality-pve_sim": {
            "e2e_change_pct": 0.47554318622875513,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5723155002654865,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.4693223605568342,
            "ttft_change_pct": 0.41038790581069406
          },
          "state-quality-sorting": {
            "e2e_change_pct": -0.01175479059857265,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.40851700838476,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.007338281812607761,
            "ttft_change_pct": -0.09951855782912578
          },
          "state-quality-time": {
            "e2e_change_pct": 2.4145123676446723,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8348586262599609,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.507848995745976,
            "ttft_change_pct": 1.8865186370621956
          },
          "time": {
            "e2e_change_pct": -0.05412224165354251,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.08049974499781953,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.05971414027811095,
            "ttft_change_pct": -0.5273196795288593
          },
          "tool-call": {
            "e2e_change_pct": 0.04729003098342677,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9870174185053537,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.07844534446601603,
            "ttft_change_pct": 0.13187367643201497
          },
          "tool-final": {
            "e2e_change_pct": 0.0634429747346621,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2898451356004204,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.011131169852407474,
            "ttft_change_pct": 0.04072721325774076
          }
        }
      },
      "complete": true,
      "state": {
        "arms": {
          "A": {
            "cold_semantic_passes": 18,
            "erase_s": 0.0060204365,
            "explicit_erases": 24,
            "foreign_markers": 0,
            "questions": 24,
            "semantic_passes": 18,
            "shift_events": 0,
            "starts": 2,
            "verified_starts": 0
          },
          "B": {
            "cold_semantic_passes": 18,
            "erase_s": 0.006032504,
            "explicit_erases": 24,
            "foreign_markers": 0,
            "questions": 24,
            "semantic_passes": 18,
            "shift_events": 0,
            "starts": 2,
            "verified_starts": 0
          }
        },
        "change_exercised": false,
        "kind": "shift",
        "note": "State operation, post-state quality, exact answer drift and possible leaks are separate. No throughput percentage across unequal shifted/truncated output lengths; explicit erase latency is reported separately from question latency."
      }
    }
  }
}
```
