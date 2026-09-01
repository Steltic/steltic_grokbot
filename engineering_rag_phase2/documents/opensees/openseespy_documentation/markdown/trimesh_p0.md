<!-- chunk_id: trimesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/trimesh.html",
 "title": "8.1.2. triangular mesh",
 "category": "general",
 "command": "trimesh",
 "doc_section": "src",
 "rel_path": "src/trimesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2174,
 "word_count": 182,
 "has_code": false,
 "has_table": true
} -->

## 8.1.2. triangular mesh

**mesh(*'tri'*, *tag*, *numlines*, **ltags*, *id*, *ndf*, *meshsize*, *eleType=''*, **eleArgs=[]*)**

Create a triangular mesh object.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh tag. |
| --- | --- |
| `numlines` ([int](https://docs.python.org/3/library/functions.html#int)) | number of lines ([line mesh](https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html#linemesh)) for defining a polygon. |
| `ltags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the [line mesh](https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html#linemesh) tags |
| `id` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh id. Meshes with same id are considered as same structure of fluid identity. `id` = 0 : not in FSI `id` > 0 : structure `id` < 0 : fluid |
| `ndf` ([int](https://docs.python.org/3/library/functions.html#int)) | ndf for nodes to be created. |
| `meshsize` ([float](https://docs.python.org/3/library/functions.html#float)) | mesh size. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the element type, (optional) [PFEMElementBubble](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementBubble.html) [PFEMElementCompressible](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementCompressible.html) [Tri31 Element](https://openseespydoc.readthedocs.io/en/latest/src/tri31.html) [Elastic Beam Column Element](https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html) [forceBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html) [dispBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumn.html) if no type is given, only nodes are created. if beam elements are given, beams are created instead of triangular elements. |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments. The arguments are same as in the element commands, but without element tag, and node tags. (optional) For example, `eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]` |
