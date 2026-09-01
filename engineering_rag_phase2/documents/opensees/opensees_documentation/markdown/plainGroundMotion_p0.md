<!-- chunk_id: plainGroundMotion_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/plainGroundMotion.html",
 "title": "Plain Ground Motion",
 "category": "command_manual",
 "manual_group": "model",
 "command": "plainGroundMotion",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/plainGroundMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1125,
 "word_count": 159,
 "has_code": true,
 "has_table": false
} -->

## Plain Ground Motion

This command is used to construct a plain GroundMotion object. Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. The command is as follows:

**`groundMotion`(*$gmTag Plain <-accel $tsTag> <-vel $tsTag> <-disp $tsTag> <-int (IntegratorType intArgs)> <-fact $cFactor>*)**

where

Note

The displacements are the ones used in the ImposedMotions to set nodal response.

Any combination of the acceleration, velocity and displacement time-series can be specified.

If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements.

For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.

```
timeSeries Sine 1 0 20.0 $period -factor $mag
pattern MultipleSupport  1   {
   groundMotion 1  Series -disp 1

   imposedSupportMotion 1 1 1
   imposedSupportMotion 4 1 1
   imposedSupportMotion 7 1 1
 }
```

Code Developed by: **fmk**
