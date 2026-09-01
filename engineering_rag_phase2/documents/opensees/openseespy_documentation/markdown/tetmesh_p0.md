<!-- chunk_id: tetmesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/tetmesh.html",
 "title": "8.1.4. tetrahedron mesh",
 "category": "general",
 "command": "tetmesh",
 "doc_section": "src",
 "rel_path": "src/tetmesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1380,
 "word_count": 150,
 "has_code": false,
 "has_table": true
} -->

## 8.1.4. tetrahedron mesh

**mesh(*'tet'*, *tag*, *nummesh*, **mtags*, *id*, *ndf*, *meshsize*, *eleType=''*, **eleArgs=[]*)**

Create a 3D tetrahedron mesh object.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh tag. |
| --- | --- |
| `nummesh` ([int](https://docs.python.org/3/library/functions.html#int)) | number of 2D mesh for defining a 3D body. |
| `mtags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the mesh tags |
| `id` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh id. Meshes with same id are considered as same structure of fluid identity. `id` = 0 : not in FSI `id` > 0 : structure `id` < 0 : fluid |
| `ndf` ([int](https://docs.python.org/3/library/functions.html#int)) | ndf for nodes to be created. |
| `meshsize` ([float](https://docs.python.org/3/library/functions.html#float)) | mesh size. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the element type, (optional) [FourNodeTetrahedron](https://openseespydoc.readthedocs.io/en/latest/src/FourNodeTetrahedron.html) if no type is given, only nodes are created. |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments. The arguments are same as in the element commands, but without element tag, and node tags. (optional) |
