<!-- chunk_id: DisplacementControl_p0_2 | collection: opensees_documentation -->
<!-- meta: {
 "source": "opensees_documentation.md",
 "source_url": "https://OpenSees.github.io/OpenSeesDocumentation/user/manual/analysis/integrator/DisplacementControl.html",
 "title": "3.2.6.2. DisplacementControl Command",
 "category": "command_manual",
 "manual_group": "analysis",
 "command": "DisplacementControl",
 "doc_section": "user/manual/analysis/integrator",
 "rel_path": "user/manual/analysis/integrator/DisplacementControl.html",
 "part_index": 0,
 "part_count": 1,
 "char_count": 2466,
 "word_count": 375,
 "has_code": false,
 "has_table": true
} -->

## 3.2.6.2. DisplacementControl Command

This command is used to construct a DisplacementControl integrator object. In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

**integrator DisplacementControl $node $dof $incr <$numIter :math`\Delta U \text{min}` $:math:\Delta U \text{max}`>**

| Argument | Type | Description |
| --- | --- | --- |
| $node | *integer* | node whose response controls solution |
|  |  |  |
| $dof | *integer* | degree of freedom at the node; valid options: 1 through ndf at node. |
| $incr | *float* | first displacement increment <math>Delta U_{text{dof}}</math> |
| $numIter | *integer* | the number of iterations the user would like to occur in the solution algorithm. Optional; default = 1.0. |
| $dUmin | *float* | the min step size the user will allow. optional; default \(\Delta U_{min} = \Delta U_0\) |
| $dUmax | *float* | the max step size the user will allow. optional: default \(\Delta U_{max} = \Delta U_0\) |

\(f(x_n+\Delta x) = 0\)

integrator DisplacementControl 1 2 0.1; # displacement control algorithm seeking constant increment of 0.1 at node 1 at 2’nd dof.

#### 3.2.6.2.1. Theory

If we write the governing finite element equation at :math:`t + Delta t` as:

\[R(U_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta t} F^{ext} - F(U_{t+\Delta t}) \!`\]

where \(F(U_{t+\Delta t})\!\) are the internal forces which are a function of the displacements \(U_{t+\Delta t}\!\), \(F^{ext}\!\) is the set of reference loads and \(\lambda\!\) is the load multiplier. Linearizing the equation results in:

\[K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left ( \lambda^i_{t+\Delta t} + \Delta \lambda^i \right ) F^{ext} - F(U_{t+\Delta t})\]

This equation represents n equations in \(n+1\) unknowns, and so an additional equation is needed to solve the equation. For displacement control, we introduce a new constraint equation in which in each analysis step we set to ensure that the displacement increment for the degree-of-freedom <math>text{dof}</math> at the specified node is:

\[\Delta U_\text{dof} = \text{incr}\!</math>\]

MORE TO COME:

In Displacement Control the \(\Delta_U\text{dof}\) set to \(t + \lambda_{t+1}\) where,

\(\Delta U_\text{dof}^{t+1} = \max \left ( \Delta U_{min}, \min \left ( \Delta U_\text{max}, \frac{\text{numIter}}{\text{lastNumIter}} \Delta U_\text{dof}^{t} \right ) \right )\)
