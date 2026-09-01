<!-- chunk_id: DiscretizeMember_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/DiscretizeMember.html",
 "title": "12.1. DiscretizeMember command",
 "category": "general",
 "command": "DiscretizeMember",
 "doc_section": "src",
 "rel_path": "src/DiscretizeMember.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1178,
 "word_count": 93,
 "has_code": false,
 "has_table": true
} -->

## 12.1. DiscretizeMember command

**preprocessing.DiscretizeMember.DiscretizeMember(*ndI*, *ndJ*, *numEle*, *eleType*, *integrTag*, *transfTag*, *nodeTag*, *eleTag*)**

Discretize beam elements between two nodes.

| `ndI` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag at I end |
| --- | --- |
| `ndJ` ([int](https://docs.python.org/3/library/functions.html#int)) | node tag at J end |
| `numEle` ([int](https://docs.python.org/3/library/functions.html#int)) | number of element to discretize |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the element type |
| `integrTag` ([int](https://docs.python.org/3/library/functions.html#int)) | beam integration tag ([beamIntegration commands](https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html)) |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | geometric transformation tag ([geomTransf commands](https://openseespydoc.readthedocs.io/en/latest/src/geomTransf.html)) |
| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | starting node tag |
| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | starting element tag |
