<!-- chunk_id: sensNodeDisp_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sensNodeDisp.html",
 "title": "9.9. sensNodeDisp command",
 "category": "general",
 "command": "sensNodeDisp",
 "doc_section": "src",
 "rel_path": "src/sensNodeDisp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 438,
 "word_count": 47,
 "has_code": false,
 "has_table": true
} -->

## 9.9. sensNodeDisp command

**sensNodeDisp(*nodeTag*, *dof*, *paramTag*)**

Returns the current displacement sensitivity to a parameter at a specified node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the node (1 through ndf) |
| `paramTag` ([int](https://docs.python.org/3/library/functions.html#int)) | parameter tag |
