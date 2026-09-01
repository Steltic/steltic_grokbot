<!-- chunk_id: uniaxialsection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/uniaxialsection.html",
 "title": "4.16.10. Uniaxial Section",
 "category": "section",
 "command": "uniaxialsection",
 "doc_section": "src",
 "rel_path": "src/uniaxialsection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 926,
 "word_count": 105,
 "has_code": false,
 "has_table": true
} -->

## 4.16.10. Uniaxial Section

**section(*'Uniaxial'*, *secTag*, *matTag*, *quantity*)**

This command is used to construct a UniaxialSection object which uses a previously-defined UniaxialMaterial object to represent a single section force-deformation response quantity.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of uniaxial material |
| `quantity` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the force-deformation quantity to be modeled by this section object. One of the following section dof may be used: `'P'` Axial force-deformation `'Mz'` Moment-curvature about section local z-axis `'Vy'` Shear force-deformation along section local y-axis `'My'` Moment-curvature about section local y-axis `'Vz'` Shear force-deformation along section local z-axis `'T'` Torsion Force-Deformation |
