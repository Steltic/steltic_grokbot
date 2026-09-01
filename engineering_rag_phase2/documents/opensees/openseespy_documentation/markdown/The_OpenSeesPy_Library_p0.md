<!-- chunk_id: The_OpenSeesPy_Library_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/",
 "title": "The OpenSeesPy Library",
 "category": "general",
 "command": "",
 "doc_section": "en/latest",
 "rel_path": "en/latest/",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3388,
 "word_count": 281,
 "has_code": true,
 "has_table": false
} -->

## The OpenSeesPy Library

Important

Version 3.8.0.0 is released for Linux, Windows, and Mac (ARM64)!

Python 3.12 is required.

OpenSeesPy is on [PyPi (Windows, Linux, Mac)](https://openseespydoc.readthedocs.io/en/latest/src/pypi.html).

OpenSeesPy is free for research, education, and internal use. Commercial redistribution of OpenSeesPy, such as, but not limited to, an application or cloud-based service that uses import openseespy, requires a license similar to that required for commercial redistribution of OpenSees.exe.
Contact [UC Berkeley](https://opensees.github.io/OpenSeesDocumentation/developer/license.html) for commercial licensing details. Contact Dr. Minjie Zhu (zhum@oregonstate.edu) for other questions.

Note

[OpenSees Cloud](https://openseescloud.com) is a SaaS implementation of OpenSees using cloud computing. Analyses run in the cloud on AWS while the front end integrates input, output, documentation, and a model viewer.

[OpenSees Amazon Machine Image](https://aws.amazon.com/marketplace/pp/prodview-pfdzfieycxidk) is a virtual machine that runs OpenSeesPy and OpenSeesMP with no additional compilation or installation required at low cost.

Note

Questions including modeling issues and the use of OpenSeesPy,
please post on [OpenSeesPy Forum](https://opensees.berkeley.edu/community/viewforum.php?f=12).

You are very welcome to contribute to OpenSeesPy with new command
documents and examples
by sending pull requests
through [github pulls](https://github.com/zhuminjie/OpenSeesPyDoc/pulls).

For errors in this document, submit on
[github issues](https://github.com/zhuminjie/OpenSeesPyDoc/issues).

[OpenSeesPy](https://github.com/zhuminjie/OpenSeesPyDoc) is a [Python 3](https://docs.python.org/3/) interpreter of [OpenSees](https://github.com/OpenSees/OpenSees).
A minimum script is shown below:

```
# import OpenSeesPy
import openseespy.opensees as ops

# wipe model
ops.wipe()

# create model
ops.model('basic', '-ndm', 2, '-ndf', 3)

# print model
ops.printModel()
```

### Developer

*Minjie Zhu*

Instructor

Civil and Construction Engineering

Oregon State University

Contents

- [1. Installation](https://openseespydoc.readthedocs.io/en/latest/src/installation.html)
- [2. Compilation](https://openseespydoc.readthedocs.io/en/latest/src/compile.html)
- [3. Change Log](https://openseespydoc.readthedocs.io/en/latest/src/changelog.html)
- [4. Model Commands](https://openseespydoc.readthedocs.io/en/latest/src/modelcmds.html)
- [5. Analysis Commands](https://openseespydoc.readthedocs.io/en/latest/src/analysiscmds.html)
- [6. Output Commands](https://openseespydoc.readthedocs.io/en/latest/src/outputcmds.html)
- [7. Utility Commands](https://openseespydoc.readthedocs.io/en/latest/src/utilitycmds.html)
- [8. FSI Commands](https://openseespydoc.readthedocs.io/en/latest/src/fsicmds.html)
- [9. Sensitivity Commands](https://openseespydoc.readthedocs.io/en/latest/src/senscmds.html)
- [10. Reliability Commands](https://openseespydoc.readthedocs.io/en/latest/src/reliabilitycmds.html)
- [11. Parallel Commands](https://openseespydoc.readthedocs.io/en/latest/src/parallelcmds.html)
- [12. Preprocessing Commands](https://openseespydoc.readthedocs.io/en/latest/src/preprocessing.html)
- [13. Postprocessing Modules](https://openseespydoc.readthedocs.io/en/latest/src/postprocessing.html)
- [14. Examples](https://openseespydoc.readthedocs.io/en/latest/src/examples.html)
