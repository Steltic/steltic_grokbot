<!-- chunk_id: TenNodeTetrahedron_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/TenNodeTetrahedron.html",
 "title": "3.1.10.23. TenNodeTetrahedron Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "TenNodeTetrahedron",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/TenNodeTetrahedron.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2186,
 "word_count": 324,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.23. TenNodeTetrahedron Element

This command is used to construct an ten-node tetrahedron element object, which uses the standard isoparametric formulation.

Command

**element TenNodeTetrahedron $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $node9 $node10 $matTag <$b1 $b2 $b3> <doInitDisp?> **

| Argument | Type | Description |
| --- | --- | --- | --- | --- |
| $eleTag | *integer* | unique element object tag |
| $node1 .. $node10 | 10 *integer* | nodes of tet (ordered as shown in fig below) |
| $matTag | *integer* | tag of nDMaterial |
| $b1 $b2 $b3 | *list float* | optional: body forces in global x y z directions |
| <-doInitDisp $value> | \|bool\| | optional: consider initial displacements if $value is 0 |

This element is based on second-order interpolation of nodal quantities, this means that the strain and stress field inside the element are linearly interpolated. Four Gauss-points inside the element are used for integration.

Fig. 3.1.10.24 TenNodeTetrahedron Element Node Numbering

Note

The valid queries to a TenNodeTetrahedron element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ (‘strains’ version > 2.2.0) and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

This element can only be defined after a [model Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/model.html#model) with **-ndm 3 -ndf 3**

Example

The following example constructs a TenNodeTetrahedron element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8, 9, 10** with an nDMaterial of tag **1** and body forces given by varaiables **b1, b2, b3**.

1. **Tcl Code**

```
element TenNodeTetrahedron 1 1 2 3 4 5 6 7 8 9 10 1 $b1 $b2 $b3
```

1. **Python Code**

```
element('TenNodeTetrahedron',1, 1,2,3,4,5,6,7,8,9,10, 1, b1, b2, b3)
```

Code Developed by: [José Antonio Abell](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/www.joseabell.com) and José Luis Larenas (UANDES). For bugs and features, start a new issue on the [OpenSees github repo](https://github.com/OpenSees/OpenSees) and tag me (@jaabell).
