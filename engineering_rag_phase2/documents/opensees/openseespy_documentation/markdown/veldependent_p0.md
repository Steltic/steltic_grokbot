<!-- chunk_id: veldependent_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/veldependent.html",
 "title": "4.17.2. Velocity Dependent Friction",
 "category": "general",
 "command": "veldependent",
 "doc_section": "src",
 "rel_path": "src/veldependent.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1311,
 "word_count": 151,
 "has_code": false,
 "has_table": true
} -->

## 4.17.2. Velocity Dependent Friction

**frictionModel(*'VelDependent'*, *frnTag*, *muSlow*, *muFast*, *transRate*)**

This command is used to construct a VelDependent friction model object. It is useful for modeling the behavior of [PTFE](http://en.wikipedia.org/wiki/Polytetrafluoroethylene) or PTFE-like materials sliding on a stainless steel surface. For a detailed presentation on the velocity dependence of such interfaces please refer to Constantinou et al. (1999).

| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique friction model tag |
| --- | --- |
| `muSlow` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of friction at low velocity |
| `muFast` ([float](https://docs.python.org/3/library/functions.html#float)) | coefficient of friction at high velocity |
| `transRate` ([float](https://docs.python.org/3/library/functions.html#float)) | transition rate from low to high velocity |

\[\mu = {\mu _{fast}} - \left( {{\mu _{fast}} - {\mu _{slow}}} \right) \cdot {e^{ - transRate\, \cdot \,\left| v \right|}}\]

REFERENCE:

Constantinou, M.C., Tsopelas, P., Kasalanati, A., and Wolff, E.D. (1999). “Property modification factors for seismic isolation bearings”. Report MCEER-99-0012, Multidisciplinary Center for Earthquake Engineering Research, State University of New York.
