<!-- chunk_id: test_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test.html",
 "title": "3.2.4. test Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "test",
 "doc_section": "user/manual/analysis",
 "rel_path": "user/manual/analysis/test.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1752,
 "word_count": 123,
 "has_code": false,
 "has_table": false
} -->

## 3.2.4. test Command

This command is used to construct the **Convergence Test**. The convergence test is that object the [algorithm Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/algorithm.html#algorithm) uses to detect if convergence has been achieved. The convergence test is applied to the matrix equation, \(Ax=b\) stored in the [system Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system.html#system). In the finite element setting and under normal integration schemes and algorithms, the \(x\) corresponds to the displacement increment and \(b\) the unbalanced forces.

**test testType? arg1? ...**

The following contain information about testType? and the args required for each of the available system types:

- [3.2.4.1. Norm Unbalance](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/NormUnbalance.html)
- [3.2.4.2. Norm Displacement Increment](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/NormDispIncr.html)
- [3.2.4.3. Energy Increment](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/NormEnergyIncr.html)
- [3.2.4.4. Relative Norm Unbalance](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/RelativeNormUnbalance.html)
- [3.2.4.5. Relative Energy Increment Test](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/RelativeEnergyIncr.html)
- [3.2.4.6. Total Relative Norm Displacement Increment](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/TotalRelativeNormDisplacementIncrement.html)
- [3.2.4.7. Fixed Number Iterations Test](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/test/FixedNumberIterations.html)
