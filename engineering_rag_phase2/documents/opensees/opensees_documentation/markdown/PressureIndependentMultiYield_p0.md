<!-- chunk_id: PressureIndependentMultiYield_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/ndMaterials/PressureIndependentMultiYield.html",
 "title": "3.1.6.9. Pressure Independent Multi Yield",
 "category": "command_manual",
 "manual_group": "material",
 "command": "PressureIndependentMultiYield",
 "doc_section": "user/manual/material/ndMaterials",
 "rel_path": "user/manual/material/ndMaterials/PressureIndependentMultiYield.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 7332,
 "word_count": 1097,
 "has_code": true,
 "has_table": true
} -->

## 3.1.6.9. Pressure Independent Multi Yield

Code Developed by: UC San Diego (**Dr. Zhaohui Yang**):

**PressureIndependMultiYield** material is an elastic-plastic material in which plasticity exhibits only in the deviatoric stress-strain response. The volumetric stress-strain response is linear-elastic and is independent of the deviatoric response. This material is implemented to simulate monotonic or cyclic response of materials whose shear behavior is insensitive to the confinement change. Such materials include, for example, organic soils or clay under fast (undrained) loading conditions.

During the application of gravity load (and static loads if any), material behavior is linear elastic. In the subsequent dynamic (fast) loading phase(s), the stress-strain response is elastic-plastic (see MATERIAL STAGE UPDATE below). Plasticity is formulated based on the multi-surface (nested surfaces) concept, with an associative flow rule. The yield surfaces are of the Von Mises type.

The command to create the material object is:

function

nDmaterial PressureIndependMultiYield $tag $nd $rho $refShearModul $refBulkModul $cohesi $peakShearStra <$frictionAng=0. $refPress=100. $pressDependCoe=0. $noYieldSurf=20 <$r1 $Gs1 …> >

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | A positive integer uniquely identifying the material among all nDMaterials. |
| $nd | *integer* | Number of dimensions, 2 for plane-strain, and 3 for 3D analysis. |
| $rho | *float* | Saturated soil mass density. |
| $refShearModul (Gr) | *float* | Reference low-strain shear modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| $refBulkModul (Br) | *float* | Reference bulk modulus, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| $cohesi (c) | *float* | Apparent cohesion at zero effective confinement. |
| $peakShearStra (γmax) | *float* | An octahedral shear strain at which the maximum shear strength is reached, specified at a reference mean effective confining pressure refPress of p’r (see below). |
| $frictionAng (Φ) | *float* | Friction angle at peak shear strength in degrees. (optional: default is 0.0). |
| $refPress (p’r) | *float* | Reference mean effective confining pressure at which Gr and Br and γmax are defined, optional (default is 100. kPa). |
| $pressDependCoe (d) | *float* | A positive constant defining variations of G and B as a function of instantaneous effective confinement p’(default is 0.0). see notes 4 and 5 below. |
| $noYieldSurf | *integer* | Number of yield surfaces, optional (must be less than 40: default is 20). The surfaces are generated based on the hyperbolic relation defined in Note 2 below. |
| $r $Gs | *float* | Instead of automatic surfaces generation (Note 2), you can define yield surfaces directly based on desired shear modulus reduction curve. To do so, add a minus sign in front of noYieldSurf, then provide noYieldSurf pairs of shear strain (γ) and modulus ratio (Gs) values. For example, to define 10 surfaces: … -10γ1Gs1 … γ10Gs10 … |

Note

1. The friction angle \(\phi\) and cohesion c define the variation of peak (octahedral) shear strength \(\tau_f\) as a function of current effective confinement \({p^t}_i\):

\[\tau_f = \frac{2 \sqrt{2} sin \phi}{3 - sin \phi}{p^t}_i + \frac{2 \sqrt{2}}{3}c\]

1. Automatic surface generation: at a constant confinement \(p^t\), the shear stress \(\tau\) (octahedral) - shear strain \(\gamma\) (octahedral) nonlinearity is defined by a hyperbolic curve (backbone curve):

\[\tau = \frac{G \gamma}{1 + \frac{\gamma}{\gamma_r}\left ( \frac{{p^t}_r}{p^t} \right)^d}\]

where \(\gamma_r\) satisfies the following equation at \({p^t}_r\)

