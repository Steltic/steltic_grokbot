<!-- chunk_id: reset_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/reset.html",
 "title": "7.9. reset command",
 "category": "general",
 "command": "reset",
 "doc_section": "src",
 "rel_path": "src/reset.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 335,
 "word_count": 61,
 "has_code": false,
 "has_table": false
} -->

## 7.9. reset command

**reset()**

This command is used to set the state of the domain to its original state.

Note

It iterates over all components of the domain telling them to set their state back to the initial state. This is not always the same as going back to the state of the model after initial model generation, e.g. if elements have been removed.
