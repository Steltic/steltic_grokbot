<!-- chunk_id: HystereticSM_p1 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/material/uniaxialMaterials/HystereticSM.html",
 "title": "3.1.5.17. HystereticSM Material",
 "category": "command_manual",
 "manual_group": "material",
 "command": "HystereticSM",
 "doc_section": "user/manual/material/uniaxialMaterials",
 "rel_path": "user/manual/material/uniaxialMaterials/HystereticSM.html",
 "part_index": 1,
 "part_count": 2,
 "char_count": 5614,
 "word_count": 694,
 "has_code": false,
 "has_table": false
} -->

## 3.1.5.17. HystereticSM Material [part 2/2]

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0

*HystereticSM_damage1=0.01*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0.01, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.01  0

*HystereticSM_damage1=0.1*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0.1, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.1  0

#### 3.1.5.17.8. Parameter Study: Damage2

*HystereticSM_damage2=0*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0

*HystereticSM_damage2=0.01*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0, 0.01)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.01

*HystereticSM_damage2=0.1*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0, 0.1)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.1

#### 3.1.5.17.9. Parameter Study: beta

*HystereticSM_beta=0*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-beta’, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0

*HystereticSM_beta=0.5*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-beta’, 0.5)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0.5

*HystereticSM_beta=1*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-beta’, 1)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  1

#### 3.1.5.17.10. Parameter Study: degEng

*HystereticSM_degEnv=0*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0.005, 0.002, ‘-degEnv’, 0, 0)

#### 3.1.5.17.11. uniaxialMaterial HystereticSM 99 -posEnv 2772.0 0.01 3104.6 0.02 1663.2 0.04 1663.2 0.06 277.2 0.08 200.0 0.1 0 0.12 -negEnv -2772.0 -0.01 -3104.6 -0.02 -1663.2 -0.04 -damage 0.005 0.002 -degEnv 0 0

*HystereticSM_degEnv=1*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0.005, 0.002, ‘-degEnv’, 1, -1)

#### 3.1.5.17.12. uniaxialMaterial HystereticSM 99 -posEnv 2772.0 0.01 3104.6 0.02 1663.2 0.04 1663.2 0.06 277.2 0.08 200.0 0.1 0 0.12 -negEnv -2772.0 -0.01 -3104.6 -0.02 -1663.2 -0.04 -damage 0.005 0.002 -degEnv 1 -1

*HystereticSM_degEnv=5*
ops.uniaxialMaterial(‘HystereticSM’, 99, ‘-posEnv’, 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, ‘-negEnv’, -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, ‘-damage’, 0.005, 0.002, ‘-degEnv’, 5, -5)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.005  0.002  -degEnv  5  -5

Modified Code Developed by: [Silvia Mazzoni](https://www.silviasbrainery.com/)

Original Hysteretic-Material Code Developed by: [Michael H. Scott](https://cce.oregonstate.edu/scott) & Filip Filippou (UC Berkeley)
