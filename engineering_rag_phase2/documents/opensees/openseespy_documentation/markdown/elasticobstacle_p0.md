<!-- chunk_id: elasticobstacle_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/elasticobstacle.html",
 "title": "14.3.1.2. Dambreak with Elastic Obstacle Analysis using moving mesh",
 "category": "analysis",
 "command": "elasticobstacle",
 "doc_section": "src",
 "rel_path": "src/elasticobstacle.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3468,
 "word_count": 456,
 "has_code": true,
 "has_table": false
} -->

## 14.3.1.2. Dambreak with Elastic Obstacle Analysis using moving mesh

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/91c1c48249e217d8fbd1f1a0b2f1cf34/ElasticObstacle.py).
2. Run the source code in your favorite Python program.
3. The [ParaView](https://www.paraview.org/) is needed to view the results. To view the displaced shape of fluid, use the “Warp By Vector” filter with scale factor = 1.0.

```
  1import os
  2import openseespy.opensees as ops
  3
  4# ------------------------------
  5# Start of model generation
  6# -----------------------------
  7
  8# remove existing model
  9ops.wipe()
 10
 11# set modelbuilder
 12ops.model('basic', '-ndm', 2, '-ndf', 3)
 13
 14# geometric
 15L = 0.146
 16H = 2*L
 17H2 = 0.3
 18b = 0.012
 19h = 0.005
 20alpha = 1.4
 21Hb = 20.0*b/3.0
 22tw =  3*h
 23
 24# material
 25rho = 1000.0
 26mu = 0.0001
 27b1 = 0.0
 28b2 = -9.81
 29thk = 0.012
 30kappa = -1.0
 31
 32rhos = 2500.0
 33A = thk*thk
 34E = 1e6
 35Iz = thk*thk*thk*thk/12.0
 36bmass = A*Hb*rhos
 37
 38# analysis
 39dtmax = 1e-3
 40dtmin = 1e-6
 41totaltime = 1.0
 42
 43filename = 'obstacle'
 44
 45# recorder
 46if not os.path.exists(filename):
 47    os.makedirs(filename)
 48ops.recorder('PVD', filename, 'disp', 'vel', 'pressure')
 49
 50# nodes
 51ops.node(1, 0.0, 0.0)
 52ops.node(2, L, 0.0)
 53ops.node(3, L, H, '-ndf', 2)
 54ops.node(4, 0.0, H)
 55ops.node(5, 0.0, H2)
 56ops.node(6, 4*L, 0.0)
 57ops.node(7, 4*L, H2)
 58ops.node(8, -tw, H2)
 59ops.node(9, -tw, -tw)
 60ops.node(10, 4*L+tw, -tw)
 61ops.node(11, 4*L+tw, H2)
 62ops.node(12, 2*L, 0.0)
 63ops.node(13, 2*L, Hb)
 64
 65# ids for meshing
 66wall_id = 1
 67beam_id = 2
 68water_bound_id = -1
 69water_body_id = -2
 70
 71# transformation
 72transfTag = 1
 73ops.geomTransf('Corotational', transfTag)
 74
 75# section
 76secTag = 1
 77ops.section('Elastic', secTag, E, A, Iz)
 78
 79# beam integration
 80inteTag = 1
 81numpts = 2
 82ops.beamIntegration('Legendre', inteTag, secTag, numpts)
 83
 84# beam mesh
 85beamTag = 6
 86ndf = 3
 87ops.mesh('line', beamTag, 2, 12, 13, beam_id, ndf, h, 'dispBeamColumn', transfTag, inteTag)
 88
 89ndmass = bmass/len(ops.getNodeTags('-mesh', beamTag))
 90
 91for nd in ops.getNodeTags('-mesh', beamTag):
 92    ops.mass(nd, ndmass, ndmass, 0.0)
 93
 94# fluid mesh
 95fluidTag = 4
 96ndf = 2
 97ops.mesh('line', 1, 10, 4,5,8,9,10,11,7,6,12,2, wall_id, ndf, h)
 98ops.mesh('line', 2, 3, 2,1,4, wall_id, ndf, h)
 99ops.mesh('line', 3, 3, 2,3,4, water_bound_id, ndf, h)
100
101eleArgs = ['PFEMElementBubble',rho,mu,b1,b2,thk,kappa]
102ops.mesh('tri', fluidTag, 2, 2,3, water_body_id, ndf, h, *eleArgs)
103
104# wall mesh
105wallTag = 5
106ops.mesh('tri', wallTag, 2, 1,2, wall_id, ndf, h)
107
108for nd in ops.getNodeTags('-mesh', wallTag):
109    ops.fix(nd, 1,1,1)
110
111# save the original modal
112ops.record()
113
114# create constraint object
115ops.constraints('Plain')
116
117# create numberer object
118ops.numberer('Plain')
119
120# create convergence test object
121ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-15, 1e-15, 20, 3, 1, 2)
122
123# create algorithm object
124ops.algorithm('Newton')
125
126# create integrator object
127ops.integrator('PFEM')
128
129# create SOE object
130ops.system('PFEM')
131
132# create analysis object
133ops.analysis('PFEM', dtmax, dtmin, b2)
134
135# analysis
136while ops.getTime() < totaltime:
137
138    # analysis
139    if ops.analyze() < 0:
140        break
141
142    ops.remesh(alpha)
```
