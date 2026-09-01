<!-- chunk_id: Concrete02IS_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete02IS.html",
 "title": "4.14.2.3. Concrete02IS material",
 "category": "material",
 "command": "Concrete02IS",
 "doc_section": "src",
 "rel_path": "src/Concrete02IS.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1431,
 "word_count": 168,
 "has_code": true,
 "has_table": false
} -->

## 4.14.2.3. Concrete02IS material

This command constructs a uniaxial concrete material with the same compressive envelope and tension/cyclic behavior as [Concrete02](https://openseespydoc.readthedocs.io/en/latest/src/Concrete02.html), but with **user-defined initial stiffness** \(E_0\). In Concrete02 the initial stiffness is fixed at \(E_c = 2 f'_c / \varepsilon_{c0}\); Concrete02IS allows any \(E_0\) (for example \(57000\sqrt{f'_c}\) in psi units, or a secant stiffness to peak).

**uniaxialMaterial(*'Concrete02IS'*, *matTag*, *E0*, *fpc*, *epsc0*, *fpcu*, *epsU*, **optional*)**

Optional trailing arguments (in order): ratio between unloading slope at `epsU` and initial slope, tensile strength `ft`, tension softening stiffness `Ets`.

Note

Compressive parameters are taken as negative; if given positive, they are converted internally. Input \(E_0\) affects unloading/reloading stiffness in compression. The ascending branch uses the Popovics equation (Concrete02 uses the Hognestad parabola).

Example

```
import openseespy.opensees as ops

fc, epsc0 = 4000.0, -0.002
fcu, epscu = -1000.0, -0.006
Ec = 2.0 * fc / (-epsc0)
ops.uniaxialMaterial('Concrete02IS', 1, Ec, fc, epsc0, fcu, epscu)
ops.uniaxialMaterial('Concrete02IS', 2, Ec, fc, epsc0, fcu, epscu, 0.1, 500.0, 1738.33)
```

See also

[Concrete02](https://openseespydoc.readthedocs.io/en/latest/src/Concrete02.html).

Code developed by: Filip Filippou (Concrete02); Nasser Marafi (Concrete02IS).
