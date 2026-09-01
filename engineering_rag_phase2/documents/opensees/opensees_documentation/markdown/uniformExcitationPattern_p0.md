<!-- chunk_id: uniformExcitationPattern_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/uniformExcitationPattern.html",
 "title": "3.1.12.2. Uniform Excitation",
 "category": "command_manual",
 "manual_group": "model",
 "command": "uniformExcitationPattern",
 "doc_section": "user/manual/model/pattern",
 "rel_path": "user/manual/model/pattern/uniformExcitationPattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2069,
 "word_count": 316,
 "has_code": true,
 "has_table": true
} -->

## 3.1.12.2. Uniform Excitation

The UniformExcitation pattern allows the user to apply a uniform excitation to a model acting in a certain direction. The command is as follows:

**pattern UniformExcitation $patternTag $dof -accel $tsTag <-vel0 $vel0> <-fact $cFact>**

| Argument | Type | Description |
| --- | --- | --- |
| $patternTag | *integer* | unique tag among load patterns |
| $dof | *integer* | dof direction the ground motion acts |
| $tsTag | *integer* | tag of the TimeSeries series defining the acceleration history. |
| $vel0 | *float* | the initial velocity (optional: default=0.0) |
| $cFact | *float* | constant factor (optional: default=1.0) |

Warning

The responses obtained from the nodes for this type of excitation are **RELATIVE** values, and not the absolute values obtained from a multiSupportPattern. This is a consequence of the equation of motion being solved:

\[M\ddot{U} + C\dot{U} + K U = P(t)\]

and how the loads are applied with this load pattern.

\[P(t) = -c_{Fact} M l \ddot{u_g}\]

where \(l\)’ is a vector of **1**’s and **0**’s, with a **1** corresponding to all matrix equations in the **$dof** degree-of-freedom direction and **0** for all other degrees-of-freedom. The \(\ddot u_g\) is obtained from the time series.

Example:

The following example shows how to construct a **UniformExcitation** pattern with a tag of **2** acting in the **1** direction. The acceleration for the pattern comes from the [Path TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/pathTimeSeries.html#pathtimeseries) with tag **3** which has been created using the contents of the `elCentro.dat` file, a \(\delta t = 0.02\), and a scale factor given by the variable **g**, which has been set to **386.1**.

1. **Tcl Code**

```
set g 386.1
timeSeries Path 3 -filePath elCentro.dat -dt 0.02 -factor $g
pattern UniformExcitation  2 1 -accel 3
```

1. **Python Code**

```
g = 386.1
timeSeries('Path', 3, '-dt', 0.005, '-filePath', 'A10000.dat', '-factor', g)
pattern('UniformExcitation', 2, 1, '-accel', 3)
```

Code Developed by: **fmk**
