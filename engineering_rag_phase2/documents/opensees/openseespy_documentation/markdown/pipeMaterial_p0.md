<!-- chunk_id: pipeMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pipeMaterial.html",
 "title": "4.14.5.42. Pipe Material",
 "category": "material",
 "command": "pipeMaterial",
 "doc_section": "src",
 "rel_path": "src/pipeMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1256,
 "word_count": 145,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.42. Pipe Material

**uniaxialMaterial(*'Pipe'*, *matTag*, *nt*, *T1*, *E1*, *xnu1*, *alpT1*, *<T2*, *E2*, *xnu2*, *alpT2*, *... >*)**

The pipe material should be used with [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html) for pipes.
The material is defined with nt temperature points, each of which defines a set of parameters.
The actual material properties are interpolated based on the average temperature of the element.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `nt` ([float](https://docs.python.org/3/library/functions.html#float)) | the number of temperature points for the material. If two or more points are provided, the expected range of average temperatures in the element must be covered. |
| `T1` ([float](https://docs.python.org/3/library/functions.html#float)) | the temperature for point 1 |
| `E1` ([float](https://docs.python.org/3/library/functions.html#float)) | the Young’s modulus for point 1 |
| `xnu1` ([float](https://docs.python.org/3/library/functions.html#float)) | the Poisson’s ratio for point 1 |
| `alpT1` ([float](https://docs.python.org/3/library/functions.html#float)) | the thermal expansion coefficient for point 1 |
