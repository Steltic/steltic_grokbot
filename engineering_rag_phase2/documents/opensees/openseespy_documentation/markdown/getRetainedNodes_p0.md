<!-- chunk_id: getRetainedNodes_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/getRetainedNodes.html",
 "title": "getRetainedNodes command",
 "category": "general",
 "command": "getRetainedNodes",
 "doc_section": "src",
 "rel_path": "src/getRetainedNodes.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 832,
 "word_count": 131,
 "has_code": false,
 "has_table": false
} -->

## getRetainedNodes command

**getRetainedNodes(*nodeTag=None*)**

Returns the master (retained) node tag(s) for multi-point constraints.

The command retrieves master nodes associated with multi-point constraints (MP_Constraint)
in the domain.

**Arguments**

**Return Value**

> - If called without arguments: Returns a list of all master (retained) node tags in the domain.
> - If called with a node tag: Returns a list containing the master node tag (e.g., `[1]`) if the specified node is a constrained (slave) node. Returns an empty list `[]` if the node is not a constrained node.

**Notes**

> - The input nodeTag must be a **constrained (slave) node**. If a master node is provided, the command returns an empty list without an error message.
> - This command does not provide reverse lookup (i.e., finding all slave nodes constrained by a master node).
