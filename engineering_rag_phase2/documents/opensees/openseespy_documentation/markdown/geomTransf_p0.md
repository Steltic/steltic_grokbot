<!-- chunk_id: geomTransf_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/geomTransf.html",
 "title": "4.18. geomTransf commands",
 "category": "geom_transf",
 "command": "geomTransf",
 "doc_section": "src",
 "rel_path": "src/geomTransf.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1169,
 "word_count": 106,
 "has_code": true,
 "has_table": true
} -->

## 4.18. geomTransf commands

**geomTransf(*transfType*, *transfTag*, **transfArgs*)**

The geometric-transformation command is used to construct a coordinate-transformation (CrdTransf) object, which transforms beam element stiffness and resisting force from the basic system to the global-coordinate system. The command has at least one argument, the transformation type.

| `transfType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | geomTransf type |
| --- | --- |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | geomTransf tag. |
| `transfArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of geomTransf arguments, must be preceded with `*`. |

For example,

```
transfType = 'Linear'
transfTag = 1
transfArgs = []
geomTransf(transfType, transfTag, *transfArgs)
```

The following contain information about available `transfType`:

1. [Linear Transformation](https://openseespydoc.readthedocs.io/en/latest/src/LinearTransf.html)
2. [PDelta Transformation](https://openseespydoc.readthedocs.io/en/latest/src/pdelta.html)
3. [Corotational Transformation](https://openseespydoc.readthedocs.io/en/latest/src/corotational.html)
