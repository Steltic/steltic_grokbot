<!-- chunk_id: J2Plasticity_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/J2Plasticity.html",
 "title": "3.1.6.3. J2 Plasticity Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "J2Plasticity",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/J2Plasticity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1516,
 "word_count": 225,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.3. J2 Plasticity Material

This command is used to construct an multi dimensional material object that has a von Mises (J2) yield criterion and isotropic hardening.

**nDMaterial J2Plasticity $matTag $K $G $sig0 $sigInf $delta $H**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | unique tag identifying material |
| $K | *float* | bulk modulus |
| $G | *float* | shear modulus |
| $sig0 | *float* | initial yield stress |
| $sigInf | *float* | final saturation yield stress |
| $delta | *float* | exponential hardening parameter |
| $H | *float* | linear hardening parameter |

Note

The material formulations for the J2 object are “ThreeDimensional,” “PlaneStrain,” “Plane Stress,” “AxiSymmetric,” and “PlateFiber.”

THEORY:

The theory for the non hardening case can be found [[1]]

J2 isotropic hardening material class

Elastic Model

\[\sigma = K*trace(\epsilon_e) + (2*G)*dev(\epsilon_e)\]

Yield Function

\[\phi(\sigma,q) = || dev(\sigma) || - \sqrt(\tfrac{2}{3}*q(xi)\]

Saturation Isotropic Hardening with linear term

\[q(xi) = \sigma_0 + (\sigma_\inf - \sigma_0)*exp(-delta*\xi) + H*\xi\]

Flow Rules

\[ \begin{align}\begin{aligned}\dot {\epsilon_p} = \gamma * \frac{\partial \phi}{\partial \sigma}\\\dot \xi = -\gamma * \frac{\partial \phi}{\partial q}\end{aligned}\end{align} \]

Linear Viscosity: \(\gamma = \frac{\phi}{\eta}\) ( if \(\phi > 0\) )

Backward Euler Integration Routine Yield condition enforced at time n+1

set \(\eta = 0\) for rate independent case

Code Developed by: **Ed Love**
