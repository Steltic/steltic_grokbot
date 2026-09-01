<!-- chunk_id: Hysteretic_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Hysteretic.html",
 "title": "4.14.3.5. Hysteretic",
 "category": "general",
 "command": "Hysteretic",
 "doc_section": "src",
 "rel_path": "src/Hysteretic.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2816,
 "word_count": 276,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.5. Hysteretic

**uniaxialMaterial(*'Hysteretic'*, *matTag*, **p1*, **p2*, **p3=p2*, **n1*, **n2*, **n3=n2*, *pinchX*, *pinchY*, *damage1*, *damage2*, *beta=0.0*)**

This command is used to construct a uniaxial bilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `p1` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `p1=[s1p, e1p]`, stress and strain (or force & deformation) at first point of the envelope in the positive direction |
| `p2` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `p2=[s2p, e2p]`, stress and strain (or force & deformation) at second point of the envelope in the positive direction |
| `p3` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `p3=[s3p, e3p]`, stress and strain (or force & deformation) at third point of the envelope in the positive direction |
| `n1` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `n1=[s1n, e1n]`, stress and strain (or force & deformation) at first point of the envelope in the negative direction |
| `n2` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `n2=[s2n, e2n]`, stress and strain (or force & deformation) at second point of the envelope in the negative direction |
| `n3` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | `n3=[s3n, e3n]`, stress and strain (or force & deformation) at third point of the envelope in the negative direction |
| `pinchX` ([float](https://docs.python.org/3/library/functions.html#float)) | pinching factor for strain (or deformation) during reloading |
| `pinchY` ([float](https://docs.python.org/3/library/functions.html#float)) | pinching factor for stress (or force) during reloading |
| `damage1` ([float](https://docs.python.org/3/library/functions.html#float)) | damage due to ductility: D1(mu-1) |
| `damage2` ([float](https://docs.python.org/3/library/functions.html#float)) | damage due to energy: D2(Eii/Eult) |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | power used to determine the degraded unloading stiffness based on ductility, mu-beta (optional, default=0.0) |

See also

[Hysteretic](http://opensees.berkeley.edu/wiki/index.php/Hysteretic_Material)
