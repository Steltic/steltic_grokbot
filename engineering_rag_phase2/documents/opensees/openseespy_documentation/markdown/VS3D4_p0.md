<!-- chunk_id: VS3D4_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/VS3D4.html",
 "title": "4.2.16.2. VS3D4",
 "category": "general",
 "command": "VS3D4",
 "doc_section": "src",
 "rel_path": "src/VS3D4.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1457,
 "word_count": 145,
 "has_code": false,
 "has_table": true
} -->

## 4.2.16.2. VS3D4

This command is used to construct a four-node 3D viscous-spring boundary quad element object based on a bilinear isoparametric formulation.

**element(*'VS3D4'*, *eleTag*, **eleNodes*, *E*, *G*, *rho*, *R*, *alphaN*, *alphaT*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | 4 end nodes |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus of element material |
| `G` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear Modulus of element material |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | Mass Density of element material |
| `R` ([float](https://docs.python.org/3/library/functions.html#float)) | distance from the scattered wave source to the boundary |
| `alphaN` ([float](https://docs.python.org/3/library/functions.html#float)) | correction parameter in the normal direction |
| `alphaT` ([float](https://docs.python.org/3/library/functions.html#float)) | correction parameter in the tangential direction |

Note

Reference: Liu J, Du Y, Du X, et al. 3D viscous-spring artificial boundary in time domain. Earthquake Engineering and Engineering Vibration, 2006, 5(1):93-102

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/VS3D4)
