<!-- chunk_id: TEMPLATE_MF_06ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_MF_06ST",
 "system": "moment_frame",
 "storeys": 6,
 "base_condition": "fixed",
 "members": "col W14x145; beam W24x76",
 "code": "ASCE7-22",
 "base_shear_kip": 380.8,
 "computed_T1_s": 1.79,
 "max_interstorey_drift": 0.00968,
 "modal_mass_mode1": 0.826,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_MF_06ST

OpenSeesPy steel building template TEMPLATE_MF_06ST: moment_frame, 6 storeys, regular, 30 ft bays, base fixed. Members: col W14x145; beam W24x76. Designed/analysed to ASCE7-22. Seismic weight 2900 kip, Cs=0.1313, base shear 380.8 kip; computed period T1=1.790 s (Ta=0.914); max interstorey drift 0.00968; mode-1 modal mass 0.826. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# MF_06ST — MF 6-storey building template

2D lateral frame, regular 30 ft bays, members W14x145/W24x76.

ASCE 7 seismic ELF (DAM 0.8E): W=2900 kip, Cs=0.1313, V=381 kip; computed T1=1.79s (Ta=0.91s); max interstorey drift 0.0097 (1/103); mode-1 modal mass 0.83.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

