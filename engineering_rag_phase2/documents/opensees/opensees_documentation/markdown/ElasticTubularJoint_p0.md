<!-- chunk_id: ElasticTubularJoint_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/ElasticTubularJoint.html",
 "title": "3.1.10.25. ElasticTubularJoint Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "ElasticTubularJoint",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/ElasticTubularJoint.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2288,
 "word_count": 338,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.25. ElasticTubularJoint Element

This command is used to construct an ElasticTubularJoint element object, which models joint flexibility of tubular joints in two dimensional analysis of any structure having tubular joints.

#### 3.1.10.25.1. Command Lines

TCL:

**element ElasticTubularJoint $eleTag $iNode $jNode $Brace_Diameter $Brace_Angle $E $Chord_Diameter $Chord_Thickness $Chord_Angle**

Python:

**element(*'ElasticTubularJoint'*, *eleTag*, *iNode*, *jNode*, *Brace_Diameter*, *Brace_Angle*, *E*, *Chord_Diameter*, *Chord_Thickness*, *Chord_Angle*)**

where:

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | Unique element object tag |
| $iNode | *integer* | First end node- it is always located on the chord axis |
| $jNode | *integer* | Second end node - it is always located on the chord wall |
| $Brace_Diameter | *float* | Outer diameter of brace |
| $Brace_Angle | *float* | Angle between brace and chord axis 0 < Brace_Angle < 90 |
| $E | *float* | Young’s Modulus |
| $Chord_Diameter | *float* | Outer diameter of chord |
| $Chord_Thickness | *float* | Thickness of chord |
| $Chord_Angle | *float* | Angle between chord axis and global x-axis 0 < Chord_Angle < 180 |

#### 3.1.10.25.2. Examples

Command Lines

The following example constructs constructs a ElasticTubularJoint joint element with element tag *1*, that is connected to nodes *1* and *2*. The brace diameter is *0.25* m, intersection angle is *45* degrees, Young’s modulus is *210e9*, outer diameter and thickness of the chord are *0.50* m and *0.016* m respectively, and angle between chord axis and global horizontal axis is *45* degrees.

1. **Tcl**

```
element ElasticTubularJoint 1 1 2 0.25 45 210E+09 0.5 0.016 45;
```

1. **Python**

```
element('ElasticTubularJoint', 1, 1, 2, 0.25, 45, 210E+09, 0.5, 0.016, 45)
```

References

More information available in the following reference:

1. Alanjari, P., Asgarian, B., & Salari, N. (2015). Elastic tubular joint element for modelling of multi-brace, uni-planar tubular connections. Ships and Offshore Structures, 10(4), 404–415. [https://doi.org/10.1080/17445302.2014.942077](https://doi.org/10.1080/17445302.2014.942077)

Code developed by: M. Kia and P. Alanjari, Sharif University of Technology and K. N. Toosi University of Technology, Tehran, Iran.
