<!-- chunk_id: FPBearingPTV_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/FPBearingPTV.html",
 "title": "4.2.6.14. FPBearingPTV",
 "category": "general",
 "command": "FPBearingPTV",
 "doc_section": "src",
 "rel_path": "src/FPBearingPTV.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4699,
 "word_count": 511,
 "has_code": false,
 "has_table": true
} -->

## 4.2.6.14. FPBearingPTV

The FPBearingPTV command creates a single Friction Pendulum bearing element, which is capable of accounting for the changes in the coefficient of friction at the sliding surface with instantaneous values of the sliding velocity, axial pressure and temperature at the sliding surface. The constitutive modelling is similar to the existing singleFPBearing element, otherwise. The FPBearingPTV element has been verified and validated in accordance with the ASME guidelines, details of which are presented in Chapter 4 of Kumar et al. (2015a).

**element(*'FPBearingPTV'*, *eleTag*, **eleNodes*, *MuRef*, *IsPressureDependent*, *pRef*, *IsTemperatureDependent*, *Diffusivity*, *Conductivity*, *IsVelocityDependent*, *rateParameter*, *ReffectiveFP*, *Radius_Contact*, *kInitial*, *theMaterialA*, *theMaterialB*, *theMaterialC*, *theMaterialD*, *x1*, *x2*, *x3*, *y1*, *y2*, *y3*, *shearDist*, *doRayleigh*, *mass*, *iter*, *tol*, *unit*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `MuRef` ([float](https://docs.python.org/3/library/functions.html#float)) | Reference coefficient of friction |
| `IsPressureDependent` ([int](https://docs.python.org/3/library/functions.html#int)) | 1 if the coefficient of friction is a function of instantaneous axial pressure |
| `pRef` ([float](https://docs.python.org/3/library/functions.html#float)) | Reference axial pressure (the bearing pressure under static loads) |
| `IsTemperatureDependent` ([int](https://docs.python.org/3/library/functions.html#int)) | 1 if the coefficient of friction is a function of instantaneous temperature at the sliding surface |
| `Diffusivity` ([float](https://docs.python.org/3/library/functions.html#float)) | Thermal diffusivity of steel |
| `Conductivity` ([float](https://docs.python.org/3/library/functions.html#float)) | Thermal conductivity of steel |
| `IsVelocityDependent` ([int](https://docs.python.org/3/library/functions.html#int)) | 1 if the coefficient of friction is a function of instantaneous velocity at the sliding surface |
| `rateParameter` ([float](https://docs.python.org/3/library/functions.html#float)) | The exponent that determines the shape of the coefficient of friction vs. sliding velocity curve |
| `ReffectiveFP` ([float](https://docs.python.org/3/library/functions.html#float)) | Effective radius of curvature of the sliding surface of the FPbearing |
| `Radius_Contact` ([float](https://docs.python.org/3/library/functions.html#float)) | Radius of contact area at the sliding surface |
| `kInitial` ([float](https://docs.python.org/3/library/functions.html#float)) | Lateral stiffness of the sliding bearing before sliding begins |
| `theMaterialA` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag for the uniaxial material in the axial direction |
| `theMaterialB` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag for the uniaxial material in the torsional direction |
| `theMaterialC` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag for the uniaxial material for rocking about local Y axis |
| `theMaterialD` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag for the uniaxial material for rocking about local Z axis |
| `x1` `x2` `x3` ([float](https://docs.python.org/3/library/functions.html#float)) | Vector components to define local X axis |
| `y1` `y2` `y3` ([float](https://docs.python.org/3/library/functions.html#float)) | Vector components to define local Y axis |
| `shearDist` ([float](https://docs.python.org/3/library/functions.html#float)) | Shear distance from iNode as a fraction of the length of the element |
| `doRayleigh` ([int](https://docs.python.org/3/library/functions.html#int)) | To include Rayleigh damping from the bearing |
| `mass` ([float](https://docs.python.org/3/library/functions.html#float)) | Element mass |
| `iter` ([int](https://docs.python.org/3/library/functions.html#int)) | Maximum number of iterations to satisfy the equilibrium of element |
| `tol` ([float](https://docs.python.org/3/library/functions.html#float)) | Convergence tolerance to satisfy the equilibrium of the element |
| `unit` ([int](https://docs.python.org/3/library/functions.html#int)) | Tag to identify the unit from the list below. `1`: N, m, s, C `2`: kN, m, s, C `3`: N, mm, s, C `4`: kN, mm, s, C `5`: lb, in, s, C `6`: kip, in, s, C `7`: lb, ft, s, C `8`: kip, ft, s, C |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/FPBearingPTV)
