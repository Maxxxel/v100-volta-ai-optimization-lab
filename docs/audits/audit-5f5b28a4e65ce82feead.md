# Public audit excerpt

Original SHA256: `5f5b28a4e65ce82feead1fbc527e1a655a839fabc80688272a1e4d78057b60ef`

Original file: `RESULTS.json`; 39504 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.525709827,
              "format_passes": 2,
              "gpu_energy_j": 136.0043932313759,
              "semantic_passes": 2,
              "tokens_per_s": 96.53393863649889,
              "ttft_s": 0.13203700499999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3670257785,
              "format_passes": 0,
              "gpu_energy_j": 354.96575385655126,
              "semantic_passes": 0,
              "tokens_per_s": 97.03679079356596,
              "ttft_s": 0.0578746115
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20463552499999998,
              "format_passes": 2,
              "gpu_energy_j": 45.47533735970467,
              "semantic_passes": 2,
              "tokens_per_s": 95.2082755893654,
              "ttft_s": 0.0680576395
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2305588105,
              "format_passes": 0,
              "gpu_energy_j": 54.18060670314523,
              "semantic_passes": 0,
              "tokens_per_s": 93.64637538404,
              "ttft_s": 0.134437169
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1572714725,
              "format_passes": 2,
              "gpu_energy_j": 33.936046461996284,
              "semantic_passes": 2,
              "tokens_per_s": 93.28895847396177,
              "ttft_s": 0.060828814499999995
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30654201849999996,
              "format_passes": 0,
              "gpu_energy_j": 75.42268411043187,
              "semantic_passes": 0,
              "tokens_per_s": 95.95415529910514,
              "ttft_s": 0.0771927205
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3982023835,
              "format_passes": 0,
              "gpu_energy_j": 99.17394421722062,
              "semantic_passes": 2,
              "tokens_per_s": 96.26431623541097,
              "ttft_s": 0.1073427455
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.029955763,
              "format_passes": 2,
              "gpu_energy_j": 271.23951156626674,
              "semantic_passes": 2,
              "tokens_per_s": 94.02685978245034,
              "ttft_s": 0.8704499864999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14844074299999999,
              "format_passes": 0,
              "gpu_energy_j": 30.709063882402184,
              "semantic_passes": 0,
              "tokens_per_s": 93.58502706391138,
              "ttft_s": 0.062964817
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2053610165,
              "format_passes": 0,
              "gpu_energy_j": 51.61689677194249,
              "semantic_passes": 0,
              "tokens_per_s": 2471.1908259331635,
              "ttft_s": 0.2052334455
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7544872465,
              "format_passes": 0,
              "gpu_energy_j": 198.98948068524533,
              "semantic_passes": 0,
              "tokens_per_s": 2718.8528846928507,
              "ttft_s": 0.7542525735000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4976357784999998,
              "format_passes": 0,
              "gpu_energy_j": 404.0167585886483,
              "semantic_passes": 0,
              "tokens_per_s": 2738.1219147845386,
              "ttft_s": 1.4973229319999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.253781787,
              "format_passes": 2,
              "gpu_energy_j": 60.5820667568966,
              "semantic_passes": 2,
              "tokens_per_s": 95.73163263428975,
              "ttft_s": 0.076155856
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3513658205,
              "format_passes": 0,
              "gpu_energy_j": 83.69817252508639,
              "semantic_passes": 2,
              "tokens_per_s": 96.18612601703265,
              "ttft_s": 0.07064145999999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314656565,
              "format_passes": 0,
              "gpu_energy_j": 73.70689308829807,
              "semantic_passes": 0,
              "tokens_per_s": 95.96110783289606,
              "ttft_s": 0.0749370805
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5502635195000001,
              "format_passes": 0,
              "gpu_energy_j": 138.24907937466213,
              "semantic_passes": 0,
              "tokens_per_s": 96.18061299207281,
              "ttft_s": 0.3030462075
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5244580365,
              "format_passes": 0,
              "gpu_energy_j": 132.88534767370032,
              "semantic_passes": 0,
              "tokens_per_s": 95.80341149750892,
              "ttft_s": 0.274002506
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
              "e2e_s": 0.5262917735,
              "format_passes": 2,
              "gpu_energy_j": 131.87902373884543,
              "semantic_passes": 2,
              "tokens_per_s": 96.43264673821461,
              "ttft_s": 0.1321600885
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3715403825,
              "format_passes": 0,
              "gpu_energy_j": 356.2861682646013,
              "semantic_passes": 0,
              "tokens_per_s": 96.68411549176905,
              "ttft_s": 0.0574298625
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20451362350000002,
              "format_passes": 2,
              "gpu_energy_j": 45.06192722905014,
              "semantic_passes": 2,
              "tokens_per_s": 95.07858623543282,
              "ttft_s": 0.06772386
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22939228849999999,
              "format_passes": 0,
              "gpu_energy_j": 55.080283635392846,
              "semantic_passes": 0,
              "tokens_per_s": 94.11129015182388,
              "ttft_s": 0.133736997
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.164752606,
              "format_passes": 2,
              "gpu_energy_j": 35.89155835772082,
              "semantic_passes": 2,
              "tokens_per_s": 92.67387771328796,
              "ttft_s": 0.067576722
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3077359195,
              "format_passes": 0,
              "gpu_energy_j": 72.60751224925102,
              "semantic_passes": 0,
              "tokens_per_s": 95.25689895919541,
              "ttft_s": 0.0767479295
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3978893905,
              "format_passes": 0,
              "gpu_energy_j": 92.59045304823884,
              "semantic_passes": 2,
              "tokens_per_s": 96.21837691479752,
              "ttft_s": 0.1068612615
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0320384405,
              "format_passes": 2,
              "gpu_energy_j": 272.4506534811304,
              "semantic_passes": 2,
              "tokens_per_s": 93.11419904268752,
              "ttft_s": 0.8708424415
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148384377,
              "format_passes": 0,
              "gpu_energy_j": 32.7765194067605,
              "semantic_passes": 0,
              "tokens_per_s": 93.85125656793646,
              "ttft_s": 0.063106753
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205368869,
              "format_passes": 0,
              "gpu_energy_j": 50.47655468805229,
              "semantic_passes": 0,
              "tokens_per_s": 2471.2927205789965,
              "ttft_s": 0.2052312925
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7541500750000001,
              "format_passes": 0,
              "gpu_energy_j": 201.14731164795592,
              "semantic_passes": 0,
              "tokens_per_s": 2720.2031849101895,
              "ttft_s": 0.7539016505
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4954240545,
              "format_passes": 0,
              "gpu_energy_j": 402.2241572577665,
              "semantic_passes": 0,
              "tokens_per_s": 2742.2316826389883,
              "ttft_s": 1.4950817779999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254579553,
              "format_passes": 2,
              "gpu_energy_j": 60.316184209201715,
              "semantic_passes": 2,
              "tokens_per_s": 95.41584774278518,
              "ttft_s": 0.0763367355
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3563520615,
              "format_passes": 0,
              "gpu_energy_j": 85.51622008145944,
              "semantic_passes": 2,
              "tokens_per_s": 94.90161398320379,
              "ttft_s": 0.071773982
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31438176949999996,
              "format_passes": 0,
              "gpu_energy_j": 73.58964666964044,
              "semantic_passes": 0,
              "tokens_per_s": 95.98691548429274,
              "ttft_s": 0.0747362835
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.551669604,
              "format_passes": 0,
              "gpu_energy_j": 135.76394327370463,
              "semantic_passes": 0,
              "tokens_per_s": 96.09465325414956,
              "ttft_s": 0.3046005685
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5242210224999999,
              "format_passes": 0,
              "gpu_energy_j": 133.12679578848662,
              "semantic_passes": 0,
              "tokens_per_s": 95.83478089284657,
              "ttft_s": 0.2736433015
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
            "e2e_change_pct": 0.1106972839600262,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.0332619369965674,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10492879469643501,
            "ttft_change_pct": 0.09321894267444453
          },
          "decode": {
            "e2e_change_pct": 0.3302500999618152,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3719836050955161,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.36344493558858604,
            "ttft_change_pct": -0.7684699533576977
          },
          "energy": {
            "e2e_change_pct": -0.05957005754497757,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.909086451375829,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1362164718663017,
            "ttft_change_pct": -0.4904364924381621
          },
          "filtering": {
            "e2e_change_pct": -0.505954206421444,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6605146878050592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4964578349960558,
            "ttft_change_pct": -0.5208172748713547
          },
          "german": {
            "e2e_change_pct": 4.756828038219063,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.762344467303926,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.659328575144813,
            "ttft_change_pct": 11.093274717691592
          },
          "ha_sim": {
            "e2e_change_pct": 0.3894738495695105,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.7325267515790905,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.7266557010858654,
            "ttft_change_pct": -0.5762084781038346
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.078601488330865,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.63832745681866,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04772206608845142,
            "ttft_change_pct": -0.44854824399848114
          },
          "long_context": {
            "e2e_change_pct": 0.20221038367063127,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4465211973985417,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.9706383281058661,
            "ttft_change_pct": 0.045086450236864195
          },
          "math": {
            "e2e_change_pct": -0.03797205461304465,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.732395139999925,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.28447873808195023,
            "ttft_change_pct": 0.22542112684929005
          },
          "prefill": {
            "e2e_change_pct": 0.0038237539596641668,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.209241847545673,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.004123301396385948,
            "ttft_change_pct": -0.0010490492886039426
          },
          "prefill2048": {
            "e2e_change_pct": -0.04468882695685128,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.084394489236229,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04966433546078619,
            "ttft_change_pct": -0.04652592676902545
          },
          "prefill4096": {
            "e2e_change_pct": -0.14768103378346442,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4436947955188564,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.15009440712843158,
            "ttft_change_pct": -0.14967739771449828
          },
          "pve_sim": {
            "e2e_change_pct": 0.31435116342688474,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4388799556175882,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3298647299904811,
            "ttft_change_pct": 0.23751226694899152
          },
          "sorting": {
            "e2e_change_pct": 1.419102459341226,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1721472542642895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.3354441924414373,
            "ttft_change_pct": 1.603197329160544
          },
          "time": {
            "e2e_change_pct": -0.08733188198378761,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.15907117196918286,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.026893865628996316,
            "ttft_change_pct": -0.2679541271960795
          },
          "tool-call": {
            "e2e_change_pct": 0.2555292964500966,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.7975787702879775,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08937324815171399,
            "ttft_change_pct": 0.5129122099308825
          },
          "tool-final": {
            "e2e_change_pct": -0.045192176209529755,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.18169656701292336,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.032743505525867356,
            "ttft_change_pct": -0.13109533385070593
          }
        }
      },
      "complete": true
    }
  }
}
```
