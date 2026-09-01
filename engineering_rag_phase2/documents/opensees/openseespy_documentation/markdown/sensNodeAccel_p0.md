<!-- chunk_id: sensNodeAccel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sensNodeAccel.html",
 "title": "9.11. sensNodeAccel command",
 "category": "general",
 "command": "sensNodeAccel",
 "doc_section": "src",
 "rel_path": "src/sensNodeAccel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 439,
 "word_count": 47,
 "has_code": false,
 "has_table": true
} -->

## 9.11. sensNodeAccel command

**sensNodeAccel(*nodeTag*, *dof*, *paramTag*)**

Returns the current acceleration sensitivity to a parameter at a specified node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the node (1 through ndf) |
| `paramTag` ([int](https://docs.python.org/3/library/functions.html#int)) | parameter tag |
