# Public audit excerpt

Original SHA256: `7eba82c4d50b936a44becb70d1f1ad90fcea1d91bba1345b57d771395545f459`

Original file: `RESULTS.json`; 61724 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.665661052,
              "format_passes": 2,
              "gpu_energy_j": 180.551425376889,
              "semantic_passes": 2,
              "tokens_per_s": 79.33258412621191,
              "ttft_s": 0.1236011305
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6586070265,
              "format_passes": 0,
              "gpu_energy_j": 459.8607595589717,
              "semantic_passes": 0,
              "tokens_per_s": 79.60353682522765,
              "ttft_s": 0.063125026
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2385341955,
              "format_passes": 2,
              "gpu_energy_j": 57.076889162852424,
              "semantic_passes": 2,
              "tokens_per_s": 78.1900789716502,
              "ttft_s": 0.0722226235
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24272845599999998,
              "format_passes": 0,
              "gpu_energy_j": 60.02740109538302,
              "semantic_passes": 0,
              "tokens_per_s": 76.9599465603392,
              "ttft_s": 0.1257149475
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.183241435,
              "format_passes": 2,
              "gpu_energy_j": 44.09174855193889,
              "semantic_passes": 2,
              "tokens_per_s": 77.31817194940919,
              "ttft_s": 0.066796559
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3576345105,
              "format_passes": 0,
              "gpu_energy_j": 89.86676231989865,
              "semantic_passes": 0,
              "tokens_per_s": 78.91231003131438,
              "ttft_s": 0.0788302685
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468870181,
              "format_passes": 0,
              "gpu_energy_j": 117.27295316701426,
              "semantic_passes": 2,
              "tokens_per_s": 79.09238111335497,
              "ttft_s": 0.1148618515
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.084694855,
              "format_passes": 2,
              "gpu_energy_j": 289.46488110459757,
              "semantic_passes": 2,
              "tokens_per_s": 77.80772824448033,
              "ttft_s": 0.8276345755
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234171595,
              "format_passes": 0,
              "gpu_energy_j": 58.38366479528551,
              "semantic_passes": 0,
              "tokens_per_s": 78.02177318835666,
              "ttft_s": 0.06750466699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1997434075,
              "format_passes": 0,
              "gpu_energy_j": 48.62471410675174,
              "semantic_passes": 0,
              "tokens_per_s": 2541.445019232913,
              "ttft_s": 0.1996056425
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7210107225,
              "format_passes": 0,
              "gpu_energy_j": 189.85254314103622,
              "semantic_passes": 0,
              "tokens_per_s": 2845.38020178504,
              "ttft_s": 0.7207823714999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4274038105,
              "format_passes": 0,
              "gpu_energy_j": 385.43539529099723,
              "semantic_passes": 0,
              "tokens_per_s": 2872.966128173939,
              "ttft_s": 1.4270972
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954985755,
              "format_passes": 2,
              "gpu_energy_j": 71.41995449631688,
              "semantic_passes": 2,
              "tokens_per_s": 78.51445554596079,
              "ttft_s": 0.07896644250000001
            },
            "ram-displace": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.116900459,
              "format_passes": 0,
              "gpu_energy_j": 300.9252805928993,
              "semantic_passes": 0,
              "tokens_per_s": 78.38271095871148,
              "ttft_s": 0.7212377235
            },
            "ram-pressure2": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1171645625,
              "format_passes": 0,
              "gpu_energy_j": 300.0682842603675,
              "semantic_passes": 0,
              "tokens_per_s": 78.32173207281784,
              "ttft_s": 0.7212864290000001
            },
            "ram-pressure3": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1164738415,
              "format_passes": 0,
              "gpu_energy_j": 301.85269614710023,
              "semantic_passes": 0,
              "tokens_per_s": 78.36329597072586,
              "ttft_s": 0.7206097565
            },
            "ram-pressure4": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1162991684999999,
              "format_passes": 0,
              "gpu_energy_j": 301.84258167340346,
              "semantic_passes": 0,
              "tokens_per_s": 78.41124125474748,
              "ttft_s": 0.720479431
            },
            "ram-pressure5": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.119133924,
              "format_passes": 0,
              "gpu_energy_j": 303.73910674901595,
              "semantic_passes": 0,
              "tokens_per_s": 78.14822688397265,
              "ttft_s": 0.720214481
            },
            "ram-pressure6": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1198432175,
              "format_passes": 0,
              "gpu_energy_j": 302.0733483239133,
              "semantic_passes": 0,
              "tokens_per_s": 78.04655501393246,
              "ttft_s": 0.7219816695000001
            },
            "ram-pressure7": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.117754307,
              "format_passes": 0,
              "gpu_energy_j": 302.8236973771997,
              "semantic_passes": 0,
              "tokens_per_s": 78.25773366714705,
              "ttft_s": 0.7216694495
            },
            "ram-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.119550543,
              "format_passes": 0,
              "gpu_energy_j": 301.78183037632164,
              "semantic_passes": 0,
              "tokens_per_s": 78.19442157449552,
              "ttft_s": 0.721848821
            },
            "ram-restore": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1172659475,
              "format_passes": 0,
              "gpu_energy_j": 301.5496921558773,
              "semantic_passes": 0,
              "tokens_per_s": 78.3214227779911,
              "ttft_s": 0.7212816895
            },
            "ram-revisit": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.118879929,
              "format_passes": 0,
              "gpu_energy_j": 301.52289741285654,
              "semantic_passes": 0,
              "tokens_per_s": 78.24572447664104,
              "ttft_s": 0.7225069865
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3529203125,
              "format_passes": 2,
              "gpu_energy_j": 91.48784262177827,
              "semantic_passes": 2,
              "tokens_per_s": 78.78261457532948,
              "ttft_s": 0.073631331
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36936060000000004,
              "format_passes": 2,
              "gpu_energy_j": 94.33697517245884,
              "semantic_passes": 2,
              "tokens_per_s": 78.91522669293272,
              "ttft_s": 0.0778645505
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.621720554,
              "format_passes": 0,
              "gpu_energy_j": 163.54326299480027,
              "semantic_passes": 0,
              "tokens_per_s": 78.93538178699043,
              "ttft_s": 0.3203727085
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5632736570000001,
              "format_passes": 0,
              "gpu_energy_j": 147.05739842566635,
              "semantic_passes": 0,
              "tokens_per_s": 78.71807820518707,
              "ttft_s": 0.2581286605
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
              "e2e_s": 0.7202396055,
              "format_passes": 2,
              "gpu_energy_j": 182.59918567806318,
              "semantic_passes": 2,
              "tokens_per_s": 79.19597589602598,
              "ttft_s": 0.1772426
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7223355864999998,
              "format_passes": 0,
              "gpu_energy_j": 466.76775110273365,
              "semantic_passes": 0,
              "tokens_per_s": 79.49307865808096,
              "ttft_s": 0.12458352
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.296676813,
              "format_passes": 2,
              "gpu_energy_j": 61.908744725664725,
              "semantic_passes": 2,
              "tokens_per_s": 77.8646492361647,
              "ttft_s": 0.129581815
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29562900000000003,
              "format_passes": 0,
              "gpu_energy_j": 65.86223534080125,
              "semantic_passes": 0,
              "tokens_per_s": 77.61276781335988,
              "ttft_s": 0.1796071055
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.263644588,
              "format_passes": 2,
              "gpu_energy_j": 49.30173840655424,
              "semantic_passes": 2,
              "tokens_per_s": 77.51073757712473,
              "ttft_s": 0.14749379699999998
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4141296545,
              "format_passes": 0,
              "gpu_energy_j": 93.57876583877862,
              "semantic_passes": 0,
              "tokens_per_s": 78.60918526769338,
              "ttft_s": 0.13416962100000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5237077665000001,
              "format_passes": 0,
              "gpu_energy_j": 124.87312671295264,
              "semantic_passes": 2,
              "tokens_per_s": 78.95831553986223,
              "ttft_s": 0.1690593275
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.16784964,
              "format_passes": 2,
              "gpu_energy_j": 295.268253564871,
              "semantic_passes": 2,
              "tokens_per_s": 77.8246464997712,
              "ttft_s": 0.9108296874999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.286200064,
              "format_passes": 0,
              "gpu_energy_j": 60.50728853105203,
              "semantic_passes": 0,
              "tokens_per_s": 78.31325928995463,
              "ttft_s": 0.120157098
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.35631750900000003,
              "format_passes": 0,
              "gpu_energy_j": 60.09513844619,
              "semantic_passes": 0,
              "tokens_per_s": 2581.414433136084,
              "ttft_s": 0.35618004449999996
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8385901785000001,
              "format_passes": 0,
              "gpu_energy_j": 199.47333591219632,
              "semantic_passes": 0,
              "tokens_per_s": 2844.0691949910088,
              "ttft_s": 0.8383810855
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4238363829999998,
              "format_passes": 0,
              "gpu_energy_j": 386.1550425096618,
              "semantic_passes": 0,
              "tokens_per_s": 2880.139181941685,
              "ttft_s": 1.423505815
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.34872520900000004,
              "format_passes": 2,
              "gpu_energy_j": 78.0058400781161,
              "semantic_passes": 2,
              "tokens_per_s": 78.57602138322272,
              "ttft_s": 0.132324304
            },
            "ram-displace": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.238427427,
              "format_passes": 0,
              "gpu_energy_j": 309.59127433557177,
              "semantic_passes": 0,
              "tokens_per_s": 78.3379226646397,
              "ttft_s": 0.8419711910000001
            },
            "ram-pressure2": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2299434200000001,
              "format_passes": 0,
              "gpu_energy_j": 307.8093084406619,
              "semantic_passes": 0,
              "tokens_per_s": 77.97411449917118,
              "ttft_s": 0.8307577255
            },
            "ram-pressure3": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2430219815,
              "format_passes": 0,
              "gpu_energy_j": 308.32349921395786,
              "semantic_passes": 0,
              "tokens_per_s": 78.18266381177462,
              "ttft_s": 0.846795763
            },
            "ram-pressure4": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2401841135,
              "format_passes": 0,
              "gpu_energy_j": 309.70167217264157,
              "semantic_passes": 0,
              "tokens_per_s": 78.22909651402003,
              "ttft_s": 0.8432095665
            },
            "ram-pressure5": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2407817429999999,
              "format_passes": 0,
              "gpu_energy_j": 310.3619552249251,
              "semantic_passes": 0,
              "tokens_per_s": 78.33886091478867,
              "ttft_s": 0.844428797
            },
            "ram-pressure6": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2382919085,
              "format_passes": 0,
              "gpu_energy_j": 310.9458017179699,
              "semantic_passes": 0,
              "tokens_per_s": 78.02609200993739,
              "ttft_s": 0.8410175115
            },
            "ram-pressure7": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.237617775,
              "format_passes": 0,
              "gpu_energy_j": 311.9029975782722,
              "semantic_passes": 0,
              "tokens_per_s": 78.25208311827794,
              "ttft_s": 0.8421741730000001
            },
            "ram-prime": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2431997655,
              "format_passes": 0,
              "gpu_energy_j": 310.9001028222981,
              "semantic_passes": 0,
              "tokens_per_s": 78.26765418410665,
              "ttft_s": 0.846199142
            },
            "ram-restore": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.599067792,
              "format_passes": 0,
              "gpu_energy_j": 126.92249880149646,
              "semantic_passes": 0,
              "tokens_per_s": 78.63948615488297,
              "ttft_s": 0.20455573900000001
            },
            "ram-revisit": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2378894635000002,
              "format_passes": 0,
              "gpu_energy_j": 309.0023609108431,
              "semantic_passes": 0,
              "tokens_per_s": 78.07551416141459,
              "ttft_s": 0.8424972715
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.48080687099999997,
              "format_passes": 2,
              "gpu_energy_j": 98.6820786326603,
              "semantic_passes": 2,
              "tokens_per_s": 78.57624098385813,
              "ttft_s": 0.200770404
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.429648344,
              "format_passes": 2,
              "gpu_energy_j": 99.58962120734226,
              "semantic_passes": 2,
              "tokens_per_s": 78.71224279075838,
              "ttft_s": 0.137441511
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6475090795,
              "format_passes": 0,
              "gpu_energy_j": 165.75263694195513,
              "semantic_passes": 0,
              "tokens_per_s": 78.88929010363066,
              "ttft_s": 0.3409410845
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561600621,
              "format_passes": 0,
              "gpu_energy_j": 147.77479405163558,
              "semantic_passes": 0,
              "tokens_per_s": 78.80078584263532,
              "ttft_s": 0.2571670455
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 8.199150804454746,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1341701107590918,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.17219687432417086,
            "ttft_change_pct": 43.398850223299526
          },
          "decode": {
            "e2e_change_pct": 3.842294104739219,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5019745434218024,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.13876037617424064,
            "ttft_change_pct": 97.35995039431747
          },
          "energy": {
            "e2e_change_pct": 24.374961157298713,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.465520167060948,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.41620335951252363,
            "ttft_change_pct": 79.41997773038526
          },
          "filtering": {
            "e2e_change_pct": 21.794125366166405,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.720284634923182,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.8482610529216617,
            "ttft_change_pct": 42.86853637671049
          },
          "german": {
            "e2e_change_pct": 43.87825984881639,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.816246861877389,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.249056105260137,
            "ttft_change_pct": 120.81047168911793
          },
          "ha_sim": {
            "e2e_change_pct": 15.79689385149534,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.130563317354596,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3841286150420786,
            "ttft_change_pct": 70.20063936481458
          },
          "jarvis_memory": {
            "e2e_change_pct": 11.695686294880847,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.480755656519177,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.16950504157993151,
            "ttft_change_pct": 47.184922837501
          },
          "long_context": {
            "e2e_change_pct": 7.666191520748034,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.004862364694371,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.02174366952047979,
            "ttft_change_pct": 10.052155197810485
          },
          "math": {
            "e2e_change_pct": 22.21809566612891,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.637359427868603,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3735958434247344,
            "ttft_change_pct": 77.99820862756054
          },
          "prefill": {
            "e2e_change_pct": 78.3876191258027,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 23.589700320408767,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.5727042529227964,
            "ttft_change_pct": 78.44187170209878
          },
          "prefill2048": {
            "e2e_change_pct": 16.307587714134186,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.06750797855422,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.04607492500329213,
            "ttft_change_pct": 16.315425938521333
          },
          "prefill4096": {
            "e2e_change_pct": -0.24992419620559758,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1867102055121972,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.24967415025896056,
            "ttft_change_pct": -0.25165664959612144
          },
          "pve_sim": {
            "e2e_change_pct": 18.01248395527375,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.221352251265923,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.07841337857319441,
            "ttft_change_pct": 67.57029924451767
          },
          "ram-displace": {
            "e2e_change_pct": 10.880734001023452,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8797825578489977,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.05714052694014704,
            "ttft_change_pct": 16.739760493129552
          },
          "ram-pressure2": {
            "e2e_change_pct": 10.095098008445834,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5797542047387934,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.44383284747006035,
            "ttft_change_pct": 15.177229474811039
          },
          "ram-pressure3": {
            "e2e_change_pct": 11.334626508578172,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.143695633483511,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.23050607649111043,
            "ttft_change_pct": 17.51100444613534
          },
          "ram-pressure4": {
            "e2e_change_pct": 11.097826505278817,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.603705035806292,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.23229416830131688,
            "ttft_change_pct": 17.034509275255072
          },
          "ram-pressure5": {
            "e2e_change_pct": 10.869817846751273,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1804398343021836,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.24393903536550354,
            "ttft_change_pct": 17.246850664198178
          },
          "ram-pressure6": {
            "e2e_change_pct": 10.577256632801824,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.937185105301876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.026218971473401798,
            "ttft_change_pct": 16.48737731560925
          },
          "ram-pressure7": {
            "e2e_change_pct": 10.72359705968906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9982132441118914,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.007220435098653777,
            "ttft_change_pct": 16.698049721169482
          },
          "ram-prime": {
            "e2e_change_pct": 11.0445413360851,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.02147827607977,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.09365451925666957,
            "ttft_change_pct": 17.22664322257028
          },
          "ram-restore": {
            "e2e_change_pct": -46.380913752855605,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -57.909922608746164,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -71.63996508190854
          },
          "ram-revisit": {
            "e2e_change_pct": 10.636488457377634,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4805623593306736,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.21753305546716728,
            "ttft_change_pct": 16.607491310397183
          },
          "sorting": {
            "e2e_change_pct": 36.236667023805836,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.863597834112102,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.26195321465755095,
            "ttft_change_pct": 172.66980139201888
          },
          "time": {
            "e2e_change_pct": 16.322191376124028,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.567961051624759,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.257217663410092,
            "ttft_change_pct": 76.51358688572918
          },
          "tool-call": {
            "e2e_change_pct": 4.147928733268169,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3509415837111627,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.05839166456957923,
            "ttft_change_pct": 6.420139872806918
          },
          "tool-final": {
            "e2e_change_pct": -0.2970201036758491,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.48783375311229893,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10506816138557973,
            "ttft_change_pct": -0.37253321585341004
          }
        }
      },
      "complete": true,
      "ram_cache": {
        "arms": {
          "A": {
            "cycles": 6,
            "evictions": 0,
            "max_observed_rss_kib": 1509096,
            "max_recorded_ram_cache_mib": 0,
            "oversize": 0,
            "restore_e2e_s": 1.1172659475,
            "restore_hits": 0,
            "revisit_e2e_s": 1.118879929,
            "revisit_hits": 0,
            "starts": 2
          },
          "B": {
            "cycles": 6,
            "evictions": 58,
            "max_observed_rss_kib": 2523160,
            "max_recorded_ram_cache_mib": 990.438,
            "oversize": 0,
            "restore_e2e_s": 0.599067792,
            "restore_hits": 6,
            "revisit_e2e_s": 1.2378894635000002,
            "revisit_hits": 0,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Matched total input, outputs and request sequence. Restored latency includes RAM state save/load. Reused tokens are not counted as freshly evaluated throughput; answer equality and LRU pressure outcomes remain separate.",
        "restore_latency_reduction_pct": 46.380913752855605
      }
    }
  }
}
```
