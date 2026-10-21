# Public audit excerpt

Original SHA256: `6e8ddb3eb116e0cc960d3f07b6b32bc6fdbda0ab7aa0ae3629188da9d00e947c`

Original file: `RESULTS.json`; 39612 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.526534256,
              "format_passes": 2,
              "gpu_energy_j": 131.9227334726433,
              "semantic_passes": 2,
              "tokens_per_s": 96.44074539040454,
              "ttft_s": 0.13246764700000002
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3671059965,
              "format_passes": 0,
              "gpu_energy_j": 356.5392905146884,
              "semantic_passes": 0,
              "tokens_per_s": 97.00884514657628,
              "ttft_s": 0.057842135
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20478219749999999,
              "format_passes": 2,
              "gpu_energy_j": 45.998757069747555,
              "semantic_passes": 2,
              "tokens_per_s": 95.07674392046607,
              "ttft_s": 0.068002142
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.230054916,
              "format_passes": 0,
              "gpu_energy_j": 55.346453929872354,
              "semantic_passes": 0,
              "tokens_per_s": 93.7289999641564,
              "ttft_s": 0.1340153485
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1569537605,
              "format_passes": 2,
              "gpu_energy_j": 31.988323374284715,
              "semantic_passes": 2,
              "tokens_per_s": 93.89454116998485,
              "ttft_s": 0.061076231
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30756892,
              "format_passes": 0,
              "gpu_energy_j": 72.40807752589394,
              "semantic_passes": 0,
              "tokens_per_s": 95.72290510705055,
              "ttft_s": 0.07769138
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.398420334,
              "format_passes": 0,
              "gpu_energy_j": 95.03754835935067,
              "semantic_passes": 2,
              "tokens_per_s": 96.22992462840926,
              "ttft_s": 0.10744247700000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.034277349,
              "format_passes": 2,
              "gpu_energy_j": 270.0304447838116,
              "semantic_passes": 2,
              "tokens_per_s": 94.16681187570842,
              "ttft_s": 0.874929254
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14895398399999998,
              "format_passes": 0,
              "gpu_energy_j": 32.88177992936744,
              "semantic_passes": 0,
              "tokens_per_s": 93.47988000770948,
              "ttft_s": 0.0633964655
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20597496799999998,
              "format_passes": 0,
              "gpu_energy_j": 49.76139203239579,
              "semantic_passes": 0,
              "tokens_per_s": 2464.061030036185,
              "ttft_s": 0.20583901500000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7581203375000001,
              "format_passes": 0,
              "gpu_energy_j": 200.19957599625047,
              "semantic_passes": 0,
              "tokens_per_s": 2706.068539315559,
              "ttft_s": 0.7578581904999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5034075169999999,
              "format_passes": 0,
              "gpu_energy_j": 406.8306536791134,
              "semantic_passes": 0,
              "tokens_per_s": 2727.617162554762,
              "ttft_s": 1.5030764765
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254221178,
              "format_passes": 2,
              "gpu_energy_j": 59.21293258688523,
              "semantic_passes": 2,
              "tokens_per_s": 95.65247811380524,
              "ttft_s": 0.0762898105
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3506980765,
              "format_passes": 0,
              "gpu_energy_j": 83.90743450218766,
              "semantic_passes": 2,
              "tokens_per_s": 96.1533438701131,
              "ttft_s": 0.0698438255
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31459997,
              "format_passes": 0,
              "gpu_energy_j": 74.97386487120272,
              "semantic_passes": 0,
              "tokens_per_s": 96.01038687165999,
              "ttft_s": 0.0749934595
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5513658845,
              "format_passes": 0,
              "gpu_energy_j": 138.86974225688402,
              "semantic_passes": 0,
              "tokens_per_s": 96.15693693707424,
              "ttft_s": 0.304238165
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524767862,
              "format_passes": 0,
              "gpu_energy_j": 129.38736389674892,
              "semantic_passes": 0,
              "tokens_per_s": 95.81586449634798,
              "ttft_s": 0.2744456845
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
              "e2e_s": 0.5272884125,
              "format_passes": 2,
              "gpu_energy_j": 132.2263485345781,
              "semantic_passes": 2,
              "tokens_per_s": 96.27531389702142,
              "ttft_s": 0.132532223
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3664171139999999,
              "format_passes": 0,
              "gpu_energy_j": 356.54881316200624,
              "semantic_passes": 0,
              "tokens_per_s": 97.05799823383524,
              "ttft_s": 0.0576925365
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20494324,
              "format_passes": 2,
              "gpu_energy_j": 45.451105189452505,
              "semantic_passes": 2,
              "tokens_per_s": 94.94595870871254,
              "ttft_s": 0.067979173
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2307574855,
              "format_passes": 0,
              "gpu_energy_j": 54.22769263735378,
              "semantic_passes": 0,
              "tokens_per_s": 93.48486397356164,
              "ttft_s": 0.1344804855
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15719455,
              "format_passes": 2,
              "gpu_energy_j": 31.773484984175504,
              "semantic_passes": 2,
              "tokens_per_s": 93.94989856480854,
              "ttft_s": 0.061347682
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30702276500000003,
              "format_passes": 0,
              "gpu_energy_j": 70.17202524260412,
              "semantic_passes": 0,
              "tokens_per_s": 95.7943498719219,
              "ttft_s": 0.077344109
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39835896049999997,
              "format_passes": 0,
              "gpu_energy_j": 93.54999130632368,
              "semantic_passes": 2,
              "tokens_per_s": 96.23530910161884,
              "ttft_s": 0.107372507
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0297750040000002,
              "format_passes": 2,
              "gpu_energy_j": 277.58496235732116,
              "semantic_passes": 2,
              "tokens_per_s": 94.20130650278362,
              "ttft_s": 0.8705143915
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14917163,
              "format_passes": 0,
              "gpu_energy_j": 33.301686393886726,
              "semantic_passes": 0,
              "tokens_per_s": 93.4659145566892,
              "ttft_s": 0.0635797805
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2063322075,
              "format_passes": 0,
              "gpu_energy_j": 50.19175353535084,
              "semantic_passes": 0,
              "tokens_per_s": 2459.880806561499,
              "ttft_s": 0.2061958245
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7564430325,
              "format_passes": 0,
              "gpu_energy_j": 199.94324404368496,
              "semantic_passes": 0,
              "tokens_per_s": 2712.056816715757,
              "ttft_s": 0.7561514145
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.501755867,
              "format_passes": 0,
              "gpu_energy_j": 407.4247402412632,
              "semantic_passes": 0,
              "tokens_per_s": 2730.5483767476585,
              "ttft_s": 1.501432731
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25459332300000004,
              "format_passes": 2,
              "gpu_energy_j": 56.89738253743623,
              "semantic_passes": 2,
              "tokens_per_s": 95.544210987006,
              "ttft_s": 0.0766175885
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.350731444,
              "format_passes": 0,
              "gpu_energy_j": 83.11040512593779,
              "semantic_passes": 2,
              "tokens_per_s": 96.22346123559848,
              "ttft_s": 0.070088216
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31469981550000004,
              "format_passes": 0,
              "gpu_energy_j": 75.2043802940699,
              "semantic_passes": 0,
              "tokens_per_s": 95.9558812439011,
              "ttft_s": 0.074949814
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5507090715,
              "format_passes": 0,
              "gpu_energy_j": 138.71180145775344,
              "semantic_passes": 0,
              "tokens_per_s": 96.12709777970974,
              "ttft_s": 0.303588729
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.525592574,
              "format_passes": 0,
              "gpu_energy_j": 134.6283151605341,
              "semantic_passes": 0,
              "tokens_per_s": 95.68731510240913,
              "ttft_s": 0.27499153649999997
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
            "e2e_change_pct": 0.14323028205784905,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.23014612716296678,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17153692945179877,
            "ttft_change_pct": 0.048748506871243436
          },
          "decode": {
            "e2e_change_pct": -0.05038983822497345,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.002670854957975699,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0506686655064259,
            "ttft_change_pct": -0.25863239660846027
          },
          "energy": {
            "e2e_change_pct": 0.07864086916051782,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.190579735588615,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13755752075705896,
            "ttft_change_pct": -0.033776877204838573
          },
          "filtering": {
            "e2e_change_pct": 0.30539208299291687,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.0213784498933185,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2604700686960504,
            "ttft_change_pct": 0.3470774095700069
          },
          "german": {
            "e2e_change_pct": 0.1534142917206438,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6716150377606755,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05895698954796469,
            "ttft_change_pct": 0.444446220003325
          },
          "ha_sim": {
            "e2e_change_pct": -0.1775715829804847,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0881254684467785,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07463706287584859,
            "ttft_change_pct": -0.44698781254756126
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.015404208762104243,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5652308784337765,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005595424947446581,
            "ttft_change_pct": -0.06512321937626186
          },
          "long_context": {
            "e2e_change_pct": -0.43531312025278934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.797654012516171,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03663140589353908,
            "ttft_change_pct": -0.5045965122112639
          },
          "math": {
            "e2e_change_pct": 0.1461162663497495,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2770186572055309,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.014939526044677187,
            "ttft_change_pct": 0.28915649879566185
          },
          "prefill": {
            "e2e_change_pct": 0.17343830828997486,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8648502089227739,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1696477247815853,
            "ttft_change_pct": 0.17334396008452657
          },
          "prefill2048": {
            "e2e_change_pct": -0.22124521887002535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.12803820951664546,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22129067734968366,
            "ttft_change_pct": -0.22521047095550584
          },
          "prefill4096": {
            "e2e_change_pct": -0.10986043247247501,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.14602797423872715,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10746428175978373,
            "ttft_change_pct": -0.10935874027032666
          },
          "pve_sim": {
            "e2e_change_pct": 0.14638630932630736,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.910547828468569,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11318799986597128,
            "ttft_change_pct": 0.42964846530848533
          },
          "sorting": {
            "e2e_change_pct": 0.009514594529003162,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.949891247394874,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07292244103345169,
            "ttft_change_pct": 0.3499099573232911
          },
          "time": {
            "e2e_change_pct": 0.031737288468280944,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3074610376071485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0567705532024787,
            "ttft_change_pct": -0.0581990753473538
          },
          "tool-call": {
            "e2e_change_pct": -0.11912470801409558,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.11373305412955004,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.03103172617074934,
            "ttft_change_pct": -0.21346302821673158
          },
          "tool-final": {
            "e2e_change_pct": 0.15715748995315248,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.050589722167497,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13416295371811993,
            "ttft_change_pct": 0.1988925426152699
          }
        }
      },
      "complete": true
    }
  }
}
```
