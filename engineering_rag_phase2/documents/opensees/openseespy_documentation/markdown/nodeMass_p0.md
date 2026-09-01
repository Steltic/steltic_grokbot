<!-- chunk_id: nodeMass_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeMass.html",
 "title": "6.18. nodeMass command",
 "category": "general",
 "command": "nodeMass",
 "doc_section": "src",
 "rel_path": "src/nodeMass.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 371,
 "word_count": 49,
 "has_code": false,
 "has_table": true
} -->

## 6.18. nodeMass command

**nodeMass(*nodeTag*, *dof=-1*)**

Returns the mass at a specified node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the node (1 through ndf), (optional), if no `dof` is provided, a list of values for all dofs is returned. |
