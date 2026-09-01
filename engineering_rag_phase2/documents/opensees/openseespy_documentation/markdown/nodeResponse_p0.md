<!-- chunk_id: nodeResponse_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nodeResponse.html",
 "title": "6.21. nodeResponse command",
 "category": "general",
 "command": "nodeResponse",
 "doc_section": "src",
 "rel_path": "src/nodeResponse.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 584,
 "word_count": 77,
 "has_code": false,
 "has_table": true
} -->

## 6.21. nodeResponse command

**nodeResponse(*nodeTag*, *dof*, *responseID*)**

Returns the responses at a specified node. To get reactions (id=6), must call the `reactions` command before
this command.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof of the response |
| `responseID` ([int](https://docs.python.org/3/library/functions.html#int)) | the id of responses: Disp = 1 Vel = 2 Accel = 3 IncrDisp = 4 IncrDeltaDisp = 5 Reaction = 6 Unbalance = 7 RayleighForces = 8 |
