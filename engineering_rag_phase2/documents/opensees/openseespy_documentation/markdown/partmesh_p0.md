<!-- chunk_id: partmesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/partmesh.html",
 "title": "8.1.5. particle mesh",
 "category": "general",
 "command": "partmesh",
 "doc_section": "src",
 "rel_path": "src/partmesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2676,
 "word_count": 311,
 "has_code": false,
 "has_table": true
} -->

## 8.1.5. particle mesh

**mesh(*'part'*, *tag*, *type*, **pArgs*, *eleType=''*, **eleArgs=[]*, *'-vel'*, **vel0*, *'-pressure'*, *p0*)**

Create or return a group of particles which will be used for background mesh.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | mesh tag. |
| --- | --- |
| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | type of the mesh |
| `pArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | coordinates of points defining the mesh region `nx`, `ny`, `nz` are number of particles in x, y, and z directions `'quad'` : [x1, y1, x2, y2, x3, y3, x4, y4, nx, ny] Coordinates of four corners in counter-clock wise order. `'cube'` : [x1, y1, z1, x2, y2, z2, nx, ny, nz] Coordinates of two opposite, diagonal corners at bottom and at top of the cube `'tri'` : [x1, y1, x2, y2, x3, y3, nx, ny] Coordinates of three corners in counter-clock wise order `'line'` : [x1, y1, x2, y2, nx] Coordinates of two ends in counter-clock wise order `'pointlist'`[num, x1n, y1n, <z1n>, x1, y1, <z1>, vx1, vy1, <vz1>,ax1, ay1, <az1>, p1, x2n, y2n, <z2n>, x2, y2, <z2>, vx2, vy2, <vz2>, ax2, ay2, <az2>, p2, ..] input particles’ data in a list, in the order of number of particles, coordinates of last time step, current coordinates, velocity, acceleration, and pressure. `'pointlist'` without list return a list of current particles’ data in this mesh [tag1, x1, y1, <z1>, vx1, vy1, <vz1>, ax1, ay1, <az1>, p1, tag2, x2, y2, <z2>, vx2, vy2, <vz2>, ax2, ay2, <az2>, p2, ..] The format is similar to the input list, but with an additional tag for each particle. |
| `eleType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the element type, (optional) [PFEMElementBubble](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementBubble.html) [PFEMElementCompressible](https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementCompressible.html) [Tri31 Element](https://openseespydoc.readthedocs.io/en/latest/src/tri31.html) if no type is given, only nodes are created |
| `eleArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of element arguments. (optional, see [line mesh](https://openseespydoc.readthedocs.io/en/latest/src/linemesh.html) and [triangular mesh](https://openseespydoc.readthedocs.io/en/latest/src/trimesh.html)) |
| `vel0` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of initial velocities. (optional) |
| `p0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial pressure. (optional) |
