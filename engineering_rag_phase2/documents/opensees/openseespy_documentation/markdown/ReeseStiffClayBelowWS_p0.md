<!-- chunk_id: ReeseStiffClayBelowWS_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/ReeseStiffClayBelowWS.html",
 "title": "4.14.5.40.1.7. ReeseStiffClayBelowWS",
 "category": "general",
 "command": "ReeseStiffClayBelowWS",
 "doc_section": "src",
 "rel_path": "src/ReeseStiffClayBelowWS.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2195,
 "word_count": 295,
 "has_code": false,
 "has_table": true
} -->

## 4.14.5.40.1.7. ReeseStiffClayBelowWS

**hystereticBackbone(*'ReeseStiffClayBelowWS'*, *backboneTag*, *Esi*, *y50*, *As*, *Pc*)**

The backbone function is defined in this [manual](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml) in page 328

| `backboneTag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the backbone function. |
| --- | --- |
| `Esi` ([float](https://docs.python.org/3/library/functions.html#float)) | see below |
| `y50` ([float](https://docs.python.org/3/library/functions.html#float)) | see below |
| `As` ([float](https://docs.python.org/3/library/functions.html#float)) | see below |
| `Pc` ([float](https://docs.python.org/3/library/functions.html#float)) | see below |

#### 4.14.5.40.1.7.1. Esi

\(Esi = k_sx\)

where ks is the k value for static load selected from the
following table

The average shear strength should be computed from the shear strength of the soil to a depth of 5 pile diameters.
It should be defined as half the total maximum principal stress difference in an unconsolidated undrained triaxial
test.

| Average Undrained Shear Strength (ton/ft^2) | 0.5-1 | 1-2 | 2-4 |
| --- | --- | --- | --- |
| \(k_s`\) (Static) \(lb/in^3\) | 500 | 1000 | 2000 |

#### 4.14.5.40.1.7.2. y50

\(y_{50} = \varepsilon_{50} b\)

Use an appropriate value of \(\varepsilon_{50}\) from results of
laboratory tests or, in the absence of laboratory tests,
from the following table.

| Average Undrained Shear Strength (ton/ft^2) | 0.5-1 | 1-2 | 2-4 |
| --- | --- | --- | --- |
| \(\varepsilon_{50}`\) \(in/in\) | 0.007 | 0.005 | 0.004 |

#### 4.14.5.40.1.7.3. As

Choose the appropriate value of As from the following figure for the particular nondimensional depth.

#### 4.14.5.40.1.7.4. Pc

Compute the ultimate soil resistance per unit length of
pile, using the smaller of the values given by the
equations below

\[ \begin{align}\begin{aligned}p_{ct} = 2c_ab+\gamma'bx+2.83c_ax\\p_{cd} = 11cb\end{aligned}\end{align} \]

where

1. Obtain values for undrained soil shear strength \(c\), soil
submerged unit weight \(\gamma'\), and pile diameter \(b\)
2. Compute the average undrained soil shear strength \(c_a\)
over the depth \(x\).
