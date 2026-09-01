<!-- chunk_id: QzSimple1_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/QzSimple1.html",
 "title": "4.14.4.3. QzSimple1 Material",
 "category": "material",
 "command": "QzSimple1",
 "doc_section": "src",
 "rel_path": "src/QzSimple1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2089,
 "word_count": 265,
 "has_code": false,
 "has_table": true
} -->

## 4.14.4.3. QzSimple1 Material

**uniaxialMaterial(*'QzSimple1'*, *matTag*, *qzType*, *qult*, *Z50*, *suction=0.0*, *c=0.0*)**

This command is used to construct a QzSimple1 uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `qzType` ([int](https://docs.python.org/3/library/functions.html#int)) | qzType = 1 Backbone of q-z curve approximates Reese and O’Neill’s (1987) relation for drilled shafts in clay. qzType = 2 Backbone of q-z curve approximates Vijayvergiya’s (1977) relation for piles in sand. |
| `qult` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate capacity of the q-z material. SEE NOTE 1. |
| `Z50` ([float](https://docs.python.org/3/library/functions.html#float)) | Displacement at which 50% of qult is mobilized in monotonic loading. SEE NOTE 2. |
| `suction` ([float](https://docs.python.org/3/library/functions.html#float)) | Uplift resistance is equal to suction*qult. Default = 0.0. The value of suction must be 0.0 to 0.1. |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Default = 0.0. Nonzero c values are used to represent radiation damping effects.* |

Note

1. `qult`: Ultimate capacity of the q-z material. Note that `q1` or `qult` are stresses [force per unit area of pile tip] in common design equations, but are both loads for this uniaxialMaterial [i.e., stress times tip area].
2. Nonzero `c` values are used to represent radiation damping effects
3. `Z50`: Displacement at which 50% of qult is mobilized in monotonic loading. Note that Vijayvergiya’s relation (`qzType=2`) refers to a “critical” displacement (`zcrit`) at which qult is fully mobilized, and that the corresponding `z50` would be 0. `125zcrit`.
4. optional args    `suction` and    `c` must either both be omitted or both provided.

See also

[Notes](https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/QzSimple1.html)
