<!-- chunk_id: SelfCentering_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SelfCentering.html",
 "title": "4.14.5.29. SelfCentering Material",
 "category": "material",
 "command": "SelfCentering",
 "doc_section": "src",
 "rel_path": "src/SelfCentering.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1436,
 "word_count": 135,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.29. SelfCentering Material

**uniaxialMaterial(*'SelfCentering'*, *matTag*, *k1*, *k2*, *sigAct*, *beta*, *epsSlip=0*, *epsBear=0*, *rBear=k1*)**

This command is used to construct a uniaxial self-centering (flag-shaped) material object with optional non-recoverable slip behaviour and an optional stiffness increase at high strains (bearing behaviour).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `k1` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial Stiffness |
| `k2` ([float](https://docs.python.org/3/library/functions.html#float)) | Post-Activation Stiffness (0< `k2``< ``k1`) |
| `sigAct` ([float](https://docs.python.org/3/library/functions.html#float)) | Forward Activation Stress/Force |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | Ratio of Forward to Reverse Activation Stress/Force |
| `epsSlip` ([float](https://docs.python.org/3/library/functions.html#float)) | slip Strain/Deformation (if `epsSlip` = 0, there will be no slippage) |
| `epsBear` ([float](https://docs.python.org/3/library/functions.html#float)) | Bearing Strain/Deformation (if `epsBear` = 0, there will be no bearing) |
| `rBear` ([float](https://docs.python.org/3/library/functions.html#float)) | Ratio of Bearing Stiffness to Initial Stiffness `k1` |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SelfCentering_Material)
