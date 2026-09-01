<!-- chunk_id: PressureIndependMultiYield_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PressureIndependMultiYield.html",
 "title": "4.15.6.1. PressureIndependMultiYield",
 "category": "general",
 "command": "PressureIndependMultiYield",
 "doc_section": "src",
 "rel_path": "src/PressureIndependMultiYield.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3483,
 "word_count": 377,
 "has_code": false,
 "has_table": true
} -->

## 4.15.6.1. PressureIndependMultiYield

**nDMaterial(*'PressureIndependMultiYield'*, *matTag*, *nd*, *rho*, *refShearModul*, *refBulkModul*, *cohesi*, *peakShearStra*, *frictionAng*, *refPress*, *pressDependCoe*, *noYieldSurf=20*, **yieldSurf*)**

PressureIndependMultiYield material is an elastic-plastic material in which plasticity exhibits only in the deviatoric stress-strain response. The volumetric stress-strain response is linear-elastic and is independent of the deviatoric response. This material is implemented to simulate monotonic or cyclic response of materials whose shear behavior is insensitive to the confinement change. Such materials include, for example, organic soils or clay under fast (undrained) loading conditions.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | Number of dimensions, 2 for plane-strain, and 3 for 3D analysis. |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | Saturated soil mass density. |
| `refShearModul` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(G_r\)) Reference low-strain shear modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `refBulkModul` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(B_r\)) Reference bulk modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `cohesi` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(c\)) Apparent cohesion at zero effective confinement. |
| `peakShearStra` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(\gamma_{max}\)) An octahedral shear strain at which the maximum shear strength is reached, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `frictionAng` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(phi\)) Friction angle at peak shear strength in degrees (recommendation is 0.0). |
| `refPress` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(p'_r\)) Reference mean effective confining pressure at which \(G_r\), \(B_r\), and \(\gamma_{max}\) are defined (recommendation is 100. kPa). |
| `pressDependCoe` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(d\)) A positive constant defining variations of \(G\) and \(B\) as a function of instantaneous effective confinement \(p'\) (recommendation is 0.0) \(G=G_r(\frac{p'}{p'_r})^d\) \(B=B_r(\frac{p'}{p'_r})^d\) If \(\phi=0\), \(d\) is reset to 0.0. |
| `noYieldSurf` ([float](https://docs.python.org/3/library/functions.html#float)) | Number of yield surfaces, optional (must be less than 40, default is 20). The surfaces are generated based on the hyperbolic relation defined in Note 2 below. |
| `yieldSurf` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | Instead of automatic surfaces generation (Note 2), you can define yield surfaces directly based on desired shear modulus reduction curve. To do so, add a minus sign in front of noYieldSurf, then provide noYieldSurf pairs of shear strain (r) and modulus ratio (Gs) values. For example, to define 10 surfaces: yieldSurf = [r1, Gs1, …, r10, Gs10] |

See also [notes](http://opensees.berkeley.edu/wiki/index.php/PressureIndependMultiYield_Material)
