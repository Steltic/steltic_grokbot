<!-- chunk_id: SimpleFracture_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SimpleFracture.html",
 "title": "4.14.5.25. SimpleFracture material wrapper",
 "category": "material",
 "command": "SimpleFracture",
 "doc_section": "src",
 "rel_path": "src/SimpleFracture.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 516,
 "word_count": 60,
 "has_code": true,
 "has_table": false
} -->

## 4.14.5.25. SimpleFracture material wrapper

Constructs a **SimpleFracture** uniaxial material wrapper that imposes tensile fracture on the wrapped material: after strain exceeds a maximum tensile strain, the wrapper supplies compressive stress based on an estimate of the elastic strain.

**uniaxialMaterial(*'SimpleFracture'*, *matTag*, *otherTag*, *maxStrain*)**

Example

```
import openseespy.opensees as ops

ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
ops.uniaxialMaterial('SimpleFracture', 2, 1, 0.8)
```

Code developed by: **Michael H. Scott**
