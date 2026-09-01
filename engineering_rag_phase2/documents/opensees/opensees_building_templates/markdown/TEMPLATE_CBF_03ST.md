<!-- chunk_id: TEMPLATE_CBF_03ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_CBF_03ST",
 "system": "chevron_braced_frame",
 "storeys": 3,
 "base_condition": "pinned",
 "members": "col W14x90; beam W24x55; brace HSS6x6x3/8",
 "code": "ASCE7-22",
 "base_shear_kip": 280.0,
 "computed_T1_s": 0.595,
 "max_interstorey_drift": 0.00252,
 "modal_mass_mode1": 0.9,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_CBF_03ST

OpenSeesPy steel building template TEMPLATE_CBF_03ST: chevron_braced_frame, 3 storeys, regular, 30 ft bays, base pinned. Members: col W14x90; beam W24x55; brace HSS6x6x3/8. Designed/analysed to ASCE7-22. Seismic weight 1400 kip, Cs=0.2000, base shear 280.0 kip; computed period T1=0.595 s (Ta=0.312); max interstorey drift 0.00252; mode-1 modal mass 0.900. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# CBF_03ST — CBF 3-storey building template

2D lateral frame, regular 30 ft bays, members W14x90/W24x55/HSS6x6x3/8.

ASCE 7 seismic ELF (DAM 0.8E): W=1400 kip, Cs=0.2000, V=280 kip; computed T1=0.60s (Ta=0.31s); max interstorey drift 0.0025 (1/397); mode-1 modal mass 0.90.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

