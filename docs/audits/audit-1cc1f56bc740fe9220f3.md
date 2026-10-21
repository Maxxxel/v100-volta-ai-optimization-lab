# Public audit excerpt

Original SHA256: `1cc1f56bc740fe9220f3aaa93a75bad8580b26add169e56d8df0bbff28dbcd8e`

Original file: `RESULTS.json`; 47568 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 1.7677363824999999,
              "format_passes": 2,
              "gpu_energy_j": 480.86209075954025,
              "semantic_passes": 2,
              "tokens_per_s": 35.26641623768483,
              "ttft_s": 0.5200906375000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.783649917,
              "format_passes": 0,
              "gpu_energy_j": 1066.9162573313174,
              "semantic_passes": 0,
              "tokens_per_s": 35.41642104167952,
              "ttft_s": 0.19484019549999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5819956565,
              "format_passes": 2,
              "gpu_energy_j": 147.22177894690913,
              "semantic_passes": 2,
              "tokens_per_s": 34.92864174188895,
              "ttft_s": 0.2097886585
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.925475849,
              "format_passes": 0,
              "gpu_energy_j": 242.19610636862984,
              "semantic_passes": 0,
              "tokens_per_s": 34.96898834655036,
              "ttft_s": 0.5251006604999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4651524145,
              "format_passes": 2,
              "gpu_energy_j": 111.0918475415805,
              "semantic_passes": 2,
              "tokens_per_s": 34.30492792253966,
              "ttft_s": 0.20277823550000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9894825709999999,
              "format_passes": 0,
              "gpu_energy_j": 266.45565605101933,
              "semantic_passes": 0,
              "tokens_per_s": 35.306503459445906,
              "ttft_s": 0.22468956699999998
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1461001175,
              "format_passes": 0,
              "gpu_energy_j": 295.7269989007021,
              "semantic_passes": 2,
              "tokens_per_s": 35.32774949836061,
              "ttft_s": 0.3535067125
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7825694595,
              "format_passes": 0,
              "gpu_energy_j": 1070.2467078834802,
              "semantic_passes": 0,
              "tokens_per_s": 35.3081199879532,
              "ttft_s": 0.185535958
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7948912244999997,
              "format_passes": 2,
              "gpu_energy_j": 1018.1710600112528,
              "semantic_passes": 2,
              "tokens_per_s": 34.37768705162098,
              "ttft_s": 3.2130871159999996
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5737801375,
              "format_passes": 2,
              "gpu_energy_j": 145.45147125567678,
              "semantic_passes": 2,
              "tokens_per_s": 35.00095011972971,
              "ttft_s": 0.2023397495
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7244501895,
              "format_passes": 0,
              "gpu_energy_j": 188.33194177321045,
              "semantic_passes": 0,
              "tokens_per_s": 698.1522729440537,
              "ttft_s": 0.7242666835
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7534734519999997,
              "format_passes": 0,
              "gpu_energy_j": 731.7191269251407,
              "semantic_passes": 0,
              "tokens_per_s": 744.1620486021266,
              "ttft_s": 2.7532261235
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.470910246000001,
              "format_passes": 0,
              "gpu_energy_j": 1472.217341544398,
              "semantic_passes": 0,
              "tokens_per_s": 748.9254442303097,
              "ttft_s": 5.470580214
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8486585520000001,
              "format_passes": 0,
              "gpu_energy_j": 227.37796097758712,
              "semantic_passes": 2,
              "tokens_per_s": 35.210169882232925,
              "ttft_s": 0.2237764545
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986482808,
              "format_passes": 0,
              "gpu_energy_j": 263.76682807902796,
              "semantic_passes": 2,
              "tokens_per_s": 35.0712994518444,
              "ttft_s": 0.21654433899999997
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0133269425,
              "format_passes": 0,
              "gpu_energy_j": 274.4023724686393,
              "semantic_passes": 2,
              "tokens_per_s": 35.26933205727879,
              "ttft_s": 0.21938862
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.708263551,
              "format_passes": 0,
              "gpu_energy_j": 460.63241532116393,
              "semantic_passes": 0,
              "tokens_per_s": 35.04883724596327,
              "ttft_s": 1.0296856239999999
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7787334245,
              "format_passes": 0,
              "gpu_energy_j": 468.60093259082953,
              "semantic_passes": 0,
              "tokens_per_s": 35.07769130161008,
              "ttft_s": 1.0942160565
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.7639204405,
              "format_passes": 2,
              "gpu_energy_j": 483.4224292440904,
              "semantic_passes": 2,
              "tokens_per_s": 35.362997895284195,
              "ttft_s": 0.519653876
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7905993155,
              "format_passes": 0,
              "gpu_energy_j": 1069.008835055223,
              "semantic_passes": 0,
              "tokens_per_s": 35.327434593376054,
              "ttft_s": 0.195402513
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5814855210000001,
              "format_passes": 2,
              "gpu_energy_j": 150.49063825902942,
              "semantic_passes": 2,
              "tokens_per_s": 34.93248080136505,
              "ttft_s": 0.20928346850000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924870092,
              "format_passes": 0,
              "gpu_energy_j": 243.79060032725837,
              "semantic_passes": 0,
              "tokens_per_s": 34.98413591040804,
              "ttft_s": 0.524708977
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46601820400000005,
              "format_passes": 2,
              "gpu_energy_j": 112.64444190441709,
              "semantic_passes": 2,
              "tokens_per_s": 34.25664374549004,
              "ttft_s": 0.203244803
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9903162405,
              "format_passes": 0,
              "gpu_energy_j": 267.825320371164,
              "semantic_passes": 0,
              "tokens_per_s": 35.249051826276805,
              "ttft_s": 0.2242980805
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.152921411,
              "format_passes": 0,
              "gpu_energy_j": 296.30664325699763,
              "semantic_passes": 2,
              "tokens_per_s": 35.23465053513118,
              "ttft_s": 0.35821030499999995
            },
            "length-decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 14.694075416,
              "format_passes": 0,
              "gpu_energy_j": 4213.743151917362,
              "semantic_passes": 0,
              "tokens_per_s": 35.26062111212723,
              "ttft_s": 0.1981749655
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8111233515,
              "format_passes": 2,
              "gpu_energy_j": 1023.4833257038526,
              "semantic_passes": 2,
              "tokens_per_s": 34.323661062554244,
              "ttft_s": 3.2283261725
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.577846513,
              "format_passes": 2,
              "gpu_energy_j": 144.73488478434797,
              "semantic_passes": 2,
              "tokens_per_s": 34.89521536247055,
              "ttft_s": 0.20528117150000003
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.727563732,
              "format_passes": 0,
              "gpu_energy_j": 187.43526003462281,
              "semantic_passes": 0,
              "tokens_per_s": 695.1547781351405,
              "ttft_s": 0.727401286
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7506679624999997,
              "format_passes": 0,
              "gpu_energy_j": 741.5859131264875,
              "semantic_passes": 0,
              "tokens_per_s": 744.8805872070825,
              "ttft_s": 2.7504080135
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4707977985,
              "format_passes": 0,
              "gpu_energy_j": 1482.1632821703806,
              "semantic_passes": 0,
              "tokens_per_s": 748.9354065098933,
              "ttft_s": 5.470444926
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8500705799999999,
              "format_passes": 0,
              "gpu_energy_j": 228.70596518658832,
              "semantic_passes": 2,
              "tokens_per_s": 35.14878695570576,
              "ttft_s": 0.22407699949999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.987976356,
              "format_passes": 0,
              "gpu_energy_j": 266.3202921094722,
              "semantic_passes": 2,
              "tokens_per_s": 35.04469253329985,
              "ttft_s": 0.21749803099999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.01818498,
              "format_passes": 0,
              "gpu_energy_j": 274.54813524947565,
              "semantic_passes": 2,
              "tokens_per_s": 35.13293742595937,
              "ttft_s": 0.2211495255
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.711330158,
              "format_passes": 0,
              "gpu_energy_j": 458.3364683110635,
              "semantic_passes": 0,
              "tokens_per_s": 34.96959349817378,
              "ttft_s": 1.0310104784999998
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7808858220000001,
              "format_passes": 0,
              "gpu_energy_j": 471.62584438261354,
              "semantic_passes": 0,
              "tokens_per_s": 35.05141536499664,
              "ttft_s": 1.0963436155
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.21586601021376106,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5324475631892645,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.273862977594419,
            "ttft_change_pct": -0.08397795855343837
          },
          "decode": {
            "e2e_change_pct": 0.18366917268894944,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.19613326814793552,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.25125759657855795,
            "ttft_change_pct": 0.28860446303546894
          },
          "energy": {
            "e2e_change_pct": -0.08765280192428726,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2203639539630338,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.01099115019835839,
            "ttft_change_pct": -0.24080901399157195
          },
          "filtering": {
            "e2e_change_pct": -0.06545357187380807,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6583483039986016,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.043317134906972754,
            "ttft_change_pct": -0.07459207909337184
          },
          "german": {
            "e2e_change_pct": 0.18613028181970748,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3975772274877896,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1407499737607676,
            "ttft_change_pct": 0.2300875628242549
          },
          "ha_sim": {
            "e2e_change_pct": 0.08425307574215779,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5140308674410177,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.16272252287766742,
            "ttft_change_pct": -0.17423439157724374
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.5951743129456455,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1960065731063665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2635292781210108,
            "ttft_change_pct": 1.330552528051343
          },
          "length-decode": {
            "e2e_change_pct": 288.46809221428924,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 293.71699262223945,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 6.812160637885611
          },
          "long_context": {
            "e2e_change_pct": 0.4277362917599614,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5217458933218122,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15715422909520216,
            "ttft_change_pct": 0.47428083801759335
          },
          "math": {
            "e2e_change_pct": 0.7086992445778151,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.49266361154173266,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.30209110580560194,
            "ttft_change_pct": 1.4537044783679676
          },
          "prefill": {
            "e2e_change_pct": 0.4297800656452244,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4761177154257834,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.42934685240986203,
            "ttft_change_pct": 0.43279672687028814
          },
          "prefill2048": {
            "e2e_change_pct": -0.10188910657418226,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3484390168683191,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.09655673872452919,
            "ttft_change_pct": -0.10235664902153996
          },
          "prefill4096": {
            "e2e_change_pct": -0.0020553709519033347,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6755755651912665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0013302097906064958,
            "ttft_change_pct": -0.0024730100776859665
          },
          "pve_sim": {
            "e2e_change_pct": 0.16638352334659157,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5840514196237656,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.17433294622681839,
            "ttft_change_pct": 0.13430590839931256
          },
          "sorting": {
            "e2e_change_pct": 0.15140132072124501,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9680762547135568,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.07586522016694852,
            "ttft_change_pct": 0.4404141915711701
          },
          "time": {
            "e2e_change_pct": 0.47941461893974413,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.05312008767452969,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3867230348958972,
            "ttft_change_pct": 0.8026421333978018
          },
          "tool-call": {
            "e2e_change_pct": 0.1795160353450731,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4984336607096185,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.22609522602241583,
            "ttft_change_pct": 0.12866592182314562
          },
          "tool-final": {
            "e2e_change_pct": 0.12100731173954049,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6455197976366955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.0749078278485027,
            "ttft_change_pct": 0.19443682875621704
          }
        }
      },
      "complete": true
    }
  }
}
```
