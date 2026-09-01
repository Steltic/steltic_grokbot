<!-- chunk_id: load_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/load.html",
 "title": "4.8.1.1. load command",
 "category": "general",
 "command": "load",
 "doc_section": "src",
 "rel_path": "src/load.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 632,
 "word_count": 81,
 "has_code": false,
 "has_table": true
} -->

## 4.8.1.1. load command

**load(*nodeTag*, **loadValues*)**

This command is used to construct a NodalLoad object and add it to the enclosing LoadPattern.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node to which load is applied. |
| --- | --- |
| `loadValues` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | ndf reference load values. |

Note

The load values are reference loads values. It is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.
