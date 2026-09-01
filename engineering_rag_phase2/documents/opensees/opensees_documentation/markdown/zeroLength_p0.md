<!-- chunk_id: zeroLength_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/zeroLength.html",
 "title": "3.1.10.1. ZeroLength Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "zeroLength",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/zeroLength.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2239,
 "word_count": 371,
 "has_code": false,
 "has_table": true
} -->

## 3.1.10.1. ZeroLength Element

This command is used to construct a zeroLength element object, which is defined by two nodes at the same location. A zeroLength element is similar to a set of springs placed between two nodes, each spring providing the force displacement relationship for a specified degree-of-freedom. The nodes are connected by multiple UniaxialMaterial objects, which provide the force-deformation relationship for the element in that degree-of-freedom direction.

**element zeroLength $eleTag $iNode $jNode -mat $matTag -dir $dir <-doRayleigh $rFlag> <-orient $x $yp>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | *integer* | unique element object tag |
| $endNodes | *list integer* | 2 end nodes |
| $matTags | *list integer* | list of **n** material tags |
| $dirIDs | *list integer* | list of **n** degree-of-freedom directions 1,2,3 - translation along local x,y,z axes, 4,5,6 - rotation about local x,y,z axes |
| $x | *list float* | (optional) 3 components in global coordinates defining local x-axis |
| $yp | *list float* | (optional) 3 components in global coordinates defining vector yp which lies in the local x-y plane for the element. |
| $rFlag | *integer* | optional, default = 0 rFlag = 0 NO RAYLEIGH DAMPING (default) rFlag = 1 include rayleigh damping |

Note

If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

The valid queries to a zero-length element when creating an ElementRecorder object are ‘force,’ ‘deformation,’ and ‘material $i matArg1 matArg2 …’ Where $i is an integer indicating which of the materials whose data is to be output (a 1 corresponds to $matTag1, a 2 to $matTag2, and so on).

Warning

If the distance between end noes is not **0.0** a warning message will appear when the script is run. This is just a warning in case you have made a mistake as most users when they use zeroLength elements are wanting to use them in the more normal way. ZeroLength elements can be used between nodes with non-zero length.

Code Developed by: [Gregory L. Fenves](http://www.caee.utexas.edu/faculty/directory/fenves)
