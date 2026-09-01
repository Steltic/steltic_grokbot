<!-- chunk_id: ModElasticBeam2d_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ModElasticBeam2d.html",
 "title": "4.2.3.2. Elastic Beam Column Element with Stiffness Modifiers",
 "category": "element",
 "command": "ModElasticBeam2d",
 "doc_section": "src",
 "rel_path": "src/ModElasticBeam2d.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2417,
 "word_count": 250,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.2. Elastic Beam Column Element with Stiffness Modifiers

This command is used to construct a ModElasticBeam2d element object. The arguments for the construction of an elastic beam-column element with stiffness modifiers is applicable for 2-D problems. This element should be used for modelling of a structural element with an equivalent combination of one elastic element with stiffness-proportional damping, and two springs at its two ends with no stiffness proportional damping to represent a prismatic section. The modelling technique is based on a number of analytical studies discussed in Zareian and Medina (2010) and Zareian and Krawinkler (2009) and is utilized in order to solve problems related to numerical damping in dynamic analysis of frame structures with concentrated plasticity springs.

**element(*'ModElasticBeam2d'*, *eleTag*, **eleNodes*, *Area*, *E_mod*, *Iz*, *K11*, *K33*, *K44*, *transfTag*, *<'-mass'*, *massDens>*, *<'-cMass'>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Area` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of element |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `Iz` ([float](https://docs.python.org/3/library/functions.html#float)) | second moment of area about the local z-axis |
| `K11` ([float](https://docs.python.org/3/library/functions.html#float)) | stiffness modifier for translation |
| `K33` ([float](https://docs.python.org/3/library/functions.html#float)) | stiffness modifier for translation |
| `K44` ([float](https://docs.python.org/3/library/functions.html#float)) | stiffness modifier for rotation |
| `transfTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined coordinate-transformation (CrdTransf) object |
| `massDens` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass per unit length (optional, default = 0.0) |
| `'-cMass'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to form consistent mass matrix (optional, default = lumped mass matrix) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element_with_Stiffness_Modifiers)
