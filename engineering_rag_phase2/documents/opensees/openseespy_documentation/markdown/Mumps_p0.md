<!-- chunk_id: Mumps_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Mumps.html",
 "title": "5.3.9. MUMPS Solver",
 "category": "general",
 "command": "Mumps",
 "doc_section": "src",
 "rel_path": "src/Mumps.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 617,
 "word_count": 100,
 "has_code": false,
 "has_table": true
} -->

## 5.3.9. MUMPS Solver

**system(*'Mumps'*, *'-ICNTL14'*, *icntl14=20.0*, *'-ICNTL7'*, *icntl7=7*)**

Create a system of equations using the Mumps solver

| `icntl14` | controls the percentage increase in the estimated working space (optional) |
| --- | --- |
| `icntl7` | computes a symmetric permutation (ordering) to determine the pivot order to be used for the factorization in case of sequential analysis (optional) 0: AMD 1: set by user 2: AMF 3: SCOTCH 4: PORD 5: Metis 6: AMD with QADM 7: automatic |

Use this command only for parallel model.

Warning

Don’t use this command if model is not parallel, for example,
parametric study.
