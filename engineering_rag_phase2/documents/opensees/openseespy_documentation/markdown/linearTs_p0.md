<!-- chunk_id: linearTs_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/linearTs.html",
 "title": "4.7.2. Linear TimeSeries",
 "category": "time_series",
 "command": "linearTs",
 "doc_section": "src",
 "rel_path": "src/linearTs.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 470,
 "word_count": 59,
 "has_code": false,
 "has_table": true
} -->

## 4.7.2. Linear TimeSeries

**timeSeries(*'Linear'*, *tag*, *'-factor'*, *factor=1.0*)**

This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e.

\(\lambda = f(t) = cFactor * t\)

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among TimeSeries objects |
| --- | --- |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | Linear factor (optional) |
