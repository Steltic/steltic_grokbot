<!-- chunk_id: elastomericBearingPlasticity_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elastomericBearingPlasticity.html",
 "title": "4.2.6.1. Elastomeric Bearing (Plasticity) Element",
 "category": "element",
 "command": "elastomericBearingPlasticity",
 "doc_section": "src",
 "rel_path": "src/elastomericBearingPlasticity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4042,
 "word_count": 424,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.1. Elastomeric Bearing (Plasticity) Element

This command is used to construct an elastomericBearing element object, which is defined by two nodes. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) plasticity properties for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. By default (sDratio = 0.5) P-Delta moments are equally distributed to the two end-nodes. To avoid the introduction of artificial viscous damping in the isolation system (sometimes referred to as “damping leakage in the isolation system”), the bearing element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

**element(*'elastomericBearingPlasticity'*, *eleTag*, **eleNodes*, *kInit*, *qd*, *alpha1*, *alpha2*, *mu*, *'-P'*, *PMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *x1*, *x2*, *x3*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*)**

For a two-dimensional problem

**element(*'elastomericBearingPlasticity'*, *eleTag*, **eleNodes*, *kInit*, *qd*, *alpha1*, *alpha2*, *mu*, *'-P'*, *PMatTag*, *'-T'*, *TMatTag*, *'-My'*, *MyMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *<x1*, *x2*, *x3>*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*)**

For a three-dimensional problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `kInit` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic stiffness in local shear direction |
| `qd` ([float](https://docs.python.org/3/library/functions.html#float)) | characteristic strength |
| `alpha1` ([float](https://docs.python.org/3/library/functions.html#float)) | post yield stiffness ratio of linear hardening component |
| `alpha2` ([float](https://docs.python.org/3/library/functions.html#float)) | post yield stiffness ratio of non-linear hardening component |
| `mu` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent of non-linear hardening component |
| `PMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in axial direction |
| `TMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in torsional direction |
| `MyMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis |
| `MzMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis (optional) |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local y-axis (optional) |
| `sDratio` ([float](https://docs.python.org/3/library/functions.html#float)) | shear distance from iNode as a fraction of the element length (optional, default = 0.5) |
| `'-doRayleigh'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass (optional, default = 0.0) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Plasticity)_Element)
