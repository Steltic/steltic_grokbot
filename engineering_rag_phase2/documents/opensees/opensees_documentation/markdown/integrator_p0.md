<!-- chunk_id: integrator_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator.html",
 "title": "3.2.6. integrator Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "integrator",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/integrator.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2634,
 "word_count": 231,
 "has_code": false,
 "has_table": true
} -->

## 3.2.6. integrator Command

This command is used to construct the Integrator object.

**The Integrator object is used for the following:**

> 1. determine the predictive step for time t+dt, \(\Delta U\) in static analysis, \(\Delta U\), \(\Delta \dot U\), and \(\Delta \ddot U\) in a transient analysis.
> 2. specify the tangent matrix and residual vector at any iteration, i.e. what constitutes the \(A\) matrix and \(b\) vector in \(Ax=b\).
> 3. determine the corrective step based on the x vector, i.e. given \(x\) what is \(\Delta U\) in static analysis, \(\Delta U\), \(\Delta \dot U\), and \(\Delta \ddot U\) in a transient analysis.

**numberer numbererType? arg1? ...**

| Argument | Type | Description |
| --- | --- | --- |
| $numbererType | *string* | the numberer type |
| $args | *list* | a list of arguments for that type |

The type of integrator used in the analysis is dependent on whether it is a static analysis or transient analysis. The following contain information about numbererType? and the args required for each of the available integrator types:

Static Integrators:

- [3.2.6.1. LoadControl Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/LoadControl.html)
- [3.2.6.2. DisplacementControl Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/DisplacementControl.html)
- [3.2.6.3. MinimumUnbalancedDisplacementNorm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/MinimumUnbalancedDisplacementNorm.html)
- [3.2.6.4. Arc-Length Control](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/ArcLength.html)

Transient Integrators:

- [3.2.6.5. Central Difference](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/CentralDifference.html)
- [3.2.6.6. Newmark Method](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/Newmark.html)
- [3.2.6.7. Hilber-Hughes-Taylor Method](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/HHT.html)
- [3.2.6.8. Generalized Alpha Method](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/GeneralizedAlpha.html)
- [3.2.6.9. TRBDF2](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/TRBDF2.html)
- [3.2.6.10. Explicit Difference](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/ExplicitDifference.html)

Utility Integrators:

- [3.2.6.11. GimmeMCK Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/gimmeMCK.html)

Code developed by: **fmk**
