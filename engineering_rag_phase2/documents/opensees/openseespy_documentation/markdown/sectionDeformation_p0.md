<!-- chunk_id: sectionDeformation_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sectionDeformation.html",
 "title": "6.33. sectionDeformation command",
 "category": "section",
 "command": "sectionDeformation",
 "doc_section": "src",
 "rel_path": "src/sectionDeformation.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 527,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 6.33. sectionDeformation command

**sectionDeformation(*eleTag*, *secNum*, *dof*)**

Returns the section deformation for a beam-column element. The dof of the section
depends on the section type. Please check with the section manual.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| --- | --- |
| `secNum` ([int](https://docs.python.org/3/library/functions.html#int)) | section number, i.e. the Gauss integratio number |
| `dof` ([int](https://docs.python.org/3/library/functions.html#int)) | the dof of the section |
