<!-- chunk_id: MultiplierUni_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MultiplierUni.html",
 "title": "4.14.5.13. Multiplier material wrapper",
 "category": "material",
 "command": "MultiplierUni",
 "doc_section": "src",
 "rel_path": "src/MultiplierUni.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 472,
 "word_count": 54,
 "has_code": true,
 "has_table": false
} -->

## 4.14.5.13. Multiplier material wrapper

Constructs a **Multiplier** uniaxial material wrapper: stress and tangent of the wrapped material are multiplied by a factor. Typical uses include overstrength factors and p-y multipliers (e.g. pile group shadowing).

**uniaxialMaterial(*'Multiplier'*, *matTag*, *otherTag*, *multiplier*)**

Example

```
import openseespy.opensees as ops

ops.uniaxialMaterial('Elastic', 1, 100.0)
ops.uniaxialMaterial('Multiplier', 2, 1, 0.8)
```

Code developed by: **Michael H. Scott**
