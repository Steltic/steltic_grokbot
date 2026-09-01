<!-- chunk_id: hello_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/hello.html",
 "title": "14.6.1. Hello World Example 1",
 "category": "examples",
 "command": "hello",
 "doc_section": "src",
 "rel_path": "src/hello.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 700,
 "word_count": 100,
 "has_code": true,
 "has_table": false
} -->

## 14.6.1. Hello World Example 1

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c376f4ce826e7f03135e58afa32fdb9f/hello.py).
2. Run the source code with 4 processors

```
mpiexec -np 4 python hello.py
```

the outputs look like

```
Hello World Process: 1
Hello World Process: 2
Hello World Process: 0
Total number of processes: 4
Hello World Process: 3
Process 1 Terminating
Process 2 Terminating
Process 0 Terminating
Process 3 Terminating
```

The script is shown below

```
1import openseespy.opensees as ops
2
3pid = ops.getPID()
4np = ops.getNP()
5
6print('Hello World Process:', pid)
7if pid == 0:
8    print('Total number of processes:', np)
9
```
