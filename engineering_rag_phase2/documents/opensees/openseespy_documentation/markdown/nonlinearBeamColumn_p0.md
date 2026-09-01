<!-- chunk_id: nonlinearBeamColumn_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nonlinearBeamColumn.html",
 "title": "4.2.3.7. nonlinearBeamColumn",
 "category": "general",
 "command": "nonlinearBeamColumn",
 "doc_section": "src",
 "rel_path": "src/nonlinearBeamColumn.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1530,
 "word_count": 137,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.7. nonlinearBeamColumn

**element(*'nonlinearBeamColumn'*, *eleTag*, **eleNodes*, *numIntgrPts*, *secTag*, *transfTag*, *'-iter'*, *maxIter=10*, *tol=1e-12*, *'-mass'*, *mass=0.0*, *'-integration'*, *intType*)**

Create a nonlinearBeamColumn element. This element is for backward compatability.

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the element |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `numIntgrPts` ([int](https://docs.python.org/3/library/functions.html#int)) | number of integration points. |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of section |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of transformation |
| `maxIter` ([int](https://docs.python.org/3/library/functions.html#int)) | maximum number of iterations to undertake to satisfy element compatibility (optional) |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | tolerance for satisfaction of element compatibility (optional) |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass density (per unit length), from which a lumped-mass matrix is formed (optional) |
| `intType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | integration type (optional, default is `'Lobatto'`) `'Lobatto'` `'Legendre'` `'Radau'` `'NewtonCotes'` `'Trapezoidal'` |
