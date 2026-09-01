<!-- chunk_id: PyLiq1_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/PyLiq1.html",
 "title": "4.14.4.4. PyLiq1 Material",
 "category": "material",
 "command": "PyLiq1",
 "doc_section": "src",
 "rel_path": "src/PyLiq1.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3759,
 "word_count": 481,
 "has_code": false,
 "has_table": true
} -->

## 4.14.4.4. PyLiq1 Material

> This command constructs a uniaxial p-y material that incorporates liquefaction effects. This p y material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh or displacement boundary condition. The p-y material obtains the average mean effective stress (which decreases with increasing excess pore pressure) either from two specified soil elements, or from a time series. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements, or PressureDependMultiYield or PressureDependMultiYield02 materials in FourNodeQuadUP or NineFourQuadUP elements. There are two possible forms:

**uniaxialMaterial(*'PyLiq1'*, *matTag*, *soilType*, *pult*, *Y50*, *Cd*, *c*, *pRes*, *ele1*, *ele2*)**

**uniaxialMaterial(*'PyLiq1'*, *matTag*, *soilType*, *pult*, *Y50*, *Cd*, *c*, *pRes*, *'-timeSeries'*, *timeSeriesTag*)**

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `soilType` ([int](https://docs.python.org/3/library/functions.html#int)) | soilType = 1 Backbone of p-y curve approximates Matlock (1970) soft clay relation. soilType = 2 Backbone of p-y curve approximates API (1993) sand relation. |
| `pult` ([float](https://docs.python.org/3/library/functions.html#float)) | Ultimate capacity of the p-y material. Note that “p” or “pult” are distributed loads [force per length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e., distributed load times the tributary length of the pile]. |
| `Y50` ([float](https://docs.python.org/3/library/functions.html#float)) | Displacement at which 50% of pult is mobilized in monotonic loading. |
| `Cd` ([float](https://docs.python.org/3/library/functions.html#float)) | Variable that sets the drag resistance within a fully-mobilized gap as Cd*pult. |
| `c` ([float](https://docs.python.org/3/library/functions.html#float)) | The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). (optional Default = 0.0). Nonzero c values are used to represent radiation damping effects |
| `pRes` ([float](https://docs.python.org/3/library/functions.html#float)) | sets the minimum (or residual) peak resistance that the material retains as the adjacent solid soil elements liquefy |
| `ele1` `ele2` ([int](https://docs.python.org/3/library/functions.html#int)) | are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures |
| `timeSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | Alternatively, mean effective stress can be supplied by a time series by specifying the text string `'-timeSeries'` and the tag of the series `seriesTag`. |

Note

1. The argument `pult` is the ultimate capacity of the p-y material. Note that `p` or `pult` are lateral stresses [force per unit length of pile] in common design equations, but are both loads for this uniaxialMaterial [i.e.,  distributed load times the tributary length of the pile].
2. Nonzero `c` values are used to represent radiation damping effects
3. To model the effects of liquefaction with `PyLiq1`, it is necessary to use the `updateMaterialStage` command. When material stage is 0 (which is the default value), the `PyLiq1` behavior will be independent of any pore pressure in the specified solidElem’s. When material stage is set to 1, the behviour of `PyLiq1` will depend on the mean effective stresses (and hence excess pore pressures) in the solidElem’s.

See also

[Notes](https://opensees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/PyLiq1.html)
