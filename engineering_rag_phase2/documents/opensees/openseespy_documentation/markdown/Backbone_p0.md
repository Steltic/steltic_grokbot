<!-- chunk_id: Backbone_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Backbone.html",
 "title": "4.14.5.40. Backbone Material",
 "category": "material",
 "command": "Backbone",
 "doc_section": "src",
 "rel_path": "src/Backbone.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1304,
 "word_count": 79,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.40. Backbone Material

**uniaxialMaterial(*'Backbone'*, *matTag*, *backboneTag*)**

This command uses a Hysteretic Backbone object to represent a path-independent uniaxial material. Since it is path-independent, no state information is stored by BackboneMaterial.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `backboneTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying a predefined backbone function. |

#### 4.14.5.40.1. Hysteretic Backbone

HystereticBackbone represents a backbone curve for hysteretic models.

1. [ArctangentBackbone](https://openseespydoc.readthedocs.io/en/latest/src/ArctangentBackbone.html)
2. [BilinearBackbone](https://openseespydoc.readthedocs.io/en/latest/src/BilinearBackbone.html)
3. [ManderBackbone](https://openseespydoc.readthedocs.io/en/latest/src/ManderBackbone.html)
4. [MultilinearBackbone](https://openseespydoc.readthedocs.io/en/latest/src/MultilinearBackbone.html)
5. [TrilinearBackbone](https://openseespydoc.readthedocs.io/en/latest/src/TrilinearBackbone.html)
6. [MaterialBackbone](https://openseespydoc.readthedocs.io/en/latest/src/MaterialBackbone.html)
7. [ReeseStiffClayBelowWS](https://openseespydoc.readthedocs.io/en/latest/src/ReeseStiffClayBelowWS.html)
