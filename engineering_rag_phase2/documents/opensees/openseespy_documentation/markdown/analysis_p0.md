<!-- chunk_id: analysis_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/analysis.html",
 "title": "5.7. analysis command",
 "category": "analysis",
 "command": "analysis",
 "doc_section": "src",
 "rel_path": "src/analysis.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1050,
 "word_count": 140,
 "has_code": false,
 "has_table": true
} -->

## 5.7. analysis command

**analysis(*analysisType*)**

This command is used to construct the Analysis object, which defines what type of analysis is to be performed.

- determine the predictive step for time t+dt
- specify the tangent matrix and residual vector at any iteration
- determine the corrective step based on the displacement increment dU

| analysisType ([str](https://docs.python.org/3/library/stdtypes.html#str)) | char string identifying type of analysis object to be constructed. Currently 3 valid options: `'Static'` - for static analysis `'Transient'` - for transient analysis constant time step `'VariableTransient'` - for transient analysis with variable time step `'PFEM'` - for [PFEM analysis](https://openseespydoc.readthedocs.io/en/latest/src/pfemAnalysis.html#pfem-analysis). |
| --- | --- |

Note

If the component objects are not defined before hand, the command automatically creates default component objects and issues warning messages to this effect. The number of warning messages depends on the number of component objects that are undefined.
