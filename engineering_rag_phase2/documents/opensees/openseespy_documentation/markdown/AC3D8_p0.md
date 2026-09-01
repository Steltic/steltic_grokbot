<!-- chunk_id: AC3D8_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/AC3D8.html",
 "title": "4.2.16.3. AC3D8",
 "category": "general",
 "command": "AC3D8",
 "doc_section": "src",
 "rel_path": "src/AC3D8.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 743,
 "word_count": 71,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.3. AC3D8

This command is used to construct an eight-node 3D brick acoustic element object based on a trilinear isoparametric formulation.

**element(*'AC3D8'*, *eleTag*, **eleNodes*, *matTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | 8 end nodes |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Material Tag of previously defined nD material |

Note

Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/AC3D8)
