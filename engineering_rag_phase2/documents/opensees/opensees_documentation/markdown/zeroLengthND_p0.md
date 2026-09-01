<!-- chunk_id: zeroLengthND_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLengthND.html",
 "title": "3.1.10.3. ZeroLengthND Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "zeroLengthND",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/zeroLengthND.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2580,
 "word_count": 417,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.3. ZeroLengthND Element

This command is used to construct a zeroLengthND element object, which is defined by two nodes at the same location. The nodes are connected by a single NDMaterial object to represent the force-deformation relationship for the element.

**element zeroLengthND $eleTag $iNode $jNode $matTag <$uniTag> <-orient $x1 $x2 $x3 $yp1 $yp2 $yp3>**

| Argument | Type | Description |
| --- | --- | --- | --- |
| $eleTag | *integer* | unique element object tag |
| $nodes | intList\| | tags of two end nodes |
| $matTag | *integer* | tag associated with previously-defined ndMaterial object |
| $uniTag | *integer* | tag associated with previously-defined UniaxialMaterial object which may be used to represent uncoupled behavior orthogonal to the plane of the NDmaterial response. SEE NOTES 2 and 3. |
| $x | *list float* | vector components in global coordinates defining local x-axis (optional) |
| $yp | *list float* | vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional) |

Note

The zeroLengthND element only represents translational response between its nodes

If the NDMaterial object is of order two, the response lies in the element local x-y plane and the UniaxialMaterial object may be used to represent the uncoupled behavior orthogonal to this plane, i.e. along the local z-axis.

If the NDMaterial object is of order three, the response is along each of the element local exes.

If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

The valid queries to a zero-length element when creating an ElementRecorder object are ‘force’, ‘deformation’, and ‘material matArg1 matArg2 …’

Example

The following examples demonstrate the commands in a script to add three zeroLength elements to domain. The three to be added have element tags **1**, **2**, and **3**. Element **1** has nodes **2** and **3** as its end ndes, has two materials **5** and **6** acting in directions **1** and **2**. Element **2** has as its end nodes **4** and **5**, has only one material **1** acting in direction **1**, the element has a global orientation.

1. **Tcl Code**

```
element zeroLengthND 1 2 4 5
element zeroLengthND 2 4 5 5 1 -orient 1 1 0 -1 1 0
```

1. **Python Code**

```
element('zeroLength',1,2,4,5)
element('zeroLength',2,4,5,5, 1,'-orient',1,1,0,-1,1,0)
```

Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott)
