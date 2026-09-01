<!-- chunk_id: ForceBeamColumn_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html",
 "title": "4.2.3.6. forceBeamColumn",
 "category": "general",
 "command": "ForceBeamColumn",
 "doc_section": "src",
 "rel_path": "src/ForceBeamColumn.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1245,
 "word_count": 103,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.6. forceBeamColumn

**element(*'forceBeamColumn'*, *eleTag*, **eleNodes*, *transfTag*, *integrationTag*, *'-iter'*, *maxIter=10*, *tol=1e-12*, *'-mass'*, *mass=0.0*)**

Create a ForceBeamColumn element.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the element |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of transformation |
| `integrationTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of [`beamIntegration()`](https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html#beamIntegration) |
| `maxIter` ([int](https://docs.python.org/3/library/functions.html#int)) | maximum number of iterations to undertake to satisfy element compatibility (optional) |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance for satisfaction of element compatibility (optional) |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass density (per unit length), from which a lumped-mass matrix is formed (optional) |
