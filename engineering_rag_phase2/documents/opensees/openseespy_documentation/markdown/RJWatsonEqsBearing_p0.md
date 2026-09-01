<!-- chunk_id: RJWatsonEqsBearing_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/RJWatsonEqsBearing.html",
 "title": "4.2.6.13. RJ-Watson EQS Bearing Element",
 "category": "element",
 "command": "RJWatsonEqsBearing",
 "doc_section": "src",
 "rel_path": "src/RJWatsonEqsBearing.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5019,
 "word_count": 550,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.13. RJ-Watson EQS Bearing Element

This command is used to construct a RJWatsonEqsBearing element object, which is defined by two nodes. The iNode represents the masonry plate and the jNode represents the sliding surface plate. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) friction properties (with post-yield stiffening due to the mass-energy-regulator (MER) springs) for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. To capture the uplift behavior of the bearing, the user-specified UniaxialMaterial in the axial direction is modified for no-tension behavior. By default (sDratio = 1.0) P-Delta moments are entirely transferred to the sliding surface (jNode). It is important to note that rotations of the sliding surface (rotations at the jNode) affect the shear behavior of the bearing. To avoid the introduction of artificial viscous damping in the isolation system (sometimes referred to as “damping leakage in the isolation system”), the bearing element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

**element(*'RJWatsonEqsBearing'*, *eleTag*, **eleNodes*, *frnMdlTag*, *kInit*, *'-P'*, *PMatTag*, *'-Vy'*, *VyMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *x1*, *x2*, *x3*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*, *<'-iter'*, *maxIter*, *tol>*)**

For a two-dimensional problem

**element(*'RJWatsonEqsBearing'*, *eleTag*, **eleNodes*, *frnMdlTag*, *kInit*, *'-P'*, *PMatTag*, *'-Vy'*, *VyMatTag*, *'-Vz'*, *VzMatTag*, *'-T'*, *TMatTag*, *'-My'*, *MyMatTag*, *'-Mz'*, *MzMatTag*, *<'-orient'*, *<x1*, *x2*, *x3>*, *y1*, *y2*, *y3>*, *<'-shearDist'*, *sDratio>*, *<'-doRayleigh'>*, *<'-mass'*, *m>*, *<'-iter'*, *maxIter*, *tol>*)**

For a three-dimensional problem

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `frnMdlTag` ([float](https://docs.python.org/3/library/functions.html#float)) | tag associated with previously-defined FrictionModel |
| `kInit` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stiffness of sliding friction component in local shear direction |
| `'-P'` `PMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in axial direction |
| `'-Vy'` `VyMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in shear direction along local y-axis (MER spring behavior not including friction) |
| `'-Vz'` `VzMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in shear direction along local z-axis (MER spring behavior not including friction) |
| `'-T'` `TMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in torsional direction |
| `'-My'` `MyMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local y-axis |
| `'-Mz'` `MzMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial in moment direction around local z-axis |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local x-axis (optional) |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | vector components in global coordinates defining local y-axis (optional) |
| `sDratio` ([float](https://docs.python.org/3/library/functions.html#float)) | shear distance from iNode as a fraction of the element length (optional, default = 0.0) |
| `'-doRayleigh'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | to include Rayleigh damping from the bearing (optional, default = no Rayleigh damping contribution) |
| `m` ([float](https://docs.python.org/3/library/functions.html#float)) | element mass (optional, default = 0.0) |
| `maxIter` ([int](https://docs.python.org/3/library/functions.html#int)) | maximum number of iterations to undertake to satisfy element equilibrium (optional, default = 20) |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | convergence tolerance to satisfy element equilibrium (optional, default = 1E-8) |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/RJ-Watson_EQS_Bearing_Element)
