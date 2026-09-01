<!-- chunk_id: PenaltyMethod_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PenaltyMethod.html",
 "title": "5.1.3. Penalty Method",
 "category": "general",
 "command": "PenaltyMethod",
 "doc_section": "src",
 "rel_path": "src/PenaltyMethod.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 773,
 "word_count": 98,
 "has_code": false,
 "has_table": true
} -->

## 5.1.3. Penalty Method

**constraints(*'Penalty'*, *alphaS=1.0*, *alphaM=1.0*)**

This command is used to construct a Penalty constraint handler, which enforces the constraints using the penalty method. The following is the command to construct a penalty constraint handler:

| `alphaS` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_S\) factor on single points. |
| --- | --- |
| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_M\) factor on multi-points. |

Note

The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).
