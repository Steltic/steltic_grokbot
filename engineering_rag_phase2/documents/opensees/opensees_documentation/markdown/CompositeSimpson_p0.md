<!-- chunk_id: CompositeSimpson_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/CompositeSimpson.html",
 "title": "3.1.9.6. CompositeSimpson",
 "category": "command_manual",
 "manual_group": "model",
 "command": "CompositeSimpson",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/CompositeSimpson.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 681,
 "word_count": 107,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.6. CompositeSimpson

To create a CompositeSimpson beamIntegration object.

**beamIntegration 'CompositeSimpson' tag secTag N**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique object tag |
| $sectTag | *integer* | A previous-defined section |
| $N | *integer* | Number of Integration Points along the elementa |

Example:

The following examples demonstrate the command in Tcl and Python script to add a CompositeSimpson beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
beamIntegration 'CompositeSimpson' 2 1 6
```

1. **Python Code**

```
beamIntegration('CompositeSimpson',2,1,6)
```
