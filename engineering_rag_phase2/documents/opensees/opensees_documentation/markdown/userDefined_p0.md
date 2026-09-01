<!-- chunk_id: userDefined_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/beamIntegrations/userDefined.html",
 "title": "3.1.9.7. UserDefined",
 "category": "command_manual",
 "manual_group": "model",
 "command": "userDefined",
 "doc_section": "user/manual/model/beamIntegrations",
 "rel_path": "user/manual/model/beamIntegrations/userDefined.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 748,
 "word_count": 121,
 "has_code": true,
 "has_table": false
} -->

## 3.1.9.7. UserDefined

Create a UserDefined beamIntegration object. This option allows the user to specified locations and weights of the integration points.

**beamIntegration 'UserDefined' tag N secTags locs wts**

Example:

The following examples demonstrate the command in Tcl and Python script to add a Lobatto beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

1. **Tcl Code**

```
locs = [0.1, 0.3, 0.5, 0.7, 0.9]
wts = [0.2, 0.15, 0.3, 0.15, 0.2]
secs = [1, 2, 2, 2, 1]
beamIntegration 'UserDefined' 1 5  secs  locs wtsa
```

1. **Python Code**

```
locs = [0.1, 0.3, 0.5, 0.7, 0.9]
wts = [0.2, 0.15, 0.3, 0.15, 0.2]
secs = [1, 2, 2, 2, 1]
beamIntegration('UserDefined',1,len(secs),*secs,*locs,*wts)
```
