<!-- chunk_id: InitialStateAnalysisWrapper_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/InitialStateAnalysisWrapper.html",
 "title": "4.15.5.1. InitialStateAnalysisWrapper",
 "category": "analysis",
 "command": "InitialStateAnalysisWrapper",
 "doc_section": "src",
 "rel_path": "src/InitialStateAnalysisWrapper.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1397,
 "word_count": 178,
 "has_code": false,
 "has_table": true
} -->

## 4.15.5.1. InitialStateAnalysisWrapper

**nDMaterial(*'InitialStateAnalysisWrapper'*, *matTag*, *nDMatTag*, *nDim*)**

The InitialStateAnalysisWrapper nDMaterial allows for the use of the InitialStateAnalysis command for setting initial conditions. The InitialStateAnalysisWrapper can be used with any nDMaterial. This material wrapper allows for the development of an initial stress field while maintaining the original geometry of the problem. An example analysis is provided below to demonstrate the use of this material wrapper object.

| `matTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying material |
| --- | --- |
| `nDMatTag` ([int](https://docs.python.org/3/library/functions.html#int)) | the tag of the associated nDMaterial object |
| `nDim` ([int](https://docs.python.org/3/library/functions.html#int)) | number of dimensions (2 for 2D, 3 for 3D) |

Note

1. There are no valid recorder queries for the InitialStateAnalysisWrapper.
2. The InitialStateAnalysis off command removes all previously defined recorders. Two sets of recorders are needed if the results before and after this command are desired. See the example below for more.
3. The InitialStateAnalysisWrapper material is somewhat tricky to use in dynamic analysis. Sometimes setting the displacement to zero appears to be interpreted as an initial displacement in subsequent steps, resulting in undesirable vibrations.
