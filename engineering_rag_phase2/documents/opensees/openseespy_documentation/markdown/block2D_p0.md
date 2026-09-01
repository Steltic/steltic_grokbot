<!-- chunk_id: block2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/block2D.html",
 "title": "4.12.1. block2D command",
 "category": "general",
 "command": "block2D",
 "doc_section": "src",
 "rel_path": "src/block2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1254,
 "word_count": 148,
 "has_code": false,
 "has_table": true
} -->

## 4.12.1. block2D command

**block2D(*numX*, *numY*, *startNode*, *startEle*, *eleType*, **eleArgs*, **crds*)**

Create mesh of quadrilateral elements

| `numX` ([int](https://docs.python.org/3/library/functions.html#int)) | number of elements in local x directions of the block. |
| --- | --- |
| `numY` ([int](https://docs.python.org/3/library/functions.html#int)) | number of elements in local y directions of the block. |
| `startNode` ([int](https://docs.python.org/3/library/functions.html#int)) | node from which the mesh generation will start. |
| `startEle` ([int](https://docs.python.org/3/library/functions.html#int)) | element from which the mesh generation will start. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | element type (`'quad'`, `'shell'`, `'bbarQuad'`, `'enhancedQuad'`, or `'SSPquad'`) |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element parameters. |
| `crds` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | coordinates of the block elements with the format: [1, x1, y1, <z1>, 2, x2, y2, <z2>, 3, x3, y3, <z3>, 4, x4, y4, <z4>, <5>, <x5>, <y5>, <z5>, <6>, <x6>, <y6>, <z6>, <7>, <x7>, <y7>, <z7>, <8>, <x8>, <y8>, <z8>, <9>, <x9>, <y9>, <z9>] <> means optional |
