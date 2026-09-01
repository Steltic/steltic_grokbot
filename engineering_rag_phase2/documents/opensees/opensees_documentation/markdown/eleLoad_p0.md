<!-- chunk_id: eleLoad_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/PlainPatternloadcommands/eleLoad.html",
 "title": "3.1.12.1.2. eleLoad Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "eleLoad",
 "doc_section": "user/manual/model/pattern/PlainPatternloadcommands",
 "rel_path": "user/manual/model/pattern/PlainPatternloadcommands/eleLoad.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1998,
 "word_count": 345,
 "has_code": true,
 "has_table": true
} -->

## 3.1.12.1.2. eleLoad Command

The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

**eleLoad $eleLoad $arg1 $arg2 $arg3 ....**

The beam column elements all accept eleLoad commands of the following form:

```
eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy <$Wx>
```

```
eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $xL <$Px>
```

When NDM=3, the beam column elements all accept eleLoad commands of the following form:

```
eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy $Wz <$Wx>
```

```
eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $Pz $xL <$Px>
```

| Argument | Type | Description |
| --- | --- | --- |
| $eleTags | *list integer* | tags of PREVIOUSLY DEFINED element |
| $Wx | *float* | mag of uniformily distributed ref load acting in direction along member length |
| $Wy | *float* | mag of uniformily distributed ref load acting in local y direction of element |
| $Wz | *float* | mag of uniformily distributed ref load acting in local z direction of element |
| $Py | *float* | mag of ref point load acting in direction along member length |
| $Py | *float* | mag of ref point load acting in local y direction of element |
| $Pz | *float* | mag of ref point load acting in local z direction of element |
| $xL location of point load relative to node I | prescribed as fraction of element length |  |

Note

The load values are reference loads values, it is the time sereries that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.

Warning

At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.

```
set width 20.0
set W 4000.0;
timeSeries Linear 1
pattern Plain 1 1 {
    eleLoad -ele 3 -type -beamUniform [expr -$W/$width]
}
```

```
width = 20.0;
W = 4000.0;
timeSeries('Linear', 1)
pattern('Plain',1,1)
eleLoad('-ele',3, '-type', -beamUniform', W/width)
```

Code Developed by: **fmk**
