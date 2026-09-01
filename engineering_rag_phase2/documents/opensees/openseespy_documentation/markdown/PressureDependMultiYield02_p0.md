<!-- chunk_id: PressureDependMultiYield02_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PressureDependMultiYield02.html",
 "title": "4.15.6.3. PressureDependMultiYield02",
 "category": "general",
 "command": "PressureDependMultiYield02",
 "doc_section": "src",
 "rel_path": "src/PressureDependMultiYield02.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3861,
 "word_count": 381,
 "has_code": false,
 "has_table": true
} -->

## 4.15.6.3. PressureDependMultiYield02

**nDMaterial(*'PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf=20.0, *yieldSurf=[], contrac[1]=5.0, dilat[1]=3.0, *liquefac=[1.0,0.0],e=0.6, *params=[0.9, 0.02, 0.7, 101.0], c=0.1*)**

PressureDependMultiYield02 material is modified from PressureDependMultiYield material, with:

1. additional parameters (`contrac[2]` and `dilat[2]`) to account for \(K_{\sigma}\) effect,
2. a parameter to account for the influence of previous dilation history on subsequent contraction phase (`contrac[1]`), and
3. modified logic related to permanent shear strain accumulation (`liquefac[0]` and `liquefac[1]`).

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `nd` ([float](https://docs.python.org/3/library/functions.html#float)) | Number of dimensions, 2 for plane-strain, and 3 for 3D analysis. |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | Saturated soil mass density. |
| `refShearModul` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(G_r\)) Reference low-strain shear modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `refBulkModul` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(B_r\)) Reference bulk modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `frictionAng` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(phi\)) Friction angle at peak shear strength in degrees, optional (default is 0.0). |
| `peakShearStra` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(\gamma_{max}\)) An octahedral shear strain at which the maximum shear strength is reached, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| `refPress` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(p'_r\)) Reference mean effective confining pressure at which \(G_r\), \(B_r\), and \(\gamma_{max}\) are defined, optional (default is 100. kPa). |
| `pressDependCoe` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(d\)) A positive constant defining variations of \(G\) and \(B\) as a function of instantaneous effective confinement \(p'\) (default is 0.0) \(G=G_r(\frac{p'}{p'_r})^d\) \(B=B_r(\frac{p'}{p'_r})^d\) If \(\phi=0\), \(d\) is reset to 0.0. |
| `PTAng` ([float](https://docs.python.org/3/library/functions.html#float)) | (\(\phi_{PT}\)) Phase transformation angle, in degrees. |
| `contrac[2]` ([float](https://docs.python.org/3/library/functions.html#float)) | A non-negative constant reflecting \(K_\sigma\) effect. |
| `dilat[2]` ([float](https://docs.python.org/3/library/functions.html#float)) | A non-negative constant reflecting \(K_\sigma\) effect. |
| `contrac[1]` ([float](https://docs.python.org/3/library/functions.html#float)) | A non-negative constant reflecting dilation history on contraction tendency. |
| `liquefac[0]` ([float](https://docs.python.org/3/library/functions.html#float)) | Damage parameter to define accumulated permanent shear strain as a function of dilation history. (Redefined and different from PressureDependMultiYield material). |
| `liquefac[1]` ([float](https://docs.python.org/3/library/functions.html#float)) | Damage parameter to define biased accumulation of permanent shear strain as a function of load reversal history. (Redefined and different from PressureDependMultiYield material). |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | Numerical constant (default value = 0.1 kPa) |

See also [notes](http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material)
