<!-- chunk_id: sp_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/sp_constraint/sp.html",
 "title": "sp Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "sp",
 "doc_section": "user/manual/model/sp_constraint",
 "rel_path": "user/manual/model/sp_constraint/sp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 559,
 "word_count": 88,
 "has_code": false,
 "has_table": false
} -->

## sp Command

This command is used to construct a single-point constraint object and add it to the enclosing LoadPattern.

**sp $nodeTag $dofTag $dofValue**

> $nodeTag, *integer*, tag of node to which constraint is applied.
> $dofTag, *integer*, the degree-of-freedom at the node to which constraint is applied (1 through ndf)
> $dofValue, *integer*, reference constraint value.

Note

The $dofValue is a reference value, it is the time series that provides the load factor. The load factor times the reference value is the constraint that is actually applied to the node.
