<!-- chunk_id: quadmesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/quadmesh.html",
 "title": "8.1.3. quad mesh",
 "category": "general",
 "command": "quadmesh",
 "doc_section": "src",
 "rel_path": "src/quadmesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2411,
 "word_count": 214,
 "has_code": false,
 "has_table": true
} -->

## 8.1.3. quad mesh

**mesh(*'quad'*, *tag*, *numlines*, **ltags*, *id*, *ndf*, *meshsize*, *eleType=''*, **eleArgs=[]*)**

Create a quad mesh object. The number of lines must be 4. These lines are continuous
to form a loop.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh tag. |
| --- | --- |
| `numlines` ([int](https://docs.python.org/3/library/functions.html#int)) | number of lines ([line mesh](https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html#linemesh)) for defining a polygon. |
| `ltags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | the [line mesh](https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html#linemesh) tags |
| `id` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh id. Meshes with same id are considered as same structure of fluid identity. `id` = 0 : not in FSI `id` > 0 : structure `id` < 0 : fluid |
| `ndf` ([int](https://docs.python.org/3/library/functions.html#int)) | ndf for nodes to be created. |
| `meshsize` ([float](https://docs.python.org/3/library/functions.html#float)) | mesh size. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the element type, (optional) [PFEMElementBubble](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementBubble.html) [PFEMElementCompressible](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementCompressible.html) [Tri31 Element](https://openseespydoc.readthedocs.io/en/latest/src/tri31.html) [Elastic Beam Column Element](https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html) [forceBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html) [dispBeamColumn](https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumn.html) [Shell Element](https://openseespydoc.readthedocs.io/en/latest/src/ShellMITC4.html) if no type is given, only nodes are created. If beam elements are given, beams are created instead of quad elements. If triangular elements are given, they are created by dividing one quad to two triangles. |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments. The arguments are same as in the element commands, but without element tag, and node tags. (optional) For example, `eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thickness, kappa]` |
