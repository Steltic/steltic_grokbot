<!-- chunk_id: groundMotion_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/groundMotion.html",
 "title": "4.8.3.1. Plain Ground Motion",
 "category": "general",
 "command": "groundMotion",
 "doc_section": "src",
 "rel_path": "src/groundMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1766,
 "word_count": 203,
 "has_code": false,
 "has_table": true
} -->

## 4.8.3.1. Plain Ground Motion

**groundMotion(*gmTag*, *'Plain'*, *'-disp'*, *dispSeriesTag*, *'-vel'*, *velSeriesTag*, *'-accel'*, *accelSeriesTag*, *'-int'*, *tsInt='Trapezoidal'*, *'-fact'*, *factor=1.0*)**

This command is used to construct a plain GroundMotion object. Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. T

| `gmTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique tag among ground motions in load pattern |
| --- | --- |
| `dispSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the displacement history. (optional) |
| `velSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the velocity history. (optional) |
| `accelSeriesTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of the TimeSeries series defining the acceleration history. (optional) |
| `tsInt` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | `'Trapezoidal'` or `'Simpson'` numerical integration method |
| `factor` ([float](https://docs.python.org/3/library/functions.html#float)) | constant factor. (optional) |

Note

1. The displacements are the ones used in the ImposedMotions to set nodal response.
2. If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements.
3. For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.
4. Any combination of the acceleration, velocity and displacement time-series can be specified.
