<!-- chunk_id: numberer_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/numberer.html",
 "title": "5.2. numberer commands",
 "category": "analysis",
 "command": "numberer",
 "doc_section": "src",
 "rel_path": "src/numberer.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 992,
 "word_count": 73,
 "has_code": false,
 "has_table": true
} -->

## 5.2. numberer commands

**numberer(*numbererType*, **numbererArgs*)**

This command is used to construct the DOF_Numberer object. The DOF_Numberer object determines the mapping between equation numbers and degrees-of-freedom – how degrees-of-freedom are numbered.

| `numbererType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | numberer type |
| --- | --- |
| `numbererArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of numberer arguments |

The following contain information about available `numbererType`:

1. [Plain Numberer](https://openseespydoc.readthedocs.io/en/latest/src/PlainNumberer.html)
2. [RCM Numberer](https://openseespydoc.readthedocs.io/en/latest/src/RCM.html)
3. [AMD Numberer](https://openseespydoc.readthedocs.io/en/latest/src/AMD.html)
4. [Parallel Plain Numberer](https://openseespydoc.readthedocs.io/en/latest/src/ParallelPlainNumberer.html)
5. [Parallel RCM Numberer](https://openseespydoc.readthedocs.io/en/latest/src/ParallelRCMNumberer.html)
