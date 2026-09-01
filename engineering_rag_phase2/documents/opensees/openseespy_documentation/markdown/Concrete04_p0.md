<!-- chunk_id: Concrete04_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete04.html",
 "title": "4.14.2.4. Concrete04",
 "category": "general",
 "command": "Concrete04",
 "doc_section": "src",
 "rel_path": "src/Concrete04.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2548,
 "word_count": 306,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.4. Concrete04

**uniaxialMaterial(*'Concrete04'*, *matTag*, *fc*, *epsc*, *epscu*, *Ec*, *fct*, *et*, *beta*)**

This command is used to construct a uniaxial Popovics concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and tensile strength with exponential decay.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point values defining concrete compressive strength at 28 days (compression is negative) |
| `epsc` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point values defining concrete strain at maximum strength |
| `epscu` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point values defining concrete strain at crushing strength |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point values defining initial stiffness |
| `fct` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining the maximum tensile strength of concrete (optional) |
| `et` ([float](https://docs.python.org/3/library/functions.html#float)) | floating point value defining ultimate tensile strain of concrete (optional) |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | loating point value defining the exponential curve parameter to define the residual stress (as a factor of ft) at etu |

Note

1. Compressive concrete parameters should be input as negative values.
2. The envelope of the compressive stress-strain response is defined using the model proposed by Popovics (1973). If the user defines \(Ec = 57000*sqrt(|fcc|)\) (in psi)’ then the envelope curve is identical to proposed by Mander et al. (1988).
3. Model Characteristic: For loading in compression, the envelope to the stress-strain curve follows the model proposed by Popovics (1973) until the concrete crushing strength is achieved and also for strains beyond that corresponding to the crushing strength. For unloading and reloading in compression, the Karsan-Jirsa model (1969) is used to determine the slope of the curve. For tensile loading, an exponential curve is used to define the envelope to the stress-strain curve. For unloading and reloading in tensile, the secant stiffness is used to define the path.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Concrete04_Material_--_Popovics_Concrete_Material)
