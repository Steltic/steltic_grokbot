<!-- chunk_id: nonlinearTruss_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/nonlinearTruss.html",
 "title": "14.1.2. Nonlinear Truss Analysis",
 "category": "analysis",
 "command": "nonlinearTruss",
 "doc_section": "src",
 "rel_path": "src/nonlinearTruss.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2197,
 "word_count": 264,
 "has_code": true,
 "has_table": false
} -->

## 14.1.2. Nonlinear Truss Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/0c20eb7d761b60e0696e00aa57510e17/NonlinearTruss.py).
2. Make sure the [numpy](http://www.numpy.org/) and [matplotlib](https://matplotlib.org/) packages are installed in your Python distribution.
3. Run the source code in your favorite Python program and should see

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
10# set modelbuilder
11wipe()
12model('basic', '-ndm', 2, '-ndf', 2)
13
14# variables
15A = 4.0
16E = 29000.0
17alpha = 0.05
18sY = 36.0
19udisp = 2.5
20Nsteps = 1000
21Px = 160.0
22Py = 0.0
23
24# create nodes
25node(1, 0.0, 0.0)
26node(2, 72.0, 0.0)
27node(3, 168.0, 0.0)
28node(4, 48.0, 144.0)
29
30# set boundary condition
31fix(1, 1, 1)
32fix(2, 1, 1)
33fix(3, 1, 1)
34
35# define materials
36uniaxialMaterial("Hardening", 1, E, sY, 0.0, alpha/(1-alpha)*E)
37
38# define elements
39element("Truss",1,1,4,A,1)
40element("Truss",2,2,4,A,1)
41element("Truss",3,3,4,A,1)
42
43# create TimeSeries
44timeSeries("Linear", 1)
45
46# create a plain load pattern
47pattern("Plain", 1, 1)
48
49# Create the nodal load
50load(4, Px, Py)
51
52# ------------------------------
53# Start of analysis generation
54# ------------------------------
55
56# create SOE
57system("ProfileSPD")
58
59# create DOF number
60numberer("Plain")
61
62# create constraint handler
63constraints("Plain")
64
65# create integrator
66integrator("LoadControl", 1.0/Nsteps)
67
68# create algorithm
69algorithm("Newton")
70
71# create test
72test('NormUnbalance',1e-8, 10)
73
74# create analysis object
75analysis("Static")
76
77# ------------------------------
78# Finally perform the analysis
79# ------------------------------
80
81# perform the analysis
82data = np.zeros((Nsteps+1,2))
83for j in range(Nsteps):
84    analyze(1)
85    data[j+1,0] = nodeDisp(4,1)
86    data[j+1,1] = getLoadFactor(1)*Px
87
88plt.plot(data[:,0], data[:,1])
89plt.xlabel('Horizontal Displacement')
90plt.ylabel('Horizontal Load')
91plt.show()
92
```
