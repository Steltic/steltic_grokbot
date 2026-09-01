<!-- chunk_id: nodeCoord_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeCoord.html",
 "title": "6.14. nodeCoord command",
 "category": "general",
 "command": "nodeCoord",
 "doc_section": "src",
 "rel_path": "src/nodeCoord.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 391,
 "word_count": 49,
 "has_code": false,
 "has_table": true
} -->

## 6.14. nodeCoord command

**nodeCoord(*nodeTag*, *dim=-1*)**

Returns the coordinates of a specified node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dimension at the node (1 through ndf), (optional), if no `dim` is provided, a list of values for all dimensions is returned. |
