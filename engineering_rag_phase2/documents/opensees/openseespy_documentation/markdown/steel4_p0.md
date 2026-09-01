<!-- chunk_id: steel4_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/steel4.html",
 "title": "4.14.1.3. Steel4",
 "category": "general",
 "command": "steel4",
 "doc_section": "src",
 "rel_path": "src/steel4.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3253,
 "word_count": 314,
 "has_code": false,
 "has_table": true
} -->

## 4.14.1.3. Steel4

**uniaxialMaterial(*'Steel4'*, *matTag*, *Fy*, *E0*, *'-asym'*, *'-kin'*, *b_k*, **params*, *b_kc*, *R_0c*, *r_1c*, *r_2c*, *'-iso'*, *b_i*, *rho_i*, *b_l*, *R_i*, *l_yp*, *b_ic*, *rho_ic*, *b_lc*, *R_ic*, *'-ult'*, *f_u*, *R_u*, *f_uc*, *R_uc*, *'-init'*, *sig_init*, *'-mem'*, *cycNum*)**

This command is used to construct a general uniaxial material with combined kinematic and isotropic hardening and optional non-symmetric behavior.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield strength |
| `E0` ([float](https://docs.python.org/3/library/functions.html#float)) | initial elastic tangent |
| `'-kin'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | apply kinematic hardening |
| `b_k` ([float](https://docs.python.org/3/library/functions.html#float)) | hardening ratio (E_k/E_0) |
| `params` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | control the exponential transition from linear elastic to hardening asymptote `params=[R_0,r_1,r_2]`. Recommended values: `R_0 = 20, r_1 = 0.90, r_2 = 0.15` |
| `'-iso'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | apply isotropic hardening |
| `b_i` ([float](https://docs.python.org/3/library/functions.html#float)) | initial hardening ratio (E_i/E_0) |
| `b_l` ([float](https://docs.python.org/3/library/functions.html#float)) | saturated hardening ratio (E_is/E_0) |
| `rho_i` ([float](https://docs.python.org/3/library/functions.html#float)) | specifies the position of the intersection point between initial and saturated hardening asymptotes |
| `R_i` ([float](https://docs.python.org/3/library/functions.html#float)) | control the exponential transition from initial to saturated asymptote |
| `l_yp` ([float](https://docs.python.org/3/library/functions.html#float)) | length of the yield plateau in eps_y0 = f_y / E_0 units |
| `'-ult'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | apply an ultimate strength limit |
| `f_u` ([float](https://docs.python.org/3/library/functions.html#float)) | ultimate strength |
| `R_u` ([float](https://docs.python.org/3/library/functions.html#float)) | control the exponential transition from kinematic hardening to perfectly plastic asymptote |
| `'-asym'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | assume non-symmetric behavior |
| `'-init'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | apply initial stress |
| `sig_init` ([float](https://docs.python.org/3/library/functions.html#float)) | initial stress value |
| `'-mem'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | configure the load history memory |
| `cycNum` ([float](https://docs.python.org/3/library/functions.html#float)) | expected number of half-cycles during the loading process Efficiency of the material can be slightly increased by correctly setting this value. The default value is `cycNum = 50` Load history memory can be turned off by setting `cycNum = 0`. |

See also

[Steel4](http://opensees.berkeley.edu/wiki/index.php/Steel4_Material)
