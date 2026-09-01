<!-- chunk_id: enhancedQuad_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/enhancedQuad.html",
 "title": "4.2.7.9. Enhanced Strain Quadrilateral Element",
 "category": "element",
 "command": "enhancedQuad",
 "doc_section": "src",
 "rel_path": "src/enhancedQuad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1104,
 "word_count": 103,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.9. Enhanced Strain Quadrilateral Element

This command is used to construct a four-node quadrilateral element, which uses a bilinear isoparametric formulation with enhanced strain modes.

**element(*'enhancedQuad'*, *eleTag*, **eleNodes*, *thick*, *type*, *matTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `thick` ([float](https://docs.python.org/3/library/functions.html#float)) | element thickness |
| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string representing material behavior. Valid options depend on the NDMaterial object and its available material formulations. The type parameter can be either `'PlaneStrain'` or `'PlaneStress'` |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Enhanced_Strain_Quadrilateral_Element)
