<!-- chunk_id: setNodeVel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setNodeVel.html",
 "title": "7.16. setNodeVel command",
 "category": "general",
 "command": "setNodeVel",
 "doc_section": "src",
 "rel_path": "src/setNodeVel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 517,
 "word_count": 53,
 "has_code": false,
 "has_table": true
} -->

## 7.16. setNodeVel command

**setNodeVel(*nodeTag*, *dof*, *value*, *'-commit'*)**

set the nodal velocity at the specified DOF.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the DOF of the velocity to be set. |
| `value` ([float](https://docs.python.org/3/library/functions.html#float)) | velocity value |
| `'-commit'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | commit nodal state. (optional) |
