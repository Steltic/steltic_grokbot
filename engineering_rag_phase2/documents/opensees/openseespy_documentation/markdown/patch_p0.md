<!-- chunk_id: patch_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/patch.html",
 "title": "4.16.2.2. Patch Command",
 "category": "general",
 "command": "patch",
 "doc_section": "src",
 "rel_path": "src/patch.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4259,
 "word_count": 433,
 "has_code": false,
 "has_table": true
} -->

## 4.16.2.2. Patch Command

**patch(*type*, **args*)**

The patch command is used to generate a number of fibers over a cross-sectional area. Currently there are three types of cross-section that fibers can be generated: quadrilateral, rectangular and circular.

**patch(*'quad'*, *matTag*, *numSubdivIJ*, *numSubdivJK*, **crdsI*, **crdsJ*, **crdsK*, **crdsL*)**

This is the command to generate a quadrilateral shaped patch (the geometry of the patch is defined by four vertices: I J K L. The coordinates of each of the four vertices is specified in COUNTER CLOCKWISE sequence)

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numSubdivIJ` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in the IJ direction. |
| `numSubdivJK` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in the JK direction. |
| `crdsI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex I (local coordinate system) |
| `crdsJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex J (local coordinate system) |
| `crdsK` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex K (local coordinate system) |
| `crdsL` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex L (local coordinate system) |

**patch(*'rect'*, *matTag*, *numSubdivY*, *numSubdivZ*, **crdsI*, **crdsJ*)**

This is the command to generate a rectangular patch. The geometry of the patch is defined by coordinates of vertices: I and J. To ensure positive fiber areas are created, (zJ-zI)/(yJ-yI) should be positive.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numSubdivY` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in local y direction. |
| `numSubdivZ` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in local z direction. |
| `crdsI` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex I (local coordinate system) |
| `crdsJ` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of vertex J (local coordinate system) |

**patch(*'circ'*, *matTag*, *numSubdivCirc*, *numSubdivRad*, **center*, **rad*, **ang*)**

This is the command to generate a circular shaped patch

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | material tag associated with this fiber (UniaxialMaterial tag for a FiberSection and NDMaterial tag for use in an NDFiberSection). |
| --- | --- |
| `numSubdivCirc` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in the circumferential direction (number of wedges) |
| `numSubdivRad` ([int](https://docs.python.org/3/library/functions.html#int)) | number of subdivisions (fibers) in the radial direction (number of rings) |
| `center` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | y & z-coordinates of the center of the circle |
| `rad` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | internal & external radius |
| `ang` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | starting & ending-coordinates angles (degrees) |
