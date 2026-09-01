<!-- chunk_id: interpreters_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/interpreters.html",
 "title": "1. OpenSees Interpreters",
 "category": "user_guide",
 "manual_group": "",
 "command": "interpreters",
 "doc_section": "user",
 "rel_path": "user/interpreters.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1839,
 "word_count": 285,
 "has_code": true,
 "has_table": false
} -->

## 1. OpenSees Interpreters

In computer science, an interpreter is a computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program. Matlab is a great example of an interpreter. The scripts that the user provides, e.g. a .m file if the user is using Matlab, contains a sequence of instructions written in some high level scripting language. For performing finite element analysis using OpenSees two popular scripting languages, **Tcl** and **Python** have been extended, by extended we mean additional commands have been added to the languages.

The extensions introduce **IDENTICAL** new commands with the same arguments into the interpreter languages read by the interpreters. How the command is expressed in the language is the only difference. The languages to add a node number 3 at location (168.0, 0.0):

1. Tcl

```
node 3 168.0 0.0
```

1. Python

```
node(3, 168.0,  0.0)
```

In order to perform finite element analysis using either **Tcl** or **Python**, the user must understand the existing commands available in the scripting languages (and here the **Tcl** and **Python** languages will differ) and the new commands.

Warning

To **know and use** the commands in a programming language in order to develop an application (**coding**) is one thing. To **program** in a language is something different. **Programming** involves creativity and thinking at a higher level, thinking in terms of problem solving, what are the abstractions and algorithms that can be employed to solve the problem. Programmers finally use code to express their thoughts of how to solve the problem. All programmers are coders. Most coders are **NOT** programmers. To utilize the OpenSees interpreters effectively **YOU WANT TO BECOME A PROGRAMMER**.
