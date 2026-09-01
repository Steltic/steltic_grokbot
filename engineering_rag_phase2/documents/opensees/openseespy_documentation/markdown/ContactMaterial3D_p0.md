<!-- chunk_id: ContactMaterial3D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ContactMaterial3D.html",
 "title": "4.15.4.2. ContactMaterial3D",
 "category": "material",
 "command": "ContactMaterial3D",
 "doc_section": "src",
 "rel_path": "src/ContactMaterial3D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1461,
 "word_count": 172,
 "has_code": false,
 "has_table": true
} -->

## 4.15.4.2. ContactMaterial3D

**nDMaterial(*'ContactMaterial3D'*, *matTag*, *mu*, *G*, *c*, *t*)**

This command is used to construct a ContactMaterial3D nDMaterial object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | interface frictional coefficient |
| `G` ([float](https://docs.python.org/3/library/functions.html#float)) | interface stiffness parameter |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | interface cohesive intercept |
| `t` ([float](https://docs.python.org/3/library/functions.html#float)) | interface tensile strength |

The ContactMaterial3D nDMaterial defines the constitutive behavior of a frictional interface between two bodies in contact. The interface defined by this material object allows for sticking, frictional slip, and separation between the two bodies in a three-dimensional analysis. A regularized Coulomb frictional law is assumed. Information on the theory behind this material can be found in, e.g. Wriggers (2002).

Note

1. The ContactMaterial3D nDMaterial has been written to work with the SimpleContact3D and BeamContact3D element objects.
2. There are no valid recorder queries for this material other than those which are listed with those elements.

References:

Wriggers, P. (2002). Computational Contact Mechanics. John Wilely & Sons, Ltd, West Sussex, England.
