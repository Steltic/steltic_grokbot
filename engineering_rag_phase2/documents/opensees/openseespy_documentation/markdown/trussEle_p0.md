<!-- chunk_id: trussEle_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/trussEle.html",
 "title": "4.2.2.1. Truss Element",
 "category": "element",
 "command": "trussEle",
 "doc_section": "src",
 "rel_path": "src/trussEle.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2354,
 "word_count": 264,
 "has_code": false,
 "has_table": true
} -->

## 4.2.2.1. Truss Element

This command is used to construct a truss element object. There are two ways to construct a truss element object:

**element(*'Truss'*, *eleTag*, **eleNodes*, *A*, *matTag*, *<'-rho'*, *rho>*, *<'-cMass'*, *cFlag>*, *<'-doRayleigh'*, *rFlag>*)**

One way is to specify an area and a UniaxialMaterial identifier:

**element(*'TrussSection'*, *eleTag*, **eleNodes*, *secTag*, *<'-rho'*, *rho>*, *<'-cMass'*, *cFlag>*, *<'-doRayleigh'*, *rFlag>*)**

the other is to specify a Section identifier:

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `A` ([float](https://docs.python.org/3/library/functions.html#float)) | cross-sectional area of element |
| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined UniaxialMaterial |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag associated with previously-defined Section |
| `rho` ([float](https://docs.python.org/3/library/functions.html#float)) | mass per unit length, optional, default = 0.0 |
| `cFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | consistent mass flag, optional, default = 0 `cFlag` = 0 lumped mass matrix (default) `cFlag` = 1 consistent mass matrix |
| `rFlag` ([float](https://docs.python.org/3/library/functions.html#float)) | Rayleigh damping flag, optional, default = 0 `rFlag` = 0 NO RAYLEIGH DAMPING (default) `rFlag` = 1 include Rayleigh damping |

Note

1. The truss element DOES NOT include geometric nonlinearities, even when used with beam-columns utilizing P-Delta or Corotational transformations.
2. When constructed with a UniaxialMaterial object, the truss element considers strain-rate effects, and is thus suitable for use as a damping element.
3. The valid queries to a truss element when creating an ElementRecorder object are ‘axialForce,’ ‘forces,’ ‘localForce’, deformations,’ ‘material matArg1 matArg2…,’ ‘section sectArg1 sectArg2…’ There will be more queries after the interface for the methods involved have been developed further.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/Truss_Element)
