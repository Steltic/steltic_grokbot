<!-- chunk_id: ProfileSPD_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/system/ProfileSPD.html",
 "title": "3.2.3.3. ProfileSPD System",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "ProfileSPD",
 "doc_section": "user/manual/analysis/system",
 "rel_path": "user/manual/analysis/system/ProfileSPD.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1779,
 "word_count": 298,
 "has_code": true,
 "has_table": false
} -->

## 3.2.3.3. ProfileSPD System

This command is used to construct a ProfileSPD linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems. The matrix is stored as shown below in a 1 dimensional array with only those values below the first non-zero row in any column being stored. This is sometimes also referred to as a skyline storage scheme. The following command is used to construct such a system:

**system ProfileSPD**

An n×n matrix A= is a symmetric positive definite matrix if:

1. \(a_{i,j} = a_{j,i}\)
2. \(y^T A y != 0\) for all non-zero vectors y with real entries (\(y \in \mathbb{R}^n\)).

In the skyline or profile storage scheme only the entries below the first no-zero row entry in any column are stored if storing by rows: The reason for this is that as no reordering of the rows is required in gaussian eleimination because the matrix is SPD, no non-zero entries will ocur in the elimination process outside the area stored.

For example, a symmetric 6-by-6 matrix with a structure as shown below:

\[\begin{split}\begin{bmatrix}
A_{11} & A_{12} & 0      &   0    & 0     \\
& A_{22}  & A_{23}  &  0     & A_{25} \\
&         & A_{33}  & 0      & 0     \\
&         &         & A_{44} & A_{45} \\
& sym     &         &        & A_{55}
\end{bmatrix}\end{split}\]

The matrix is stored as 1-d array

\[\begin{bmatrix}
A_{11} & A_{12} & A_{22} & A_{23} & A_{33} & A_{44} & A_{25} &  0 & A_{45} & A_{55}
\end{bmatrix}\]

with a further array containing indices of diagonal elements:

\[\begin{bmatrix}
1 & 3 & 5 & 6 & 10
\end{bmatrix}\]

Example

The following example shows how to construct a ProfileSPD system

1. **Tcl Code**

```
system ProfileSPD
```

1. **Python Code**

```
system('ProfileSPD')
```

Code Developed by: **fmk**
