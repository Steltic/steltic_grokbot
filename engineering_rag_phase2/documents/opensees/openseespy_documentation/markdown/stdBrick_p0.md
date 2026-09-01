<!-- chunk_id: stdBrick_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/stdBrick.html",
 "title": "4.2.9.1. Standard Brick Element",
 "category": "element",
 "command": "stdBrick",
 "doc_section": "src",
 "rel_path": "src/stdBrick.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1219,
 "word_count": 142,
 "has_code": false,
 "has_table": true
} -->

## 4.2.9.1. Standard Brick Element

This element is used to construct an eight-node brick element object, which uses a trilinear isoparametric formulation.

**element(*'stdBrick'*, *eleTag*, **eleNodes*, *matTag*, *<b1*, *b2*, *b3>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of eight element nodes in bottom and top faces and in counter-clockwise order |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |
| `b1` `b2` `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | body forces in global x,y,z directions |

Note

1. The valid queries to a Brick element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ (‘strains’ version > 2.2.0) and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.
2. This element can only be defined in -ndm 3 -ndf 3

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Standard_Brick_Element)
