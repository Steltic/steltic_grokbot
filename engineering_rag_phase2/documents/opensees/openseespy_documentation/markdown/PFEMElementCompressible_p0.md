<!-- chunk_id: PFEMElementCompressible_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PFEMElementCompressible.html",
 "title": "4.2.15.2. PFEMElementCompressible",
 "category": "element",
 "command": "PFEMElementCompressible",
 "doc_section": "src",
 "rel_path": "src/PFEMElementCompressible.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1137,
 "word_count": 106,
 "has_code": false,
 "has_table": true
} -->

## 4.2.15.2. PFEMElementCompressible

**element(*'PFEMElementCompressible'*, *eleTag*, **eleNodes*, *rho*, *mu*, *b1*, *b2*, *<thickness*, *kappa>*)**

Create a PFEM compressible element, which is a fluid element for FSI analysis.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the element |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | A list of four element nodes, last one is middle node |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid density |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid viscosity |
| `b1` ([float](https://docs.python.org/3/library/functions.html#float)) | body body acceleration in x direction |
| `b2` ([float](https://docs.python.org/3/library/functions.html#float)) | body body acceleration in y direction |
| `thickness` ([float](https://docs.python.org/3/library/functions.html#float)) | element thickness (optional) |
| `kappa` ([float](https://docs.python.org/3/library/functions.html#float)) | fluid bulk modulus (optional) |
