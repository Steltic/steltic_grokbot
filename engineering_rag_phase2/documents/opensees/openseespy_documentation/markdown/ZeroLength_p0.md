<!-- chunk_id: ZeroLength_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ZeroLength.html",
 "title": "4.2.1.1. zeroLength Element",
 "category": "element",
 "command": "ZeroLength",
 "doc_section": "src",
 "rel_path": "src/ZeroLength.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2160,
 "word_count": 221,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.1. zeroLength Element

**element(*'zeroLength'*, *eleTag*, **eleNodes*, *'-mat'*, **matTags*, *'-dir'*, **dirs*, *<'-doRayleigh'*, *rFlag=0>*, *<'-orient'*, **vecx*, **vecyp>*)**

This command is used to construct a zeroLength element object, which is defined by two nodes at the same location. The nodes are connected by multiple UniaxialMaterial objects to represent the force-deformation relationship for the element.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `matTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of tags associated with previously-defined UniaxialMaterials |
| `dirs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of material directions: 1,2,3 - translation along local x,y,z axes, respectively; 4,5,6 - rotation about local x,y,z axes, respectively |
| `rFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = 0 NO RAYLEIGH DAMPING (default), 1 include Rayleigh damping |
| `vecx` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining local x-axis (optional) |
| `vecyp` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional) |

Note

If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ZeroLength_Element)
