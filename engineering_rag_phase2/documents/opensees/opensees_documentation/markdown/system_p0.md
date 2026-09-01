<!-- chunk_id: system_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system.html",
 "title": "3.2.3. system Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "system",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/system.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1396,
 "word_count": 94,
 "has_code": false,
 "has_table": false
} -->

## 3.2.3. system Command

This command is used to construct the `LinearSOE` and `LinearSolver` objects to store and solve the system of equations, \(Ax=b\) during each step.

**system systemType? arg1? ...**

The type of `LinearSOE` created and the additional arguments required depends on the `systemType`? provided in the command.

The following contain information about systemType? and the args required for each of the available system types:

- [3.2.3.1. BandGeneral System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/BandGeneral.html)
- [3.2.3.2. BandSPD System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/BandSPD.html)
- [3.2.3.3. ProfileSPD System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/ProfileSPD.html)
- [3.2.3.4. SuperLU System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/SuperLU.html)
- [3.2.3.5. Umfpack System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/Umfpack.html)
- [3.2.3.6. FullGeneral System](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/FullGeneral.html)
- [3.2.3.7. SparseSYM Solver](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/SparseSYM.html)
- [3.2.3.8. Mumps Solver](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/Mumps.html)
