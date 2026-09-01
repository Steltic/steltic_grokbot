<!-- chunk_id: ASI3D8_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ASI3D8.html",
 "title": "4.2.16.4. ASI3D8",
 "category": "general",
 "command": "ASI3D8",
 "doc_section": "src",
 "rel_path": "src/ASI3D8.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1007,
 "word_count": 97,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.4. ASI3D8

This command is used to construct an eight-node zero-thickness 3D brick acoustic-structure interface element object based on a bilinear isoparametric formulation. The nodes in the acoustic domain share the same coordinates with the nodes in the solid domain.

**element(*'ASI3D8'*, *eleTag*, **eleNodes1*, **eleNodes2*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `*eleNodes1` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | four nodes defining structure domain of element boundaries |
| `*eleNodes2` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | four nodes defining acoustic domain of element boundaries |

Note

Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ASI3D8)
