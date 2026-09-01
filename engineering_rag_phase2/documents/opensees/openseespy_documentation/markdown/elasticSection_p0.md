<!-- chunk_id: elasticSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticSection.html",
 "title": "4.16.1. Elastic Section",
 "category": "section",
 "command": "elasticSection",
 "doc_section": "src",
 "rel_path": "src/elasticSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1667,
 "word_count": 186,
 "has_code": false,
 "has_table": true
} -->

## 4.16.1. Elastic Section

**section(*'Elastic'*, *secTag*, *E_mod*, *A*, *Iz*, *G_mod=None*, *alphaY=None*)**

**section(*'Elastic'*, *secTag*, *E_mod*, *A*, *Iz*, *Iy*, *G_mod*, *Jxx*, *alphaY=None*, *alphaZ=None*)**

This command allows the user to construct an ElasticSection. The inclusion of shear deformations is optional. The dofs for 2D elastic section are `[P, Mz]`,
for 3D are `[P,Mz,My,T]`.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of section |
| `Iz` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local z-axis |
| `Iy` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local y-axis (required for 3D analysis) |
| `G_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear Modulus (optional for 2D analysis, required for 3D analysis) |
| `Jxx` ([float](https://docs.python.org/3/library/functions.html#float)) | torsional moment of inertia of section (required for 3D analysis) |
| `alphaY` ([float](https://docs.python.org/3/library/functions.html#float)) | shear shape factor along the local y-axis (optional) |
| `alphaZ` ([float](https://docs.python.org/3/library/functions.html#float)) | shear shape factor along the local z-axis (optional) |

Note

The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.
