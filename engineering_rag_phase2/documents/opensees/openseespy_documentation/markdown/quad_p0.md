<!-- chunk_id: quad_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/quad.html",
 "title": "4.2.7.1. Quad Element",
 "category": "element",
 "command": "quad",
 "doc_section": "src",
 "rel_path": "src/quad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1842,
 "word_count": 195,
 "has_code": false,
 "has_table": true
} -->

## 4.2.7.1. Quad Element

This command is used to construct a FourNodeQuad element object which uses a bilinear isoparametric formulation.

**element(*'quad'*, *eleTag*, **eleNodes*, *thick*, *type*, *matTag*, *<pressure=0.0*, *rho=0.0*, *b1=0.0*, *b2=0.0>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of four element nodes in counter-clockwise order |
| `thick` ([float](https://docs.python.org/3/library/functions.html#float)) | element thickness |
| `type` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | string representing material behavior. The type parameter can be either `'PlaneStrain'` or `'PlaneStress'` |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of nDMaterial |
| `pressure` ([float](https://docs.python.org/3/library/functions.html#float)) | surface pressure (optional, default = 0.0) |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0) |
| `b1` `b2` ([float](https://docs.python.org/3/library/functions.html#float)) | constant body forces defined in the isoparametric domain (optional, default=0.0) |

Note

1. Consistent nodal loads are computed from the pressure and body forces.
2. The valid queries to a Quad element when creating an ElementRecorder object are ‘forces’, ‘stresses,’ and ‘material $matNum matArg1 matArg2 …’ Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Quad_Element)
