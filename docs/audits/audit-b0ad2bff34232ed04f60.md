# Public audit excerpt

Original SHA256: `b0ad2bff34232ed04f602e6067092f57ccffc69622deafecbb8e4e5fe317ec5c`

Original file: `RESULTS.json`; 43844 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.4788273165,
              "format_passes": 2,
              "gpu_energy_j": 116.97195922605476,
              "semantic_passes": 2,
              "tokens_per_s": 96.34550405361475,
              "ttft_s": 0.084353816
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3667984455,
              "format_passes": 0,
              "gpu_energy_j": 361.0553159958547,
              "semantic_passes": 0,
              "tokens_per_s": 97.03835684360533,
              "ttft_s": 0.057402035000000004
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2046329515,
              "format_passes": 2,
              "gpu_energy_j": 46.33363019614259,
              "semantic_passes": 2,
              "tokens_per_s": 95.10491079508432,
              "ttft_s": 0.067919867
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18812461949999998,
              "format_passes": 0,
              "gpu_energy_j": 40.24037704275622,
              "semantic_passes": 0,
              "tokens_per_s": 94.15161579649296,
              "ttft_s": 0.09249299350000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15661362,
              "format_passes": 2,
              "gpu_energy_j": 33.19287756720421,
              "semantic_passes": 2,
              "tokens_per_s": 94.00486161711143,
              "ttft_s": 0.060837586
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3057609115,
              "format_passes": 0,
              "gpu_energy_j": 73.88999527405875,
              "semantic_passes": 0,
              "tokens_per_s": 95.91261409175203,
              "ttft_s": 0.0763199235
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4009519595,
              "format_passes": 0,
              "gpu_energy_j": 95.0360383706362,
              "semantic_passes": 2,
              "tokens_per_s": 95.97100545845805,
              "ttft_s": 0.10918673549999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.4115433130000001,
              "format_passes": 2,
              "gpu_energy_j": 370.10468533760263,
              "semantic_passes": 2,
              "tokens_per_s": 94.5908357979933,
              "ttft_s": 1.2529033295
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1493233425,
              "format_passes": 0,
              "gpu_energy_j": 27.317937489486738,
              "semantic_passes": 0,
              "tokens_per_s": 93.11721698129031,
              "ttft_s": 0.06336322
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.3052709745,
              "format_passes": 0,
              "gpu_energy_j": 77.4887459078488,
              "semantic_passes": 0,
              "tokens_per_s": 1659.9529058618166,
              "ttft_s": 0.30514197099999996
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.1493664190000001,
              "format_passes": 0,
              "gpu_energy_j": 309.9407164658584,
              "semantic_passes": 0,
              "tokens_per_s": 1783.87113051383,
              "ttft_s": 1.1490962915
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.282724828,
              "format_passes": 0,
              "gpu_energy_j": 626.9986123466552,
              "semantic_passes": 0,
              "tokens_per_s": 1795.7040386205467,
              "ttft_s": 2.2823957459999997
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2546036775,
              "format_passes": 2,
              "gpu_energy_j": 58.47694084281004,
              "semantic_passes": 2,
              "tokens_per_s": 95.52566359774742,
              "ttft_s": 0.076620211
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.351557287,
              "format_passes": 0,
              "gpu_energy_j": 87.1685431837094,
              "semantic_passes": 2,
              "tokens_per_s": 96.06602912356396,
              "ttft_s": 0.070501836
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3140121085,
              "format_passes": 0,
              "gpu_energy_j": 76.76695307236172,
              "semantic_passes": 0,
              "tokens_per_s": 96.04486511849882,
              "ttft_s": 0.074510088
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5820624395,
              "format_passes": 0,
              "gpu_energy_j": 146.7061482726691,
              "semantic_passes": 0,
              "tokens_per_s": 96.25679826816352,
              "ttft_s": 0.334870812
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5451220235,
              "format_passes": 0,
              "gpu_energy_j": 134.45615406213457,
              "semantic_passes": 0,
              "tokens_per_s": 95.86426600196154,
              "ttft_s": 0.2948650145
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
              "e2e_s": 0.482429435,
              "format_passes": 2,
              "gpu_energy_j": 120.28722068770975,
              "semantic_passes": 2,
              "tokens_per_s": 96.42443114780085,
              "ttft_s": 0.0883120755
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3672449549999999,
              "format_passes": 0,
              "gpu_energy_j": 364.7825830081346,
              "semantic_passes": 0,
              "tokens_per_s": 96.97317715810871,
              "ttft_s": 0.057658872
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2079996015,
              "format_passes": 2,
              "gpu_energy_j": 48.464700579332515,
              "semantic_passes": 2,
              "tokens_per_s": 95.10003431692286,
              "ttft_s": 0.071265048
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.195906924,
              "format_passes": 0,
              "gpu_energy_j": 46.70024993848146,
              "semantic_passes": 0,
              "tokens_per_s": 94.15616815771136,
              "ttft_s": 0.1002889815
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1568819135,
              "format_passes": 2,
              "gpu_energy_j": 33.2626008004238,
              "semantic_passes": 2,
              "tokens_per_s": 93.73164024051437,
              "ttft_s": 0.060852409499999996
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.30898147899999995,
              "format_passes": 0,
              "gpu_energy_j": 75.49790355256845,
              "semantic_passes": 0,
              "tokens_per_s": 95.83041855416872,
              "ttft_s": 0.0793320095
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.401577295,
              "format_passes": 0,
              "gpu_energy_j": 94.16897444360748,
              "semantic_passes": 2,
              "tokens_per_s": 96.18590898261107,
              "ttft_s": 0.1104054425
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.6854408945000001,
              "format_passes": 2,
              "gpu_energy_j": 462.0197589614714,
              "semantic_passes": 2,
              "tokens_per_s": 94.52668173557404,
              "ttft_s": 1.526690394
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.156309398,
              "format_passes": 0,
              "gpu_energy_j": 32.01117717615686,
              "semantic_passes": 0,
              "tokens_per_s": 93.70437453144598,
              "ttft_s": 0.0709316075
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.370689777,
              "format_passes": 0,
              "gpu_energy_j": 97.60360291530786,
              "semantic_passes": 0,
              "tokens_per_s": 1366.1757452572451,
              "ttft_s": 0.370545004
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4117264239999998,
              "format_passes": 0,
              "gpu_energy_j": 395.3774978657553,
              "semantic_passes": 0,
              "tokens_per_s": 1451.9869463853543,
              "ttft_s": 1.41148337
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.808571143,
              "format_passes": 0,
              "gpu_energy_j": 797.3600303734987,
              "semantic_passes": 0,
              "tokens_per_s": 1459.3040057323578,
              "ttft_s": 2.8082463755
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2574108815,
              "format_passes": 2,
              "gpu_energy_j": 58.03471348248787,
              "semantic_passes": 2,
              "tokens_per_s": 95.40458561212613,
              "ttft_s": 0.0791881745
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.303715574,
              "format_passes": 2,
              "gpu_energy_j": 72.21857836894003,
              "semantic_passes": 2,
              "tokens_per_s": 95.75048334628406,
              "ttft_s": 0.073955857
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3183268895,
              "format_passes": 0,
              "gpu_energy_j": 78.5445695001273,
              "semantic_passes": 0,
              "tokens_per_s": 95.91495624438971,
              "ttft_s": 0.078521224
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196344524999999,
              "format_passes": 0,
              "gpu_energy_j": 161.3362168823328,
              "semantic_passes": 0,
              "tokens_per_s": 96.17234428581128,
              "ttft_s": 0.372183677
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5784887544999999,
              "format_passes": 0,
              "gpu_energy_j": 152.99590824893315,
              "semantic_passes": 0,
              "tokens_per_s": 95.79442563098343,
              "ttft_s": 0.327710076
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
            "e2e_change_pct": 0.7522792405265877,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.8342360712690695,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08192088978244971,
            "ttft_change_pct": 4.692448649863112
          },
          "decode": {
            "e2e_change_pct": 0.03266827683847673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.032325753742036,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06716899133161203,
            "ttft_change_pct": 0.44743535660363154
          },
          "energy": {
            "e2e_change_pct": 1.6452140162773299,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.59940301281927,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.005127472515031872,
            "ttft_change_pct": 4.9251877951999035
          },
          "filtering": {
            "e2e_change_pct": 4.1367815231647675,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 16.053211650729548,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.00483513870674912,
            "ttft_change_pct": 8.428733577533087
          },
          "german": {
            "e2e_change_pct": 0.171309174770351,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.21005480190268155,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2906460069160177,
            "ttft_change_pct": 0.024365693931382992
          },
          "ha_sim": {
            "e2e_change_pct": 1.0532960162240812,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.176083883272617,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08569836028521349,
            "ttft_change_pct": 3.946657519906971
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.15596269956625886,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.912352768375313,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22392546907934463,
            "ttft_change_pct": 1.1161676319189962
          },
          "long_context": {
            "e2e_change_pct": 19.4041216431309,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 24.83488517310326,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06782270383597355,
            "ttft_change_pct": 21.852209827653745
          },
          "math": {
            "e2e_change_pct": 4.678475168743268,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 17.18006598586117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6305574513396861,
            "ttft_change_pct": 11.944449003696466
          },
          "prefill": {
            "e2e_change_pct": 21.429748637959676,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 25.958423732112102,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -17.697921402899553,
            "ttft_change_pct": 21.433640474190963
          },
          "prefill2048": {
            "e2e_change_pct": 22.82648950438839,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 27.565523618226596,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -18.604717484994502,
            "ttft_change_pct": 22.834211583564223
          },
          "prefill4096": {
            "e2e_change_pct": 23.03590465876335,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 27.170940201802864,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -18.733601175537263,
            "ttft_change_pct": 23.039415071710366
          },
          "pve_sim": {
            "e2e_change_pct": 1.1025779468562424,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7562422964479398,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12674916986826767,
            "ttft_change_pct": 3.3515484576256416
          },
          "sorting": {
            "e2e_change_pct": -13.608511263770218,
            "format_pass_change": 2,
            "gpu_energy_change_pct": -17.150642042120666,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.32846759687968907,
            "ttft_change_pct": 4.8991929798821054
          },
          "time": {
            "e2e_change_pct": 1.3740810889781407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.315601123428679,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.13525853146737488,
            "ttft_change_pct": 5.383346212126328
          },
          "tool-call": {
            "e2e_change_pct": 6.454979818363604,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.972362291505421,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08773820018089795,
            "ttft_change_pct": 11.14246559058123
          },
          "tool-final": {
            "e2e_change_pct": 6.120965501589182,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 13.788698863297121,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07285339354362597,
            "ttft_change_pct": 11.139016120883326
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 345763773248569,
          "end_ns": 345764580803212,
          "model": "qwen35",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 345811196760898,
          "end_ns": 345811801597579,
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
