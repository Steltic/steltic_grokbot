<!-- chunk_id: zeroLengthSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthSection.html",
 "title": "4.2.1.3. zeroLengthSection Element",
 "category": "element",
 "command": "zeroLengthSection",
 "doc_section": "src",
 "rel_path": "src/zeroLengthSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1551,
 "word_count": 155,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.3. zeroLengthSection Element

**element(*'zeroLengthSection'*, *eleTag*, **eleNodes*, *secTag*, *<'-orient'*, **vecx*, **vecyp>*, *<'-doRayleigh'*, *rFlag>*)**

This command is used to construct a zero length element object, which is defined by two nodes at the same location. The nodes are connected by a single section object to represent the force-deformation relationship for the element.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined Section object |
| `vecx` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining local x-axis (optional) |
| `vecyp` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional) |
| `rFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = 0 `rFlag` = 0 NO RAYLEIGH DAMPING (default) `rFlag` = 1 include rayleigh damping |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ZeroLengthSection_Element)
