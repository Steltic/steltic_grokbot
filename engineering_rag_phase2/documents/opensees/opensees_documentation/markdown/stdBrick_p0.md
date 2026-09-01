<!-- chunk_id: stdBrick_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/stdBrick.html",
 "title": "3.1.10.19. stdBrick Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "stdBrick",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/stdBrick.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1500,
 "word_count": 242,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.19. stdBrick Element

This command is used to construct an eight-node brick element object, which uses the standard isoparametric formulation.

Command

**element stdBrick $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $matTag <$b1 $b2 $b3>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | unique element object tag |
| $node1 .. $node8 | 8 *integer* | nodes of brick (ordered as shown in fig below) |
| $matTag | *integer* | tag of nDMaterial |
| $b1 $b2 $b3 | *list float* | optional: body forces in global x y z directions |

Fig. 3.1.10.20 stdBrick Element Node Numbering

Note

The valid queries to a Brick element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ (‘strains’ version > 2.2.0) and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

This element can only be defined after a [Section 3.1.1](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/model.html#model) with **-ndm 3 -ndf 3**

Example

The following example constructs a brick element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8** with an nDMaterial of tag **1** and body forces given by varaiables **b1, b2, b3**.

1. **Tcl Code**

```
element stdBrick 1 1 2 3 4 5 6 7 8 1 $b1 $b2 $b3
```

1. **Python Code**

```
element('stdBrick',1,1,2,3,4,5,6,7,8,1, b1, b2, b3)
```

Code Developed by: **Edward Love, Sandia National Laboratories**
