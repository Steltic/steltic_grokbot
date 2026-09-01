<!-- chunk_id: J2Plasticity_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/J2Plasticity.html",
 "title": "4.15.1.3. J2Plasticity",
 "category": "general",
 "command": "J2Plasticity",
 "doc_section": "src",
 "rel_path": "src/J2Plasticity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1820,
 "word_count": 200,
 "has_code": false,
 "has_table": true
} -->

## 4.15.1.3. J2Plasticity

**nDMaterial(*'J2Plasticity'*, *matTag*, *K*, *G*, *sig0*, *sigInf*, *delta*, *H*)**

This command is used to construct an multi dimensional material object that has a von Mises (J2) yield criterium and isotropic hardening.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `K` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus |
| `G` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus |
| `sig0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial yield stress |
| `sigInf` ([float](https://docs.python.org/3/library/functions.html#float)) | final saturation yield stress |
| `delta` ([float](https://docs.python.org/3/library/functions.html#float)) | exponential hardening parameter |
| `H` ([float](https://docs.python.org/3/library/functions.html#float)) | linear hardening parameter |

The material formulations for the J2Plasticity object are:

- `'ThreeDimensional'`
- `'PlaneStrain'`
- `'Plane Stress'`
- `'AxiSymmetric'`
- `'PlateFiber'`

J2 isotropic hardening material class

Elastic Model

\[\sigma = K * trace(\epsilon_e) + (2 * G) * dev(\epsilon_e)\]

Yield Function

\[\phi(\sigma,q) = || dev(\sigma) ||  - \sqrt(\tfrac{2}{3}*q(x_i))\]

Saturation Isotropic Hardening with linear term

\[q(x_i) = \sigma_0 + (\sigma_\infty - \sigma_0)*exp(-delta*\xi) + H*\xi\]

Flow Rules

\[ \begin{align}\begin{aligned}\dot {\epsilon_p} =  \gamma * \frac{\partial \phi}{\partial \sigma}\\\dot \xi  = -\gamma * \frac{\partial \phi}{\partial q}\end{aligned}\end{align} \]

Linear Viscosity

\[\gamma = \frac{\phi}{\eta}  ( if   \phi > 0 )\]

Backward Euler Integration Routine Yield condition enforced at time n+1

set \(\eta\) = 0 for rate independent case
