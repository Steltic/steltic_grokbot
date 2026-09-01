<!-- chunk_id: ManderBackbone_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ManderBackbone.html",
 "title": "4.14.5.40.1.3. ManderBackbone",
 "category": "general",
 "command": "ManderBackbone",
 "doc_section": "src",
 "rel_path": "src/ManderBackbone.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 744,
 "word_count": 68,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.40.1.3. ManderBackbone

**hystereticBackbone(*'Mander'*, *backboneTag*, *fc*, *epsc*, *E*)**

The backbone function \(F(x)\) is developed by Mander, Priestly, and Park (1988) and defined as

\[ \begin{align}\begin{aligned}F(x) = -f_c\frac{sr}{r-1+s^r}\\s = x / \epsilon_c\\r = \frac{E}{E-f_c/\epsilon_c}\end{aligned}\end{align} \]

| `backboneTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the backbone function. |
| --- | --- |
| `fc` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(f_c\). |
| `epsc` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(\epsilon_c\). |
| `E` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(E\). |
