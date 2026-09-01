<!-- chunk_id: YieldFunctions_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html",
 "title": "3.1.6.19.1. Yield Functions",
 "category": "command_manual",
 "manual_group": "material",
 "command": "YieldFunctions",
 "doc_section": "user/manual/material/ndMaterials/ASDPlasticMaterial",
 "rel_path": "user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3350,
 "word_count": 453,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.19.1. Yield Functions

Specifies the shape of the yield surface, i.e. the locus of points in stress-space where the response of the material is linear. Points outside the yield surface are not allowed. Yield surfaces can have parameters and internal variables which define its shape and location.

Yield Functions may define internal variables they need for their specification, as well as paramters. When specifying the `ASDPlasticMaterial` instance, once must provide the internal variables mentioned below, together with their hardening function.

Yield functions are also responsible for providing their stress-derivative (\(\mathbf{n} = \partial f / \partial \boldsymbol{\sigma}\)) as well as computing the hardening term \(H\) in the plastic multiplier (see [ASDPlasticMaterial Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#asdplastictheory)).

Available functions:

#### VonMises_YF

Defines a yield surface which corresponds to the [Von Mises Yield Criterion](https://en.wikipedia.org/wiki/Von_Mises_yield_criterion). Its definition is:

\[ \begin{align}\begin{aligned}\newcommand{\vec}[1]{\boldsymbol{#1}}
\newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }
\newcommand{\matorvec}[2]{
 \left[\begin{array}{#1}
     #2
 \end{array}\right]
 }
f(\vec{\sigma}) = \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha}) } - \sqrt{ \dfrac{2}{3}} k\\\vec{s} = \vec{\sigma} - p \vec{I}\end{aligned}\end{align} \]

Where \(p = -(\sigma_{11} + \sigma_{22} + \sigma_{33})/3\) is the mean stress (positive in compression), and \(\vec{I}\) is the Kronecker delta in Voigt notation (\(\vec{I} = \matorvec{cccccc}{1 & 1 & 1 & 0 & 0 & 0}^T\)). Finally, \(\vec{s}\) is the deviatoric part of the stress vector in Voigt notation.

Internal variables defined

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `BackStress` | Rank-6 Tensor | \(\vec{\alpha}\) | Backstress, definining the location in stress space for the axis of the Von-Mises cylinder. |
| `VonMisesRadius` | Scalar | \(k\) | Shear strength, definining the radius of the Von-Mises cylinder in stress space. |

Parameters required

#### DruckerPrager_YF

Defines a yield surface which corresponds to the [Drucker-Prager Yield Criterion](https://en.wikipedia.org/wiki/Drucker%E2%80%93Prager_yield_criterion). Its definition is:

\[f(\vec{\sigma}) = \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha}) } - \sqrt{ \dfrac{2}{3}} k p\]

Where all symbols are as before. In this case note that \(k\), defines the slope of the opening of the Drucker-Prager cone with respect to  \(p\), thus now the radius of the cone at a given confinement is \(kp\).

Internal variables defined

It uses the same variables as the Von-Mises yield function, but the `VonMisesRadius` is now unitless and should be defined with respect to a reference confinement.

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `BackStress` | Rank-6 Tensor | \(\vec{\alpha}\) | Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. |
| `VonMisesRadius` | Scalar | \(k\) | Shear strength at reference confinement, definining the radius of the DruckerPrager cone in stress space as \(kp\) |

Parameters required

#### RoundedMohrCoulomb_YF

Coming soon
