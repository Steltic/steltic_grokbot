<!-- chunk_id: groundMotion_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/groundMotion.html",
 "title": "3.1.7.3.1. Ground Motion",
 "category": "command_manual",
 "manual_group": "model",
 "command": "groundMotion",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/groundMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3262,
 "word_count": 489,
 "has_code": true,
 "has_table": true
} -->

## 3.1.7.3.1. Ground Motion

The groundMotion command is used to construct a GroundMotion object used by the ImposedMotionSP constraints in a MultipleSupportExcitation object. This command is of the following form:

**groundMotion $tag $type arg1? ...**

The type of GroundMotion created and the additional arguments required depends on the type? provided in the command. The following contain information about type? and the args required for each of the available ground motion types:

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among ground motions in load pattern |
| $type | *string* | the type of ground motion |
| $args | *list float* | args specific to the type of motion |

There are presently two type of groundMotions that can be created: 1) Plain Ground Motion and 2) interpolaatedGroundMotion

#### Plain Ground Motion

Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. The particular form of the command is as follows:

**groundMotion $gmTag Plain <-accel $tsTag> <-vel $tsTag> <-disp $tsTag> <-int (IntegratorType intArgs)> <-fact $cFactor>)**

where

Note

The displacements are the ones used in the ImposedMotions to set nodal response.

Any combination of the acceleration, velocity and displacement time-series can be specified.

If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements. If only velocity are provided, numerical integration is used to obtain the displacements.

For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.

#### Interpolated Ground Motion

This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern. The command is as follows:

**groundMotion $tag Interpolated $gmTag1 $gmTag2 ... -fact $fact1 $fact2 ...**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among ground motions in load pattern |
| $gmTags | *list integer* | the tags of existing ground motions in pattern to be used for interpolation. |
| $factors | *list float* | the interpolation factors. |

Example:

The following example shows how to construct a **Multi-Suppert Excitation** pattern with a tag of **1* that will constrain the nodes **1**, **4**, and **7** to move in the **1** dof direcection with the ground Motion supplied by the **groundMotion** with tag **101**, whose displacement is given by **timeSeries** with a tag of 3.

1. **Tcl Code**

```
timeSeries Path 3 -filePath elCentroDisp.dat -dt 0.02
pattern MultipleSupport  1  {
     groundMotion 101 Series -disp 3

     imposedSupportMotion 1 1 101
     imposedSupportMotion 4 1 101
     imposedSupportMotion 7 1 101
}
```

1. **Python Code**

```
timeSeries('Path', 3, '-dt', 0.02, '-filePath', 'elCentroDisp.dat')
pattern('MultiSupport', 1)
groundMotion(101, 'Series', '-disp', 3)
imposedSupportMotion(1,1,101)
imposedSupportMotion(4,1,101)
imposedSupportMotion(7,1,101)
```

Code Developed by: **fmk**
