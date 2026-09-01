<!-- chunk_id: zeroLengthInterface2D_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/zeroLengthInterface2D.html",
 "title": "4.2.1.8. zeroLengthInterface2D",
 "category": "general",
 "command": "zeroLengthInterface2D",
 "doc_section": "src",
 "rel_path": "src/zeroLengthInterface2D.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1987,
 "word_count": 221,
 "has_code": false,
 "has_table": true
} -->

## 4.2.1.8. zeroLengthInterface2D

**element(*'zeroLengthInterface2D'*, *eleTag*, *'-sNdNum'*, *sNdNum*, *'-mNdNum'*, *mNdNum*, *'-dof'*, *sdof*, *mdof*, *'-Nodes'*, **NodesTags*, *kn*, *kt*, *phi*)**

| `eleTag` ([int](https://docs.python.org/3/library/functions.html#int)) | unique element object tag |
| --- | --- |
| `sNdNum` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of Slave Nodes |
| `mNdNum` ([int](https://docs.python.org/3/library/functions.html#int)) | Number of Master nodes |
| `sdof`, `mdof` ([int](https://docs.python.org/3/library/functions.html#int)) | Slave and Master degree of freedom |
| `NodesTags` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | Slave and master node tags respectively |
| `kn` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in normal direction |
| `kt` ([float](https://docs.python.org/3/library/functions.html#float)) | Penalty in tangential direction |
| `phi` ([float](https://docs.python.org/3/library/functions.html#float)) | Friction angle in degrees |

Note

1. The contact element is node-to-segment (NTS) contact. The relation follows Mohr-Coulomb frictional law: \(T = N \times \tan(\phi)\), where \(T\) is the tangential force, \(N\) is normal force across the interface and \(\phi\) is friction angle.
2. For 2D contact, slave nodes and master nodes must be 2 DOF and notice that the slave and master nodes must be entered in counterclockwise order.
3. The resulting tangent from the contact element is non-symmetric. Switch to the non-symmetric matrix solver if convergence problem is experienced.
4. As opposed to node-to-node contact, predefined normal vector for node-to-segment (NTS) element is not required because contact normal will be calculated automatically at each step.
5. contact element is implemented to handle large deformations.

See also

[Notes](http://opensees.berkeley.edu/wiki/index.php/ZeroLengthInterface2D)
