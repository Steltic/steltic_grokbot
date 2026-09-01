<!-- chunk_id: paralleltri31_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/paralleltri31.html",
 "title": "14.6.4. Parallel Tri31 Example",
 "category": "examples",
 "command": "paralleltri31",
 "doc_section": "src",
 "rel_path": "src/paralleltri31.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2433,
 "word_count": 358,
 "has_code": true,
 "has_table": false
} -->

## 14.6.4. Parallel Tri31 Example

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/a6b8a0d9b194acb742724e2fa6d01805/paralleltri31.py).
2. Run the source code with 4 processors

```
mpiexec -np 4 python paralleltri31.py
```

the outputs look like

```
opensees.msg: TIME(sec) Real: 0.177647

opensees.msg: TIME(sec) Real: 0.187682

opensees.msg: TIME(sec) Real: 0.193193

opensees.msg: TIME(sec) Real: 0.19473

opensees.msg: TIME(sec) Real: 14.4652

Node 4 [-0.16838893553441528, -2.88399389660282]

opensees.msg: TIME(sec) Real: 14.4618

opensees.msg: TIME(sec) Real: 14.4619

opensees.msg: TIME(sec) Real: 14.4948

Process 0 Terminating
Process 1 Terminating
Process 2 Terminating
Process 3 Terminating
```

The script is shown below

```
 1import openseespy.opensees as ops
 2
 3pid = ops.getPID()
 4np = ops.getNP()
 5ops.start()
 6
 7ops.model('basic', '-ndm', 2, '-ndf', 2)
 8
 9L = 48.0
10H = 4.0
11
12Lp = L / np
13ndf = 2
14meshsize = 0.05
15
16ops.node(pid, Lp * pid, 0.0)
17ops.node(pid + 1, Lp * (pid + 1), 0.0)
18ops.node(np + pid + 2, Lp * (pid + 1), H)
19ops.node(np + pid + 1, Lp * pid, H)
20
21sid = 1
22ops.setStartNodeTag(2 * np + 2 + pid * int(H / meshsize + 10))
23ops.mesh('line', 3, 2, pid, np + pid + 1, sid, ndf, meshsize)
24ops.setStartNodeTag(2 * np + 2 + (pid + 1) * int(H / meshsize + 10))
25ops.mesh('line', 4, 2, pid + 1, np + pid + 2, sid, ndf, meshsize)
26
27ops.setStartNodeTag(int(2 * L / meshsize + (np + 1) * H / meshsize * 2) +
28                    pid * int(H * L / meshsize ** 2 * 2))
29ops.mesh('line', 1, 2, pid, pid + 1, sid, ndf, meshsize)
30ops.mesh('line', 2, 2, np + pid + 1, np + pid + 2, sid, ndf, meshsize)
31
32ops.nDMaterial('ElasticIsotropic', 1, 3000.0, 0.3)
33
34eleArgs = ['tri31', 1.0, 'PlaneStress', 1]
35
36ops.mesh('quad', 5, 4, 1, 4, 2, 3, sid, ndf, meshsize, *eleArgs)
37
38
39if pid == 0:
40    ops.fix(pid, 1, 1)
41    ops.fix(np+pid+1, 1, 1)
42if pid == np-1:
43    ops.timeSeries('Linear', 1)
44    ops.pattern('Plain', 1, 1)
45    ops.load(np + pid + 2, 0.0, -1.0)
46
47
48ops.constraints('Transformation')
49ops.numberer('ParallelPlain')
50ops.system('Mumps')
51ops.test('NormDispIncr', 1e-6, 6)
52ops.algorithm('Newton')
53ops.integrator('LoadControl', 1.0)
54ops.analysis('Static')
55
56ops.stop()
57ops.start()
58ops.analyze(1)
59
60if pid == np-1:
61    print('Node', pid+1, ops.nodeDisp(pid+1))
62
63
64ops.stop()
```
