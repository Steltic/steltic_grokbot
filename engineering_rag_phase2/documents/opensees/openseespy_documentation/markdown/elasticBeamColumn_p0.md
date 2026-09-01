<!-- chunk_id: elasticBeamColumn_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticBeamColumn.html",
 "title": "4.2.3.1. Elastic Beam Column Element",
 "category": "element",
 "command": "elasticBeamColumn",
 "doc_section": "src",
 "rel_path": "src/elasticBeamColumn.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2693,
 "word_count": 246,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.1. Elastic Beam Column Element

This command is used to construct an elasticBeamColumn element object. The arguments for the construction of an elastic beam-column element depend on the dimension of the problem, (ndm)

**element(*'elasticBeamColumn'*, *eleTag*, **eleNodes*, *Area*, *E_mod*, *Iz*, *transfTag*, *<'-mass'*, *mass>*, *<'-cMass'>*, *<'-release'*, *releaseCode>*)**

**element(*'elasticBeamColumn'*, *eleTag*, **eleNodes*, *secTag*, *transfTag*, *<'-mass'*, *mass>*, *<'-cMass'>*, *<'-release'*, *releaseCode>*)**

For a two-dimensional problem

**element(*'elasticBeamColumn'*, *eleTag*, **eleNodes*, *Area*, *E_mod*, *G_mod*, *Jxx*, *Iy*, *Iz*, *transfTag*, *<'-mass'*, *mass>*, *<'-cMass'>*)**

**element(*'elasticBeamColumn'*, *eleTag*, **eleNodes*, *secTag*, *transfTag*, *<'-mass'*, *mass>*, *<'-cMass'> <'-releasez'*, *releaseCode>*, *<'-releasey'*, *releaseCode>*)**

For a three-dimensional problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Area` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of element |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `G_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear Modulus |
| `Jxx` ([float](https://docs.python.org/3/library/functions.html#float)) | torsional moment of inertia of cross section |
| `Iy` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local y-axis |
| `Iz` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local z-axis |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined section object |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined coordinate-transformation (CrdTransf) object |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass per unit length (optional, default = 0.0) |
| `'-cMass'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to form consistent mass matrix (optional, default = lumped mass matrix) |
| `'releaseCode'` ([int](https://docs.python.org/3/library/functions.html#int)) | moment release (optional, 0=no release (default), 1=release at I, 2=release at J, 3=release at I and J) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element)
