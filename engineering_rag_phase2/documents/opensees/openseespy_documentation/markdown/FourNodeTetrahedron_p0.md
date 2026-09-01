<!-- chunk_id: FourNodeTetrahedron_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/FourNodeTetrahedron.html",
 "title": "4.2.10.1. FourNodeTetrahedron",
 "category": "general",
 "command": "FourNodeTetrahedron",
 "doc_section": "src",
 "rel_path": "src/FourNodeTetrahedron.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 799,
 "word_count": 73,
 "has_code": false,
 "has_table": true
} -->

## 4.2.10.1. FourNodeTetrahedron

This command is used to construct a standard four-node tetrahedron element objec with one-point Gauss integration.

**element(*'FourNodeTetrahedron'*, *eleTag*, **eleNodes*, *matTag*, *<b1*, *b2*, *b3>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |
| `b1` `b2` `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | body forces in global x,y,z directions |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/FourNodeTetrahedron)
