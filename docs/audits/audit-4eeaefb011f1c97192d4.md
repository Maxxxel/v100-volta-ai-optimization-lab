# Public audit excerpt

Original SHA256: `4eeaefb011f1c97192d467464687d5d44ca3e558545977ff7d1a349951c94230`

Original file: `RESULTS.json`; 39633 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5288932074999999,
              "format_passes": 2,
              "gpu_energy_j": 131.7233409819674,
              "semantic_passes": 2,
              "tokens_per_s": 95.82854644359453,
              "ttft_s": 0.1322944775
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3667595989999999,
              "format_passes": 0,
              "gpu_energy_j": 355.84978684465113,
              "semantic_passes": 0,
              "tokens_per_s": 97.0307818035663,
              "ttft_s": 0.057801871000000005
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204773771,
              "format_passes": 2,
              "gpu_energy_j": 44.20574296741212,
              "semantic_passes": 2,
              "tokens_per_s": 95.12835567979775,
              "ttft_s": 0.06806461
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229765239,
              "format_passes": 0,
              "gpu_energy_j": 54.78667987177943,
              "semantic_passes": 0,
              "tokens_per_s": 93.79424988133249,
              "ttft_s": 0.13374554900000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1568188905,
              "format_passes": 2,
              "gpu_energy_j": 31.787862961458707,
              "semantic_passes": 2,
              "tokens_per_s": 93.88699398888309,
              "ttft_s": 0.0609253835
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.313215216,
              "format_passes": 0,
              "gpu_energy_j": 71.50830720507247,
              "semantic_passes": 0,
              "tokens_per_s": 93.47259030299209,
              "ttft_s": 0.077717272
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398273095,
              "format_passes": 0,
              "gpu_energy_j": 94.76233435291908,
              "semantic_passes": 2,
              "tokens_per_s": 96.33340298188935,
              "ttft_s": 0.1075665745
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.032917369,
              "format_passes": 2,
              "gpu_energy_j": 270.33972117911594,
              "semantic_passes": 2,
              "tokens_per_s": 93.68650150042453,
              "ttft_s": 0.872751553
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1488076625,
              "format_passes": 0,
              "gpu_energy_j": 31.731321319286316,
              "semantic_passes": 0,
              "tokens_per_s": 93.50818204311771,
              "ttft_s": 0.063221471
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206244483,
              "format_passes": 0,
              "gpu_energy_j": 50.28329932606492,
              "semantic_passes": 0,
              "tokens_per_s": 2461.44961539657,
              "ttft_s": 0.2060700275
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.757052136,
              "format_passes": 0,
              "gpu_energy_j": 198.3042396708862,
              "semantic_passes": 0,
              "tokens_per_s": 2709.549920157198,
              "ttft_s": 0.7568087960000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.50133709,
              "format_passes": 0,
              "gpu_energy_j": 405.9656128772528,
              "semantic_passes": 0,
              "tokens_per_s": 2731.482291081231,
              "ttft_s": 1.5010291085
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25466914350000003,
              "format_passes": 2,
              "gpu_energy_j": 59.23540727598819,
              "semantic_passes": 2,
              "tokens_per_s": 95.30157253840905,
              "ttft_s": 0.0762548595
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3510222275,
              "format_passes": 0,
              "gpu_energy_j": 79.51895735949896,
              "semantic_passes": 2,
              "tokens_per_s": 96.08187032941693,
              "ttft_s": 0.070005282
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31458799849999997,
              "format_passes": 0,
              "gpu_energy_j": 73.73110950601244,
              "semantic_passes": 0,
              "tokens_per_s": 95.94767406191878,
              "ttft_s": 0.07482525300000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550532043,
              "format_passes": 0,
              "gpu_energy_j": 138.1547633487088,
              "semantic_passes": 0,
              "tokens_per_s": 96.12751755078895,
              "ttft_s": 0.303248121
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5249290945,
              "format_passes": 0,
              "gpu_energy_j": 131.76626118593043,
              "semantic_passes": 0,
              "tokens_per_s": 95.86521653867557,
              "ttft_s": 0.2742246865
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
              "e2e_s": 0.5274089525000001,
              "format_passes": 2,
              "gpu_energy_j": 133.94990325789865,
              "semantic_passes": 2,
              "tokens_per_s": 96.19890468598902,
              "ttft_s": 0.132357633
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.366350915,
              "format_passes": 0,
              "gpu_energy_j": 357.26797181830136,
              "semantic_passes": 0,
              "tokens_per_s": 97.05903534294976,
              "ttft_s": 0.0577062795
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20521227549999999,
              "format_passes": 2,
              "gpu_energy_j": 42.350921793316985,
              "semantic_passes": 2,
              "tokens_per_s": 94.900961645158,
              "ttft_s": 0.0682015165
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22984697799999998,
              "format_passes": 0,
              "gpu_energy_j": 55.346173558192895,
              "semantic_passes": 0,
              "tokens_per_s": 94.17820496662826,
              "ttft_s": 0.1343098435
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157086329,
              "format_passes": 2,
              "gpu_energy_j": 33.29818378467726,
              "semantic_passes": 2,
              "tokens_per_s": 93.70444225113759,
              "ttft_s": 0.061042884
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30712530950000005,
              "format_passes": 0,
              "gpu_energy_j": 73.08103340809546,
              "semantic_passes": 0,
              "tokens_per_s": 95.69603403682854,
              "ttft_s": 0.07723033700000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39890784749999997,
              "format_passes": 0,
              "gpu_energy_j": 94.21275056847796,
              "semantic_passes": 2,
              "tokens_per_s": 96.2546636501504,
              "ttft_s": 0.10796768500000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0324556255,
              "format_passes": 2,
              "gpu_energy_j": 276.7487340327043,
              "semantic_passes": 2,
              "tokens_per_s": 93.98916461030493,
              "ttft_s": 0.8726364870000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148754773,
              "format_passes": 0,
              "gpu_energy_j": 29.787441655324848,
              "semantic_passes": 0,
              "tokens_per_s": 93.91726161086939,
              "ttft_s": 0.063577346
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2064155345,
              "format_passes": 0,
              "gpu_energy_j": 49.98344142709619,
              "semantic_passes": 0,
              "tokens_per_s": 2459.0184592006194,
              "ttft_s": 0.20627019
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.756094982,
              "format_passes": 0,
              "gpu_energy_j": 204.60197303108208,
              "semantic_passes": 0,
              "tokens_per_s": 2713.2332531024103,
              "ttft_s": 0.7558648225
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.501309471,
              "format_passes": 0,
              "gpu_energy_j": 405.2959937858136,
              "semantic_passes": 0,
              "tokens_per_s": 2731.5590766941523,
              "ttft_s": 1.500957294
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254219027,
              "format_passes": 2,
              "gpu_energy_j": 58.17120509482513,
              "semantic_passes": 2,
              "tokens_per_s": 95.66075362350699,
              "ttft_s": 0.0764474275
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.350560869,
              "format_passes": 0,
              "gpu_energy_j": 86.19597194007932,
              "semantic_passes": 2,
              "tokens_per_s": 96.20344386911698,
              "ttft_s": 0.06985588449999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3145578655,
              "format_passes": 0,
              "gpu_energy_j": 74.12472537942106,
              "semantic_passes": 0,
              "tokens_per_s": 95.96582170947357,
              "ttft_s": 0.074845844
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5508194055,
              "format_passes": 0,
              "gpu_energy_j": 139.97745065972794,
              "semantic_passes": 0,
              "tokens_per_s": 96.13157797139883,
              "ttft_s": 0.303464652
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5250850855,
              "format_passes": 0,
              "gpu_energy_j": 133.16541261655325,
              "semantic_passes": 0,
              "tokens_per_s": 95.87865279113974,
              "ttft_s": 0.27482131350000005
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
            "e2e_change_pct": -0.2806341580780858,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6903323733916453,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.38648007941191054,
            "ttft_change_pct": 0.04773857623798783
          },
          "decode": {
            "e2e_change_pct": -0.029901674025112346,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.39853472619033603,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02911811989791957,
            "ttft_change_pct": -0.16537786467155646
          },
          "energy": {
            "e2e_change_pct": 0.21414095069822725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.1958828188058845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.23903917293088828,
            "ttft_change_pct": 0.20114197378051646
          },
          "filtering": {
            "e2e_change_pct": 0.03557500706186101,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.021222106765518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.40935887411173155,
            "ttft_change_pct": 0.42191647065576987
          },
          "german": {
            "e2e_change_pct": 0.17053972206237944,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.751249950491321,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19443772772947954,
            "ttft_change_pct": 0.19285968056319547
          },
          "ha_sim": {
            "e2e_change_pct": -1.944320131624755,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1993615350349494,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 2.378712012397588,
            "ttft_change_pct": -0.6265466960806321
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.15937619386514612,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5799601584257519,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0817362714299108,
            "ttft_change_pct": 0.37289511343507886
          },
          "long_context": {
            "e2e_change_pct": -0.04470284979786188,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3707255543635064,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3230594643125029,
            "ttft_change_pct": -0.013184279031575041
          },
          "math": {
            "e2e_change_pct": -0.035542188561688004,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.126059625446412,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.43747997107146386,
            "ttft_change_pct": 0.5629021191234207
          },
          "prefill": {
            "e2e_change_pct": 0.08293627907611789,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5963369607556723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09876928541391328,
            "ttft_change_pct": 0.09713324272739854
          },
          "prefill2048": {
            "e2e_change_pct": -0.1264317151335459,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.175793604134669,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13593892173053845,
            "ttft_change_pct": -0.1247307781026441
          },
          "prefill4096": {
            "e2e_change_pct": -0.0018396268355758139,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1649447810846083,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0028111334703595503,
            "ttft_change_pct": -0.004784350922537595
          },
          "pve_sim": {
            "e2e_change_pct": -0.17674559776419407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.796564301828374,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.37688893848335514,
            "ttft_change_pct": 0.25253210256062086
          },
          "sorting": {
            "e2e_change_pct": -0.13143284494712137,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.39675820998771,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12653119603442953,
            "ttft_change_pct": -0.213408896774403
          },
          "time": {
            "e2e_change_pct": -0.009578559939882325,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5338531808971592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.018914108895518034,
            "ttft_change_pct": 0.02751878433340238
          },
          "tool-call": {
            "e2e_change_pct": 0.05219723423073308,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3193083371425995,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.004223994037633183,
            "ttft_change_pct": 0.07140390492312854
          },
          "tool-final": {
            "e2e_change_pct": 0.029716584893924036,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0618434628334228,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.014015774385445212,
            "ttft_change_pct": 0.21756866882225445
          }
        }
      },
      "complete": true
    }
  }
}
```
