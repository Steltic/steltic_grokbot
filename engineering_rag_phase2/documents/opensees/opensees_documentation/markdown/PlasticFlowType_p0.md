<!-- chunk_id: PlasticFlowType_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html",
 "title": "3.1.6.19.2. Plastic Flow Directions",
 "category": "command_manual",
 "manual_group": "material",
 "command": "PlasticFlowType",
 "doc_section": "user/manual/material/ndMaterials/ASDPlasticMaterial",
 "rel_path": "user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3582,
 "word_count": 449,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.19.2. Plastic Flow Directions

Specifies the direction of plastic flow \(\mathbf{m}\) used to define the evolution of the plastic strain (see [ASDPlasticMaterial Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#asdplastictheory)).

Plastic Flow Directions may define internal variables they need for their specification, as well as paramters. When specifying the `ASDPlasticMaterial` instance, once must provide the internal variables mentioned below, together with their hardening function, when defining the internal variables.

Available functions:

#### VonMises_PF

Defines a plastic flow direction derived from the [Von Mises Yield Criterion](https://en.wikipedia.org/wiki/Von_Mises_yield_criterion). Its definition. It is the stress-derivative of the [VonMises_YF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#vonmises-yf).

\[\newcommand{\vec}[1]{\boldsymbol{#1}}
\mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}}\]

Internal variables defined

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `BackStress` | Rank-6 Tensor | \(\vec{\alpha}\) | Backstress, definining the location in stress space for the axis of the Von-Mises cylinder. |

Parameters required

#### DruckerPrager_PF

Defines a plastic flow direction derived from the [Drucker-Prager Yield Criterion](https://en.wikipedia.org/wiki/Drucker%E2%80%93Prager_yield_criterion).  It is the stress-derivative of the [DruckerPrager_YF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#druckerprager-yf).

\[\mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}} - \dfrac{\sqrt{2/3}k}{3} \vec{I} ;\]

Internal variables defined

It uses the same variables as the Von-Mises yield function, but the `VonMisesRadius` is now unitless and should be defined with respect to a reference confinement.

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `BackStress` | Rank-6 Tensor | \(\vec{\alpha}\) | Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. |
| `VonMisesRadius` | Scalar | \(k\) | Shear strength at reference confinement, definining the radius of the DruckerPrager cone in stress space as \(kp\) |

Parameters required

#### ConstantDilatancy_PF

Von-Mises PF provides no volumetric change (dilatancy) during plasticity. On the other hand Drucker-Prager PF provides a constant negative volumetric change which is proportional to the current value of the \(k\) parameter. This PF defines a controllable dilatancy during plasticity by specifying a constant dilatancy coeficient \(D\).

\[\mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}} - \dfrac{D}{3} \vec{I} ;\]

Internal variables defined

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `BackStress` | Rank-6 Tensor | \(\vec{\alpha}\) | Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. |

Parameters required

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `Dilatancy` | Scalar | \(D\) | Defines the rate of dilatancy with plastic flow. Positive values specify negative plastic volumetric change. |
