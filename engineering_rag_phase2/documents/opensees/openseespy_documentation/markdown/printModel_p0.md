<!-- chunk_id: printModel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/printModel.html",
 "title": "6.29. printModel command",
 "category": "model",
 "command": "printModel",
 "doc_section": "src",
 "rel_path": "src/printModel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1278,
 "word_count": 147,
 "has_code": false,
 "has_table": true
} -->

## 6.29. printModel command

**printModel(*'-JSON'*, *'-file'*, *filename*, *'-node'*, *'-flag'*, *flag*, **nodes=[]*, **eles=[]*)**

This command is used to print output to screen or file.

| `filename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | name of file to which output is sent, by default, print to the screen. (optional) |
| --- | --- |
| `'-JSON'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | print to a JSON file. (optional) |
| `'-node'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | print node information. (optional) |
| `flag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer flag to be sent to the print() method, depending on the node and element type (optional) |
| `nodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of nodes tags to be printed, default is to print all, (optional) |
| `eles` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of element tags to be printed, default is to print all, (optional) |

Note

This command was called `print` in Tcl. Since `print` is a built-in function in Python, it is renamed to `printModel`.
