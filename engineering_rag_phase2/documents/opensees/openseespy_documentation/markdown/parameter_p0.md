<!-- chunk_id: parameter_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/parameter.html",
 "title": "9.1. parameter command",
 "category": "general",
 "command": "parameter",
 "doc_section": "src",
 "rel_path": "src/parameter.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1457,
 "word_count": 214,
 "has_code": true,
 "has_table": true
} -->

## 9.1. parameter command

**parameter(*tag*, *<specific parameter args>*)**

In DDM-based FE response sensitivity analysis, the sensitivity parameters can be material,
geometry or discrete loading parameters.

| `tag` ([int](https://docs.python.org/3/library/functions.html#int)) | integer tag identifying the parameter. |
| --- | --- |
| `<specific parameter args>` | depend on the object in the FE model encapsulating the desired parameters. |

Note

Each parameter must be unique in the FE domain, and all parameter tags must be numbered sequentially starting from 1.

#### 9.1.1. Examples

1. To identify the elastic modulus, E, of the material 1 at section 3 of element 4, the <specific object arguments> string becomes:

  ```
  parameter(1, 'element', 4, 'section', 3, 'material', 1, 'E')
  ```
2. To identify the elastic modulus, E, of elastic section 3 of element 4 (for elastic section, no specific material need to be defined), the <specific object arguments> string becomes:

  ```
  parameter(1, 'element', 4, 'section', 3, 'E')
  ```
3. To parameterize E for element 4 with material 1 (no section need to be defined), the <specific object arguments> string simplifies as:

  ```
  parameter(1, 'element', 4, 'material', 1, 'E')
  ```

Note

Notice that the format of the <specific object arguments> is different for each considered element/section/material. The specific set of parameters and the relative <specific object arguments> format will be added in the future.
