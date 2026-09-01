<!-- chunk_id: Dodd_Restrepo_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Dodd_Restrepo.html",
 "title": "4.14.1.5. Dodd_Restrepo",
 "category": "general",
 "command": "Dodd_Restrepo",
 "doc_section": "src",
 "rel_path": "src/Dodd_Restrepo.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1550,
 "word_count": 159,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.5. Dodd_Restrepo

**uniaxialMaterial(*'Dodd_Restrepo'*, *matTag*, *Fy*, *Fsu*, *ESH*, *ESU*, *Youngs*, *ESHI*, *FSHI*, *OmegaFac=1.0*)**

This command is used to construct a Dodd-Restrepo steel material

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength |
| `Fsu` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate tensile strength (UTS) |
| `ESH` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strain at initiation of strain hardening |
| `ESU` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strain at the UTS |
| `Youngs` ([float](https://docs.python.org/3/library/functions.html#float)) | Modulus of elasticity |
| `ESHI` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strain for a point on strain hardening curve, recommended range of values for ESHI: [ (ESU + 5*ESH)/6, (ESU + 3*ESH)/4] |
| `FSHI` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile stress at point on strain hardening curve corresponding to ESHI |
| `OmegaFac` ([float](https://docs.python.org/3/library/functions.html#float)) | Roundedness factor for Bauschinger curve in cycle reversals from the strain hardening curve. Range: [0.75, 1.15]. Largest value tends to near a bilinear Bauschinger curve. Default = 1.0. |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/DoddRestrepo)
