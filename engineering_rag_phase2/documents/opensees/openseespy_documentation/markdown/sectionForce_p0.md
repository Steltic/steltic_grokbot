<!-- chunk_id: sectionForce_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sectionForce.html",
 "title": "6.32. sectionForce command",
 "category": "section",
 "command": "sectionForce",
 "doc_section": "src",
 "rel_path": "src/sectionForce.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 515,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 6.32. sectionForce command

**sectionForce(*eleTag*, *secNum*, *dof*)**

Returns the section force for a beam-column element. The dof of the section
depends on the section type. Please check with the section manual.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| --- | --- |
| `secNum` ([int](https://docs.python.org/3/library/functions.html#int)) | section number, i.e. the Gauss integratio number |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the dof of the section |
