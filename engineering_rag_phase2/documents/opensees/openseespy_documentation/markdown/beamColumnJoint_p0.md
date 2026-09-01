<!-- chunk_id: beamColumnJoint_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/beamColumnJoint.html",
 "title": "4.2.4.1. BeamColumnJoint Element",
 "category": "element",
 "command": "beamColumnJoint",
 "doc_section": "src",
 "rel_path": "src/beamColumnJoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3156,
 "word_count": 334,
 "has_code": false,
 "has_table": true
} -->

## 4.2.4.1. BeamColumnJoint Element

This command is used to construct a two-dimensional beam-column-joint element object. The element may be used with both two-dimensional and three-dimensional structures; however, load is transferred only in the plane of the element.

**element(*'beamColumnJoint'*, *eleTag*, **eleNodes*, *Mat1Tag*, *Mat2Tag*, *Mat3Tag*, *Mat4Tag*, *Mat5Tag*, *Mat6Tag*, *Mat7Tag*, *Mat8Tag*, *Mat9Tag*, *Mat10Tag*, *Mat11Tag*, *Mat12Tag*, *Mat13Tag*, *<eleHeightFac=1.0*, *eleWidthFac=1.0>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes |
| `Mat1Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for left bar-slip spring at node 1 |
| `Mat2Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for right bar-slip spring at node 1 |
| `Mat3Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface-shear spring at node 1 |
| `Mat4Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for lower bar-slip spring at node 2 |
| `Mat5Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for upper bar-slip spring at node 2 |
| `Mat6Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface-shear spring at node 2 |
| `Mat7Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for left bar-slip spring at node 3 |
| `Mat8Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for right bar-slip spring at node 3 |
| `Mat9Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface-shear spring at node 3 |
| `Mat10Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for lower bar-slip spring at node 4 |
| `Mat11Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for upper bar-slip spring at node 4 |
| `Mat12Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface-shear spring at node 4 |
| `Mat13Tag` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for shear-panel |
| `eleHeightFac` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value (as a ratio to the total height of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0) |
| `eleWidthFac` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value (as a ratio to the total width of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/BeamColumnJoint_Element)
