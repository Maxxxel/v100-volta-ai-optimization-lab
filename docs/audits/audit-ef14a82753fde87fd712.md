# Public audit excerpt

Original SHA256: `ef14a82753fde87fd7128b70a3dbbc912c60ec4a4fa4dbc144dc7b8100b1d1ad`

Original file: `RESULTS.json`; 42850 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.2142719260000003,
              "format_passes": 2,
              "gpu_energy_j": 734.8476199941947,
              "semantic_passes": 2,
              "tokens_per_s": 12.612230363763018,
              "ttft_s": 0.2012980905
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 10.2307932565,
              "format_passes": 0,
              "gpu_energy_j": 2342.864733279026,
              "semantic_passes": 0,
              "tokens_per_s": 12.62433924891548,
              "ttft_s": 0.170644682
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.2202307655,
              "format_passes": 2,
              "gpu_energy_j": 275.2359166116056,
              "semantic_passes": 2,
              "tokens_per_s": 12.572163014443,
              "ttft_s": 0.1861351905
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9208976520000001,
              "format_passes": 0,
              "gpu_energy_j": 208.39660176282138,
              "semantic_passes": 0,
              "tokens_per_s": 12.541849959800135,
              "ttft_s": 0.2032501715
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8916476725,
              "format_passes": 2,
              "gpu_energy_j": 197.3171589251391,
              "semantic_passes": 2,
              "tokens_per_s": 12.543061642485325,
              "ttft_s": 0.17402700399999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.934974731,
              "format_passes": 0,
              "gpu_energy_j": 436.7555421330809,
              "semantic_passes": 0,
              "tokens_per_s": 12.58935584603283,
              "ttft_s": 0.1874269475
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.491863298,
              "format_passes": 0,
              "gpu_energy_j": 561.5872868034813,
              "semantic_passes": 2,
              "tokens_per_s": 12.598684525078419,
              "ttft_s": 0.2693474575
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.140801175,
              "format_passes": 2,
              "gpu_energy_j": 523.8625523239718,
              "semantic_passes": 2,
              "tokens_per_s": 12.557287403245137,
              "ttft_s": 0.9462146625
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8228079994999999,
              "format_passes": 0,
              "gpu_energy_j": 185.50102131447187,
              "semantic_passes": 0,
              "tokens_per_s": 12.539794848605224,
              "ttft_s": 0.184792135
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2760182245,
              "format_passes": 0,
              "gpu_energy_j": 64.18244456870985,
              "semantic_passes": 0,
              "tokens_per_s": 1836.2280518196328,
              "ttft_s": 0.2758530985
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8301331055000001,
              "format_passes": 0,
              "gpu_energy_j": 217.64320577161283,
              "semantic_passes": 0,
              "tokens_per_s": 2470.900680900021,
              "ttft_s": 0.8298917615
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.5763248765,
              "format_passes": 0,
              "gpu_energy_j": 423.4659256952395,
              "semantic_passes": 0,
              "tokens_per_s": 2601.2898595269708,
              "ttft_s": 1.57596544
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.5396157155,
              "format_passes": 2,
              "gpu_energy_j": 346.44468292288127,
              "semantic_passes": 2,
              "tokens_per_s": 12.572949887190621,
              "ttft_s": 0.187441223
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.9369887585,
              "format_passes": 2,
              "gpu_energy_j": 439.5807378793561,
              "semantic_passes": 2,
              "tokens_per_s": 12.58871165763493,
              "ttft_s": 0.189353388
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 2.012188418,
              "format_passes": 0,
              "gpu_energy_j": 455.2845363317582,
              "semantic_passes": 0,
              "tokens_per_s": 12.598935906513653,
              "ttft_s": 0.18652905
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.949603593,
              "format_passes": 0,
              "gpu_energy_j": 677.3502198026431,
              "semantic_passes": 0,
              "tokens_per_s": 12.604064704784157,
              "ttft_s": 1.048552614
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.249259813,
              "format_passes": 0,
              "gpu_energy_j": 520.6605073920173,
              "semantic_passes": 0,
              "tokens_per_s": 12.597568826999307,
              "ttft_s": 0.344055052
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
              "e2e_s": 0.4780071885,
              "format_passes": 2,
              "gpu_energy_j": 117.11045952393329,
              "semantic_passes": 2,
              "tokens_per_s": 96.53895203278176,
              "ttft_s": 0.0843311145
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3660952690000001,
              "format_passes": 0,
              "gpu_energy_j": 358.9322202815191,
              "semantic_passes": 0,
              "tokens_per_s": 97.03278512277114,
              "ttft_s": 0.0572375675
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204589355,
              "format_passes": 2,
              "gpu_energy_j": 46.752012134014585,
              "semantic_passes": 2,
              "tokens_per_s": 95.00916374699004,
              "ttft_s": 0.067703753
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.188295288,
              "format_passes": 0,
              "gpu_energy_j": 39.54109558064437,
              "semantic_passes": 0,
              "tokens_per_s": 94.24173417161771,
              "ttft_s": 0.0927358905
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15698940849999998,
              "format_passes": 2,
              "gpu_energy_j": 33.76356785457462,
              "semantic_passes": 2,
              "tokens_per_s": 93.665872085447,
              "ttft_s": 0.0608537635
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3065748215,
              "format_passes": 0,
              "gpu_energy_j": 72.4901820917926,
              "semantic_passes": 0,
              "tokens_per_s": 95.58841876632805,
              "ttft_s": 0.07640638350000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.39915113700000004,
              "format_passes": 0,
              "gpu_energy_j": 96.08668153296867,
              "semantic_passes": 2,
              "tokens_per_s": 96.1317279516071,
              "ttft_s": 0.10785582899999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.410799357,
              "format_passes": 2,
              "gpu_energy_j": 375.49296256817445,
              "semantic_passes": 2,
              "tokens_per_s": 94.49682464582708,
              "ttft_s": 1.2520081115
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148441296,
              "format_passes": 0,
              "gpu_energy_j": 30.01909209722394,
              "semantic_passes": 0,
              "tokens_per_s": 93.89953136664099,
              "ttft_s": 0.06322331
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.30506975599999997,
              "format_passes": 0,
              "gpu_energy_j": 78.73312520094649,
              "semantic_passes": 0,
              "tokens_per_s": 1661.5094127769562,
              "ttft_s": 0.3048589765
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1485030495,
              "format_passes": 0,
              "gpu_energy_j": 314.2219063556979,
              "semantic_passes": 0,
              "tokens_per_s": 1785.1049207511237,
              "ttft_s": 1.148280396
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.281598391,
              "format_passes": 0,
              "gpu_energy_j": 624.7255747723931,
              "semantic_passes": 0,
              "tokens_per_s": 1796.5656966973647,
              "ttft_s": 2.2812604395
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2543337875,
              "format_passes": 2,
              "gpu_energy_j": 58.1595693155838,
              "semantic_passes": 2,
              "tokens_per_s": 95.38505228830536,
              "ttft_s": 0.076103231
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351035314,
              "format_passes": 0,
              "gpu_energy_j": 81.07290007933281,
              "semantic_passes": 2,
              "tokens_per_s": 96.1215069001089,
              "ttft_s": 0.070102598
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31436459,
              "format_passes": 0,
              "gpu_energy_j": 75.45962256722477,
              "semantic_passes": 0,
              "tokens_per_s": 95.9748872962142,
              "ttft_s": 0.0746939415
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5819116915,
              "format_passes": 0,
              "gpu_energy_j": 146.12652952704718,
              "semantic_passes": 0,
              "tokens_per_s": 96.2611305046328,
              "ttft_s": 0.33483514999999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.543942385,
              "format_passes": 0,
              "gpu_energy_j": 134.23093781174282,
              "semantic_passes": 0,
              "tokens_per_s": 95.90584021324588,
              "ttft_s": 0.293611621
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": -2,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -85.12860145299356,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -84.0633001540022,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 665.4391748992614,
            "ttft_change_pct": -58.10635148573354
          },
          "decode": {
            "e2e_change_pct": -86.64722045739641,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -84.6797719397498,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 668.6167427028464,
            "ttft_change_pct": -66.45804203848556
          },
          "energy": {
            "e2e_change_pct": -83.23355214567404,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -83.01384037753043,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 655.7105618010422,
            "ttft_change_pct": -63.62657011920591
          },
          "filtering": {
            "e2e_change_pct": -79.55307111587683,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -81.0260362951376,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 651.4181278972941,
            "ttft_change_pct": -54.37352410794891
          },
          "german": {
            "e2e_change_pct": -82.39333614141185,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -82.88868132984608,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 646.7544588012383,
            "ttft_change_pct": -65.03199957404311
          },
          "ha_sim": {
            "e2e_change_pct": -84.156133070453,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -83.40257304171665,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 659.2796639905127,
            "ttft_change_pct": -59.23404584071348
          },
          "jarvis_memory": {
            "e2e_change_pct": -83.98182045859564,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -82.89016083681527,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 663.0298842728483,
            "ttft_change_pct": -59.95661885911807
          },
          "long_context": {
            "e2e_change_pct": -34.09946829835798,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -28.32223626170578,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 652.5257773538461,
            "ttft_change_pct": 32.317555531433115
          },
          "math": {
            "e2e_change_pct": -81.95918171794585,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -83.81729012352235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 648.8123410335157,
            "ttft_change_pct": -65.78679606683477
          },
          "prefill": {
            "e2e_change_pct": 10.525222221331965,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 22.670810889198133,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -9.51508386278801,
            "ttft_change_pct": 10.514972700225078
          },
          "prefill2048": {
            "e2e_change_pct": 38.351674194253626,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 44.37478314183232,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -27.754889763480804,
            "ttft_change_pct": 38.36507955260622
          },
          "prefill4096": {
            "e2e_change_pct": 44.741634482477835,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 47.52676351626845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -30.935582202897617,
            "ttft_change_pct": 44.75320217047398
          },
          "pve_sim": {
            "e2e_change_pct": -83.48069684275706,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -83.21245145836741,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 658.6529266730323,
            "ttft_change_pct": -59.39888260332147
          },
          "sorting": {
            "e2e_change_pct": -81.87726632591091,
            "format_pass_change": -2,
            "gpu_energy_change_pct": -81.5567669160282,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 663.5531698099713,
            "ttft_change_pct": -62.977901404119585
          },
          "time": {
            "e2e_change_pct": -84.3769804463709,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -83.42583229924625,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 661.7697876103581,
            "ttft_change_pct": -59.955866659911685
          },
          "tool-call": {
            "e2e_change_pct": -80.27152893083691,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -78.42673918824097,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 663.7308500018627,
            "ttft_change_pct": -68.06691952989591
          },
          "tool-final": {
            "e2e_change_pct": -75.81682730220015,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -74.21910517390612,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 661.3043558666571,
            "ttft_change_pct": -14.66144173927142
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 345991433644750,
          "end_ns": 345992141550227,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 346035568856472,
          "end_ns": 346036077557818,
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
