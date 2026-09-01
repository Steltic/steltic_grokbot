<!-- chunk_id: NineFourNodeQuadUP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/NineFourNodeQuadUP.html",
 "title": "4.2.11.5. Nine Four Node Quad u-p Element",
 "category": "element",
 "command": "NineFourNodeQuadUP",
 "doc_section": "src",
 "rel_path": "src/NineFourNodeQuadUP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1989,
 "word_count": 216,
 "has_code": false,
 "has_table": true
} -->

## 4.2.11.5. Nine Four Node Quad u-p Element

Nine_Four_Node_QuadUP is a 9-node quadrilateral plane-strain element. The four corner nodes have 3 degrees-of-freedom (DOF) each: DOF 1 and 2 for solid displacement (u) and DOF 3 for fluid pressure (p). The other five nodes have 2 DOFs each for solid displacement. This element is implemented for simulating dynamic response of solid-fluid fully coupled material, based on Biot’s theory of porous medium.

**element(*'9_4_QuadUP'*, *eleTag*, **eleNodes*, *thick*, *matTag*, *bulk*, *fmass*, *hPerm*, *vPerm*, *<b1=0*, *b2=0>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of nine element nodes |
| `thick` ([float](https://docs.python.org/3/library/functions.html#float)) | Element thickness |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag of an NDMaterial object (previously defined) of which the element is composed |
| `bulk` ([float](https://docs.python.org/3/library/functions.html#float)) | Combined undrained bulk modulus Bc relating changes in pore pressure and volumetric strain, may be approximated by: \(B_c \approx B_f/n\) where \(B_f\) is the bulk modulus of fluid phase (\(2.2\times 10^6\) kPa (or \(3.191\times 10^5\) psi) for water), and n the initial porosity. |
| `fmass` ([float](https://docs.python.org/3/library/functions.html#float)) | Fluid mass density |
| `hPerm`, `vPerm` ([float](https://docs.python.org/3/library/functions.html#float)) | Permeability coefficient in horizontal and vertical directions respectively. |
| `b1`, `b2` ([float](https://docs.python.org/3/library/functions.html#float)) | Optional gravity acceleration components in horizontal and vertical directions respectively (defaults are 0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Nine_Four_Node_Quad_u-p_Element)
