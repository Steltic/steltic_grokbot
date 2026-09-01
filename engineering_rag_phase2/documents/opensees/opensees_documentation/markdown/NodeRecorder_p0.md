<!-- chunk_id: NodeRecorder_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/output/NodeRecorder.html",
 "title": "3.3.1.1. Node Recorder",
 "category": "command_manual",
 "manual_group": "output",
 "command": "NodeRecorder",
 "doc_section": "user/manual/output",
 "rel_path": "user/manual/output/NodeRecorder.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4315,
 "word_count": 744,
 "has_code": true,
 "has_table": true
} -->

## 3.3.1.1. Node Recorder

The Node recorder type records the response of a number of nodes at every converged step. The command to create a node recorder is:

**recorder(*Node*, *<-file $filename>*, *<-xml $filename>*, *<-binary $filename>*, *<-tcp $inetAddress $port>*, *<-precision $nSD>*, *<-timeSeries $tsTag>*, *<-time>*, *<-dT $deltaT>*, *<-closeOnWrite>*, *<-node $nodeTags>*, *< -nodeRange $startNode $endNode>*, *<-region $regionTag> -dof $dofs $respType*)**

| Argument | Type | Description |
| --- | --- | --- |
| $fileName | *string* | optional: name of file to which output is sent. |
| $inetAddr | *string* | optional: ip address (“xx.xx.xx.xx”) of remote machine |
| $port | *integer* | optional: port on remote machine awaiting tcp |
| $nSD | *integer* | optional: number of significant digits (optional: default is 6) |
| -time | *string* | optional: places domain time in first output column. |
| -closeOnWrite | *string* | optional: opens and closes file on each write. |
| $deltaT | *float* | optional: time interval for recording. |
| $tsTag | *integer* | optional: the tag of a previously constructed TimeSeries. |
| $nodes | *list integer* | optional: tags of nodes whose response is being recorded |
| $startNode | *integer* | optional: tag for start node |
| $startNode | *integer* | optional: tag for end node |
| $regionTag | *integer* | optional: tag of previously defined region. |
| $dofs | *list integer* | list of dof at nodes whose response is requested. |
| $respType | *string* | a string indicating response required. |

Note

1. Only one of the options **-file**, **-xml**, **-binary**, or **-tcp** may be used. The option specifies where the data is going to be sent.
2. Similarly only one of the options: **-node**, **-nodeRange**, or **-region** may be used. This option specifies the node tags.
3. The valid strings for respType are:

```
disp
vel
accel
incrDisp
eigen $mode
reaction
rayleighForces!
```

1. The function returns a value:

  SUCCESS: **>0** an integer tag that can be used as a handle on the recorder for the remove a recorder in the remove.

  FAILURE: **-1** recorder command failed (read the log)

To remove a recorder using the remove you need to save this tag in a variable for use later in the script.

1. $deltaT specifies a time interval for recording. will record when next step is $deltaT greater than last recorder step. It is useful if user script subdivides time step and user is not interested in the responses at each time step due to memory or file size constraints.
2. If the **-timeSeries** option is being used, the recorded results are those obtained from the time series for the current time added to the response quantity measures. Need as many time series tags as dof specified. Useful for obtaining for example total acceleration as opposed to relative if user using UniformAcceleration to impose a ground motion.
3. The -closeOnWrite option will slow the program down. It is useful if you want to see just exactly where the application is, as files are only written to disk when the operating system feels like it under typical operation.

Example:

The following examples demonstrate the use of the recorder Node command.

1. The first recorder will output to a file `nodesD.out` the displacements in **x** and **y** (**1** and **2**) directions at nodes **1**, **2**, **3**, and **4**. The output file will contain **9** columns (time, displacement in x and y at node 1, disp. in x and y at node 2, … , disp. x and y at node 4))
2. The second recorder will output to a file `nodesA.out` the total accelerations in **x** and **y** (**1** and **2**) directions at nodes **1**, **2**, **3**, and **4**. The output file will contain **9** columns (time, accel. in x and y at node 1, accel. in x and y at node 2, … , accel. in x and y at node 4)). The accelerations output will be the accelerations stored at the nodes added to the values obtained from the time series. The **x** values are the accelerations in **x** direction at node plus values from timeSeries **1**, the **y** values are the accelerations in **y** direction at nodes plus the values from timeSries **2**.

```
recorder Node -file nodesD.out -time -node 1 2 3 4 -dof 1 2 disp;

recorder Node -file nodesA.out -timeSeries 1 2 -time -node 1 2 3 4 -dof 1 2 accel;
```

Code developed by: **fmk**
