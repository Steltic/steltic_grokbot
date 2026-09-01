<!-- chunk_id: zeroLengthSection_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLengthSection.html",
 "title": "3.1.10.2. ZeroLength Section Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "zeroLengthSection",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/zeroLengthSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2605,
 "word_count": 442,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.2. ZeroLength Section Element

This command is used to construct a zero length element object, which is defined by two nodes at the same location. The nodes are connected by a single section object to represent the force-deformation relationship for the element.

**element zeroLengthSection $eleTag $iNode $jNode $secTag <-orient $x1 $x2 $x3 $yp1 $yp2 $yp3> <-doRayleigh $rFlag>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | unique element object tag |
| $endNodes | *list integer* | 2 end nodes |
| $secTag | *integer* | tag associated with previously-defined Section object |
| $x | *list float* | (optional) 3 components in global coordinates defining local x-axis |
| $yp | *list float* | (optional) 3 components in global coordinates defining vector yp which lies in the local x-y plane for the element. |
| $rFlag | *integer* | optional, default = 0 rFlag = 0 NO RAYLEIGH DAMPING (default) rFlag = 1 include rayleigh damping |

Note

If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

The section force-deformation response represented by section string P acts along the element local x-axis, and the response for code Vy along the local y-axis. The other modes of section response follow from this orientation.

The valid queries to a zero-length element when creating an ElementRecorder object are ‘force,’ ‘deformation,’ ‘stiff,’ and ‘section $secArg1 secArg2 …’.

Warning

If the distance between end noes is not **0.0** a warning message will appear when the script is run. This is just a warning in case you have made a mistake as most users when they use zeroLength elements are wanting to use them in the more normal way. ZeroLength elements can be used between nodes with non-zero length.

Example

The following examples demonstrate the commands in a script to add three zeroLength elements to domain. The three to be added have element tags **1**, **2**, and **3**. Element **1** has nodes **2** and **3** as its end ndes, has two materials **5** and **6** acting in directions **1** and **2**. Element **2** has as its end nodes **4** and **5**, has only one material **1** acting in direction **1**, the element has a global orientation.

1. **Tcl Code**

```
element zeroLengthSection 1 2 4 6
element zeroLengthSection 2 4 5 6 -orient 1 1 0 -1 1 0
element zeroLengthSection 2 4 5 6 -orient 1 1 0 -1 1 0 -doRayleigh 1
```

Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott)
