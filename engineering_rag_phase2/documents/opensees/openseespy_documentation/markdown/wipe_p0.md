<!-- chunk_id: wipe_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/wipe.html",
 "title": "7.26. wipe command",
 "category": "general",
 "command": "wipe",
 "doc_section": "src",
 "rel_path": "src/wipe.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 431,
 "word_count": 69,
 "has_code": false,
 "has_table": false
} -->

## 7.26. wipe command

**wipe()**

This command is used to destroy all constructed objects, i.e. all components of the model, all components of the analysis and all recorders.

This command is used to start over without having to exit and restart the interpreter. It causes all elements, nodes, constraints, loads to be removed from the domain. In addition it deletes all recorders, analysis objects and all material objects created by the model builder.
