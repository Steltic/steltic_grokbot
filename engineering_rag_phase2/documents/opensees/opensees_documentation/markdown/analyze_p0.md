<!-- chunk_id: analyze_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/analyze.html",
 "title": "3.2.8. analyze Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "analyze",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/analyze.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1854,
 "word_count": 247,
 "has_code": true,
 "has_table": false
} -->

## 3.2.8. analyze Command

This command is used to perform the analysis. It returns a value indicating success or failure of the analysis.

**analyze $numIncr <$dt> <$dtMin $dtMax $Jd>**

> $numIncr, *integer*, number of analysis steps to perform.
> $dt, *float*, time-step increment. Required if transient or variable transient analysis
> $dtMin $dtMax, *float*, minimum and maximum time steps. Required if a variable time step transient analysis was specified.
> $Jd, *integer*, number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge. Required if a variable time step transient analysis was specified.

RETURNS:

0 if successful

<0 if NOT successful

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
set ok [analyze 10]
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
ok = analyse(10)
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
set ok [analyze 2000 0.02]
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
ok = analyze(2000, 0.02)
```

Code Developed by: **fmk**
