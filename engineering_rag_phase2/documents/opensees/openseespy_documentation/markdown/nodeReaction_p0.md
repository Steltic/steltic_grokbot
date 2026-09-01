<!-- chunk_id: nodeReaction_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeReaction.html",
 "title": "6.20. nodeReaction command",
 "category": "general",
 "command": "nodeReaction",
 "doc_section": "src",
 "rel_path": "src/nodeReaction.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 512,
 "word_count": 56,
 "has_code": false,
 "has_table": true
} -->

## 6.20. nodeReaction command

**nodeReaction(*nodeTag*, *dof=-1*)**

Returns the reactions at a specified node. Must call [`reactions()`](https://openseespydoc.readthedocs.io/en/latest/src/reactions.html#reactions) command before
this command.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the node (1 through ndf), (optional), if no `dof` is provided, a list of values for all dofs is returned. |
