<!-- chunk_id: TripleFrictionPendulum_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TripleFrictionPendulum.html",
 "title": "4.2.6.6. Triple Friction Pendulum Element",
 "category": "element",
 "command": "TripleFrictionPendulum",
 "doc_section": "src",
 "rel_path": "src/TripleFrictionPendulum.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2778,
 "word_count": 320,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.6. Triple Friction Pendulum Element

**element(*'TripleFrictionPendulum'*, *eleTag*, **eleNodes*, *frnTag1*, *frnTag2*, *frnTag3*, *vertMatTag*, *rotZMatTag*, *rotXMatTag*, *rotYMatTag*, *L1*, *L2*, *L3*, *d1*, *d2*, *d3*, *W*, *uy*, *kvt*, *minFv*, *tol*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `frnTag1`, `frnTag2` `frnTag3` ([int](https://docs.python.org/3/library/functions.html#int)) | = tags associated with previously-defined FrictionModels at the three sliding interfaces |
| `vertMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | = Pre-defined material tag for COMPRESSION behavior of the bearing |
| `rotZMatTag` `rotXMatTag` `rotYMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | = Pre-defined material tags for rotational behavior about 3-axis, 1-axis and 2-axis, respectively. |
| `L1` `L2` `L3` ([float](https://docs.python.org/3/library/functions.html#float)) | = effective radii. Li = R_i - h_i (see Figure 1) |
| `d1` `d2` `d3` ([float](https://docs.python.org/3/library/functions.html#float)) | = displacement limits of pendulums (Figure 1). Displacement limit of the bearing is 2 `d1` + `d2` + `d3` + `L1`. `d3`/ `L3` - `L1`. `d2`/ `L2` |
| `W` ([float](https://docs.python.org/3/library/functions.html#float)) | = axial force used for the first trial of the first analysis step. |
| `uy` ([float](https://docs.python.org/3/library/functions.html#float)) | = lateral displacement where sliding of the bearing starts. Recommended value = 0.25 to 1 mm. A smaller value may cause convergence problem. |
| `kvt` ([float](https://docs.python.org/3/library/functions.html#float)) | = Tension stiffness k_vt of the bearing. |
| `minFv (>=0)` ([float](https://docs.python.org/3/library/functions.html#float)) | = minimum vertical compression force in the bearing used for computing the horizontal tangent stiffness matrix from the normalized tangent stiffness matrix of the element. `minFv` is substituted for the actual compressive force when it is less than `minFv`, and prevents the element from using a negative stiffness matrix in the horizontal direction when uplift occurs. The vertical nodal force returned to nodes is always computed from `kvc` (or `kvt`) and vertical deformation, and thus is not affected by `minFv`. |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | = relative tolerance for checking the convergence of the element. Recommended value = 1.e-10 to 1.e-3. |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element)
