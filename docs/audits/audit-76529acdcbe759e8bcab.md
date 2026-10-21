# Public audit excerpt

Original SHA256: `76529acdcbe759e8bcaba8f4114a794430ecfd88da9a82e34f5df0ffbb2e51fb`

Original file: `RESULTS.json`; 44401 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.566487321,
              "format_passes": 2,
              "gpu_energy_j": 147.90949655882798,
              "semantic_passes": 2,
              "tokens_per_s": 79.22059990139934,
              "ttft_s": 0.086764704
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6580663919999998,
              "format_passes": 0,
              "gpu_energy_j": 459.1308128800839,
              "semantic_passes": 0,
              "tokens_per_s": 79.63900833161358,
              "ttft_s": 0.063018608
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2378591365,
              "format_passes": 2,
              "gpu_energy_j": 57.72414830207724,
              "semantic_passes": 2,
              "tokens_per_s": 78.22137599386862,
              "ttft_s": 0.071642168
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20939124050000002,
              "format_passes": 0,
              "gpu_energy_j": 50.15066327186837,
              "semantic_passes": 0,
              "tokens_per_s": 77.46705138450038,
              "ttft_s": 0.0932240715
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.181950491,
              "format_passes": 2,
              "gpu_energy_j": 40.164749912639486,
              "semantic_passes": 2,
              "tokens_per_s": 77.56250470592222,
              "ttft_s": 0.065874761
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35821794799999995,
              "format_passes": 0,
              "gpu_energy_j": 87.61927519826845,
              "semantic_passes": 0,
              "tokens_per_s": 78.75656068518956,
              "ttft_s": 0.0788586505
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4690248695,
              "format_passes": 0,
              "gpu_energy_j": 117.76161517150935,
              "semantic_passes": 2,
              "tokens_per_s": 78.97364315116513,
              "ttft_s": 0.11445495950000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.469989003,
              "format_passes": 2,
              "gpu_energy_j": 413.600280213626,
              "semantic_passes": 2,
              "tokens_per_s": 77.96322374977845,
              "ttft_s": 1.213422408
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233863398,
              "format_passes": 0,
              "gpu_energy_j": 55.52812897615543,
              "semantic_passes": 0,
              "tokens_per_s": 78.23858147908823,
              "ttft_s": 0.067629567
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.299568925,
              "format_passes": 0,
              "gpu_energy_j": 79.725865518586,
              "semantic_passes": 0,
              "tokens_per_s": 1691.9315546125847,
              "ttft_s": 0.299386396
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.116793615,
              "format_passes": 0,
              "gpu_energy_j": 313.7034124234033,
              "semantic_passes": 0,
              "tokens_per_s": 1835.8207802326926,
              "ttft_s": 1.1165643875
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.2129933025,
              "format_passes": 0,
              "gpu_energy_j": 631.8440673445643,
              "semantic_passes": 0,
              "tokens_per_s": 1852.3342089389794,
              "ttft_s": 2.2126236075
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295145577,
              "format_passes": 2,
              "gpu_energy_j": 70.66915878434338,
              "semantic_passes": 2,
              "tokens_per_s": 78.63726427539342,
              "ttft_s": 0.078899521
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353538883,
              "format_passes": 2,
              "gpu_energy_j": 85.3914648179115,
              "semantic_passes": 2,
              "tokens_per_s": 78.62507610905121,
              "ttft_s": 0.0736931355
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3692563925,
              "format_passes": 2,
              "gpu_energy_j": 93.78966881686196,
              "semantic_passes": 2,
              "tokens_per_s": 78.88903069904464,
              "ttft_s": 0.07766834950000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6578142035,
              "format_passes": 0,
              "gpu_energy_j": 173.99154529279608,
              "semantic_passes": 0,
              "tokens_per_s": 79.10928112225423,
              "ttft_s": 0.356839221
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.593445351,
              "format_passes": 0,
              "gpu_energy_j": 154.6963981161213,
              "semantic_passes": 0,
              "tokens_per_s": 78.81605371342332,
              "ttft_s": 0.288720858
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
              "e2e_s": 0.571808196,
              "format_passes": 2,
              "gpu_energy_j": 150.59569220436373,
              "semantic_passes": 2,
              "tokens_per_s": 79.27038172906302,
              "ttft_s": 0.0923639295
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.65721081,
              "format_passes": 0,
              "gpu_energy_j": 460.51087412085235,
              "semantic_passes": 0,
              "tokens_per_s": 79.6433316896919,
              "ttft_s": 0.0627955215
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23799521699999998,
              "format_passes": 2,
              "gpu_energy_j": 56.81780243970299,
              "semantic_passes": 2,
              "tokens_per_s": 78.22116697960912,
              "ttft_s": 0.0717630195
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2163390265,
              "format_passes": 0,
              "gpu_energy_j": 51.28663048351204,
              "semantic_passes": 0,
              "tokens_per_s": 77.58520865720484,
              "ttft_s": 0.10028086
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1825916185,
              "format_passes": 2,
              "gpu_energy_j": 42.44949192418745,
              "semantic_passes": 2,
              "tokens_per_s": 77.51102098613447,
              "ttft_s": 0.06649045149999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36327219899999996,
              "format_passes": 0,
              "gpu_energy_j": 92.46248101047871,
              "semantic_passes": 0,
              "tokens_per_s": 78.08529076856415,
              "ttft_s": 0.08152952150000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468240522,
              "format_passes": 0,
              "gpu_energy_j": 117.18452039991038,
              "semantic_passes": 2,
              "tokens_per_s": 78.97522700048162,
              "ttft_s": 0.11370136550000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.654250915,
              "format_passes": 2,
              "gpu_energy_j": 457.2175795055244,
              "semantic_passes": 2,
              "tokens_per_s": 77.93935075869598,
              "ttft_s": 1.397632714
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233236644,
              "format_passes": 0,
              "gpu_energy_j": 57.484100325709925,
              "semantic_passes": 0,
              "tokens_per_s": 78.294203266873,
              "ttft_s": 0.0671294425
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.3392078515,
              "format_passes": 0,
              "gpu_energy_j": 91.13298151160939,
              "semantic_passes": 0,
              "tokens_per_s": 1493.449638665843,
              "ttft_s": 0.3390710835
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.2760122045000002,
              "format_passes": 0,
              "gpu_energy_j": 361.53470523142835,
              "semantic_passes": 0,
              "tokens_per_s": 1606.577730079675,
              "ttft_s": 1.2757581340000002
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.535740165,
              "format_passes": 0,
              "gpu_energy_j": 725.0793456876123,
              "semantic_passes": 0,
              "tokens_per_s": 1616.3966714625283,
              "ttft_s": 2.535393621
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2950772955,
              "format_passes": 2,
              "gpu_energy_j": 74.16306132170682,
              "semantic_passes": 2,
              "tokens_per_s": 78.69085722868266,
              "ttft_s": 0.078996058
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3523284135,
              "format_passes": 2,
              "gpu_energy_j": 84.65612177812937,
              "semantic_passes": 2,
              "tokens_per_s": 78.91500648535957,
              "ttft_s": 0.073474749
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3693492955,
              "format_passes": 2,
              "gpu_energy_j": 95.94102180336503,
              "semantic_passes": 2,
              "tokens_per_s": 78.8233095218655,
              "ttft_s": 0.077488528
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.676909575,
              "format_passes": 0,
              "gpu_energy_j": 184.45960829562466,
              "semantic_passes": 0,
              "tokens_per_s": 79.0897568656683,
              "ttft_s": 0.375962261
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6126435475,
              "format_passes": 0,
              "gpu_energy_j": 166.67833393054067,
              "semantic_passes": 0,
              "tokens_per_s": 78.9079213729651,
              "ttft_s": 0.30828955150000004
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.9392752145992,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8161076252919184,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06283949847090131,
            "ttft_change_pct": 6.453344784072557
          },
          "decode": {
            "e2e_change_pct": -0.05160119064760993,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3005812727121082,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.005428694014275592,
            "ttft_change_pct": -0.3540009960232626
          },
          "energy": {
            "e2e_change_pct": 0.05721054150045202,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5701329322889923,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.00026720862019713465,
            "ttft_change_pct": 0.16868766450506278
          },
          "filtering": {
            "e2e_change_pct": 3.318088179529166,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2651090484796965,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1525258423971776,
            "ttft_change_pct": 7.569706392838671
          },
          "german": {
            "e2e_change_pct": 0.35236370975222364,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.68842583737581,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06637707225024547,
            "ttft_change_pct": 0.9346379260487758
          },
          "ha_sim": {
            "e2e_change_pct": 1.4109429826782538,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.5275574937716065,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.8523352350398361,
            "ttft_change_pct": 3.386909341036737
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.16722940530555785,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4900533766953541,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.002005541663385735,
            "ttft_change_pct": -0.6584196991481162
          },
          "long_context": {
            "e2e_change_pct": 12.53491771870079,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.545761542852429,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.030620836253625328,
            "ttft_change_pct": 15.18105358740005
          },
          "math": {
            "e2e_change_pct": -0.26800003992074606,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.52248740524721,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0710925309907795,
            "ttft_change_pct": -0.7395056957854029
          },
          "prefill": {
            "e2e_change_pct": 13.23198876518985,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.307923681761858,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -11.731084239527046,
            "ttft_change_pct": 13.255340934061666
          },
          "prefill2048": {
            "e2e_change_pct": 14.256760368387344,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 15.247297579111919,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -12.487223841314233,
            "ttft_change_pct": 14.25746229077185
          },
          "prefill4096": {
            "e2e_change_pct": 14.58417710236155,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.756058205133682,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -12.737309300765798,
            "ttft_change_pct": 14.58766020600728
          },
          "pve_sim": {
            "e2e_change_pct": -0.023134854567030683,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.944027348656532,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06815210801529581,
            "ttft_change_pct": 0.12235435497762737
          },
          "sorting": {
            "e2e_change_pct": -0.3423865261236392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8611434893992853,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.36875051911713363,
            "ttft_change_pct": -0.2963457837942052
          },
          "time": {
            "e2e_change_pct": 0.0251594831902624,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.293805931550841,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0833083846978222,
            "ttft_change_pct": -0.2315248117896629
          },
          "tool-call": {
            "e2e_change_pct": 2.9028518080637777,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.016420502049535,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02468010871663484,
            "ttft_change_pct": 5.3590073272803185
          },
          "tool-final": {
            "e2e_change_pct": 3.23504033988129,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.745452357219884,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11655957792029437,
            "ttft_change_pct": 6.77772074922276
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 340278398577836,
          "end_ns": 340279159097064,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 340328031734831,
          "end_ns": 340328588775828,
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
