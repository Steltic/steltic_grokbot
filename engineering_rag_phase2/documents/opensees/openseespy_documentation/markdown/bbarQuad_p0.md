<!-- chunk_id: bbarQuad_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bbarQuad.html",
 "title": "4.2.7.8. Bbar Plane Strain Quadrilateral Element",
 "category": "element",
 "command": "bbarQuad",
 "doc_section": "src",
 "rel_path": "src/bbarQuad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1212,
 "word_count": 130,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.8. Bbar Plane Strain Quadrilateral Element

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

**element(*'bbarQuad'*, *eleTag*, **eleNodes*, *thick*, *matTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `thick` ([float](https://docs.python.org/3/library/functions.html#float)) | element thickness |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |

Note

1. PlainStrain only.
2. The valid queries to a Quad element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Bbar_Plane_Strain_Quadrilateral_Element)
