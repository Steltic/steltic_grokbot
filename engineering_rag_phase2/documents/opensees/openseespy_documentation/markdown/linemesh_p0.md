<!-- chunk_id: linemesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html",
 "title": "8.1.1. line mesh",
 "category": "general",
 "command": "linemesh",
 "doc_section": "src",
 "rel_path": "src/linemesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1640,
 "word_count": 163,
 "has_code": false,
 "has_table": true
} -->

## 8.1.1. line mesh

**mesh(*'line'*, *tag*, *numnodes*, **ndtags*, *id*, *ndf*, *meshsize*, *eleType=''*, **eleArgs=[]*)**

Create a line mesh object.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh tag. |
| --- | --- |
| `numnodes` ([int](https://docs.python.org/3/library/functions.html#int)) | number of nodes for defining consective lines. |
| `ndtags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the node tags |
| `id` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh id. Meshes with same id are considered as same structure of fluid identity. `id` = 0 : not in FSI `id` > 0 : structure `id` < 0 : fluid |
| `ndf` ([int](https://docs.python.org/3/library/functions.html#int)) | ndf for nodes to be created. |
| `meshsize` ([float](https://docs.python.org/3/library/functions.html#float)) | mesh size. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the type of the element, (optional) [Elastic Beam Column Element](https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html) [forceBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html) [dispBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumn.html) if no type is given, only nodes are created |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments. The arguments are same as in the element commands, but without element tag, and node tags. (optional) For example, `eleArgs = ['elasticBeamColumn', A, E, Iz, transfTag]` |
