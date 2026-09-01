<!-- chunk_id: PySimple1_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/PySimple1.html",
 "title": "3.4.1.3. PySimple1 Material",
 "category": "command_manual",
 "manual_group": "model",
 "command": "PySimple1",
 "doc_section": "user/manual/model/uniaxialMaterials",
 "rel_path": "user/manual/model/uniaxialMaterials/PySimple1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 7217,
 "word_count": 1101,
 "has_code": true,
 "has_table": true
} -->

## 3.4.1.3. PySimple1 Material

This command is used to construct a PySimple1 uniaxial material object:

**`uniaxialMaterial PySimple1 $matTag $soilType $pult $Y50 $Cd <$c>`**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | integer tag identifying material |
| $soilType | *integer* | = 1 for clay; = 2 for sand. see note below. |
| $pult | *float* | Ultimate capacity of the p-y material. |
| $Y50 | *float* | Displacement at which 50% of pult is mobilized in monotonic loading. |
| $Cd | *float* | To set the drag resistance within a fully-mobilized gap as Cd*pult. |
| $c | *float* | The viscous damping term (dashpot). (optional Default = 0.0). |

Note

$soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation.

soilType = 2 Backbone of p-y curve approximates API (1993) sand relation.

The “p” or “pult” are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile].

The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Nonzero $c values are used to represent radiation damping effects. See theory below.

In general the hht algorithm is preferred over a newmark algorithm when using this material. This is due to the numerical oscillations that can develop with viscous damping forces under transient loading with certain solution algorithms and damping ratios.

The equations describing PySimple1 behavior are described in [[BoulangerEtAl1999]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/uniaxialMaterials/QzSimple1.html#boulangeretal1999). Only minor changes have been made in its implementation for OpenSees.

The nonlinear \(p-y\) behavior is conceptualized as consisting of elastic (\(p-y^e\)), plastic (\(p-y^p\)), and gap \((p-y^g)\) components in series. Radiation damping is modeled by a dashpot on the “far-field” elastic component \((p-y^e)\) of the displacement rate. The gap component consists of a nonlinear closure spring (\(p^c-y^g\)) in parallel with a nonlinear drag spring \((p^d-y^g)\). Note that \(y = y^e + y^p + y^g\), and that \(p = p^d + p^c\).

The plastic component has an initial range of rigid behavior between \(-C_r p_{ult} < p < C_r p_{ult}\) with \(C_r\) = the ratio of \(p/p_{ult} \), which is initially \(2 C_r p_{ult}\), translates with plastic yielding (kinematic hardening). The rigid range of \(p\) can be constrained to maintain a minimum size on both the positive and negative loading sides (e.g., 25% of \(p{ult}\)), and this is accomplished by allowing the rigid range to expand or contract as necessary. Beyond the rigid range, loading of the plastic \((p-y^p)\) component is described by:

\[p = p_{{ult}} - (p_{{ult}} - p_o) \left [\frac{c y_{50}}{c y_{50} + | z_p - z^p_0|} \right ]^n\]

where \(p_{ult}\) = the ultimate resistance of the \(p-y\) material in the current loading direction, \(p_o = p\) at the start of the current plastic loading cycle, \(y^p_o = y_p\) at the start of the current plastic loading cycle, \(c\) = constant to control the tangent modulus at the start of plastic yielding, and n = an exponent to control sharpness of the \(p-y^p\) curve.

The closure \((p^c-y^g)\) spring is described by:

\(p^c = 1.8 p_{{ult}} \left [\frac{y_{50}}{y_{50} + 50(y_o^{+} - y^g)} - \frac{y_{50}}{y_{50} + 50(y_o^{-} - y^g)} \right ] \) = memory term for the positive side of the gap, \(y_o^-\) and \(y_o^-\) were set as \(y_{50}/100\) and \(- y_{50}/100\), respectively. The factor of 1.8 brings \(p^c\) up to \(p_{ult}\) during virgin loading to \(y_o^+\) (or \(y_o^-\)). Gap enlargement follows logic similar to that of Matlock et al. (1978). The gap grows on the positive side when the plastic deformation occurs on the negative loading side. Consequently, the \(y_o^+\) value equals the opposite value of the largest past negative value of, \(y^p + y^g + 1.5 y_{50}\) where the \(1.5y_{50}\) represents some rebounding of the gap. Similarly, the \(y_o^-\) value equals the opposite value of the largest past positive value of \(y^p+y^g-1.5y_{50}\). This closure spring allows for a smooth transition in the load displacement behavior as the gap opens or closes.

The nonlinear drag \((p^d-y^g)\) spring is described by:

\[p^d = C_d p_{{ult}} - (C_d p_{{ult}} - p^d_o) \left [\frac{y_{50}}{y_{50} + 2| y^g - y^g_o|} \right ]^n\]

where \(C_d =\) ratio of the maximum drag force to the ultimate resistance of the p-y material, \(d^p_o =p^d\) at the start of the current loading cycle, and \(y^g_o = y^g\) at the start of the current loading cycle.

The flexibility of the above equations can be used to approximate different p-y backbone relations. Matlock’s (1970) recommended backbone for soft clay is closely approximated using \(c = 10\), \(n = 5\), and \(C_r = 0.35\). API’s (1993) recommended backbone for drained sand is closely approximated using \(c = 0.5\), \(n = 2\), and \(C_r = 0.2\). PySimple1 is currently implemented to allow use of these two default sets of values. Values of \(p_{ult}\), \(y_{50}\), and \(C_d\) must then be specified to define the \(p-y\) material behavior.

Viscous damping on the far-field (elastic) component of the p-y material is included for approximating radiation damping. For implementation in OpenSees the viscous damper is placed across the entire material, but the viscous force is calculated as proportional to the component of velocity (or displacement) that developed in the far-field elastic component of the material. For example, this correctly causes the damper force to become zero during load increments across a fully formed gap. In addition, the total force across the p-y material is restricted to pult in magnitude so that the viscous damper cannot cause the total force to exceed the near-field soil capacity. Users should also be familiar with numerical oscillations that can develop in viscous damper forces under transient loading with certain solution algorithms and damping ratios. In general, an HHT algorithm is preferred over a Newmark algorithm for reducing such oscillations in materials like PySimple1.

Example

The following constructs a PySimple material with tag **1**, soil type **2** (sand), \(p_{ult}\) of **4577.81** and a \(Y_{50}\) of **0.0066**. Cd is set to **0.0** for zero damping.

1. **Tcl Code**

```
uniaxialMaterial PySimple1 1  2  4577.81  0.0066 0.0
```

1. **Python Code**

```
uniaxialMaterial('PySimple1', 1, 2, 4577.81, 0.0066, 0.0)
```

Code Developed by: [Ross Boulanger](https://faculty.engineering.ucdavis.edu/boulanger/), UC Davis

**BoulangerEtAl1999**

> Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and Abghari, A. (1999). “Seismic soil-pile-structure interaction experiments and analyses.” Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 125(9): 750-759. Only minor changes have been made in its implementation for OpenSees.

**BoulangerEtAl1990**

> Boulanger, R.W., Curras, C.J., Kutter, B.L., Wilson, D.W., and Abghari, A. (1990). “Seismic Soil-pile-strcture interaction experiments and analysis”, Jornal of Geotechnical and Geoenvironmental Engineering, ASCS, 125(9):750-759.
