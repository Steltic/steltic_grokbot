<!-- chunk_id: constantTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/constantTs.html",
 "title": "4.7.1. Constant TimeSeries",
 "category": "time_series",
 "command": "constantTs",
 "doc_section": "src",
 "rel_path": "src/constantTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 484,
 "word_count": 61,
 "has_code": false,
 "has_table": true
} -->

## 4.7.1. Constant TimeSeries

**timeSeries(*'Constant'*, *tag*, *'-factor'*, *factor=1.0*)**

This command is used to construct a TimeSeries object in which the load factor applied remains constant and is independent of the time in the domain, i.e. \(\lambda = f(t) = C\).

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects. |
| --- | --- |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | the load factor applied (optional) |
