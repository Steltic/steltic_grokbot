<!-- chunk_id: Legendre_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/Legendre.html",
 "title": "3.1.9.2. Legendre",
 "category": "command_manual",
 "manual_group": "model",
 "command": "Legendre",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/Legendre.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1169,
 "word_count": 184,
 "has_code": true,
 "has_table": true
} -->

## 3.1.9.2. Legendre

> This command is used to create a Gauss-Legendre beamIntegration object. Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common in force-based elements because there are no integration points at the element ends. The command places `N` Gauss-Legendre integration points along the element. The location and weight of each integration point are tabulated in references on numerical analysis.  The force deformation response at each integration point is defined by the section. The order of accuracy for Gauss-Legendre integration is 2N-1.

**beamIntegration 'Legendre' tag secTag N**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique object tag |
| $sectTag | *integer* | A previous-defined section |
| $N | *integer* | Number of Integration Points along the elementa |

Example:

The following examples demonstrate the command in Tcl and Python script to add a Legendre beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
beamIntegration 'Legendre' 2 1 6
```

1. **Python Code**

```
beamIntegration('Legendre',2,1,6)
```
