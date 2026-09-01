<!-- chunk_id: outputcmds_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/outputcmds.html",
 "title": "6. Output Commands",
 "category": "output",
 "command": "outputcmds",
 "doc_section": "src",
 "rel_path": "src/outputcmds.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 4652,
 "word_count": 158,
 "has_code": false,
 "has_table": false
} -->

## 6. Output Commands

Get outputs from OpenSees. These commands don’t change internal states of OpenSees.

1. [basicDeformation command](https://openseespydoc.readthedocs.io/en/latest/src/basicDeformation.html)
2. [basicForce command](https://openseespydoc.readthedocs.io/en/latest/src/basicForce.html)
3. [basicStiffness command](https://openseespydoc.readthedocs.io/en/latest/src/basicStiffness.html)
4. [eleDynamicalForce command](https://openseespydoc.readthedocs.io/en/latest/src/eleDynamicalForce.html)
5. [eleForce command](https://openseespydoc.readthedocs.io/en/latest/src/eleForce.html)
6. [eleNodes command](https://openseespydoc.readthedocs.io/en/latest/src/eleNodes.html)
7. [eleResponse command](https://openseespydoc.readthedocs.io/en/latest/src/eleResponse.html)
8. [getConstrainedDOFs command](https://openseespydoc.readthedocs.io/en/latest/src/getConstrainedDOFs.html)
9. [getConstrainedNodes command](https://openseespydoc.readthedocs.io/en/latest/src/getConstrainedNodes.html)
10. [getEleTags command](https://openseespydoc.readthedocs.io/en/latest/src/getEleTags.html)
11. [getFixedDOFs command](https://openseespydoc.readthedocs.io/en/latest/src/getFixedDOFs.html)
12. [getFixedNodes command](https://openseespydoc.readthedocs.io/en/latest/src/getFixedNodes.html)
13. [getLoadFactor command](https://openseespydoc.readthedocs.io/en/latest/src/getLoadFactor.html)
14. [getNodeTags command](https://openseespydoc.readthedocs.io/en/latest/src/getNodeTags.html)
15. [getRetainedDOFs command](https://openseespydoc.readthedocs.io/en/latest/src/getRetainedDOFs.html)
16. [getRetainedNodes command](https://openseespydoc.readthedocs.io/en/latest/src/getRetainedNodes.html)
17. [getTime command](https://openseespydoc.readthedocs.io/en/latest/src/getTime.html)
18. [nodeAccel command](https://openseespydoc.readthedocs.io/en/latest/src/nodeAccel.html)
19. [nodeBounds command](https://openseespydoc.readthedocs.io/en/latest/src/nodeBounds.html)
20. [nodeCoord command](https://openseespydoc.readthedocs.io/en/latest/src/nodeCoord.html)
21. [nodeDisp command](https://openseespydoc.readthedocs.io/en/latest/src/nodeDisp.html)
22. [nodeEigenvector command](https://openseespydoc.readthedocs.io/en/latest/src/nodeEigenvector.html)
23. [nodeDOFs command](https://openseespydoc.readthedocs.io/en/latest/src/nodeDOFs.html)
24. [nodeMass command](https://openseespydoc.readthedocs.io/en/latest/src/nodeMass.html)
25. [nodePressure command](https://openseespydoc.readthedocs.io/en/latest/src/nodePressure.html)
26. [nodeReaction command](https://openseespydoc.readthedocs.io/en/latest/src/nodeReaction.html)
27. [nodeResponse command](https://openseespydoc.readthedocs.io/en/latest/src/nodeResponse.html)
28. [nodeVel command](https://openseespydoc.readthedocs.io/en/latest/src/nodeVel.html)
29. [nodeUnbalance command](https://openseespydoc.readthedocs.io/en/latest/src/nodeUnbalance.html)
30. [numFact command](https://openseespydoc.readthedocs.io/en/latest/src/numFact.html)
31. [numIter command](https://openseespydoc.readthedocs.io/en/latest/src/numIter.html)
32. [printA command](https://openseespydoc.readthedocs.io/en/latest/src/printA.html)
33. [printB command](https://openseespydoc.readthedocs.io/en/latest/src/printB.html)
34. [printGID command](https://openseespydoc.readthedocs.io/en/latest/src/printGID.html)
35. [printModel command](https://openseespydoc.readthedocs.io/en/latest/src/printModel.html)
36. [record command](https://openseespydoc.readthedocs.io/en/latest/src/record.html)
37. [recorder command](https://openseespydoc.readthedocs.io/en/latest/src/recorder.html)
38. [sectionForce command](https://openseespydoc.readthedocs.io/en/latest/src/sectionForce.html)
39. [sectionDeformation command](https://openseespydoc.readthedocs.io/en/latest/src/sectionDeformation.html)
40. [sectionStiffness command](https://openseespydoc.readthedocs.io/en/latest/src/sectionStiff.html)
41. [sectionFlexibility command](https://openseespydoc.readthedocs.io/en/latest/src/sectionFlexibility.html)
42. [sectionLocation command](https://openseespydoc.readthedocs.io/en/latest/src/sectionLocation.html)
43. [sectionWeight command](https://openseespydoc.readthedocs.io/en/latest/src/sectionWeight.html)
44. sectionTag
45. [systemSize command](https://openseespydoc.readthedocs.io/en/latest/src/systemSize.html)
46. [testIter command](https://openseespydoc.readthedocs.io/en/latest/src/testIter.html)
47. [testNorm command](https://openseespydoc.readthedocs.io/en/latest/src/testNorm.html)
48. [version command](https://openseespydoc.readthedocs.io/en/latest/src/version.html)
49. [logFile command](https://openseespydoc.readthedocs.io/en/latest/src/logFile.html)
