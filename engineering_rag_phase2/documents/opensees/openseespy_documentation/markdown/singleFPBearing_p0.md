<!-- chunk_id: singleFPBearing_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/singleFPBearing.html",
 "title": "4.2.6.4. Single Friction Pendulum Bearing Element",
 "category": "element",
 "command": "singleFPBearing",
 "doc_section": "src",
 "rel_path": "src/singleFPBearing.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4604,
 "word_count": 507,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.4. Single Friction Pendulum Bearing Element

This command is used to construct a singleFPBearing element object, which is defined by two nodes. The iNode represents the concave sliding surface and the jNode represents the articulated slider. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) friction properties (with post-yield stiffening due to the concave sliding surface) for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. To capture the uplift behavior of the bearing, the user-specified UniaxialMaterial in the axial direction is modified for no-tension behavior. By default (sDratio = 0.0) P-Delta moments are entirely transferred to the concave sliding surface (iNode). It is important to note that rotations of the concave sliding surface (rotations at the iNode) affect the shear behavior of the bearing. To avoid the introduction of artificial viscous damping in the isolation system (sometimes referred to as “damping leakage in the isolation system”), the bearing element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

**element(*'singleFPBearing'*, *eleTag*, **eleNodes*, *frnMdlTag*, *Reff*, *kInit*, *'-P'*, *PMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *x1*, *x2*, *x3*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*, *<'-iter'*, *maxIter*, *tol>*)**

For a two-dimensional problem

**element(*'singleFPBearing'*, *eleTag*, **eleNodes*, *frnMdlTag*, *Reff*, *kInit*, *'-P'*, *PMatTag*, *'-T'*, *TMatTag*, *'-My'*, *MyMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *<x1*, *x2*, *x3>*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*, *<'-iter'*, *maxIter*, *tol>*)**

For a three-dimensional problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `frnMdlTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tag associated with previously-defined FrictionModel |
| `Reff` ([float](https://docs.python.org/3/library/functions.html#float)) | effective radius of concave sliding surface |
| `kInit` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic stiffness in local shear direction |
| `PMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in axial direction |
| `TMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in torsional direction |
| `MyMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local y axis |
| `MzMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis (optional) |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local y-axis (optional) |
| `sDratio` ([float](https://docs.python.org/3/library/functions.html#float)) | shear distance from iNode as a fraction of the element length (optional, default = 0.0) |
| `'-doRayleigh'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass (optional, default = 0.0) |
| `maxIter` ([int](https://docs.python.org/3/library/functions.html#int)) | maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20) |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | convergence tolerance to satisfy element equilibrium (optional, default = 1E-8) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Single_Friction_Pendulum_Bearing_Element)
