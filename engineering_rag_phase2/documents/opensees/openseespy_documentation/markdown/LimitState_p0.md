<!-- chunk_id: LimitState_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/LimitState.html",
 "title": "4.14.5.16. Limit State Material",
 "category": "material",
 "command": "LimitState",
 "doc_section": "src",
 "rel_path": "src/LimitState.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2900,
 "word_count": 338,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.16. Limit State Material

**uniaxialMaterial(*'LimitState'*, *matTag*, *s1p*, *e1p*, *s2p*, *e2p*, *s3p*, *e3p*, *s1n*, *e1n*, *s2n*, *e2n*, *s3n*, *e3n*, *pinchX*, *pinchY*, *damage1*, *damage2*, *beta*, *curveTag*, *curveType*)**

This command is used to construct a uniaxial hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. Failure of the material is defined by the associated Limit Curve.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `s1p` `e1p` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at first point of the envelope in the positive direction |
| `s2p` `e2p` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at second point of the envelope in the positive direction |
| `s3p` `e3p` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at third point of the envelope in the positive direction |
| `s1n` `e1n` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at first point of the envelope in the negative direction |
| `s2n` `e2n` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at second point of the envelope in the negative direction |
| `s3n` `e3n` ([float](https://docs.python.org/3/library/functions.html#float)) | stress and strain (or force & deformation) at third point of the envelope in the negative direction |
| `pinchX` ([float](https://docs.python.org/3/library/functions.html#float)) | pinching factor for strain (or deformation) during reloading |
| `pinchY` ([float](https://docs.python.org/3/library/functions.html#float)) | pinching factor for stress (or force) during reloading |
| `damage1` ([float](https://docs.python.org/3/library/functions.html#float)) | damage due to ductility: D1(m-1) |
| `damage2` ([float](https://docs.python.org/3/library/functions.html#float)) | damage due to energy: D2(Ei/Eult) |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | power used to determine the degraded unloading stiffness based on ductility, m-b (optional, default=0.0) |
| `curveTag` ([int](https://docs.python.org/3/library/functions.html#int)) | an integer tag for the Limit Curve defining the limit surface |
| `curveType` ([int](https://docs.python.org/3/library/functions.html#int)) | an integer defining the type of LimitCurve (0 = no curve, 1 = axial curve, all other curves can be any other integer) |

Note

- negative backbone points should be entered as negative numeric values

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Limit_State_Material)
