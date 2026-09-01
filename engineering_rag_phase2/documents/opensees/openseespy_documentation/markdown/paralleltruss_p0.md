<!-- chunk_id: paralleltruss_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/paralleltruss.html",
 "title": "14.6.3. Parallel Truss Example",
 "category": "examples",
 "command": "paralleltruss",
 "doc_section": "src",
 "rel_path": "src/paralleltruss.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2015,
 "word_count": 230,
 "has_code": true,
 "has_table": false
} -->

## 14.6.3. Parallel Truss Example

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/e49e0dcfecd70d3ef1749279112ac52e/paralleltruss.py).
2. Run the source code with 2 processors

```
mpiexec -np 2 python paralleltruss.py
```

the outputs look like

```
Node 4:  [[72.0, 96.0], [0.5300927771322836, -0.17789363846931772]]
Node 4:  [[72.0, 96.0], [0.5300927771322836, -0.17789363846931772]]
Node 4:  [[72.0, 96.0], [1.530092777132284, -0.19400676316761836]]
Node 4:  [[72.0, 96.0], [1.530092777132284, -0.19400676316761836]]
opensees.msg: TIME(sec) Real: 0.208238

opensees.msg: TIME(sec) Real: 0.209045

Process 0 Terminating
Process 1 Terminating
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
10ops.uniaxialMaterial('Elastic', 1, 3000.0)
11
12if pid == 0:
13    ops.node(1, 0.0, 0.0)
14    ops.node(4, 72.0, 96.0)
15
16    ops.fix(1, 1, 1)
17
18    ops.element('Truss', 1, 1, 4, 10.0, 1)
19    ops.timeSeries('Linear', 1)
20    ops.pattern('Plain', 1, 1)
21    ops.load(4, 100.0, -50.0)
22
23else:
24    ops.node(2, 144.0, 0.0)
25    ops.node(3, 168.0, 0.0)
26    ops.node(4, 72.0, 96.0)
27
28    ops.fix(2, 1, 1)
29    ops.fix(3, 1, 1)
30
31    ops.element('Truss', 2, 2, 4, 5.0, 1)
32    ops.element('Truss', 3, 3, 4, 5.0, 1)
33
34ops.constraints('Transformation')
35ops.numberer('ParallelPlain')
36ops.system('Mumps')
37ops.test('NormDispIncr', 1e-6, 6, 2)
38ops.algorithm('Newton')
39ops.integrator('LoadControl', 0.1)
40ops.analysis('Static')
41
42ops.analyze(10)
43
44print('Node 4: ', [ops.nodeCoord(4), ops.nodeDisp(4)])
45
46ops.loadConst('-time', 0.0)
47
48if pid == 0:
49    ops.pattern('Plain', 2, 1)
50    ops.load(4, 1.0, 0.0)
51
52ops.domainChange()
53ops.integrator('ParallelDisplacementControl', 4, 1, 0.1)
54ops.analyze(10)
55
56print('Node 4: ', [ops.nodeCoord(4), ops.nodeDisp(4)])
57ops.stop()
```
