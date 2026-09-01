<!-- chunk_id: SimpleContact2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SimpleContact2D.html",
 "title": "4.2.13.1. SimpleContact2D",
 "category": "general",
 "command": "SimpleContact2D",
 "doc_section": "src",
 "rel_path": "src/SimpleContact2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3158,
 "word_count": 426,
 "has_code": false,
 "has_table": true
} -->

## 4.2.13.1. SimpleContact2D

This command is used to construct a SimpleContact2D element object.

**element(*'SimpleContact2D'*, *eleTag*, *iNode*, *jNode*, *cNode*, *lNode*, *matTag*, *gTol*, *fTol*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `iNode` `jNode` ([int](https://docs.python.org/3/library/functions.html#int)) | retained nodes (-ndm 2 -ndf 2) |
| `cNode` ([int](https://docs.python.org/3/library/functions.html#int)) | constrained node (-ndm 2 -ndf 2) |
| `lNode` ([int](https://docs.python.org/3/library/functions.html#int)) | Lagrange multiplier node (-ndm 2 -ndf 2) |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique integer tag associated with previously-defined nDMaterial object |
| `gTol` ([float](https://docs.python.org/3/library/functions.html#float)) | gap tolerance |
| `fTol` ([float](https://docs.python.org/3/library/functions.html#float)) | force tolerance |

The SimpleContact2D element is a two-dimensional node-to-segment contact element which defines a frictional contact interface between two separate bodies. The master nodes are the nodes which define the endpoints of a line segment on the first body, and the slave node is a node from the second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain. Information on the theory behind this element can be found in, e.g. Wriggers (2002).

Note

1. The SimpleContact2D element has been written to work exclusively with the ContactMaterial2D nDMaterial object.
2. The valid recorder queries for this element are:

  1. force - returns the contact force acting on the slave node in vector form.
  2. frictionforce - returns the frictional force acting on the slave node in vector form.
  3. forcescalar - returns the scalar magnitudes of the normal and tangential contact forces.
  4. The SimpleContact2D elements are set to consider frictional behavior as a default, but the frictional state of the SimpleContact2D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below
3. The SimpleContact2D element works well in static and pseudo-static analysis situations.
4. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SimpleContact2D)
