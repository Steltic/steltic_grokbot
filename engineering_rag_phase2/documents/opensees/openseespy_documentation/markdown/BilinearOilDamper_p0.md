<!-- chunk_id: BilinearOilDamper_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BilinearOilDamper.html",
 "title": "4.14.5.5. BilinearOilDamper Material",
 "category": "material",
 "command": "BilinearOilDamper",
 "doc_section": "src",
 "rel_path": "src/BilinearOilDamper.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2211,
 "word_count": 232,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.5. BilinearOilDamper Material

**uniaxialMaterial(*'BilinearOilDamper'*, *matTag*, *K_el*, *Cd*, *Fr=1.0*, *p=1.0*, *LGap=0.0*, *NM=1*, *RelTol=1e-6*, *AbsTol=1e-10*, *MaxHalf=15*)**

This command is used to construct a BilinearOilDamper material, which simulates the hysteretic response of bilinear oil dampers with relief valve. Two adaptive iterative algorithms have been implemented and validated to solve numerically the constitutive equations within a bilinear oil damper with a high-precision accuracy.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `K_el` ([float](https://docs.python.org/3/library/functions.html#float)) | Elastic stiffness of linear spring to model the axial flexibility of a viscous damper (e.g. combined stiffness of the supporting brace and internal damper portion) |
| `Cd` ([float](https://docs.python.org/3/library/functions.html#float)) | Damping coefficient |
| `Fr` ([float](https://docs.python.org/3/library/functions.html#float)) | Damper relief load (default=1.0, Damper property) |
| `p` ([float](https://docs.python.org/3/library/functions.html#float)) | Post-relief viscous damping coefficient ratio (default=1.0, linear oil damper) |
| `LGap` ([float](https://docs.python.org/3/library/functions.html#float)) | Gap length to simulate the gap length due to the pin tolerance |
| `NM` ([int](https://docs.python.org/3/library/functions.html#int)) | Employed adaptive numerical algorithm (default value NM = 1; `1` = Dormand-Prince54, `2` = 6th order Adams-Bashforth-Moulton, `3` = modified Rosenbrock Triple) |
| `RelTol` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for absolute relative error control of the adaptive iterative algorithm (default value 10^-6) |
| `AbsTol` ([float](https://docs.python.org/3/library/functions.html#float)) | Tolerance for absolute error control of adaptive iterative algorithm (default value 10^-10) |
| `MaxHalf` ([int](https://docs.python.org/3/library/functions.html#int)) | Maximum number of sub-step iterations within an integration step (default value 15) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BilinearOilDamper_Material)
