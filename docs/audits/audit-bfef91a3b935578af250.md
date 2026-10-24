# Public audit excerpt

Original SHA256: `bfef91a3b935578af250cdfa057e7e6dd44f64ba5ecce53add6501c410c8625e`

Original file: `RESULTS.json`; 41671 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7970793215,
              "format_passes": 2,
              "gpu_energy_j": 477.6186281014036,
              "semantic_passes": 2,
              "tokens_per_s": 35.284552463243635,
              "ttft_s": 0.545470023
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7832386845,
              "format_passes": 0,
              "gpu_energy_j": 1066.966531429262,
              "semantic_passes": 0,
              "tokens_per_s": 35.41452334297574,
              "ttft_s": 0.196036946
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5956914425,
              "format_passes": 2,
              "gpu_energy_j": 149.80500726699483,
              "semantic_passes": 2,
              "tokens_per_s": 34.81397010082884,
              "ttft_s": 0.2192369515
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.960797728,
              "format_passes": 0,
              "gpu_energy_j": 244.67714504248488,
              "semantic_passes": 0,
              "tokens_per_s": 34.92404181990193,
              "ttft_s": 0.5371278884999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4865371355,
              "format_passes": 2,
              "gpu_energy_j": 109.55458260630908,
              "semantic_passes": 2,
              "tokens_per_s": 33.71626380345319,
              "ttft_s": 0.21759123
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0205184354999999,
              "format_passes": 0,
              "gpu_energy_j": 263.2343385978738,
              "semantic_passes": 0,
              "tokens_per_s": 35.06970814322759,
              "ttft_s": 0.2469690755
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1597226809999999,
              "format_passes": 0,
              "gpu_energy_j": 301.2027279579203,
              "semantic_passes": 2,
              "tokens_per_s": 35.297380477298304,
              "ttft_s": 0.3617689035
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8124069945,
              "format_passes": 2,
              "gpu_energy_j": 1015.6730340279601,
              "semantic_passes": 2,
              "tokens_per_s": 34.20744732888561,
              "ttft_s": 3.222711488
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5874932385,
              "format_passes": 2,
              "gpu_energy_j": 140.99621292718916,
              "semantic_passes": 2,
              "tokens_per_s": 34.88634078312094,
              "ttft_s": 0.212861566
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.72362256,
              "format_passes": 0,
              "gpu_energy_j": 186.63174598689181,
              "semantic_passes": 0,
              "tokens_per_s": 698.9172148991879,
              "ttft_s": 0.7234888685
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7475920985,
              "format_passes": 0,
              "gpu_energy_j": 735.2504736059064,
              "semantic_passes": 0,
              "tokens_per_s": 745.7243254207359,
              "ttft_s": 2.7473227785
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4511968500000005,
              "format_passes": 0,
              "gpu_energy_j": 1472.6661437490636,
              "semantic_passes": 0,
              "tokens_per_s": 751.6323840891177,
              "ttft_s": 5.45087939
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8769235045,
              "format_passes": 0,
              "gpu_energy_j": 227.80678574456724,
              "semantic_passes": 2,
              "tokens_per_s": 35.072784023643905,
              "ttft_s": 0.24358106
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0134086335,
              "format_passes": 0,
              "gpu_energy_j": 272.1938899743917,
              "semantic_passes": 2,
              "tokens_per_s": 35.04616278143012,
              "ttft_s": 0.22276522199999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.02925236,
              "format_passes": 0,
              "gpu_energy_j": 279.5903874170186,
              "semantic_passes": 2,
              "tokens_per_s": 35.27487953471501,
              "ttft_s": 0.23142113549999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7081971020000002,
              "format_passes": 0,
              "gpu_energy_j": 456.1903811220053,
              "semantic_passes": 0,
              "tokens_per_s": 35.00436904989799,
              "ttft_s": 1.0296687345
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.776729823,
              "format_passes": 0,
              "gpu_energy_j": 466.44830575830247,
              "semantic_passes": 0,
              "tokens_per_s": 35.11282117907497,
              "ttft_s": 1.0931474775
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
              "e2e_s": 1.760837137,
              "format_passes": 2,
              "gpu_energy_j": 481.4858171592514,
              "semantic_passes": 2,
              "tokens_per_s": 35.50328390681918,
              "ttft_s": 0.5214567285
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7748086575,
              "format_passes": 0,
              "gpu_energy_j": 1063.8384965505975,
              "semantic_passes": 0,
              "tokens_per_s": 35.47525314154801,
              "ttft_s": 0.19530469849999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.580226986,
              "format_passes": 2,
              "gpu_energy_j": 146.43385885764084,
              "semantic_passes": 2,
              "tokens_per_s": 35.02366418622556,
              "ttft_s": 0.2089728185
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9239777655,
              "format_passes": 0,
              "gpu_energy_j": 243.94932683285884,
              "semantic_passes": 0,
              "tokens_per_s": 35.03933422116968,
              "ttft_s": 0.5243526505
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46459171099999996,
              "format_passes": 2,
              "gpu_energy_j": 110.12494123371224,
              "semantic_passes": 2,
              "tokens_per_s": 34.32137829191949,
              "ttft_s": 0.2023583785
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9874498955,
              "format_passes": 0,
              "gpu_energy_j": 264.4168762928284,
              "semantic_passes": 0,
              "tokens_per_s": 35.38537418136542,
              "ttft_s": 0.224368352
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1487139265000001,
              "format_passes": 0,
              "gpu_energy_j": 292.8469960787715,
              "semantic_passes": 2,
              "tokens_per_s": 35.19591724807847,
              "ttft_s": 0.3531830935
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.0112344925,
              "format_passes": 2,
              "gpu_energy_j": 796.8721270716726,
              "semantic_passes": 2,
              "tokens_per_s": 33.824621030549835,
              "ttft_s": 2.419916938
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.572167095,
              "format_passes": 2,
              "gpu_energy_j": 144.75527291641697,
              "semantic_passes": 2,
              "tokens_per_s": 35.100131160380926,
              "ttft_s": 0.201758147
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7295379479999999,
              "format_passes": 0,
              "gpu_energy_j": 187.31825194572548,
              "semantic_passes": 0,
              "tokens_per_s": 693.2440213068103,
              "ttft_s": 0.7293981629999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.9286679764999999,
              "format_passes": 0,
              "gpu_energy_j": 514.6812967485074,
              "semantic_passes": 0,
              "tokens_per_s": 1062.5501245099463,
              "ttft_s": 1.928426574
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.8726208609999997,
              "format_passes": 0,
              "gpu_energy_j": 1033.3702296006754,
              "semantic_passes": 0,
              "tokens_per_s": 1058.2189153095735,
              "ttft_s": 3.8722219475
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8451651025,
              "format_passes": 0,
              "gpu_energy_j": 222.18753860751139,
              "semantic_passes": 2,
              "tokens_per_s": 35.27265318106476,
              "ttft_s": 0.22142700999999998
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9855354585,
              "format_passes": 0,
              "gpu_energy_j": 265.1670094074276,
              "semantic_passes": 2,
              "tokens_per_s": 35.161841078945734,
              "ttft_s": 0.21764114099999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.012533656,
              "format_passes": 0,
              "gpu_energy_j": 273.7065963380868,
              "semantic_passes": 2,
              "tokens_per_s": 35.36325434562643,
              "ttft_s": 0.22073901499999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7045236675,
              "format_passes": 0,
              "gpu_energy_j": 460.478842788708,
              "semantic_passes": 0,
              "tokens_per_s": 35.14051515775292,
              "ttft_s": 1.0285286855
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7777744505,
              "format_passes": 0,
              "gpu_energy_j": 466.6027695251073,
              "semantic_passes": 0,
              "tokens_per_s": 35.17715481104007,
              "ttft_s": 1.094540888
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
            "e2e_change_pct": -2.0167270340492927,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8096813713527773,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6199070933474271,
            "ttft_change_pct": -4.4023124071842945
          },
          "decode": {
            "e2e_change_pct": -0.2228256714158161,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2931708527421528,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17148275012519587,
            "ttft_change_pct": -0.37352525375498047
          },
          "energy": {
            "e2e_change_pct": -2.596051478446404,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.25035762879785,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6023274127868739,
            "ttft_change_pct": -4.6817532034511995
          },
          "filtering": {
            "e2e_change_pct": -3.8322283064349594,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2974606432896154,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3301233054933794,
            "ttft_change_pct": -2.3784350568123447
          },
          "german": {
            "e2e_change_pct": -4.510534324876836,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5206159467128435,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.794725809460318,
            "ttft_change_pct": -7.000673464642859
          },
          "ha_sim": {
            "e2e_change_pct": -3.2403667439675488,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.44923382764325837,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9001102514130555,
            "ttft_change_pct": -9.1512362243102
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.9492574975344281,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.7741222451066694,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.28745257536911817,
            "ttft_change_pct": -2.3732857956930586
          },
          "long_context": {
            "e2e_change_pct": -21.01487336362089,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -21.542455064359245,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.119131441335297,
            "ttft_change_pct": -24.910531178148076
          },
          "math": {
            "e2e_change_pct": -2.608735300363807,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.666071599503872,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6128197238829403,
            "ttft_change_pct": -5.216262949037964
          },
          "prefill": {
            "e2e_change_pct": 0.8174687091015986,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.36783986304338434,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8117118124205791,
            "ttft_change_pct": 0.8167775286234358
          },
          "prefill2048": {
            "e2e_change_pct": -29.805156393013277,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -29.999188681328736,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 42.48564627558018,
            "ttft_change_pct": -29.807062020834184
          },
          "prefill4096": {
            "e2e_change_pct": -28.95833763552311,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -29.829973073872907,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 40.78942548384199,
            "ttft_change_pct": -28.96151849178963
          },
          "pve_sim": {
            "e2e_change_pct": -3.6215703920614906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.4666724121890415,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5698696667082892,
            "ttft_change_pct": -9.095144753865513
          },
          "sorting": {
            "e2e_change_pct": -2.7504378864165346,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.5815717493236967,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3300740746913,
            "ttft_change_pct": -2.3002158748101187
          },
          "time": {
            "e2e_change_pct": -1.6243542059986238,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1044325354991233,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2505318574495652,
            "ttft_change_pct": -4.615879391016131
          },
          "tool-call": {
            "e2e_change_pct": -0.21504746119164198,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9400596426770713,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.38894032816549906,
            "ttft_change_pct": -0.11071997835824243
          },
          "tool-final": {
            "e2e_change_pct": 0.05879495500538123,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.033114873587924976,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1832197750132325,
            "ttft_change_pct": 0.1274677505716415
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 372807390538651,
          "end_ns": 372808095875011,
          "model": "qwen38",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 372922979686481,
          "end_ns": 372924653168159,
          "model": "qwen38",
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
