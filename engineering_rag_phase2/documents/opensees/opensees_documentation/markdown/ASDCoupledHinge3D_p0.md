<!-- chunk_id: ASDCoupledHinge3D_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/section/ASDCoupledHinge3D.html",
 "title": "3.1.7.4. ASDCoupledHinge3D",
 "category": "command_manual",
 "manual_group": "section",
 "command": "ASDCoupledHinge3D",
 "doc_section": "user/manual/section",
 "rel_path": "user/manual/section/ASDCoupledHinge3D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 5335,
 "word_count": 645,
 "has_code": false,
 "has_table": true
} -->

## 3.1.7.4. ASDCoupledHinge3D

This command is used to construct an ASDCoupledHinge3D section object.

It is a phenomenological section for lumped-plasticity modeling of RC beam-column elements that considers P-M-M interaction.

Internally it uses the Pinching4 material object for the moment-rotation responses in the My and Mz DOFs.

Using a P-M-M interaction domain, it internally updates the backbone curves of the My/Mz materials to account for P-M-M interaction.

**section ASDCoupledHinge3D $tag $Ktor $Kvy $Kvz? $Kax**

**-initialFlexuralStiffness $Ky $Kz**

**-thetaP $thetaPy $thetaPz**

**-thetaPC $thetaPCy $thetaPCz**

**<-simpleStrengthDomain $Nmin $Nmax $MyMax $MzMax $NMMax>**

**<-strengthDomainByPoints $nN $nTheta $listN $listMy $listMz>**

**<-hardening $as>**

**<-hystereticParams $rDispP $rForceP $uForceP $rDispN $rForceN $uForceN>**

**<-damageUnloadStiffness $gk1 $gk2 $gk3 $gk4 $gklim>**

**<-damageReloadStiffness $gd1 $gd2 $gd3 $gd4 $gdlim>**

**<-damageForce $gf1 $gf2 $gf3 $gf4 $gflim>**

**<-damageType $type $ge>**

| Argument | Type | Description |
| --- | --- | --- |
| $tag | *integer* | Unique tag identifying this section. |
| $Ktor $Kvy $Kvz? $Kax | 4 *float* | Mandatory. Penalty stiffnesses for torsional, shear-y, shear-z and axial responses respectively. |
| -initialFlexuralStiffness $Ky $Kz | *string* + 2 *string* | Mandatory. **-initialFlexuralStiffness**: A keyword preceding the 2 strings. **$Ky** and **$Kz**: Strings representing (currently Tcl only) expressions for the initial rotational stiffnesses. |
| -thetaP $thetaPy $thetaPz | *string* + 2 *string* | Mandatory. **-thetaP**: A keyword preceding the 2 strings. **$thetaPy** and **$thetaPz**: Strings representing (currently Tcl only) expressions for the pre-cap rotations. |
| -thetaPC $thetaPCy $thetaPCz | *string* + 2 *string* | Mandatory. **-thetaPC**: A keyword preceding the 2 strings. **$thetaPCy** and **$thetaPCz**: Strings representing (currently Tcl only) expressions for the post-cap rotations. |
| <-simpleStrengthDomain $Nmin $Nmax $MyMax $MzMax $NMMax> | *string* + 5 *float* | Optional. **-simpleStrengthDomain**: A keyword activating the use of the simplified interaction domain. **$Nmin** **$Nmax** **$MyMax** **$MzMax** **$NMMax**: Values for the simplified interaction domain representing the minimum axial strength, maximum axial strength, maximum My, maximum Mz and the value of axial coordinate of MyMax and MzMax. |
| <-strengthDomainByPoints $nN $nTheta $listN $listMy $listMz> | *string* + 2 *integer* + 3 *list* | Optional. **-strengthDomainByPoints**: A keyword activating the use of the interaction domain as a structured list of triplets (N, My, Mz). **$nN** **$nTheta**: 2 integers defining the number of points along the axial direction and the number of points along each My-Mz section. **$listN** **$listMy** **$listMz**: Lists of floats (size = nN * nTheta) for the N, My and Mz (respectively) coordinates of each point. Points are expected going from Nmin to Nmax. For each N coordinate, nTheta values (at constant N) of N My and Mz are expected going in ccw direction from the point N(i), My(max), Mz(zero). |
| <-hardening $as> | *string* + 1 *float* | Optional. **-hardening**: A keyword defining the hardening ratio. **$as**: Hardening ratio of Mu (ultimate moment) to My (yield moment). |
| <-hystereticParams $rDispP $rForceP $uForceP $rDispN $rForceN $uForceN> | *string* + 6 *float* | Optional. Same as those defined for Pinching4 material here: [https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material](https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material). |
| <-damageUnloadStiffness $gk1 $gk2 $gk3 $gk4 $gklim> | *string* + 5 *float* | Optional. Same as those defined for Pinching4 material here: [https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material](https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material). |
| <-damageReloadStiffness $gd1 $gd2 $gd3 $gd4 $gdlim> | *string* + 5 *float* | Optional. Same as those defined for Pinching4 material here: [https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material](https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material). |
| <-damageForce $gf1 $gf2 $gf3 $gf4 $gflim> | *string* + 5 *float* | Optional. Same as those defined for Pinching4 material here: [https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material](https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material). |
| <-damageType $type $ge> | *string* + *string* + *float* | Optional. Same as those defined for Pinching4 material here: [https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material](https://opensees.berkeley.edu/wiki/index.php/Pinching4_Material). |

Notes

- In the current implementation this section works only for the Tcl interpreter. The Python counterpart will be available soon.

Example 1 - Link to the live webinar

Webinar page: [https://asdea.eu/software/webinars/](https://asdea.eu/software/webinars/)

Link to youtube video: [https://www.youtube.com/live/C1iwsf7-mbU](https://www.youtube.com/live/C1iwsf7-mbU)

Example 2 - Simple Tcl example

[`ASDCoupledHinge3D_Example.tcl`](https://OpenSees.github.io/OpenSeesDocumentation/_downloads/27732a5f25b84b28b47a624985aac4cc/ASDCoupledHinge3D_Example.tcl)

Code Developed by: **Diego A. Talledo** at IUAV, Italy. **Massimo Petracca** at ASDEA Software, Italy.
