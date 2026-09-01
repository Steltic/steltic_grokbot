<!-- chunk_id: BarSlip_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BarSlip.html",
 "title": "4.14.5.10. BarSlip Material",
 "category": "material",
 "command": "BarSlip",
 "doc_section": "src",
 "rel_path": "src/BarSlip.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3538,
 "word_count": 400,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.10. BarSlip Material

**uniaxialMaterial(*'BarSlip'*, *matTag*, *fc*, *fy*, *Es*, *fu*, *Eh*, *db*, *ld*, *nb*, *depth*, *height*, *ancLratio=1.0*, *bsFlag*, *type*, *damage='Damage'*, *unit='psi'*)**

This command is used to construct a uniaxial material that simulates the bar force versus slip response of a reinforcing bar anchored in a beam-column joint. The model exhibits degradation under cyclic loading. Cyclic degradation of strength and stiffness occurs in three ways: unloading stiffness degradation, reloading stiffness degradation, strength degradation.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | positive floating point value defining the compressive strength of the concrete in which the reinforcing bar is anchored |
| `fy` ([float](https://docs.python.org/3/library/functions.html#float)) | positive floating point value defining the yield strength of the reinforcing steel |
| `Es` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the modulus of elasticity of the reinforcing steel |
| `fu` ([float](https://docs.python.org/3/library/functions.html#float)) | positive floating point value defining the ultimate strength of the reinforcing steel |
| `Eh` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the hardening modulus of the reinforcing steel |
| `ld` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the development length of the reinforcing steel |
| `db` ([float](https://docs.python.org/3/library/functions.html#float)) | point value defining the diameter of reinforcing steel |
| `nb` ([int](https://docs.python.org/3/library/functions.html#int)) | an integer defining the number of anchored bars |
| `depth` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the dimension of the member (beam or column) perpendicular to the dimension of the plane of the paper |
| `height` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the height of the flexural member, perpendicular to direction in which the reinforcing steel is placed, but in the plane of the paper |
| `ancLratio` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the ratio of anchorage length used for the reinforcing bar to the dimension of the joint in the direction of the reinforcing bar (optional, default: 1.0) |
| `bsFlag` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string indicating relative bond strength for the anchored reinforcing bar (options: `'Strong'` or `'Weak'`) |
| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string indicating where the reinforcing bar is placed. (options: `'beamtop'`, `'beambot'` or `'column'`) |
| `damage` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string indicating type of damage:whether there is full damage in the material or no damage (optional, options: `'Damage'`, `'NoDamage'` ; default: `'Damage'`) |
| `unit` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string indicating the type of unit system used (optional, options: `'psi'`, `'MPa'`, `'Pa'`, `'psf'`, `'ksi'`, `'ksf'`) (default: `'psi'` / `'MPa'`) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BARSLIP_Material)
