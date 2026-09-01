<!-- chunk_id: RambergOsgoodSteel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/RambergOsgoodSteel.html",
 "title": "4.14.1.6. RambergOsgoodSteel",
 "category": "general",
 "command": "RambergOsgoodSteel",
 "doc_section": "src",
 "rel_path": "src/RambergOsgoodSteel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 988,
 "word_count": 105,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.6. RambergOsgoodSteel

**uniaxialMaterial(*'RambergOsgoodSteel'*, *matTag*, *fy*, *E0*, *a*, *n*)**

This command is used to construct a Ramberg-Osgood steel material object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `fy` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic tangent |
| `a` ([float](https://docs.python.org/3/library/functions.html#float)) | “yield offset” and the Commonly used value for a is 0.002 |
| `n` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameters to control the transition from elastic to plastic branches. And controls the hardening of the material by increasing the “n” hardening ratio will be decreased. Commonly used values for n are ~5 or greater. |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/RambergOsgoodSteel_Material)
