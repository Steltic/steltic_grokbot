<!-- chunk_id: FSIFluidBoundaryElement2D_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIFluidBoundaryElement2D.html",
 "title": "3.1.10.34. FSIFluidBoundaryElement2D Element",
 "category": "command_manual",
 "manual_group": "model",
 "command": "FSIFluidBoundaryElement2D",
 "doc_section": "user/manual/model/elements",
 "rel_path": "user/manual/model/elements/FSIFluidBoundaryElement2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5742,
 "word_count": 721,
 "has_code": true,
 "has_table": true
} -->

## 3.1.10.34. FSIFluidBoundaryElement2D Element

#### 3.1.10.34.1. Description

This command is used to construct an FSIFluidBoundaryElement2D element object. The FSIFluidBoundaryElement2D element is a 2-node linear acoustic boundary element object with the following features:

1. It is based on the Eulerian pressure formulation ([[ZienkiewiczEtAl1978]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#zienkiewiczetal1978) , [[ZienkiewiczEtAl2000]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#zienkiewiczetal2000) , [[LøkkeEtAl2017]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#lokkeetal2017) ) for (Class I) fluid-structure interaction problems.
2. It uses a 2 integration points Gauss quadrature.
3. Depending on the input variables, it enables the implementation of radiation boundary, reservoir bottom absorption or free surface effects.

#### 3.1.10.34.2. Input Parameters

**element FSIFluidBoundaryElement2D $eleTag $n1 $n2 $cc $alpha $g <-thickness $thickness>**

| Argument | Type | Description |
| --- | --- | --- |
| $eleTag | integer | unique integer tag identifying element object |
| $n1 $n2 | 2 integers | the two nodes defining the element (-ndm 2 -ndf 1) |
| $cc | float | speed of pressure waves in water |
| $alpha | float | reservoir bottom reflection coefficient ([[LøkkeEtAl2017]](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/elements/FSIInterfaceElement2D.html#lokkeetal2017)) |
| $g | float | acceleration due to gravity |
| Optional: |  |  |
| $thickness | float | the thickness in 2D problems (default 1.0). |

Fig. 3.1.10.42 **Figure 1. Nodes, Gauss points and parent coordinate system**

#### 3.1.10.34.3. Theory

For additional documentation regarding the derivation of the implemented finite elements ([FSIFluidElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIFluidElement2D.rst), FSIFluidBoundaryElement2D, [FSIInterfaceElement2D](https://github.com/esimbort/OpenSeesDocumentation/blob/master/source/user/manual/model/elements/FSIInterfaceElement2D.rst)) based on the Eulerian pressure formulation, please refer to the attached PDF document ([Link to PDF](https://drive.google.com/drive/folders/1QnWEC6kJrFct5korO89bqL1lcn7zi4yG))

#### 3.1.10.34.4. Example

Three cases of valid inputs are shown below: 1. Radiation boundary, 2. Reservoir bottom absorption and 3. Surface waves effects.

1. **Tcl Code**

```
# set up a 2D-1DOF model: Radiation Boundary Side
model Basic -ndm 2 -ndf 1
node 11  0.0  0.0
node 22  1.0  1.0

# create the acoustic boundary element at radiation boundary side with speed of pressure waves in water, cc = 1.440000e+03 (set alpha = 0, g = 0 to exclude bottom absorption and mass terms for water surface, respectively)
set cc 1.440000e+03
element FSIFluidBoundaryElement2D 3  11 22  $cc 0.0 0.0 -thickness 1.0

    # set up a 2D-1DOF model: Reservoir Bottom Absorption Boundary
model Basic -ndm 2 -ndf 1
node 11  0.0  0.0
node 22  1.0  1.0

# create the acoustic boundary element at the bottom boundary of a reservoir given speed of pressure waves in water, cc = 1.440000e+03 and reservoir bottom reflection coefficient, alpha = 9.990000e-01 (set g = 0 to exclude mass terms for water surface)
set cc 1.440000e+03
    set alpha 9.990000e-01
element FSIFluidBoundaryElement2D 4  11 22  $cc $alpha 0.0 -thickness 1.0

    # set up a 2D-1DOF model: Free Surface Boundary
model Basic -ndm 2 -ndf 1
node 11  0.0  0.0
node 22  1.0  1.0

# create the acoustic boundary element at the free surface boundary of the reservoir given g = 9.807 (set alpha = 0, cc = 0 to exclude damping terms)
set cc 1.440000e+03
    set alpha 9.990000e-01
set g 9.807
    element FSIFluidBoundaryElement2D 5  11 22   0.0 0.0 $g -thickness 1.0
```

1. **Python Code**

```
# set up a 2D-1DOF model: Radiation Boundary Side
model('Basic', '-ndm', 2, '-ndf', 1)
node(11, 0.0, 0.0)
node(22, 1.0, 1.0)

# create the acoustic boundary element at radiation boundary side
cc = 1.440000e+03
element('FSIFluidBoundaryElement2D', 3, 11, 22, cc, 0.0, 0.0, thickness=1.0)

    # set up a 2D-1DOF model: Reservoir Bottom Absorption Boundary
model('Basic', '-ndm', 2, '-ndf', 1)
node(11, 0.0, 0.0)
node(22, 1.0, 1.0)

# create the acoustic boundary element at the bottom boundary of a reservoir
cc = 1.440000e+03
    alpha = 9.990000e-01
element('FSIFluidBoundaryElement2D', 4, 11, 22, cc, alpha, 0.0, thickness=1.0)

    # set up a 2D-1DOF model: Free Surface Boundary
model('Basic', '-ndm', 2, '-ndf', 1)
node(11, 0.0, 0.0)
node(22, 1.0, 1.0)

# create the acoustic boundary element at the free surface boundary of the reservoir
g = 9.807
element('FSIFluidBoundaryElement2D', 5, 11, 22, 0.0, 0.0, g, thickness=1.0)
```

Code Developed, implemented and tested by:

Massimo Petracca (ASDEA Software),

Enrique Simbort (UC San Diego),

Joel Conte (UC San Diego).

#### 3.1.10.34.5. References

**ZienkiewiczEtAl1978**

> Zienkiewicz O.C., Bettess P. (1978) “Fluid-structure dynamic interaction and wave forces. An introduction to numerical treatment”, Inter. J. Numer. Meth. Eng.., 13(1): 1–16. ([Link to article](https://onlinelibrary.wiley.com/doi/10.1002/nme.1620130102))

**ZienkiewiczEtAl2000**

> Zienkiewicz O.C., Taylor R.L. (2000) “The Finite Element Method”, Butterworth-Heinemann, Vol.1, 5th Ed., Ch.19.

**LøkkeEtAl2017(1,2)**

> Løkke A., Chopra A.K. (2017) “Direct finite element method for nonlinear analysis of semi-unbounded dam–water–foundation rock systems”, Earthquake Engineering and Structural Dynamics 46(8): 1267–1285. ([Link to article](https://onlinelibrary.wiley.com/doi/abs/10.1002/eqe.2855))
