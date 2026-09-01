<!-- chunk_id: TzSimple1_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TzSimple1.html",
 "title": "4.14.4.2. TzSimple1 Material",
 "category": "material",
 "command": "TzSimple1",
 "doc_section": "src",
 "rel_path": "src/TzSimple1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1486,
 "word_count": 179,
 "has_code": false,
 "has_table": true
} -->

## 4.14.4.2. TzSimple1 Material

**uniaxialMaterial(*'TzSimple1'*, *matTag*, *soilType*, *tult*, *z50*, *c=0.0*)**

This command is used to construct a TzSimple1 uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `soilType` ([int](https://docs.python.org/3/library/functions.html#int)) | soilType = 1 Backbone of t-z curve approximates Reese and O’Neill (1987). soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation. |
| `tult` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate capacity of the t-z material. SEE NOTE 1. |
| `z50` ([float](https://docs.python.org/3/library/functions.html#float)) | Displacement at which 50% of tult is mobilized in monotonic loading. |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). See NOTE 2. |

Note

1. The argument `tult` is the ultimate capacity of the t-z material. Note that `t` or `tult` are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].
2. Nonzero `c` values are used to represent radiation damping effects

See also

[Notes](https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/TzSimple1.html)
