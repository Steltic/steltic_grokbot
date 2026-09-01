<!-- chunk_id: equalDOF_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/equalDOF.html",
 "title": "4.5.1. equalDOF command",
 "category": "general",
 "command": "equalDOF",
 "doc_section": "src",
 "rel_path": "src/equalDOF.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 690,
 "word_count": 75,
 "has_code": false,
 "has_table": true
} -->

## 4.5.1. equalDOF command

**equalDOF(*rNodeTag*, *cNodeTag*, **dofs*)**

Create a multi-point constraint between nodes.

| `rNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the retained, or primary node. |
| --- | --- |
| `cNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the constrained, or secondary node. |
| `dofs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | nodal degrees-of-freedom that are constrained at the cNode to be the same as those at the rNode Valid range is from 1 through ndf, the number of nodal degrees-of-freedom. |
