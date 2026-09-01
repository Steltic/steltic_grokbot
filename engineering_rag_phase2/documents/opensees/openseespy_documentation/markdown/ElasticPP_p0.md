<!-- chunk_id: ElasticPP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticPP.html",
 "title": "4.14.3.2. Elastic-Perfectly Plastic Material",
 "category": "material",
 "command": "ElasticPP",
 "doc_section": "src",
 "rel_path": "src/ElasticPP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 952,
 "word_count": 88,
 "has_code": false,
 "has_table": true
} -->

## 4.14.3.2. Elastic-Perfectly Plastic Material

**uniaxialMaterial(*'ElasticPP'*, *matTag*, *E*, *epsyP*, *epsyN=epsyP*, *eps0=0.0*)**

This command is used to construct an elastic perfectly-plastic uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | tangent |
| `epsyP` ([float](https://docs.python.org/3/library/functions.html#float)) | strain or deformation at which material reaches plastic state in tension |
| `epsyN` ([float](https://docs.python.org/3/library/functions.html#float)) | strain or deformation at which material reaches plastic state in compression. (optional, default is tension value) |
| `eps0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial strain (optional, default: zero) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Material)
