<!-- chunk_id: node_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/node.html",
 "title": "4.3. node command",
 "category": "general",
 "command": "node",
 "doc_section": "src",
 "rel_path": "src/node.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1024,
 "word_count": 71,
 "has_code": false,
 "has_table": true
} -->

## 4.3. node command

**node(*nodeTag*, **crds*, *'-ndf'*, *ndf*, *'-mass'*, **mass*, *'-disp'*, **disp*, *'-vel'*, **vel*, *'-accel'*, **accel*)**

Create a OpenSees node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `crds` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | nodal coordinates. |
| `ndf` ([float](https://docs.python.org/3/library/functions.html#float)) | nodal ndf. (optional) |
| `mass` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | nodal mass. (optional) |
| `vel` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | nodal velocities. (optional) |
| `accel` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | nodal accelerations. (optional) |
