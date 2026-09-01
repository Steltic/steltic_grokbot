<!-- chunk_id: pfemAnalysis_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pfemAnalysis.html",
 "title": "8.6. PFEM analysis",
 "category": "analysis",
 "command": "pfemAnalysis",
 "doc_section": "src",
 "rel_path": "src/pfemAnalysis.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 602,
 "word_count": 60,
 "has_code": false,
 "has_table": true
} -->

## 8.6. PFEM analysis

**analysis(*'PFEM'*, *dtmax*, *dtmin*, *gravity*, *ratio=0.5*)**

Create a OpenSees PFEMAnalysis object.

| `dtmax` ([float](https://docs.python.org/3/library/functions.html#float)) | Maximum time steps. |
| --- | --- |
| `dtmin` ([float](https://docs.python.org/3/library/functions.html#float)) | Mimimum time steps. |
| `gravity` ([float](https://docs.python.org/3/library/functions.html#float)) | Gravity acceleration used to move isolated particles. |
| `ratio` ([float](https://docs.python.org/3/library/functions.html#float)) | The ratio to reduce time steps if it was not converged. (optional) |
