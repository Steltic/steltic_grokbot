<!-- chunk_id: InitStrainMaterial_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/InitStrainMaterial.html",
 "title": "4.14.5.21. Initial Strain Material",
 "category": "material",
 "command": "InitStrainMaterial",
 "doc_section": "src",
 "rel_path": "src/InitStrainMaterial.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 840,
 "word_count": 88,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.21. Initial Strain Material

**uniaxialMaterial(*'InitStrainMaterial'*, *matTag*, *otherTag*, *initStrain*)**

This command is used to construct an Initial Strain material object. The stress-strain behaviour for this material is defined by another material. Initial Strain Material enables definition of initial strains for the material under consideration. The stress that corresponds to the initial strain will be calculated from the other material.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `otherTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the other material |
| `initStrain` ([float](https://docs.python.org/3/library/functions.html#float)) | initial strain |

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Initial_Strain_Material)
