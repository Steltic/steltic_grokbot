<!-- chunk_id: sp_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sp.html",
 "title": "4.8.1.3. sp command",
 "category": "general",
 "command": "sp",
 "doc_section": "src",
 "rel_path": "src/sp.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 735,
 "word_count": 98,
 "has_code": false,
 "has_table": true
} -->

## 4.8.1.3. sp command

**sp(*nodeTag*, *dof*, *dofValue*)**

This command is used to construct a single-point constraint object and add it to the enclosing LoadPattern.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node to which load is applied. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the degree-of-freedom at the node to which constraint is applied (1 through ndf) |
| `dofValue` ([float](https://docs.python.org/3/library/functions.html#float)) | reference constraint value. |

Note

The dofValue is a reference value, it is the time series that provides the load factor. The load factor times the reference value is the constraint that is actually applied to the node.
