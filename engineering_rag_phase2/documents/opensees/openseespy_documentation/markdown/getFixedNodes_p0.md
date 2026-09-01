<!-- chunk_id: getFixedNodes_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/getFixedNodes.html",
 "title": "getFixedNodes command",
 "category": "general",
 "command": "getFixedNodes",
 "doc_section": "src",
 "rel_path": "src/getFixedNodes.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 401,
 "word_count": 65,
 "has_code": false,
 "has_table": false
} -->

## getFixedNodes command

**getFixedNodes()**

Returns a list of node tags that are fixed (via the `fix` command) in the domain.

The command iterates over all single-point constraints (SP_Constraint) in the domain,
extracts the node tags, sorts them, and removes duplicates.

**Return Value**

A list of integers containing the tags of nodes that have at least one fixed DOF.
Returns an empty list if no fixed nodes are found.
