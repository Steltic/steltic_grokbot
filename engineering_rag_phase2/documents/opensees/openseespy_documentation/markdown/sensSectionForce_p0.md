<!-- chunk_id: sensSectionForce_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sensSectionForce.html",
 "title": "9.13. sensSectionForce command",
 "category": "section",
 "command": "sensSectionForce",
 "doc_section": "src",
 "rel_path": "src/sensSectionForce.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 591,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 9.13. sensSectionForce command

**sensSectionForce(*eleTag*, *<secNum>*, *dof*, *paramTag*)**

Returns the current section force sensitivity to a parameter at a specified element and section.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag |
| --- | --- |
| `secNum` ([int](https://docs.python.org/3/library/functions.html#int)) | section number (optional) |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | specific dof at the element (1 through element force ndf) |
| `paramTag` ([int](https://docs.python.org/3/library/functions.html#int)) | parameter tag |
