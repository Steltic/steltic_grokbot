<!-- chunk_id: imposedMotion_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/imposedMotion.html",
 "title": "4.8.3.3. Imposed Motion",
 "category": "general",
 "command": "imposedMotion",
 "doc_section": "src",
 "rel_path": "src/imposedMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 700,
 "word_count": 95,
 "has_code": false,
 "has_table": true
} -->

## 4.8.3.3. Imposed Motion

**imposedMotion(*nodeTag*, *dof*, *gmTag*)**

This command is used to construct an ImposedMotionSP constraint which is used to enforce the response of a dof at a node in the model. The response enforced at the node at any give time is obtained from the GroundMotion object associated with the constraint.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node on which constraint is to be placed |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | dof of enforced response. Valid range is from 1 through ndf at node. |
| `gmTag` ([int](https://docs.python.org/3/library/functions.html#int)) | pre-defined GroundMotion object tag |
