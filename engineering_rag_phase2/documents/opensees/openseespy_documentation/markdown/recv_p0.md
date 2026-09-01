<!-- chunk_id: recv_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/recv.html",
 "title": "11.5. recv command",
 "category": "general",
 "command": "recv",
 "doc_section": "src",
 "rel_path": "src/recv.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 508,
 "word_count": 58,
 "has_code": false,
 "has_table": true
} -->

## 11.5. recv command

**recv(*'-pid'*, *pid*)**

Receive information from another processor.

| `pid` ([int](https://docs.python.org/3/library/functions.html#int)) | ID of processor where data is received from |
| --- | --- |
| `pid` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | if `pid` is `'ANY'`, the processor can receive data from any processor. |

Note

[send command](https://openseespydoc.readthedocs.io/en/latest/src/send.html) and recv command must match and the order of calling both
commands matters.
