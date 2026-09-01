<!-- chunk_id: equalDOF_Mixed_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/equalDOF_Mixed.html",
 "title": "4.5.2. equalDOF_Mixed command",
 "category": "general",
 "command": "equalDOF_Mixed",
 "doc_section": "src",
 "rel_path": "src/equalDOF_Mixed.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 860,
 "word_count": 94,
 "has_code": false,
 "has_table": true
} -->

## 4.5.2. equalDOF_Mixed command

**equalDOF_Mixed(*rNodeTag*, *cNodeTag*, *numDOF*, **rcdofs*)**

Create a multi-point constraint between nodes.

| `rNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the retained, or master node. |
| --- | --- |
| `cNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the constrained, or slave node. |
| `numDOF` ([int](https://docs.python.org/3/library/functions.html#int)) | number of dofs to be constrained |
| `rcdofs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | nodal degrees-of-freedom that are constrained at the cNode to be the same as those at the rNode Valid range is from 1 through ndf, the number of nodal degrees-of-freedom. `rcdofs = [rdof1, cdof1, rdof2, cdof2, ...]` |
