<!-- chunk_id: dambreakbg_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/dambreakbg.html",
 "title": "14.3.2.1. Dambreak Analysis using background mesh",
 "category": "analysis",
 "command": "dambreakbg",
 "doc_section": "src",
 "rel_path": "src/dambreakbg.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2878,
 "word_count": 411,
 "has_code": true,
 "has_table": false
} -->

## 14.3.2.1. Dambreak Analysis using background mesh

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/c78f4b5cf86097600359c3e5699f35bb/dambreak-bg.py).
2. Run the source code in your favorite Python program.
3. The [ParaView](https://www.paraview.org/) is needed to view the results. To view the displaced shape of fluid, use the “Warp By Vector” filter with scale factor = 1.0.

```
  1import os
  2import os.path
  3import openseespy.opensees as ops
  4
  5# ------------------------------
  6# Start of model generation
  7# -----------------------------
  8
  9# wipe all previous objects
 10ops.wipe()
 11
 12# create a model with fluid
 13ops.model('basic', '-ndm', 2, '-ndf', 2)
 14
 15# geometric
 16L = 0.146
 17H = L * 2
 18h = L / 40
 19
 20# number of particles per cell in each direction
 21numx = 3.0
 22numy = 3.0
 23
 24# material
 25rho = 1000.0
 26mu = 0.0001
 27b1 = 0.0
 28b2 = -9.81
 29thk = 0.012
 30kappa = -1.0
 31
 32# analysis
 33dtmax = 1e-3
 34dtmin = 1e-3
 35totaltime = 1.0
 36filename = 'dambreak-bg'
 37
 38# recorder
 39ops.recorder('BgPVD', filename, 'disp', 'vel', 'pressure', '-dT', 1e-3)
 40if not os.path.exists(filename):
 41    os.makedirs(filename)
 42
 43# fluid particles
 44ndf = 2
 45
 46# total number of particles in each direction
 47nx = round(L / h * numx)
 48ny = round(H / h * numy)
 49
 50# create particles
 51eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thk, kappa]
 52partArgs = ['quad', 0.0, 0.0, L, 0.0, L, H, 0.0, H, nx, ny]
 53parttag = 1
 54ops.mesh('part', parttag, *partArgs, *eleArgs, '-vel', 0.0, 0.0)
 55
 56print('num particles =', nx * ny)
 57
 58# wall
 59ops.node(1, 0.0, H)
 60ops.node(2, 0.0, 0.0)
 61ops.node(3, 4 * L, 0.0)
 62ops.node(4, 4 * L, H)
 63
 64walltag = 2
 65wallid = 1
 66ops.mesh('line', walltag, 4, 1, 2, 3, 4, wallid, ndf, h)
 67
 68wallnodes = ops.getNodeTags('-mesh', walltag)
 69
 70for nd in wallnodes:
 71    ops.fix(nd, 1, 1)
 72
 73# background mesh
 74lower = [-h, -h]
 75upper = [4 * L + L, H + L]
 76
 77ops.mesh('bg', h, *lower, *upper,
 78         '-structure', wallid, len(wallnodes), *wallnodes)
 79
 80# create constraint object
 81ops.constraints('Plain')
 82
 83# create numberer object
 84ops.numberer('Plain')
 85
 86# create convergence test object
 87ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 10, 3, 1, 2)
 88
 89# create algorithm object
 90ops.algorithm('Newton')
 91
 92# create integrator object
 93ops.integrator('PFEM', 0.5, 0.25)
 94
 95# create SOE object
 96ops.system('PFEM')
 97# ops.system('PFEM', '-mumps) Linux version can use mumps
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
109    ops.remesh()
110
111print("==========================================")
```
