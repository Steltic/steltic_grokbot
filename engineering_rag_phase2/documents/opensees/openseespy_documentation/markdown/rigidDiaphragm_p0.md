<!-- chunk_id: rigidDiaphragm_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/rigidDiaphragm.html",
 "title": "4.5.3. rigidDiaphragm command",
 "category": "general",
 "command": "rigidDiaphragm",
 "doc_section": "src",
 "rel_path": "src/rigidDiaphragm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 853,
 "word_count": 91,
 "has_code": false,
 "has_table": true
} -->

## 4.5.3. rigidDiaphragm command

**rigidDiaphragm(*perpDirn*, *rNodeTag*, **cNodeTags*)**

Create a multi-point constraint between nodes.
These objects will constrain certain degrees-of-freedom at the listed secondary nodes to move as if in a rigid plane with the primary (retained) node. To enforce this constraint, `Transformation` constraint handler is recommended.

| `perpDirn` ([int](https://docs.python.org/3/library/functions.html#int)) | direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane) |
| --- | --- |
| `rNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the retained (primary) node |
| `cNodeTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | integar tags identifying the constrained (secondary) nodes |
