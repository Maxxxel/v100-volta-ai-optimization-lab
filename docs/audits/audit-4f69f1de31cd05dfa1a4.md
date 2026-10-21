# Public audit excerpt

Original SHA256: `4f69f1de31cd05dfa1a494d4662cd4377dcbc96d5872a9189c7a0c38b4c6dfd0`

Original file: `RESULTS.json`; 39613 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.526547614,
              "format_passes": 2,
              "gpu_energy_j": 132.58765345792506,
              "semantic_passes": 2,
              "tokens_per_s": 96.40425815557971,
              "ttft_s": 0.1324004635
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.366448863,
              "format_passes": 0,
              "gpu_energy_j": 357.86911808227467,
              "semantic_passes": 0,
              "tokens_per_s": 97.04680249438529,
              "ttft_s": 0.057829741000000004
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20464705649999998,
              "format_passes": 2,
              "gpu_energy_j": 47.22527286036993,
              "semantic_passes": 2,
              "tokens_per_s": 95.0417514817762,
              "ttft_s": 0.067827519
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2303808135,
              "format_passes": 0,
              "gpu_energy_j": 56.067017286328564,
              "semantic_passes": 0,
              "tokens_per_s": 93.73738349843758,
              "ttft_s": 0.1343433705
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1571072435,
              "format_passes": 2,
              "gpu_energy_j": 32.32987332502067,
              "semantic_passes": 2,
              "tokens_per_s": 93.81792039007647,
              "ttft_s": 0.0611719795
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30719436499999997,
              "format_passes": 0,
              "gpu_energy_j": 69.07289763286363,
              "semantic_passes": 0,
              "tokens_per_s": 95.70824016102083,
              "ttft_s": 0.0772841235
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39879119900000004,
              "format_passes": 0,
              "gpu_energy_j": 92.94534771242118,
              "semantic_passes": 2,
              "tokens_per_s": 96.18854121555154,
              "ttft_s": 0.1076594655
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0349565795000002,
              "format_passes": 2,
              "gpu_energy_j": 271.3306205477177,
              "semantic_passes": 2,
              "tokens_per_s": 94.18694578710964,
              "ttft_s": 0.87565907
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14947390300000002,
              "format_passes": 0,
              "gpu_energy_j": 29.558330974253998,
              "semantic_passes": 0,
              "tokens_per_s": 93.1485104178128,
              "ttft_s": 0.063619746
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2060041375,
              "format_passes": 0,
              "gpu_energy_j": 50.2040148064594,
              "semantic_passes": 0,
              "tokens_per_s": 2464.514983805673,
              "ttft_s": 0.20581768849999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7566281735,
              "format_passes": 0,
              "gpu_energy_j": 201.66268353038674,
              "semantic_passes": 0,
              "tokens_per_s": 2711.119819991836,
              "ttft_s": 0.7564046625
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5016463135,
              "format_passes": 0,
              "gpu_energy_j": 403.56845080458424,
              "semantic_passes": 0,
              "tokens_per_s": 2730.8359837848875,
              "ttft_s": 1.5013109225
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25445486,
              "format_passes": 2,
              "gpu_energy_j": 59.82786784718383,
              "semantic_passes": 2,
              "tokens_per_s": 95.49037777365555,
              "ttft_s": 0.0763845625
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3511028445,
              "format_passes": 0,
              "gpu_energy_j": 83.33143718158686,
              "semantic_passes": 2,
              "tokens_per_s": 96.2270420882634,
              "ttft_s": 0.070474992
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31433708000000005,
              "format_passes": 0,
              "gpu_energy_j": 76.07900929485413,
              "semantic_passes": 0,
              "tokens_per_s": 96.09961803129208,
              "ttft_s": 0.074961456
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5506992589999999,
              "format_passes": 0,
              "gpu_energy_j": 135.77441487653078,
              "semantic_passes": 0,
              "tokens_per_s": 96.22325951519366,
              "ttft_s": 0.30362156149999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.525074275,
              "format_passes": 0,
              "gpu_energy_j": 135.52770504610476,
              "semantic_passes": 0,
              "tokens_per_s": 95.86425716913556,
              "ttft_s": 0.2747524845
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
              "e2e_s": 0.5291244655,
              "format_passes": 2,
              "gpu_energy_j": 133.38522099668523,
              "semantic_passes": 2,
              "tokens_per_s": 95.84067830940444,
              "ttft_s": 0.1325893325
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.37051035,
              "format_passes": 0,
              "gpu_energy_j": 356.8164259111577,
              "semantic_passes": 0,
              "tokens_per_s": 96.75125428495939,
              "ttft_s": 0.0579920695
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2052920205,
              "format_passes": 2,
              "gpu_energy_j": 45.28785610261443,
              "semantic_passes": 2,
              "tokens_per_s": 94.89578946414088,
              "ttft_s": 0.06822681950000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23424262099999998,
              "format_passes": 0,
              "gpu_energy_j": 56.01660892186614,
              "semantic_passes": 0,
              "tokens_per_s": 92.88229738417041,
              "ttft_s": 0.137426819
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157072193,
              "format_passes": 2,
              "gpu_energy_j": 33.34849280874502,
              "semantic_passes": 2,
              "tokens_per_s": 93.64612485257214,
              "ttft_s": 0.060914448499999996
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3116215055,
              "format_passes": 0,
              "gpu_energy_j": 71.947267508664,
              "semantic_passes": 0,
              "tokens_per_s": 94.56180665165728,
              "ttft_s": 0.07892991099999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.399201896,
              "format_passes": 0,
              "gpu_energy_j": 93.94516961020705,
              "semantic_passes": 2,
              "tokens_per_s": 96.12152766976997,
              "ttft_s": 0.1078676695
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0334738350000001,
              "format_passes": 2,
              "gpu_energy_j": 270.6598644049984,
              "semantic_passes": 2,
              "tokens_per_s": 94.05072739766717,
              "ttft_s": 0.873946009
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149038055,
              "format_passes": 0,
              "gpu_energy_j": 29.54007080291473,
              "semantic_passes": 0,
              "tokens_per_s": 93.62864566902054,
              "ttft_s": 0.0635517625
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206308149,
              "format_passes": 0,
              "gpu_energy_j": 50.94526715329527,
              "semantic_passes": 0,
              "tokens_per_s": 2460.0777722783196,
              "ttft_s": 0.206152605
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7563383085,
              "format_passes": 0,
              "gpu_energy_j": 202.97036039861237,
              "semantic_passes": 0,
              "tokens_per_s": 2712.187605246714,
              "ttft_s": 0.7560927575
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.502007471,
              "format_passes": 0,
              "gpu_energy_j": 405.350314163912,
              "semantic_passes": 0,
              "tokens_per_s": 2730.1476465846386,
              "ttft_s": 1.501681477
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2550244075,
              "format_passes": 2,
              "gpu_energy_j": 59.8268051318378,
              "semantic_passes": 2,
              "tokens_per_s": 95.32291966375792,
              "ttft_s": 0.076660595
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35205963100000004,
              "format_passes": 0,
              "gpu_energy_j": 83.18945046712935,
              "semantic_passes": 2,
              "tokens_per_s": 95.92524006122072,
              "ttft_s": 0.070559385
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31581965300000003,
              "format_passes": 0,
              "gpu_energy_j": 71.7165846236808,
              "semantic_passes": 0,
              "tokens_per_s": 95.7623104985455,
              "ttft_s": 0.0756037625
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5516258414999999,
              "format_passes": 0,
              "gpu_energy_j": 139.57496650175048,
              "semantic_passes": 0,
              "tokens_per_s": 95.87421758447883,
              "ttft_s": 0.303875758
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5256029965,
              "format_passes": 0,
              "gpu_energy_j": 132.32312359990243,
              "semantic_passes": 0,
              "tokens_per_s": 95.61545496691389,
              "ttft_s": 0.274630064
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
            "e2e_change_pct": 0.4893862267126181,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6015398251340676,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5846005736237836,
            "ttft_change_pct": 0.14264980273273054
          },
          "decode": {
            "e2e_change_pct": 0.29722934461544614,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2941556334220885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3045419342311728,
            "ttft_change_pct": 0.2807007211047319
          },
          "energy": {
            "e2e_change_pct": 0.31515918725175673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.102499870109433,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1535767337613847,
            "ttft_change_pct": 0.5886998461494652
          },
          "filtering": {
            "e2e_change_pct": 1.676271318488065,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.08990734107541254,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9122146174278645,
            "ttft_change_pct": 2.2951995982563256
          },
          "german": {
            "e2e_change_pct": -0.022309919784180288,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.1507066961998342,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18311590876245454,
            "ttft_change_pct": -0.4209950407114138
          },
          "ha_sim": {
            "e2e_change_pct": 1.4411529000540213,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.161357021791989,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.1978420117586208,
            "ttft_change_pct": 2.1295285829307398
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.10298547235489952,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.07570945979929,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06966894906056398,
            "ttft_change_pct": 0.1933912629354495
          },
          "long_context": {
            "e2e_change_pct": -0.14326634849902709,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2472098952065349,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14462555113566866,
            "ttft_change_pct": -0.1956310462244204
          },
          "math": {
            "e2e_change_pct": -0.29158802389740446,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.06177673345350021,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5154513465154942,
            "ttft_change_pct": -0.1068591188653989
          },
          "prefill": {
            "e2e_change_pct": 0.14757543401282547,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4764802171568503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18004400689427547,
            "ttft_change_pct": 0.16272483790915615
          },
          "prefill2048": {
            "e2e_change_pct": -0.038310098692095895,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6484476182370136,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03938539517893691,
            "ttft_change_pct": -0.04123520325338692
          },
          "prefill4096": {
            "e2e_change_pct": 0.024050769928529725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44152692208108135,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.025206098218133466,
            "ttft_change_pct": 0.024682062485958944
          },
          "pve_sim": {
            "e2e_change_pct": 0.2238304664332169,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.0017762881818650378,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17536647545218775,
            "ttft_change_pct": 0.3613721031654693
          },
          "sorting": {
            "e2e_change_pct": 0.2725089001664349,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.17038793432556654,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.31363535706091517,
            "ttft_change_pct": 0.11974886070225121
          },
          "time": {
            "e2e_change_pct": 0.4716506878539306,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.734071344523139,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3509977871470227,
            "ttft_change_pct": 0.856849018514283
          },
          "tool-call": {
            "e2e_change_pct": 0.16825562861344512,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.7991662705199705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.36274174505563916,
            "ttft_change_pct": 0.08372149156476993
          },
          "tool-final": {
            "e2e_change_pct": 0.1006946112528384,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.364521294824673,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2595359413078202,
            "ttft_change_pct": -0.04455664894997824
          }
        }
      },
      "complete": true
    }
  }
}
```
