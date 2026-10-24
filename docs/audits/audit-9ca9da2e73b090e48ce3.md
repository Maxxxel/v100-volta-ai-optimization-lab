# Public audit excerpt

Original SHA256: `9ca9da2e73b090e48ce3d357b041646a6eeba0e8edac02d7a8e600f49e4ae6b4`

Original file: `RESULTS.json`; 39530 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5261854425,
              "format_passes": 2,
              "gpu_energy_j": 135.22818063544497,
              "semantic_passes": 2,
              "tokens_per_s": 96.44001015906332,
              "ttft_s": 0.1321264225
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3676854294999998,
              "format_passes": 0,
              "gpu_energy_j": 356.9410503066303,
              "semantic_passes": 0,
              "tokens_per_s": 96.95200281518919,
              "ttft_s": 0.0575959155
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20479957599999998,
              "format_passes": 2,
              "gpu_energy_j": 46.68039327246193,
              "semantic_passes": 2,
              "tokens_per_s": 94.92239162509247,
              "ttft_s": 0.067840676
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2298063575,
              "format_passes": 0,
              "gpu_energy_j": 55.11891739876465,
              "semantic_passes": 0,
              "tokens_per_s": 93.84895054591142,
              "ttft_s": 0.133869571
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15651839350000002,
              "format_passes": 2,
              "gpu_energy_j": 33.58589647460107,
              "semantic_passes": 2,
              "tokens_per_s": 93.78615416841077,
              "ttft_s": 0.0605169815
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.306903079,
              "format_passes": 0,
              "gpu_energy_j": 75.11524099851513,
              "semantic_passes": 0,
              "tokens_per_s": 95.79360170905855,
              "ttft_s": 0.077228203
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3988080035,
              "format_passes": 0,
              "gpu_energy_j": 97.08087179974322,
              "semantic_passes": 2,
              "tokens_per_s": 96.21779749765435,
              "ttft_s": 0.10778278250000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0329250175000002,
              "format_passes": 2,
              "gpu_energy_j": 273.3273830299969,
              "semantic_passes": 2,
              "tokens_per_s": 93.99356210030456,
              "ttft_s": 0.8732907599999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14881184349999999,
              "format_passes": 0,
              "gpu_energy_j": 27.301904639836934,
              "semantic_passes": 0,
              "tokens_per_s": 93.78330662946833,
              "ttft_s": 0.063464631
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205749742,
              "format_passes": 0,
              "gpu_energy_j": 49.387057344873,
              "semantic_passes": 0,
              "tokens_per_s": 2467.27518687571,
              "ttft_s": 0.20559365699999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7556327995000001,
              "format_passes": 0,
              "gpu_energy_j": 198.7176464466104,
              "semantic_passes": 0,
              "tokens_per_s": 2714.740301087912,
              "ttft_s": 0.7553718789999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4982062415,
              "format_passes": 0,
              "gpu_energy_j": 403.77166621249967,
              "semantic_passes": 0,
              "tokens_per_s": 2737.1937412947455,
              "ttft_s": 1.4978410325
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254489109,
              "format_passes": 2,
              "gpu_energy_j": 60.219421824027236,
              "semantic_passes": 2,
              "tokens_per_s": 95.45535603639428,
              "ttft_s": 0.0763652785
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.350805399,
              "format_passes": 0,
              "gpu_energy_j": 83.75306377601427,
              "semantic_passes": 2,
              "tokens_per_s": 96.08257283108644,
              "ttft_s": 0.0697572545
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31445316349999997,
              "format_passes": 0,
              "gpu_energy_j": 73.58934744455922,
              "semantic_passes": 0,
              "tokens_per_s": 95.97810030295909,
              "ttft_s": 0.07481278599999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550343649,
              "format_passes": 0,
              "gpu_energy_j": 140.5683352316501,
              "semantic_passes": 0,
              "tokens_per_s": 96.22562298048427,
              "ttft_s": 0.3034941125
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524274438,
              "format_passes": 0,
              "gpu_energy_j": 130.12994801768806,
              "semantic_passes": 0,
              "tokens_per_s": 95.83746133262449,
              "ttft_s": 0.27384765749999995
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
              "e2e_s": 0.527546485,
              "format_passes": 2,
              "gpu_energy_j": 135.6512719690275,
              "semantic_passes": 2,
              "tokens_per_s": 96.14998238000342,
              "ttft_s": 0.1322835825
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3708417155000001,
              "format_passes": 0,
              "gpu_energy_j": 381.2080333380355,
              "semantic_passes": 0,
              "tokens_per_s": 96.88451471397406,
              "ttft_s": 0.0595091785
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204727591,
              "format_passes": 2,
              "gpu_energy_j": 49.84622100950082,
              "semantic_passes": 2,
              "tokens_per_s": 94.93132320156712,
              "ttft_s": 0.0677458165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2291888405,
              "format_passes": 0,
              "gpu_energy_j": 59.32166168585646,
              "semantic_passes": 0,
              "tokens_per_s": 93.8126336854599,
              "ttft_s": 0.13323733100000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15634963400000002,
              "format_passes": 2,
              "gpu_energy_j": 34.09432362176524,
              "semantic_passes": 2,
              "tokens_per_s": 93.88020765770122,
              "ttft_s": 0.0604570995
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3058644695,
              "format_passes": 0,
              "gpu_energy_j": 74.69259695274667,
              "semantic_passes": 0,
              "tokens_per_s": 95.73150291379986,
              "ttft_s": 0.07599480950000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398637085,
              "format_passes": 0,
              "gpu_energy_j": 95.22749502643428,
              "semantic_passes": 2,
              "tokens_per_s": 96.05664267986916,
              "ttft_s": 0.107100729
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.9540656809999999,
              "format_passes": 2,
              "gpu_energy_j": 530.9464605480447,
              "semantic_passes": 2,
              "tokens_per_s": 94.06517071073853,
              "ttft_s": 1.7945641215
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14840514900000001,
              "format_passes": 0,
              "gpu_energy_j": 33.68984496613493,
              "semantic_passes": 0,
              "tokens_per_s": 93.60154608915587,
              "ttft_s": 0.0629043805
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.4352411725,
              "format_passes": 0,
              "gpu_energy_j": 114.36289164604821,
              "semantic_passes": 0,
              "tokens_per_s": 1163.093751541663,
              "ttft_s": 0.4350893525
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6565353059999999,
              "format_passes": 0,
              "gpu_energy_j": 456.52124993053076,
              "semantic_passes": 0,
              "tokens_per_s": 1237.2327667550148,
              "ttft_s": 1.6563101695
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.3055252675,
              "format_passes": 0,
              "gpu_energy_j": 919.8179493731386,
              "semantic_passes": 0,
              "tokens_per_s": 1239.7931190816932,
              "ttft_s": 3.3051671385
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2547412565,
              "format_passes": 2,
              "gpu_energy_j": 59.10284480494737,
              "semantic_passes": 2,
              "tokens_per_s": 95.0882591043272,
              "ttft_s": 0.0759212
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35130470999999996,
              "format_passes": 0,
              "gpu_energy_j": 90.18099177980733,
              "semantic_passes": 2,
              "tokens_per_s": 95.83473858958173,
              "ttft_s": 0.0695064085
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3147127865,
              "format_passes": 0,
              "gpu_energy_j": 76.49586852837072,
              "semantic_passes": 0,
              "tokens_per_s": 95.7984246341207,
              "ttft_s": 0.074585349
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6779590664999999,
              "format_passes": 0,
              "gpu_energy_j": 179.7957317760239,
              "semantic_passes": 0,
              "tokens_per_s": 96.06609501280657,
              "ttft_s": 0.430345523
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.64607853,
              "format_passes": 0,
              "gpu_energy_j": 166.3816002431218,
              "semantic_passes": 0,
              "tokens_per_s": 95.64651430669907,
              "ttft_s": 0.39541081450000004
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.2586621350703755,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3128721628838038,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3007338744381527,
            "ttft_change_pct": 0.11894668532328456
          },
          "decode": {
            "e2e_change_pct": 0.23077572751171171,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.79859685809705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06960980614684198,
            "ttft_change_pct": 3.3218727116161695
          },
          "energy": {
            "e2e_change_pct": -0.03514899855066034,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.781921734379437,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.009409346226685322,
            "ttft_change_pct": -0.13982687908358216
          },
          "filtering": {
            "e2e_change_pct": -0.26871188713741834,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.624867260520629,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.038697140714172296,
            "ttft_change_pct": -0.4722805901872795
          },
          "german": {
            "e2e_change_pct": -0.10782087410065033,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5138114522226909,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10028504753649692,
            "ttft_change_pct": -0.09895073831466261
          },
          "ha_sim": {
            "e2e_change_pct": -0.33841612257008435,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5626608397313437,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06482561898788486,
            "ttft_change_pct": -1.597076523974006
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.04285733949670467,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9091060256772874,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16748961416324093,
            "ttft_change_pct": -0.6328037597285063
          },
          "long_context": {
            "e2e_change_pct": 89.17788299187936,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 94.25293384884705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07618459055478422,
            "ttft_change_pct": 105.49445885583401
          },
          "math": {
            "e2e_change_pct": -0.2732944437987328,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 23.397416446093587,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19380905498520562,
            "ttft_change_pct": -0.8827759512223365
          },
          "prefill": {
            "e2e_change_pct": 111.5391097306941,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 131.56449846251172,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -52.85918013002517,
            "ttft_change_pct": 111.62586377847252
          },
          "prefill2048": {
            "e2e_change_pct": 119.22490753394035,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 129.73362360809998,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -54.42537298101027,
            "ttft_change_pct": 119.27082746219102
          },
          "prefill4096": {
            "e2e_change_pct": 120.63219174621227,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 127.80646249929055,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -54.70568632473757,
            "ttft_change_pct": 120.66207740239618
          },
          "pve_sim": {
            "e2e_change_pct": 0.09907987850279465,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8541809025379274,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3845744726227007,
            "ttft_change_pct": -0.5815188639690438
          },
          "sorting": {
            "e2e_change_pct": 0.14233275811126322,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.674857150281267,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.25793880638521616,
            "ttft_change_pct": -0.35959844147822606
          },
          "time": {
            "e2e_change_pct": 0.08256332902183416,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.949649215195472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1872048605580101,
            "ttft_change_pct": -0.3040081945350881
          },
          "tool-call": {
            "e2e_change_pct": 23.188314743321392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 27.906282364181713,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16578533111711868,
            "ttft_change_pct": 41.79699219041686
          },
          "tool-final": {
            "e2e_change_pct": 23.232887810563074,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 27.8580394272548,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19924048829161878,
            "ttft_change_pct": 44.39079673339916
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
