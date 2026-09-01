<!-- chunk_id: AV3D4_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/AV3D4.html",
 "title": "4.2.16.5. AV3D4",
 "category": "general",
 "command": "AV3D4",
 "doc_section": "src",
 "rel_path": "src/AV3D4.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 664,
 "word_count": 63,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.5. AV3D4

This command is used to construct a four-node 3D acoustic viscous boundary quad element object based on a bilinear isoparametric formulation.

**element(*'AV3D4'*, *eleTag*, **eleNodes*, *matTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | 4 end nodes |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Material Tag of previously defined nD material |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/AV3D4)
