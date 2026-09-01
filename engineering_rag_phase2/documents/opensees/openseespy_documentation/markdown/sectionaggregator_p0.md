<!-- chunk_id: sectionaggregator_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/sectionaggregator.html",
 "title": "4.16.9. Section Aggregator",
 "category": "section",
 "command": "sectionaggregator",
 "doc_section": "src",
 "rel_path": "src/sectionaggregator.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1436,
 "word_count": 161,
 "has_code": false,
 "has_table": true
} -->

## 4.16.9. Section Aggregator

**section(*'Aggregator'*, *secTag*, **mats*, *'-section'*, *sectionTag*)**

This command is used to construct a SectionAggregator object which aggregates groups previously-defined UniaxialMaterial objects into a single section force-deformation model. Each UniaxialMaterial object represents the section force-deformation response for a particular section degree-of-freedom (dof). There is no interaction between responses in different dof directions. The aggregation can include one previously defined section.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `mats` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | list of tags and dofs of previously-defined UniaxialMaterial objects, `mats = [matTag1,dof1,matTag2,dof2,...]` the force-deformation quantity to be modeled by this section object. One of the following section dof may be used: `'P'` Axial force-deformation `'Mz'` Moment-curvature about section local z-axis `'Vy'` Shear force-deformation along section local y-axis `'My'` Moment-curvature about section local y-axis `'Vz'` Shear force-deformation along section local z-axis `'T'` Torsion Force-Deformation |
| `sectionTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships (optional) |
