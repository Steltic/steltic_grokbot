<!-- chunk_id: ElasticBilin_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticBilin.html",
 "title": "4.14.5.18. ElasticBilin Material",
 "category": "material",
 "command": "ElasticBilin",
 "doc_section": "src",
 "rel_path": "src/ElasticBilin.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1430,
 "word_count": 154,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.18. ElasticBilin Material

**uniaxialMaterial(*'ElasticBilin'*, *matTag*, *EP1*, *EP2*, *epsP2*, *EN1=EP1*, *EN2=EP2*, *epsN2=-epsP2*)**

This command is used to construct an elastic bilinear uniaxial material object. Unlike all other bilinear materials, the unloading curve follows the loading curve exactly.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `EP1` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent in tension for stains: 0 <= strains <= `epsP2` |
| `EP2` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent when material in tension with strains > `epsP2` |
| `epsP2` ([float](https://docs.python.org/3/library/functions.html#float)) | strain at which material changes tangent in tension. |
| `EN1` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = `EP1`. tangent in compression for stains: 0 < strains <= `epsN2` |
| `EN2` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = `EP2`. tangent in compression with strains < `epsN2` |
| `epsN2` ([float](https://docs.python.org/3/library/functions.html#float)) | optional, default = `-epsP2`. strain at which material changes tangent in compression. |

Note

`eps0` can not be controlled. It is always zero.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ElasticBilin_Material)
