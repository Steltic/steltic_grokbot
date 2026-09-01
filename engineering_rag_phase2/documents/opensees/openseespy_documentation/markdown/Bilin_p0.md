<!-- chunk_id: Bilin_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Bilin.html",
 "title": "4.14.5.6. Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)",
 "category": "material",
 "command": "Bilin",
 "doc_section": "src",
 "rel_path": "src/Bilin.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5620,
 "word_count": 567,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.6. Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)

**uniaxialMaterial(*'Bilin'*, *matTag*, *K0*, *as_Plus*, *as_Neg*, *My_Plus*, *My_Neg*, *Lamda_S*, *Lamda_C*, *Lamda_A*, *Lamda_K*, *c_S*, *c_C*, *c_A*, *c_K*, *theta_p_Plus*, *theta_p_Neg*, *theta_pc_Plus*, *theta_pc_Neg*, *Res_Pos*, *Res_Neg*, *theta_u_Plus*, *theta_u_Neg*, *D_Plus*, *D_Neg*, *nFactor=0.0*)**

This command is used to construct a bilin material. The bilin material simulates the modified Ibarra-Krawinkler deterioration model with bilinear hysteretic response. Note that the hysteretic response of this material has been calibrated with respect to more than 350 experimental data of steel beam-to-column connections and multivariate regression formulas are provided to estimate the deterioration parameters of the model for different connection types. These relationships were developed by Lignos and Krawinkler (2009, 2011) and have been adopted by PEER/ATC (2010). The input parameters for this component model can be computed interactively from this [link](http://dimitrios-lignos.research.mcgill.ca/databases/). **Use the module Component Model.**

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `K0` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic stiffness |
| `as_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | strain hardening ratio for positive loading direction |
| `as_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | strain hardening ratio for negative loading direction |
| `My_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | effective yield strength for positive loading direction |
| `My_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | effective yield strength for negative loading direction (negative value) |
| `Lamda_S` ([float](https://docs.python.org/3/library/functions.html#float)) | Cyclic deterioration parameter for strength deterioration [E_t=Lamda_S*M_y; set Lamda_S = 0 to disable this mode of deterioration] |
| `Lamda_C` ([float](https://docs.python.org/3/library/functions.html#float)) | Cyclic deterioration parameter for post-capping strength deterioration [E_t=Lamda_C*M_y; set Lamda_C = 0 to disable this mode of deterioration] |
| `Lamda_A` ([float](https://docs.python.org/3/library/functions.html#float)) | Cyclic deterioration parameter for acceleration reloading stiffness deterioration (is not a deterioration mode for a component with Bilinear hysteretic response) [Input value is required, but not used; set Lamda_A = 0]. |
| `Lamda_K` ([float](https://docs.python.org/3/library/functions.html#float)) | Cyclic deterioration parameter for unloading stiffness deterioration [E_t=Lamda_K*M_y; set Lamda_k = 0 to disable this mode of deterioration] |
| `c_S` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of strength deterioration. The default value is 1.0. |
| `c_C` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of post-capping strength deterioration. The default value is 1.0. |
| `c_A` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of accelerated reloading deterioration. The default value is 1.0. |
| `c_K` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of unloading stiffness deterioration. The default value is 1.0. |
| `theta_p_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | pre-capping rotation for positive loading direction (often noted as plastic rotation capacity) |
| `theta_p_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (positive value) |
| `theta_pc_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | post-capping rotation for positive loading direction |
| `theta_pc_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | post-capping rotation for negative loading direction (positive value) |
| `Res_Pos` ([float](https://docs.python.org/3/library/functions.html#float)) | residual strength ratio for positive loading direction |
| `Res_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | residual strength ratio for negative loading direction (positive value) |
| `theta_u_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate rotation capacity for positive loading direction |
| `theta_u_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate rotation capacity for negative loading direction (positive value) |
| `D_Plus` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0. |
| `D_Neg` ([float](https://docs.python.org/3/library/functions.html#float)) | rate of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0. |
| `nFactor` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic stiffness amplification factor, mainly for use with concentrated plastic hinge elements (optional, default = 0). |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Bilinear_Hysteretic_Response_(Bilin_Material))
