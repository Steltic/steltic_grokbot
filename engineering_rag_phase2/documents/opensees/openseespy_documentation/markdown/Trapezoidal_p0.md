<!-- chunk_id: Trapezoidal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Trapezoidal.html",
 "title": "4.13.5. Trapezoidal",
 "category": "general",
 "command": "Trapezoidal",
 "doc_section": "src",
 "rel_path": "src/Trapezoidal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 423,
 "word_count": 34,
 "has_code": true,
 "has_table": false
} -->

## 4.13.5. Trapezoidal

**beamIntegration(*'Trapezoidal'*, *tag*, *secTag*, *N*)**

**beamIntegration(*'Trapezoidal'*, *tag*, *N*, **secTags*)**

Trapezoidal rule `beamIntegration`. Two forms as in [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html#lobatto-beamintegration).

Example

```
import openseespy.opensees as ops

ops.beamIntegration('Trapezoidal', 2, 1, 6)
ops.beamIntegration('Trapezoidal', 3, 4, 1, 2, 2, 1)
```
