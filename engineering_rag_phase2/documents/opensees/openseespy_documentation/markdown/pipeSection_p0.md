<!-- chunk_id: pipeSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/pipeSection.html",
 "title": "4.16.16. Pipe Section",
 "category": "section",
 "command": "pipeSection",
 "doc_section": "src",
 "rel_path": "src/pipeSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1544,
 "word_count": 175,
 "has_code": false,
 "has_table": true
} -->

## 4.16.16. Pipe Section

**section(*'Pipe'*, *secTag*, *do*, *t*, *<'-alphaV'*, *alphaV>*, *<'-defaultAlphaV'>*, *<'-rho'*, *rho>*)**

The pipe section should be used with [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html) and [Curved Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/curvedPipe.html) for pipes.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `do` ([float](https://docs.python.org/3/library/functions.html#float)) | the outside diameter of the pipe |
| `t` ([float](https://docs.python.org/3/library/functions.html#float)) | the thickness of the pipe wall |
| `alphaV` ([float](https://docs.python.org/3/library/functions.html#float)) | the shape factor for shear distortion and must follow the option `'-alphaV'`. This is optional to be set by the user. |
| `'-defaultAlphaV'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | use the option to set the shape factor to the default value \(\alpha_V = \frac{4}{3}\frac{r_o^3-r_i^3}{(r_o^2+r_i^2)(r_o-r_i)}\) where \(r_o=d_o/2\) and \(r_i=r_o-t\). If neither `'-alphaV'` nor `'-defaultAlphaV'` is used, the shear distortion is ignored. If both are given, the last one is used. |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | the mass per unit length of the section, which is used as mass coefficient in the dynamic analysis and will **not** be used to apply the gravity load, which should be added using the ops.eleLoad command. Default is `0`. |
