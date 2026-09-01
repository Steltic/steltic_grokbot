<!-- chunk_id: dispBeamColumn_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/dispBeamColumn.html",
 "title": "4.2.3.5. dispBeamColumn",
 "category": "general",
 "command": "dispBeamColumn",
 "doc_section": "src",
 "rel_path": "src/dispBeamColumn.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 995,
 "word_count": 87,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.5. dispBeamColumn

**element(*'dispBeamColumn'*, *eleTag*, **eleNodes*, *transfTag*, *integrationTag*, *'-cMass'*, *'-mass'*, *mass=0.0*)**

Create a dispBeamColumn element.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the element |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | list of two node tags |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of transformation |
| `integrationTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of [`beamIntegration()`](https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html#beamIntegration) |
| `'-cMass'` | to form consistent mass matrix (optional, default = lumped mass matrix) |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass density (per unit length), from which a lumped-mass matrix is formed (optional) |
