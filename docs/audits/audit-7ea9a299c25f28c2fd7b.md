# Public audit excerpt

Original SHA256: `7ea9a299c25f28c2fd7bd50a62477cfc5c2dbb5842195ea4f3e5d0414d9f4e41`

Original file: `RESULTS.json`; 46188 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.792876631,
              "format_passes": 2,
              "gpu_energy_j": 487.7143470181238,
              "semantic_passes": 2,
              "tokens_per_s": 35.36493633694669,
              "ttft_s": 0.54447058
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 9.5333427875,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 35.276675388613356,
              "ttft_s": 5.9360357525000005
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.453239016,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 34.9018840830842,
              "ttft_s": 1.8295562655
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7842235085,
              "format_passes": 0,
              "gpu_energy_j": 1066.5091470722505,
              "semantic_passes": 0,
              "tokens_per_s": 35.391392157935954,
              "ttft_s": 0.195722027
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6020290605,
              "format_passes": 2,
              "gpu_energy_j": 147.79543892009713,
              "semantic_passes": 2,
              "tokens_per_s": 34.81680464615236,
              "ttft_s": 0.225425202
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9465055385,
              "format_passes": 0,
              "gpu_energy_j": 247.91750193640635,
              "semantic_passes": 0,
              "tokens_per_s": 34.921255976898365,
              "ttft_s": 0.5419197165
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4941488935,
              "format_passes": 2,
              "gpu_energy_j": 110.21948323664755,
              "semantic_passes": 2,
              "tokens_per_s": 33.65115753446433,
              "ttft_s": 0.222658847
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.021271118,
              "format_passes": 0,
              "gpu_energy_j": 266.76370511695745,
              "semantic_passes": 0,
              "tokens_per_s": 35.08436247013054,
              "ttft_s": 0.24733158
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1713561160000001,
              "format_passes": 0,
              "gpu_energy_j": 299.763656204825,
              "semantic_passes": 2,
              "tokens_per_s": 35.19616404553814,
              "ttft_s": 0.37199017300000004
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8079069839999997,
              "format_passes": 2,
              "gpu_energy_j": 1016.6981301990511,
              "semantic_passes": 2,
              "tokens_per_s": 34.313599702773026,
              "ttft_s": 3.222911993
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.589903961,
              "format_passes": 2,
              "gpu_energy_j": 144.25629366242077,
              "semantic_passes": 2,
              "tokens_per_s": 34.932812146741426,
              "ttft_s": 0.21475518
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7229991794999999,
              "format_passes": 0,
              "gpu_energy_j": 186.3675278342535,
              "semantic_passes": 0,
              "tokens_per_s": 699.5044053626111,
              "ttft_s": 0.722856002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.750220841,
              "format_passes": 0,
              "gpu_energy_j": 734.2689030877484,
              "semantic_passes": 0,
              "tokens_per_s": 745.0027863867517,
              "ttft_s": 2.749997692
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.461201726500001,
              "format_passes": 0,
              "gpu_energy_j": 1479.1905128997337,
              "semantic_passes": 0,
              "tokens_per_s": 750.2621517796654,
              "ttft_s": 5.4608465509999995
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8715951040000001,
              "format_passes": 0,
              "gpu_energy_j": 232.11256143160648,
              "semantic_passes": 2,
              "tokens_per_s": 35.18482544603049,
              "ttft_s": 0.241859808
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0004002585,
              "format_passes": 0,
              "gpu_energy_j": 267.35199327487044,
              "semantic_passes": 2,
              "tokens_per_s": 34.99366983096944,
              "ttft_s": 0.22588458
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.035755231,
              "format_passes": 0,
              "gpu_energy_j": 276.4048569328342,
              "semantic_passes": 2,
              "tokens_per_s": 35.02331497146925,
              "ttft_s": 0.232592665
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.708003518,
              "format_passes": 0,
              "gpu_energy_j": 462.4399936864663,
              "semantic_passes": 0,
              "tokens_per_s": 35.04016544852239,
              "ttft_s": 1.0300721845
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.780879877,
              "format_passes": 0,
              "gpu_energy_j": 467.01670320687685,
              "semantic_passes": 0,
              "tokens_per_s": 35.03928945184218,
              "ttft_s": 1.0954284785000001
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
              "e2e_s": 1.766120425,
              "format_passes": 2,
              "gpu_energy_j": 485.9593223341244,
              "semantic_passes": 2,
              "tokens_per_s": 35.29483306495493,
              "ttft_s": 0.5194623945
            },
            "concurrent-decode": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 7.206899704,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 29.05871375961821,
              "ttft_s": 2.877399259
            },
            "concurrent-quality": {
              "attempts": 24,
              "complete": 24,
              "e2e_s": 2.6626589285,
              "format_passes": 0,
              "semantic_passes": 0,
              "tokens_per_s": 23.863569255274754,
              "ttft_s": 1.184347035
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.8846910015000002,
              "format_passes": 0,
              "gpu_energy_j": 1099.8212439984309,
              "semantic_passes": 0,
              "tokens_per_s": 34.52914978340295,
              "ttft_s": 0.204418921
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.72215696,
              "format_passes": 0,
              "gpu_energy_j": 187.86768049598288,
              "semantic_passes": 2,
              "tokens_per_s": 35.08565190650816,
              "ttft_s": 0.2091052655
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9364322795,
              "format_passes": 0,
              "gpu_energy_j": 248.4849992804343,
              "semantic_passes": 0,
              "tokens_per_s": 34.711222560664794,
              "ttft_s": 0.53308896
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.456324373,
              "format_passes": 2,
              "gpu_energy_j": 111.64764863285626,
              "semantic_passes": 2,
              "tokens_per_s": 34.56466782696394,
              "ttft_s": 0.195910256
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.98906388,
              "format_passes": 0,
              "gpu_energy_j": 269.3997328621827,
              "semantic_passes": 0,
              "tokens_per_s": 35.26116114425348,
              "ttft_s": 0.223320701
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.148194194,
              "format_passes": 0,
              "gpu_energy_j": 299.6188922406668,
              "semantic_passes": 2,
              "tokens_per_s": 35.275192013799504,
              "ttft_s": 0.3544206175
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.9475303564999997,
              "format_passes": 0,
              "gpu_energy_j": 1063.3665047525706,
              "semantic_passes": 2,
              "tokens_per_s": 34.46487342966988,
              "ttft_s": 3.2220646984999997
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5833819565,
              "format_passes": 2,
              "gpu_energy_j": 146.02965121549704,
              "semantic_passes": 2,
              "tokens_per_s": 34.84628792052533,
              "ttft_s": 0.210298071
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7702229135,
              "format_passes": 0,
              "gpu_energy_j": 196.51881105588535,
              "semantic_passes": 0,
              "tokens_per_s": 656.5899187688015,
              "ttft_s": 0.7700377755000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7687549909999998,
              "format_passes": 0,
              "gpu_energy_j": 742.6443262142221,
              "semantic_passes": 0,
              "tokens_per_s": 740.0129289379784,
              "ttft_s": 2.7685205515
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.5152137595,
              "format_passes": 0,
              "gpu_energy_j": 1491.0260475310133,
              "semantic_passes": 0,
              "tokens_per_s": 742.9155904736663,
              "ttft_s": 5.5148853395
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8477480470000001,
              "format_passes": 0,
              "gpu_energy_j": 226.88654639878342,
              "semantic_passes": 2,
              "tokens_per_s": 35.192697916543345,
              "ttft_s": 0.2226092195
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9951005635000001,
              "format_passes": 0,
              "gpu_energy_j": 268.51545324843437,
              "semantic_passes": 2,
              "tokens_per_s": 34.71724786650023,
              "ttft_s": 0.21736123899999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.018245069,
              "format_passes": 0,
              "gpu_energy_j": 274.8631905499303,
              "semantic_passes": 2,
              "tokens_per_s": 35.22194568037074,
              "ttft_s": 0.22323450849999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.706449661,
              "format_passes": 0,
              "gpu_energy_j": 465.50763593674657,
              "semantic_passes": 0,
              "tokens_per_s": 35.15621966876461,
              "ttft_s": 1.027833206
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.782134749,
              "format_passes": 0,
              "gpu_energy_j": 469.06473061929904,
              "semantic_passes": 0,
              "tokens_per_s": 35.05475714793193,
              "ttft_s": 1.0969476325
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": -4,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -1.492361802109965,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.35984684369644304,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.19822818659657182,
            "ttft_change_pct": -4.593119705384274
          },
          "concurrent-decode": {
            "e2e_change_pct": -24.40322492704662,
            "format_pass_change": 0,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -17.626268803670165,
            "ttft_change_pct": -51.52658476175511
          },
          "concurrent-quality": {
            "e2e_change_pct": 8.536465918492464,
            "format_pass_change": 0,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -35.26588619692822
          },
          "decode": {
            "e2e_change_pct": 2.654903780771223,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1234703441248346,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.436305332904687,
            "ttft_change_pct": 4.44349270917781
          },
          "energy": {
            "e2e_change_pct": 19.95383734470073,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 27.113314097297735,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -7.23962376664522
          },
          "filtering": {
            "e2e_change_pct": -1.064257797789947,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.22890572048983593,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.601448631665813,
            "ttft_change_pct": -1.629532240870235
          },
          "german": {
            "e2e_change_pct": -7.654478437074552,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2957467720496885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.7146474577108393,
            "ttft_change_pct": -12.013262154366577
          },
          "ha_sim": {
            "e2e_change_pct": -3.1536423024546956,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9881508221178503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5039244314998026,
            "ttft_change_pct": -9.707971379958835
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.9773595479310346,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04829270031964095,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.2245357424721428,
            "ttft_change_pct": -4.7231235595032945
          },
          "long_context": {
            "e2e_change_pct": 3.6666697239892354,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 4.590189867309258,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -0.026289718795935446
          },
          "math": {
            "e2e_change_pct": -1.1056044595706527,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.229310353159474,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.24768754903738976,
            "ttft_change_pct": -2.075437249057266
          },
          "prefill": {
            "e2e_change_pct": 6.531644203615605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.446916283967629,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.13498446397397,
            "ttft_change_pct": 6.527133117724326
          },
          "prefill2048": {
            "e2e_change_pct": 0.6739149716159076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.140647941272377,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6697770182812479,
            "ttft_change_pct": 0.6735590925724955
          },
          "prefill4096": {
            "e2e_change_pct": 0.989013695244223,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8001359208340109,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9791992423678342,
            "ttft_change_pct": 0.9895679725720363
          },
          "pve_sim": {
            "e2e_change_pct": -2.7360246622037065,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.251500306829768,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.02237461864045276,
            "ttft_change_pct": -7.959399562576353
          },
          "sorting": {
            "e2e_change_pct": -0.5297574600736654,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4351790907979991,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7899199078130859,
            "ttft_change_pct": -3.7733168859955035
          },
          "time": {
            "e2e_change_pct": -1.6905694971093066,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5577566183211147,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5671385163377618,
            "ttft_change_pct": -4.023409981565851
          },
          "tool-call": {
            "e2e_change_pct": -0.09097504680900537,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6633600666382078,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.33120340260013315,
            "ttft_change_pct": -0.21736132027357913
          },
          "tool-final": {
            "e2e_change_pct": 0.07046359590034967,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4385340820486583,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.04414386345079624,
            "ttft_change_pct": 0.13868125850444724
          }
        }
      },
      "complete": true,
      "concurrency": {
        "aggregate_throughput_change_pct": 59.22897039728947,
        "arms": {
          "A": {
            "active_slots_max": 1,
            "aggregate_tokens_per_s": 33.66819786759992,
            "exact_serial_matches": 24,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 12,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 20,
            "request_e2e_s": 9.5333427875,
            "wave_elapsed_s": 15.20722995,
            "waves": 6
          },
          "B": {
            "active_slots_max": 2,
            "aggregate_tokens_per_s": 53.60952481590152,
            "exact_serial_matches": 20,
            "exercised": true,
            "marker_passes": 24,
            "offered_load": 4,
            "parallel_format_passes": 10,
            "parallel_quality_attempts": 24,
            "parallel_quality_passes": 20,
            "request_e2e_s": 7.206899704,
            "wave_elapsed_s": 9.5505418745,
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
