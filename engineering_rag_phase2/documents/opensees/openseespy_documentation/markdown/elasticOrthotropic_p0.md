<!-- chunk_id: elasticOrthotropic_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticOrthotropic.html",
 "title": "4.15.1.2. ElasticOrthotropic",
 "category": "general",
 "command": "elasticOrthotropic",
 "doc_section": "src",
 "rel_path": "src/elasticOrthotropic.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1598,
 "word_count": 167,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.2. ElasticOrthotropic

**nDMaterial(*'ElasticOrthotropic'*, *matTag*, *Ex*, *Ey*, *Ez*, *nu_xy*, *nu_yz*, *nu_zx*, *Gxy*, *Gyz*, *Gzx*, *rho=0.0*)**

This command is used to construct an ElasticOrthotropic material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Ex` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus in x direction |
| `Ey` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus in y direction |
| `Ez` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus in z direction |
| `nu_xy` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s ratios in x and y plane |
| `nu_yz` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s ratios in y and z plane |
| `nu_zx` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s ratios in z and x plane |
| `Gxy` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulii in x and y plane |
| `Gyz` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulii in y and z plane |
| `Gzx` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulii in z and x plane |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density (optional) |

The material formulations for the ElasticOrthotropic object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`
- `'Plane Stress'`
- `'AxiSymmetric'`
- `'BeamFiber'`
- `'PlateFiber'`
