<!-- chunk_id: TEMPLATE_CBF_06ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_CBF_06ST",
 "system": "chevron_braced_frame",
 "storeys": 6,
 "base_condition": "pinned",
 "members": "col W14x145; beam W24x76; brace HSS8x8x1/2",
 "code": "ASCE7-22",
 "base_shear_kip": 580.0,
 "computed_T1_s": 0.982,
 "max_interstorey_drift": 0.00377,
 "modal_mass_mode1": 0.802,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_CBF_06ST

OpenSeesPy steel building template TEMPLATE_CBF_06ST: chevron_braced_frame, 6 storeys, regular, 30 ft bays, base pinned. Members: col W14x145; beam W24x76; brace HSS8x8x1/2. Designed/analysed to ASCE7-22. Seismic weight 2900 kip, Cs=0.2000, base shear 580.0 kip; computed period T1=0.982 s (Ta=0.525); max interstorey drift 0.00377; mode-1 modal mass 0.802. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# CBF_06ST — CBF 6-storey building template

2D lateral frame, regular 30 ft bays, members W14x145/W24x76/HSS8x8x1/2.

ASCE 7 seismic ELF (DAM 0.8E): W=2900 kip, Cs=0.2000, V=580 kip; computed T1=0.98s (Ta=0.52s); max interstorey drift 0.0038 (1/266); mode-1 modal mass 0.80.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

