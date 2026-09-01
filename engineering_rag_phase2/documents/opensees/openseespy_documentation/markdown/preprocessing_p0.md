<!-- chunk_id: preprocessing_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/preprocessing.html",
 "title": "12. Preprocessing Commands",
 "category": "general",
 "command": "preprocessing",
 "doc_section": "src",
 "rel_path": "src/preprocessing.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 740,
 "word_count": 41,
 "has_code": true,
 "has_table": false
} -->

## 12. Preprocessing Commands

The [mesh command](https://openseespydoc.readthedocs.io/en/latest/src/mesh.html) and [remesh command](https://openseespydoc.readthedocs.io/en/latest/src/remesh.html) should be
called as

```
import openseespy.opensees as ops
ops.mesh()
ops.remesh()
```

The [DiscretizeMember command](https://openseespydoc.readthedocs.io/en/latest/src/DiscretizeMember.html) should be called as

```
import openseespy.preprocessing.DiscretizeMember as opsdm

opsdm.DiscretizeMember()
```

1. [mesh command](https://openseespydoc.readthedocs.io/en/latest/src/mesh.html)
2. [remesh command](https://openseespydoc.readthedocs.io/en/latest/src/remesh.html)
3. [DiscretizeMember command](https://openseespydoc.readthedocs.io/en/latest/src/DiscretizeMember.html)
