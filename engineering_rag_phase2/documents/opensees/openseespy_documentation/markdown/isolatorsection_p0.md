<!-- chunk_id: isolatorsection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/isolatorsection.html",
 "title": "4.16.14. Isolator2spring Section",
 "category": "section",
 "command": "isolatorsection",
 "doc_section": "src",
 "rel_path": "src/isolatorsection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1757,
 "word_count": 189,
 "has_code": false,
 "has_table": true
} -->

## 4.16.14. Isolator2spring Section

**section(*'Isolator2spring'*, *matTag*, *tol*, *k1*, *Fyo*, *k2o*, *kvo*, *hb*, *PE*, *Po=0.0*)**

This command is used to construct an Isolator2spring section object, which represents the buckling behavior of an elastomeric bearing for two-dimensional analysis in the lateral and vertical plane. An Isolator2spring section represents the resultant force-deformation behavior of the bearing, and should be used with a zeroLengthSection element. The bearing should be constrained against rotation.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance for convergence of the element state. Suggested value: E-12 to E-10. OpenSees will warn if convergence is not achieved, however this usually does not prevent global convergence. |
| `k1` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stiffness for lateral force-deformation |
| `Fyo` ([float](https://docs.python.org/3/library/functions.html#float)) | nominal yield strength for lateral force-deformation |
| `k2o` ([float](https://docs.python.org/3/library/functions.html#float)) | nominal postyield stiffness for lateral force-deformation |
| `kvo` ([float](https://docs.python.org/3/library/functions.html#float)) | nominal stiffness in the vertical direction |
| `hb` ([float](https://docs.python.org/3/library/functions.html#float)) | total height of elastomeric bearing |
| `PE` ([float](https://docs.python.org/3/library/functions.html#float)) | Euler Buckling load for the bearing |
| `Po` ([float](https://docs.python.org/3/library/functions.html#float)) | axial load at which nominal yield strength is achieved (optional) |
