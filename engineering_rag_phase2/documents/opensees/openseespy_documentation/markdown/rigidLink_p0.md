<!-- chunk_id: rigidLink_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/rigidLink.html",
 "title": "4.5.4. rigidLink command",
 "category": "general",
 "command": "rigidLink",
 "doc_section": "src",
 "rel_path": "src/rigidLink.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 667,
 "word_count": 76,
 "has_code": false,
 "has_table": true
} -->

## 4.5.4. rigidLink command

**rigidLink(*type*, *rNodeTag*, *cNodeTag*)**

Create a multi-point constraint between nodes.

| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string-based argument for rigid-link type: `'bar'`: only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node `'beam'`: both the translational and rotational degrees of freedom are constrained. |
| --- | --- |
| `rNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the master node |
| `cNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integar tag identifying the slave node |
