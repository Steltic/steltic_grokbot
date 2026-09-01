<!-- chunk_id: SmearedSteelDoubleLayer_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/SmearedSteelDoubleLayer.html",
 "title": "3.1.6.21. SmearedSteelDoubleLayer Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "SmearedSteelDoubleLayer",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/SmearedSteelDoubleLayer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3527,
 "word_count": 444,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.21. SmearedSteelDoubleLayer Material

This command is used to construct a SmearedSteelDoubleLayer material object. It is the abstract representation of a double perpendicular smeared steel layer (plane stress) 2D material with a tangent formulation. Each layer works only in the direction of the bars, so a uniaxial constitutive model is used to represent the behavior of reinforcing steel bars in each direction. The angle that defines the orientation
of the steel layers with respect to the local coordinate system **x-y** is denoted as \(\theta_{s}\), represented by the argument `$OrientationEmbeddedSteel` (based on the work of Rojas et al., 2016).

Fig. 3.1.6.7 SmearedSteelDoubleLayer Material: (a) Distributed reinforcement; (b) Rebar layers; (c) Steel layers orientation; (d) Steel behavior in the local coordinate system; (e) Uniaxial steel behavior.

Command

nDMaterial SmearedSteelDoubleLayer $matTag $s1 $s2 $ratioSteelLayer1 $ratioSteelLayer2 $OrientationEmbeddedSteel

| Parameter | Type | Description |
| --- | --- | --- |
| $matTag | integer | unique tag identifyieng this material |
| $s1 | integer | tag of unixial simulating horizontal reinforcement |
| $s2 | integer | tag of unixial simulating vertical reinforcement |
| $ratioSteelLayer1 | float | reinforcing ratio in horizontal direction of smeared steel |
| $ratioSteelLayer2 | float | reinforcing ratio in vertical direction of smeared steel |
| $OrientationEmbeddedSteel | float | orientation of the smeared steel layers |

The following recorders are available with the SmearedSteelDoubleLayer material.

| Recorder | Description |
| --- | --- |
| steel_layer_stress | in-plane panel steel stresses \(\sigma^{s}_{xx}\), \(\sigma^{s}_{yy}\), \(\tau^{s}_{xy}\) |
| strain_stress_steel1 | Uniaxial strain and stress of steel 1 \(\varepsilon_{s1}\), \(\sigma_{s1}\) |
| strain_stress_steel2 | Uniaxial strain and stress of steel 2 \(\varepsilon_{s2}\), \(\sigma_{s2}\) |

Notes

1. The implementation of this material does not include the reductions in yield strength and strain-hardening ratio for embedded steel bars in concrete (Belarbi and Hsu, 1995).

Examples

The following example constructs a SmearedSteelDoubleLayer material with tag **2** , composed of a horizontal and vertical uniaxial steel material (e.g. [Steel02](https://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening), [SteelMPF](https://opensees.berkeley.edu/wiki/index.php/SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983))) of tag **1**, reinforcing ratio in horizontal and vertical direction of **1%** and an orientation of the double smeared steel layer of **0.0** radians.

1. **Tcl Code**

```
nDMaterial SmearedSteelDoubleLayer 2 1 1 0.01 0.01 0.0;
```

1. **Python Code**

```
nDMaterial('SmearedSteelDoubleLayer', 2, 1, 1, 0.01, 0.01, 0.0)
```

**REFERENCES:**

1. Rojas, F., Anderson, J. C., Massone, L. M. (2016). A nonlinear quadrilateral layered membrane element with drilling degrees of freedom for the modeling of reinforced concrete walls. Engineering Structures, 124, 521-538. ([link](https://www.sciencedirect.com/science/article/pii/S0141029616302954)).
2. Belarbi, A., & Hsu, T. C. (1995). Constitutive  laws   of   softened   concrete   in   biaxial   tension-compression.  ACI  Structural  Journal, 92(5), 562–573. ([link](https://www.scopus.com/record/display.uri?eid=2-s2.0-0029361065&origin=inward))

**Code Developed by:** F. Rojas (University of Chile), M.J. Núñez (University of Chile).
