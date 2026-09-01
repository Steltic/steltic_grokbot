<!-- chunk_id: fixZ_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fixZ.html",
 "title": "4.4.4. fixZ command",
 "category": "general",
 "command": "fixZ",
 "doc_section": "src",
 "rel_path": "src/fixZ.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 562,
 "word_count": 55,
 "has_code": false,
 "has_table": true
} -->

## 4.4.4. fixZ command

**fixZ(*z*, **constrValues*, *'-tol'*, *tol=1e-10*)**

Create homogeneous SP constriants.

| `z` ([float](https://docs.python.org/3/library/functions.html#float)) | z-coordinate of nodes to be constrained |
| --- | --- |
| `constrValues` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of constraint values (0 or 1), must be preceded with `*`. `0` free `1` fixed |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | user-defined tolerance (optional) |
