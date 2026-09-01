<!-- chunk_id: TEMPLATE_MF_03ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_MF_03ST",
 "system": "moment_frame",
 "storeys": 3,
 "base_condition": "fixed",
 "members": "col W14x90; beam W24x55",
 "code": "ASCE7-22",
 "base_shear_kip": 280.0,
 "computed_T1_s": 1.121,
 "max_interstorey_drift": 0.00925,
 "modal_mass_mode1": 0.858,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_MF_03ST

OpenSeesPy steel building template TEMPLATE_MF_03ST: moment_frame, 3 storeys, regular, 30 ft bays, base fixed. Members: col W14x90; beam W24x55. Designed/analysed to ASCE7-22. Seismic weight 1400 kip, Cs=0.2000, base shear 280.0 kip; computed period T1=1.121 s (Ta=0.525); max interstorey drift 0.00925; mode-1 modal mass 0.858. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# MF_03ST — MF 3-storey building template

2D lateral frame, regular 30 ft bays, members W14x90/W24x55.

ASCE 7 seismic ELF (DAM 0.8E): W=1400 kip, Cs=0.2000, V=280 kip; computed T1=1.12s (Ta=0.52s); max interstorey drift 0.0092 (1/108); mode-1 modal mass 0.86.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

