<!-- chunk_id: PenaltyUni_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PenaltyUni.html",
 "title": "4.14.5.23. Penalty material wrapper",
 "category": "material",
 "command": "PenaltyUni",
 "doc_section": "src",
 "rel_path": "src/PenaltyUni.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 718,
 "word_count": 96,
 "has_code": true,
 "has_table": false
} -->

## 4.14.5.23. Penalty material wrapper

Constructs a **Penalty** uniaxial material wrapper that adds a small stiffness to the wrapped material. Helps avoid singular stiffness from perfect plasticity; lightweight alternative to placing the wrapped material in parallel with an elastic material.

**uniaxialMaterial(*'Penalty'*, *matTag*, *otherTag*, *penalty*, **args*)**

Optional `'-noStress'`: penalty stiffness is added only to the tangent, not to stress.

Note

Use a small penalty value so the response stays dominated by the wrapped material.

Example

```
import openseespy.opensees as ops

E = 29000.0
penalty = 0.05 * E
ops.uniaxialMaterial('Elastic', 1, E)
ops.uniaxialMaterial('Penalty', 2, 1, penalty)
```

Code developed by: **Michael H. Scott**
