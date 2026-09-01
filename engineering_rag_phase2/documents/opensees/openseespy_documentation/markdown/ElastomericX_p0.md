<!-- chunk_id: ElastomericX_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ElastomericX.html",
 "title": "4.2.6.10. ElastomericX",
 "category": "general",
 "command": "ElastomericX",
 "doc_section": "src",
 "rel_path": "src/ElastomericX.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4386,
 "word_count": 454,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.10. ElastomericX

This command is used to construct an ElastomericX bearing element object in three-dimension. The 3D continuum geometry of an elastomeric bearing is modeled as a 2-node, 12 DOF discrete element. This elements extends the formulation of Elastomeric_Bearing_(Bouc-Wen)_Element element. However, instead of the user providing material models as input arguments, it only requires geometric and material properties of an elastomeric bearing as arguments. The material models in six direction are formulated within the element from input arguments. The time-dependent values of mechanical properties (e.g., shear stiffness, buckling load capacity) can also be recorded using the “parameters” recorder.

**element(*'ElastomericX'*, *eleTag*, **eleNodes*, *Fy*, *alpha*, *Gr*, *Kbulk*, *D1*, *D2*, *ts*, *tr*, *n*, *<<x1*, *x2*, *x3>*, *y1*, *y2*, *y3>*, *<kc>*, *<PhiM>*, *<ac>*, *<sDratio>*, *<m>*, *<cd>*, *<tc>*, *<tag1>*, *<tag2>*, *<tag3>*, *<tag4>*)**

For 3D problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield strength |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | post-yield stiffness ratio |
| `Gr` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus of elastomeric bearing |
| `Kbulk` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus of rubber |
| `D1` ([float](https://docs.python.org/3/library/functions.html#float)) | internal diameter |
| `D2` ([float](https://docs.python.org/3/library/functions.html#float)) | outer diameter (excluding cover thickness) |
| `ts` ([float](https://docs.python.org/3/library/functions.html#float)) | single steel shim layer thickness |
| `tr` ([float](https://docs.python.org/3/library/functions.html#float)) | single rubber layer thickness |
| `n` ([int](https://docs.python.org/3/library/functions.html#int)) | number of rubber layers |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis (optional) |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local y-axis (optional) |
| `kc` ([float](https://docs.python.org/3/library/functions.html#float)) | cavitation parameter (optional, default = 10.0) |
| `PhiM` ([float](https://docs.python.org/3/library/functions.html#float)) | damage parameter (optional, default = 0.5) |
| `ac` ([float](https://docs.python.org/3/library/functions.html#float)) | strength reduction parameter (optional, default = 1.0) |
| `sDratio` ([float](https://docs.python.org/3/library/functions.html#float)) | shear distance from iNode as a fraction of the element length (optional, default = 0.5) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass (optional, default = 0.0) |
| `cd` ([float](https://docs.python.org/3/library/functions.html#float)) | viscous damping parameter (optional, default = 0.0) |
| `tc` ([float](https://docs.python.org/3/library/functions.html#float)) | cover thickness (optional, default = 0.0) |
| `tag1` ([float](https://docs.python.org/3/library/functions.html#float)) | Tag to include cavitation and post-cavitation (optional, default = 0) |
| `tag2` ([float](https://docs.python.org/3/library/functions.html#float)) | Tag to include buckling load variation (optional, default = 0) |
| `tag3` ([float](https://docs.python.org/3/library/functions.html#float)) | Tag to include horizontal stiffness variation (optional, default = 0) |
| `tag4` ([float](https://docs.python.org/3/library/functions.html#float)) | Tag to include vertical stiffness variation (optional, default = 0) |

Note

Because default values of heating parameters are in SI units, user must override the default heating parameters values if using Imperial units

User should distinguish between yield strength of elastomeric bearing (\(F_y\)) and characteristic strength (\(Q_d\)): \(Q_d=F_y*(1-alpha)\)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ElastomericX)
