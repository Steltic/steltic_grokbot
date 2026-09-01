<!-- chunk_id: ElasticityType_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html",
 "title": "3.1.6.19.3. Elasticity Types",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ElasticityType",
 "doc_section": "user/manual/material/ndMaterials/ASDPlasticMaterial",
 "rel_path": "user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2170,
 "word_count": 278,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.19.3. Elasticity Types

These components define the stress-strain relationship for the linear part of the model (see [ASDPlasticMaterial Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#asdplastictheory)).

\[\newcommand{\vec}[1]{\boldsymbol{#1}}
\vec{\sigma} = \vec{E} \vec{\epsilon}\]

Where the operator \(\vec{E}\) may depend on the material state, parameters, etc.

#### LinearIsotropic3D_EL

A classic!

\[\begin{split}\vec{E}\,=\,{\frac {E}{(1+\nu )(1-2\nu )}}{\begin{bmatrix}1-\nu &\nu &\nu &0&0&0\\\nu &1-\nu &\nu &0&0&0\\\nu &\nu &1-\nu &0&0&0\\0&0&0&{\frac {1-2\nu }{2}}&0&0\\0&0&0&0&{\frac {1-2\nu }{2}}&0\\0&0&0&0&0&{\frac {1-2\nu }{2}}\end{bmatrix}}\end{split}\]

Parameters required

| Parameter name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `YoungsModulus` | scalar | \(E\) | Young’s modulus |
| `PoissonsRatio` | scalar | \(\nu\) | Poisson’s ratio |

#### DuncanChang_EL

This is a hypoelastic model that features pressure dependent behavior. It is composed of an isotropic elastic model where the Young’s modulus has the following dependency on the maximum principal stress \(\sigma_3\) (it is assumed that \(\sigma_1 \leq \sigma_2 \leq \sigma_3 < 0\)).

\[E(\sigma_3) = E_{ref} \cdot p_{ref} \cdot \left(\dfrac{\vert \sigma_3 \vert}{ p_{ref}} \right)^n\]

Where \(E_{ref}\) (dimensionless) specifies the Young’s modulus at reference pressure \(p_{ref}\) and \(n\) is a material constant. A cut-off maximum confinement pressure \(\sigma_{3max}\) at which the Young’s modulus will be evaluated should the confinement be greater than that value.

Parameters required

| Parameter name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `ReferenceYoungsModulus` | scalar | \(E_{ref}\) | Dimensionless reference Young’s modulus at reference pressure \(p_{ref}\). |
| `PoissonsRatio` | scalar | \(\nu\) | Poisson’s ratio |
| `ReferencePressure` | scalar | \(p_{ref}\) | Reference pressure for the definition of Young’s modulus. |
| `DuncanChang_MaxSigma3` | scalar | \(\sigma_{3max}\) | Maximum confinement stress. |
| `DuncanChang_n` | scalar | \(\nu\) | Exponent for Duncan-Chang law. |
