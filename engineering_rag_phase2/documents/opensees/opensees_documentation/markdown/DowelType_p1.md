<!-- chunk_id: DowelType_p1 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/DowelType.html",
 "title": "3.1.5.26. DowelType Timber Joint Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "DowelType",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/DowelType.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 5217,
 "word_count": 742,
 "has_code": true,
 "has_table": false
} -->

## 3.1.5.26. DowelType Timber Joint Material [part 2/2]

The stiffness of the three guiding lines are defined. In the definitions, degradation models are included. Two kinds of degradation models can be selected by specifying the sign of the related parameters. The stiffnesses are expressed as:

\[\begin{split}K_{\mathrm{pinching}} = \begin{cases} K_{p}, & \alpha_p \geq 0 \ \mathrm{and} \ D_m \leq D_y \\ K_{p}\left(\frac{D_y}{D_m}\right)^{\alpha_p}, & \alpha_p \geq 0 \ \mathrm{and} \ D_m > D_y \\ K_{p}\left(\frac{F_{env}(D_{m,s})}{D_{m,s}K_{0,s}}\right)^{\lvert\alpha_p\rvert}, & \alpha_p < 0 \end{cases}\end{split}\]

\[\begin{split}K_{\mathrm{unloading}} = \begin{cases} R_uK_{0,s}, & \alpha_u \geq 0 \ \mathrm{and} \ \lvert D_{m,s}\rvert \leq D_y \\ R_uK_{0,s} \left(\frac{D_y}{\lvert D_{m,s}\rvert}\right)^{\alpha_u}, & \alpha_u \geq 0 \ \mathrm{and} \ \lvert D_{m,s}\rvert > D_y \\ R_uK_{0,s} \left(\frac{F_{env}(D_{m,s})}{D_{m,s}K_{0,s}}\right)^{\lvert\alpha_u\rvert}, & \alpha_u < 0 \end{cases}\end{split}\]

\[\begin{split}K_{\mathrm{reloading}} = \begin{cases} K_{0,o}, & \alpha_r \geq 0 \ \mathrm{and} \ \lvert D_{m,o}\rvert \leq D_y \\ K_{0,o} \left(\frac{D_y}{\lvert D_{m,o}\rvert}\right)^{\alpha_r}, & \alpha_r \geq 0 \ \mathrm{and} \ \lvert D_{m,o}\rvert > D_y \\ K_{0,o} \left(\frac{F_{env}(D_{m,s})}{D_{m,s}K_{0,s}}\right)^{\lvert\alpha_r\rvert}, & \alpha_r < 0 \end{cases}\end{split}\]

where \(K_{0,s}\) and \(K_{0,o}\) are the stiffness on the same and opposite side of the unloading point, respectively. \(D_{m,s}\) is the maximum or minimum displacement on the same side of the unloading point. \(D_{m,o}\) is the maximum or minimum displacement on the opposite side of the unloading point.

There are also a few special scenarios, illustrated in the following figure:

Special scenario 1 is the smooth transition from the pinching curve to the unloaded envelope curve.

Special scenario 2 is the case when reloading starts without reaching the pinching line.

Special scenario 3 is the case when large damage occurs. The hysteretic curve no longer reaches the pinching line.

Example 1

The following command constructs a DowelType hysteretic model with tag **1**. It simulates a nailed connection with symmetric exponential envelope curve.

1. **Tcl Code**

```
uniaxialMaterial DowelType 1 90 98.9 4.3 1.2 1.09 1.01 0.21 1.6 1.32 0 0.66 -exponential 823 0.02 955 10.7 123
```

1. **Python Code**

```
uniaxialMaterial('DowelType', 1, 90, 98.9, 4.3, 1.2, 1.09, 1.01, 0.21, 1.6, 1.32, 0, 0.66, '-exponential', 823, 0.02, 955, 10.7, 123)
```

The results of Example 1 is shown in the following figure:

Example 2

The following command constructs a DowelType hysteretic model with tag **2**.
It simulates a CLT angle bracket connection under shear force. The yielding of the steel connector is considered within the single model.
This example uses asymmetric Bezier curve as the envelope curve.

1. **Tcl Code**

```
uniaxialMaterial DowelType 2 445 170 3.8 1.3 1.03 1 0.34 3.2 0.92 0.03 -0.25 -bezier 3.2 19100 15 30500 34 40000 520 -5.3 -12800 -15.2 -25200 -43.1 -30400 510
```

1. **Python Code**

```
uniaxialMaterial('DowelType', 2, 445, 170, 3.8, 1.3, 1.03, 1, 0.34, 3.2, 0.92, 0.03, -0.25, '-bezier', 3.2, 19100, 15, 30500, 34, 40000, 520, -5.3, -12800, -15.2, -25200, -43.1, -30400, 510)
```

The results of Example 2 is shown in the following figure:

Example 3

The following command constructs a DowelType hysteretic model with tag **3**.
It simulates a nailed connection with asymmetric layout.
It uses an asymmetric piecewise envelope curve.

1. **Tcl Code**

```
uniaxialMaterial DowelType 3 60 114.9 4.9 1.3 1.09 1 0.06 0.9 1.69 0.26 0.53 -piecewise 0.5 340 0.9 700 2.5 1030 10 300 -0.9 -600 -1.8 -800 -4.2 -1020 -10 -790
```

1. **Python Code**

```
uniaxialMaterial('DowelType', 3, 60, 114.9, 4.9, 1.3, 1.09, 1, 0.06, 0.9, 1.69, 0.26, 0.53, '-piecewise', 0.5, 340, 0.9, 700, 2.5, 1030, 10, 300, -0.9, -600, -1.8, -800, -4.2, -1020, -10, -790)
```

The results of Example 3 is shown in the following figure:

Example 4

The following command constructs a DowelType hysteretic model with tag **4**.
It simulates the moment-rotational behavior of a bolted connection with a small initial stiffness.
It uses an asymmetric piecewise envelope curve.

1. **Tcl Code**

```
uniaxialMaterial DowelType 4 305 621.2 3.7 1.2 1.02 1 0.06 2.7 0.76 0.2 0 -piecewise 0.01 580 2.5 4200 4.4 17300 7 23700 10 16000 -0.1 -790 -2.2 -3900 -5 -14100 -5.2 -16500 -10 -7000
```

1. **Python Code**

```
uniaxialMaterial('DowelType', 4, 305, 621.2, 3.7, 1.2, 1.02, 1, 0.06, 2.7, 0.76, 0.2, 0, '-piecewise', 0.01, 580, 2.5, 4200, 4.4, 17300, 7, 23700, 10, 16000, -0.1, -790, -2.2, -3900, -5, -14100, -5.2, -16500, -10, -7000)
```

The results of Example 4 is shown in the following figure:

Code Developed by: [Hanlin Dong](http://www.hanlindong.com/en/) (self@hanlindong.com) and Xijun Wang, Tongji University, China.

**DongEtAl2021**

> Dong, H., He, M., Wang, X.*, Christopoulos, C., Li, Z., Shu, Z. (2021). “Development of a uniaxial hysteretic model for dowel-type timber joints in OpenSees.”, Construction and Building Materials, 288: 123112. [DOI: https://doi.org/10.1016/j.conbuildmat.2021.123112](https://doi.org/10.1016/j.conbuildmat.2021.123112)
