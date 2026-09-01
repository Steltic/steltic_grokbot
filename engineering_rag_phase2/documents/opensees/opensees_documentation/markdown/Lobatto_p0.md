<!-- chunk_id: Lobatto_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Lobatto.html",
 "title": "3.1.9.1. Lobatto",
 "category": "command_manual",
 "manual_group": "model",
 "command": "Lobatto",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/Lobatto.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 941,
 "word_count": 152,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.1. Lobatto

This command is used to create a Gauss-Lobatto beamIntegration object. Gauss-Lobatto integration is the most common approach for evaluating the response of ForceBeamColumn (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

**beamIntegration 'Lobatto' tag secTag N**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique object tag |
| $sectTag | *integer* | A previous-defined section |
| $N | *integer* | Number of Integration Points along the elementa |

Example:

The following examples demonstrate the command in Tcl and Python script to add a Lobatto beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
beamIntegration 'Lobatto' 2 1 6
```

1. **Python Code**

```
beamIntegration('Lobatto',2,1,6)
```
