<!-- chunk_id: parallelcmds_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/parallelcmds.html",
 "title": "11. Parallel Commands",
 "category": "general",
 "command": "parallelcmds",
 "doc_section": "src",
 "rel_path": "src/parallelcmds.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2156,
 "word_count": 184,
 "has_code": true,
 "has_table": false
} -->

## 11. Parallel Commands

The parallel commands are currently only
working in the Linux version.
The parallel OpenSeesPy is similar to OpenSeesMP, which
requires users to divide the model
to distributed processors.

You can still run the single-processor version as before.
To run the parallel version, you have
to install a MPI implementation, such as [mpich](https://www.mpich.org/downloads/). Then
call your python scripts in the command line

```
mpiexec -np np python filename.py
```

where `np` is the number of processors to be used,
`python` is the python interpreter, and
`filename.py` is the script name.

Inside the script, OpenSeesPy is still imported as

```
import openseespy.opensees as ops
```

Common problems:

1. Unmatch send/recv will cause deadlock.
2. Writing to the same files at the same from different processors will cause race conditions.
3. Poor model decomposition will cause load imbalance problem.

Following are commands related to parallel computing:

1. [getPID command](https://openseespydoc.readthedocs.io/en/latest/src/getPID.html)
2. [getNP command](https://openseespydoc.readthedocs.io/en/latest/src/getNP.html)
3. [barrier command](https://openseespydoc.readthedocs.io/en/latest/src/barrier.html)
4. [send command](https://openseespydoc.readthedocs.io/en/latest/src/send.html)
5. [recv command](https://openseespydoc.readthedocs.io/en/latest/src/recv.html)
6. [Bcast command](https://openseespydoc.readthedocs.io/en/latest/src/Bcast.html)
7. [setStartNodeTag command](https://openseespydoc.readthedocs.io/en/latest/src/setStartNodeTag.html)
8. [domainChange command](https://openseespydoc.readthedocs.io/en/latest/src/domainChange.html)
9. [Parallel Plain Numberer](https://openseespydoc.readthedocs.io/en/latest/src/ParallelPlainNumberer.html)
10. [Parallel RCM Numberer](https://openseespydoc.readthedocs.io/en/latest/src/ParallelRCMNumberer.html)
11. [MUMPS Solver](https://openseespydoc.readthedocs.io/en/latest/src/Mumps.html)
12. [Parallel DisplacementControl](https://openseespydoc.readthedocs.io/en/latest/src/ParallelDisplacementControl.html)
13. [partition command](https://openseespydoc.readthedocs.io/en/latest/src/partition.html)
