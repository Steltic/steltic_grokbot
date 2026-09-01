<!-- chunk_id: eleload_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/eleload.html",
 "title": "4.8.1.2. eleLoad command",
 "category": "general",
 "command": "eleload",
 "doc_section": "src",
 "rel_path": "src/eleload.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3938,
 "word_count": 492,
 "has_code": true,
 "has_table": true
} -->

## 4.8.1.2. eleLoad command

**eleLoad(*'-ele'*, **eleTags*, *'-range'*, *eleTag1*, *eleTag2*, *'-type'*, *'-beamUniform'*, *Wy*, *<Wz>*, *Wx=0.0*, *'-beamPoint'*, *Py*, *<Pz>*, *xL*, *Px=0.0*, *'-beamThermal'*, **tempPts*)**

The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

| `eleTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | tag of PREVIOUSLY DEFINED element |
| --- | --- |
| `eleTag1` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag |
| `eleTag2` ([int](https://docs.python.org/3/library/functions.html#int)) | element tag |
| `Wx` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of uniformily distributed ref load acting in direction along member length. (optional) |
| `Wy` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of uniformily distributed ref load acting in local y direction of element |
| `Wz` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of uniformily distributed ref load acting in local z direction of element. (required only for 3D) |
| `Px` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of ref point load acting in direction along member length. (optional) |
| `Py` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of ref point load acting in local y direction of element |
| `Pz` ([float](https://docs.python.org/3/library/functions.html#float)) | mag of ref point load acting in local z direction of element. (required only for 3D) |
| `xL` ([float](https://docs.python.org/3/library/functions.html#float)) | location of point load relative to node I, prescribed as fraction of element length |
| `tempPts` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([float](https://docs.python.org/3/library/functions.html#float))) | temperature points: `temPts = [T1, y1, T2, y2, ..., T9, y9]` Each point `(T1, y1)` define a temperature and location. This command may accept 2,5 or 9 temperature points. |

**Uniform (full span)** — `NDM` = 2:

```
ops.eleLoad('-ele', eleTag, '-type', '-beamUniform', Wy, Wx)
```

**Trapezoidal (partial span, 2D)** — intensity varies linearly between normalized positions `aOverL` and `bOverL` (fraction of length, 0 to 1). Give transverse and axial intensities at start (\(W_{ya}\), \(W_{xa}\)) and end (\(W_{yb}\), \(W_{xb}\)). Supported by 2D `elasticBeamColumn` and `forceBeamColumn`:

```
ops.eleLoad('-ele', eleTag, '-type', '-beamUniform',
            Wya, Wxa, aOverL, bOverL, Wyb, Wxb)
```

**Uniform** — `NDM` = 3:

```
ops.eleLoad('-ele', eleTag, '-type', '-beamUniform', Wy, Wz, Wx)
```

For **trapezoidal** loads in 3D, pass `Wy`, `Wz`, `Wx`, `aOverL`, `bOverL`, then end values `Wyb`, `Wzb`, `Wxb`. Some 3D `elasticBeamColumn` paths may approximate a segment as triangular; combine loads if you need an exact trapezoid.

**Point load** — `NDM` = 2:

```
ops.eleLoad('-range', eleTag1, eleTag2, '-type', '-beamPoint', Py, xL, Px)
```

`NDM` = 3:

```
ops.eleLoad('-range', eleTag1, eleTag2, '-type', '-beamPoint', Py, Pz, xL, Px)
```

Example

Uniform span load and a 2D trapezoidal segment from \(0.2L\) to \(0.8L\).

```
import openseespy.opensees as ops

width = 20.0
W = 4000.0
wya, wxa = -0.5, 0.0
a_over_l, b_over_l = 0.2, 0.8
wyb, wxb = -1.0, 0.0
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
ops.eleLoad('-ele', 3, '-type', '-beamUniform', -W / width)
ops.eleLoad('-ele', 4, '-type', '-beamUniform',
            wya, wxa, a_over_l, b_over_l, wyb, wxb)
```

Note

1. The load values are reference load values, it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the element.
2. At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.
