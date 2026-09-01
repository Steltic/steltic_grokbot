<!-- chunk_id: Damper_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Damper.html",
 "title": "4.14.5.3. Damper material wrapper",
 "category": "material",
 "command": "Damper",
 "doc_section": "src",
 "rel_path": "src/Damper.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 585,
 "word_count": 71,
 "has_code": true,
 "has_table": false
} -->

## 4.14.5.3. Damper material wrapper

Constructs a **Damper** uniaxial material wrapper. The wrapper uses the stress–strain response of any uniaxial material as a **stress versus strain-rate** relationship for damping: strain rate is passed as strain, and the material tangent provides the damping tangent.

**uniaxialMaterial(*'Damper'*, *matTag*, *otherTag*, **args*)**

`*args` may include `'-factors'`, `fact1`, `fact2`, … for multiple materials.

Example

```
import openseespy.opensees as ops

ops.uniaxialMaterial('Elastic', 1, 100.0)
ops.uniaxialMaterial('Damper', 2, 1)
```

Code developed by: **Michael H. Scott**
