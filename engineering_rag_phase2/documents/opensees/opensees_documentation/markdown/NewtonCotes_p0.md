<!-- chunk_id: NewtonCotes_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/NewtonCotes.html",
 "title": "3.1.9.3. NewtonCotes",
 "category": "command_manual",
 "manual_group": "model",
 "command": "NewtonCotes",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/NewtonCotes.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1040,
 "word_count": 164,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.3. NewtonCotes

**This command creates a Newton-Cotes beamIntegration object. Newton-Cotes places integration points uniformly along the element, including a point at each end of the element. The weights for the uniformly spaced integration points are tabulated in references on numerical analysis. The force deformation**

> response at each integration point is defined by the section.
> The order of accuracy for Gauss-Radau integration is N-1.

**beamIntegration 'NewtonCotes' tag secTag N**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique object tag |
| $sectTag | *integer* | A previous-defined section |
| $N | *integer* | Number of Integration Points along the elementa |

Example:

The following examples demonstrate the command in Tcl and Python script to add a NewtonCotes beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
beamIntegration 'NewtonCotes' 2 1 6
```

1. **Python Code**

```
beamIntegration('NewtonCotes',2,1,6)
```
