<!-- chunk_id: basicExamples_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/examples/basicExamples.html",
 "title": "4.1. Basic Examples",
 "category": "examples",
 "manual_group": "",
 "command": "basicExamples",
 "doc_section": "user/examples",
 "rel_path": "user/examples/basicExamples.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1116,
 "word_count": 166,
 "has_code": false,
 "has_table": false
} -->

## 4.1. Basic Examples

In OpenSees, an analysis is an object which is composed by the aggregation of component objects. It is the component objects which define the type of analysis that is performed on the model. The component classes, as shown in the figure below, consist of the following:

1. Constraint Handler – determines how the constraint equations are enforced in the analysis – how it handles the boundary conditions/imposed displacements
2. DOF Numberer – determines the mapping between equation numbers in the system of equation and the degrees-of-freedom at the nodes
3. SystemOfEqn & Solver – it specifies how to store and solve the system of equations \(Ax=b\)
4. Convergence Test – determines when convergence has been achieved.
5. Solution Algorithm – determines the sequence of steps taken to solve the non-linear equation at the current time step
6. Integrator – determines the equations to solve, the predictive step, and how to update the reponses at the nodes given the solution to \(Ax=b\)

- [4.1.1. Basic Truss Example](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/basicExamples/basicTruss.html)
