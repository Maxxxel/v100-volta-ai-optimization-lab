# Public audit excerpt

Original SHA256: `45fe8bfb578d9aeee029e8f934e8a685422dd5ab358f29c6bd52a8afe3b744fb`

Original file: `RESULTS.json`; 42946 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5264795835,
              "format_passes": 2,
              "gpu_energy_j": 129.7223537411238,
              "semantic_passes": 2,
              "tokens_per_s": 96.43000200725591,
              "ttft_s": 0.1323871435
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3666738944999999,
              "format_passes": 0,
              "gpu_energy_j": 356.1580557051128,
              "semantic_passes": 0,
              "tokens_per_s": 97.04301529212162,
              "ttft_s": 0.0576836015
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204874057,
              "format_passes": 2,
              "gpu_energy_j": 44.11386042870321,
              "semantic_passes": 2,
              "tokens_per_s": 95.01402938326723,
              "ttft_s": 0.068046571
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2298257255,
              "format_passes": 0,
              "gpu_energy_j": 53.712071699075636,
              "semantic_passes": 0,
              "tokens_per_s": 94.2902721978328,
              "ttft_s": 0.134295106
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.157743622,
              "format_passes": 2,
              "gpu_energy_j": 31.63942668491655,
              "semantic_passes": 2,
              "tokens_per_s": 93.76616512538791,
              "ttft_s": 0.06175857
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.306995602,
              "format_passes": 0,
              "gpu_energy_j": 70.38466625438201,
              "semantic_passes": 0,
              "tokens_per_s": 95.83496655300742,
              "ttft_s": 0.077450885
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39821241949999997,
              "format_passes": 0,
              "gpu_energy_j": 94.77883335530697,
              "semantic_passes": 2,
              "tokens_per_s": 96.19813618970562,
              "ttft_s": 0.107112614
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.030854924,
              "format_passes": 2,
              "gpu_energy_j": 273.66641397566787,
              "semantic_passes": 2,
              "tokens_per_s": 94.07898851195932,
              "ttft_s": 0.8713844105
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14885203800000002,
              "format_passes": 0,
              "gpu_energy_j": 29.826448220972576,
              "semantic_passes": 0,
              "tokens_per_s": 93.52257308336581,
              "ttft_s": 0.0632748765
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2059356285,
              "format_passes": 0,
              "gpu_energy_j": 51.06006654518859,
              "semantic_passes": 0,
              "tokens_per_s": 2464.8274334987746,
              "ttft_s": 0.2057573925
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7553718295,
              "format_passes": 0,
              "gpu_energy_j": 201.5600395168977,
              "semantic_passes": 0,
              "tokens_per_s": 2715.725701104754,
              "ttft_s": 0.7551449615
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5017094405,
              "format_passes": 0,
              "gpu_energy_j": 403.2184444506262,
              "semantic_passes": 0,
              "tokens_per_s": 2730.6045603039242,
              "ttft_s": 1.5014000035000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25416560850000003,
              "format_passes": 2,
              "gpu_energy_j": 57.357169767947326,
              "semantic_passes": 2,
              "tokens_per_s": 95.55422842264755,
              "ttft_s": 0.076198265
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.350933306,
              "format_passes": 0,
              "gpu_energy_j": 81.46288641783508,
              "semantic_passes": 2,
              "tokens_per_s": 96.16687494925894,
              "ttft_s": 0.070110806
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3157814265,
              "format_passes": 0,
              "gpu_energy_j": 73.2644463178938,
              "semantic_passes": 0,
              "tokens_per_s": 95.5639084865441,
              "ttft_s": 0.07508163749999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550180613,
              "format_passes": 0,
              "gpu_energy_j": 140.8837112232853,
              "semantic_passes": 0,
              "tokens_per_s": 96.19883994476909,
              "ttft_s": 0.30329894599999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5245200425000001,
              "format_passes": 0,
              "gpu_energy_j": 135.01699702720106,
              "semantic_passes": 0,
              "tokens_per_s": 95.82693672101584,
              "ttft_s": 0.273925379
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5371763505,
              "format_passes": 2,
              "gpu_energy_j": 132.52254705356017,
              "semantic_passes": 2,
              "tokens_per_s": 93.88176001882456,
              "ttft_s": 0.132391258
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.405196581,
              "format_passes": 0,
              "gpu_energy_j": 352.75827034795907,
              "semantic_passes": 0,
              "tokens_per_s": 94.27159059494821,
              "ttft_s": 0.058278421999999996
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.208989738,
              "format_passes": 2,
              "gpu_energy_j": 47.10418301669186,
              "semantic_passes": 2,
              "tokens_per_s": 92.42350718021811,
              "ttft_s": 0.06827647349999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2325404345,
              "format_passes": 0,
              "gpu_energy_j": 56.097484586525226,
              "semantic_passes": 0,
              "tokens_per_s": 91.61055670563407,
              "ttft_s": 0.134306805
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1599926395,
              "format_passes": 2,
              "gpu_energy_j": 33.57164134895129,
              "semantic_passes": 2,
              "tokens_per_s": 90.94911968869084,
              "ttft_s": 0.061001778
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31359947499999996,
              "format_passes": 0,
              "gpu_energy_j": 71.82954218846916,
              "semantic_passes": 0,
              "tokens_per_s": 93.1941254289099,
              "ttft_s": 0.0775136435
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.407065844,
              "format_passes": 0,
              "gpu_energy_j": 92.90425921604822,
              "semantic_passes": 2,
              "tokens_per_s": 93.62137560397031,
              "ttft_s": 0.1079107265
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0392390950000001,
              "format_passes": 2,
              "gpu_energy_j": 276.4993137441337,
              "semantic_passes": 2,
              "tokens_per_s": 91.40377981517588,
              "ttft_s": 0.8750168545
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1511946165,
              "format_passes": 0,
              "gpu_energy_j": 32.94780319047538,
              "semantic_passes": 0,
              "tokens_per_s": 91.18264878770528,
              "ttft_s": 0.06343214450000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20693186349999998,
              "format_passes": 0,
              "gpu_energy_j": 50.42457616506575,
              "semantic_passes": 0,
              "tokens_per_s": 2452.9105044388807,
              "ttft_s": 0.206804025
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7562678064999999,
              "format_passes": 0,
              "gpu_energy_j": 198.05543039749915,
              "semantic_passes": 0,
              "tokens_per_s": 2712.6147317236773,
              "ttft_s": 0.7560387959999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5005726235,
              "format_passes": 0,
              "gpu_energy_j": 404.2703462630591,
              "semantic_passes": 0,
              "tokens_per_s": 2732.697127469458,
              "ttft_s": 1.500230176
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25939957049999995,
              "format_passes": 2,
              "gpu_energy_j": 56.90659636442612,
              "semantic_passes": 2,
              "tokens_per_s": 92.90181665277537,
              "ttft_s": 0.07636755149999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30667055,
              "format_passes": 2,
              "gpu_energy_j": 68.80783584587178,
              "semantic_passes": 2,
              "tokens_per_s": 93.01361685903058,
              "ttft_s": 0.0701573505
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.32597014150000003,
              "format_passes": 0,
              "gpu_energy_j": 74.08405497129857,
              "semantic_passes": 0,
              "tokens_per_s": 91.67323329919495,
              "ttft_s": 0.075025145
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560999073,
              "format_passes": 0,
              "gpu_energy_j": 138.797037385372,
              "semantic_passes": 0,
              "tokens_per_s": 93.40320846450956,
              "ttft_s": 0.306517008
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5318703595000001,
              "format_passes": 0,
              "gpu_energy_j": 129.2142245916397,
              "semantic_passes": 0,
              "tokens_per_s": 93.22888072032585,
              "ttft_s": 0.27430228300000004
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 2,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 2.031753430757677,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1586050759027087,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.6425821169635544,
            "ttft_change_pct": 0.003107930189627517
          },
          "decode": {
            "e2e_change_pct": 2.8187182512982467,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9545720790795964,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.855872407540916,
            "ttft_change_pct": 1.0311778122938486
          },
          "energy": {
            "e2e_change_pct": 2.008883438082165,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.778646345906658,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.726462839081878,
            "ttft_change_pct": 0.3378605220239361
          },
          "filtering": {
            "e2e_change_pct": 1.1812032765670555,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.441111303272716,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.8419851059252044,
            "ttft_change_pct": 0.008711412015260933
          },
          "german": {
            "e2e_change_pct": 1.4257422718491952,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.106983806239086,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.0043304351095146,
            "ttft_change_pct": -1.2254040208508732
          },
          "ha_sim": {
            "e2e_change_pct": 2.151129513575234,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.052827712310412,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.7556133414382122,
            "ttft_change_pct": 0.08103006182564876
          },
          "jarvis_memory": {
            "e2e_change_pct": 2.2232919081520697,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.97784048705405,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.678597203436317,
            "ttft_change_pct": 0.7451153232055363
          },
          "long_context": {
            "e2e_change_pct": 0.8133221081650488,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0351653048363163,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.8435772313212815,
            "ttft_change_pct": 0.4168589610084483
          },
          "math": {
            "e2e_change_pct": 1.5737631351745218,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.465057543485901,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.5019887910640914,
            "ttft_change_pct": 0.2485473045530373
          },
          "prefill": {
            "e2e_change_pct": 0.4837603902036802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.244593717010578,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4834792447509395,
            "ttft_change_pct": 0.5086730966421982
          },
          "prefill2048": {
            "e2e_change_pct": 0.11861403417612326,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7387420283298427,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11455388811215661,
            "ttft_change_pct": 0.11836594899929942
          },
          "prefill4096": {
            "e2e_change_pct": -0.07570152849417644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2608764125029195,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07663384130951467,
            "ttft_change_pct": -0.07791577842500841
          },
          "pve_sim": {
            "e2e_change_pct": 2.0592723110294253,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7855572465379823,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.775818311399325,
            "ttft_change_pct": 0.22216581965479598
          },
          "sorting": {
            "e2e_change_pct": -12.612868383601072,
            "format_pass_change": 2,
            "gpu_energy_change_pct": -15.53474364639339,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -3.2789441186397483,
            "ttft_change_pct": 0.06638705594113059
          },
          "time": {
            "e2e_change_pct": 3.2265086369796414,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.118699034247106,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -4.07128093541399,
            "ttft_change_pct": -0.07524143303346831
          },
          "tool-call": {
            "e2e_change_pct": 1.9663470039428699,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.481132076799252,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.906096873792441,
            "ttft_change_pct": 1.061019842779154
          },
          "tool-final": {
            "e2e_change_pct": 1.4013414940192703,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.297808841350781,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -2.7111959221380544,
            "ttft_change_pct": 0.13759367656109855
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 362223182324101,
          "end_ns": 362223889956209,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 362268089419277,
          "end_ns": 362268846863070,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```

</details>
