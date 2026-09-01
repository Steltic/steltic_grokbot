<!-- chunk_id: velnormal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/velnormal.html",
 "title": "4.17.3. Velocity and Normal Force Dependent Friction",
 "category": "general",
 "command": "velnormal",
 "doc_section": "src",
 "rel_path": "src/velnormal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1580,
 "word_count": 159,
 "has_code": false,
 "has_table": true
} -->

## 4.17.3. Velocity and Normal Force Dependent Friction

**frictionModel(*'VelNormalFrcDep'*, *frnTag*, *aSlow*, *nSlow*, *aFast*, *nFast*, *alpha0*, *alpha1*, *alpha2*, *maxMuFact*)**

This command is used to construct a VelNormalFrcDep friction model object.

| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique friction model tag |
| --- | --- |
| `aSlow` ([float](https://docs.python.org/3/library/functions.html#float)) | constant for coefficient of friction at low velocity |
| `nSlow` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent for coefficient of friction at low velocity |
| `aFast` ([float](https://docs.python.org/3/library/functions.html#float)) | constant for coefficient of friction at high velocity |
| `nFast` ([float](https://docs.python.org/3/library/functions.html#float)) | exponent for coefficient of friction at high velocity |
| `alpha0` ([float](https://docs.python.org/3/library/functions.html#float)) | constant rate parameter coefficient |
| `alpha1` ([float](https://docs.python.org/3/library/functions.html#float)) | linear rate parameter coefficient |
| `alpha2` ([float](https://docs.python.org/3/library/functions.html#float)) | quadratic rate parameter coefficient |
| `maxMuFact` ([float](https://docs.python.org/3/library/functions.html#float)) | factor for determining the maximum coefficient of friction. This value prevents the friction coefficient from exceeding an unrealistic maximum value when the normal force becomes very small. The maximum friction coefficient is determined from μFast, for example \(\mu \leq maxMuFac*μFast\). |
