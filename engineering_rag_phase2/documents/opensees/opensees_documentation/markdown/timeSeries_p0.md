<!-- chunk_id: timeSeries_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeSeries.html",
 "title": "3.1.11. Time Series Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "timeSeries",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/timeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2012,
 "word_count": 161,
 "has_code": false,
 "has_table": true
} -->

## 3.1.11. Time Series Command

This command is used to construct a TimeSeries object which represents the relationship between the time in the domain, \(t\), and the load factor applied to the loads, \(\lambda\), in the load pattern with which the TimeSeries object is associated, i.e. \(\lambda = F(t)\).

**timeSeries $type $tag $arg1 ...**

| Argument | Type | Description |
| --- | --- | --- |
| $type | *string* | type of time series |
| $tag | *integer* | unique time series tag. |
| $args | *list* | a list of arguments with args depending on type |

The following subsections contain information about **$type** and the number of nodes and args required for each of the available element types:

- [3.1.11.1. Constant TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/constantTimeSeries.html)
- [3.1.11.2. Linear TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/linearTimeSeries.html)
- [3.1.11.3. Trig TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/trigTimeSeries.html)
- [3.1.11.4. Ramp TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/RampTimeSeries.html)
- [3.1.11.5. Triangular TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/triangleTimeSeries.html)
- [3.1.11.6. Rectangular Time Series](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/rectangularTimeSeries.html)
- [3.1.11.7. Pulse TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/pulseTimeSeries.html)
- [3.1.11.8. Path TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/pathTimeSeries.html)
- [3.1.11.9. PeerMotion TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/peerMotion.html)
- [3.1.11.10. PeerNGAMotion TimeSeries](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/PeerNGAMotion.html)
