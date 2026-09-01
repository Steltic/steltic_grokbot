<!-- chunk_id: CFSWSWP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/CFSWSWP.html",
 "title": "4.14.5.38. CFSWSWP Wood-Sheathed Cold-Formed Steel Shear Wall Panel",
 "category": "general",
 "command": "CFSWSWP",
 "doc_section": "src",
 "rel_path": "src/CFSWSWP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2531,
 "word_count": 254,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.38. CFSWSWP Wood-Sheathed Cold-Formed Steel Shear Wall Panel

**uniaxialMaterial(*'CFSWSWP'*, *matTag*, *height*, *width*, *fut*, *tf*, *Ife*, *Ifi*, *ts*, *np*, *ds*, *Vs*, *sc*, *nc*, *type*, *openingArea*, *openingLength*)**

This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-Lateral displacement) of a wood-sheathed cold-formed steel shear wall panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.

This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `height` ([float](https://docs.python.org/3/library/functions.html#float)) | SWP’s height (mm) |
| `width` ([float](https://docs.python.org/3/library/functions.html#float)) | SWP’s width (mm) |
| `fut` ([float](https://docs.python.org/3/library/functions.html#float)) | Tensile strength of framing members (MPa) |
| `tf` ([float](https://docs.python.org/3/library/functions.html#float)) | Framing thickness (mm) |
| `Ife` ([float](https://docs.python.org/3/library/functions.html#float)) | Moment of inertia of the double end-stud (mm4) |
| `Ifi` ([float](https://docs.python.org/3/library/functions.html#float)) | Moment of inertia of the intermediate stud (mm4) |
| `ts` ([float](https://docs.python.org/3/library/functions.html#float)) | Sheathing thickness (mm) |
| `np` ([float](https://docs.python.org/3/library/functions.html#float)) | Sheathing number (one or two sides sheathed) |
| `ds` ([float](https://docs.python.org/3/library/functions.html#float)) | Screws diameter (mm) |
| `Vs` ([float](https://docs.python.org/3/library/functions.html#float)) | Screws shear strength (N) |
| `sc` ([float](https://docs.python.org/3/library/functions.html#float)) | Screw spacing on the SWP perimeter (mm) |
| `nc` ([float](https://docs.python.org/3/library/functions.html#float)) | Total number of screws located on the SWP perimeter |
| `type` ([int](https://docs.python.org/3/library/functions.html#int)) | Integer identifier used to define wood sheathing type (DFP=1, OSB=2, CSP=3) |
| `openingArea` ([float](https://docs.python.org/3/library/functions.html#float)) | Total area of openings (mm2) |
| `openingLength` ([float](https://docs.python.org/3/library/functions.html#float)) | Cumulative length of openings (mm) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/CFSWSWP)
