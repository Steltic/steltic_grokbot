<!-- chunk_id: MVLEM_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MVLEM.html",
 "title": "4.2.3.9. MVLEM - Multiple-Vertical-Line-Element-Model for RC Walls",
 "category": "element",
 "command": "MVLEM",
 "doc_section": "src",
 "rel_path": "src/MVLEM.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3809,
 "word_count": 422,
 "has_code": false,
 "has_table": true
} -->

## 4.2.3.9. MVLEM - Multiple-Vertical-Line-Element-Model for RC Walls

Developed and implemented by:

Kristijan Kolozvari (CSU Fullerton)

Kutay Orakcal (Bogazici University)

John Wallace (UCLA)

The MVLEM element command is used to generate a two-dimensional Multiple-Vertical-Line-Element-Model (MVLEM; Vulcano et al., 1988; Orakcal et al., 2004, Kolozvari et al., 2015) for simulation of flexure-dominated RC wall behavior. A single model element incorporates six global degrees of freedom, three of each located at the center of rigid top and bottom beams, as illustrated in Figure 1a. The axial/flexural response of the MVLEM is simulated by a series of uniaxial elements (or macro-fibers) connected to the rigid beams at the top and bottom (e.g., floor) levels, whereas the shear response is described by a shear spring located at height ch from the bottom of the wall element (Figure 1a). Shear and flexural responses of the model element are uncoupled. The relative rotation between top and bottom faces of the wall element occurs about the point located on the central axis of the element at height ch (Figure 1b). Rotations and resulting transverse displacements are calculated based on the wall curvature, derived from section and material properties, corresponding to the bending moment at height ch of each element (Figure 1b). A value of c=0.4 was recommended by Vulcano et al. (1988) based on comparison of the model response with experimental results.

**element(*'MVLEM'*, *eleTag*, *Dens*, **eleNodes*, *m*, *c*, *'-thick'*, **thick*, *'-width'*, **widths*, *'-rho'*, **rho*, *'-matConcrete'*, **matConcreteTags*, *'-matSteel'*, **matSteelTags*, *'-matShear'*, *matShearTag*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `Dens` ([float](https://docs.python.org/3/library/functions.html#float)) | Wall density |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `m` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of element macro-fibers |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | Location of center of rotation from the iNode, `c` = 0.4 (recommended) |
| `thick` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of `m` macro-fiber thicknesses |
| `widths` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of `m` macro-fiber widths |
| `rho` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | a list of m reinforcing ratios corresponding to macro-fibers; for each fiber: \(rho_i = A_{s,i}/A_{gross,i} (1 < i < m)\) |
| `matConcreteTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of `m` uniaxialMaterial tags for concrete |
| `matSteelTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of `m` uniaxialMaterial tags for steel |
| `matShearTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag of uniaxialMaterial for shear material |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls)

> Kolozvari K., Orakcal K., and Wallace J. W. (2015a). “New opensees models for simulating nonlinear flexural and coupled shear-flexural behavior of RC walls and columns”, Computers and Structures, Volume 196, February 2018, Pages 246-262, [doi](https://doi.org/10.1016/j.compstruc.2017.10.010)
