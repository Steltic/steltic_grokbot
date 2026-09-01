<!-- chunk_id: arcLength_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/arcLength.html",
 "title": "5.6.1.5. Arc-Length Control",
 "category": "general",
 "command": "arcLength",
 "doc_section": "src",
 "rel_path": "src/arcLength.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 444,
 "word_count": 54,
 "has_code": false,
 "has_table": true
} -->

## 5.6.1.5. Arc-Length Control

**integrator(*'ArcLength'*, *s*, *alpha*)**

Create a ArcLength integrator. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied.

| `s` ([float](https://docs.python.org/3/library/functions.html#float)) | The arcLength. |
| --- | --- |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha\) a scaling factor on the reference loads. |
