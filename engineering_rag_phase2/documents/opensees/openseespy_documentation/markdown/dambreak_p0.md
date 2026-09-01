<!-- chunk_id: dambreak_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/dambreak.html",
 "title": "14.3.1.1. Dambreak Analysis using moving mesh",
 "category": "analysis",
 "command": "dambreak",
 "doc_section": "src",
 "rel_path": "src/dambreak.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2734,
 "word_count": 361,
 "has_code": true,
 "has_table": false
} -->

## 14.3.1.1. Dambreak Analysis using moving mesh

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/d7892ee8ac87c295211e0e4e3be5a192/dambreak.py).
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
 12ops.model('basic', '-ndm', 2, '-ndf', 2)
 13
 14# geometric
 15L = 0.146
 16H = L*2
 17H2 = 0.3
 18h = 0.005
 19alpha = 1.4
 20tw =  3*h
 21
 22# material
 23rho = 1000.0
 24mu = 0.0001
 25b1 = 0.0
 26b2 = -9.81
 27thk = 0.012
 28kappa = -1.0
 29
 30# time steps
 31dtmax = 1e-3
 32dtmin = 1e-6
 33totaltime = 1.0
 34
 35# filename
 36filename = 'dambreak'
 37
 38# recorder
 39if not os.path.exists(filename):
 40    os.makedirs(filename)
 41ops.recorder('PVD', filename, 'disp', 'vel', 'pressure')
 42
 43# nodes
 44ops.node(1, 0.0, 0.0)
 45ops.node(2, L, 0.0)
 46ops.node(3, L, H)
 47ops.node(4, 0.0, H)
 48ops.node(5, 0.0, H2)
 49ops.node(6, 4*L, 0.0)
 50ops.node(7, 4*L, H2)
 51ops.node(8, -tw, H2)
 52ops.node(9, -tw, -tw)
 53ops.node(10, 4*L+tw, -tw)
 54ops.node(11, 4*L+tw, H2)
 55
 56# ids for meshing
 57wall_id = 1
 58water_bound_id = -1
 59water_body_id = -2
 60
 61# wall mesh
 62wall_tag = 3
 63ndf = 2
 64ops.mesh('line', 1, 9, 4,5,8,9,10,11,7,6,2, wall_id, ndf, h)
 65ops.mesh('line', 2, 3, 2,1,4, wall_id, ndf, h)
 66ops.mesh('tri', wall_tag, 2, 1,2, wall_id, ndf, h)
 67
 68# fluid mesh
 69fluid_tag = 4
 70ops.mesh('line', 5, 3, 2,3,4, water_bound_id, ndf, h)
 71
 72eleArgs = ['PFEMElementBubble',rho,mu,b1,b2,thk,kappa]
 73ops.mesh('tri', fluid_tag, 2, 2,5, water_body_id, ndf, h, *eleArgs)
 74
 75for nd in ops.getNodeTags('-mesh', wall_tag):
 76    ops.fix(nd, 1,1)
 77
 78# save the original modal
 79ops.record()
 80
 81# create constraint object
 82ops.constraints('Plain')
 83
 84# create numberer object
 85ops.numberer('Plain')
 86
 87# create convergence test object
 88ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-15, 1e-15, 20, 3, 1, 2)
 89
 90# create algorithm object
 91ops.algorithm('Newton')
 92
 93# create integrator object
 94ops.integrator('PFEM')
 95
 96# create SOE object
 97ops.system('PFEM', '-umfpack', '-print')
 98
 99# create analysis object
100ops.analysis('PFEM', dtmax, dtmin, b2)
101
102# analysis
103while ops.getTime() < totaltime:
104
105    # analysis
106    if ops.analyze() < 0:
107        break
108
109    ops.remesh(alpha)
110
111
112
```
