<!-- chunk_id: exit_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/misc/exit.html",
 "title": "3.4.11. exit Command",
 "category": "command_manual",
 "manual_group": "misc",
 "command": "exit",
 "doc_section": "user/manual/misc",
 "rel_path": "user/manual/misc/exit.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 451,
 "word_count": 72,
 "has_code": true,
 "has_table": false
} -->

## 3.4.11. exit Command

This command is used to exit the program in a controlled way.

**exit()**

This command is used to terminate the application, invoking the necessary destructors on all the objects. This is needed for example to ensure files get closed and that the parallel interpreters shutdown correctly.

Example:

The following demonstrates the use of the exit command!

1. **Tcl Code**

```
exit
```

1. **Python Code**

```
exit()
```

Code Developed by: **fmk**
