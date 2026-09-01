<!-- chunk_id: Material_Properties_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "",
 "title": "Material Properties",
 "category": "other",
 "manual_group": "",
 "command": "",
 "doc_section": "",
 "rel_path": "",
 "part_index": 0,
 "part_count": 3,
 "char_count": 14389,
 "word_count": 1349,
 "has_code": true,
 "has_table": false
} -->

## Material Properties [part 1/3]

```

```
[5]:
```

```
OpenSeesMaterialBaseValues = {}
OpenSeesMaterialDefaultValues = {}
M1 = 2772.
M2 = round(1.12*M1,1)
M3 = round(0.6*M1,1)
M4 = M3
M5 = round(0.1*M1,1)
M6 = M5
M7 = 0.01*M1
eps1 = 0.01
eps2 = 2.*eps1
eps3 = 4.*eps1
eps4 = 6.*eps1
eps5 = 8.*eps1
eps6 = 10.*eps1
eps7 = 12.*eps1

limitStateInput = ['-defoLimitStates',eps1,-eps1,eps2,-eps2,'-forceLimitStates',M1,-M1,M2,-M2]
positiveEnvelope = [M1, eps1, M2, eps2, M3, eps3, M4, eps4, M5, eps5, 200., eps6, 0, eps7]
negativeEnvelope = [-M1, -eps1, -M2, -eps2, -M3, -eps3]

OpenSeesMaterialBaseValues[f'HystereticSM']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope]
OpenSeesMaterialBaseValues[f'HystereticSMsymm']=    ['HystereticSM','-posEnv',*positiveEnvelope]

for thisPinch in [[1,1],[.2,.8],[.8,.2]]:
    OpenSeesMaterialDefaultValues[f'HystereticSM_pinch={thisPinch}']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope, '-pinch',*thisPinch]
for thisDamage1 in [0,0.01,0.1]:
    OpenSeesMaterialDefaultValues[f'HystereticSM_damage1={thisDamage1}']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope, '-damage',thisDamage1,0]
for thisDamage2 in [0,0.01,0.1]:
    OpenSeesMaterialDefaultValues[f'HystereticSM_damage2={thisDamage2}']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope, '-damage',0,thisDamage2]
for thisBeta in [0,0.5,1]:
    OpenSeesMaterialDefaultValues[f'HystereticSM_beta={thisBeta}']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope, '-beta',thisBeta]
dmg1a = 0.005
dmg2a = 0.002
for thisDegEnv in [0,1,5]:
    OpenSeesMaterialDefaultValues[f'HystereticSM_degEnv={thisDegEnv}']=    ['HystereticSM','-posEnv',*positiveEnvelope, '-negEnv',*negativeEnvelope,'-damage',dmg1a,dmg2a,'-degEnv',thisDegEnv,-thisDegEnv]
```

#### Analysis Set 1: Pushover

```
[6]:
```

```
AllStressStrain = {}
allStrainArrayPush = ['strainPush','strainPull']
figSizeH = 4
figSizeV = 4
DPI = 200

for thisMaterial in OpenSeesMaterialBaseValues.keys():
    print('--------------------------------------------')
    print(thisMaterial)
    figEach = plt.figure(f'Material Response Each {thisMaterial}',figsize=(figSizeH,figSizeV), dpi=DPI, facecolor='w', edgecolor='k' )
    axEach = figEach.add_subplot(1,1,1)

    istrain = 0
    for thisStrainLabel in allStrainArrayPush:
        thisStrain = strainMap[thisStrainLabel]
        ops.wipe()
        materialTag = 99
        istrain +=1

        inputArray = OpenSeesMaterialBaseValues[thisMaterial]

        MaterialInput = inputArray[0],materialTag,*inputArray[1:]
        print(f'ops.uniaxialMaterial{MaterialInput}')
        MaterialInputTcl = str(MaterialInput).replace(',',' ').replace('(','').replace(')','').replace("'",'')
        print(f'uniaxialMaterial {MaterialInputTcl}')

        ops.uniaxialMaterial(*MaterialInput)

        ops.testUniaxialMaterial(materialTag)
        stress = []
        MUy = []
        for eps in thisStrain:
            ops.setStrain(eps)
            stress.append(ops.getStress())
            tangent = ops.getTangent() # Not used

        thisCount = len(list(AllStressStrain.keys()))
        thisKey = 'Run' + str(thisCount+1) + ' ' + thisMaterial
        AllStressStrain[thisKey] = {}
        AllStressStrain[thisKey]['strain'] = thisStrain
        AllStressStrain[thisKey]['stress'] = stress

        MaterialInputStr = str(MaterialInput).replace(',',',\n')

        zeros = np.zeros(len(AllStressStrain[thisKey]['strain']))
        line, = axEach.plot(zeros,AllStressStrain[thisKey]['stress'],'k-',linewidth='1.0',marker = '')
        line, = axEach.plot(AllStressStrain[thisKey]['strain'], zeros,'k-',linewidth='1.0',marker = '')
        line, = axEach.plot(AllStressStrain[thisKey]['strain'], AllStressStrain[thisKey]['stress'],'b',linewidth='1.5',marker = '')
    formatAx(axEach,thisMaterial,'Strain,Rotation,Curvature, or Deformation','Stress,Moment,Moment, or Force',8,8,'best','lightgrey',4)
    plt.xticks([])
    plt.yticks([])
    figEach.tight_layout()
    plt.show()
    figFilename = f'D:\\Projects\\OpenSees\\Development\\_JupyterNotebooks\\HystereticSM\\{thisMaterial}_{thisStrainLabel}.jpg'