\[\tau_f = \frac{2 \sqrt{2} sin \phi}{3 - sin \phi}{p^t}_r + \frac{2 \sqrt{2}}{3}c = \frac{G_r \gamma_{max}}{1 + \gamma_{max}/\gamma_r}\]

1. (User defined surfaces) The user specified friction angle \(\phi = 0\). cohesion c will be ignored. Instead, c is defined by \(c=\sqrt 3 \sigma_m / 2\), where \(\sigma_m\) is the product of the last modulus and strain pair in the modulus reduction curve. Therefore, it is important to adjust the backbone curve so as to render an appropriate c.

If the user specifies \(\gamma\) > 0, this \(\phi\) will be ignored. Instead, \(\phi\) is defined as follows:

\[sin \phi = \frac{3 (\sqrt 3 \sigma_m - 2c)/{p^t}_r}{6 + (\sqrt 3 \sigma_m - 2c)/{p^t}_r}\]

If the resulting \(\phi <0\), we set \(\phi =0\) and \(c=\sqrt 3 \sigma_m/2\).

Also remember that improper modulus reduction curves can result in strain softening response (negative tangent shear modulus), which is not allowed in the current model formulation. Finally, note that the backbone curve varies with confinement, although the variation is small within commonly interested confinement ranges. Backbone curves at different confinements can be obtained using the OpenSees element recorder facility

1. **$presDependCoef d** defines variations of G and B as a function of instantaneous effective confinement :math:p^t as follows:

\[ \begin{align}\begin{aligned}G = G_r \left ( \frac{p^t}{{p^t}_r} \right)^d\\B = B_r \left ( \frac{p^t}{{p^t}_r} \right)^d\end{aligned}\end{align} \]

1. If \(\phi = 0.0\), **d is reset to 0.0**.
2. **OUTPUT** The following information may be extracted for this material at a given integration point, using the OpenSees Element Recorder facility “stress”, “strain”, “backbone”, or “tangent”.

  - For 2D problems, the stress output follows this order: \(\sigma_{xx}\), \(\sigma_{yy}\), \(\sigma_{zz}\), \(\sigma_{xy}\),:math:eta_r, where \(\eta_r\) is the ratio between the shear (deviatoric) stress and peak shear strength at the current confinement \((0<=\eta_r<=1.0)\). The strain output follows this order: \(\epsilon_{xx}\), \(\epsilon_{yy}\), \(\epsilon_{xy}\)
  - For 3D problems, the stress output follows this order: \(\sigma_{xx}\), \(\sigma_{yy}\), \(\sigma_{zz}\), \(\sigma_{xy}\),:math:sigma_{yz}, \(\sigma_{zx}\), \(\eta_r\) and the strain output follows this order: \(\epsilon_{xx}\), \(\epsilon_{yy}\), \(\epsilon_{zz}\), \(\gamma_{xy}\), \(\gamma_{yz}\), \(\gamma_{zx}\)
  - The “backbone” option records (secant) shear modulus reduction curves at one or more given confinements. The specific recorder command is as follows:

```
recorder Element –ele $eleNum -file $fName -dT $deltaT material $GaussNum backbone $p1 <$p2 …>
```

where p1, p2, … are the confinements at which modulus reduction curves are recorded. In the output file, corresponding to each given confinement there are two columns: shear strain γ and secant modulus Gs. The number of rows equals the number of yield surfaces.

** SUGGESTED PARAMETER VALUES **

| Parameters | Soft Clay | Medium Clay | Stiff Clay |
| --- | --- | --- | --- |
| rho | 1.3 ton/m3 or 1.217x10-4(lbf)(s2)/in4 | 1.5 ton/m3 or 1.404x10-4(lbf)(s2)/in4 | 1.8 ton/m3 or 1.685x10-4(lbf)(s2)/in4 |
| refShearModul | 1.3x104kPa or 1.885x103psi | 6.0x104kPa or 8.702x104psi | 1.5x105kPa or 2.176x104 psi |
| refBulkModu | 6.5x104kPa or 9.427x103psi | 3.0x105kPa or 4.351x104psi | 7.5x105kPa or 1.088x105psi |
| cohesi | 18kPa or 2.611psi | 37kPa or 5.366psi | 75kPa or 10.878psi |
| peakShearStra (at p’r=80 kPa or 11.6 psi) | 0.1 | 0.1 | 0.1 |
| frictionAng | 0 | 0 | 0 |
| pressDependCoe | 0 | 0 | 0 |

** Pressure Dependent Multi Yield Examples **
