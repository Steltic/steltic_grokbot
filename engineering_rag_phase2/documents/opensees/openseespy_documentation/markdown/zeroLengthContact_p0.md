<!-- chunk_id: zeroLengthContact_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthContact.html",
 "title": "4.2.1.5. zeroLengthContact elements",
 "category": "element",
 "command": "zeroLengthContact",
 "doc_section": "src",
 "rel_path": "src/zeroLengthContact.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1110,
 "word_count": 141,
 "has_code": true,
 "has_table": false
} -->

## 4.2.1.5. zeroLengthContact elements

Node-to-node frictional contact (**2D** or **3D**): constrained node vs retained node. Mohr–Coulomb: \(T = \mu N + c\) (\(T\) tangential, \(N\) normal, \(\mu\) friction, \(c\) cohesion).

**2D**

**element(*'zeroLengthContact2D'*, *eleTag*, *cNode*, *rNode*, *Kn*, *Kt*, *mu*, *'-normal'*, *Nx*, *Ny*)**

**3D**

**element(*'zeroLengthContact3D'*, *eleTag*, *cNode*, *rNode*, *Kn*, *Kt*, *mu*, *c*, *dir*)**

Note

1. Element tangent is non-symmetric; use a non-symmetric linear system solver.
2. 2D contact: nodes with 2 DOF; 3D contact: nodes with 3 DOF.
3. Out-normal of the master (retained) plane is taken fixed during analysis.

See also

[Notes (OpenSees wiki)](http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element)

Example

**2D:** contact between nodes **2** and **4**, normal `(0, -1)`.

```
import openseespy.opensees as ops

ops.element('zeroLengthContact2D', 1, 2, 4, 1e8, 1e8, 0.3, '-normal', 0, -1)
```

**3D:** cohesion `0`, out-normal **+Z** (`dir` = 3).

```
ops.element('zeroLengthContact3D', 1, 2, 4, 1e8, 1e8, 0.3, 0.0, 3)
```

Code developed by: **Gang Wang**, Geomatrix