```

```
--------------------------------------------
HystereticSM
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04
```

```
HystereticSM: multi-point envelope + DCR recorders  - Code by Silvia Mazzoni, 2023 (silviamazzoni@yahoo.com)
```

```
--------------------------------------------
HystereticSMsymm
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12
```

#### Analysis Set 2: Cyclic

```
[7]:
```

```
AllStressStrain = {}

Nmaterials = len(OpenSeesMaterialDefaultValues.keys())
Ncols = 2
Nrows = int(Nmaterials/Ncols)
Nrows = 2

figSizeH = 2*Ncols
figSizeV = 2*Nrows
DPI = 200

thisCount = 0
allStrainArray = ['symmCycles',  'strainOneSidedPush', 'strainOneSidedPull','strainDip']
iStrain = 0
for thisStrainLabel in allStrainArray:
    thisStrain = strainMap[thisStrainLabel]
    iStrain += 1
    iplt = 1
    for thisMaterial in OpenSeesMaterialDefaultValues.keys():
        print('--------------------------------------------')
        print(thisMaterial)
        if iplt == 1:
            figEach = plt.figure(f'Material Response Each {thisMaterial} {thisStrainLabel}',figsize=(figSizeH,figSizeV), dpi=DPI, facecolor='w', edgecolor='k' )
            axAll = figEach.add_subplot(Nrows,Ncols,1)
        iplt += 1
        axEach = figEach.add_subplot(Nrows,Ncols,iplt)

        counter = thisCount + 1
        ops.wipe()
        materialTag = 99

        inputArray = OpenSeesMaterialDefaultValues[thisMaterial]

        MaterialInput = inputArray[0],materialTag,*inputArray[1:]
        print(f'ops.uniaxialMaterial{MaterialInput}')
        MaterialInputTcl = str(MaterialInput).replace(',',' ').replace('(','').replace(')','').replace("'",'')
        print(f'uniaxialMaterial {MaterialInputTcl}')
        ops.uniaxialMaterial(*MaterialInput)

        ops.testUniaxialMaterial(materialTag)
        stress = []
        MUy = []
        for eps in thisStrain:
            ops.setStrain(eps)
            stress.append(ops.getStress())
            tangent = ops.getTangent() # Not used

        thisCount = len(list(AllStressStrain.keys()))
        thisKey = 'Run' + str(thisCount+1) + ' ' + thisMaterial
        AllStressStrain[thisKey] = {}
        AllStressStrain[thisKey]['strain'] = thisStrain
        AllStressStrain[thisKey]['stress'] = stress

        MaterialInputStr = str(MaterialInput).replace(',',',\n')
        line, = axAll.plot(AllStressStrain[thisKey]['strain'], AllStressStrain[thisKey]['stress'],linewidth='1',label=thisMaterial,marker = '')
        line, = axEach.plot(AllStressStrain[thisKey]['strain'], AllStressStrain[thisKey]['stress'],linewidth='1',label=MaterialInputStr,marker = '')
        formatAx(axEach,thisMaterial,'Strain,Rotation,Curvature, or Deformation','Stress,Moment,Moment, or Force',4,4,'best','lightgrey',2)
        if iplt == 4:
            figEach.tight_layout()
            formatAx(axAll,"Compare All",'Strain,Rotation,Curvature, or Deformation','Stress,Moment,Moment, or Force',4, 4,'best','lightblue',2)
            plt.show()
            iplt = 1
```

```
--------------------------------------------
HystereticSM_pinch=[1, 1]
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 1, 1)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  1  1
--------------------------------------------
HystereticSM_pinch=[0.2, 0.8]
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 0.2, 0.8)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  0.2  0.8
--------------------------------------------
HystereticSM_pinch=[0.8, 0.2]
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 0.8, 0.2)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  0.8  0.2
```

```
--------------------------------------------
HystereticSM_damage1=0
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0
--------------------------------------------
HystereticSM_damage1=0.01
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0.01, 0)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.01  0
--------------------------------------------
HystereticSM_damage1=0.1
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0.1, 0)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.1  0
```

```
--------------------------------------------
HystereticSM_damage2=0
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0
--------------------------------------------
HystereticSM_damage2=0.01
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0.01)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.01
--------------------------------------------
HystereticSM_damage2=0.1
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0.1)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.1
```

```
--------------------------------------------
HystereticSM_beta=0
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 0)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0
--------------------------------------------
HystereticSM_beta=0.5
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 0.5)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0.5
--------------------------------------------
HystereticSM_beta=1
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 1)
uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  1
```
