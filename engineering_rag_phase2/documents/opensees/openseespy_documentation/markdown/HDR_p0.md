<!-- chunk_id: HDR_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/HDR.html",
 "title": "4.2.6.12. HDR",
 "category": "general",
 "command": "HDR",
 "doc_section": "src",
 "rel_path": "src/HDR.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3352,
 "word_count": 368,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.12. HDR

This command is used to construct an HDR bearing element object in three-dimension. The 3D continuum geometry of an high damping rubber bearing is modeled as a 2-node, 12 DOF discrete element. This is the third element in the series of elements developed for analysis of base-isolated structures under extreme loading (others being ElastomericX and LeadRubberX). The major difference between HDR element with ElastomericX is the hysteresis model in shear. The HDR element uses a model proposed by Grant et al. (2004) to capture the shear behavior of a high damping rubber bearing. The time-dependent values of mechanical properties (e.g., vertical stiffness, buckling load capacity) can also be recorded using the “parameters” recorder.

**element(*'HDR'*, *eleTag*, **eleNodes*, *Gr*, *Kbulk*, *D1*, *D2*, *ts*, *tr*, *n*, *a1*, *a2*, *a3*, *b1*, *b2*, *b3*, *c1*, *c2*, *c3*, *c4*, *<<x1*, *x2*, *x3>*, *y1*, *y2*, *y3>*, *<kc>*, *<PhiM>*, *<ac>*, *<sDratio>*, *<m>*, *<tc>*)**

For 3D problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `Gr` ([float](https://docs.python.org/3/library/functions.html#float)) | shear modulus of elastomeric bearing |
| `Kbulk` ([float](https://docs.python.org/3/library/functions.html#float)) | bulk modulus of rubber |
| `D1` ([float](https://docs.python.org/3/library/functions.html#float)) | internal diameter |
| `D2` ([float](https://docs.python.org/3/library/functions.html#float)) | outer diameter (excluding cover thickness) |
| `ts` ([float](https://docs.python.org/3/library/functions.html#float)) | single steel shim layer thickness |
| `tr` ([float](https://docs.python.org/3/library/functions.html#float)) | single rubber layer thickness |
| `n` ([int](https://docs.python.org/3/library/functions.html#int)) | number of rubber layers |
| `a1` `a2` `a3` `b1` `b2` `b3` `c1` `c2` `c3` `c4` ([float](https://docs.python.org/3/library/functions.html#float)) | parameters of the Grant model |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis (optional) |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local y-axis (optional) |
| `kc` ([float](https://docs.python.org/3/library/functions.html#float)) | cavitation parameter (optional, default = 10.0) |
| `PhiM` ([float](https://docs.python.org/3/library/functions.html#float)) | damage parameter (optional, default = 0.5) |
| `ac` ([float](https://docs.python.org/3/library/functions.html#float)) | strength reduction parameter (optional, default = 1.0) |
| `sDratio` ([float](https://docs.python.org/3/library/functions.html#float)) | shear distance from iNode as a fraction of the element length (optional, default = 0.5) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass (optional, default = 0.0) |
| `tc` ([float](https://docs.python.org/3/library/functions.html#float)) | cover thickness (optional, default = 0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/HDR)
