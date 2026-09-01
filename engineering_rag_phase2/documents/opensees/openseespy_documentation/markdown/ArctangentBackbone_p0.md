<!-- chunk_id: ArctangentBackbone_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ArctangentBackbone.html",
 "title": "4.14.5.40.1.1. ArctangentBackbone",
 "category": "general",
 "command": "ArctangentBackbone",
 "doc_section": "src",
 "rel_path": "src/ArctangentBackbone.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 718,
 "word_count": 63,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.40.1.1. ArctangentBackbone

**hystereticBackbone(*'Arctangent'*, *backboneTag*, *K1*, *gamma*, *alpha*)**

The backbone function \(F(x)\) is developed by Ranzo and Petrangeli (1998) and defined as

\[ \begin{align}\begin{aligned}F(x) = K_1atan(K_2x)\\K_2 = tan(\alpha)/\gamma\end{aligned}\end{align} \]

| `backboneTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the backbone function. |
| --- | --- |
| `K1` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(K_1\). |
| `gamma` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(\gamma\). |
| `alpha` ([float](https://docs.python.org/3/library/functions.html#float)) | parameter \(\alpha\). |
