<!-- chunk_id: elasticIsotropic_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticIsotropic.html",
 "title": "4.15.1.1. ElasticIsotropic",
 "category": "general",
 "command": "elasticIsotropic",
 "doc_section": "src",
 "rel_path": "src/elasticIsotropic.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 713,
 "word_count": 70,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.1. ElasticIsotropic

**nDMaterial(*'ElasticIsotropic'*, *matTag*, *E*, *nu*, *rho=0.0*)**

This command is used to construct an ElasticIsotropic material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s ratio |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density (optional) |

The material formulations for the ElasticIsotropic object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`
- `'Plane Stress'`
- `'AxiSymmetric'`
- `'PlateFiber'`
