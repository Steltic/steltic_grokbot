<!-- chunk_id: getFixedDOFs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/getFixedDOFs.html",
 "title": "getFixedDOFs command",
 "category": "general",
 "command": "getFixedDOFs",
 "doc_section": "src",
 "rel_path": "src/getFixedDOFs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 548,
 "word_count": 86,
 "has_code": false,
 "has_table": true
} -->

## getFixedDOFs command

**getFixedDOFs(*nodeTag*)**

Returns a list of fixed DOF numbers for a specified node.

> The command retrieves all single-point constraints (SP_Constraint) applied to the given node
> and returns the DOF numbers that are fixed.

**Arguments**

> | `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Node tag to query. |
> | --- | --- |

**Return Value**

> A list of integers containing the fixed DOF numbers (1-based) for the specified node.
> Returns an empty list if the node has no fixed DOFs or the node does not exist.
