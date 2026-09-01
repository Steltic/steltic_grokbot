<!-- chunk_id: elementalDamping_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping.html",
 "title": "3.1.13.3. Elemental Damping Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "elementalDamping",
 "doc_section": "user/manual/model/damping",
 "rel_path": "user/manual/model/damping/elementalDamping.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2788,
 "word_count": 350,
 "has_code": true,
 "has_table": true
} -->

## 3.1.13.3. Elemental Damping Command

**damping $dampingType $dampingTag $dampingArgs**

| Argument | Type | Description |
| --- | --- | --- |
| $dampingType | *string* | damping type |
| $dampingTag | *integer* | unique damping tag. |
| $dampingArgs | *list* | a list of damping arguments with number dependent on damping type |

The following subsections contain information about **$dampingType**

> - [3.1.13.3.1. Uniform Damping](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping/UniformDamping.html)
> - [3.1.13.3.2. Universal Rate-Dependent (URD) Damping](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping/URDDamping.html)
> - [3.1.13.3.3. Secant Stiffness-Proportional Damping](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/damping/elementalDamping/SecStifDamping.html)

The following is used to assign the damping model to a specific element. The user should append the parameters of **“-damp $dampingTag”** to the end of the element definition.

> ```
> element dispBeamColumn $eleTag $iNode $jNode $numIntgrPts $secTag $transfTag <-damp $dampingTag>
>
> element ASDShellQ4 $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element ShellDKGQ $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element ShellDKGT $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element ShellNLDKGQ $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element ShellNLDKGT $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampingTag>
>
> element zeroLength $eleTag $iNode $jNode -mat $matTag1 $matTag2 ... -dir $dir1 $dir2 ...<-doRayleigh $rFlag> <-orient $x1 $x2 $x3 $yp1 $yp2 $yp3> <-damp $dampingTag>
>
> element elasticBeamColumn $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $transfTag <-mass $massDens> <-cMass> <-damp $dampingTag>
>
> element forceBeamColumn $eleTag $iNode $jNode $transfTag "IntegrationType arg1 arg2 ..." <-mass $massDens> <-iter $maxIters $tol> <-damp $dampingTag>
>
> element quad $eleTag $iNode $jNode $kNode $lNode $thick $type $matTag <$pressure $rho $b1 $b2> <-damp $dampingTag>
>
> element stdBrick $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $matTag <$b1 $b2 $b3> <-damp $dampingTag>
> ```

The following is used to assign the damping model to groups of elements.

> ```
> region $regTag <-ele ($ele1 $ele2 ...)> <-eleOnly ($ele1 $ele2 ...)> <-eleRange $startEle $endEle> <-eleOnlyRange $startEle $endEle> <-node ($node1 $node2 ...)> <-nodeOnly ($node1 $node2 ...)> <-nodeRange $startNode $endNode> <-nodeOnlyRange $startNode $endNode> <-node all> <-rayleigh $alphaM $betaK $betaKinit $betaKcomm> <-damp $dampingTag>
> ```
