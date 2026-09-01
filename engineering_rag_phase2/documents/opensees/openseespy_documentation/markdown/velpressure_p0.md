<!-- chunk_id: velpressure_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/velpressure.html",
 "title": "4.17.4. Velocity and Pressure Dependent Friction",
 "category": "general",
 "command": "velpressure",
 "doc_section": "src",
 "rel_path": "src/velpressure.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1042,
 "word_count": 98,
 "has_code": false,
 "has_table": true
} -->

## 4.17.4. Velocity and Pressure Dependent Friction

**frictionModel(*'VelPressureDep'*, *frnTag*, *muSlow*, *muFast0*, *A*, *deltaMu*, *alpha*, *transRate*)**

This command is used to construct a VelPressureDep friction model object.

| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique friction model tag |
| --- | --- |
| `muSlow` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of friction at low velocity |
| `muFast0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial coefficient of friction at high velocity |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | nominal contact area |
| `deltaMu` ([float](https://docs.python.org/3/library/functions.html#float)) | pressure parameter calibrated from experimental data |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | pressure parameter calibrated from experimental data |
| `transRate` ([float](https://docs.python.org/3/library/functions.html#float)) | transition rate from low to high velocity |
