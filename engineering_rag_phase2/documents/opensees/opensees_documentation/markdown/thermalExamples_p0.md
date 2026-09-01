<!-- chunk_id: thermalExamples_p0 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples.html",
 "title": "4.2. Thermal Examples",
 "category": "examples",
 "manual_group": "",
 "command": "thermalExamples",
 "doc_section": "user/examples",
 "rel_path": "user/examples/thermalExamples.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 3224,
 "word_count": 413,
 "has_code": false,
 "has_table": false
} -->

## 4.2. Thermal Examples

- [4.2.1. Example 1](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples/thermalexample1.html)
- [4.2.2. Example 2](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples/thermalexample2.html)
- [4.2.3. Example 3](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples/thermalexample3.html)
- [4.2.4. Example 4](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples/thermalexample4.html)
- [4.2.5. Example 5](https://OpenSees.github.io/OpenSeesDocumentation/user/examples/thermalExamples/thermalexample5.html)

**Structural Fire Engineering**

The following types of fire analyses are represented in these examples. The fire analysis is performed is a stress-based analysis where the temperature of the elements is set within the code. Heat transfer analysis between the gas temperatures and the structural member should be performed using lump mass heat transfer analysis techniques or appropriate finite element programs.

#### 4.2.6. Target temperature

The temperature of the elements are set and a linear time-temperature curve is assumed for each element to reach the set temperature over the time period of the step.

#### 4.2.7. Standard fire curve

The standard fire curve is defined by ASTM E119 and ISO 834. These two curves are essentially the same and are used for standardized fire testing. These time-temperature curves increase rapidly at the beginning and then steadily increase over a time period of eight hours.

#### 4.2.8. Parametric time-temperature fire curve

When the research involves structural fire engineering, a parametric time-temperature curve that is based on Eurocode 1 may be required. This time-temperature curve is dependent upon the ventilation (openings) in the compartment, the material of the compartment, the fuel load density, and the size of the compartment. These factors combined will produce a time-temperature curve that characterizes the fire in the compartment under consideration. The shape of this curve and the maximum temperature is highly dependent upon all of the factors previously listed. This type of fire curve will also include a cooling portion of the fire, when all of the fuel has been consumed. This type of fire time-temperature curve is used when a complete burn out fire scenario is being investigated.

#### 4.2.9. Simulation process

Each example script does the following:

**Build the model**

1. Model dimensions and degress-of-freedom
2. Nodal coordinates
3. Nodal constraints – boundary conditions
4. Nodal masses
5. Elements and element connectivity
6. Set element temperatures
7. Recorders for output

**Define and apply gravity load**

1. Nodal or element load
2. Static-analysis parameters (tolerances and load increments)
3. Analyze
4. Hold gravity loads constant
5. Reset time to zero

**Define and apply element temperatures**

1. Load pattern (nodal loads for gravity analysis and temperature patterns for fire)
2. Provide temperature history for the loads either through a set temperature or reference to a time-temperature curve
3. Analyze

#### 4.2.10. Author Info

- [Dr. Erica Fischer](https://www.ericafischer.org/)
- Walker Maddalozzo
