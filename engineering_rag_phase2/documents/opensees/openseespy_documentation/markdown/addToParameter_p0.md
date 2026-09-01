<!-- chunk_id: addToParameter_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/addToParameter.html",
 "title": "9.2. addToParameter command",
 "category": "general",
 "command": "addToParameter",
 "doc_section": "src",
 "rel_path": "src/addToParameter.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 467,
 "word_count": 65,
 "has_code": false,
 "has_table": true
} -->

## 9.2. addToParameter command

**addToParameter(*tag*, *<specific parameter args>*)**

In case that more objects (e.g., element, section) are mapped to an existing parameter,
the  command can be used to relate these additional objects to the specific parameter.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the parameter. |
| --- | --- |
| `<specific parameter args>` | depend on the object in the FE model encapsulating the desired parameters. |
