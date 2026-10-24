# Public audit excerpt

Original SHA256: `4ed8062b94ba0bc465fc2dbc0c9455e9729935853fe6d5010e9f1f20f9be3fc8`

Original file: `RESULTS.json`; 61683 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6662196,
              "format_passes": 2,
              "gpu_energy_j": 177.27304265872266,
              "semantic_passes": 2,
              "tokens_per_s": 79.30068646083471,
              "ttft_s": 0.1239369155
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593296915,
              "format_passes": 0,
              "gpu_energy_j": 462.97363135580486,
              "semantic_passes": 0,
              "tokens_per_s": 79.57923050441363,
              "ttft_s": 0.06338052050000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2384077565,
              "format_passes": 2,
              "gpu_energy_j": 60.19152936739849,
              "semantic_passes": 2,
              "tokens_per_s": 77.99118943870333,
              "ttft_s": 0.0716813305
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241472213,
              "format_passes": 0,
              "gpu_energy_j": 60.608446561039145,
              "semantic_passes": 0,
              "tokens_per_s": 77.59928192074227,
              "ttft_s": 0.125480368
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18349242249999997,
              "format_passes": 2,
              "gpu_energy_j": 40.251625155260946,
              "semantic_passes": 2,
              "tokens_per_s": 77.31427420692017,
              "ttft_s": 0.067023239
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35831727599999996,
              "format_passes": 0,
              "gpu_energy_j": 89.55795438396035,
              "semantic_passes": 0,
              "tokens_per_s": 78.74553449876396,
              "ttft_s": 0.07890534099999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4693005455,
              "format_passes": 0,
              "gpu_energy_j": 117.64112709614298,
              "semantic_passes": 2,
              "tokens_per_s": 79.01347337384692,
              "ttft_s": 0.114824838
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0829081995,
              "format_passes": 2,
              "gpu_energy_j": 288.96450506909207,
              "semantic_passes": 2,
              "tokens_per_s": 77.78202026003973,
              "ttft_s": 0.8257527115000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23378557049999998,
              "format_passes": 0,
              "gpu_energy_j": 57.190120670166735,
              "semantic_passes": 0,
              "tokens_per_s": 78.39334408111534,
              "ttft_s": 0.06789688699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1993610315,
              "format_passes": 0,
              "gpu_energy_j": 48.23103321809123,
              "semantic_passes": 0,
              "tokens_per_s": 2548.0663708380825,
              "ttft_s": 0.1991730555
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.721282569,
              "format_passes": 0,
              "gpu_energy_j": 191.3667970597514,
              "semantic_passes": 0,
              "tokens_per_s": 2844.331842038585,
              "ttft_s": 0.721046823
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.427608168,
              "format_passes": 0,
              "gpu_energy_j": 385.31194817857215,
              "semantic_passes": 0,
              "tokens_per_s": 2872.625670344104,
              "ttft_s": 1.427271314
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295235327,
              "format_passes": 2,
              "gpu_energy_j": 73.3733205458721,
              "semantic_passes": 2,
              "tokens_per_s": 78.54838682334336,
              "ttft_s": 0.0787364925
            },
            "ram-displace": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1192081685000002,
              "format_passes": 0,
              "gpu_energy_j": 299.9648905778316,
              "semantic_passes": 0,
              "tokens_per_s": 78.20778559150816,
              "ttft_s": 0.722649716
            },
            "ram-pressure2": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.118050677,
              "format_passes": 0,
              "gpu_energy_j": 301.2034894849806,
              "semantic_passes": 0,
              "tokens_per_s": 78.1636123010779,
              "ttft_s": 0.721406899
            },
            "ram-pressure3": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.117902773,
              "format_passes": 0,
              "gpu_energy_j": 302.7626581985824,
              "semantic_passes": 0,
              "tokens_per_s": 78.23652328947605,
              "ttft_s": 0.7218063475000001
            },
            "ram-pressure4": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.117590187,
              "format_passes": 0,
              "gpu_energy_j": 299.75524861713643,
              "semantic_passes": 0,
              "tokens_per_s": 78.24548397496854,
              "ttft_s": 0.721357283
            },
            "ram-pressure5": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.117533297,
              "format_passes": 0,
              "gpu_energy_j": 302.0162762363382,
              "semantic_passes": 0,
              "tokens_per_s": 78.28490401904452,
              "ttft_s": 0.7212998035
            },
            "ram-pressure6": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.119746974,
              "format_passes": 0,
              "gpu_energy_j": 300.09639751603834,
              "semantic_passes": 0,
              "tokens_per_s": 78.22782436318656,
              "ttft_s": 0.7225456525
            },
            "ram-pressure7": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1187118675,
              "format_passes": 0,
              "gpu_energy_j": 300.0379122846539,
              "semantic_passes": 0,
              "tokens_per_s": 78.25943269513468,
              "ttft_s": 0.7215862
            },
            "ram-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1196857370000002,
              "format_passes": 0,
              "gpu_energy_j": 299.1129345268195,
              "semantic_passes": 0,
              "tokens_per_s": 78.22055575043399,
              "ttft_s": 0.7231491290000001
            },
            "ram-restore": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1172203475,
              "format_passes": 0,
              "gpu_energy_j": 301.86840202812743,
              "semantic_passes": 0,
              "tokens_per_s": 78.37211423256767,
              "ttft_s": 0.720533155
            },
            "ram-revisit": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.121206955,
              "format_passes": 0,
              "gpu_energy_j": 300.3832608090497,
              "semantic_passes": 0,
              "tokens_per_s": 78.31852671016068,
              "ttft_s": 0.723872743
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353115266,
              "format_passes": 2,
              "gpu_energy_j": 91.78517066400799,
              "semantic_passes": 2,
              "tokens_per_s": 78.74822373880221,
              "ttft_s": 0.0737468895
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3698742075,
              "format_passes": 2,
              "gpu_energy_j": 90.40623596721883,
              "semantic_passes": 2,
              "tokens_per_s": 78.85570233417573,
              "ttft_s": 0.078188146
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.622926286,
              "format_passes": 0,
              "gpu_energy_j": 163.93703248453897,
              "semantic_passes": 0,
              "tokens_per_s": 78.83222661160237,
              "ttft_s": 0.320658523
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5612103310000001,
              "format_passes": 0,
              "gpu_energy_j": 146.5520854030642,
              "semantic_passes": 0,
              "tokens_per_s": 78.75101156220782,
              "ttft_s": 0.256358522
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
              "e2e_s": 0.7186963485,
              "format_passes": 2,
              "gpu_energy_j": 186.03108267575635,
              "semantic_passes": 2,
              "tokens_per_s": 79.18817061490621,
              "ttft_s": 0.1756571375
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7273400730000001,
              "format_passes": 0,
              "gpu_energy_j": 466.6962517596495,
              "semantic_passes": 0,
              "tokens_per_s": 79.58061689041168,
              "ttft_s": 0.131378312
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.290864871,
              "format_passes": 2,
              "gpu_energy_j": 65.78399996995012,
              "semantic_passes": 2,
              "tokens_per_s": 78.31136776728218,
              "ttft_s": 0.1247342195
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.304007907,
              "format_passes": 0,
              "gpu_energy_j": 67.41114573520093,
              "semantic_passes": 0,
              "tokens_per_s": 77.50235977864963,
              "ttft_s": 0.187876616
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.27172707,
              "format_passes": 2,
              "gpu_energy_j": 49.004695662926785,
              "semantic_passes": 2,
              "tokens_per_s": 77.61779954512996,
              "ttft_s": 0.155718303
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.41523725,
              "format_passes": 0,
              "gpu_energy_j": 98.07406761226804,
              "semantic_passes": 0,
              "tokens_per_s": 78.91348612277869,
              "ttft_s": 0.1364337765
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5254210804999999,
              "format_passes": 0,
              "gpu_energy_j": 122.39893141756795,
              "semantic_passes": 2,
              "tokens_per_s": 79.10867146909933,
              "ttft_s": 0.17144971250000002
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1699251995,
              "format_passes": 2,
              "gpu_energy_j": 294.5307310286371,
              "semantic_passes": 2,
              "tokens_per_s": 77.83597269697545,
              "ttft_s": 0.9129249015
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29379258750000004,
              "format_passes": 0,
              "gpu_energy_j": 61.679289337838945,
              "semantic_passes": 0,
              "tokens_per_s": 78.1702657955721,
              "ttft_s": 0.1274707735
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2005503945,
              "format_passes": 0,
              "gpu_energy_j": 50.56384360726835,
              "semantic_passes": 0,
              "tokens_per_s": 2541.541627555403,
              "ttft_s": 0.2004172015
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8103707035000001,
              "format_passes": 0,
              "gpu_energy_j": 198.3860768133776,
              "semantic_passes": 0,
              "tokens_per_s": 2849.400151275354,
              "ttft_s": 0.8101136825
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.422264521,
              "format_passes": 0,
              "gpu_energy_j": 384.37124634286556,
              "semantic_passes": 0,
              "tokens_per_s": 2883.3871957679203,
              "ttft_s": 1.4219583155
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3522409005,
              "format_passes": 2,
              "gpu_energy_j": 76.45312615983876,
              "semantic_passes": 2,
              "tokens_per_s": 78.37303308712683,
              "ttft_s": 0.1352903915
            },
            "ram-displace": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2355781330000002,
              "format_passes": 0,
              "gpu_energy_j": 308.93431428196254,
              "semantic_passes": 0,
              "tokens_per_s": 78.29014355858303,
              "ttft_s": 0.8401000105
            },
            "ram-pressure2": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2370450095,
              "format_passes": 0,
              "gpu_energy_j": 309.690090117875,
              "semantic_passes": 0,
              "tokens_per_s": 78.35252586222066,
              "ttft_s": 0.8411814005
            },
            "ram-pressure3": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.237019831,
              "format_passes": 0,
              "gpu_energy_j": 313.6458327455481,
              "semantic_passes": 0,
              "tokens_per_s": 78.21804399289462,
              "ttft_s": 0.8415191
            },
            "ram-pressure4": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.237061309,
              "format_passes": 0,
              "gpu_energy_j": 310.5526428872435,
              "semantic_passes": 0,
              "tokens_per_s": 78.30734891018008,
              "ttft_s": 0.8408002235
            },
            "ram-pressure5": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2359819765000002,
              "format_passes": 0,
              "gpu_energy_j": 309.1490481530801,
              "semantic_passes": 0,
              "tokens_per_s": 78.24903894953985,
              "ttft_s": 0.839018084
            },
            "ram-pressure6": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.236741672,
              "format_passes": 0,
              "gpu_energy_j": 310.2284490884419,
              "semantic_passes": 0,
              "tokens_per_s": 78.15201496278081,
              "ttft_s": 0.8399081095
            },
            "ram-pressure7": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.236702851,
              "format_passes": 0,
              "gpu_energy_j": 312.02846783990583,
              "semantic_passes": 0,
              "tokens_per_s": 78.39061540015288,
              "ttft_s": 0.840700478
            },
            "ram-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2358854314999999,
              "format_passes": 0,
              "gpu_energy_j": 308.00263275451096,
              "semantic_passes": 0,
              "tokens_per_s": 78.20740321077298,
              "ttft_s": 0.8397827585
            },
            "ram-restore": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2388148715,
              "format_passes": 0,
              "gpu_energy_j": 308.9606365962834,
              "semantic_passes": 0,
              "tokens_per_s": 78.23206175413742,
              "ttft_s": 0.8419529455
            },
            "ram-revisit": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.238698788,
              "format_passes": 0,
              "gpu_energy_j": 310.90615627615387,
              "semantic_passes": 0,
              "tokens_per_s": 78.31170081055416,
              "ttft_s": 0.8425281485
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4720039665,
              "format_passes": 2,
              "gpu_energy_j": 100.37599725000496,
              "semantic_passes": 2,
              "tokens_per_s": 78.85813538780081,
              "ttft_s": 0.19299997
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4288530405,
              "format_passes": 2,
              "gpu_energy_j": 101.57048040198336,
              "semantic_passes": 2,
              "tokens_per_s": 78.6245560116399,
              "ttft_s": 0.13630420999999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6772020785,
              "format_passes": 0,
              "gpu_energy_j": 169.87103566184936,
              "semantic_passes": 0,
              "tokens_per_s": 78.96806106117387,
              "ttft_s": 0.375899747
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560625293,
              "format_passes": 0,
              "gpu_energy_j": 148.1142321507822,
              "semantic_passes": 0,
              "tokens_per_s": 78.68930738412108,
              "ttft_s": 0.255805353
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
            "e2e_change_pct": 7.876794453360425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.940424040610747,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.14188508441735914,
            "ttft_change_pct": 41.731086973840334
          },
          "decode": {
            "e2e_change_pct": 4.098665976290716,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8040674785177337,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.0017421455186905632,
            "ttft_change_pct": 107.28500012870671
          },
          "energy": {
            "e2e_change_pct": 22.003107310814364,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.291125614064688,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.41053140859006465,
            "ttft_change_pct": 74.01214323163265
          },
          "filtering": {
            "e2e_change_pct": 25.897677096287698,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.224011767585473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.12490082342724307,
            "ttft_change_pct": 49.7259045335283
          },
          "german": {
            "e2e_change_pct": 48.08626225423562,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 21.745881002078747,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.39258641605746103,
            "ttft_change_pct": 132.33479211591072
          },
          "ha_sim": {
            "e2e_change_pct": 15.88535574823917,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.509052866255407,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.21328399773243856,
            "ttft_change_pct": 72.90816410007024
          },
          "jarvis_memory": {
            "e2e_change_pct": 11.958335769716232,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.0443375874294585,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.12048336971846041,
            "ttft_change_pct": 49.31413402037634
          },
          "long_context": {
            "e2e_change_pct": 8.03549183949086,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9262663274903336,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.06936363539458146,
            "ttft_change_pct": 10.556694369389309
          },
          "math": {
            "e2e_change_pct": 25.66754520891188,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.849552711319929,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2845627880249779,
            "ttft_change_pct": 87.74170530086307
          },
          "prefill": {
            "e2e_change_pct": 0.5965875031099133,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.836741478517825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.2560664571909621,
            "ttft_change_pct": 0.6246557783013085
          },
          "prefill2048": {
            "e2e_change_pct": 12.351349988051652,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.667971592498631,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.17818980056618638,
            "ttft_change_pct": 12.352437686283245
          },
          "prefill4096": {
            "e2e_change_pct": -0.3743076790801769,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.24414032322470636,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.37462331186810527,
            "ttft_change_pct": -0.3722486711450812
          },
          "pve_sim": {
            "e2e_change_pct": 19.3085204535838,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.197446143985273,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.22324295037516872,
            "ttft_change_pct": 71.82679492612651
          },
          "ram-displace": {
            "e2e_change_pct": 10.397526374022359,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9901578437572685,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10530660912078105,
            "ttft_change_pct": 16.252728244343494
          },
          "ram-pressure2": {
            "e2e_change_pct": 10.643017794085207,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8175638494113864,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.24168990605895058,
            "ttft_change_pct": 16.602904916217053
          },
          "ram-pressure3": {
            "e2e_change_pct": 10.655404108206824,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5946224715160735,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.02361978242956253,
            "ttft_change_pct": 16.585162061074833
          },
          "ram-pressure4": {
            "e2e_change_pct": 10.690065409459425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.602070128853052,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.07906518315017319,
            "ttft_change_pct": 16.55808339568674
          },
          "ram-pressure5": {
            "e2e_change_pct": 10.599118596105694,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3617177211867624,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.04581351916320697,
            "ttft_change_pct": 16.320298429139935
          },
          "ram-pressure6": {
            "e2e_change_pct": 10.448315620989579,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.3762656453955042,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09690848623603587,
            "ttft_change_pct": 16.242912346635418
          },
          "ram-pressure7": {
            "e2e_change_pct": 10.547039584345864,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.996346816290397,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.16762542290491567,
            "ttft_change_pct": 16.50728326012887
          },
          "ram-prime": {
            "e2e_change_pct": 10.37788467426013,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9720206656239867,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.016814684496713195,
            "ttft_change_pct": 16.12857221598063
          },
          "ram-restore": {
            "e2e_change_pct": 10.883665363962592,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.3494458249045724,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.17870192708422383,
            "ttft_change_pct": 16.85138146071847
          },
          "ram-revisit": {
            "e2e_change_pct": 10.479049605966818,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.5031564138300775,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.008715561813088524,
            "ttft_change_pct": 16.39174932989569
          },
          "sorting": {
            "e2e_change_pct": 33.66852468508117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.359710859442472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.13957349611233294,
            "ttft_change_pct": 161.7059123558018
          },
          "time": {
            "e2e_change_pct": 15.945646331665353,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.348976058258486,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.29312569122303955,
            "ttft_change_pct": 74.32848452500713
          },
          "tool-call": {
            "e2e_change_pct": 8.71303615208172,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.6196843918533395,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.1723082746866167,
            "ttft_change_pct": 17.227430440075974
          },
          "tool-final": {
            "e2e_change_pct": -0.10424576449931111,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.065932800220204,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.078353505387041,
            "ttft_change_pct": -0.215779446567399
          }
        }
      },
      "complete": true,
      "ram_cache": {
        "arms": {
          "A": {
            "cycles": 6,
            "evictions": 0,
            "max_observed_rss_kib": 1508644,
            "max_recorded_ram_cache_mib": 0,
            "oversize": 0,
            "restore_e2e_s": 1.1172203475,
            "restore_hits": 0,
            "revisit_e2e_s": 1.121206955,
            "revisit_hits": 0,
            "starts": 2
          },
          "B": {
            "cycles": 6,
            "evictions": 58,
            "max_observed_rss_kib": 1729772,
            "max_recorded_ram_cache_mib": 215.768,
            "oversize": 2,
            "restore_e2e_s": 1.2388148715,
            "restore_hits": 0,
            "revisit_e2e_s": 1.238698788,
            "revisit_hits": 0,
            "starts": 2
          }
        },
        "change_exercised": false,
        "note": "Matched total input, outputs and request sequence. Restored latency includes RAM state save/load. Reused tokens are not counted as freshly evaluated throughput; answer equality and LRU pressure outcomes remain separate."
      }
    }
  }
}
```

</details>
