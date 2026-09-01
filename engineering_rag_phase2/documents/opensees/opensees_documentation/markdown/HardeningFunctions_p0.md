<!-- chunk_id: HardeningFunctions_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html",
 "title": "3.1.6.19.4. Hardening Functions",
 "category": "command_manual",
 "manual_group": "material",
 "command": "HardeningFunctions",
 "doc_section": "user/manual/material/ndMaterials/ASDPlasticMaterial",
 "rel_path": "user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3007,
 "word_count": 403,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.19.4. Hardening Functions

Internal variables evolve accoding with their own laws to provide plastic hardening to the constitutive model. These laws are specified as hardening functions that specify an ODE for the evolution of the internal variable. Two types of internal variable are considered: scalar-valued and tensor-valued internal variables. These evolve in the following manner:

\[ \begin{align}\begin{aligned}\newcommand{\vec}[1]{\boldsymbol{#1}}
\newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }\\s^{\text{trial}} = s^{\text{commit}} + \Delta \lambda  h_s(\state)\\\vec{T}^{\text{trial}} = \vec{T}^{\text{commit}} + \Delta \lambda  \vec{h}_T(\state)\end{aligned}\end{align} \]

Where \(s\) is a scalar-valued internal variable and \(\vec{T}\) is tensor-valued. These functions are used to define the hardening term in the plastic multiplier (see [ASDPlasticMaterial Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html#asdplastictheory)).

Available functions:

#### Hardening Functions for Scalar-Valued Internal Variables

**ScalarLinearHardeningFunction**

Provides linear hardening for the scalar variable, as a function of the plastic flow direction :

\[h_s(\state) = H \cdot \sqrt{  (2/3) \vec{m} \cdot \vec{m} }\]

Where \(\vec{m}\) is the plastic flow direction computed at the current state.

Parameters required

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `ScalarLinearHardeningParameter` | scalar | \(H\) | Linear hardening constant |

#### Hardening Functions for Tensor-Valued Internal Variables

**TensorLinearHardeningFunction**

Provides linear hardening for the tensor variable, as a function of the deviatoric plastic flow direction :

\[h_T(\state) = H \vec{m}_{dev}\]

Where \(\vec{m}_{dev}\) is the deviatoric part of the plastic flow direction computed at the current state.

Parameters required

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `TensorLinearHardeningFunction` | scalar | \(H\) | Linear hardening constant |

**ArmstrongFrederickHardeningFunction**

A type of hardening with saturation.

\[h_T(\state) = (2 / 3) h_a \vec{m}_{dev} - c_r \sqrt{  (2/3) \vec{m}_{dev} \cdot \vec{m}_{dev} } \cdot  \vec{T}\]

Where \(\vec{m}_{dev}\) is the deviatoric part of the plastic flow direction computed at the current state. Model paramters \(h_a\) and \(c_r\)  specify the maximum (saturation) value and the saturation rate. The saturation value for the internal variable will be such that:

\[\Vert \vec{T} \Vert = \sqrt{\dfrac{2}{3}} \dfrac{h_a}{c_r}\]

Setting \(c_r = 0\) results in linear hardening.

Parameters required

| IV Name | Type | Symbol | Description |
| --- | --- | --- | --- |
| `AF_ha` | scalar | \(h_a\) | Model constant for the linear part of the hardening model. Controls the rate of saturation. |
| `AF_cr` | scalar | \(c_r\) | Model constant for saturation part of the hardening model. Controls the saturation value. |
