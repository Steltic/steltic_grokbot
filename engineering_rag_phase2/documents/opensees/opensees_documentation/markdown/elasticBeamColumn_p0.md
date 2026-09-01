<!-- chunk_id: elasticBeamColumn_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/elasticBeamColumn.html",
 "title": "3.1.10.5. Elastic Beam Column Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "elasticBeamColumn",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/elasticBeamColumn.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2250,
 "word_count": 354,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.5. Elastic Beam Column Element

This command is used to construct an elasticBeamColumn element object. The arguments for the construction of an elastic beam-column element depend on the dimension of the problem, ndm:

For a two-dimensional problem:

**element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-release $relcode> <-mass $massDens> <-cMass>**

**element elasticBeamColumn $eleTag $iNode $jNode $secTag $transfTag <-release $relcode> <-mass $massDens> <-cMass>**

For a three-dimensional problem:

**element elasticBeamColumn $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $transfTag <-releasez $relcode> <-releasey $relcode> <-mass $massDens> <-cMass>**

**element elasticBeamColumn $eleTag $iNode $jNode $secTag $transfTag <-releasez $relcode> <-releasey $relcode> <-mass $massDens> <-cMass>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | Unique element object tag |
| $iNode $jNode | *integer* | End node tags |
| $A | *float* | Cross-sectional area of element |
| $E | *float* | Young’s Modulus |
| $G | *float* | Shear Modulus |
| $J | *float* | Torsional moment of inertia of cross section |
| $Iz | *float* | Second moment of area about the local z-axis |
| $Iy | *float* | Second moment of area about the local y-axis |
| $secTag | *integer* | Identifier for previously-defined section object |
| $transfTag | *integer* | Identifier for previously-defined coordinate-transformation object |
| $relcode | *integer* | Code for moment releases (0=no release, 1=release at end I, 2=release at end J, 3=release at both ends (optional, default = 0) |
| $massDens | *float* | Element mass per unit length (optional: default = 0.0) |
| -cMass | *string* | To form consistent mass matrix (optional) |

The valid queries to an elastic beam-column element when creating an ElementRecorder object are ‘force’.

Example

The following example constructs an elastic element with tag **1** between nodes **2** and **4** with an area of **5.5**, E of **100.0** and an Iz of **1e6** which uses the geometric transformation object with a tag of **9**

1. **Tcl Code**

```
element elasticBeamColumn 1 2 4 5.5 100.0 1e6 9;
```

1. **Python Code**

```
element('elasticBeamColumn',1,2,4,5.5,100.0, 1.0e6, 9)
```

Code developed by: **fmk**
