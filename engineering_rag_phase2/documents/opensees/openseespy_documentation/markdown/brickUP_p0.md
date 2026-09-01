<!-- chunk_id: brickUP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/brickUP.html",
 "title": "4.2.11.2. Brick u-p Element",
 "category": "element",
 "command": "brickUP",
 "doc_section": "src",
 "rel_path": "src/brickUP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1798,
 "word_count": 202,
 "has_code": false,
 "has_table": true
} -->

## 4.2.11.2. Brick u-p Element

BrickUP is an 8-node hexahedral linear isoparametric element. Each node has 4 degrees-of-freedom (DOF): DOFs 1 to 3 for solid displacement (u) and DOF 4 for fluid pressure (p). This element is implemented for simulating dynamic response of solid-fluid fully coupled material, based on Biot’s theory of porous medium.

**element(*'brickUP'*, *eleTag*, **eleNodes*, *matTag*, *bulk*, *fmass*, *permX*, *permY*, *permZ*, *<bX=0*, *bY=0*, *bZ=0>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of eight element nodes |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag of an NDMaterial object (previously defined) of which the element is composed |
| `bulk` ([float](https://docs.python.org/3/library/functions.html#float)) | Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: \(B_c \approx B_f/n\) where \(B_f\) is the bulk modulus of fluid phase (\(2.2\times 10^6\) kPa (or \(3.191\times 10^5\) psi) for water), and n the initial porosity. |
| `fmass` ([float](https://docs.python.org/3/library/functions.html#float)) | Fluid mass density |
| `permX`, `permY`, `permZ` ([float](https://docs.python.org/3/library/functions.html#float)) | Permeability coefficients in x, y, and z directions respectively. |
| `bX`, `bY`, `bZ` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional gravity acceleration components in x, y, and z directions directions respectively (defaults are 0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Brick_u-p_Element)
