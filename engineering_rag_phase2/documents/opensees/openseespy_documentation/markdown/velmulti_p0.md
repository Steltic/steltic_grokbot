<!-- chunk_id: velmulti_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/velmulti.html",
 "title": "4.17.5. Multi-Linear Velocity Dependent Friction",
 "category": "general",
 "command": "velmulti",
 "doc_section": "src",
 "rel_path": "src/velmulti.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1133,
 "word_count": 129,
 "has_code": false,
 "has_table": true
} -->

## 4.17.5. Multi-Linear Velocity Dependent Friction

**frictionModel(*'VelDepMultiLinear'*, *frnTag*, *'-vel'*, **velPoints*, *'-frn'*, **frnPoints*)**

This command is used to construct a VelDepMultiLinear friction model object. The friction-velocity relationship is given by a multi-linear curve that is define by a set of points. The slope given by the last two specified points on the positive velocity axis is extrapolated to infinite positive velocities. Velocity and friction points need to be equal or larger than zero (no negative values should be defined). The number of provided velocity points needs to be equal to the number of provided friction points.

| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique friction model tag |
| --- | --- |
| `velPoints` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | list of velocity points along friction-velocity curve |
| `frnPoints` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | list of friction points along friction-velocity curve |
