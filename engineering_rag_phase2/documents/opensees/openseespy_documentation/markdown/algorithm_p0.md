<!-- chunk_id: algorithm_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/algorithm.html",
 "title": "5.5. algorithm commands",
 "category": "analysis",
 "command": "algorithm",
 "doc_section": "src",
 "rel_path": "src/algorithm.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1414,
 "word_count": 85,
 "has_code": false,
 "has_table": true
} -->

## 5.5. algorithm commands

**algorithm(*algoType*, **algoArgs*)**

This command is used to construct a SolutionAlgorithm object, which determines the sequence of steps taken to solve the non-linear equation.

| `algoType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | algorithm type |
| --- | --- |
| `algoArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of algorithm arguments |

The following contain information about available `algoType`:

1. [Linear Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/linearAlgo.html)
2. [Newton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/newton.html)
3. [Newton with Line Search](https://openseespydoc.readthedocs.io/en/latest/src/newtonLineSearch.html)
4. [Modified Newton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/modifiedNewton.html)
5. [Krylov-Newton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/krylovNewton.html)
6. [SecantNewton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/secantNewton.html)
7. [RaphsonNewton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/raphsonNewton.html)
8. [PeriodicNewton Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/periodicNewton.html)
9. [BFGS Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/bfgs.html)
10. [Broyden Algorithm](https://openseespydoc.readthedocs.io/en/latest/src/broyden.html)
