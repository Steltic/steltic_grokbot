<!-- chunk_id: algorithm_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm.html",
 "title": "3.2.5. algorithm Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "algorithm",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/algorithm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1764,
 "word_count": 104,
 "has_code": false,
 "has_table": false
} -->

## 3.2.5. algorithm Command

This command is used to construct a SolutionAlgorithm object, which determines the sequence of steps taken to solve the non-linear equation.

**algorithm algorithmType? arg1? ...**

The type of solution algorithm created and the additional arguments required depends on the algorithmType? provided in the command.

The following contain information about algorithmType? and the args required for each of the available algorithm types:

- [3.2.5.1. Linear Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/LinearAlgorithm.html)
- [3.2.5.2. Newton Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/Newton.html)
- [3.2.5.3. Newton Line Search Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/NewtonLineSearch.html)

  - [3.2.5.3.1. Theory](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/NewtonLineSearch.html#theory)
- [3.2.5.4. Modified Newton Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/ModifiedNewton.html)
- [3.2.5.5. Krylov-Newton Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/KrylovNewton.html)
- [3.2.5.6. Secant Newton  Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/SecantNewton.html)
- [3.2.5.7. BFGS Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/BFGS.html)
- [3.2.5.8. Broyden Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/Broyden.html)
- [3.2.5.9. ExpressNewton Algorithm](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm/ExpressNewton.html)
