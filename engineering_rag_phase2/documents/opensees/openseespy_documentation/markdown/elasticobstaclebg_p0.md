<!-- chunk_id: elasticobstaclebg_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticobstaclebg.html",
 "title": "14.3.2.2. Dambreak with Elastic Obstacle Analysis using background mesh",
 "category": "analysis",
 "command": "elasticobstaclebg",
 "doc_section": "src",
 "rel_path": "src/elasticobstaclebg.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4353,
 "word_count": 620,
 "has_code": true,
 "has_table": false
} -->

## 14.3.2.2. Dambreak with Elastic Obstacle Analysis using background mesh

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/3d5ef8c261a5ddc444d5e8ac682e1909/obstacle-bg.py).
2. Run the source code in your favorite Python program.
3. The [ParaView](https://www.paraview.org/) is needed to view the results. To view the displaced shape of fluid, use the “Warp By Vector” filter with scale factor = 1.0.

```
  1import os
  2import openseespy.opensees as ops
  3
  4
  5print("=======================================================")
  6print("Starting Dambreak with Obstacle Background Mesh example")
  7
  8# ------------------------------
  9# Start of model generation
 10# -----------------------------
 11
 12# wipe all previous objects
 13ops.wipe()
 14
 15# create a model with fluid
 16ops.model('basic', '-ndm', 2, '-ndf', 3)
 17
 18# geometric
 19L = 0.146
 20H = L * 2
 21H2 = 0.3
 22b = 0.012
 23h = L / 40
 24Hb = 20.0 * b / 3.0
 25
 26# number of particles per cell in each direction
 27numx = 3.0
 28numy = 3.0
 29
 30# fluid properties
 31rho = 1000.0
 32mu = 0.0001
 33b1 = 0.0
 34b2 = -9.81
 35thk = 0.012
 36kappa = -1.0
 37
 38# elastis structural material
 39rhos = 2500.0
 40A = thk * thk
 41E = 1e6
 42Iz = thk * thk * thk * thk / 12.0
 43bmass = A * Hb * rhos
 44
 45# nonlinear structural material
 46E0 = 1e6
 47Fy = 5e4
 48hardening = 0.02
 49
 50nonlinear = False
 51
 52# analysis
 53dtmax = 1e-3
 54dtmin = 1e-3
 55totaltime = 1.0
 56
 57if nonlinear:
 58    filename = 'obstaclenonlinear-bg'
 59else:
 60    filename = 'obstacle-bg'
 61
 62# recorder
 63ops.recorder('BgPVD', filename, 'disp', 'vel', 'pressure', '-dT', 1e-3)
 64if not os.path.exists(filename):
 65    os.makedirs(filename)
 66
 67# fluid mesh
 68ndf = 3
 69
 70# total number of particles in each direction
 71nx = round(L / h * numx)
 72ny = round(H / h * numy)
 73
 74# create particles
 75eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thk, kappa]
 76partArgs = ['quad', 0.0, 0.0, L, 0.0, L, H, 0.0, H, nx, ny]
 77parttag = 1
 78ops.mesh('part', parttag, *partArgs, *eleArgs, '-vel', 0.0, 0.0)
 79
 80# wall mesh
 81ops.node(1, 2 * L, 0.0)
 82ops.node(2, 2 * L, Hb)
 83ops.node(3, 0.0, H)
 84ops.node(4, 0.0, 0.0)
 85ops.node(5, 4 * L, 0.0)
 86ops.node(6, 4 * L, H)
 87
 88sid = 1
 89walltag = 4
 90ops.mesh('line', walltag, 5, 3, 4, 1, 5, 6, sid, ndf, h)
 91
 92wallNodes = ops.getNodeTags('-mesh', walltag)
 93for nd in wallNodes:
 94    ops.fix(nd, 1, 1, 1)
 95
 96# structural mesh
 97
 98# transformation
 99transfTag = 1
100ops.geomTransf('Corotational', transfTag)
101
102# section
103secTag = 1
104if nonlinear:
105    matTag = 1
106    ops.uniaxialMaterial('Steel01', matTag, Fy, E0, hardening)
107    numfiber = 5
108    ops.section('Fiber', secTag)
109    ops.patch('rect', matTag, numfiber, numfiber, 0.0, 0.0, thk, thk)
110else:
111    ops.section('Elastic', secTag, E, A, Iz)
112
113# beam integration
114inteTag = 1
115numpts = 2
116ops.beamIntegration('Legendre', inteTag, secTag, numpts)
117
118coltag = 3
119eleArgs = ['dispBeamColumn', transfTag, inteTag]
120ops.mesh('line', coltag, 2, 1, 2, sid, ndf, h, *eleArgs)
121
122# mass
123sNodes = ops.getNodeTags('-mesh', coltag)
124bmass = bmass / len(sNodes)
125for nd in sNodes:
126    ops.mass(int(nd), bmass, bmass, 0.0)
127
128
129# background mesh
130lower = [-h, -h]
131upper = [5 * L, 3 * L]
132
133ops.mesh('bg', h, *lower, *upper,
134     '-structure', sid, len(sNodes), *sNodes,
135     '-structure', sid, len(wallNodes), *wallNodes)
136
137print('num nodes =', len(ops.getNodeTags()))
138print('num particles =', nx * ny)
139
140# create constraint object
141ops.constraints('Plain')
142
143# create numberer object
144ops.numberer('Plain')
145
146# create convergence test object
147ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 100, 3, 1, 2)
148
149# create algorithm object
150ops.algorithm('Newton')
151
152# create integrator object
153ops.integrator('PFEM', 0.5, 0.25)
154
155# create SOE object
156ops.system('PFEM')
157# system('PFEM', '-mumps') Linux version can use mumps
158
159# create analysis object
160ops.analysis('PFEM', dtmax, dtmin, b2)
161
162# analysis
163while ops.getTime() < totaltime:
164
165    # analysis
166    if ops.analyze() < 0:
167        break
168
169    ops.remesh()
170
171print("==========================================")
```
