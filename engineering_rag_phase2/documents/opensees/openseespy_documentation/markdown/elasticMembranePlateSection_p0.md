<!-- chunk_id: elasticMembranePlateSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticMembranePlateSection.html",
 "title": "4.16.11. Elastic Membrane Plate Section",
 "category": "section",
 "command": "elasticMembranePlateSection",
 "doc_section": "src",
 "rel_path": "src/elasticMembranePlateSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 910,
 "word_count": 85,
 "has_code": false,
 "has_table": true
} -->

## 4.16.11. Elastic Membrane Plate Section

**section(*'ElasticMembranePlateSection'*, *secTag*, *E_mod*, *nu*, *h*, *rho*, *<Ep_modifier>*)**

This command allows the user to construct an ElasticMembranePlateSection object, which is an isotropic section appropriate for plate and shell analysis.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | Young’s Modulus |
| `nu` ([float](https://docs.python.org/3/library/functions.html#float)) | Poisson’s Ratio |
| `h` ([float](https://docs.python.org/3/library/functions.html#float)) | depth of section |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | mass density |
| `Ep_modifier` ([float](https://docs.python.org/3/library/functions.html#float)) | factor to modify out-of-plane bending stiffness (optional). E_plate = Ep_modifier*E_mod |
