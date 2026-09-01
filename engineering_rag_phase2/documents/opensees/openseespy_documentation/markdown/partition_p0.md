<!-- chunk_id: partition_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/partition.html",
 "title": "11.9. partition command",
 "category": "general",
 "command": "partition",
 "doc_section": "src",
 "rel_path": "src/partition.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1035,
 "word_count": 125,
 "has_code": false,
 "has_table": true
} -->

## 11.9. partition command

**partition(*'-ncuts'*, *ncuts*, *'-niter'*, *niters*, *'-ufactor'*, *ufactor*, *'-info'*)**

In a parallel environment, this command partitions the model. It requires that all processors
have the exact same model to be partitioned.

| `ncuts` ([int](https://docs.python.org/3/library/functions.html#int)) | Specifies the number of different partitionings that it will compute. The final partitioning is the one that achieves the best edge cut or communication volume. (Optional default is 1). |
| --- | --- |
| `niters` ([int](https://docs.python.org/3/library/functions.html#int)) | Specifies the number of iterations for the refinement algorithms at each stage of the uncoarsening process. (Optional default is 10). |
| `ufactor` ([int](https://docs.python.org/3/library/functions.html#int)) | Specifies the maximum allowed load imbalance among the partitions. (Optional default is 30, indicating a load imbalance of 1.03). |
| `'-info'` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | print information. (optional) |
