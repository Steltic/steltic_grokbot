<!-- chunk_id: node_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/node.html",
 "title": "3.1.2. node Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "node",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/node.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1018,
 "word_count": 181,
 "has_code": true,
 "has_table": true
} -->

## 3.1.2. node Command

This command is used to construct a Node object. It assigns coordinates and masses to the Node object. The assignment of mass is optional.

**node $nodeTag [ndm $coords] <-mass [ndf $massValues]>**

| Argument | Type | Description |
| --- | --- | --- |
| $nodeTag | *integer* | unique tag identifying node |
| $coords | *list float* | **ndm** nodal coordinates |
| $massValues | *list float* | optional **ndf** nodal mass values |

Example:

The following examples demonstrate the commands in a script to add two nodes to domain in which the last model command specified an **ndm** of **2** and a **ndf** of 3. The two nodes to be added have node tags **3** and **4**. Node **3** is located at coordinates (168.0, 144.0) and node **4** at location (168.0,144.0). Node **4** is assigned a mass of (10.0, 10.0, 0.).

1. **Tcl Code**

```
node 3 168.0 0.0
node 4 168.0 144.0 -mass 10.0 10.0 0.0
```

1. **Python Code**

```
node(3, 168.0,  0.0)
node(4, 168.0,  0.0, '-mass', 10.0 10.0 0.0)
```

Code Developed by: **fmk**
