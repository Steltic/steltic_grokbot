<!-- chunk_id: bbarBrick_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bbarBrick.html",
 "title": "4.2.9.2. Bbar Brick Element",
 "category": "element",
 "command": "bbarBrick",
 "doc_section": "src",
 "rel_path": "src/bbarBrick.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1269,
 "word_count": 145,
 "has_code": false,
 "has_table": true
} -->

## 4.2.9.2. Bbar Brick Element

This command is used to construct an eight-node mixed volume/pressure brick element object, which uses a trilinear isoparametric formulation.

**element(*'bbarBrick'*, *eleTag*, **eleNodes*, *matTag*, *<b1*, *b2*, *b3>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of eight element nodes in bottom and top faces and in counter-clockwise order |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |
| `b1` `b2` `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | body forces in global x,y,z directions |

Note

1. Node numbering for this element is different from that for the eight-node brick (Brick8N) element.
2. The valid queries to a Quad element when creating an ElementRecorder object are ‘forces’, ‘stresses’, ‘strains’, and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Bbar_Brick_Element)
