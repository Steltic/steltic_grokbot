<!-- chunk_id: pathTimeSeries_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/timeseries/pathTimeSeries.html",
 "title": "3.1.11.8. Path TimeSeries",
 "category": "command_manual",
 "manual_group": "model",
 "command": "pathTimeSeries",
 "doc_section": "user/manual/model/timeseries",
 "rel_path": "user/manual/model/timeseries/pathTimeSeries.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1415,
 "word_count": 220,
 "has_code": false,
 "has_table": false
} -->

## 3.1.11.8. Path TimeSeries

This command is used to construct a Path TimeSeries object. The relationship between load factor and time is input by the user as a series of discrete points in the 2d space (load factor, time). The input points can come from a file or from a list in the script. When the time specified does not match any of the input points, linear interpolation is used between points. There are many ways to specify the load path:

For a load path where the factors are specified in a tcl list with a constant time interval between points:

**timeSeries Path $tag -dt $dt -values {list_of_values} <-factor $cFactor> <-useLast> <-prependZero> <-startTime $tStart>**

For a load path where the factors are specified in a file for a constant time interval between points:

**timeSeries Path $tag -dt $dt -filePath $filePath <-factor $cFactor> <-useLast> <-prependZero> <-startTime $tStart>**

For a load path where the values are specified at non-constant time intervals:

**timeSeries Path $tag -time {list_of_times} -values {list_of_values} <-factor $cFactor> <-useLast>**

For a load path where both time and values are specified in a list included in the command

**timeSeries Path $tag -fileTime $fileTime -filePath $filePath <-factor $cFactor> <-useLast>**

EXAMPLE:

timeSeries Path 1 -dt 0.02 -filePath A-ELC270.AT2 -factor $G

timeSeries Path 2 -time {0.0 0.2 0.4 1.0} -values {0.0 1.0 2.0 0.0}

Code developed by: **fmk**
