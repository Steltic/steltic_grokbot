<!-- chunk_id: BeamContact2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BeamContact2D.html",
 "title": "4.2.13.3. BeamContact2D",
 "category": "general",
 "command": "BeamContact2D",
 "doc_section": "src",
 "rel_path": "src/BeamContact2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4035,
 "word_count": 557,
 "has_code": false,
 "has_table": true
} -->

## 4.2.13.3. BeamContact2D

This command is used to construct a BeamContact2D element object.

**element(*'BeamContact2D'*, *eleTag*, *iNode*, *jNode*, *sNode*, *lNode*, *matTag*, *width*, *gTol*, *fTol*, *<cFlag>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `iNode` `jNode` ([int](https://docs.python.org/3/library/functions.html#int)) | master nodes (-ndm 2 -ndf 3) |
| `sNode` ([int](https://docs.python.org/3/library/functions.html#int)) | slave node (-ndm 2 -ndf 2) |
| `lNode` ([int](https://docs.python.org/3/library/functions.html#int)) | Lagrange multiplier node (-ndm 2 -ndf 2) |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique integer tag associated with previously-defined nDMaterial object |
| `width` ([float](https://docs.python.org/3/library/functions.html#float)) | the width of the wall represented by the beam element in plane strain |
| `gTol` ([float](https://docs.python.org/3/library/functions.html#float)) | gap tolerance |
| `fTol` ([float](https://docs.python.org/3/library/functions.html#float)) | force tolerance |
| `cFlag` ([int](https://docs.python.org/3/library/functions.html#int)) | optional initial contact flag `cFlag` = 0 >> contact between bodies is initially assumed (DEFAULT) `cFlag` = 1 >> no contact between bodies is initially assumed |

The BeamContact2D element is a two-dimensional beam-to-node contact element which defines a frictional contact interface between a beam element and a separate body. The master nodes (3 DOF) are the endpoints of the beam element, and the slave node (2 DOF) is a node from a second body. The Lagrange multiplier node (2 DOF) is required to enforce the contact condition. Each contact element should have a unique Lagrange multiplier node. The Lagrange multiplier node should not be fixed, otherwise the contact condition will not work.

Under plane strain conditions in 2D, a beam element represents a unit thickness of a wall. The width is the dimension of this wall in the 2D plane. This width should be built-in to the model to ensure proper enforcement of the contact condition. The Excavation Supported by Cantilevered Sheet Pile Wall practical example provides some further examples and discussion on the usage of this element.

Note

1. The BeamContact2D element has been written to work exclusively with the ContactMaterial2D nDMaterial object.
2. The valid recorder queries for this element are:

  1. force - returns the contact force acting on the slave node in vector form.
  2. frictionforce - returns the frictional force acting on the slave node in vector form.
  3. forcescalar - returns the scalar magnitudes of the normal and tangential contact forces.
  4. masterforce - returns the reactions (forces and moments) acting on the master nodes.
  5. The BeamContact2D elements are set to consider frictional behavior as a default, but the frictional state of the BeamContact2D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below
3. The BeamContact2D element works well in static and pseudo-static analysis situations.
4. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BeamContact2D)
