<!-- chunk_id: nodeEigenvector_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeEigenvector.html",
 "title": "6.16. nodeEigenvector command",
 "category": "general",
 "command": "nodeEigenvector",
 "doc_section": "src",
 "rel_path": "src/nodeEigenvector.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 524,
 "word_count": 62,
 "has_code": false,
 "has_table": true
} -->

## 6.16. nodeEigenvector command

**nodeEigenvector(*nodeTag*, *eigenvector*, *dof=-1*)**

Returns the eigenvector at a specified node.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `eigenvector` ([int](https://docs.python.org/3/library/functions.html#int)) | mode number of eigenvector to be returned |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the node (1 through ndf), (optional), if no `dof` is provided, a list of values for all dofs is returned. |
