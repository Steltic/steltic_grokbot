<!-- chunk_id: frictionModel_p0 | collection: openseespy_documentation -->
<!-- meta: {
 "source": "openseespy",
 "source_file": "openseespy_documentation.md",
 "source_url": "https://openseespydoc.readthedocs.io/en/latest/src/frictionModel.html",
 "title": "4.17. frictionModel commands",
 "category": "friction_model",
 "command": "frictionModel",
 "doc_section": "src",
 "rel_path": "src/frictionModel.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 1373,
 "word_count": 129,
 "has_code": true,
 "has_table": true
} -->

## 4.17. frictionModel commands

**frictionModel(*frnType*, *frnTag*, **frnArgs*)**

The frictionModel command is used to construct a friction model object, which specifies the behavior of the coefficient of friction in terms of the absolute sliding velocity and the pressure on the contact area. The command has at least one argument, the friction model type.

| `frnType` ([str](https://docs.python.org/3/library/stdtypes.html#str)) | frictionModel type |
| --- | --- |
| `frnTag` ([int](https://docs.python.org/3/library/functions.html#int)) | frictionModel tag. |
| `frnArgs` ([list](https://docs.python.org/3/library/stdtypes.html#list)) | a list of frictionModel arguments, must be preceded with `*`. |

For example,

```
frnType = 'Coulomb'
frnTag = 1
frnArgs = [mu]
frictionModel(frnType, frnTag, *frnArgs)
```

The following contain information about available `frnType`:

1. [Coulomb](https://openseespydoc.readthedocs.io/en/latest/src/Coulomb.html)
2. [Velocity Dependent Friction](https://openseespydoc.readthedocs.io/en/latest/src/veldependent.html)
3. [Velocity and Normal Force Dependent Friction](https://openseespydoc.readthedocs.io/en/latest/src/velnormal.html)
4. [Velocity and Pressure Dependent Friction](https://openseespydoc.readthedocs.io/en/latest/src/velpressure.html)
5. [Multi-Linear Velocity Dependent Friction](https://openseespydoc.readthedocs.io/en/latest/src/velmulti.html)
