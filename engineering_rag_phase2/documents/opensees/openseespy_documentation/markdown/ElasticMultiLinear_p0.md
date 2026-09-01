<!-- chunk_id: ElasticMultiLinear_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticMultiLinear.html",
 "title": "4.14.5.19. ElasticMultiLinear Material",
 "category": "material",
 "command": "ElasticMultiLinear",
 "doc_section": "src",
 "rel_path": "src/ElasticMultiLinear.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1519,
 "word_count": 172,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.19. ElasticMultiLinear Material

**uniaxialMaterial(*'ElasticMultiLinear'*, *matTag*, *eta=0.0*, *'-strain'*, **strain*, *'-stress'*, **stress*)**

This command is used to construct a multi-linear elastic uniaxial material object. The nonlinear stress-strain relationship is given by a multi-linear curve that is define by a set of points. The behavior is nonlinear but it is elastic. This means that the material loads and unloads along the same curve, and no energy is dissipated. The slope given by the last two specified points on the positive strain axis is extrapolated to infinite positive strain. Similarly, the slope given by the last two specified points on the negative strain axis is extrapolated to infinite negative strain. The number of provided strain points needs to be equal to the number of provided stress points.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `eta` ([float](https://docs.python.org/3/library/functions.html#float)) | damping tangent (optional, default=0.0) |
| `strain` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | list of strain points along stress-strain curve |
| `stress` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | list of stress points along stress-strain curve |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ElasticMultiLinear_Material)
