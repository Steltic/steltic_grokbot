<!-- chunk_id: hello2_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/hello2.html",
 "title": "14.6.2. Hello World Example 2",
 "category": "examples",
 "command": "hello2",
 "doc_section": "src",
 "rel_path": "src/hello2.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1790,
 "word_count": 250,
 "has_code": true,
 "has_table": false
} -->

## 14.6.2. Hello World Example 2

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/2d2c1cd6ac3191b1e2f0b4f60b201913/hello2.py).
2. Run the source code with 4 processors

```
mpiexec -np 4 python hello2.py
```

the outputs look like

```
Random:
Hello from 2
Hello from 1
Hello from 3

Ordered:
Hello from 1
Hello from 2
Hello from 3

Broadcasting:
Hello from 0
Hello from 0
Hello from 0
Process 3 Terminating
Process 2 Terminating
Process 1 Terminating
Process 0 Terminating
```

The script is shown below

```
 1import openseespy.opensees as ops
 2
 3pid = ops.getPID()
 4np = ops.getNP()
 5
 6# datatype = 'float'
 7# datatype = 'int'
 8datatype = 'str'
 9
10if pid == 0:
11    print('Random: ')
12
13    for i in range(1, np):
14        data = ops.recv('-pid', 'ANY')
15        print(data)
16else:
17    if datatype == 'str':
18        ops.send('-pid', 0, 'Hello from {}'.format(pid))
19    elif datatype == 'float':
20        ops.send('-pid', 0, float(pid))
21    elif datatype == 'int':
22        ops.send('-pid', 0, int(pid))
23
24ops.barrier()
25
26if pid == 0:
27    print('\nOrdered: ')
28
29    for i in range(1, np):
30        data = ops.recv('-pid', i)
31        print(data)
32else:
33    if datatype == 'str':
34        ops.send('-pid', 0, 'Hello from {}'.format(pid))
35    elif datatype == 'float':
36        ops.send('-pid', 0, float(pid))
37    elif datatype == 'int':
38        ops.send('-pid', 0, int(pid))
39
40ops.barrier()
41if pid == 0:
42    print('\nBroadcasting: ')
43    if datatype == 'str':
44        ops.Bcast('Hello from {}'.format(pid))
45    elif datatype == 'float':
46        ops.Bcast(float(pid))
47    elif datatype == 'int':
48        ops.Bcast(int(pid))
49else:
50    data = ops.Bcast()
51    print(data)
```
