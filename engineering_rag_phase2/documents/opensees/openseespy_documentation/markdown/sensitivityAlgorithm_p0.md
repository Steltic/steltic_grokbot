<!-- chunk_id: sensitivityAlgorithm_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sensitivityAlgorithm.html",
 "title": "9.8. sensitivityAlgorithm command",
 "category": "analysis",
 "command": "sensitivityAlgorithm",
 "doc_section": "src",
 "rel_path": "src/sensitivityAlgorithm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 348,
 "word_count": 40,
 "has_code": false,
 "has_table": true
} -->

## 9.8. sensitivityAlgorithm command

**sensitivityAlgorithm(*type*)**

This command is used to create a sensitivity algorithm.

| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the type of the sensitivity algorithm, `'-computeAtEachStep'` automatically compute at the end of each step `'-compuateByCommand'` compute by calling `computeGradients`. |
| --- | --- |
