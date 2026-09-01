<!-- chunk_id: pc_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pc.html",
 "title": "4.6. pressureConstraint command",
 "category": "constraint",
 "command": "pc",
 "doc_section": "src",
 "rel_path": "src/pc.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 482,
 "word_count": 56,
 "has_code": true,
 "has_table": true
} -->

## 4.6. pressureConstraint command

**pressureConstraint(*nodeTag*, *pNodeTag*)**

Create a pressure constraint for incompressible flow.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node to be constrained |
| --- | --- |
| `pNodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of extra pressure node, which must exist before calling this command |

For example,

```
ops.node(1, 0.0, 0.0)
ops.node(2, 0.0, 0.0, '-ndf', 1)
ops.pressureConstraint(1, 2)
```
