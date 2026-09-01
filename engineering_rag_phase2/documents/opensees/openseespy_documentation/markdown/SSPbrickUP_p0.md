<!-- chunk_id: SSPbrickUP_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/SSPbrickUP.html",
 "title": "4.2.12.2. SSPbrickUP Element",
 "category": "element",
 "command": "SSPbrickUP",
 "doc_section": "src",
 "rel_path": "src/SSPbrickUP.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4362,
 "word_count": 573,
 "has_code": false,
 "has_table": true
} -->

## 4.2.12.2. SSPbrickUP Element

This command is used to construct a SSPbrickUP element object.

**element(*'SSPbrickUP'*, *eleTag*, **eleNodes*, *matTag*, *fBulk*, *fDen*, *k1*, *k2*, *k3*, *void*, *alpha*, *<b1*, *b2*, *b3>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of eight element nodes in counter-clockwise order |
| `matTag` ([float](https://docs.python.org/3/library/functions.html#float)) | unique integer tag associated with previously-defined nDMaterial object |
| `fBulk` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus of the pore fluid |
| `fDen` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density of the pore fluid |
| `k1` `k2` `k3` ([float](https://docs.python.org/3/library/functions.html#float)) | permeability coefficients in global x-, y-, and z-directions, respectively |
| `void` ([float](https://docs.python.org/3/library/functions.html#float)) | voids ratio |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | spatial pressure field stabilization parameter (see discussion below for more information) |
| `b1` `b2` `b3` ([float](https://docs.python.org/3/library/functions.html#float)) | constant body forces in global x-, y-, and z-directions, respectively (optional, default = 0.0) - See Note 3 |

The SSPbrickUP element is an extension of the SSPbrick Element for use in dynamic 3D analysis of fluid saturated porous media. A mixed displacement-pressure (u-p) formulation is used, based upon the work of Biot as extended by Zienkiewicz and Shiomi (1984).

The physical stabilization necessary to allow for reduced integration incorporates an enhanced assumed strain field, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements.

Equal-order interpolation is used for the displacement and pressure fields, thus, the SSPbrickUP element does not inherently pass the inf-sup condition, and is not fully acceptable in the incompressible-impermeable limit (the brickUP Element has the same issue). A stabilizing parameter is employed to permit the use of equal-order interpolation for the SSPbrickUP element. This parameter $alpha can be computed as

\[\alpha = h^2/(4*(K_s + (4/3)*G_s))\]

where \(h\) is the element size, and \(K_s\) and \(G_s\) are the bulk and shear moduli for the solid phase. The \(\alpha\) parameter should be a small number. With a properly defined \(\alpha\) parameter, the SSPbrickUP element can produce comparable results to a higher-order element such as the 20_8_BrickUP Element at a significantly lower computational cost and with a greater ease in mesh generation.

Note

1. The SSPbrickUP element will only work in dynamic analysis.
2. For saturated soils, the mass density input into the associated nDMaterial object should be the saturated mass density.
3. When modeling soil, the body forces input into the SSPbrickUP element should be the components of the gravitational vector, not the unit weight.
4. Fixing the pore pressure degree-of-freedom (dof 4) at a node is a drainage boundary condition at which zero pore pressure will be maintained throughout the analysis. Leaving the fourth dof free allows pore pressures to build at that node.
5. Valid queries to the SSPbrickUP element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., ‘stress’, ‘strain’). Material response is recorded at the single integration point located in the center of the element.
6. The SSPbrickUP element was designed with intentions of duplicating the functionality of the brickUP Element. If an example is found where the SSPbrickUP element cannot do something that works for the brickUP Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/SSPbrickUP_Element)
