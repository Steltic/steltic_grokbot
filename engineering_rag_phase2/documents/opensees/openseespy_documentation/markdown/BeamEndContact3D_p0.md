<!-- chunk_id: BeamEndContact3D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/BeamEndContact3D.html",
 "title": "4.2.13.5. BeamEndContact3D",
 "category": "general",
 "command": "BeamEndContact3D",
 "doc_section": "src",
 "rel_path": "src/BeamEndContact3D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3879,
 "word_count": 550,
 "has_code": false,
 "has_table": true
} -->

## 4.2.13.5. BeamEndContact3D

This command is used to construct a BeamEndContact3D element object.

**element(*'BeamEndContact3D'*, *eleTag*, *iNode*, *jNode*, *cNode*, *lNode*, *radius*, *gTol*, *fTol*, *<cFlag>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `iNode` ([int](https://docs.python.org/3/library/functions.html#int)) | master node from the beam (-ndm 3 -ndf 6) |
| `jNode` ([int](https://docs.python.org/3/library/functions.html#int)) | the remaining node on the beam element with `iNode` (-ndm 3 -ndf 6) |
| `cNode` ([int](https://docs.python.org/3/library/functions.html#int)) | constrained node (-ndm 3 -ndf 3) |
| `lNode` ([int](https://docs.python.org/3/library/functions.html#int)) | Lagrange multiplier node (-ndm 3 -ndf 3) |
| `radius` ([float](https://docs.python.org/3/library/functions.html#float)) | radius of circular beam associated with beam element |
| `gTol` ([float](https://docs.python.org/3/library/functions.html#float)) | gap tolerance |
| `fTol` ([float](https://docs.python.org/3/library/functions.html#float)) | force tolerance |
| `cFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | optional initial contact flag `cFlag` = 0 >> contact between bodies is initially assumed (DEFAULT) `cFlag1` = 1 >> no contact between bodies is initially assumed |

The BeamEndContact3D element is a node-to-surface contact element which defines a normal contact interface between the end of a beam element and a separate body. The first master node ($iNode) is the beam node which is at the end of the beam (i.e. only connected to a single beam element), the second node ($jNode) is the remaining node on the beam element in question. The slave node is a node from a second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain, and should be created with the same number of DOF as the slave node.

The BeamEndContact3D element enforces a contact condition between a fictitious circular plane associated with a beam element and a node from a second body. The normal direction of the contact plane coincides with the endpoint tangent of the beam element at the master beam node ($iNode). The extents of this circular plane are defined by the radius input parameter. The master beam node can only come into contact with a slave node which is within the extents of the contact plane. There is a lag step associated with changing between the ‘in contact’ and ‘not in contact’ conditions.

This element was developed for use in establishing a contact condition for the tip of a pile modeled as using beam elements and the underlying soil elements in three-dimensional analysis.

Note

1. The BeamEndContact3D element does not use a material object.
2. The valid recorder queries for this element are:

  1. force - returns the contact force acting on the slave node in vector form.
  2. masterforce - returns the reactions (forces and moments) acting on the master node.
  3. The BeamEndContact3D element works well in static and pseudo-static analysis situations.
3. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BeamEndContact3D)
