<!-- chunk_id: TzLiq1_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/TzLiq1.html",
 "title": "4.14.4.5. TzLiq1 Material",
 "category": "material",
 "command": "TzLiq1",
 "doc_section": "src",
 "rel_path": "src/TzLiq1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2885,
 "word_count": 371,
 "has_code": false,
 "has_table": true
} -->

## 4.14.4.5. TzLiq1 Material

> The command constructs a uniaxial t-z material that incorporates liquefaction effects. This t z material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh. The t-z material obtains the average mean effective stress (which decreases with increasing excess pore pressure) from two specified soil elements. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements. There are two possible forms:

**uniaxialMaterial(*'TzLiq1'*, *matTag*, *tzType*, *tult*, *z50*, *c*, *ele1*, *ele2*)**

**uniaxialMaterial(*'TzLiq1'*, *matTag*, *tzType*, *tult*, *z50*, *c*, *'-timeSeries'*, *timeSeriesTag*)**

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `tzType` ([int](https://docs.python.org/3/library/functions.html#int)) | tzType = 1 Backbone of t-z curve approximates Reese and O’Neill (1987). tzType = 2 Backbone of t-z curve approximates Mosher (1984) relation. |
| `tult` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate capacity of the t-z material. SEE NOTE 1. |
| `z50` ([float](https://docs.python.org/3/library/functions.html#float)) | Displacement at which 50% of tult is mobilized in monotonic loading. |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). |
| `ele1` `ele2` ([int](https://docs.python.org/3/library/functions.html#int)) | are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures |
| `timeSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Alternatively, mean effective stress can be supplied by a time series by specifying the text string `'-timeSeries'` and the tag of the seriesm `seriesTag`. |

Note

1. The argument `tult` is the ultimate capacity of the t-z material. Note that `t` or `tult` are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].
2. Nonzero `c` values are used to represent radiation damping effects
3. To model the effects of liquefaction with `TzLiq1`, it is necessary to use the `updateMaterialStage` command. When material stage is 0 (which is the default value), the `TzLiq1` behavior will be independent of any pore pressure in the specified solidElem’s. When material stage is set to 1, the behviour of `TzLiq1` will depend on the mean effective stresses (and hence excess pore pressures) in the solidElem’s.

See also

[Notes](https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/TzLiq1.html)
