<!-- chunk_id: MVLEM_3D_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/MVLEM_3D.html",
 "title": "3.1.10.8. MVLEM_3D Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "MVLEM_3D",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/MVLEM_3D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4875,
 "word_count": 689,
 "has_code": false,
 "has_table": true
} -->

## 3.1.10.8. MVLEM_3D Element

Developed and implemented by:

Kristijan Kolozvari (CSU Fullerton)

Kamiar Kalbasi (CSU Fullerton)

Kutay Orakcal (Bogazici University)

John Wallace (UCLA)

#### 3.1.10.8.1. Description

The MVLEM_3D model (Figure 1a) is a three-dimensional four-node element with 24 DOFs for nonlinear analysis of flexure-controlled non-rectangular reinforced concrete walls subjected to multidirectional loading. The model is an extension of the two-dimensional, two-node Multiple-Vertical-Line-Element-Model ([MVLEM](https://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls)). The baseline MVLEM, which is essentially a line element for rectangular walls subjected to in-plane loading, is extended to a three-dimensional model formulation by: 1) applying geometric transformation of the element in-plane degrees of freedom that convert it into a four-node element formulation (Figure 1b), as well as by incorporating linear elastic out-of-plane behavior based on the Kirchhoff plate theory (Figure 1c). The in-plane and the out-of-plane element behaviors are uncoupled in the present model.

This element shall be used in Domain defined with **-ndm 3 -ndf 6**.

Fig. 3.1.10.4 **Figure 1: MVLEM_3D Element Formulation**

#### 3.1.10.8.2. Input Parameters

Command

element MVLEM_3D eleTag iNode jNode kNode lNode m -thick {Thicknesses} -width {Widths} -rho {Reinforcing_ratios} -matConcrete {Concrete_tags} -matSteel {Steel_tags} -matShear {Shear_tag} <-CoR c> <-ThickMod tMod> <-Poisson Nu> <-Density Dens>

| Parameter | Type | Description |
| --- | --- | --- | --- |
| eleTag | integer | unique element object tag |
| iNode jNode kNode lNode | 4 integer | tags of element nodes defined in counterclockwise direction\| |
| m | integer | number of element fibers |
| {Thicknesses} | *m* float | array of *m* fiber thicknesses |
| {Widths} | *m* float | array of *m* macro-fiber widths |
| {Reinforcing_ratios} | *m* float | array of *m* reinforcing ratios corresponding to macro-fibers |
| {Concrete_tags} | *m* float | array of *m* uniaxialMaterial tags for concrete |
| {Steel_tags} | *m* float | array of *m* uniaxialMaterial tags for steel |
| {Shear_tag} | *m* float | tag of uniaxialMaterial for shear material |
| c | float | location of center of rotation from the base (optional; default = 0.4 (recommended)) |
| tMod | float | thickness multiplier (optional; default = 0.63 equivalent to 0.25Ig for out-of-plane bending) |
| Nu | float | Poisson ratio for out-of-plane bending (optional; default = 0.25) |
| Dens | float | Density (optional; default = 0.0) |

#### 3.1.10.8.3. Recorders

The following recorders are available with the MVLEM_3D element.

| Recorder | Description |
| --- | --- |
| globalForce | Element global forces |
| Curvature | Element curvature |
| Shear_Force_Deformation | Element shear force-deformation relationship |
| Fiber_Strain | Vertical strains in m fibers along the cross-section |
| Fiber_Stress_Concrete | Vertical concrete stresses in m fibers along the cross-section |
| Fiber_Stress_Steel | Vertical steel stresses in m fibers along the cross-section |

#### 3.1.10.8.4. OpenSeesPy Documentation

OpenSeesPy user documetation for the MVLEM_3D element can be accessed from [HERE](https://openseespydoc.readthedocs.io/en/latest/src/MVLEM_3D.html).

#### 3.1.10.8.5. Example

Specimen TUB (Beyer et al. 2008) is analyzed using the MVLEM_3D. Figure 2a shows the photo of the test specimen and the multidirectional displacement pattern applied at the top of the wall, while Figure 2b-c show the MVLEM_3D model of specimen TUB. Tcl Input files can be downloaded from [MVLEM-3D GitHub Page](https://github.com/kkolozvari/MVLEM-3D).

Fig. 3.1.10.5 **Figure 2: MVLEM_3D Model of Specimen TUB**

Fig. 3.1.10.6 **Figure 3: Animation of MVLEM_3D Analysis of Specimen TUB (displacement scale factor = 3.0)**

Figure 4 compares experimentally measured and analytically predicted load deformation behavior of the specimen TUB in E-W, N-S, and diagonal loading directions. The model provides accurate predictions of the lateral load capacity and the stiffness under cyclic loading in loading directions parallel to the principal axes of the cross-section (E-W, N-S direction). Analysis results overestimate the lateral load capacity in diagonal loading directions due to plane-sections-remain-plane assumption implemented in the model formulation that cannot capture pronounced shear lag effect observed in the test specimen.

Fig. 3.1.10.7 **Figure 4: Experimental vs. MVLEM_3D Load-Deformation Response of Specimen TUB**

#### 3.1.10.8.6. References

1. Kolozvari, K. Kalbasi, K. Orakcal & J. W. Wallace, “Three-Dimensional Model for Nonlinear Analysis of Slender Flanged Reinforced Concrete Walls”, Engineering Structures, [Volume 236, 1 June 2021, 112105](https://doi.org/10.1016/j.engstruct.2021.112105).
