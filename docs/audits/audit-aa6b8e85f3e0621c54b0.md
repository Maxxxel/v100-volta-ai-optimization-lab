# Public audit excerpt

Original SHA256: `aa6b8e85f3e0621c54b08a58d49dfe9e2ad34ce88e131d38bbd57322b1335098`

Original file: `RESULTS.json`; 43422 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
            "cache-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7198377385,
              "format_passes": 0,
              "gpu_energy_j": 191.01899351567192,
              "semantic_passes": 0,
              "ttft_s": 0.719608759
            },
            "cache-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7218445035000001,
              "format_passes": 0,
              "gpu_energy_j": 190.39165088781334,
              "semantic_passes": 0,
              "ttft_s": 0.721580224
            },
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.667425198,
              "format_passes": 2,
              "gpu_energy_j": 172.73923914201205,
              "semantic_passes": 2,
              "tokens_per_s": 79.12689314955867,
              "ttft_s": 0.123959
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658244053,
              "format_passes": 0,
              "gpu_energy_j": 454.08512094348384,
              "semantic_passes": 0,
              "tokens_per_s": 79.63625891020348,
              "ttft_s": 0.063118308
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2399610165,
              "format_passes": 2,
              "gpu_energy_j": 57.246959123651166,
              "semantic_passes": 2,
              "tokens_per_s": 77.60465458837167,
              "ttft_s": 0.07242454
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24179706,
              "format_passes": 0,
              "gpu_energy_j": 57.70597094193718,
              "semantic_passes": 0,
              "tokens_per_s": 77.50503240909958,
              "ttft_s": 0.125665153
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1833143055,
              "format_passes": 2,
              "gpu_energy_j": 42.99291981540087,
              "semantic_passes": 2,
              "tokens_per_s": 77.20640264548712,
              "ttft_s": 0.066687051
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357399313,
              "format_passes": 0,
              "gpu_energy_j": 90.36430655515424,
              "semantic_passes": 0,
              "tokens_per_s": 78.93426325849683,
              "ttft_s": 0.0786724455
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4727761425,
              "format_passes": 0,
              "gpu_energy_j": 119.53505789949085,
              "semantic_passes": 2,
              "tokens_per_s": 78.28743407730744,
              "ttft_s": 0.1150775745
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.079896491,
              "format_passes": 2,
              "gpu_energy_j": 288.2155518406904,
              "semantic_passes": 2,
              "tokens_per_s": 78.04895768186384,
              "ttft_s": 0.823591398
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2335526705,
              "format_passes": 0,
              "gpu_energy_j": 54.250314340144826,
              "semantic_passes": 0,
              "tokens_per_s": 78.24679718305458,
              "ttft_s": 0.06737103250000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198803632,
              "format_passes": 0,
              "gpu_energy_j": 48.949969756632385,
              "semantic_passes": 0,
              "tokens_per_s": 2553.3744962373794,
              "ttft_s": 0.1986576425
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.716234158,
              "format_passes": 0,
              "gpu_energy_j": 191.08260010822818,
              "semantic_passes": 0,
              "tokens_per_s": 2864.510496291233,
              "ttft_s": 0.715949452
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4171914335,
              "format_passes": 0,
              "gpu_energy_j": 381.3097153022468,
              "semantic_passes": 0,
              "tokens_per_s": 2893.8301718707453,
              "ttft_s": 1.41683769
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2949001495,
              "format_passes": 2,
              "gpu_energy_j": 74.95648105698587,
              "semantic_passes": 2,
              "tokens_per_s": 78.70917231785262,
              "ttft_s": 0.0788529225
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354077625,
              "format_passes": 2,
              "gpu_energy_j": 84.94170149178572,
              "semantic_passes": 2,
              "tokens_per_s": 78.64628397731515,
              "ttft_s": 0.0743175295
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36917725599999995,
              "format_passes": 2,
              "gpu_energy_j": 94.03643512616647,
              "semantic_passes": 2,
              "tokens_per_s": 78.96263761857442,
              "ttft_s": 0.077844065
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6203092095,
              "format_passes": 0,
              "gpu_energy_j": 160.5766227919356,
              "semantic_passes": 0,
              "tokens_per_s": 79.00178924207609,
              "ttft_s": 0.3189814945
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561103533,
              "format_passes": 0,
              "gpu_energy_j": 145.20243284352824,
              "semantic_passes": 0,
              "tokens_per_s": 78.79625623914538,
              "ttft_s": 0.2564527285
            }
          }
        },
        "B": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "cache-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7186236214999999,
              "format_passes": 0,
              "gpu_energy_j": 190.49976954030376,
              "semantic_passes": 0,
              "ttft_s": 0.7183759894999999
            },
            "cache-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.056152312,
              "format_passes": 0,
              "gpu_energy_j": 6.168229772068376,
              "semantic_passes": 0,
              "ttft_s": 0.0559162625
            },
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6680880645,
              "format_passes": 2,
              "gpu_energy_j": 178.05258043501647,
              "semantic_passes": 2,
              "tokens_per_s": 79.11870302329339,
              "ttft_s": 0.12457533
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658034405,
              "format_passes": 0,
              "gpu_energy_j": 459.5107225712003,
              "semantic_passes": 0,
              "tokens_per_s": 79.62529714594103,
              "ttft_s": 0.06294795149999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2377931815,
              "format_passes": 2,
              "gpu_energy_j": 59.53077945678358,
              "semantic_passes": 2,
              "tokens_per_s": 78.25152755178271,
              "ttft_s": 0.07163456200000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2415736775,
              "format_passes": 0,
              "gpu_energy_j": 62.21447197397265,
              "semantic_passes": 0,
              "tokens_per_s": 77.46485344408615,
              "ttft_s": 0.1253529965
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182457347,
              "format_passes": 2,
              "gpu_energy_j": 41.74075332306175,
              "semantic_passes": 2,
              "tokens_per_s": 77.36378664200902,
              "ttft_s": 0.0660915425
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35755814350000004,
              "format_passes": 0,
              "gpu_energy_j": 91.26608502543073,
              "semantic_passes": 0,
              "tokens_per_s": 78.85265040207607,
              "ttft_s": 0.078526313
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47087671600000003,
              "format_passes": 0,
              "gpu_energy_j": 118.8963876917962,
              "semantic_passes": 2,
              "tokens_per_s": 79.09228153802154,
              "ttft_s": 0.11684859950000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0810639544999998,
              "format_passes": 2,
              "gpu_energy_j": 289.0666754573408,
              "semantic_passes": 2,
              "tokens_per_s": 77.97288460870752,
              "ttft_s": 0.82452977
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23664120649999998,
              "format_passes": 0,
              "gpu_energy_j": 57.61450789903011,
              "semantic_passes": 0,
              "tokens_per_s": 76.84401048923193,
              "ttft_s": 0.0673291255
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19960544149999998,
              "format_passes": 0,
              "gpu_energy_j": 49.042248991631425,
              "semantic_passes": 0,
              "tokens_per_s": 2543.416685601727,
              "ttft_s": 0.199438687
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.719213703,
              "format_passes": 0,
              "gpu_energy_j": 188.4349212698458,
              "semantic_passes": 0,
              "tokens_per_s": 2852.6343116883563,
              "ttft_s": 0.7189323925
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.740392954,
              "format_passes": 0,
              "gpu_energy_j": 196.50465512696138,
              "semantic_passes": 0,
              "tokens_per_s": 2772.5150082017144,
              "ttft_s": 0.7400672285000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2987470635,
              "format_passes": 2,
              "gpu_energy_j": 74.78887556645742,
              "semantic_passes": 2,
              "tokens_per_s": 77.32945236969834,
              "ttft_s": 0.0787595675
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3528911925,
              "format_passes": 2,
              "gpu_energy_j": 87.94308450641651,
              "semantic_passes": 2,
              "tokens_per_s": 78.85997168627763,
              "ttft_s": 0.073817029
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369533312,
              "format_passes": 2,
              "gpu_energy_j": 95.05858193380887,
              "semantic_passes": 2,
              "tokens_per_s": 78.90968244917147,
              "ttft_s": 0.0780507265
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6209720995,
              "format_passes": 0,
              "gpu_energy_j": 162.45228505731865,
              "semantic_passes": 0,
              "tokens_per_s": 78.99179559760131,
              "ttft_s": 0.319694323
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.4043326265,
              "format_passes": 0,
              "gpu_energy_j": 99.58142871698884,
              "semantic_passes": 0,
              "tokens_per_s": 78.9011722894461,
              "ttft_s": 0.1000866175
            }
          }
        }
      },
      "cache": {
        "arms": {
          "A": {
            "hits": 0,
            "repeat_e2e_s": 0.7218445035000001,
            "repeat_ttft_s": 0.721580224
          },
          "B": {
            "hits": 6,
            "repeat_e2e_s": 0.056152312,
            "repeat_ttft_s": 0.0559162625
          }
        },
        "change_exercised": true,
        "note": "Identical total input; cached and evaluated tokens differ. Latency is reported separately from uncached token throughput."
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "cache-prime": {
            "e2e_change_pct": -0.16866537207816945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2718179830245804,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "ttft_change_pct": -0.17131107488368436
          },
          "cache-repeat": {
            "e2e_change_pct": -92.22099611097198,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -96.760241458433,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "ttft_change_pct": -92.25085989884334
          },
          "code": {
            "e2e_change_pct": 0.09931697244669468,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.0759318608762687,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01035062282781496,
            "ttft_change_pct": 0.49720472091578927
          },
          "decode": {
            "e2e_change_pct": -0.012642771106019524,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1948424155460824,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.01376479057713098,
            "ttft_change_pct": -0.2699002958064245
          },
          "energy": {
            "e2e_change_pct": -0.9034113255642073,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.9894177229561567,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8335491818656671,
            "ttft_change_pct": -1.0907601208098527
          },
          "filtering": {
            "e2e_change_pct": -0.09238429119030611,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.812884799342257,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05184045959927275,
            "ttft_change_pct": -0.2484033899198712
          },
          "german": {
            "e2e_change_pct": -0.46748042803457235,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.91249465659823,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.20384837413622847,
            "ttft_change_pct": -0.8929897050028446
          },
          "ha_sim": {
            "e2e_change_pct": 0.04444062823367734,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9979365798885143,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10339344798023786,
            "ttft_change_pct": -0.18574800754095344
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.4017602262999076,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5342953096083791,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.0280672373542465,
            "ttft_change_pct": 1.5389836010142988
          },
          "long_context": {
            "e2e_change_pct": 0.10810883355298895,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2953080120814855,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09746840369913023,
            "ttft_change_pct": 0.11393659553495805
          },
          "math": {
            "e2e_change_pct": 1.322415193706794,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.201242517770633,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.7927720294300342,
            "ttft_change_pct": -0.06220329189701168
          },
          "prefill": {
            "e2e_change_pct": 0.40331732973568624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.18851745048633628,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3899862965783596,
            "ttft_change_pct": 0.3931610635115712
          },
          "prefill2048": {
            "e2e_change_pct": 0.41600152222842635,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3856200600592339,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4145973498178135,
            "ttft_change_pct": 0.41664121561475476
          },
          "prefill4096": {
            "e2e_change_pct": -47.75632024733093,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -48.465867183268294,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -4.1922005253890005,
            "ttft_change_pct": -47.76626612043331
          },
          "pve_sim": {
            "e2e_change_pct": 1.3044801796548544,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22360373401336675,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.7529341340073112,
            "ttft_change_pct": -0.11839129995467879
          },
          "sorting": {
            "e2e_change_pct": -0.33507694816919953,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.533462318177172,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2717073180776408,
            "ttft_change_pct": -0.6734622415025204
          },
          "time": {
            "e2e_change_pct": 0.09644581138552599,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0869689033522034,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.067063577154991,
            "ttft_change_pct": 0.2654813825562652
          },
          "tool-call": {
            "e2e_change_pct": 0.1068644459646606,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.168079283753154,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.012649896376593084,
            "ttft_change_pct": 0.22347017375328182
          },
          "tool-final": {
            "e2e_change_pct": -27.939746816743003,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -31.418897902145414,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13314852165349222,
            "ttft_change_pct": -60.9726837045526
          }
        }
      },
      "complete": true
    }
  }
}
```
