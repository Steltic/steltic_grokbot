<!-- chunk_id: dambreak3Dexample_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/dambreak3Dexample.html",
 "title": "14.3.2.3. Dambreak 3D Analysis using background mesh",
 "category": "analysis",
 "command": "dambreak3Dexample",
 "doc_section": "src",
 "rel_path": "src/dambreak3Dexample.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3430,
 "word_count": 477,
 "has_code": true,
 "has_table": false
} -->

## 14.3.2.3. Dambreak 3D Analysis using background mesh

1. The source code is shown below, which can be downloaded [`here`](https://openseespydoc.readthedocs.io/en/latest/_downloads/8555bc800a29229385d7680974c3aed3/dambreak3D.py).
2. Run the source code in your favorite Python program.
3. The [ParaView](https://www.paraview.org/) is needed to view the results. To view the displaced shape of fluid, use the “Warp By Vector” filter with scale factor = 1.0.

```
  1import openseespy.opensees as ops
  2
  3import os.path
  4import os
  5
  6# remove existing model
  7ops.wipe()
  8
  9# set modelbuilder
 10ops.model('basic', '-ndm', 3, '-ndf', 3)
 11
 12# geometric
 13L = 0.146
 14H = L*2
 15h = L/20
 16
 17numx = 3.0
 18numy = 3.0
 19numz = 3.0
 20
 21# material
 22rho = 1000.0
 23mu = 0.0001
 24b1 = 0.0
 25b2 = 0.0
 26b3 = -9.81
 27kappa = -1.0
 28
 29# time steps
 30dtmax = 1e-3
 31dtmin = 1e-3
 32totaltime = 1.0
 33
 34# filename
 35filename = 'dambreak3D'
 36
 37# recorder
 38ops.recorder('BgPVD', filename, 'disp', 'vel', 'pressure','-dT',0.05)
 39if not os.path.exists(filename):
 40    os.makedirs(filename)
 41
 42# fluid particles
 43nx = round(L/h*numx)
 44ny = round(L/h*numy)
 45nz = round(H/h*numz)
 46
 47eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, b3, kappa]
 48partArgs = ['cube', 0.0,0.0,0.0,  L,L,H,   nx,ny,nz]
 49ops.mesh('part',100, *partArgs, *eleArgs)
 50
 51print('num particles =',nx*ny*nz)
 52
 53# wall nodes
 54ndf = 3
 55
 56ops.node(1, 0.0, 0.0, 0.0)
 57ops.node(2, 4*L, 0.0, 0.0)
 58ops.node(3, 4*L, L, 0.0)
 59ops.node(4, 0.0, L, 0.0)
 60
 61ops.node(5, 0.0, 0.0, H)
 62ops.node(6, 4*L, 0.0, H)
 63ops.node(7, 4*L, L, H)
 64ops.node(8, 0.0, L, H)
 65
 66id = 1
 67ops.mesh('line', 1, 2, 1,2, id, ndf, h)
 68ops.mesh('line', 2, 2, 2,3, id, ndf, h)
 69ops.mesh('line', 3, 2, 3,4, id, ndf, h)
 70ops.mesh('line', 4, 2, 1,4, id, ndf, h)
 71
 72ops.mesh('line', 5, 2, 5,6, id, ndf, h)
 73ops.mesh('line', 6, 2, 6,7, id, ndf, h)
 74ops.mesh('line', 7, 2, 7,8, id, ndf, h)
 75ops.mesh('line', 8, 2, 5,8, id, ndf, h)
 76
 77ops.mesh('line', 9, 2, 1,5, id, ndf, h)
 78ops.mesh('line', 10, 2, 2,6, id, ndf, h)
 79ops.mesh('line', 11, 2, 3,7, id, ndf, h)
 80ops.mesh('line', 12, 2, 4,8, id, ndf, h)
 81
 82ops.mesh('quad', 13, 4, 1,2,3,4, id ,ndf, h)
 83ops.mesh('quad', 14, 4, 1,10,5,9, id ,ndf, h)
 84ops.mesh('quad', 15, 4, 2,11,6,10, id ,ndf, h)
 85ops.mesh('quad', 16, 4, 3,12,7,11, id ,ndf, h)
 86ops.mesh('quad', 17, 4, 4,9,8,12, id ,ndf, h)
 87
 88fixedNodes = set()
 89for mid in [13,14,15,16,17]:
 90    for nd in ops.getNodeTags('-mesh', mid):
 91        fixedNodes.add(nd)
 92for nd in fixedNodes:
 93    ops.fix(nd, 1,1,1)
 94fixedNodes = list(fixedNodes)
 95
 96
 97# background mesh
 98lower = [-L, -L, -L]
 99upper = [5*L, 5*L, 3*L]
100ops.mesh('bg', h, *lower, *upper, '-structure',1, len(fixedNodes),*fixedNodes)
101
102# create constraint object
103ops.constraints('Plain')
104
105# create numberer object
106ops.numberer('Plain')
107
108# create convergence test object
109ops.test('PFEM', 1e-5, 1e-2, 1e-5, 1e-5, 1e-15, 1e-15, 10,3, 1, 2)
110
111# create algorithm object
112ops.algorithm('Newton')
113
114# create integrator object
115ops.integrator('PFEM')
116
117# create SOE object
118ops.system('PFEM')
119
120# create analysis object
121ops.analysis('PFEM', dtmax, dtmin, b3)
122
123
124# analyze
125while ops.getTime() < totaltime:
126
127    if ops.analyze() < 0:
128        break
129
130    ops.remesh()
131
132
133
```
