<!-- chunk_id: setNodeDisp_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setNodeDisp.html",
 "title": "7.15. setNodeDisp command",
 "category": "general",
 "command": "setNodeDisp",
 "doc_section": "src",
 "rel_path": "src/setNodeDisp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 530,
 "word_count": 53,
 "has_code": false,
 "has_table": true
} -->

## 7.15. setNodeDisp command

**setNodeDisp(*nodeTag*, *dof*, *value*, *'-commit'*)**

set the nodal displacement at the specified DOF.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the DOF of the displacement to be set. |
| `value` ([float](https://docs.python.org/3/library/functions.html#float)) | displacement value |
| `'-commit'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | commit nodal state. (optional) |
