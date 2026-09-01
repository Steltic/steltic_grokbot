<!-- chunk_id: test_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/test.html",
 "title": "5.4. test commands",
 "category": "general",
 "command": "test",
 "doc_section": "src",
 "rel_path": "src/test.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1510,
 "word_count": 76,
 "has_code": false,
 "has_table": true
} -->

## 5.4. test commands

**test(*testType*, **testArgs*)**

This command is used to construct the LinearSOE and LinearSolver objects to store and solve the test of equations in the analysis.

| `testType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | test type |
| --- | --- |
| `testArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of test arguments |

The following contain information about available `testType`:

1. [NormUnbalance](https://openseespydoc.readthedocs.io/en/latest/src/normUnbalance.html)
2. [NormDispIncr](https://openseespydoc.readthedocs.io/en/latest/src/normDispIncr.html)
3. [energyIncr](https://openseespydoc.readthedocs.io/en/latest/src/energyIncr.html)
4. [RelativeNormUnbalance](https://openseespydoc.readthedocs.io/en/latest/src/relativeNormUnbalance.html)
5. [RelativeNormDispIncr](https://openseespydoc.readthedocs.io/en/latest/src/relativeNormDispIncr.html)
6. [RelativeTotalNormDispIncr](https://openseespydoc.readthedocs.io/en/latest/src/relativeTotalNormDispIncr.html)
7. [RelativeEnergyIncr](https://openseespydoc.readthedocs.io/en/latest/src/relativeEnergyIncr.html)
8. [FixedNumIter](https://openseespydoc.readthedocs.io/en/latest/src/fixedNumIter.html)
9. [NormDispAndUnbalance](https://openseespydoc.readthedocs.io/en/latest/src/normDispAndUnbalance.html)
10. [NormDispOrUnbalance](https://openseespydoc.readthedocs.io/en/latest/src/normDispOrUnbalance.html)
11. [PFEM test](https://openseespydoc.readthedocs.io/en/latest/src/pfemTest.html#pfem-test)
