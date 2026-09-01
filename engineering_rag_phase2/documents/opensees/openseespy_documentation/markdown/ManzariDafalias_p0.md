<!-- chunk_id: ManzariDafalias_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ManzariDafalias.html",
 "title": "4.15.1.11. ManzariDafalias",
 "category": "general",
 "command": "ManzariDafalias",
 "doc_section": "src",
 "rel_path": "src/ManzariDafalias.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2688,
 "word_count": 247,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.11. ManzariDafalias

**nDMaterial(*'ManzariDafalias'*, *matTag*, *G0*, *nu*, *e_init*, *Mc*, *c*, *lambda_c*, *e0*, *ksi*, *P_atm*, *m*, *h0*, *ch*, *nb*, *A0*, *nd*, *z_max*, *cz*, *Den*)**

This command is used to construct a multi-dimensional Manzari-Dafalias(2004) material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `G0` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus constant |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | poisson ratio |
| `e_init` ([float](https://docs.python.org/3/library/functions.html#float)) | initial void ratio |
| `Mc` ([float](https://docs.python.org/3/library/functions.html#float)) | critical state stress ratio |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | ratio of critical state stress ratio in extension and compression |
| `lambda_c` ([float](https://docs.python.org/3/library/functions.html#float)) | critical state line constant |
| `e0` ([float](https://docs.python.org/3/library/functions.html#float)) | critical void ratio at p = 0 |
| `ksi` ([float](https://docs.python.org/3/library/functions.html#float)) | critical state line constant |
| `P_atm` ([float](https://docs.python.org/3/library/functions.html#float)) | atmospheric pressure |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | yield surface constant (radius of yield surface in stress ratio space) |
| `h0` ([float](https://docs.python.org/3/library/functions.html#float)) | constant parameter |
| `ch` ([float](https://docs.python.org/3/library/functions.html#float)) | constant parameter |
| `nb` ([float](https://docs.python.org/3/library/functions.html#float)) | bounding surface parameter, \(nb \ge 0\) |
| `A0` ([float](https://docs.python.org/3/library/functions.html#float)) | dilatancy parameter |
| `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | dilatancy surface parameter \(nd \ge 0\) |
| `z_max` ([float](https://docs.python.org/3/library/functions.html#float)) | fabric-dilatancy tensor parameter |
| `cz` ([float](https://docs.python.org/3/library/functions.html#float)) | fabric-dilatancy tensor parameter |
| `Den` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density of the material |

The material formulations for the ManzariDafalias object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`

See also [here](http://opensees.berkeley.edu/wiki/index.php/Manzari_Dafalias_Material)

References

Dafalias YF, Manzari MT. “Simple plasticity sand model accounting for fabric change effects”. Journal of Engineering Mechanics 2004
