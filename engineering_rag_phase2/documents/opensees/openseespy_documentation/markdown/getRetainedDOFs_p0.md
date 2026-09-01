<!-- chunk_id: getRetainedDOFs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/getRetainedDOFs.html",
 "title": "getRetainedDOFs command",
 "category": "general",
 "command": "getRetainedDOFs",
 "doc_section": "src",
 "rel_path": "src/getRetainedDOFs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 536,
 "word_count": 79,
 "has_code": false,
 "has_table": true
} -->

## getRetainedDOFs command

**getRetainedDOFs(*nodeTag*)**

Returns the retained (master) DOF numbers for a multi-point constraint.

The command retrieves the DOF numbers on the master node that participate in
the constraint.

**Arguments**

> | `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | **Master (retained) node** tag to query. |
> | --- | --- |

**Return Value**

> A list of integers containing the retained DOF numbers (1-based) on the master node.
> Returns an empty list if the node is not a master node or has no constraints.
