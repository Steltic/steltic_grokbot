<!-- chunk_id: Bcast_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Bcast.html",
 "title": "11.6. Bcast command",
 "category": "general",
 "command": "Bcast",
 "doc_section": "src",
 "rel_path": "src/Bcast.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 737,
 "word_count": 86,
 "has_code": true,
 "has_table": true
} -->

## 11.6. Bcast command

**Bcast(**data*)**

Broadcast information from processor 0 to all processors.

| `data` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | can be a list of integers |
| --- | --- |
| `data` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | can be a list of floats |
| `data` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | can be a string |

Note

Run the same command to receive data sent from pid = 0.

For example,

```
if pid == 0:

  data1 = []
  data2 = []

  ops.Bcast(*data1)
  ops.Bcast(*data2)

if pid != 0:
  data1 = ops.Bcast()
  data2 = ops.Bcast()
```
