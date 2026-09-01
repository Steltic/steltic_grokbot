<!-- chunk_id: ElasticTimoshenkoBeam_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElasticTimoshenkoBeam.html",
 "title": "4.2.3.3. Elastic Timoshenko Beam Column Element",
 "category": "element",
 "command": "ElasticTimoshenkoBeam",
 "doc_section": "src",
 "rel_path": "src/ElasticTimoshenkoBeam.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2386,
 "word_count": 229,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.3. Elastic Timoshenko Beam Column Element

This command is used to construct an ElasticTimoshenkoBeam element object. A Timoshenko beam is a frame member that accounts for shear deformations. The arguments for the construction of an elastic Timoshenko beam element depend on the dimension of the problem, ndm:

**element(*'ElasticTimoshenkoBeam'*, *eleTag*, **eleNodes*, *E_mod*, *G_mod*, *Area*, *Iz*, *Avy*, *transfTag*, *<'-mass'*, *massDens>*, *<'-cMass'>*)**

For a two-dimensional problem:

**element(*'ElasticTimoshenkoBeam'*, *eleTag*, **eleNodes*, *E_mod*, *G_mod*, *Area*, *Jxx*, *Iy*, *Iz*, *Avy*, *Avz*, *transfTag*, *<'-mass'*, *massDens>*, *<'-cMass'>*)**

For a three-dimensional problem:

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `G_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear Modulus |
| `Area` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of element |
| `Jxx` ([float](https://docs.python.org/3/library/functions.html#float)) | torsional moment of inertia of cross section |
| `Iy` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local y-axis |
| `Iz` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local z-axis |
| `Avy` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear area for the local y-axis |
| `Avz` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear area for the local z-axis |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined coordinate-transformation (CrdTransf) object |
| `massDens` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass per unit length (optional, default = 0.0) |
| `'-cMass'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to form consistent mass matrix (optional, default = lumped mass matrix) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic_Timoshenko_Beam_Column_Element)
