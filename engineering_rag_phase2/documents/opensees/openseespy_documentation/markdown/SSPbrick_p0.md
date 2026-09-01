<!-- chunk_id: SSPbrick_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SSPbrick.html",
 "title": "4.2.9.4. SSPbrick Element",
 "category": "element",
 "command": "SSPbrick",
 "doc_section": "src",
 "rel_path": "src/SSPbrick.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2061,
 "word_count": 255,
 "has_code": false,
 "has_table": true
} -->

## 4.2.9.4. SSPbrick Element

This command is used to construct a SSPbrick element object.

**element(*'SSPbrick'*, *eleTag*, **eleNodes*, *matTag*, *<b1*, *b2*, *b3>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of eight element nodes in bottom and top faces and in counter-clockwise order |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique integer tag associated with previously-defined nDMaterial object |
| `b1` `b2` `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | constant body forces in global x-, y-, and z-directions, respectively (optional, default = 0.0) |

The SSPbrick element is an eight-node hexahedral element using physically stabilized single-point integration (SSP –> Stabilized Single Point). The stabilization incorporates an enhanced assumed strain field, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.

Note

1. Valid queries to the SSPbrick element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., ‘stress’, ‘strain’). Material response is recorded at the single integration point located in the center of the element.
2. The SSPbrick element was designed with intentions of duplicating the functionality of the stdBrick Element. If an example is found where the SSPbrick element cannot do something that works for the stdBrick Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SSPbrick_Element)
