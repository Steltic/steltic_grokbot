<!-- chunk_id: analysis_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/analysis.html",
 "title": "3.2.7. analysis Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "analysis",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/analysis.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2299,
 "word_count": 307,
 "has_code": true,
 "has_table": true
} -->

## 3.2.7. analysis Command

This is the command issued to create an analysis.

**analysis analysisType? <-numSublevels $x -numSubSteps $y>**

| Argument | Type | Description |
| --- | --- | --- |
| $analysisType | *string* | type of analysis object to be constructed. Currently 3 valid options: |
|  |  | **Static** - for static analysis |
|  |  | **Transient** - for transient analysis with constant time step |
|  |  | **VariableTransient** - for transient analysis with variable time step |
| $x | *integer* | number of sublevels transient analysis should try if failure |
| $y | *integer* | number of subdivisions to be tried at each sublevel |

Note

The <-numSublevels $x -numSubSteps $y> only works for the **Transient** type

The components of the analysis, i.e. numberer, constraint handler, system, test, integrator, algorithm, should all be issued BEFORE the analysis object is created.

The **VariableTransient** option is still available. The optional additions for the Transient analysis have been found to provide better options for nonlinear problems with convergence issues.

Warning

When switching from one type of analysis to another, e.g. Static to Transient, it is necessary to issue a [wipeAnalysis Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/wipeAnalysis.html#wipeanalysis).

Static Analysis Example

The following example shows how to construct a Static analysis.

1. **Tcl Code**

```
system SuperLU
constraints Transformation
numberer RCM
test NormDispIncr 1.0e-12  10 3
algorithm Newton
integrator LoadControl 0.1
analysis Static
```

1. **Python Code**

```
system('SuperLU');
constraints('Transformation')
numberer('RCM')
test('NormDispIncr',1.0e-12, 10, 3)
algorithm('Newton')
integrator('LoadControl', 0.1)
analysis Static
```

Transient Analysis Example

The following example shows how to construct a Transient analysis.

1. **Tcl Code**

```
system SuperLU
constraints Transformation
numberer RCM
test NormDispIncr 1.0e-12  10 3
algorithm Newton
integrator Newmark 0.5 0.25
analysis Transient -numSubLevels 3  -numSubSteps 10
```

1. **Python Code**

```
system('SuperLU');
constraints('Transformation')
numberer('RCM')
test('NormDispIncr',1.0e-12, 10, 3)
algorithm('Newton')
integrator('Newmark', 0.5, 0.25)
analysis('Transient')
```

Code Developed by **fmk**
