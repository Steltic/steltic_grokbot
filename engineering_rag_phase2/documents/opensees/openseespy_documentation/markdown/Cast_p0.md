<!-- chunk_id: Cast_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Cast.html",
 "title": "4.14.5.2. CastFuse Material",
 "category": "material",
 "command": "Cast",
 "doc_section": "src",
 "rel_path": "src/Cast.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3103,
 "word_count": 351,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.2. CastFuse Material

**uniaxialMaterial(*'Cast'*, *matTag*, *n*, *bo*, *h*, *fy*, *E*, *L*, *b*, *Ro*, *cR1*, *cR2*, *a1=s2*Pp/Kp*, *a2=1.0*, *a3=a4*Pp/Kp*, *a4=1.0*)**

This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `n` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of yield fingers of the CSF-brace |
| `bo` ([float](https://docs.python.org/3/library/functions.html#float)) | Width of an individual yielding finger at its base of the CSF-brace |
| `h` ([float](https://docs.python.org/3/library/functions.html#float)) | Thickness of an individual yielding finger |
| `fy` ([float](https://docs.python.org/3/library/functions.html#float)) | Yield strength of the steel material of the yielding finger |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | Modulus of elasticity of the steel material of the yielding finger |
| `L` ([float](https://docs.python.org/3/library/functions.html#float)) | Height of an individual yielding finger |
| `b` ([float](https://docs.python.org/3/library/functions.html#float)) | Strain hardening ratio |
| `Ro` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter that controls the Bauschinger effect. Recommended Values for $Ro=between 10 to 30 |
| `cR1` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter that controls the Bauschinger effect. Recommended Value cR1=0.925 |
| `cR2` ([float](https://docs.python.org/3/library/functions.html#float)) | Parameter that controls the Bauschinger effect. Recommended Value cR2=0.150 |
| `a1` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic deformation of a2*(Pp/Kp) |
| `a2` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under a1). (optional default = 1.0) |
| `a3` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic deformation of a4*(Pp/Kp) |
| `a4` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening parameter (see explanation under a3). (optional default = 1.0) |

Gray et al. [1] showed that the monotonic backbone curve of a CSF-brace with known properties (`n`, `bo`, `h`, `L`, `fy`, `E`) after yielding can be expressed as a close-form solution that is given by,
\(P = P_p/\cos(2d/L)\), in which \(d\) is the axial deformation of the brace at increment \(i\) and \(P_p\) is the yield strength of the CSF-brace and is given by the following expression

\(P_p = nb_oh^2f_y/4L\)

The elastic stiffness of the CSF-brace is given by,

\(K_p = nb_oEh^3f_y/6L^3\)

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/CastFuse_Material)
