<!-- chunk_id: section_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/section.html",
 "title": "4.16. section commands",
 "category": "section",
 "command": "section",
 "doc_section": "src",
 "rel_path": "src/section.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2555,
 "word_count": 172,
 "has_code": true,
 "has_table": true
} -->

## 4.16. section commands

**section(*secType*, *secTag*, **secArgs*)**

This command is used to construct a SectionForceDeformation object, hereto referred to as Section, which represents force-deformation (or resultant stress-strain) relationships at beam-column and plate sample points.

| `secType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | section type |
| --- | --- |
| `secTag` ([int](https://docs.python.org/3/library/functions.html#int)) | section tag. |
| `secArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of section arguments, must be preceded with `*`. |

For example,

```
secType = 'Elastic'
secTag = 1
secArgs = [E, A, Iz]
section(secType, secTag, *secArgs)
```

Note

Valid queries for many sections when using an element recorder include `force` and `deformation`; some sections support more (see each section’s notes). For fiber output (e.g. `stressStrain`) and `sectionX` recorders, see [element recorder command](https://openseespydoc.readthedocs.io/en/latest/src/elementRecorder.html#elementrecorder).

The following contain information about available `secType`:

1. [Elastic Section](https://openseespydoc.readthedocs.io/en/latest/src/elasticSection.html)
2. [Fiber Section](https://openseespydoc.readthedocs.io/en/latest/src/fibersection.html)
3. [NDFiber Section](https://openseespydoc.readthedocs.io/en/latest/src/ndfiber.html)
4. [Wide Flange Section](https://openseespydoc.readthedocs.io/en/latest/src/wfsection2d.html)
5. [RC Section](https://openseespydoc.readthedocs.io/en/latest/src/rcsection2d.html)
6. [RCCircular Section](https://openseespydoc.readthedocs.io/en/latest/src/rccircularsection.html)
7. [Parallel Section](https://openseespydoc.readthedocs.io/en/latest/src/parallelsection.html)
8. [Section Aggregator](https://openseespydoc.readthedocs.io/en/latest/src/sectionaggregator.html)
9. [Uniaxial Section](https://openseespydoc.readthedocs.io/en/latest/src/uniaxialsection.html)
10. [Elastic Membrane Plate Section](https://openseespydoc.readthedocs.io/en/latest/src/elasticMembranePlateSection.html)
11. [Plate Fiber Section](https://openseespydoc.readthedocs.io/en/latest/src/plateFiberSection.html)
12. [Bidirectional Section](https://openseespydoc.readthedocs.io/en/latest/src/bidirectionalSection.html)
13. [Isolator2spring Section](https://openseespydoc.readthedocs.io/en/latest/src/isolatorsection.html)
14. [LayeredShell](https://openseespydoc.readthedocs.io/en/latest/src/LayeredShell.html)
15. [Pipe Section](https://openseespydoc.readthedocs.io/en/latest/src/pipeSection.html)
