<!-- chunk_id: dispBeamColumnInt_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumnInt.html",
 "title": "4.2.3.8. Flexure-Shear Interaction Displacement-Based Beam-Column Element",
 "category": "element",
 "command": "dispBeamColumnInt",
 "doc_section": "src",
 "rel_path": "src/dispBeamColumnInt.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1599,
 "word_count": 147,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.8. Flexure-Shear Interaction Displacement-Based Beam-Column Element

This command is used to construct a dispBeamColumnInt element object, which is a distributed-plasticity, displacement-based beam-column element which includes interaction between flexural and shear components.

**element(*'dispBeamColumnInt'*, *eleTag*, **eleNodes*, *numIntgrPts*, *secTag*, *transfTag*, *cRot*, *<'-mass'*, *massDens>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `numIntgrPts` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points along the element. |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined section object |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined coordinate-transformation (CrdTransf) object |
| `cRot` ([float](https://docs.python.org/3/library/functions.html#float)) | identifier for element center of rotation (or center of curvature distribution). Fraction of the height distance from bottom to the center of rotation (0 to 1) |
| `massDens` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass density (per unit length), from which a lumped-mass matrix is formed (optional, default=0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Flexure-Shear_Interaction_Displacement-Based_Beam-Column_Element)
