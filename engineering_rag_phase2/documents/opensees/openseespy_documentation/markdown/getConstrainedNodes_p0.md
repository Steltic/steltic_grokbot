<!-- chunk_id: getConstrainedNodes_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/getConstrainedNodes.html",
 "title": "getConstrainedNodes command",
 "category": "general",
 "command": "getConstrainedNodes",
 "doc_section": "src",
 "rel_path": "src/getConstrainedNodes.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 652,
 "word_count": 95,
 "has_code": false,
 "has_table": false
} -->

## getConstrainedNodes command

**getConstrainedNodes()**

Returns all constrained (slave) node tags for multi-point constraints in the domain.

The command retrieves all slave nodes associated with multi-point constraints (MP_Constraint)
in the domain.

**Arguments**

> None.

**Return Value**

> Returns a list of all constrained (slave) node tags (e.g., `[2, 5, 7]`) in the domain.
> Returns an empty list `[]` if no multi-point constraints exist.

**Notes**

> - This command does not accept any arguments. Calling with a node tag (e.g., `getConstrainedNodes(2)`) returns an empty list.
> - To find the master node for a specific slave node, use `getRetainedNodes(slaveNodeTag)`.
