<!-- chunk_id: InitStrain_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/InitStrain.html",
 "title": "3.1.6.17. InitStrain Material Wrapper",
 "category": "command_manual",
 "manual_group": "material",
 "command": "InitStrain",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/InitStrain.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1335,
 "word_count": 174,
 "has_code": false,
 "has_table": true
} -->

## 3.1.6.17. InitStrain Material Wrapper

This command is used to construct a InitStrain material object. It is a wrapper that imposes an inital-strain to another nDMaterial such that \(\sigma = f\left (\varepsilon + \varepsilon_{0}\right )\).

**nDMaterial InitStrain $matTag $otherTag $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13>**

| Argument | Type | Description |
| --- | --- | --- |
| $matTag | *integer* | unique tag identifying this init-strain material wrapper |
| $otherTag | *integer* | unique tag identifying the previously defined nD material |
| $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13> | 1 or 6 *float* | initial strain values. If only one is given, a volumetric strain = eps0_11 is imposed. |

#### 3.1.6.17.1. Usage Notes

Limitations

- The only material formulation for the InitStrain material object is “ThreeDimensional”.
- The only material formulation allowed for the sub-material object is “ThreeDimensional”.

Responses

- All responses available for the nDMaterial object: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.

Example 1 - Simple Linear Validation

[`InitStrainExample.py`](https://OpenSees.github.io/OpenSeesDocumentation/_downloads/b24e9ffc94fc4ef12ef20908c7dc0ee0/InitStrainExample.py)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
