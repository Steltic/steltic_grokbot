<!-- chunk_id: beamIntegration_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html",
 "title": "4.13. beamIntegration commands",
 "category": "beam_integration",
 "command": "beamIntegration",
 "doc_section": "src",
 "rel_path": "src/beamIntegration.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3161,
 "word_count": 172,
 "has_code": false,
 "has_table": false
} -->

## 4.13. beamIntegration commands

**beamIntegration(*type*, *tag*, **args*)**

A wide range of numerical integration options are available in OpenSees to represent distributed plasticity or non-prismatic section details in beam–column elements, i.e. along the element domain \([0, L]\).

For **distributed** rules such as [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html), [Legendre](https://openseespydoc.readthedocs.io/en/latest/src/Legendre.html), [Radau](https://openseespydoc.readthedocs.io/en/latest/src/Radau.html), [NewtonCotes](https://openseespydoc.readthedocs.io/en/latest/src/NewtonCotes.html), [Trapezoidal](https://openseespydoc.readthedocs.io/en/latest/src/Trapezoidal.html), and [CompositeSimpson](https://openseespydoc.readthedocs.io/en/latest/src/CompositeSimpson.html), two forms are supported: **prismatic** (one `secTag` and point count `N`) and **non-prismatic** (`N` then `N` section tags, node *I* to *J*). See [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html#lobatto-beamintegration).

Following are beamIntegration types available in the OpenSees:

Integration Methods for Distributed Plasticity.
Distributed plasticity methods permit yielding at any integration point along the element
length.

1. [Lobatto](https://openseespydoc.readthedocs.io/en/latest/src/Lobatto.html)
2. [Legendre](https://openseespydoc.readthedocs.io/en/latest/src/Legendre.html)
3. [NewtonCotes](https://openseespydoc.readthedocs.io/en/latest/src/NewtonCotes.html)
4. [Radau](https://openseespydoc.readthedocs.io/en/latest/src/Radau.html)
5. [Trapezoidal](https://openseespydoc.readthedocs.io/en/latest/src/Trapezoidal.html)
6. [CompositeSimpson](https://openseespydoc.readthedocs.io/en/latest/src/CompositeSimpson.html)
7. [UserDefined](https://openseespydoc.readthedocs.io/en/latest/src/userDefined.html)
8. [FixedLocation](https://openseespydoc.readthedocs.io/en/latest/src/FixedLocation.html)
9. [LowOrder](https://openseespydoc.readthedocs.io/en/latest/src/LowOrder.html)
10. [MidDistance](https://openseespydoc.readthedocs.io/en/latest/src/MidDistance.html)

Plastic Hinge Integration Methods. Plastic hinge integration methods confine material yielding to regions of the element of  specified length while the remainder of the element is linear elastic. A summary of plastic hinge integration methods is found in ([Scott and Fenves 2006](https://doi.org/10.1061/(ASCE)0733-9445(2006)132:2(244))).

1. [UserHinge](https://openseespydoc.readthedocs.io/en/latest/src/UserHinge.html)
2. [HingeMidpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeMidpoint.html)
3. [HingeRadau](https://openseespydoc.readthedocs.io/en/latest/src/HingeRadau.html)
4. [HingeRadauTwo](https://openseespydoc.readthedocs.io/en/latest/src/HingeRadauTwo.html)
5. [HingeEndpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeEndpoint.html)
6. [HingeEndpoint](https://openseespydoc.readthedocs.io/en/latest/src/HingeEndpoint.html)
7. [ConcentratedPlasticity](https://openseespydoc.readthedocs.io/en/latest/src/ConcentratedPlasticity.html)
8. [ConcentratedCurvature](https://openseespydoc.readthedocs.io/en/latest/src/ConcentratedCurvature.html)
