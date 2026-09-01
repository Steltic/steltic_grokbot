<!-- chunk_id: RCFrameGravity_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/RCFrameGravity.html",
 "title": "14.1.5. Reinforced Concrete Frame Gravity Analysis",
 "category": "analysis",
 "command": "RCFrameGravity",
 "doc_section": "src",
 "rel_path": "src/RCFrameGravity.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5479,
 "word_count": 768,
 "has_code": true,
 "has_table": false
} -->

## 14.1.5. Reinforced Concrete Frame Gravity Analysis

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c5216600efa55eb2f4414ae80ad646a5/RCFrameGravity.py).
2. Run the source code in your favorite Python program and should see `Passed!` in the results.

```
  1print("==========================")
  2
  3from openseespy.opensees import *
  4
  5print("Starting RCFrameGravity example")
  6
  7# Create ModelBuilder (with two-dimensions and 3 DOF/node)
  8model('basic', '-ndm', 2, '-ndf', 3)
  9
 10# Create nodes
 11# ------------
 12
 13# Set parameters for overall model geometry
 14width = 360.0
 15height = 144.0
 16
 17# Create nodes
 18#    tag, X, Y
 19node(1, 0.0, 0.0)
 20node(2, width, 0.0)
 21node(3, 0.0, height)
 22node(4, width, height)
 23
 24# Fix supports at base of columns
 25#   tag, DX, DY, RZ
 26fix(1, 1, 1, 1)
 27fix(2, 1, 1, 1)
 28
 29# Define materials for nonlinear columns
 30# ------------------------------------------
 31# CONCRETE                   tag  f'c    ec0    f'cu   ecu
 32# Core concrete (confined)
 33uniaxialMaterial('Concrete01', 1, -6.0, -0.004, -5.0, -0.014)
 34
 35# Cover concrete (unconfined)
 36uniaxialMaterial('Concrete01', 2, -5.0, -0.002, 0.0, -0.006)
 37
 38# STEEL
 39# Reinforcing steel
 40fy = 60.0;  # Yield stress
 41E = 30000.0;  # Young's modulus
 42#                         tag  fy E0    b
 43uniaxialMaterial('Steel01', 3, fy, E, 0.01)
 44
 45# Define cross-section for nonlinear columns
 46# ------------------------------------------
 47
 48#  some parameters
 49colWidth = 15
 50colDepth = 24
 51
 52cover = 1.5
 53As = 0.60  # area of no. 7 bars
 54
 55# some variables derived from the parameters
 56y1 = colDepth / 2.0
 57z1 = colWidth / 2.0
 58
 59section('Fiber', 1)
 60
 61# Create the concrete core fibers
 62patch('rect', 1, 10, 1, cover - y1, cover - z1, y1 - cover, z1 - cover)
 63
 64# Create the concrete cover fibers (top, bottom, left, right)
 65patch('rect', 2, 10, 1, -y1, z1 - cover, y1, z1)
 66patch('rect', 2, 10, 1, -y1, -z1, y1, cover - z1)
 67patch('rect', 2, 2, 1, -y1, cover - z1, cover - y1, z1 - cover)
 68patch('rect', 2, 2, 1, y1 - cover, cover - z1, y1, z1 - cover)
 69
 70# Create the reinforcing fibers (left, middle, right)
 71layer('straight', 3, 3, As, y1 - cover, z1 - cover, y1 - cover, cover - z1)
 72layer('straight', 3, 2, As, 0.0, z1 - cover, 0.0, cover - z1)
 73layer('straight', 3, 3, As, cover - y1, z1 - cover, cover - y1, cover - z1)
 74
 75# Define column elements
 76# ----------------------
 77
 78# Geometry of column elements
 79#                tag
 80
 81geomTransf('PDelta', 1)
 82
 83# Number of integration points along length of element
 84np = 5
 85
 86# Lobatto integratoin
 87beamIntegration('Lobatto', 1, 1, np)
 88
 89# Create the coulumns using Beam-column elements
 90#               e            tag ndI ndJ transfTag integrationTag
 91eleType = 'forceBeamColumn'
 92element(eleType, 1, 1, 3, 1, 1)
 93element(eleType, 2, 2, 4, 1, 1)
 94
 95# Define beam elment
 96# -----------------------------
 97
 98# Geometry of column elements
 99#                tag
100geomTransf('Linear', 2)
101
102# Create the beam element
103#                          tag, ndI, ndJ, A,     E,    Iz, transfTag
104element('elasticBeamColumn', 3, 3, 4, 360.0, 4030.0, 8640.0, 2)
105
106# Define gravity loads
107# --------------------
108
109#  a parameter for the axial load
110P = 180.0;  # 10% of axial capacity of columns
111
112# Create a Plain load pattern with a Linear TimeSeries
113timeSeries('Linear', 1)
114pattern('Plain', 1, 1)
115
116# Create nodal loads at nodes 3 & 4
117#    nd  FX,  FY, MZ
118load(3, 0.0, -P, 0.0)
119load(4, 0.0, -P, 0.0)
120
121# ------------------------------
122# End of model generation
123# ------------------------------
124
125
126# ------------------------------
127# Start of analysis generation
128# ------------------------------
129
130# Create the system of equation, a sparse solver with partial pivoting
131system('BandGeneral')
132
133# Create the constraint handler, the transformation method
134constraints('Transformation')
135
136# Create the DOF numberer, the reverse Cuthill-McKee algorithm
137numberer('RCM')
138
139# Create the convergence test, the norm of the residual with a tolerance of
140# 1e-12 and a max number of iterations of 10
141test('NormDispIncr', 1.0e-12, 10, 3)
142
143# Create the solution algorithm, a Newton-Raphson algorithm
144algorithm('Newton')
145
146# Create the integration scheme, the LoadControl scheme using steps of 0.1
147integrator('LoadControl', 0.1)
148
149# Create the analysis object
150analysis('Static')
151
152# ------------------------------
153# End of analysis generation
154# ------------------------------
155
156
157# ------------------------------
158# Finally perform the analysis
159# ------------------------------
160
161# perform the gravity load analysis, requires 10 steps to reach the load level
162analyze(10)
163
164# Print out the state of nodes 3 and 4
165# print node 3 4
166
167# Print out the state of element 1
168# print ele 1
169
170u3 = nodeDisp(3, 2)
171u4 = nodeDisp(4, 2)
172
173results = open('results.out', 'a+')
174
175if abs(u3 + 0.0183736) < 1e-6 and abs(u4 + 0.0183736) < 1e-6:
176    results.write('PASSED : RCFrameGravity.py\n')
177    print("Passed!")
178else:
179    results.write('FAILED : RCFrameGravity.py\n')
180    print("Failed!")
181
182results.close()
183
184print("==========================")
```
