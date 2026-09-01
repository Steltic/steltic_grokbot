<!-- chunk_id: FluidSolidPorousMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/FluidSolidPorousMaterial.html",
 "title": "4.15.7.1. FluidSolidPorousMaterial",
 "category": "material",
 "command": "FluidSolidPorousMaterial",
 "doc_section": "src",
 "rel_path": "src/FluidSolidPorousMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1450,
 "word_count": 167,
 "has_code": false,
 "has_table": true
} -->

## 4.15.7.1. FluidSolidPorousMaterial

**nDMaterial(*'FluidSolidPorous'*, *matTag*, *nd*, *soilMatTag*, *combinedBulkModul*, *pa=101.0*)**

FluidSolidPorous material couples the responses of two phases: fluid and solid. The fluid phase response is only volumetric and linear elastic. The solid phase can be any NDMaterial. This material is developed to simulate the response of saturated porous media under fully undrained condition.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | Number of dimensions, 2 for plane-strain, and 3 for 3D analysis. |
| `soilMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | The material number for the solid phase material (previously defined). |
| `combinedBulkModul` ([float](https://docs.python.org/3/library/functions.html#float)) | Combined undrained bulk modulus \(B_c\) relating changes in pore pressure and volumetric strain, may be approximated by: \(B_c \approx B_f /n\) where \(B_f\) is the bulk modulus of fluid phase (2.2x106 kPa (or 3.191x105 psi) for water), and \(n\) the initial porosity. |
| `pa` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional atmospheric pressure for normalization (typically 101 kPa in SI units, or 14.65 psi in English units) |

See also [notes](http://opensees.berkeley.edu/wiki/index.php/FluidSolidPorousMaterial)
