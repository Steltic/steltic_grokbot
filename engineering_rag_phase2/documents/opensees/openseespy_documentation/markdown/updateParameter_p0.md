<!-- chunk_id: updateParameter_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/updateParameter.html",
 "title": "9.3. updateParameter command",
 "category": "general",
 "command": "updateParameter",
 "doc_section": "src",
 "rel_path": "src/updateParameter.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 571,
 "word_count": 70,
 "has_code": false,
 "has_table": true
} -->

## 9.3. updateParameter command

**updateParameter(*tag*, *newValue*)**

Once the parameters in FE model are defined, their value can be updated.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the parameter. |
| --- | --- |
| `newValue` ([float](https://docs.python.org/3/library/functions.html#float)) | the updated value to which the parameter needs to be set. |

Note

Scott M.H., Haukaas T. (2008). “Software framework for parameter updating and finite element response sensitivity analysis.” Journal of Computing in Civil Engineering, 22(5):281-291.
