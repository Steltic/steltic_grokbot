<!-- chunk_id: truss_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/truss.html",
 "title": "14.1.1. Elastic Truss Analysis",
 "category": "analysis",
 "command": "truss",
 "doc_section": "src",
 "rel_path": "src/truss.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1767,
 "word_count": 210,
 "has_code": true,
 "has_table": false
} -->

## 14.1.1. Elastic Truss Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/ce7e03cd0f3959f5f6412cdbdd0f1ff5/ElasticTruss.py).
2. Run the source code in your favorite Python program and should see `Passed!` in the results.

```
 1from openseespy.opensees import *
 2
 3import numpy as np
 4import matplotlib.pyplot as plt
 5
 6# ------------------------------
 7# Start of model generation
 8# -----------------------------
 9
10# remove existing model
11wipe()
12
13# set modelbuilder
14model('basic', '-ndm', 2, '-ndf', 2)
15
16# create nodes
17node(1, 0.0, 0.0)
18node(2, 144.0,  0.0)
19node(3, 168.0,  0.0)
20node(4,  72.0, 96.0)
21
22# set boundary condition
23fix(1, 1, 1)
24fix(2, 1, 1)
25fix(3, 1, 1)
26
27# define materials
28uniaxialMaterial("Elastic", 1, 3000.0)
29
30# define elements
31element("Truss",1,1,4,10.0,1)
32element("Truss",2,2,4,5.0,1)
33element("Truss",3,3,4,5.0,1)
34
35# create TimeSeries
36timeSeries("Linear", 1)
37
38# create a plain load pattern
39pattern("Plain", 1, 1)
40
41# Create the nodal load - command: load nodeID xForce yForce
42load(4, 100.0, -50.0)
43
44# ------------------------------
45# Start of analysis generation
46# ------------------------------
47
48# create SOE
49system("BandSPD")
50
51# create DOF number
52numberer("RCM")
53
54# create constraint handler
55constraints("Plain")
56
57# create integrator
58integrator("LoadControl", 1.0)
59
60# create algorithm
61algorithm("Linear")
62
63# create analysis object
64analysis("Static")
65
66# perform the analysis
67analyze(1)
68
69ux = nodeDisp(4,1)
70uy = nodeDisp(4,2)
71if abs(ux-0.53009277713228375450)<1e-12 and abs(uy+0.17789363846931768864)<1e-12:
72    print("Passed!")
73else:
74    print("Failed!")
```
