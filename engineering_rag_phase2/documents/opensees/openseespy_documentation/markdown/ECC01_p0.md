<!-- chunk_id: ECC01_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ECC01.html",
 "title": "4.14.5.28. Engineered Cementitious Composites Material",
 "category": "material",
 "command": "ECC01",
 "doc_section": "src",
 "rel_path": "src/ECC01.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2364,
 "word_count": 222,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.28. Engineered Cementitious Composites Material

**uniaxialMaterial(*'ECC01'*, *matTag*, *sigt0*, *epst0*, *sigt1*, *epst1*, *epst2*, *sigc0*, *epsc0*, *epsc1*, *alphaT1*, *alphaT2*, *alphaC*, *alphaCU*, *betaT*, *betaC*)**

This command is used to construct a uniaxial Engineered Cementitious Composites (ECC)material object based on the ECC material model of Han, et al. (see references). Reloading in tension and compression is linear.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `sigt0` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile cracking stress |
| `epst0` ([float](https://docs.python.org/3/library/functions.html#float)) | strain at tensile cracking stress |
| `sigt1` ([float](https://docs.python.org/3/library/functions.html#float)) | peak tensile stress |
| `epst1` ([float](https://docs.python.org/3/library/functions.html#float)) | strain at peak tensile stress |
| `epst2` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate tensile strain |
| `sigc0` ([float](https://docs.python.org/3/library/functions.html#float)) | compressive strength (see NOTES) |
| `epsc0` ([float](https://docs.python.org/3/library/functions.html#float)) | strain at compressive strength (see NOTES) |
| `epsc1` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate compressive strain (see NOTES) |
| `alphaT1` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of the unloading curve in tensile strain hardening region |
| `alphaT2` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of the unloading curve in tensile softening region |
| `alphaC` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of the unloading curve in the compressive softening |
| `alphaCU` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of the compressive softening curve (use 1 for linear softening) |
| `betaT` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter to determine permanent strain in tension |
| `betaC` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter to determine permanent strain in compression |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Engineered_Cementitious_Composites_Material)
