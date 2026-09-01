<!-- chunk_id: LoadControl_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/LoadControl.html",
 "title": "3.2.6.1. LoadControl Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "LoadControl",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/LoadControl.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2104,
 "word_count": 347,
 "has_code": true,
 "has_table": true
} -->

## 3.2.6.1. LoadControl Command

This command is used to construct a LoadControl integrator object.

**integrator LoadControl $lambda <$numIter $minLambda $maxLambda>**

| Argument | Type | Description |
| --- | --- | --- |
| $lambda | *float* | the load factor increment \(\lambda\) |
| $numIter | *integer* | the number of iterations the user would like to occur in the solution algorithm. Optional: optional default = 1 |
| $minLambda | *float* | the min stepsize the user will allow. optional: defualt \(= \lambda_{min} = \lambda\) |
| $maxLambda | *float* | the max stepsize the user will allow. optional: default \(= \lambda_{max} = \lambda\) |

Note

The change in applied loads that this causes depends on the active load patterns (those load patterns not set constant) and the loads in the load patterns. If the only active loads acting on the domain are in load patterns with a Linear time series with a factor of 1.0, this integrator is the same as the classical load control method.

The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.

#### 3.2.6.1.1. Theory

In Load Control the time in the domain is set to \(t + \lambda_{t+1}\) where,

> \[\lambda_{t+1} = \max \left ( \lambda_{min}, \min \left ( \lambda_{max}, \frac{\text{numIter}}{\text{lastNumIter}} \lambda_{t} \right ) \right )\]

where *lastNumIter* is number of steps required to achieve convergence in the previous step. Changing the step size based on number of iterations in previous step, allows user to reduce the step size when the analysis struggles to converge.

Example

The following example shows how to construct a Load Control Integrator with a step size of **0.1**, which in a static analysis would increment the pseudo time by the **0.1** factor at each analysis step, thus requiring **10** analysis steps if the full load is considered to be applied when the pseudo domain time is **1.0**.

1. **Tcl Code**

```
integrator LoadControl 0.1
```

1. **Python Code**

```
integrator('LoadControl', 0.1)
```

Code Developed by: **fmk**
