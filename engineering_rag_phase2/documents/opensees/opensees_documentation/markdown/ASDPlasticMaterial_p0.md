<!-- chunk_id: ASDPlasticMaterial_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial.html",
 "title": "3.1.6.19. ASDPlasticMaterial",
 "category": "command_manual",
 "manual_group": "material",
 "command": "ASDPlasticMaterial",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/ASDPlasticMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 18141,
 "word_count": 1959,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.19. ASDPlasticMaterial

This command is used to construct an `ASDPlasticMaterial` material object. `ASDPlasticMaterial` implements a large family of constitutive models based on the classical theory of elastoplasticity. Users build new constitutive models by selecting the yield function, plastic-flow direction, elasticity law, and hardening models for the internal variables from several possible options for each component.

To create a new model, specify the Yield Function type (`$YieldFunctionType`), Plastic Flow type (`$PlasticFlowType`), and Elasticity type (`$ElasticityType`). All internal variables and model parameters are set to zero unless specified by the user, which might or not make sense depending on context, and this initialization is printed out to the screen.

After setting the `$YieldFunctionType`, `$PlasticFlowType` and `$ElasticityType`, you can give initial values to internal variables within the `Begin_Internal_Variables` … `End_Internal_Variables` block. Then, the `Begin_Model_Parameters` … `End_Model_Parameters` block is used to provide model parameter values (these can be changed during the analysis with the `setParameter` command as expected). Finally, model integration options are set within the `Begin_Integration_Options` … `End_Integration_Options` code block. Specification blocks can occur in any order or ommitted.

The complete command looks as follows:

```
nDMaterial ASDPlasticMaterial $tag
   $YieldFunctionType
   $PlasticFlowType $
   ElasticityType
   $IV_TYPE
   Begin_Internal_Variables
      $InternalVariable1 $$double_value1 $$double_value2... $$double_valueN1
      $InternalVariable2 $$double_value1 $$double_value2... $$double_valueN2
      #... (depends on how many internal variables the particular selected model has)
   End_Internal_Variables
   Begin_Model_Parameters
      $ModelParameters1 $$double_value1
      $ModelParameters2 $$double_value2
      #... (depends on how many model parameters the particular selected model has)
   End_Model_Parameters
   Begin_Integration_Options
      f_relative_tol $double_value
      stress_relative_tol $double_value
      n_max_iterations $int_value
      return_to_yield_surface (0 or 1)
      method (string) : Forward_Euler | Runge_Kutta_45_Error_Control
   End_Integration_Options
```

Explanation

