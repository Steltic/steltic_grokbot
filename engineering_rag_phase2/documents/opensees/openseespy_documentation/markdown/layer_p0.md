<!-- chunk_id: layer_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/layer.html",
 "title": "4.16.2.3. Layer Command",
 "category": "general",
 "command": "layer",
 "doc_section": "src",
 "rel_path": "src/layer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3578,
 "word_count": 366,
 "has_code": false,
 "has_table": true
} -->

## 4.16.2.3. Layer Command

**layer(*type*, **args*)**

The layer command is used to generate a number of fibers along a line or a circular arc.

**layer(*'straight'*, *matTag*, *numFiber*, *areaFiber*, **start*, **end*)**

This command is used to construct a straight line of fibers

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numFiber` ([int](https://docs.python.org/3/library/functions.html#int)) | number of fibers along line |
| `areaFiber` ([float](https://docs.python.org/3/library/functions.html#float)) | area of each fiber |
| `start` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of first fiber in line (local coordinate system) |
| `end` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of last fiber in line (local coordinate system) |

**layer(*'circ', matTag,numFiber,areaFiber,*center,radius,*ang=[0.0,360.0-360/numFiber]*)**

This command is used to construct a line of fibers along a circular arc

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numFiber` ([int](https://docs.python.org/3/library/functions.html#int)) | number of fibers along line |
| `areaFiber` ([float](https://docs.python.org/3/library/functions.html#float)) | area of each fiber |
| `center` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of center of circular arc |
| `radius` ([float](https://docs.python.org/3/library/functions.html#float)) | radius of circlular arc |
| `ang` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | starting and ending angle (optional) |

**layer(*'rect'*, *matTag*, *numFiberY*, *numFiberZ*, *areaFiber*, **center*, *distY*, *distZ*)**

This command is used to construct a line of fibers around a rectangle with specified center coordinate, extending +/-distY/2 and +/-distZ/2 from center. If numFiberY and numFiberZ are zero, there will be four corner fibers. The total number of fibers is 4+2*numFiberY+2*numFiberZ.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numFiberY` ([int](https://docs.python.org/3/library/functions.html#int)) | number of intermediate fibers on each side along Y-direction |
| `numFiberZ` ([int](https://docs.python.org/3/library/functions.html#int)) | number of intermediate fibers on each side along Z-direction |
| `areaFiber` ([float](https://docs.python.org/3/library/functions.html#float)) | area of each fiber |
| `center` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of center of rectangle |
| `distY` ([float](https://docs.python.org/3/library/functions.html#float)) | height of rectangle in Y-direction |
| `distZ` ([float](https://docs.python.org/3/library/functions.html#float)) | width of rectangle in Z-direction |
