<!-- chunk_id: setParameter_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/setParameter.html",
 "title": "9.4. setParameter command",
 "category": "general",
 "command": "setParameter",
 "doc_section": "src",
 "rel_path": "src/setParameter.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 827,
 "word_count": 76,
 "has_code": false,
 "has_table": true
} -->

## 9.4. setParameter command

**setParameter(*'-val'*, *newValue*, *<'-ele'*, **eleTags>*, *<'-eleRange'*, *start*, *end>*, *<*args>*)**

set value for an element parameter

| `newValue` ([float](https://docs.python.org/3/library/functions.html#float)) | the updated value to which the parameter needs to be set. |
| --- | --- |
| `eleTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of element tags |
| `start` ([int](https://docs.python.org/3/library/functions.html#int)) | start element tag |
| `end` ([int](https://docs.python.org/3/library/functions.html#int)) | end element tag |
| `args` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([str](https://docs.python.org/3/library/stdtypes.html#str))) | a list of strings for the element parameter |
