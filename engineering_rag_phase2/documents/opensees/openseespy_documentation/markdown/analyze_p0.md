<!-- chunk_id: analyze_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/analyze.html",
 "title": "5.9. analyze command",
 "category": "general",
 "command": "analyze",
 "doc_section": "src",
 "rel_path": "src/analyze.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1159,
 "word_count": 116,
 "has_code": false,
 "has_table": true
} -->

## 5.9. analyze command

**analyze(*numIncr=1*, *dt=0.0*, *dtMin=0.0*, *dtMax=0.0*, *Jd=0*)**

Perform the analysis. Return `0` if successful, `<0` if **NOT** successful

| `numIncr` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of analysis steps to perform. (required except for [PFEM analysis](https://openseespydoc.readthedocs.io/en/latest/src/pfemAnalysis.html#pfem-analysis)) |
| --- | --- |
| `dt` ([float](https://docs.python.org/3/library/functions.html#float)) | Time-step increment. (required for Transient analysis and VariableTransient analysis.`) |
| `dtMin` ([float](https://docs.python.org/3/library/functions.html#float)) | Minimum time steps. (required for VariableTransient analysis) |
| `dtMax` ([float](https://docs.python.org/3/library/functions.html#float)) | Maximum time steps (required for VariableTransient analysis) |
| `Jd` ([float](https://docs.python.org/3/library/functions.html#float)) | Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge (required for VariableTransient analysis) |
