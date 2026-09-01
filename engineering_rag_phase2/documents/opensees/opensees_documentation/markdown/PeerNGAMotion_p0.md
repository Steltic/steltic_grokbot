<!-- chunk_id: PeerNGAMotion_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/PeerNGAMotion.html",
 "title": "3.1.11.10. PeerNGAMotion TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "PeerNGAMotion",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/PeerNGAMotion.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1667,
 "word_count": 282,
 "has_code": true,
 "has_table": true
} -->

## 3.1.11.10. PeerNGAMotion TimeSeries

This command is used to construct a TimeSeries object which, similar to a Path TimeSeries, the load factor obtained is dependent on a series of points obtained from a file. The difference is that the file is obtained from the [Peer NGA strong motion database](https://peer.berkeley.edu/research/databases) using an internet connection.

**timeSeries PeerNGAMotion $tag $eqMotion $factor <-dT $dT> <-NPTS $nPts>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | unique tag among TimeSeries objects |
| $eqMotion | *string* | the PEER NGA name of the motion (a string containing the earthquake name, station & dirn) |
| $factor | *float* | factor to be applied to the data points, if accel record type you want to specify G |
| $dT | *float* | optional, if provided will set the variable nPts equal to number of data points found in record |
| $nPts | *integer* | optional, if provided will set the variable dT equal to time interval between points in the record |

Note

- If the time in the domain does not match a data point in record, linear interpolation is performed between nearest points in record.
- The command can be used with the results obtained from the searchPeerNGA command (hence the craziness of the $eqMotion names).
- An internet connection is required to run command.

Example:

To create 2 time series for two horizontal motions recorded for the Borrego Mtn 1968-04-09 earthquake recorded at the USGS 117 El Centro Array #9 station

1. **Tcl Code**

```
timeSeries PeerNGAMotion 1 /BORREGO/A-ELC180 $G -dT dt -NPTS nPts
timeSeries PeerNGAMotion 2 /BORREGO/A-ELC270 $G
```

1. **Python Code**

Code Developed by: **fmk**
