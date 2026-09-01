<!-- chunk_id: HystereticSM_materialDemo_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/examples/notebooks/hystereticSM/HystereticSM_materialDemo.html",
 "title": "Opensees uniaxialMaterial Demo: HystereticSM",
 "category": "examples",
 "manual_group": "",
 "command": "HystereticSM_materialDemo",
 "doc_section": "user/examples/notebooks/hystereticSM",
 "rel_path": "user/examples/notebooks/hystereticSM/HystereticSM_materialDemo.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4959,
 "word_count": 350,
 "has_code": true,
 "has_table": false
} -->

## Opensees uniaxialMaterial Demo: HystereticSM

#### Silvia Mazzoni, 2023

##### silviamazzoni@yahoo.com

#### Initialize Notebook

```
[1]:
```

```
import sys

OpenSeesPyPath = r'D:\Projects\OpenSees\Development\OpenSeesFork\Win64\bin'
sys.path.append(OpenSeesPyPath)
import opensees as ops

# import openseespy.opensees as ops
# ------------------
#  initialize
# ------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# https://github.com/jupyter-widgets/ipywidgets/issues/1853
from ipywidgets.widgets.interaction import show_inline_matplotlib_plots
#%matplotlib notebook

import glob
import urllib
import webbrowser
from ipywidgets import widgets, Output
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
from IPython.display import display
from IPython.display import clear_output
from IPython.display import HTML
from IPython.display import Image
from IPython.display import Javascript
from urllib.parse import urljoin
from urllib.request import pathname2url
from pathlib import Path
from datetime import date
import os
from os.path import expanduser
#http://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html
#https://stackoverflow.com/questions/22487231/how-to-start-a-batch-file-from-within-a-python-script-and-detach-from-it
import subprocess

#from ipysheet import sheet, cell, row, column, cell_range,from_dataframe,to_dataframe
pd.set_option("display.max_rows", None)
np.set_printoptions(threshold=np.inf)
plt.interactive(True)
```

#### Define Strain Histories

```
[2]:
```

```
strainMap = {}
def defineStrainHistory(peaksArray,scaleFactor,nSteps,nCycles):
    strain = []
    for thisPeak in peaksArray:
        for i in range(nCycles):
            strain = np.append(strain,np.linspace(0,thisPeak*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(thisPeak*scaleFactor,-thisPeak*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(-thisPeak*scaleFactor,0,nSteps))

    return strain

def defineStrainHistoryOneSided(peaksArray,scaleFactor,nSteps,nCycles):
    strain = []
    for thisPeak in peaksArray:
        for i in range(nCycles):
            strain = np.append(strain,np.linspace(0,thisPeak*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(thisPeak*scaleFactor,0,nSteps))

    return strain

def defineStrainHistoryUnsymm(peaksArray,scaleFactor,nSteps,nCycles):
    strain = []
    for thisPeak in peaksArray:
        for i in range(nCycles):
            strain = np.append(strain,np.linspace(0,thisPeak*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(thisPeak*scaleFactor,-thisPeak*scaleFactor/2,nSteps))
            strain = np.append(strain,np.linspace(-thisPeak*scaleFactor/2,0,nSteps))

    return strain

def defineStrainHistoryDip(peaksArray,scaleFactor,nSteps,nCycles):
    strain = []
    for thisPeak in peaksArray:
        for i in range(nCycles):
            strain = np.append(strain,np.linspace(0,thisPeak/2*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(thisPeak/2*scaleFactor,-thisPeak/2*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(-thisPeak/2*scaleFactor,thisPeak/2*scaleFactor,nSteps))
            strain = np.append(strain,np.linspace(thisPeak/2*scaleFactor,thisPeak*scaleFactor,nSteps))
    return strain

peaksArray=np.array([.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])/10
# peaksArray=[1,10]
scaleFactor = .1
# scaleFactor = 0.01
nSteps = 100
nCycles = 3
strain=defineStrainHistory(peaksArray,scaleFactor,nSteps,nCycles)
plt.plot(strain)
strainMap['symmCycles'] = strain

strainUnsymm=defineStrainHistoryUnsymm(peaksArray,scaleFactor,nSteps,nCycles)
plt.plot(strainUnsymm)
strainMap['strainUnsymm'] = strainUnsymm

strainOneSidedPush=defineStrainHistoryOneSided(peaksArray,scaleFactor,nSteps,nCycles)
plt.plot(strainOneSidedPush)
strainMap['strainOneSidedPush'] = strainOneSidedPush

strainOneSidedPull=defineStrainHistoryOneSided(peaksArray,-scaleFactor,nSteps,nCycles)
plt.plot(strainOneSidedPull)
strainMap['strainOneSidedPull'] = strainOneSidedPull

peaksArray=np.array([10])/10
scaleFactor = .1
nSteps = 100
nCycles = 1
strainOneCycle=defineStrainHistory(peaksArray,scaleFactor,nSteps,nCycles)
plt.plot(strainOneCycle)
strainMap['strainOneCycle'] = strainOneCycle

peaksArray=np.array([10])/10
scaleFactor = .1
nSteps = 100
nCycles = 1
strainDip=defineStrainHistoryDip(peaksArray,scaleFactor,nSteps,nCycles)
plt.plot(strainOneCycle)
strainMap['strainDip'] = strainDip

thisPeak = 10
scaleFactor = 0.02
strainPush = np.linspace(0,thisPeak*scaleFactor,nSteps)
strainMap['strainPush'] = strainPush

thisPeak = -10
scaleFactor = 0.02
strainPull = np.linspace(0,thisPeak*scaleFactor,nSteps)
strainMap['strainPull'] = strainPull

plt.show()
```

#### Utilities

```
[3]:
```

```
def formatAx(axModel,Title,xLabel,yLabel,titleFontSize = 12, otherFontSize = 12,legendLocation = 'best',backgroundColor = '',legendFontSize=0,ncol = 1):
