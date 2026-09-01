<!-- chunk_id: fixX_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fixX.html",
 "title": "4.4.2. fixX command",
 "category": "general",
 "command": "fixX",
 "doc_section": "src",
 "rel_path": "src/fixX.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 562,
 "word_count": 55,
 "has_code": false,
 "has_table": true
} -->

## 4.4.2. fixX command

**fixX(*x*, **constrValues*, *'-tol'*, *tol=1e-10*)**

Create homogeneous SP constriants.

| `x` ([float](https://docs.python.org/3/library/functions.html#float)) | x-coordinate of nodes to be constrained |
| --- | --- |
| `constrValues` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of constraint values (0 or 1), must be preceded with `*`. `0` free `1` fixed |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | user-defined tolerance (optional) |
