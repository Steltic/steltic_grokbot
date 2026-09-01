<!-- chunk_id: analysiscmds_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/analysiscmds.html",
 "title": "5. Analysis Commands",
 "category": "analysis",
 "command": "analysiscmds",
 "doc_section": "src",
 "rel_path": "src/analysiscmds.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1929,
 "word_count": 173,
 "has_code": false,
 "has_table": false
} -->

## 5. Analysis Commands

In OpenSees, an analysis is an object which is composed by the aggregation of component objects. It is the component objects which define the type of analysis that is performed on the model. The component classes, as shown in the figure below, consist of the following:

1. ConstraintHandler – determines how the constraint equations are enforced in the analysis – how it handles the boundary conditions/imposed displacements
2. DOF_Numberer – determines the mapping between equation numbers and degrees-of-freedom
3. Integrator – determines the predictive step for time t+dt
4. SolutionAlgorithm – determines the sequence of steps taken to solve the non-linear equation at the current time step
5. SystemOfEqn/Solver – within the solution algorithm, it specifies how to store and solve the system of equations in the analysis
6. Convergence Test – determines when convergence has been achieved.

Analysis commands

1. [constraints commands](https://openseespydoc.readthedocs.io/en/latest/src/constraints.html)
2. [numberer commands](https://openseespydoc.readthedocs.io/en/latest/src/numberer.html)
3. [system commands](https://openseespydoc.readthedocs.io/en/latest/src/system.html)
4. [test commands](https://openseespydoc.readthedocs.io/en/latest/src/test.html)
5. [algorithm commands](https://openseespydoc.readthedocs.io/en/latest/src/algorithm.html)
6. [integrator commands](https://openseespydoc.readthedocs.io/en/latest/src/integrator.html)
7. [analysis command](https://openseespydoc.readthedocs.io/en/latest/src/analysis.html)
8. [eigen command](https://openseespydoc.readthedocs.io/en/latest/src/eigen.html)
9. [analyze command](https://openseespydoc.readthedocs.io/en/latest/src/analyze.html)
10. [modalProperties Command](https://openseespydoc.readthedocs.io/en/latest/src/modalProperties.html)
11. [responseSpectrumAnalysis Command](https://openseespydoc.readthedocs.io/en/latest/src/responseSpectrumAnalysis.html)
