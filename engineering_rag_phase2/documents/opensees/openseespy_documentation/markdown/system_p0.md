<!-- chunk_id: system_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/system.html",
 "title": "5.3. system commands",
 "category": "analysis",
 "command": "system",
 "doc_section": "src",
 "rel_path": "src/system.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1410,
 "word_count": 86,
 "has_code": false,
 "has_table": true
} -->

## 5.3. system commands

**system(*systemType*, **systemArgs*)**

This command is used to construct the LinearSOE and LinearSolver objects to store and solve the system of equations in the analysis.

| `systemType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | system type |
| --- | --- |
| `systemArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of system arguments |

The following contain information about available `systemType`:

1. [BandGeneral SOE](https://openseespydoc.readthedocs.io/en/latest/src/BandGen.html)
2. [BandSPD SOE](https://openseespydoc.readthedocs.io/en/latest/src/BandSPD.html)
3. [ProfileSPD SOE](https://openseespydoc.readthedocs.io/en/latest/src/ProfileSPD.html)
4. [SuperLU SOE](https://openseespydoc.readthedocs.io/en/latest/src/SuperLU.html)
5. [UmfPack SOE](https://openseespydoc.readthedocs.io/en/latest/src/UmfPack.html)
6. [FullGeneral SOE](https://openseespydoc.readthedocs.io/en/latest/src/FullGeneral.html)
7. [SparseSYM SOE](https://openseespydoc.readthedocs.io/en/latest/src/SparseSYM.html)
8. [Diagonal System](https://openseespydoc.readthedocs.io/en/latest/src/Diagonal.html)
9. [PFEM SOE](https://openseespydoc.readthedocs.io/en/latest/src/pfemSystem.html#pfem-system)
10. [MUMPS Solver](https://openseespydoc.readthedocs.io/en/latest/src/Mumps.html)
11. [PythonSparse system](https://openseespydoc.readthedocs.io/en/latest/src/PythonSparse.html)
