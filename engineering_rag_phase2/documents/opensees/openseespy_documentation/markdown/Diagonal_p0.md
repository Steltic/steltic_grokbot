<!-- chunk_id: Diagonal_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/Diagonal.html",
 "title": "5.3.8. Diagonal System",
 "category": "analysis",
 "command": "Diagonal",
 "doc_section": "src",
 "rel_path": "src/Diagonal.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3987,
 "word_count": 570,
 "has_code": true,
 "has_table": false
} -->

## 5.3.8. Diagonal System

This command is used to construct a Diagonal linear system of equation object. This system stores only the diagonal entries of the coefficient matrix, making it extremely memory efficient for problems where off-diagonal coupling can be neglected or lumped into the diagonal. The system is solved by direct inversion of the diagonal entries. The following command is used to construct such a system:

**system(*'Diagonal'*, *<-'lumped'>*)**

**Optional Parameter:**

- **-lumped** - If specified, off-diagonal matrix entries are added (lumped) to the diagonal before solving. This is useful for mass matrix lumping or when converting a coupled system to a diagonal approximation.

A diagonal system stores only the diagonal entries of an n×n matrix **A**, where:

\(K = \begin{bmatrix} k_{11} & 0 & \cdots & 0 \\ 0 & k_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & k_{nn} \end{bmatrix}\)

The solution for \(K u = f\) is obtained directly as:

\(u_i = \frac{f_i}{k_{ii}} \quad \text{for } i = 1, \ldots, n\)

Note

1. This solver requires that all diagonal entries are non-zero.
2. The system only stores n values instead of n² for a full matrix, providing significant memory savings
3. When using the **-lumped** option, the solver accumulates all off-diagonal entries in each row/column into the corresponding diagonal entry

#### 5.3.8.1. Mass Lumping

When the **-lumped** option is specified, the Diagonal system performs **mass lumping** (also called diagonal lumping or row-sum lumping). This technique converts a consistent (coupled) mass matrix into a diagonal form by summing all entries in each row and placing the total on the diagonal.

**Mathematical Formulation:**

For a consistent mass matrix **M** with entries \(m_{ij}\), the lumped diagonal entry is:

\(\tilde{m}_{ii} = \sum_{j=1}^{n} m_{ij}\)

All off-diagonal entries are set to zero: \(\tilde{m}_{ij} = 0\) for \(i \neq j\)

Warning

1. This system is only appropriate when the problem structure allows diagonal treatment
2. Mass lumping is generally only recommended for the mass matrix in dynamic analysis (ExplicitDifference integrator or CentralDifference integrator if no damping matrix is used or only mass proportional Rayleigh damping is used)
3. Lumping the stiffness matrix is rarely appropriate and can lead to poor results
4. For static analysis or implicit dynamics use full sparse solvers.
5. Ideally, lumping should be handled at the element level, especially for high-order elements (like the TenNodeTetrahedron or SixNodeTriangle) where this technique leads to negative mass values (!!).

**Implementation Details:**

When **-lumped** is specified:

```
For each element matrix entry m(i,j) at DOF locations id(i), id(j):
   A[id(i)] += m(i,i)           // Add diagonal entry
   if (lumped):
      for all j ≠ i:
         A[id(i)] += m(j,i)     // Add all column entries to diagonal
```

This ensures that the total contribution from each element is preserved while creating a diagonal system.

Example

The following examples show how to construct a Diagonal system

**1. Python Code - Basic diagonal system**

```
import openseespy.opensees as ops

ops.system('Diagonal')
```

**2. Python Code - Lumped mass for explicit analysis**

```
import openseespy.opensees as ops

# Setup for explicit central difference method
ops.system('Diagonal', '-lumped')
ops.constraints('Plain')
ops.numberer('Plain')
ops.integrator('CentralDifference')
ops.analysis('Transient')
```

**3. Python Code - Complete explicit dynamics example**

```
import openseespy.opensees as ops

# ... model definition ...

# Analysis setup for blast/impact with lumped mass
ops.system('Diagonal', '-lumped')
ops.constraints('Plain')
ops.numberer('Plain')
ops.test('NormDispIncr', 1.0e-6, 10, 0)
ops.algorithm('Linear')
ops.integrator('CentralDifference')
ops.analysis('Transient')

# Time step (must satisfy CFL condition)
dt = 0.0001
ops.analyze(1000, dt)
```

Code Developed by: **Frank McKenna**
