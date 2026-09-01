<!-- chunk_id: analysisCommands_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysisCommands.html",
 "title": "3.2. Analysis Commands",
 "category": "command_manual",
 "manual_group": "",
 "command": "analysisCommands",
 "doc_section": "user/manual",
 "rel_path": "user/manual/analysisCommands.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2304,
 "word_count": 209,
 "has_code": false,
 "has_table": false
} -->

## 3.2. Analysis Commands

In OpenSees, an analysis is an object which is composed by the aggregation of component objects. It is the component objects which define the type of analysis that is performed on the model. The component classes, as shown in the figure below, consist of the following:

1. Constraint Handler – determines how the constraint equations are enforced in the analysis – how it handles the boundary conditions/imposed displacements
2. DOF Numberer – determines the mapping between equation numbers in the system of equation and the degrees-of-freedom at the nodes
3. SystemOfEqn & Solver – it specifies how to store and solve the system of equations \(Ax=b\)
4. Convergence Test – determines when convergence has been achieved.
5. Solution Algorithm – determines the sequence of steps taken to solve the non-linear equation at the current time step
6. Integrator – determines the equations to solve, the predictive step, and how to update the response at the nodes given the solution to \(Ax=b\)

Fig. 3.2.1 OpenSees Analysis

- [3.2.1. constraints Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/constraints.html)
- [3.2.2. numberer Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/numberer.html)
- [3.2.3. system Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system.html)
- [3.2.4. test Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test.html)
- [3.2.5. algorithm Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm.html)
- [3.2.6. integrator Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator.html)
- [3.2.7. analysis Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/analysis.html)
- [3.2.8. analyze Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/analyze.html)
- [3.2.9. eigen Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/eigen.html)
- [3.2.10. modalProperties Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/modalProperties.html)
- [3.2.11. responseSpectrumAnalysis Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/responseSpectrumAnalysis.html)