| Argument | Type | Description |
| --- | --- | --- | --- | --- |
| $tag | *integer* | Unique tag identifying this material. |
| $YieldFunctionType | *string* | Mandatory. Yield function to be used -> [Yield Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#yieldfunctiontype) |
| $PlasticFlowType | *string* | Mandatory. Plastic flow direction to be used -> [Plastic Flow Directions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html#plasticflowtype) |
| $ElasticityType | *string* | Mandatory. Elastic model to be used -> [Elasticity Types](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html#elasticitytype) |
| $IV_TYPE | *string* | Mandatory. Hardening model for internal variables. Admitted types depend on YF, PF, and EL chosen. |
| Begin_Internal_Variables | *string* | Optional. Marks the beginning of the code block to set the internal variables. If ommitted, all internal variables are initialized to zero. You can specify as many of the following variables as wanted. Ommitted variables are initialized to zero. Number and name of variables that can be set is model dependent (once YF, PF, and EL are specified) |
| $InternalVariable1 | \|list of name/value pairs\| | Initial value of internal variable1. Dimension depends on internal variable type. |
| $InternalVariable2 | \|list of name/value pairs\| | Initial value of internal variable2. |
| – | – | … (input as many as model supports) |
| End_Internal_Variables | *string* | Mandatory if block started. Marks the end of the code block to set the internal variables |
| Begin_Model_Parameters | *string* | Optional. Marks the beginning of the code block to set the model parameters |
| $ModelParameters | \|list of name/value pairs\| | Values for parameters of the models to be used. This depends on the particular choices of `$YieldFunctionType`, `$PlasticFlowType`, `$ElasticityType`, and `$IV_type`. |
| – | – | … (input as many as model supports) |
| End_Model_Parameters | *string* | Mandatory if block started. Marks the beginning of the code block to set the model parameters |
| Begin_Integration_Options | *string* | Optional. Marks the beginning of the code block to set the integration options. You can set any ammount |
| End_Integration_Options | *string* | Mandatory if block started. Marks the beginning of the code block to set the model parameters |

The [Yield Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#yieldfunctiontype), [Plastic Flow Directions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html#plasticflowtype), and [Elasticity Types](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html#elasticitytype) have different variables and parameters to be set.

Specification of internal variables (`$IV_TYPE`)

All internal variables are specified in a single string with no spaces. Internal variables specifications are separated with a colon `:`. After the name of the internal variable, the name of the hardening function must be provided in parenthesis. The specification string must end in a colon. The syntax is, thus:

```
InternalVariable1(HardeningFunction1):InternalVariable2(HardeningFunction2):
```

Internal variables are required for the yield function and plastic flow direction (see speficic components for details), and all internal variables must be provided with their hardening function otherwise instantiation fails.

Note

Any internal variable or parameter that is not specified is set to zero by default.

Arguments detailed description

- [3.1.6.19.1. Yield Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html)

  - [VonMises_YF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#vonmises-yf)
  - [DruckerPrager_YF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#druckerprager-yf)
  - [RoundedMohrCoulomb_YF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/YieldFunctions.html#roundedmohrcoulomb-yf)
- [3.1.6.19.2. Plastic Flow Directions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html)

  - [VonMises_PF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html#id1)
  - [DruckerPrager_PF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html#id2)
  - [ConstantDilatancy_PF](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/PlasticFlowType.html#id3)
- [3.1.6.19.3. Elasticity Types](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html)

  - [LinearIsotropic3D_EL](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html#id1)
  - [DuncanChang_EL](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/ElasticityType.html#id2)
- [3.1.6.19.4. Hardening Functions](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html)

  - [Hardening Functions for Scalar-Valued Internal Variables](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html#hardening-functions-for-scalar-valued-internal-variables)
  - [Hardening Functions for Tensor-Valued Internal Variables](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/ASDPlasticMaterial/HardeningFunctions.html#hardening-functions-for-tensor-valued-internal-variables)

#### 3.1.6.19.5. ASDPlasticMaterial Theory

The `ASDPlasticMaterial` internally uses Voigt notation to represent tensors.

\[\begin{split}\newcommand{\vec}[1]{\boldsymbol{#1}}
\newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }
\newcommand{\matorvec}[2]{
 \left[\begin{array}{#1}
     #2
 \end{array}\right]
 }
\vec{\epsilon} = \matorvec{c}{\epsilon_{11} \\ \epsilon_{22} \\ \epsilon_{33} \\ \gamma_{12} \\ \gamma_{23} \\ \gamma_{13} }
\vec{\sigma} = \matorvec{c}{\sigma_{11} \\ \sigma_{22} \\ \sigma_{22} \\ \tau_{12} \\ \tau_{23} \\ \tau_{13} }\end{split}\]

Where \(\gamma_{ij} = 2 \epsilon_{ij}\).

The material recieves the total (trial) strain \(\vec{\epsilon}^{\text{trial}}\) from the finite element that contains it. From this, the trial strain increment is computed by subtracting the previously committed total strain:

\[\Delta \vec{\epsilon}^{\text{trial}} = \vec{\epsilon}^{\text{trial}} - \vec{\epsilon}^{\text{commit}}\]

The elastic trial stress increment is computed using the elasticity law (depending on choice of `$ElasticityType`), which may depend on stress (\(\sigma\)) internal variables (represented as the list of internal variables of the model \(\left\lbrace iv \right\rbrace\)) and parameters (represented as the list of parameters of the model \(\left\lbrace param \right\rbrace\)):

\[\Delta \vec{\sigma}^{\text{trial}} = \vec{E}^{\text{current}}(\state) \Delta \vec{\epsilon}^{\text{trial}}\]

\(\vec{E}^{\text{current}}(\state )\) is the 6x6 elastic tangent operator. The trial strain is computed as \(\mathbf{\sigma}^{\text{trial}} = \mathbf{\sigma}^{\text{commit}} + \Delta \sigma^{\text{trial}}\). With this predictor, the yield-function (\(f(\state )\)) is evaluated to see whether the stress point falls inside or outside the yield surface (depending on choice of `$YieldFunctionType`). If it falls inside, then the step is elastic and the integration stops. Otherwise, we need to do some plasticity for which the explicit Forward-Euler version will be used to present all components.

The exact intersection point with the yield function is computed iteratively with a robust Brent algorithm. The trial stress increment is advanced to the yield-surface intersection point and plastic integration continues. Starting from \(\Delta \epsilon^{\text{trial}}\) corresponding to a \(\Delta \sigma^{\text{trial}}\)  on the yield surface, the strain increment is separated into elastic and plastic components (the “trial” qualifier es removed and implied in what follows):

\[\Delta \vec{\epsilon}   = \Delta \epsilon^{el} + \Delta \epsilon^{pl}\]

The plastic increment comes from:

\[\Delta \vec{\epsilon}^{pl}   = \Delta \lambda \cdot \mathbf{m} (\state)\]

Where the vector \(\mathbf{m} (\state)\) is the plastic flow direction defined with the `$PlasticFlowType` option and :math:`Delta lambda` is the plastic multiplier defined as:

\[\Delta \lambda\ = \dfrac{ \vec{n}^T E \Delta \vec{\epsilon} }{ \vec{n}^T E \Delta \vec{m} - H }\]

Where \(\mathbf{n} (\state)\) is the outward normal to the yield surface, and \(H\) is the hardening term due to internal variable evolution. For example, if the model has two internal variables \(s\) a scalar internal variable and  \(\vec{T}\) a tensor internal variable (e.g. \(\left\lbrace iv \right\rbrace = \left\lbrace s,\, \vec{T} \right\rbrace\)), the hardening term is computed with:

\[H = \left.\dfrac{\partial f}{\partial s}\right\Vert_{(\state)} h_s(\state) + \left.\dfrac{\partial f}{\partial \vec{T}}\right\Vert_{(\state)} h_s(\state) \cdot \vec{h}_T(\state)\]

Here the hardening functions of the scalar internal varialbe (a scalar) \(h_s(\state)\) and the tensor internal variable \(\vec{h}_T(\state)\) are introduced. These are specified using the `$IV_type` option.

Finally, the trial stress increment considering plasticity is computed using:

\[\Delta \vec{\sigma}^{\text{trial}} = \vec{E}(\state) \cdot \Delta \vec{\epsilon}^{pl}\]

And the new trial state of the material is computed:

\[ \begin{align}\begin{aligned}\vec{\sigma}^{\text{trial}} = \vec{\sigma}^{\text{commit}} + \Delta \vec{\sigma}^{\text{trial}}\\s^{\text{trial}} = s^{\text{commit}} + \Delta \lambda  h_s(\state)\\\vec{T}^{\text{trial}} = \vec{T}^{\text{commit}} + \Delta \lambda  \vec{h}_T(\state)\end{aligned}\end{align} \]

After this, an aditional algorithm can be called to return the stress point to the yield surface (recommended) as well as specific provisions in case integration is ocurring near an apex of the yield surface.

#### 3.1.6.19.6. Integration Options

| Parameter | Type | Description |
| --- | --- | --- | --- | --- |
| $f_relative_tol | \|double\| | Relative tolerance to evaluate the yield function crossing. |
| $stress_relative_tol | \|double\| | Tolerance for the convergece of the integration algorithm. |
| $n_max_iterations | \|int\| | Maximum number of iterations for constitutive integration. |
| $return_to_yield_surface | \|0 or 1\| | Whether to apply a return to yield surface algorithm after integration convergence. |
| $method | *string* | Constitutive integration method. Options: `Forward_Euler`, `Runge_Kutta_45_Error_Control` |

The default integration method is **Runge_Kutta_45_Error_Control** that uses the classical RK45 ODE integration algorithm employing a 4-th order prediction of the stress increment together with a 5-order prediction to estimate the integration error. In this scheme the strain increment provided by the element to the Gauss point is sub-divided into sub-increments, a process which is automated such that the provided **$stress_relative_tol** is met. This method is provided as a robust standard method which is applicable across all possible combinations of components, although there are possibly better approaches for specific cases which might become available in the future.

The different parameters are activated depending on the integration algorithm selected. The *Forward_Euler* algorithm only uses the **$return_to_yield_surface** parameter, while **Runge_Kutta_45_Error_Control** uses the rest.

The **$f_relative_tol** parameter comes into play when the yield surface is being crossed, that is, when the previous (committed) stress is within the yield surface and the elastic prediction of the stress increment brings the stress state beyond the yield surface. In that case, an elastic increment occurs until the yield surface is touched which requires iterations with the Brent root finding algorithm. This is used by both currently available integration methods.

#### 3.1.6.19.7. Other Features

General parameters

These parameters are defined for all models.

| Parameter | Type | Description |
| --- | --- | --- |
| `MassDensity` | scalar | Defines the material mass density \(\rho\). |
| `InitialP0` | scalar | Defines the initial mean pressure at which material constants will be evaluated at the first step. |

Responses  (setResponse and getResponse behavior)

- *Valid queries for recorders*. stresses for stress, strains for strains, and pstrains for plastic strains.
- You can also request any and all internal variables by their specific name as an output.

setParameter behavior

- Not yet provided.

#### 3.1.6.19.8. Implementation details

`ASDPlasticMaterial` is implemented using C++ template metaprogramming, with a header-only design and using the “eigen” C++ library for high-performance array operations. This design provides modularity and the ability to mix and match components to create new models, while also providing high-performance because runtime polymorphism is avoided.

#### 3.1.6.19.9. Example

The following example defines an instance of `ASDPlasticMaterial` with a Drucker-Prager yield function, a constant dilatancy plastic-flow direction, elastic-isotropic elasticity law and linear hardening for both internal variables.

TCL code

```
nDMaterial ASDPlasticMaterial 1 \
    DruckerPrager_YF \
    ConstantDilatancy_PF \
    LinearIsotropic3D_EL \
    BackStress(TensorLinearHardeningFunction):VonMisesRadius(ScalarLinearHardeningFunction): \
    Begin_Internal_Variables \
        VonMisesRadius 1. \
        BackStress 0. 0. 0. 0. 0. 0. \
    End_Internal_Variables \
    Begin_Model_Parameters \
        YoungsModulus 1. \
        PoissonsRatio 0. \
        TensorLinearHardeningParameter 0. \
        ScalarLinearHardeningParameter 0. \
        Dilatancy 0.02 \
        MassDensity 2000. \
    End_Model_Parameters
```

Python code

```
ops.nDMaterial("ASDPlasticMaterial", 1,
"DruckerPrager_YF",
"ConstantDilatancy_PF",
"LinearIsotropic3D_EL",
"BackStress(TensorLinearHardeningFunction):VonMisesRadius(ScalarLinearHardeningFunction):",
"Begin_Internal_Variables",
    "VonMisesRadius", 1.,
    "BackStress", 0., 0., 0., 0., 0., 0.,
"End_Internal_Variables",
"Begin_Model_Parameters",
    "YoungsModulus", 1.,
    "PoissonsRatio", 0.,
    "TensorLinearHardeningParameter", 0.,
    "ScalarLinearHardeningParameter", 0.,
    "Dilatancy", 0.02,
    "MassDensity", 2000.,
"End_Model_Parameters",
)
```

If you subject this material to strain-controlled cyclic loading you get the following response.

Fig. 3.1.6.4 (Left) strain response with input strain history in blue and plastic strains in orange. (Right) stress response.

Plotted in principal-stress space you can see the material soften as it dilates.

Fig. 3.1.6.5 Response of the material in principal-stress space with Drucker-Prager surface for reference.

Code Developed by: **José A. Abell** (UANDES, Chile and ASDEA), **Guido Camata** and **Massimo Petracca**  (ASDEA Software, Italy).
