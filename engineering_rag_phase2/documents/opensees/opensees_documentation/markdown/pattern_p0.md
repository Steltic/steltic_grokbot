<!-- chunk_id: pattern_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern.html",
 "title": "3.1.12. Pattern Command",
 "category": "command_manual",
 "manual_group": "model",
 "command": "pattern",
 "doc_section": "user/manual/model",
 "rel_path": "user/manual/model/pattern.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2514,
 "word_count": 186,
 "has_code": false,
 "has_table": true
} -->

## 3.1.12. Pattern Command

The pattern command is used to construct a LoadPattern and add it to the Domain. Each LoadPattern in OpenSees has a TimeSeries associated with it. In addition it may contain ElementLoads, NodalLoads and SinglePointConstraints. Some of these SinglePoint constraints may be associated with GroundMotions.

The command has the following form:

**pattern patternType? arg1? arg2? ...**

| Argument | Type | Description |
| --- | --- | --- |
| $patternType | *string* | pattern type |
| $eleTag | *integer* | unique epattern tag. |
| $args | *list* | a list of args |

The type of pattern created and the additional arguments required depends on the patternType? provided in the command. The following contain information about patternType? and the additional args required for each of the available pattern types:

Fig. 3.1.12.1 OpenSees Loads

- [3.1.12.1. Plain Pattern](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/plainPattern.html)

  - [3.1.12.1.1. load Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/PlainPatternloadcommands/load.html)
  - [3.1.12.1.2. eleLoad Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/PlainPatternloadcommands/eleLoad.html)
  - [3.1.12.1.3. Sp Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/PlainPatternloadcommands/sp.html)
- [3.1.12.2. Uniform Excitation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/uniformExcitationPattern.html)
- [3.1.12.3. Multisupport Excitation](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/multiSupportPattern.html)

  - [3.1.12.3.1. Ground Motion](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/groundmotion/groundMotion.html)

    - [Plain Ground Motion](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/groundmotion/groundMotion.html#plain-ground-motion)
    - [Interpolated Ground Motion](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/groundmotion/groundMotion.html#interpolated-ground-motion)
  - [3.1.12.3.2. Imposed Motion Command](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/groundmotion/imposedMotion.html)
- [3.1.12.4. DRM Load Pattern](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/DRM.html)
- [3.1.12.5. H5DRM Pattern](https://OpenSees.github.io/OpenSeesDocumentation/user/manual/model/pattern/H5DRM.html)
