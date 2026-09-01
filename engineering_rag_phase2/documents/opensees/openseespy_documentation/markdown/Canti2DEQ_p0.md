<!-- chunk_id: Canti2DEQ_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Canti2DEQ.html",
 "title": "14.2.1. Cantilever 2D EQ ground motion with gravity Analysis",
 "category": "analysis",
 "command": "Canti2DEQ",
 "doc_section": "src",
 "rel_path": "src/Canti2DEQ.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4633,
 "word_count": 546,
 "has_code": true,
 "has_table": false
} -->

## 14.2.1. Cantilever 2D EQ ground motion with gravity Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/8081ec8b17600a21a98aa0cb4f9e86f8/Canti2DEQ.py).
2. The ground motion data file [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/be63293bb5508d09e1d21deb15d6851c/A10000.dat) must be put in the same folder.
3. Run the source code in your favorate Python program and should see results below

```
=========================================================
Start cantilever 2D EQ ground motion with gravity example
u2 =  -0.07441860465116278
Passed!
=========================================
```

```
 1print("=========================================================")
 2print("Start cantilever 2D EQ ground motion with gravity example")
 3
 4from openseespy.opensees import *
 5
 6
 7# --------------------------------------------------------------------------------------------------
 8# Example 1. cantilever 2D
 9# EQ ground motion with gravity
10# all units are in kip, inch, second
11# elasticBeamColumn ELEMENT
12#		Silvia Mazzoni & Frank McKenna, 2006
13#
14#    ^Y
15#    |
16#    2       __
17#    |         |
18#    |         |
19#    |         |
20#  (1)      36'
21#    |         |
22#    |         |
23#    |         |
24#  =1=    ----  -------->X
25#
26
27# SET UP ----------------------------------------------------------------------------
28wipe()						       # clear opensees model
29model('basic', '-ndm', 2, '-ndf', 3)	       # 2 dimensions, 3 dof per node
30# file mkdir data 				   # create data directory
31
32# define GEOMETRY -------------------------------------------------------------
33# nodal coordinates:
34node(1, 0., 0.)					   # node#, X Y
35node(2, 0., 432.)
36
37# Single point constraints -- Boundary Conditions
38fix(1, 1, 1, 1) 			           # node DX DY RZ
39
40# nodal masses:
41mass(2, 5.18, 0., 0.)			   # node#, Mx My Mz, Mass=Weight/g.
42
43# Define ELEMENTS -------------------------------------------------------------
44# define geometric transformation: performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system
45geomTransf('Linear', 1)  		       # associate a tag to transformation
46
47# connectivity:
48element('elasticBeamColumn', 1, 1, 2, 3600.0, 3225.0,1080000.0, 1)
49
50# define GRAVITY -------------------------------------------------------------
51timeSeries('Linear', 1)
52pattern('Plain', 1, 1,)
53load(2, 0., -2000., 0.)			    # node#, FX FY MZ --  superstructure-weight
54
55constraints('Plain')  				# how it handles boundary conditions
56numberer('Plain')			    # renumber dof's to minimize band-width (optimization), if you want to
57system('BandGeneral')		    # how to store and solve the system of equations in the analysis
58algorithm('Linear')                 # use Linear algorithm for linear analysis
59integrator('LoadControl', 0.1)			# determine the next time step for an analysis, # apply gravity in 10 steps
60analysis('Static')					    # define type of analysis static or transient
61analyze(10)					        # perform gravity analysis
62loadConst('-time', 0.0)				# hold gravity constant and restart time
63
64# DYNAMIC ground-motion analysis -------------------------------------------------------------
65# create load pattern
66G = 386.0
67timeSeries('Path', 2, '-dt', 0.005, '-filePath', 'A10000.dat', '-factor', G) # define acceleration vector from file (dt=0.005 is associated with the input file gm)
68pattern('UniformExcitation', 2, 1, '-accel', 2)		         # define where and how (pattern tag, dof) acceleration is applied
69
70# set damping based on first eigen mode
71freq = eigen('-fullGenLapack', 1)[0]**0.5
72dampRatio = 0.02
73rayleigh(0., 0., 0., 2*dampRatio/freq)
74
75# create the analysis
76wipeAnalysis()			     # clear previously-define analysis parameters
77constraints('Plain')    	 # how it handles boundary conditions
78numberer('Plain')    # renumber dof's to minimize band-width (optimization), if you want to
79system('BandGeneral') # how to store and solve the system of equations in the analysis
80algorithm('Linear')	 # use Linear algorithm for linear analysis
81integrator('Newmark', 0.5, 0.25)    # determine the next time step for an analysis
82analysis('Transient')   # define type of analysis: time-dependent
83analyze(3995, 0.01)	 # apply 3995 0.01-sec time steps in analysis
84
85u2 = nodeDisp(2, 2)
86print("u2 = ", u2)
87
88
89if abs(u2+0.07441860465116277579) < 1e-12:
90    print("Passed!")
91else:
92    print("Failed!")
93
94wipe()
95
96print("=========================================")
```
