<!-- chunk_id: TRBDF2_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/TRBDF2.html",
 "title": "3.2.6.9. TRBDF2",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "TRBDF2",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/TRBDF2.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 531,
 "word_count": 86,
 "has_code": false,
 "has_table": false
} -->

## 3.2.6.9. TRBDF2

**integrator TRBDF2**

Note

- As opposed to dividing the time-step in 2 as outlined in the papers, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the papers.

This command is used to construct a TRBDF2 integrator object. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something newmark does not always do.
