<!-- chunk_id: TzSimple1_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/TzSimple1.html",
 "title": "3.1.5.33. TzSimple1 Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "TzSimple1",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/TzSimple1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4851,
 "word_count": 764,
 "has_code": true,
 "has_table": true
} -->

## 3.1.5.33. TzSimple1 Material

This command is used to construct a TzSimple1 uniaxial material object:

**uniaxialMaterial TzSimple1 $matTag $tzType $tult $z50 <$c>**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material |
| $soilType | *integer* | 1 or 2. see note. |
| $tult | *float* | Ultimate capacity of the t-z material. see notes |
| $Z50 | *float* | Displacement at which 50% of tult is mobilized in monotonic loading. |
| $c | *float* | The viscous damping term (optional: default = 0.0). see note. |

Note

soilType = 1 Backbone of t-z curve approximates Reese and O’Neill (1987)

soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation.

The argument tult is the ultimate capacity of the t-z material. Note that “t” or “tult” are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].

The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Nonzero c values are used to represent radiation damping effects

EQUATIONS and EXAMPLERESPONSES:

The equations describing PySimple1 behavior are described in [BoulangerEtAl1990]. Only minor changes have been made in its implementation for OpenSees.

The nonlinear t-z behavior is conceptualized as consisting of elastic (\(t-z^e\)) and plastic (\(t-z^p\)) components in series. Radiation damping is modeled by a dashpot on the “far-field” elastic component (\(t-z^e\)) of the displacement rate. Note that \(z = z^e + z^p\), and that \(t = t^e = t^p\).

The plastic component is described by:

\[t^p = t_{ult} - (t_{ult} - t^p_0) \left [\frac{c z_{50}}{c z_{50} + | z_p - z^p_0|} \right ]\]

where \(t_{ult} = \) at the start of the current plastic loading cycle, \(z^p_0 = z^P\) at the start of the current plastic loading cycle, and c = a constant and n = an exponent that define the shape of the \(t-z^p\) curve.

The elastic component can be conveniently expressed as:

\[t^e = C_e \frac{t_{ult}}{z_{50}} z^e\]

where \(C_e\) = a constant that defines the normalized elastic stiffness. The value of \(C_e\) is not an independent parameter, but rather depends on the constants c & n (along with the fact that \(t = 0.5 t_{ult}\) at \(z = z_{50}\)).

The flexibility of the above equations can be used to approximate different t-z backbone relations. Reese and O’Neill’s (1987) recommended backbone for drilled shafts is closely approximated using c = 0.5, n = 1.5, and Ce = 0.708. Mosher’s (1984) recommended backbone for axially loaded piles in sand is closely approximated using c = 0.6, n = 0.85, and Ce = 2.05. TzSimple1 is currently implemented to allow use of these two default sets of values. Values of tult and z50 must then be specified to define the t-z material behavior.

Viscous damping on the far-field (elastic) component of the t-z material is included for approximating radiation damping. For implementation in OpenSees the viscous damper is placed across the entire material, but the viscous force is calculated as proportional to the component of velocity (displacement rate) that developed in the far-field elastic component of the material. In addition, the total force across the t-z material is restricted to tult in magnitude so that the viscous damper cannot cause the total force to exceed the near-field soil capacity. Users should also be familiar with numerical oscillations that can develop in viscous damper forces under transient loading with certain solution algorithms and damping ratios. In general, an HHT algorithm is preferred over a Newmark algorithm for reducing such oscillations in materials like TzSimple1.

Examples of the cyclic loading response of TzSimple1 are given in the following plots. Note that the response for tzType = 2 has greater nonlinearity at smaller displacements (and hence greater hysteretic damping) and that it approaches tult more gradually (such that t/tult is still well below

Example

The following constructs a TzSimple material with tag **102**, soil type **2** (Mosher relationship for backbone), \(t_{ult}\) of **0.734** and a \(Z_{50}\) of **0.0000254**. C is set to **0.0** for zero damping.

1. **Tcl Code**

```
uniaxialMaterial TzSimple1 102  2  0.734  2.54e-5  0.0
```

1. **Python Code**

```
uniaxialMaterial('TzSimple1', 102, 2, 0.734, 2.54e-5, 0.0)
```

Code Developed by: [Ross Boulanger](https://faculty.engineering.ucdavis.edu/boulanger/), UC Davis

**BoulangerEtAl1999**

> Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and Abghari, A. (1999). “Seismic soil-pile-structure interaction experiments and analyses.” Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 125(9): 750-759. Only minor changes have been made in its implementation for OpenSees.
