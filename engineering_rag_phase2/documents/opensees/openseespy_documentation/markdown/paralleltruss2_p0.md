<!-- chunk_id: paralleltruss2_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/paralleltruss2.html",
 "title": "14.6.5. Parallel Parametric Study Example",
 "category": "examples",
 "command": "paralleltruss2",
 "doc_section": "src",
 "rel_path": "src/paralleltruss2.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1684,
 "word_count": 218,
 "has_code": true,
 "has_table": false
} -->

## 14.6.5. Parallel Parametric Study Example

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c2834e7774110d9078895a541b28adfc/paralleltruss2.py).
2. Run the source code with 2 processors

```
mpiexec -np 2 python paralleltruss2.py
```

the outputs look like

```
Processor 0
Node 4 (E = 3000.0 ) Disp : [0.5300927771322836, -0.17789363846931766]
Processor 1

Node 4 (E = 6000.0 ) Disp : [0.2650463885661418, -0.08894681923465883]

Process 1 Terminating
Process 0 Terminating
```

The script is shown below

```
 1import openseespy.opensees as ops
 2
 3pid = ops.getPID()
 4np = ops.getNP()
 5ops.start()
 6if np != 2:
 7    exit()
 8
 9ops.model('basic', '-ndm', 2, '-ndf', 2)
10
11if pid == 0:
12    E = 3000.0
13else:
14    E = 6000.0
15
16ops.uniaxialMaterial('Elastic', 1, E)
17
18ops.node(1, 0.0, 0.0)
19ops.node(2, 144.0, 0.0)
20ops.node(3, 168.0, 0.0)
21ops.node(4, 72.0, 96.0)
22
23ops.fix(1, 1, 1)
24ops.fix(2, 1, 1)
25ops.fix(3, 1, 1)
26
27ops.element('Truss', 1, 1, 4, 10.0, 1)
28ops.timeSeries('Linear', 1)
29ops.pattern('Plain', 1, 1)
30ops.load(4, 100.0, -50.0)
31
32ops.element('Truss', 2, 2, 4, 5.0, 1)
33ops.element('Truss', 3, 3, 4, 5.0, 1)
34
35ops.constraints('Transformation')
36ops.numberer('ParallelPlain')
37ops.system('Umfpack')
38ops.test('NormDispIncr', 1e-6, 6)
39ops.algorithm('Newton')
40ops.integrator('LoadControl', 0.1)
41ops.analysis('Static')
42
43ops.analyze(10)
44
45
46if pid == 0:
47    print('Processor 0')
48    print('Node 4 (E =', E, ') Disp :', ops.nodeDisp(4))
49
50ops.barrier()
51
52if pid == 1:
53    print('Processor 1')
54    print('Node 4 (E =', E, ') Disp :', ops.nodeDisp(4))
55
56
57ops.stop()
```
