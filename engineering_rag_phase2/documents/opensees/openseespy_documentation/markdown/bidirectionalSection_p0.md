<!-- chunk_id: bidirectionalSection_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/bidirectionalSection.html",
 "title": "4.16.13. Bidirectional Section",
 "category": "section",
 "command": "bidirectionalSection",
 "doc_section": "src",
 "rel_path": "src/bidirectionalSection.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1400,
 "word_count": 149,
 "has_code": false,
 "has_table": true
} -->

## 4.16.13. Bidirectional Section

**section(*'Bidirectional'*, *secTag*, *E_mod*, *Fy*, *Hiso*, *Hkin*, *code1='Vy'*, *code2='P'*)**

This command allows the user to construct a Bidirectional section, which is a stress-resultant plasticity model of two coupled forces. The yield surface is circular and there is combined isotropic and kinematic hardening.

| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique section tag |
| --- | --- |
| `E_mod` ([float](https://docs.python.org/3/library/functions.html#float)) | elastic modulus |
| `Fy` ([float](https://docs.python.org/3/library/functions.html#float)) | yield force |
| `Hiso` ([float](https://docs.python.org/3/library/functions.html#float)) | isotropic hardening modulus |
| `Hkin` ([float](https://docs.python.org/3/library/functions.html#float)) | kinematic hardening modulus |
| `code1` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | section force code for direction 1 (optional) |
| `code2` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | section force code for direction 2 (optional) One of the following section code may be used: `'P'` Axial force-deformation `'Mz'` Moment-curvature about section local z-axis `'Vy'` Shear force-deformation along section local y-axis `'My'` Moment-curvature about section local y-axis `'Vz'` Shear force-deformation along section local z-axis `'T'` Torsion Force-Deformation |
