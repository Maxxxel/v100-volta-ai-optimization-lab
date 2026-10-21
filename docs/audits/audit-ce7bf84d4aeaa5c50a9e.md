# Public audit excerpt

Original SHA256: `ce7bf84d4aeaa5c50a9ec57021c617483960ff870b6c8950d8bb9bd72f557d40`

Original file: `RESULTS.json`; 43217 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6671537095,
              "format_passes": 2,
              "gpu_energy_j": 176.25846651781384,
              "semantic_passes": 2,
              "tokens_per_s": 79.21311177938371,
              "ttft_s": 0.12425837249999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6580534285,
              "format_passes": 0,
              "gpu_energy_j": 452.52451526375665,
              "semantic_passes": 0,
              "tokens_per_s": 79.63009019024196,
              "ttft_s": 0.06304270049999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238267123,
              "format_passes": 2,
              "gpu_energy_j": 54.45110123079861,
              "semantic_passes": 2,
              "tokens_per_s": 78.13896365949546,
              "ttft_s": 0.071853577
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24306805799999998,
              "format_passes": 0,
              "gpu_energy_j": 60.87113768971308,
              "semantic_passes": 0,
              "tokens_per_s": 76.61076670920372,
              "ttft_s": 0.12553854650000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182845726,
              "format_passes": 2,
              "gpu_energy_j": 41.303329668242256,
              "semantic_passes": 2,
              "tokens_per_s": 77.28362505630069,
              "ttft_s": 0.0663561835
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36456657400000003,
              "format_passes": 0,
              "gpu_energy_j": 90.41025996790265,
              "semantic_passes": 0,
              "tokens_per_s": 77.40720613016595,
              "ttft_s": 0.080262683
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468750389,
              "format_passes": 0,
              "gpu_energy_j": 116.6463114519636,
              "semantic_passes": 2,
              "tokens_per_s": 79.13150570766831,
              "ttft_s": 0.1148962685
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081218624,
              "format_passes": 2,
              "gpu_energy_j": 288.48050966733746,
              "semantic_passes": 2,
              "tokens_per_s": 77.70528846964648,
              "ttft_s": 0.8237768655
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2342273145,
              "format_passes": 0,
              "gpu_energy_j": 57.0045031268819,
              "semantic_passes": 0,
              "tokens_per_s": 77.97597227661531,
              "ttft_s": 0.0675262365
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199485246,
              "format_passes": 0,
              "gpu_energy_j": 47.748473088643266,
              "semantic_passes": 0,
              "tokens_per_s": 2544.8196469801806,
              "ttft_s": 0.199351796
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.719121407,
              "format_passes": 0,
              "gpu_energy_j": 189.98712035800236,
              "semantic_passes": 0,
              "tokens_per_s": 2853.1676078910386,
              "ttft_s": 0.718871553
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4185547944999999,
              "format_passes": 0,
              "gpu_energy_j": 380.53733203744173,
              "semantic_passes": 0,
              "tokens_per_s": 2891.0662683456667,
              "ttft_s": 1.4182378325
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29544615399999996,
              "format_passes": 2,
              "gpu_energy_j": 74.4810435345635,
              "semantic_passes": 2,
              "tokens_per_s": 78.63017349314433,
              "ttft_s": 0.0791754265
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3537849115,
              "format_passes": 2,
              "gpu_energy_j": 89.76510869278628,
              "semantic_passes": 2,
              "tokens_per_s": 78.77161256471817,
              "ttft_s": 0.074441964
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3697399295,
              "format_passes": 2,
              "gpu_energy_j": 93.6040738147428,
              "semantic_passes": 2,
              "tokens_per_s": 78.80501184181469,
              "ttft_s": 0.0778757105
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6205677035,
              "format_passes": 0,
              "gpu_energy_j": 163.7563402889575,
              "semantic_passes": 0,
              "tokens_per_s": 78.87659510434088,
              "ttft_s": 0.3184039065
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5619588475,
              "format_passes": 0,
              "gpu_energy_j": 147.04034382560917,
              "semantic_passes": 0,
              "tokens_per_s": 78.66504940725274,
              "ttft_s": 0.256465446
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
              "e2e_s": 0.6584113025,
              "format_passes": 2,
              "gpu_energy_j": 176.48776961044632,
              "semantic_passes": 2,
              "tokens_per_s": 80.36578951205814,
              "ttft_s": 0.12332966449999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.637505633,
              "format_passes": 0,
              "gpu_energy_j": 453.4159583875655,
              "semantic_passes": 0,
              "tokens_per_s": 80.65228754106352,
              "ttft_s": 0.06266742
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23708606,
              "format_passes": 2,
              "gpu_energy_j": 54.34957295711993,
              "semantic_passes": 2,
              "tokens_per_s": 78.91939353814061,
              "ttft_s": 0.07229661600000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2405880305,
              "format_passes": 0,
              "gpu_energy_j": 55.55769485719982,
              "semantic_passes": 0,
              "tokens_per_s": 78.36922803934233,
              "ttft_s": 0.1257600015
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1806687325,
              "format_passes": 2,
              "gpu_energy_j": 40.47047957526285,
              "semantic_passes": 2,
              "tokens_per_s": 78.0550549191649,
              "ttft_s": 0.0653106575
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3533955315,
              "format_passes": 0,
              "gpu_energy_j": 88.72951093855801,
              "semantic_passes": 0,
              "tokens_per_s": 79.94004124955683,
              "ttft_s": 0.07815097900000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46363524700000003,
              "format_passes": 0,
              "gpu_energy_j": 121.01685550113066,
              "semantic_passes": 2,
              "tokens_per_s": 80.10129594756683,
              "ttft_s": 0.113980215
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0646306485,
              "format_passes": 2,
              "gpu_energy_j": 288.78688015376963,
              "semantic_passes": 2,
              "tokens_per_s": 79.02171675285012,
              "ttft_s": 0.811457293
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233236341,
              "format_passes": 0,
              "gpu_energy_j": 53.9490325709553,
              "semantic_passes": 0,
              "tokens_per_s": 78.52862622703938,
              "ttft_s": 0.0675706085
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19656182849999998,
              "format_passes": 0,
              "gpu_energy_j": 49.27807727358832,
              "semantic_passes": 0,
              "tokens_per_s": 2583.1994958060895,
              "ttft_s": 0.19642136300000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7078428905,
              "format_passes": 0,
              "gpu_energy_j": 188.5969679439536,
              "semantic_passes": 0,
              "tokens_per_s": 2898.60205343172,
              "ttft_s": 0.707598992
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3997449325,
              "format_passes": 0,
              "gpu_energy_j": 377.0562098412205,
              "semantic_passes": 0,
              "tokens_per_s": 2930.0979736511417,
              "ttft_s": 1.3993799155
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2930600085,
              "format_passes": 2,
              "gpu_energy_j": 73.3419116385416,
              "semantic_passes": 2,
              "tokens_per_s": 79.50159540715896,
              "ttft_s": 0.0791847185
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.350404538,
              "format_passes": 2,
              "gpu_energy_j": 87.06486453384376,
              "semantic_passes": 2,
              "tokens_per_s": 79.61468312033583,
              "ttft_s": 0.074025173
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3650491425,
              "format_passes": 2,
              "gpu_energy_j": 93.74971669737877,
              "semantic_passes": 2,
              "tokens_per_s": 79.93761570621332,
              "ttft_s": 0.0772995755
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6126229085,
              "format_passes": 0,
              "gpu_energy_j": 163.73345787115463,
              "semantic_passes": 0,
              "tokens_per_s": 80.08192634337621,
              "ttft_s": 0.31552038400000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5553645334999999,
              "format_passes": 0,
              "gpu_energy_j": 147.5537172631661,
              "semantic_passes": 0,
              "tokens_per_s": 79.60779892471402,
              "ttft_s": 0.25381358350000005
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
            "e2e_change_pct": -1.3104037158920945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.13009479610404107,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.4551602718054557,
            "ttft_change_pct": -0.7474007435595564
          },
          "decode": {
            "e2e_change_pct": -1.2392722180604943,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.19699333267928498,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.283682271839015,
            "ttft_change_pct": -0.5952798611474353
          },
          "energy": {
            "e2e_change_pct": -0.49568861416100507,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.18645770495685499,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.9987717293590048,
            "ttft_change_pct": 0.6165858660035939
          },
          "filtering": {
            "e2e_change_pct": -1.0203016885089733,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -8.729002010112264,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.29531879874445,
            "ttft_change_pct": 0.17640398600597962
          },
          "german": {
            "e2e_change_pct": -1.1906176576421457,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.0164236144375014,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.9981802255034422,
            "ttft_change_pct": -1.5756270853039767
          },
          "ha_sim": {
            "e2e_change_pct": -3.0641982278934887,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8590246615166617,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 3.2720921552597204,
            "ttft_change_pct": -2.6309910422505967
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.09122938775843,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.7468343360063328,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.2255425082914106,
            "ttft_change_pct": -0.7972874245258832
          },
          "long_context": {
            "e2e_change_pct": -1.5341925427285075,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.10620145076194465,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.6941295877408447,
            "ttft_change_pct": -1.4954987225239025
          },
          "math": {
            "e2e_change_pct": -0.4230819544319142,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.360051203543803,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.7087490342070568,
            "ttft_change_pct": 0.06571075525585446
          },
          "prefill": {
            "e2e_change_pct": -1.465480559900667,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.2034619873716252,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.5081559461965321,
            "ttft_change_pct": -1.469980736968124
          },
          "prefill2048": {
            "e2e_change_pct": -1.5683744622554396,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7317087660622668,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.592421188822657,
            "ttft_change_pct": -1.5680911218363458
          },
          "prefill4096": {
            "e2e_change_pct": -1.3259876934559878,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9147912446810125,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.3500799249340556,
            "ttft_change_pct": -1.3296723982294423
          },
          "pve_sim": {
            "e2e_change_pct": -0.8076414154302824,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5294252630782101,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.1082538360297711,
            "ttft_change_pct": 0.011735964567227697
          },
          "sorting": {
            "e2e_change_pct": -0.955488317935238,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0081221961017035,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.0702720538125376,
            "ttft_change_pct": -0.5598871625686841
          },
          "time": {
            "e2e_change_pct": -1.2686720112548788,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.15559459829090905,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.437223138386301,
            "ttft_change_pct": -0.7398134749602159
          },
          "tool-call": {
            "e2e_change_pct": -1.2802462898393485,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.013973454562110632,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.5281228068235952,
            "ttft_change_pct": -0.9056178147110683
          },
          "tool-final": {
            "e2e_change_pct": -1.173451406510706,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.34913781088936613,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 1.198435041438306,
            "ttft_change_pct": -1.0340038166388843
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 420111439940863,
          "end_ns": 420113050925476,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 420157938953387,
          "end_ns": 420159498836118,
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
