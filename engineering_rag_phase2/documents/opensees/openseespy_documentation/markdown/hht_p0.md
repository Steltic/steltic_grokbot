<!-- chunk_id: hht_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/hht.html",
 "title": "5.6.2.3. Hilber-Hughes-Taylor Method",
 "category": "general",
 "command": "hht",
 "doc_section": "src",
 "rel_path": "src/hht.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1509,
 "word_count": 197,
 "has_code": false,
 "has_table": true
} -->

## 5.6.2.3. Hilber-Hughes-Taylor Method

**integrator(*'HHT'*, *alpha*, *gamma=1.5-alpha*, *beta=(2-alpha)^2/4*)**

Create a Hilber-Hughes-Taylor (HHT) integrator. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular Newmark object). Depending on choices of input parameters, the method can be unconditionally stable.

| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\alpha\) factor. |
| --- | --- |
| `gamma` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\gamma\) factor. (optional) |
| `beta` ([float](https://docs.python.org/3/library/functions.html#float)) | \(\beta\) factor. (optional) |

1. Like Mewmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
2. \(\alpha\) = 1.0 corresponds to the Newmark method.
3. \(\alpha\) should be between 0.67 and 1.0. The smaller the \(\alpha\) the greater the numerical damping.
4. \(\gamma\) and \(\beta\) are optional. The default values ensure the method is second order accurate and unconditionally stable when \(\alpha\) is \(\tfrac{2}{3} <= \alpha <= 1.0\). The defaults are:

  \(\beta = \frac{(2 - \alpha)^2}{4}\)

  and

  \(\gamma = \frac{3}{2} - \alpha\)
