<!-- chunk_id: eleForce_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/eleForce.html",
 "title": "6.5. eleForce command",
 "category": "general",
 "command": "eleForce",
 "doc_section": "src",
 "rel_path": "src/eleForce.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 360,
 "word_count": 44,
 "has_code": false,
 "has_table": true
} -->

## 6.5. eleForce command

**eleForce(*eleTag*, *dof=-1*)**

Returns the elemental resisting force.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| --- | --- |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the element, (optional), if no `dof` is provided, a list of values for all dofs is returned. |
