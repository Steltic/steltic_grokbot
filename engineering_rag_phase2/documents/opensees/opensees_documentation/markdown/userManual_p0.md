<!-- chunk_id: userManual_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/userManual.html",
 "title": "3. Command Manual",
 "category": "user_guide",
 "manual_group": "",
 "command": "userManual",
 "doc_section": "user",
 "rel_path": "user/userManual.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1868,
 "word_count": 245,
 "has_code": false,
 "has_table": false
} -->

## 3. Command Manual

To understand how to run a finite element simulation using OpenSees, it is helpful to have a small understanding of the following abstractions. In OpenSees there exists:

1. The **Model Generator**, code that allows the user to build a finite element model.
2. The **Domain**, code that holds the current state and the last committed state of the finite element model.
3. The **Analysis**, code that moves the state of the model from one converged state to another via a number of trial steps.
4. The **Recorders**, code that allows the user to obtain output from a finite element analysis, e.g. to record the node displacement history.

Fig. 3.1 OpenSees Abstractions

The OpenSees interpreters add [commands](http://en.wikipedia.org/wiki/Command_(computing)) to interpreters, e.g. Python and Tcl, to allow the user to specify the model builder, the domain, the analysis and the output. Each of these added commands is associated (bound) with a C++ procedure that is provided in the OpenSees Framework. It is this procedure that is called upon by the interpreter to parse the command when it is encountered. In this document we focus primarily on those commands which have been added to these languages. All existing commands that exist in the Tcl and Python languages are available to these interpreters. We provide a brief [[Introduction To Tcl]], more detailed documentation on these existing commands can be found in books and on-line.

- [3.1. Model Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/modelCommands.html)
- [3.2. Analysis Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysisCommands.html)
- [3.3. Output Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/outputCommands.html)
- [3.4. Misc. Commands](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/miscCommands.html)
