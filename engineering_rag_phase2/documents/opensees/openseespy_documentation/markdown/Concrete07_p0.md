<!-- chunk_id: Concrete07_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Concrete07.html",
 "title": "4.14.2.6. Concrete07",
 "category": "general",
 "command": "Concrete07",
 "doc_section": "src",
 "rel_path": "src/Concrete07.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1840,
 "word_count": 192,
 "has_code": false,
 "has_table": true
} -->

## 4.14.2.6. Concrete07

**uniaxialMaterial(*'Concrete07'*, *matTag*, *fc*, *epsc*, *Ec*, *ft*, *et*, *xp*, *xn*, *r*)**

Concrete07 is an implementation of Chang & Mander’s 1994 concrete model with simplified unloading and reloading curves. Additionally the tension envelope shift with respect to the origin proposed by Chang and Mander has been removed. The model requires eight input parameters to define the monotonic envelope of confined and unconfined concrete in the following form:

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete compressive strength (compression is negative) |
| `epsc` ([float](https://docs.python.org/3/library/functions.html#float)) | concrete strain at maximum compressive strength |
| `Ec` ([float](https://docs.python.org/3/library/functions.html#float)) | Initial Elastic modulus of the concrete |
| `ft` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile strength of concrete (tension is positive) |
| `et` ([float](https://docs.python.org/3/library/functions.html#float)) | tensile strain at max tensile strength of concrete |
| `xp` ([float](https://docs.python.org/3/library/functions.html#float)) | Non-dimensional term that defines the strain at which the straight line descent begins in tension |
| `xn` ([float](https://docs.python.org/3/library/functions.html#float)) | Non-dimensional term that defines the strain at which the straight line descent begins in compression |
| `r` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter that controls the nonlinear descending branch |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Concrete07_%E2%80%93_Chang_%26_Mander%E2%80%99s_1994_Concrete_Model)
