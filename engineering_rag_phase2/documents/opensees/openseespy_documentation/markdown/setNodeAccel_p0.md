<!-- chunk_id: setNodeAccel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setNodeAccel.html",
 "title": "7.17. setNodeAccel command",
 "category": "general",
 "command": "setNodeAccel",
 "doc_section": "src",
 "rel_path": "src/setNodeAccel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 531,
 "word_count": 53,
 "has_code": false,
 "has_table": true
} -->

## 7.17. setNodeAccel command

**setNodeAccel(*nodeTag*, *dof*, *value*, *'-commit'*)**

set the nodal acceleration at the specified DOF.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the DOF of the acceleration to be set. |
| `value` ([float](https://docs.python.org/3/library/functions.html#float)) | acceleration value |
| `'-commit'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | commit nodal state. (optional) |
