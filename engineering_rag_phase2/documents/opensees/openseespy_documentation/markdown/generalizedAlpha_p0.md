<!-- chunk_id: generalizedAlpha_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/generalizedAlpha.html",
 "title": "5.6.2.4. Generalized Alpha Method",
 "category": "general",
 "command": "generalizedAlpha",
 "doc_section": "src",
 "rel_path": "src/generalizedAlpha.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1882,
 "word_count": 229,
 "has_code": false,
 "has_table": true
} -->

## 5.6.2.4. Generalized Alpha Method

**integrator(*'GeneralizedAlpha'*, *alphaM*, *alphaF*, *gamma=0.5+alphaM-alphaF*, *beta=(1+alphaM-alphaF)^2/4*)**

Create a GeneralizedAlpha integrator. This is an implicit method that like the HHT method allows for high frequency energy dissipation and second order accuracy, i.e. \(\Delta t^2\). Depending on choices of input parameters, the method can be unconditionally stable.

| `alphaM` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_M\) factor. |
| --- | --- |
| `alphaF` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha_F\) factor. |
| `gamma` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\gamma\) factor. (optional) |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\beta\) factor. (optional) |

1. Like Newmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
2. \(\alpha_M\) = 1.0, \(\alpha_F\) = 1.0 produces the Newmark Method.
3. \(\alpha_M\) = 1.0 corresponds to the `integrator.HHT()` method.
4. The method is second-order accurate provided \(\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F\)
5. The method is unconditionally stable provided \(\alpha_M >= \alpha_F >= \tfrac{1}{2}, \beta>=\tfrac{1}{4} +\tfrac{1}{2}(\gamma_M - \gamma_F)\)
6. \(\gamma\) and \(\beta\) are optional. The default values ensure the method is unconditionally stable, second order accurate and high frequency dissipation is maximized.

  The defaults are:

  \(\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F\)

  and

  \(\beta = \tfrac{1}{4}(1 + \alpha_M - \alpha_F)^2\)
