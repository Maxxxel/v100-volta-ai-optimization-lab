# Public audit excerpt

Original SHA256: `f681d1b3ad53e12ab335f64878149859195b49d859e6faa4da05c540061439a3`

Original file: `RESULTS.json`; 48245 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.668974137,
              "format_passes": 2,
              "gpu_energy_j": 179.60429521966103,
              "semantic_passes": 2,
              "tokens_per_s": 78.95655200555893,
              "ttft_s": 0.1243352445
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.661780761,
              "format_passes": 0,
              "gpu_energy_j": 463.7622649370395,
              "semantic_passes": 0,
              "tokens_per_s": 79.4741006760516,
              "ttft_s": 0.06360531999999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23831580200000002,
              "format_passes": 2,
              "gpu_energy_j": 60.173154351198185,
              "semantic_passes": 2,
              "tokens_per_s": 78.26783453576087,
              "ttft_s": 0.07220067150000001
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241895524,
              "format_passes": 0,
              "gpu_energy_j": 61.20894642719554,
              "semantic_passes": 0,
              "tokens_per_s": 77.38543477165162,
              "ttft_s": 0.125564083
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1829184285,
              "format_passes": 2,
              "gpu_energy_j": 41.98998188220835,
              "semantic_passes": 2,
              "tokens_per_s": 77.32191311553919,
              "ttft_s": 0.066507562
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358376512,
              "format_passes": 0,
              "gpu_energy_j": 88.79464328527688,
              "semantic_passes": 0,
              "tokens_per_s": 78.75674843257951,
              "ttft_s": 0.078976061
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.476714381,
              "format_passes": 0,
              "gpu_energy_j": 116.10623984778533,
              "semantic_passes": 2,
              "tokens_per_s": 77.6928417999536,
              "ttft_s": 0.11624870400000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0862158105000002,
              "format_passes": 2,
              "gpu_energy_j": 291.7975233379133,
              "semantic_passes": 2,
              "tokens_per_s": 77.62241094178833,
              "ttft_s": 0.8285187869999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234203789,
              "format_passes": 0,
              "gpu_energy_j": 57.97216094417807,
              "semantic_passes": 0,
              "tokens_per_s": 77.98015862852516,
              "ttft_s": 0.0674504545
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1998563975,
              "format_passes": 0,
              "gpu_energy_j": 48.86923776816818,
              "semantic_passes": 0,
              "tokens_per_s": 2545.005670105453,
              "ttft_s": 0.1996028895
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7217902245000001,
              "format_passes": 0,
              "gpu_energy_j": 189.7490598261686,
              "semantic_passes": 0,
              "tokens_per_s": 2842.8005262780416,
              "ttft_s": 0.7215124865
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4268792824999998,
              "format_passes": 0,
              "gpu_energy_j": 382.56533304231505,
              "semantic_passes": 0,
              "tokens_per_s": 2874.3396309683876,
              "ttft_s": 1.4265137110000001
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2961607385,
              "format_passes": 2,
              "gpu_energy_j": 75.12518900137385,
              "semantic_passes": 2,
              "tokens_per_s": 78.37598559393305,
              "ttft_s": 0.079250984
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3577819865,
              "format_passes": 2,
              "gpu_energy_j": 91.14192039245134,
              "semantic_passes": 2,
              "tokens_per_s": 77.99024382690553,
              "ttft_s": 0.075659525
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5302145355,
              "format_passes": 0,
              "gpu_energy_j": 1003.6321618616582,
              "semantic_passes": 0,
              "tokens_per_s": 79.32655179844737
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5937959905000003,
              "format_passes": 0,
              "gpu_energy_j": 1018.1701153766332,
              "semantic_passes": 0,
              "tokens_per_s": 79.28437807828368
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.412336819,
              "format_passes": 0,
              "gpu_energy_j": 968.4033633514402,
              "semantic_passes": 0,
              "tokens_per_s": 79.41258444028348
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3707606415,
              "format_passes": 2,
              "gpu_energy_j": 94.93208490262047,
              "semantic_passes": 2,
              "tokens_per_s": 78.57515819847848,
              "ttft_s": 0.0779659295
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6210990489999999,
              "format_passes": 0,
              "gpu_energy_j": 160.85416342044368,
              "semantic_passes": 0,
              "tokens_per_s": 78.80775839181305,
              "ttft_s": 0.319349649
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5637695925,
              "format_passes": 0,
              "gpu_energy_j": 147.12241430009558,
              "semantic_passes": 0,
              "tokens_per_s": 78.54823228942688,
              "ttft_s": 0.258175103
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
              "e2e_s": 0.6733853245,
              "format_passes": 2,
              "gpu_energy_j": 182.54534974194544,
              "semantic_passes": 2,
              "tokens_per_s": 78.281873626968,
              "ttft_s": 0.124078203
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6763234765,
              "format_passes": 0,
              "gpu_energy_j": 467.17627552338723,
              "semantic_passes": 0,
              "tokens_per_s": 78.77290705825675,
              "ttft_s": 0.06389929750000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2411596445,
              "format_passes": 2,
              "gpu_energy_j": 60.44716680988482,
              "semantic_passes": 2,
              "tokens_per_s": 77.24181523460584,
              "ttft_s": 0.0728392885
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2431443315,
              "format_passes": 0,
              "gpu_energy_j": 58.98689062348784,
              "semantic_passes": 0,
              "tokens_per_s": 76.69921009168297,
              "ttft_s": 0.1258131065
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1843280675,
              "format_passes": 2,
              "gpu_energy_j": 41.02400720548635,
              "semantic_passes": 2,
              "tokens_per_s": 76.57367307397371,
              "ttft_s": 0.0667630555
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3607054705,
              "format_passes": 0,
              "gpu_energy_j": 94.05278958767065,
              "semantic_passes": 0,
              "tokens_per_s": 78.13041563235939,
              "ttft_s": 0.07913706749999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.473164386,
              "format_passes": 0,
              "gpu_energy_j": 117.24493995209434,
              "semantic_passes": 2,
              "tokens_per_s": 78.41525923420727,
              "ttft_s": 0.11600355000000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0887256325,
              "format_passes": 2,
              "gpu_energy_j": 293.24285171936197,
              "semantic_passes": 2,
              "tokens_per_s": 77.06253537232269,
              "ttft_s": 0.8291982920000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23642686400000001,
              "format_passes": 0,
              "gpu_energy_j": 57.67125693314547,
              "semantic_passes": 0,
              "tokens_per_s": 77.04110454628892,
              "ttft_s": 0.0676815915
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2008969145,
              "format_passes": 0,
              "gpu_energy_j": 48.43365715908132,
              "semantic_passes": 0,
              "tokens_per_s": 2530.8044696782463,
              "ttft_s": 0.2007386085
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7231629175000001,
              "format_passes": 0,
              "gpu_energy_j": 193.20075607934177,
              "semantic_passes": 0,
              "tokens_per_s": 2837.4219368005356,
              "ttft_s": 0.722877191
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4268586365,
              "format_passes": 0,
              "gpu_energy_j": 389.24004958817164,
              "semantic_passes": 0,
              "tokens_per_s": 2874.5443288557544,
              "ttft_s": 1.4264962625000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29960371100000005,
              "format_passes": 2,
              "gpu_energy_j": 73.64623080760234,
              "semantic_passes": 2,
              "tokens_per_s": 77.41730574354288,
              "ttft_s": 0.0800213385
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3619837855,
              "format_passes": 2,
              "gpu_energy_j": 92.07076393411302,
              "semantic_passes": 2,
              "tokens_per_s": 76.74005159082597,
              "ttft_s": 0.0751217745
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6521596005,
              "format_passes": 0,
              "gpu_energy_j": 425.0853620372041,
              "semantic_passes": 0,
              "tokens_per_s": 191.01917729503015
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.8995538305,
              "format_passes": 0,
              "gpu_energy_j": 195.94440964735256,
              "semantic_passes": 0,
              "tokens_per_s": 489.5559064149022
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3594672884999999,
              "format_passes": 0,
              "gpu_energy_j": 342.1314298818668,
              "semantic_passes": 0,
              "tokens_per_s": 220.09779732772677
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37841931900000003,
              "format_passes": 2,
              "gpu_energy_j": 98.29398256996187,
              "semantic_passes": 2,
              "tokens_per_s": 76.65346501082155,
              "ttft_s": 0.07836237900000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6255903574999999,
              "format_passes": 0,
              "gpu_energy_j": 168.10571334921778,
              "semantic_passes": 0,
              "tokens_per_s": 78.19090053846418,
              "ttft_s": 0.32186705000000004
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5667070830000001,
              "format_passes": 0,
              "gpu_energy_j": 150.3443311752368,
              "semantic_passes": 0,
              "tokens_per_s": 77.96093418263236,
              "ttft_s": 0.25845567199999997
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
            "e2e_change_pct": 0.6593958205592054,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6375190352142965,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8544932136137828,
            "ttft_change_pct": -0.20673261313287616
          },
          "decode": {
            "e2e_change_pct": 0.8751284069054233,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7361553201856941,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8822919817023545,
            "ttft_change_pct": 0.46219011239942986
          },
          "energy": {
            "e2e_change_pct": 1.1933084068004751,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4553732667683885,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.310907995910171,
            "ttft_change_pct": 0.8845028539658406
          },
          "filtering": {
            "e2e_change_pct": 0.5162590358637642,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.6302794499995295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8867620657473263,
            "ttft_change_pct": 0.1983238311866531
          },
          "german": {
            "e2e_change_pct": 0.7706380442690008,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.3004884341979004,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9676946824212829,
            "ttft_change_pct": 0.3841570677331374
          },
          "ha_sim": {
            "e2e_change_pct": 0.6498635993198221,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.92169314257005,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7952750877676329,
            "ttft_change_pct": 0.20386747320810805
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.7446796533708944,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9807397998607525,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.9298378299944066,
            "ttft_change_pct": -0.2108875123459364
          },
          "long_context": {
            "e2e_change_pct": 0.23106108157684435,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4953189337988162,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.721280829431481,
            "ttft_change_pct": 0.08201443475537307
          },
          "math": {
            "e2e_change_pct": 0.9492053947940171,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5190491541661624,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2042218158462847,
            "ttft_change_pct": 0.3426767124304453
          },
          "prefill": {
            "e2e_change_pct": 0.5206323205140251,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8913186065091172,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5580027028630696,
            "ttft_change_pct": 0.5689892580437839
          },
          "prefill2048": {
            "e2e_change_pct": 0.19017894028017235,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8190847724543602,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1892003827840827,
            "ttft_change_pct": 0.1891449594476402
          },
          "prefill4096": {
            "e2e_change_pct": -0.0014469338964429035,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7447259250535252,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.007121562294210015,
            "ttft_change_pct": -0.0012231568379150737
          },
          "pve_sim": {
            "e2e_change_pct": 1.162535087344141,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.9686582003067832,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.2231805994212364,
            "ttft_change_pct": 0.9720440821277432
          },
          "sorting": {
            "e2e_change_pct": 1.1744020544757205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0191178084268282,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.6030110623250216,
            "ttft_change_pct": -0.710750563131346
          },
          "spec-branch": {
            "e2e_change_pct": -53.199456183588644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -57.64530291170578,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 140.80105962549715
          },
          "spec-code": {
            "e2e_change_pct": -74.96925721777417,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -80.75523857082857,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 517.4683062173046
          },
          "spec-repeat": {
            "e2e_change_pct": -60.160225657372315,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -64.67056571366895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 177.15732824844088
          },
          "time": {
            "e2e_change_pct": 2.0656662662506653,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.541371361210466,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.445675238480316,
            "ttft_change_pct": 0.5084906991329019
          },
          "tool-call": {
            "e2e_change_pct": 0.7231227462401124,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.5081518405090115,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7827374689202693,
            "ttft_change_pct": 0.7882898909965741
          },
          "tool-final": {
            "e2e_change_pct": 0.521044508089541,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1899565001490817,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7476910551347582,
            "ttft_change_pct": 0.10867391810431837
          }
        }
      },
      "complete": true,
      "speculation": {
        "arms": {
          "A": {
            "accepted_n": 0,
            "checkpoint_events": 0,
            "draft_n": 0,
            "median_e2e_s": 3.566359641,
            "restore_events": 0,
            "starts": 2
          },
          "B": {
            "acceptance_pct": 96.84376643871647,
            "accepted_n": 3682,
            "checkpoint_events": 96,
            "draft_n": 3802,
            "median_e2e_s": 1.5183964680000002,
            "restore_events": 10,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Token drift is reported separately from semantic quality and protocol validity. No draft is inactivity, not an optimization gain. Internal RAM checkpoint trace is not a new model checkpoint."
      }
    }
  }
}
```

</details>
