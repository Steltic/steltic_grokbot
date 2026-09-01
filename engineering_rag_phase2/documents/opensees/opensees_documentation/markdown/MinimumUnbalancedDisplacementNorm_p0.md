<!-- chunk_id: MinimumUnbalancedDisplacementNorm_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/MinimumUnbalancedDisplacementNorm.html",
 "title": "3.2.6.3. MinimumUnbalancedDisplacementNorm",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "MinimumUnbalancedDisplacementNorm",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/MinimumUnbalancedDisplacementNorm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 927,
 "word_count": 138,
 "has_code": false,
 "has_table": true
} -->

## 3.2.6.3. MinimumUnbalancedDisplacementNorm

This command is used to construct a StaticIntegrator object of type MinUnbalDispNorm.

**integrator MinUnbalDispNorm $dlambda11 <$Jd $minLambda $maxLambda>**

| Argument | Type | Description |
| --- | --- | --- |
| $dlambda11 | *float* | First load increment (pseudo-time step) at the first iteration in the next invocation of the analysis command. |
| $Jd | *float* | Factor relating first load increment at subsequent time steps. (optional, default: 1.0) |
| $minLambda | *float* | arguments used to bound the load increment (optional, default: $dLambda11) |
| $maxLambda | *float* | arguments used to bound the load increment (optional, default: $dLambda11) |

#### 3.2.6.3.1. Theory

The load increment at iteration i, \(d\lambda_{1,i}\) is related to load increment at i-1, \(d\lambda_{1,i-1}\), and the number of iteration at (i-1), \(J_{i-1}\) by the following:

\(d\lambda_{1,i} = d\lambda_{1,i-1} \frac{J_d}{J_{i-1}}\)
