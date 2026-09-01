<!-- chunk_id: CatenaryCable_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CatenaryCable.html",
 "title": "4.2.14.1. CatenaryCableElement",
 "category": "element",
 "command": "CatenaryCable",
 "doc_section": "src",
 "rel_path": "src/CatenaryCable.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3093,
 "word_count": 357,
 "has_code": false,
 "has_table": true
} -->

## 4.2.14.1. CatenaryCableElement

This command is used to construct a catenary cable element object.

**element(*'CatenaryCable'*, *eleTag*, *iNode*, *jNode*, *weight*, *E*, *A*, *L0*, *alpha*, *temperature_change*, *rho*, *errorTol*, *Nsubsteps*, *massType*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `iNode` `jNode` ([int](https://docs.python.org/3/library/functions.html#int)) | end nodes (3 dof per node) |
| `weight` ([float](https://docs.python.org/3/library/functions.html#float)) | undefined |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus of the cable material |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of element |
| `L0` ([float](https://docs.python.org/3/library/functions.html#float)) | unstretched length of the cable |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of thermal expansion |
| `temperature_change` ([float](https://docs.python.org/3/library/functions.html#float)) | temperature change for the element |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | mass per unit length |
| `errorTol` ([float](https://docs.python.org/3/library/functions.html#float)) | allowed tolerance for within-element equilbrium (Newton-Rhapson iterations) |
| `Nsubsteps` ([int](https://docs.python.org/3/library/functions.html#int)) | number of within-element substeps into which equilibrium iterations are subdivided (not number of steps to convergence) |
| `massType` ([int](https://docs.python.org/3/library/functions.html#int)) | Mass matrix model to use (`massType` = 0 lumped mass matrix, `massType` = 1 rigid-body mass matrix (in development)) |

This cable is a flexibility-based formulation of the catenary cable. An iterative scheme is used internally to compute equilibrium. At each iteration, node i is considered fixed while node j is free. End-forces are applied at node-j and its displacements computed. Corrections to these forces are applied iteratively using a Newton-Rhapson scheme (with optional sub-stepping via $Nsubsteps) until nodal displacements are within the provided tolerance ($errortol). When convergence is reached, a stiffness matrix is computed by inversion of the flexibility matrix and rigid-body mode injection.

Note

1. The stiffness of the cable comes from the large-deformation interaction between loading and cable shape. Therefore, all cables must have distributed forces applied to them. See example. Should not work for only nodal forces.
2. Valid queries to the CatenaryCable element when creating an ElementalRecorder object correspond to ‘forces’, which output the end-forces of the element in global coordinates (3 for each node).
3. Only the lumped-mass formulation is currently available.
4. The element does up 100 internal iterations. If convergence is not achieved, will result in error and some diagnostic information is printed out.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/CatenaryCableElement)
