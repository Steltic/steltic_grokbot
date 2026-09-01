<!-- chunk_id: TensionOnly_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TensionOnly.html",
 "title": "4.14.5.26. TensionOnly material wrapper",
 "category": "material",
 "command": "TensionOnly",
 "doc_section": "src",
 "rel_path": "src/TensionOnly.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 572,
 "word_count": 65,
 "has_code": true,
 "has_table": false
} -->

## 4.14.5.26. TensionOnly material wrapper

Constructs a **TensionOnly** uniaxial material wrapper: when the wrapped material would return negative stress, the wrapper returns zero stress and zero tangent and does **not** call `commitState()` on the wrapped material. Only tensile (positive) stress is returned.

**uniaxialMaterial(*'TensionOnly'*, *matTag*, *otherTag*, **args*)**

Optional: `'-min'`, `minStrain`, `'-max'`, `maxStrain`.

Example

```
import openseespy.opensees as ops

ops.uniaxialMaterial('Elastic', 1, 100.0)
ops.uniaxialMaterial('TensionOnly', 2, 1)
```

Code developed by: **Michael H. Scott**
