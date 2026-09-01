<!-- chunk_id: sectionFlexibility_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sectionFlexibility.html",
 "title": "6.35. sectionFlexibility command",
 "category": "section",
 "command": "sectionFlexibility",
 "doc_section": "src",
 "rel_path": "src/sectionFlexibility.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 393,
 "word_count": 46,
 "has_code": false,
 "has_table": true
} -->

## 6.35. sectionFlexibility command

**sectionFlexibility(*eleTag*, *secNum*)**

Returns the section flexibility matrix for a beam-column element.
A list of values in the row order will be returned.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag. |
| --- | --- |
| `secNum` ([int](https://docs.python.org/3/library/functions.html#int)) | section number, i.e. the Gauss integration number |
