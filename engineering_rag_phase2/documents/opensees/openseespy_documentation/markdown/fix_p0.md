<!-- chunk_id: fix_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/fix.html",
 "title": "4.4.1. fix command",
 "category": "general",
 "command": "fix",
 "doc_section": "src",
 "rel_path": "src/fix.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 497,
 "word_count": 58,
 "has_code": true,
 "has_table": true
} -->

## 4.4.1. fix command

**fix(*nodeTag*, **constrValues*)**

Create a homogeneous SP constriant.

| `nodeTag` ([int](https://docs.python.org/3/library/functions.html#int)) | tag of node to be constrained |
| --- | --- |
| `constrValues` ([list](https://docs.python.org/3/library/stdtypes.html#list) ([int](https://docs.python.org/3/library/functions.html#int))) | a list of constraint values (0 or 1), must be preceded with `*`. `0` free `1` fixed |

For example,

```
# fully fixed
vals = [1,1,1]
fix(nodeTag, *vals)
```
