<!-- chunk_id: Joint2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Joint2D.html",
 "title": "4.2.4.3. Joint2D Element",
 "category": "element",
 "command": "Joint2D",
 "doc_section": "src",
 "rel_path": "src/Joint2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3236,
 "word_count": 398,
 "has_code": false,
 "has_table": true
} -->

## 4.2.4.3. Joint2D Element

This command is used to construct a two-dimensional beam-column-joint element object. The two dimensional beam-column joint is idealized as a parallelogram shaped shear panel with adjacent elements connected to its mid-points. The midpoints of the parallelogram are referred to as external nodes. These nodes are the only analysis components that connect the joint element to the surrounding structure.

**element(*'Joint2D'*, *eleTag*, **eleNodes*, *<Mat1*, *Mat2*, *Mat3*, *Mat4>*, *MatC*, *LrgDspTag*, *<'-damage'*, *DmgTag>*, *<'-damage'*, *Dmg1 Dmg2 Dmg3 Dmg4 DmgC>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of five element nodes = `[nd1,nd2,nd3,nd4,ndC]`. `ndC` is the central node of beam-column joint. (the tag `ndC` is used to generate the internal node, thus, the node should not exist in the domain or be used by any other node) |
| `Mat1` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface rotational spring at node 1. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional) |
| `Mat2` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface rotational spring at node 2. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional) |
| `Mat3` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface rotational spring at node 3. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional) |
| `Mat4` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for interface rotational spring at node 4. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional) |
| `MatC` ([int](https://docs.python.org/3/library/functions.html#int)) | uniaxial material tag for rotational spring of the central node that describes shear panel behavior |
| `LrgDspTag` ([int](https://docs.python.org/3/library/functions.html#int)) | an integer indicating the flag for considering large deformations: * `0` - for small deformations and constant geometry * `1` - for large deformations and time varying geometry * `2` - for large deformations ,time varying geometry and length correction |
| `DmgTag` ([int](https://docs.python.org/3/library/functions.html#int)) | damage model tag |
| `Dmg1` ([int](https://docs.python.org/3/library/functions.html#int)) | damage model tag for Mat1 |
| `Dmg2` ([int](https://docs.python.org/3/library/functions.html#int)) | damage model tag for Mat2 |
| `Dmg3` ([int](https://docs.python.org/3/library/functions.html#int)) | damage model tag for Mat3 |
| `Dmg4` ([int](https://docs.python.org/3/library/functions.html#int)) | damage model tag for Mat4 |
| `DmgC` ([int](https://docs.python.org/3/library/functions.html#int)) | panel damage model tag |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Joint2D_Element)
