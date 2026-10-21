# Public audit excerpt

Original SHA256: `2d48a4fdae7ce747ef64980e98b6fc659cced31dd640ef070ffdbadc2fa3ba03`

Original file: `RESULTS.json`; 39691 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6662284155,
              "format_passes": 2,
              "gpu_energy_j": 175.99046039894301,
              "semantic_passes": 2,
              "tokens_per_s": 79.29735594774897,
              "ttft_s": 0.123953793
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6582831800000002,
              "format_passes": 0,
              "gpu_energy_j": 457.41976295994687,
              "semantic_passes": 0,
              "tokens_per_s": 79.62410072374433,
              "ttft_s": 0.06289774149999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23760477000000002,
              "format_passes": 2,
              "gpu_energy_j": 56.23151694008101,
              "semantic_passes": 2,
              "tokens_per_s": 78.34045956208888,
              "ttft_s": 0.0716288585
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242435001,
              "format_passes": 0,
              "gpu_energy_j": 54.709912575940834,
              "semantic_passes": 0,
              "tokens_per_s": 76.9072909581273,
              "ttft_s": 0.1254511665
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18283022,
              "format_passes": 2,
              "gpu_energy_j": 41.30464451884724,
              "semantic_passes": 2,
              "tokens_per_s": 77.48910929729473,
              "ttft_s": 0.06665810150000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3580600905,
              "format_passes": 0,
              "gpu_energy_j": 90.00901720243161,
              "semantic_passes": 0,
              "tokens_per_s": 78.80376470284224,
              "ttft_s": 0.0788238285
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.474700883,
              "format_passes": 0,
              "gpu_energy_j": 121.06206021514345,
              "semantic_passes": 2,
              "tokens_per_s": 77.77223138188319,
              "ttft_s": 0.1145675655
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.07888978,
              "format_passes": 2,
              "gpu_energy_j": 288.21490027435874,
              "semantic_passes": 2,
              "tokens_per_s": 77.8833096021362,
              "ttft_s": 0.8220827875000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23330273699999998,
              "format_passes": 0,
              "gpu_energy_j": 52.100452023649666,
              "semantic_passes": 0,
              "tokens_per_s": 78.31570196915654,
              "ttft_s": 0.06723380849999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199040386,
              "format_passes": 0,
              "gpu_energy_j": 49.791192201737324,
              "semantic_passes": 0,
              "tokens_per_s": 2551.387893657037,
              "ttft_s": 0.19879369549999998
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7178700174999999,
              "format_passes": 0,
              "gpu_energy_j": 190.11659947919208,
              "semantic_passes": 0,
              "tokens_per_s": 2858.1621206936807,
              "ttft_s": 0.71764172
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4184856715,
              "format_passes": 0,
              "gpu_energy_j": 380.0652477647043,
              "semantic_passes": 0,
              "tokens_per_s": 2891.7457543710507,
              "ttft_s": 1.41816015
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2953711375,
              "format_passes": 2,
              "gpu_energy_j": 73.11912255803306,
              "semantic_passes": 2,
              "tokens_per_s": 78.57770779384582,
              "ttft_s": 0.0789672565
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353006973,
              "format_passes": 2,
              "gpu_energy_j": 89.60590390702836,
              "semantic_passes": 2,
              "tokens_per_s": 78.81103558198598,
              "ttft_s": 0.073813569
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3691081485,
              "format_passes": 2,
              "gpu_energy_j": 93.22580368850902,
              "semantic_passes": 2,
              "tokens_per_s": 78.83624332567784,
              "ttft_s": 0.07732352649999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194751515,
              "format_passes": 0,
              "gpu_energy_j": 163.85366011588536,
              "semantic_passes": 0,
              "tokens_per_s": 79.01950502201052,
              "ttft_s": 0.318241475
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5601811585,
              "format_passes": 0,
              "gpu_energy_j": 146.8323938677396,
              "semantic_passes": 0,
              "tokens_per_s": 78.83300301420968,
              "ttft_s": 0.255685973
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
              "e2e_s": 0.670954753,
              "format_passes": 2,
              "gpu_energy_j": 177.801645170273,
              "semantic_passes": 2,
              "tokens_per_s": 78.59386407784993,
              "ttft_s": 0.1237101565
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.65859377,
              "format_passes": 0,
              "gpu_energy_j": 454.5839878464575,
              "semantic_passes": 0,
              "tokens_per_s": 79.61613768897081,
              "ttft_s": 0.0635642465
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23780038,
              "format_passes": 2,
              "gpu_energy_j": 52.00185793450173,
              "semantic_passes": 2,
              "tokens_per_s": 78.36171414877842,
              "ttft_s": 0.071857012
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241406248,
              "format_passes": 0,
              "gpu_energy_j": 54.45724674998764,
              "semantic_passes": 0,
              "tokens_per_s": 77.62715794438377,
              "ttft_s": 0.125421755
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1820848075,
              "format_passes": 2,
              "gpu_energy_j": 39.542306730438355,
              "semantic_passes": 2,
              "tokens_per_s": 77.60270842962949,
              "ttft_s": 0.0660686675
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3572985785,
              "format_passes": 0,
              "gpu_energy_j": 90.13348312565054,
              "semantic_passes": 0,
              "tokens_per_s": 78.88189353150626,
              "ttft_s": 0.078383058
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46870233549999996,
              "format_passes": 0,
              "gpu_energy_j": 119.08619819280807,
              "semantic_passes": 2,
              "tokens_per_s": 79.1078066082308,
              "ttft_s": 0.11473008700000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.080148877,
              "format_passes": 2,
              "gpu_energy_j": 288.379653571106,
              "semantic_passes": 2,
              "tokens_per_s": 77.91586981429325,
              "ttft_s": 0.8234206740000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233167369,
              "format_passes": 0,
              "gpu_energy_j": 54.86781670159864,
              "semantic_passes": 0,
              "tokens_per_s": 78.3658908610005,
              "ttft_s": 0.0672104825
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198602617,
              "format_passes": 0,
              "gpu_energy_j": 49.39437244698871,
              "semantic_passes": 0,
              "tokens_per_s": 2556.700857931718,
              "ttft_s": 0.19844897449999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7172844190000001,
              "format_passes": 0,
              "gpu_energy_j": 191.050148331652,
              "semantic_passes": 0,
              "tokens_per_s": 2860.3109764844166,
              "ttft_s": 0.7170565025
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.416923665,
              "format_passes": 0,
              "gpu_energy_j": 383.0114409651348,
              "semantic_passes": 0,
              "tokens_per_s": 2894.26862024022,
              "ttft_s": 1.416621943
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295506527,
              "format_passes": 2,
              "gpu_energy_j": 73.94470491858709,
              "semantic_passes": 2,
              "tokens_per_s": 78.46911396221924,
              "ttft_s": 0.0788467615
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35314539050000004,
              "format_passes": 2,
              "gpu_energy_j": 90.01965112807522,
              "semantic_passes": 2,
              "tokens_per_s": 78.85700394298902,
              "ttft_s": 0.074110029
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369552124,
              "format_passes": 2,
              "gpu_energy_j": 94.2455783263218,
              "semantic_passes": 2,
              "tokens_per_s": 78.73869203485258,
              "ttft_s": 0.07739734649999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6194574065,
              "format_passes": 0,
              "gpu_energy_j": 161.9736585735231,
              "semantic_passes": 0,
              "tokens_per_s": 79.04996402823622,
              "ttft_s": 0.318437261
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559990561,
              "format_passes": 0,
              "gpu_energy_j": 147.1609899784661,
              "semantic_passes": 0,
              "tokens_per_s": 78.81851338688226,
              "ttft_s": 0.2553867385
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
            "e2e_change_pct": 0.7094169792281946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0291380380642812,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8871567803125591,
            "ttft_change_pct": -0.19655429180776007
          },
          "decode": {
            "e2e_change_pct": 0.01872961166982101,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6199502826767178,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01000078456289133,
            "ttft_change_pct": 1.0596644396206445
          },
          "energy": {
            "e2e_change_pct": 0.08232578832485515,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -7.521865380381443,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.027131046726491803,
            "ttft_change_pct": 0.3185217589360301
          },
          "filtering": {
            "e2e_change_pct": -0.4243417805830818,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4618282392655604,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.936019169688862,
            "ttft_change_pct": -0.023444580724563124
          },
          "german": {
            "e2e_change_pct": -0.40770748949489066,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.266681892407364,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14660012660479005,
            "ttft_change_pct": -0.8842646081062111
          },
          "ha_sim": {
            "e2e_change_pct": -0.21267715118336028,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.13828161565081487,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09914352310278485,
            "ttft_change_pct": -0.5591843334531665
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.263647849587013,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6321067218119434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.717290609535893,
            "ttft_change_pct": 0.14185646634867766
          },
          "long_context": {
            "e2e_change_pct": 0.1167030241031819,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.05716335157912589,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04180640540749625,
            "ttft_change_pct": 0.1627435241733588
          },
          "math": {
            "e2e_change_pct": -0.05802246546295908,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.311594372910244,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06408535016864114,
            "ttft_change_pct": -0.03469385495243893
          },
          "prefill": {
            "e2e_change_pct": -0.21993978649137436,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7969677712090784,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20823820195625675,
            "ttft_change_pct": -0.17340640463117118
          },
          "prefill2048": {
            "e2e_change_pct": -0.08157444742422637,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4910401590483504,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07518313167673707,
            "ttft_change_pct": -0.08154730747818029
          },
          "prefill4096": {
            "e2e_change_pct": -0.11011789060569876,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7751808979532093,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08724369579711233,
            "ttft_change_pct": -0.10846497132217525
          },
          "pve_sim": {
            "e2e_change_pct": 0.04583707844509899,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1290922698077965,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13819928663671988,
            "ttft_change_pct": -0.15258856055103687
          },
          "sorting": {
            "e2e_change_pct": 0.03921098181820515,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4617410271048117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05832731503092603,
            "ttft_change_pct": 0.40163347202464283
          },
          "time": {
            "e2e_change_pct": 0.12028331040758733,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0938759414937493,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12373914168166689,
            "ttft_change_pct": 0.09546900321468765
          },
          "tool-call": {
            "e2e_change_pct": -0.0028645216772593685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1473662175337629,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03854618706762292,
            "ttft_change_pct": 0.0615212080700811
          },
          "tool-final": {
            "e2e_change_pct": -0.03402426109981871,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.22378992950458088,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.018380153962682666,
            "ttft_change_pct": -0.11703203601239887
          }
        }
      },
      "complete": true
    }
  }
}
```
