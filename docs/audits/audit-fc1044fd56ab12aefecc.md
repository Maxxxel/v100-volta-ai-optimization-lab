# Public audit excerpt

Original SHA256: `fc1044fd56ab12aefecc7a78c41782d9258f00dfe5651d03f6e6c4dbb6685edc`

Original file: `AUDIT.json`; 81796 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "RETAIN_AS_COMPONENT_EVIDENCE; R84_GLOBAL_FORCE_MMQ_STAYS_REJECTED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Representative synthetic Q6_K matrix products only; not a full model kernel profile",
    "CPU reference uses canonical Q6 dequantization, independent double dot products",
    "Profiler timings excluded from performance rankings",
    "Does not qualify R81 or R82 flash-attention/decode tails or broad model quality"
  ],
  "qualification": "SEEDED_NUMERICAL_AND_OPERATOR_KERNEL_PATH_CHECK_PASSED"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "arms": {
    "A": {
      "cases": [
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4298700811645695e-05,
          "passed": true,
          "relative_linf": 0.003995819384106579,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4418402647509225e-05,
          "passed": true,
          "relative_linf": 0.00411584266874656,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4255142289269322e-05,
          "passed": true,
          "relative_linf": 0.0050930880930227206,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.930663873966997e-08,
          "passed": true,
          "relative_linf": 0.0002397789341162159,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            }
          ],
          "nmse": 6.912363974495058e-08,
          "passed": true,
          "relative_linf": 0.00024779115139094484,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.801979740497339e-08,
          "passed": true,
          "relative_linf": 0.0002430464214649769,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.962856163205588e-08,
          "passed": true,
          "relative_linf": 0.0002350248923150646,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            }
          ],
          "nmse": 6.733554553893778e-08,
          "passed": true,
          "relative_linf": 0.00025658634726251334,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.560335198577598e-08,
          "passed": true,
          "relative_linf": 0.00022783894242447148,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.664818152399225e-08,
          "passed": true,
          "relative_linf": 0.00022341102717206984,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            }
          ],
          "nmse": 6.756935116395535e-08,
          "passed": true,
          "relative_linf": 0.0002622424314051212,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.760410022712498e-08,
          "passed": true,
          "relative_linf": 0.00024926617318973127,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.974390720949437e-08,
          "passed": true,
          "relative_linf": 0.0002803205300664652,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            }
          ],
          "nmse": 6.652251380270426e-08,
          "passed": true,
          "relative_linf": 0.0002998190253826946,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.928078262017369e-08,
          "passed": true,
          "relative_linf": 0.0003057448377143346,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.745265761135278e-08,
          "passed": true,
          "relative_linf": 0.00024772135468183507,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 17408
            }
          ],
          "nmse": 7.046301788851264e-08,
          "passed": true,
          "relative_linf": 0.0002558030827320553,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 6.796589956578563e-08,
          "passed": true,
          "relative_linf": 0.00024381310886281598,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            }
          ],
          "nmse": 3.036436287536998e-09,
          "passed": true,
          "relative_linf": 0.0001443686624748973,
          "shape": {
            "k": 4096,
            "m": 4096,
            "n": 128,
            "pattern": 1
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 0.0,
          "passed": true,
          "relative_linf": 0.0,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 2
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 16384
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 0.0,
          "passed": true,
          "relative_linf": 0.0,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 3
          }
        }
      ],
      "cuda_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
      "max_nmse": 1.4418402647509225e-05,
      "max_relative_linf": 0.0050930880930227206,
      "max_temperature_c": 40,
      "passed": 21,
      "planned": 21
    },
    "B": {
      "cases": [
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4298700811645695e-05,
          "passed": true,
          "relative_linf": 0.003995819384106579,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4418402647509225e-05,
          "passed": true,
          "relative_linf": 0.00411584266874656,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4255142289269322e-05,
          "passed": true,
          "relative_linf": 0.0050930880930227206,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 63,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4080233702161434e-05,
          "passed": true,
          "relative_linf": 0.0035095250706456663,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4183911809499564e-05,
          "passed": true,
          "relative_linf": 0.003278735951974431,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 45392
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4495718887594699e-05,
          "passed": true,
          "relative_linf": 0.0032583256964863715,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 64,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.45060955109844e-05,
          "passed": true,
          "relative_linf": 0.00337486383851874,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 48528
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4083873908752256e-05,
          "passed": true,
          "relative_linf": 0.0035586663631826834,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.398997548378061e-05,
          "passed": true,
          "relative_linf": 0.004053447278551565,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 65,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4074311434620606e-05,
          "passed": true,
          "relative_linf": 0.0035407335006890053,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.3601009972962135e-05,
          "passed": true,
          "relative_linf": 0.003650180001505693,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4129428077748662e-05,
          "passed": true,
          "relative_linf": 0.003928557773125329,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 127,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4121473799349625e-05,
          "passed": true,
          "relative_linf": 0.004157412083826877,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4126226566609774e-05,
          "passed": true,
          "relative_linf": 0.004429043129305113,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4065038474998051e-05,
          "passed": true,
          "relative_linf": 0.004122208717414962,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4305064957967717e-05,
          "passed": true,
          "relative_linf": 0.0038344404288156056,
          "shape": {
            "k": 512,
            "m": 127,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 48528
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.4097982967908071e-05,
          "passed": true,
          "relative_linf": 0.002991551278258452,
          "shape": {
            "k": 512,
            "m": 128,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 1.3882792090364551e-05,
          "passed": true,
          "relative_linf": 0.003661194942624113,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 129,
            "pattern": 0
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 5.931913935250902e-07,
          "passed": true,
          "relative_linf": 0.0020140934137610417,
          "shape": {
            "k": 4096,
            "m": 4096,
            "n": 128,
            "pattern": 1
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 0.0,
          "passed": true,
          "relative_linf": 0.0,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 2
          }
        },
        {
          "kernels": [
            {
              "dynamic_shared_bytes": 0
            },
            {
              "dynamic_shared_bytes": 54864
            },
            {
              "dynamic_shared_bytes": 0
            }
          ],
          "nmse": 0.0,
          "passed": true,
          "relative_linf": 0.0,
          "shape": {
            "k": 512,
            "m": 129,
            "n": 128,
            "pattern": 3
          }
        }
      ],
      "cuda_sha256": "d429162ccb34d0dbbb2c11bef3f05f413d1aadd05a521ec006f348325c63f6cd",
      "max_nmse": 1.45060955109844e-05,
      "max_relative_linf": 0.0050930880930227206,
      "max_temperature_c": 40,
      "passed": 21,
      "planned": 21
    }
  }
}
```

</details>
