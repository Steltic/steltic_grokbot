<!-- chunk_id: loadConst_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/loadConst.html",
 "title": "7.5. loadConst command",
 "category": "general",
 "command": "loadConst",
 "doc_section": "src",
 "rel_path": "src/loadConst.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 522,
 "word_count": 81,
 "has_code": false,
 "has_table": true
} -->

## 7.5. loadConst command

**loadConst(*'-time'*, *pseudoTime*)**

This command is used to set the loads constant in the domain and to also set the time in the domain. When setting the loads constant, the procedure will invoke setLoadConst() on all LoadPattern objects which exist in the domain at the time the command is called.

| `pseudoTime` ([float](https://docs.python.org/3/library/functions.html#float)) | Time domain is to be set to (optional) |
| --- | --- |

Note

Load Patterns added afer this command is invoked are not set to constant.
