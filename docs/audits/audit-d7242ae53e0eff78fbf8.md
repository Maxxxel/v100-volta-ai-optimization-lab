# Public audit excerpt

Original SHA256: `d7242ae53e0eff78fbf8e5e559775814de49f5925295d06b3c2b9c4fb442816c`

Original file: `RESULTS.json`; 43140 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.665856859,
              "format_passes": 2,
              "gpu_energy_j": 174.1859533396086,
              "semantic_passes": 2,
              "tokens_per_s": 79.32474762637611,
              "ttft_s": 0.12373884600000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6585513975,
              "format_passes": 0,
              "gpu_energy_j": 458.88268366949006,
              "semantic_passes": 0,
              "tokens_per_s": 79.6317627173704,
              "ttft_s": 0.063335379
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238575606,
              "format_passes": 2,
              "gpu_energy_j": 51.281040612990324,
              "semantic_passes": 2,
              "tokens_per_s": 78.07686021112346,
              "ttft_s": 0.0720579835
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2430616685,
              "format_passes": 0,
              "gpu_energy_j": 58.06400490631509,
              "semantic_passes": 0,
              "tokens_per_s": 77.52472186442297,
              "ttft_s": 0.1269433855
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1846805995,
              "format_passes": 2,
              "gpu_energy_j": 41.703276152174766,
              "semantic_passes": 2,
              "tokens_per_s": 76.23476262650975,
              "ttft_s": 0.06659285549999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35759203500000003,
              "format_passes": 0,
              "gpu_energy_j": 89.42559752570847,
              "semantic_passes": 0,
              "tokens_per_s": 78.8498116491487,
              "ttft_s": 0.0785463475
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4698248685,
              "format_passes": 0,
              "gpu_energy_j": 117.00496654437318,
              "semantic_passes": 2,
              "tokens_per_s": 78.98263943787353,
              "ttft_s": 0.1153077195
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0825291075,
              "format_passes": 2,
              "gpu_energy_j": 290.78033715256134,
              "semantic_passes": 2,
              "tokens_per_s": 77.90073722510397,
              "ttft_s": 0.8257663184999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2346566595,
              "format_passes": 0,
              "gpu_energy_j": 55.35708185523059,
              "semantic_passes": 0,
              "tokens_per_s": 78.19598460712794,
              "ttft_s": 0.06836758500000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1992253955,
              "format_passes": 0,
              "gpu_energy_j": 49.06514442392603,
              "semantic_passes": 0,
              "tokens_per_s": 2548.8406372240697,
              "ttft_s": 0.19904628800000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7191376725,
              "format_passes": 0,
              "gpu_energy_j": 189.69874323742448,
              "semantic_passes": 0,
              "tokens_per_s": 2852.9996311209707,
              "ttft_s": 0.718869888
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4202696449999999,
              "format_passes": 0,
              "gpu_energy_j": 378.43791473961716,
              "semantic_passes": 0,
              "tokens_per_s": 2887.4068472762838,
              "ttft_s": 1.4199462999999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29641413650000004,
              "format_passes": 2,
              "gpu_energy_j": 73.55360621589912,
              "semantic_passes": 2,
              "tokens_per_s": 78.13539652079152,
              "ttft_s": 0.0787820155
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.356130606,
              "format_passes": 2,
              "gpu_energy_j": 86.82438761109711,
              "semantic_passes": 2,
              "tokens_per_s": 77.88446650997679,
              "ttft_s": 0.0735820155
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3692428965,
              "format_passes": 2,
              "gpu_energy_j": 92.16107330540744,
              "semantic_passes": 2,
              "tokens_per_s": 78.87600272261353,
              "ttft_s": 0.0776377705
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6199173645,
              "format_passes": 0,
              "gpu_energy_j": 161.70393655442427,
              "semantic_passes": 0,
              "tokens_per_s": 79.01438399519944,
              "ttft_s": 0.31877632899999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5608496895,
              "format_passes": 0,
              "gpu_energy_j": 147.025702776638,
              "semantic_passes": 0,
              "tokens_per_s": 78.72492231175114,
              "ttft_s": 0.256688715
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
              "e2e_s": 0.6690403604999999,
              "format_passes": 2,
              "gpu_energy_j": 178.15583266755417,
              "semantic_passes": 2,
              "tokens_per_s": 78.88997036220368,
              "ttft_s": 0.1239021315
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.659608572,
              "format_passes": 0,
              "gpu_energy_j": 458.0511914290209,
              "semantic_passes": 0,
              "tokens_per_s": 79.56244414613715,
              "ttft_s": 0.06316530100000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23757902749999998,
              "format_passes": 2,
              "gpu_energy_j": 56.703648538949054,
              "semantic_passes": 2,
              "tokens_per_s": 78.33944995283684,
              "ttft_s": 0.0715768805
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241569603,
              "format_passes": 0,
              "gpu_energy_j": 58.17103708030701,
              "semantic_passes": 0,
              "tokens_per_s": 77.50739885643648,
              "ttft_s": 0.1254154395
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182189791,
              "format_passes": 2,
              "gpu_energy_j": 40.08237396414334,
              "semantic_passes": 2,
              "tokens_per_s": 77.38387298356315,
              "ttft_s": 0.065838908
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35902755,
              "format_passes": 0,
              "gpu_energy_j": 91.51351990463058,
              "semantic_passes": 0,
              "tokens_per_s": 78.56067387878377,
              "ttft_s": 0.078996013
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.470038544,
              "format_passes": 0,
              "gpu_energy_j": 115.34905773907552,
              "semantic_passes": 2,
              "tokens_per_s": 79.11461819195665,
              "ttft_s": 0.116056151
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0812288795,
              "format_passes": 2,
              "gpu_energy_j": 287.09023978205505,
              "semantic_passes": 2,
              "tokens_per_s": 77.65322929625272,
              "ttft_s": 0.8235850585
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2335117295,
              "format_passes": 0,
              "gpu_energy_j": 55.75614400098175,
              "semantic_passes": 0,
              "tokens_per_s": 78.13717011080456,
              "ttft_s": 0.06707996050000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19945403750000001,
              "format_passes": 0,
              "gpu_energy_j": 48.26801318938139,
              "semantic_passes": 0,
              "tokens_per_s": 2545.5274050130843,
              "ttft_s": 0.199318312
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7177415375,
              "format_passes": 0,
              "gpu_energy_j": 191.68203487056795,
              "semantic_passes": 0,
              "tokens_per_s": 2858.43580858296,
              "ttft_s": 0.717455619
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4193795310000001,
              "format_passes": 0,
              "gpu_energy_j": 384.67759055810876,
              "semantic_passes": 0,
              "tokens_per_s": 2889.2789298400216,
              "ttft_s": 1.419031073
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29534433800000004,
              "format_passes": 2,
              "gpu_energy_j": 68.21625426580772,
              "semantic_passes": 2,
              "tokens_per_s": 78.56106743326352,
              "ttft_s": 0.0788963895
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.352831877,
              "format_passes": 2,
              "gpu_energy_j": 89.94943260463185,
              "semantic_passes": 2,
              "tokens_per_s": 78.8097076798049,
              "ttft_s": 0.0735863775
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369352515,
              "format_passes": 2,
              "gpu_energy_j": 95.27029664592894,
              "semantic_passes": 2,
              "tokens_per_s": 78.77702656240493,
              "ttft_s": 0.07735417450000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620783926,
              "format_passes": 0,
              "gpu_energy_j": 163.91694802552544,
              "semantic_passes": 0,
              "tokens_per_s": 78.8732137242823,
              "ttft_s": 0.319185712
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56191974,
              "format_passes": 0,
              "gpu_energy_j": 145.94764903945324,
              "semantic_passes": 0,
              "tokens_per_s": 78.59357108268975,
              "ttft_s": 0.25694390349999996
            }
          }
        }
      },
      "change_exercised": false,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.4781059858391945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2791041710496174,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5480978851899354,
            "ttft_change_pct": 0.13195977276205806
          },
          "decode": {
            "e2e_change_pct": 0.06374083441693656,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1811993065024997,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0870488971583816,
            "ttft_change_pct": -0.26853553682846254
          },
          "energy": {
            "e2e_change_pct": -0.41772020061431325,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.574293854296513,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.33632210747631675,
            "ttft_change_pct": -0.6676609261484723
          },
          "filtering": {
            "e2e_change_pct": -0.6138629382444138,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.18433481149744413,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.022345140453117196,
            "ttft_change_pct": -1.203643651051045
          },
          "german": {
            "e2e_change_pct": -1.3487115088122725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.886750245032955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.5073311930977384,
            "ttft_change_pct": -1.132174757095361
          },
          "ha_sim": {
            "e2e_change_pct": 0.4014393105819414,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.334815127538703,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3666943069585038,
            "ttft_change_pct": 0.5724842902465888
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.045479819040283864,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4152465952542825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16709843457045626,
            "ttft_change_pct": 0.6490731958322948
          },
          "long_context": {
            "e2e_change_pct": -0.12011021144759937,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2690326335821789,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3177221906591754,
            "ttft_change_pct": -0.264149790459145
          },
          "math": {
            "e2e_change_pct": -0.4879171136415228,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7208872512369568,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07521421543430495,
            "ttft_change_pct": -1.8833845015879924
          },
          "prefill": {
            "e2e_change_pct": 0.11476548932236597,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.624638516616539,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12998977506079035,
            "ttft_change_pct": 0.1366636890008044
          },
          "prefill2048": {
            "e2e_change_pct": -0.19414015610481616,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0454953993349392,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19054252242765024,
            "ttft_change_pct": -0.19673504532714547
          },
          "prefill4096": {
            "e2e_change_pct": -0.06267218363310567,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6487977487099181,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06483611983894022,
            "ttft_change_pct": -0.06445504312381223
          },
          "pve_sim": {
            "e2e_change_pct": -0.3609134546118331,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -7.256410969742088,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5447862702772976,
            "ttft_change_pct": 0.14517780393674684
          },
          "sorting": {
            "e2e_change_pct": -0.9262694484618361,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.599270987700387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.18796624190729,
            "ttft_change_pct": 0.005928078988270968
          },
          "time": {
            "e2e_change_pct": 0.029687368677655535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3736839524622475,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.125483235448276,
            "ttft_change_pct": -0.3652809684945635
          },
          "tool-call": {
            "e2e_change_pct": 0.1397866150594007,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.368557573956375,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17866401505544083,
            "ttft_change_pct": 0.12842327448976398
          },
          "tool-final": {
            "e2e_change_pct": 0.19079095879572794,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7332416827978472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16684834383353664,
            "ttft_change_pct": 0.09941555085501985
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 341843544475488,
          "end_ns": 341844401569264,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 341888872021518,
          "end_ns": 341889429901824,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
