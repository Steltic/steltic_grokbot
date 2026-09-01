<!-- chunk_id: curvedPipe_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/curvedPipe.html",
 "title": "4.2.3.12. Curved Pipe Element",
 "category": "element",
 "command": "curvedPipe",
 "doc_section": "src",
 "rel_path": "src/curvedPipe.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3613,
 "word_count": 421,
 "has_code": true,
 "has_table": true
} -->

## 4.2.3.12. Curved Pipe Element

A 3D pipe element can be used for piping network similar to [Elastic Pipe Element](https://openseespydoc.readthedocs.io/en/latest/src/pipe.html) for a curved-shape pipe.

The temperature is set through [setNodeTemperature command](https://openseespydoc.readthedocs.io/en/latest/src/setNodeTemperature.html).

**element(*'Pipe'*, *eleTag*, **eleNodes*, *pipeMatTag*, *pipeSecTag*, *xC*, *yC*, *zC*, *<'-Ti'>*, *<'-T0'*, *T0>*, *<'-p'*, *p>*, *<'-tolWall'>*, *<'-noThermalLoad'>*, *<'-noPressureLoad'>*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `eleNodes` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of two element nodes |
| `pipeMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined [Pipe Material](https://openseespydoc.readthedocs.io/en/latest/src/pipeMaterial.html) |
| `pipeSecTag` ([int](https://docs.python.org/3/library/functions.html#int)) | identifier for previously-defined [Pipe Section](https://openseespydoc.readthedocs.io/en/latest/src/pipeSection.html) |
| `x_c`, `y_C`, `z_C` ([float](https://docs.python.org/3/library/functions.html#float)) | the coordinates for the center of the curve or the tangent intersection point if the option `'-Ti'` is given. |
| `'-Ti'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | if the option `'-TI'` is provided, the coordinates `xC`, `yC`, `zC` are for the tangent intersection point, which will be converted internally to the coordinates of the center point. |
| `T0` ([float](https://docs.python.org/3/library/functions.html#float)) | the stress-free temperature, which must follow the option `'-T0'` and will be added to the average temperature for the element. Default is `0`. |
| `p` ([float](https://docs.python.org/3/library/functions.html#float)) | the internal pressure, which must follow the option `'-p'`. The internal pressure will affect the axial deformation for the straight pipe element. Default is `0`. |
| `'-tolWall'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | the tolerance for checking radius and the optional interaction point as a fraction of wall thickness and must follow the option `'-tolWall'`. Default is `0.1`. |
| `'-noThermalLoad'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Do not include the load due to thermal effects. Default is to include. |
| `'-noPressureLoad'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | Do not include the load due to internal pressure effects. Default is to include. |

Note

Only the uniform load is accepted by the pipe elements
for applying the gravity load. Different to
regular eleLoad, the load values are interpreted
in the global coordinate system as it’s convenient
for the curved pipe elements. For example,

```
ops.eleLoad('-ele', *eleTags, '-type', '-beamUniform', wy, wz, wx)
```

where `wy`, `wz`, and `wx` are the member load per length in the global axes.

Note

The element responses can be obtained by

```
res = ops.eleResponse(ele, 'sectionI')
res = ops.eleResponse(ele, 'sectionC')
res = ops.eleResponse(ele, 'sectionJ')
res = ops.eleResponse(ele, 'sectionX', perc)
```

where the commands above return
the section forces at node I, center, node J,
or any section X.

- `perc = -1`: section I, i.e. \(\theta = -\theta_0\)
- `perc = 0`: center section, i.e. \(\theta = 0\)
- `perc = 1`: section I, i.e. \(\theta = \theta_0\)
- other `perc`: section at \(\theta = perc \times\theta_0\)
