<!-- chunk_id: CFSSSWP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CFSSSWP.html",
 "title": "4.14.5.39. CFSSSWP Steel-Sheathed Cold-formed Steel Shear Wall Panel",
 "category": "general",
 "command": "CFSSSWP",
 "doc_section": "src",
 "rel_path": "src/CFSSSWP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2588,
 "word_count": 253,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.39. CFSSSWP Steel-Sheathed Cold-formed Steel Shear Wall Panel

**uniaxialMaterial(*'CFSSSWP'*, *matTag*, *height*, *width*, *fuf*, *fyf*, *tf*, *Af*, *fus*, *fys*, *ts*, *np*, *ds*, *Vs*, *sc*, *dt*, *openingArea*, *openingLength*)**

This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-lateral Displacement) of a Steel-Sheathed Cold-Formed Steel Shear Wall Panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.

This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `height` ([float](https://docs.python.org/3/library/functions.html#float)) | SWP’s height (mm) |
| `width` ([float](https://docs.python.org/3/library/functions.html#float)) | SWP’s width (mm) |
| `fuf` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strength of framing members (MPa) |
| `fyf` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength of framing members (MPa) |
| `tf` ([float](https://docs.python.org/3/library/functions.html#float)) | Framing thickness (mm) |
| `Af` ([float](https://docs.python.org/3/library/functions.html#float)) | Framing cross section area (mm2) |
| `fus` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strength of steel sheet sheathing (MPa) |
| `fys` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength of steel sheet sheathing (MPa) |
| `ts` ([float](https://docs.python.org/3/library/functions.html#float)) | Sheathing thickness (mm) |
| `np` ([float](https://docs.python.org/3/library/functions.html#float)) | Sheathing number (one or two sides sheathed) |
| `ds` ([float](https://docs.python.org/3/library/functions.html#float)) | Screws diameter (mm) |
| `Vs` ([float](https://docs.python.org/3/library/functions.html#float)) | Screws shear strength (N) |
| `sc` ([float](https://docs.python.org/3/library/functions.html#float)) | Screw spacing on the SWP perimeter (mm) |
| `dt` ([float](https://docs.python.org/3/library/functions.html#float)) | Anchor bolt’s diameter (mm) |
| `openingArea` ([float](https://docs.python.org/3/library/functions.html#float)) | Total area of openings (mm2) |
| `openingLength` ([float](https://docs.python.org/3/library/functions.html#float)) | Cumulative length of openings (mm) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/CFSSSWP)
