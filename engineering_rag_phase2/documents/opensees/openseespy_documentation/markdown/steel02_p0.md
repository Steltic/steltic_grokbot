<!-- chunk_id: steel02_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/steel02.html",
 "title": "4.14.1.2. Steel02",
 "category": "general",
 "command": "steel02",
 "doc_section": "src",
 "rel_path": "src/steel02.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2237,
 "word_count": 210,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.2. Steel02

**uniaxialMaterial(*'Steel02'*, *matTag*, *Fy*, *E0*, *b*, **params*, *a1=a2*Fy/E0*, *a2=1.0*, *a3=a4*Fy/E0*, *a4=1.0*, *sigInit=0.0*)**

This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield strength |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic tangent |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent) |
| `params` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | parameters to control the transition from elastic to plastic branches. `params=[R0,cR1,cR2]`. Recommended values: R0=between 10 and 20, cR1=0.925, cR2=0.15 |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of \(a_2*(F_y/E_0)\) (optional) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a1`). (optional). |
| `a3` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of \(a_4*(F_y/E_0)\). (optional) |
| `a4` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under `a3`). (optional) |
| `sigInit` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial Stress Value (optional, default: 0.0) the strain is calculated from `epsP=sigInit/E` if (sigInit!= 0.0) { double epsInit = sigInit/E; eps = trialStrain+epsInit; } else { eps = trialStrain; } |

See also

[Steel02](http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening)
