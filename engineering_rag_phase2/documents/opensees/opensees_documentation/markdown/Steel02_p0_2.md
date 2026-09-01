<!-- chunk_id: Steel02_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/Steel02.html",
 "title": "3.1.5.2. Steel02 Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "Steel02",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/Steel02.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2379,
 "word_count": 366,
 "has_code": true,
 "has_table": true
} -->

## 3.1.5.2. Steel02 Material

This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.

**uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2 <$a1 $a2 $a3 $a4 $sigInit>**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material |
| $Fy | *float* | yield strength |
| $E0 | *float* | initial elastic tangent |
| $b | *float* | strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent) |
| R0 $CR1 $CR2 | 3 *float* | parameters to control the transition from elastic to plastic branches. |
| $a1 | *float* | isotropic hardening parameter. (optional: default = 0.0). see note. |
| $a2 | *float* | isotropic hardening parameter (optional: default = 1.0). see note. |
| $a3 | *float* | isotropic hardening parameter. (optional: default = 0.0). see note. |
| $a4 | *float* | isotropic hardening parameter. (optional: default = 1.0). see note. |
| $sigInit | *float* | Initial Stress Value (optional: default = 0.0) |

Note

$a1 and $a2: increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0).

$a3 and $a4: increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0).

Recommended values: $R0=between 10 and 20, $cR1=0.925, $cR2=0.15

If $siginit is specified, strain is calculated from epsP=$sigInit/$E

```
if (sigInit!= 0.0) {
   double epsInit = sigInit/E;
   eps = trialStrain+epsInit;
} else {
   eps = trialStrain;
}
```

**FilippouEtAl1983**

> Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). “Effects of Bond Deterioration on Hysteretic Behavior of Reinforced Concrete Joints”. Report EERC 83-19, Earthquake Engineering Research Center, University of California, Berkeley.

Fig. 3.1.5.5 Steel02 Material – Material Parameters of Monotonic Envelope

Fig. 3.1.5.6 Steel02 Material – Default Hysteretic Behavior (NO isotropic hardening)

Example

The following is used to construct a Steel02 mataerial with a tag of **1**, a yield strength of $60.0** and an initial tangent stiffness of **30000,0**.

1. **Tcl Code**

```
uniaxialMaterial Steel02 60.0 30000.0 0.1 20.0 .925 .15
```

1. **Python Code**

```
uniaxialMaterial('Steel02',60.0,30000.0, 0.1, 20.0, .925, .15)
```

Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott)
