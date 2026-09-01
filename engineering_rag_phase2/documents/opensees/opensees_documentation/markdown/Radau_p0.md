<!-- chunk_id: Radau_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Radau.html",
 "title": "3.1.9.4. Radau",
 "category": "command_manual",
 "manual_group": "model",
 "command": "Radau",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/Radau.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1198,
 "word_count": 196,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.4. Radau

**To create a Gauss-Radau beamIntegration object. Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic**

> hinge integration methods.
>
> Places `N` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on
> numerical analysis. The force-deformation response at each integration point is defined
> by the section. The order of accuracy for Gauss-Radau integration is 2N-2.

**beamIntegration 'Radau' tag secTag N**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique object tag |
| $sectTag | *integer* | A previous-defined section |
| $N | *integer* | Number of Integration Points along the elementa |

Example:

The following examples demonstrate the command in Tcl and Python script to add a Radau beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
beamIntegration 'Radau' 2 1 6
```

1. **Python Code**

```
beamIntegration('Radau',2,1,6)
```
