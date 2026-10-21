# Public audit excerpt

Original SHA256: `e418ee6a18e6c213eed122461c5ed075e9180ff684a513ac4c2aabc5d5dd6739`

Original file: `RESULTS.json`; 39732 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6679870615000001,
              "format_passes": 2,
              "gpu_energy_j": 174.8444253427815,
              "semantic_passes": 2,
              "tokens_per_s": 79.20570937372887,
              "ttft_s": 0.12506251000000002
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.661664015,
              "format_passes": 0,
              "gpu_energy_j": 462.91684935123,
              "semantic_passes": 0,
              "tokens_per_s": 79.57336149045287,
              "ttft_s": 0.065384135
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238254735,
              "format_passes": 2,
              "gpu_energy_j": 59.3786113659202,
              "semantic_passes": 2,
              "tokens_per_s": 78.22489887824437,
              "ttft_s": 0.0720583125
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2424839445,
              "format_passes": 0,
              "gpu_energy_j": 59.46667066138982,
              "semantic_passes": 0,
              "tokens_per_s": 77.19494625260035,
              "ttft_s": 0.1258823315
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18323052299999998,
              "format_passes": 2,
              "gpu_energy_j": 41.17476891171707,
              "semantic_passes": 2,
              "tokens_per_s": 77.45639784614804,
              "ttft_s": 0.0669747695
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3590199335,
              "format_passes": 0,
              "gpu_energy_j": 87.39131053744899,
              "semantic_passes": 0,
              "tokens_per_s": 78.81194625358822,
              "ttft_s": 0.0798082455
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46997042899999997,
              "format_passes": 0,
              "gpu_energy_j": 115.66051704021433,
              "semantic_passes": 2,
              "tokens_per_s": 78.74541705287467,
              "ttft_s": 0.1143539435
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.8708442625,
              "format_passes": 2,
              "gpu_energy_j": 509.97060759397914,
              "semantic_passes": 2,
              "tokens_per_s": 78.07195377365267,
              "ttft_s": 1.6146508505
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23401203399999998,
              "format_passes": 0,
              "gpu_energy_j": 57.647362183478336,
              "semantic_passes": 0,
              "tokens_per_s": 78.26139736684715,
              "ttft_s": 0.0678435325
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.3952852925,
              "format_passes": 0,
              "gpu_energy_j": 101.06267954661801,
              "semantic_passes": 0,
              "tokens_per_s": 1280.8952945559022,
              "ttft_s": 0.395151556
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4841707895,
              "format_passes": 0,
              "gpu_energy_j": 408.3588073565462,
              "semantic_passes": 0,
              "tokens_per_s": 1381.0762234019955,
              "ttft_s": 1.483888788
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.958191759,
              "format_passes": 0,
              "gpu_energy_j": 822.9781843011403,
              "semantic_passes": 0,
              "tokens_per_s": 1385.4635185323568,
              "ttft_s": 2.9578151145
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295810708,
              "format_passes": 2,
              "gpu_energy_j": 75.15617984545275,
              "semantic_passes": 2,
              "tokens_per_s": 78.60799119590499,
              "ttft_s": 0.0794791945
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354432128,
              "format_passes": 2,
              "gpu_energy_j": 90.61169039425465,
              "semantic_passes": 2,
              "tokens_per_s": 78.64731357028381,
              "ttft_s": 0.07466447600000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36946529149999996,
              "format_passes": 2,
              "gpu_energy_j": 94.84247310624951,
              "semantic_passes": 2,
              "tokens_per_s": 78.8819343231434,
              "ttft_s": 0.077847471
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.735431971,
              "format_passes": 0,
              "gpu_energy_j": 197.4043785254749,
              "semantic_passes": 0,
              "tokens_per_s": 79.05204628572798,
              "ttft_s": 0.4340758215
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6728680490000001,
              "format_passes": 0,
              "gpu_energy_j": 177.9257846965014,
              "semantic_passes": 0,
              "tokens_per_s": 78.81385194577521,
              "ttft_s": 0.3683701585
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
              "e2e_s": 0.669825962,
              "format_passes": 2,
              "gpu_energy_j": 175.39039861384148,
              "semantic_passes": 2,
              "tokens_per_s": 78.9467028056146,
              "ttft_s": 0.12511749249999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6604700085,
              "format_passes": 0,
              "gpu_energy_j": 463.44140961461426,
              "semantic_passes": 0,
              "tokens_per_s": 79.6246731307871,
              "ttft_s": 0.06552991650000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2380180865,
              "format_passes": 2,
              "gpu_energy_j": 59.444667156538124,
              "semantic_passes": 2,
              "tokens_per_s": 78.26521717870526,
              "ttft_s": 0.071879575
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.242707976,
              "format_passes": 0,
              "gpu_energy_j": 63.1617087726394,
              "semantic_passes": 0,
              "tokens_per_s": 77.36868875604956,
              "ttft_s": 0.12641225350000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1833165085,
              "format_passes": 2,
              "gpu_energy_j": 40.67561389005633,
              "semantic_passes": 2,
              "tokens_per_s": 77.5073959477769,
              "ttft_s": 0.0671746765
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357870608,
              "format_passes": 0,
              "gpu_energy_j": 89.57702056562485,
              "semantic_passes": 0,
              "tokens_per_s": 78.9137362946664,
              "ttft_s": 0.07904634099999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468475,
              "format_passes": 0,
              "gpu_energy_j": 118.54605011498012,
              "semantic_passes": 2,
              "tokens_per_s": 79.11705792830938,
              "ttft_s": 0.1145122445
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.8739442629999998,
              "format_passes": 2,
              "gpu_energy_j": 511.9703413029973,
              "semantic_passes": 2,
              "tokens_per_s": 78.28902323758496,
              "ttft_s": 1.618396511
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23410814600000002,
              "format_passes": 0,
              "gpu_energy_j": 57.622066668775574,
              "semantic_passes": 0,
              "tokens_per_s": 78.16328228248972,
              "ttft_s": 0.06769331149999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.395018994,
              "format_passes": 0,
              "gpu_energy_j": 102.51663376314427,
              "semantic_passes": 0,
              "tokens_per_s": 1281.8533219863752,
              "ttft_s": 0.3948396795
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.483720455,
              "format_passes": 0,
              "gpu_energy_j": 406.30203354856496,
              "semantic_passes": 0,
              "tokens_per_s": 1381.450723793428,
              "ttft_s": 1.4834758935
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.9561205380000004,
              "format_passes": 0,
              "gpu_energy_j": 821.1336220604619,
              "semantic_passes": 0,
              "tokens_per_s": 1386.3992123565324,
              "ttft_s": 2.9557671255
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295453704,
              "format_passes": 2,
              "gpu_energy_j": 75.1802443103006,
              "semantic_passes": 2,
              "tokens_per_s": 78.61546166957086,
              "ttft_s": 0.079156955
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3535101985,
              "format_passes": 2,
              "gpu_energy_j": 89.3840189880348,
              "semantic_passes": 2,
              "tokens_per_s": 78.88533967383565,
              "ttft_s": 0.07458306649999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36910527800000004,
              "format_passes": 2,
              "gpu_energy_j": 92.43668456326341,
              "semantic_passes": 2,
              "tokens_per_s": 78.97525690203886,
              "ttft_s": 0.077820365
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7365093220000001,
              "format_passes": 0,
              "gpu_energy_j": 190.13283814613402,
              "semantic_passes": 0,
              "tokens_per_s": 79.1924437349064,
              "ttft_s": 0.435253051
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6735971335,
              "format_passes": 0,
              "gpu_energy_j": 178.2302941673465,
              "semantic_passes": 0,
              "tokens_per_s": 78.78074398161843,
              "ttft_s": 0.36912134799999996
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
            "e2e_change_pct": 0.2752898380801838,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31226232691696776,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3270049219459059,
            "ttft_change_pct": 0.04396401447561704
          },
          "decode": {
            "e2e_change_pct": -0.07185607254063253,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1133163038069318,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06448343939873258,
            "ttft_change_pct": 0.2229615792883166
          },
          "energy": {
            "e2e_change_pct": -0.09932583291576425,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11124509162205864,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05154151815989216,
            "ttft_change_pct": -0.24804563665017376
          },
          "filtering": {
            "e2e_change_pct": 0.09239024070726298,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.213628693439999,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22506979003611427,
            "ttft_change_pct": 0.42096614646831565
          },
          "german": {
            "e2e_change_pct": 0.04692749799115603,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2122837233913164,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0658410448290736,
            "ttft_change_pct": 0.2984810571091234
          },
          "ha_sim": {
            "e2e_change_pct": -0.3201286036670803,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.501061049129416,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12915559875994465,
            "ttft_change_pct": -0.9546689007215559
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.3181964029485784,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4948298249112266,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.47195238700070696,
            "ttft_change_pct": 0.1384307310748678
          },
          "long_context": {
            "e2e_change_pct": 0.16570061774450195,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3921272479707971,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2780376991225575,
            "ttft_change_pct": 0.23197959477370134
          },
          "math": {
            "e2e_change_pct": 0.04107139208064936,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04387974357309421,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12536842895549682,
            "ttft_change_pct": -0.22142272736167534
          },
          "prefill": {
            "e2e_change_pct": -0.06736868410047725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4386658092274018,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07479357872144377,
            "ttft_change_pct": -0.07892579322148485
          },
          "prefill2048": {
            "e2e_change_pct": -0.030342498530888662,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5036682865481645,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.027116562075768513,
            "ttft_change_pct": -0.027825164752171005
          },
          "prefill4096": {
            "e2e_change_pct": -0.0700164549406912,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22413258040914208,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0675365184040988,
            "ttft_change_pct": -0.06923992611843621
          },
          "pve_sim": {
            "e2e_change_pct": -0.12068663856481532,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.032019276255557116,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.009503453214132485,
            "ttft_change_pct": -0.405438809523917
          },
          "sorting": {
            "e2e_change_pct": -0.26011454018074476,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3548708791086606,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3026500114833741,
            "ttft_change_pct": -0.10903377933036973
          },
          "time": {
            "e2e_change_pct": -0.09744176470225518,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.536615151621957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1183066562657542,
            "ttft_change_pct": -0.034819371331917814
          },
          "tool-call": {
            "e2e_change_pct": 0.14649227154690525,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.683576034967473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17760128393256025,
            "ttft_change_pct": 0.2712036565252429
          },
          "tool-final": {
            "e2e_change_pct": 0.1083547511407934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1711440932322006,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04200779855242365,
            "ttft_change_pct": 0.20392246295379834
          }
        }
      },
      "complete": true
    }
  }
}
```
