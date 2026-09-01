<!-- chunk_id: MomentCurvature_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/MomentCurvature.html",
 "title": "14.1.4. Moment Curvature Analysis",
 "category": "analysis",
 "command": "MomentCurvature",
 "doc_section": "src",
 "rel_path": "src/MomentCurvature.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4295,
 "word_count": 532,
 "has_code": true,
 "has_table": false
} -->

## 14.1.4. Moment Curvature Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c0562c43b8572e30cc9cb265136e7bf3/MomentCurvature.py).
2. Run the source code in your favorite Python program and should see results below

```
Start MomentCurvature.py example
Estimated yield curvature:  0.000126984126984127
Passed!
==========================
```

```
  1from openseespy.opensees import *
  2
  3def MomentCurvature(secTag, axialLoad, maxK, numIncr=100):
  4
  5    # Define two nodes at (0,0)
  6    node(1, 0.0, 0.0)
  7    node(2, 0.0, 0.0)
  8
  9    # Fix all degrees of freedom except axial and bending
 10    fix(1, 1, 1, 1)
 11    fix(2, 0, 1, 0)
 12
 13    # Define element
 14    #                             tag ndI ndJ  secTag
 15    element('zeroLengthSection',  1,   1,   2,  secTag)
 16
 17    # Define constant axial load
 18    timeSeries('Constant', 1)
 19    pattern('Plain', 1, 1)
 20    load(2, axialLoad, 0.0, 0.0)
 21
 22    # Define analysis parameters
 23    integrator('LoadControl', 0.0)
 24    system('SparseGeneral', '-piv')
 25    test('NormUnbalance', 1e-9, 10)
 26    numberer('Plain')
 27    constraints('Plain')
 28    algorithm('Newton')
 29    analysis('Static')
 30
 31    # Do one analysis for constant axial load
 32    analyze(1)
 33
 34    # Define reference moment
 35    timeSeries('Linear', 2)
 36    pattern('Plain',2, 2)
 37    load(2, 0.0, 0.0, 1.0)
 38
 39    # Compute curvature increment
 40    dK = maxK / numIncr
 41
 42    # Use displacement control at node 2 for section analysis
 43    integrator('DisplacementControl', 2,3,dK,1,dK,dK)
 44
 45    # Do the section analysis
 46    analyze(numIncr)
 47
 48
 49wipe()
 50print("Start MomentCurvature.py example")
 51
 52# Define model builder
 53# --------------------
 54model('basic','-ndm',2,'-ndf',3)
 55
 56# Define materials for nonlinear columns
 57# ------------------------------------------
 58# CONCRETE                  tag   f'c        ec0   f'cu        ecu
 59# Core concrete (confined)
 60uniaxialMaterial('Concrete01',1, -6.0,  -0.004,  -5.0,  -0.014)
 61
 62# Cover concrete (unconfined)
 63uniaxialMaterial('Concrete01',2, -5.0,  -0.002,  0.0,  -0.006)
 64
 65# STEEL
 66# Reinforcing steel
 67fy = 60.0      # Yield stress
 68E = 30000.0    # Young's modulus
 69
 70#                        tag  fy E0    b
 71uniaxialMaterial('Steel01', 3, fy, E, 0.01)
 72
 73# Define cross-section for nonlinear columns
 74# ------------------------------------------
 75
 76# set some paramaters
 77colWidth = 15
 78colDepth = 24
 79
 80cover = 1.5
 81As = 0.60;     # area of no. 7 bars
 82
 83# some variables derived from the parameters
 84y1 = colDepth/2.0
 85z1 = colWidth/2.0
 86
 87
 88section('Fiber', 1)
 89
 90# Create the concrete core fibers
 91patch('rect',1,10,1 ,cover-y1, cover-z1, y1-cover, z1-cover)
 92
 93# Create the concrete cover fibers (top, bottom, left, right)
 94patch('rect',2,10,1 ,-y1, z1-cover, y1, z1)
 95patch('rect',2,10,1 ,-y1, -z1, y1, cover-z1)
 96patch('rect',2,2,1 ,-y1, cover-z1, cover-y1, z1-cover)
 97patch('rect',2,2,1 ,y1-cover, cover-z1, y1, z1-cover)
 98
 99# Create the reinforcing fibers (left, middle, right)
100layer('straight', 3, 3, As, y1-cover, z1-cover, y1-cover, cover-z1)
101layer('straight', 3, 2, As, 0.0     , z1-cover, 0.0      , cover-z1)
102layer('straight', 3, 3, As, cover-y1, z1-cover, cover-y1, cover-z1)
103
104# Estimate yield curvature
105# (Assuming no axial load and only top and bottom steel)
106# d -- from cover to rebar
107d = colDepth-cover
108# steel yield strain
109epsy = fy/E
110Ky = epsy/(0.7*d)
111
112# Print estimate to standard output
113print("Estimated yield curvature: ", Ky)
114
115# Set axial load
116P = -180.0
117
118# Target ductility for analysis
119mu = 15.0
120
121# Number of analysis increments
122numIncr = 100
123
124# Call the section analysis procedure
125MomentCurvature(1, P, Ky*mu, numIncr)
126
127results = open('results.out','a+')
128
129u = nodeDisp(2,3)
130if abs(u-0.00190476190476190541)<1e-12:
131    results.write('PASSED : MomentCurvature.py\n');
132    print("Passed!")
133else:
134    results.write('FAILED : MomentCurvature.py\n');
135    print("Failed!")
136
137results.close()
138
139print("==========================")
```
