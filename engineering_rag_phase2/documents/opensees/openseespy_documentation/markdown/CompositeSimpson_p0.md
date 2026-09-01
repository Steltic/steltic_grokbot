<!-- chunk_id: CompositeSimpson_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CompositeSimpson.html",
 "title": "4.13.6. CompositeSimpson",
 "category": "general",
 "command": "CompositeSimpson",
 "doc_section": "src",
 "rel_path": "src/CompositeSimpson.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 444,
 "word_count": 34,
 "has_code": true,
 "has_table": false
} -->

## 4.13.6. CompositeSimpson

**beamIntegration(*'CompositeSimpson'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'CompositeSimpson'*, *tag*, *N*, **secTags*)**

Composite Simpson `beamIntegration`. Two forms as in [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html#lobatto-beamintegration).

Example

```
import openseespy.opensees as ops

ops.beamIntegration('CompositeSimpson', 2, 1, 6)
ops.beamIntegration('CompositeSimpson', 3, 4, 1, 2, 2, 1)
```
