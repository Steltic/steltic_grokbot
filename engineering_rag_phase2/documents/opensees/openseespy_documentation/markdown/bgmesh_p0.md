<!-- chunk_id: bgmesh_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bgmesh.html",
 "title": "8.1.6. background mesh",
 "category": "general",
 "command": "bgmesh",
 "doc_section": "src",
 "rel_path": "src/bgmesh.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2122,
 "word_count": 211,
 "has_code": false,
 "has_table": true
} -->

## 8.1.6. background mesh

**mesh(*'bg'*, *basicsize*, **lower*, **upper*, *'-tol'*, *tol*, *'-meshtol'*, *meshtol*, *'-wave'*, *wavefilename*, *numl*, **locations*, *'-numsub'*, *numsub*, *'-structure'*, *id*, *numnodes*, **snodes*)**

Create a background mesh.

| `basicsize` ([float](https://docs.python.org/3/library/functions.html#float)) | basic mesh size |
| --- | --- |
| `lower` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of coordinates of the lower point of the background region. |
| `upper` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of coordinates of the uuper point of the background region. |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance for intri check. (optional, default 1e-10) |
| `meshtol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance for cell boundary check. (optional, default 0.1) |
| `wavefilename` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | a filename to record wave heights and velocities (optional) the recorded data are in the following format for columns: `time vx vy <vz> xmin xmax ymin ymax <zmin zmax> dt` |
| `numl` ([int](https://docs.python.org/3/library/functions.html#int)) | number of locations to record wave (optional) |
| `locations` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | coordinates of the locations (optional) |
| `id` ([int](https://docs.python.org/3/library/functions.html#int)) | structural id used to identify FSI and SSI (solid-solid-interaction) `id` = 0 : ignore the structure `id` > 0 : both FSI and SSI `id` < 0 : only SSI |
| `numsnodes` ([int](https://docs.python.org/3/library/functions.html#int)) | number of structural nodes (optional) |
| `sNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of structural nodes (optional) |
