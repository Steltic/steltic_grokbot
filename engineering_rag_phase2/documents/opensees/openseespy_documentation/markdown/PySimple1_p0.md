<!-- chunk_id: PySimple1_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PySimple1.html",
 "title": "4.14.4.1. PySimple1 Material",
 "category": "material",
 "command": "PySimple1",
 "doc_section": "src",
 "rel_path": "src/PySimple1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1513,
 "word_count": 177,
 "has_code": false,
 "has_table": true
} -->

## 4.14.4.1. PySimple1 Material

**uniaxialMaterial(*'PySimple1'*, *matTag*, *soilType*, *pult*, *Y50*, *Cd*, *c=0.0*)**

This command is used to construct a PySimple1 uniaxial material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `soilType` ([int](https://docs.python.org/3/library/functions.html#int)) | soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation. soilType = 2 Backbone of p-y curve approximates API (1993) sand relation. |
| `pult` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate capacity of the p-y material. Note that “p” or “pult” are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile]. |
| `Y50` ([float](https://docs.python.org/3/library/functions.html#float)) | Displacement at which 50% of pult is mobilized in monotonic loading. |
| `Cd` ([float](https://docs.python.org/3/library/functions.html#float)) | Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult. |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/PySimple1_Material)
