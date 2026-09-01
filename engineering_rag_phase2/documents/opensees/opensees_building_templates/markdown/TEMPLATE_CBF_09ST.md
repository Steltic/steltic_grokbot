<!-- chunk_id: TEMPLATE_CBF_09ST | collection: opensees_building_templates -->
<!-- meta: {
 "source": "building_template",
 "kind": "building_template",
 "template_id": "TEMPLATE_CBF_09ST",
 "system": "chevron_braced_frame",
 "storeys": 9,
 "base_condition": "pinned",
 "members": "col W14x211; beam W27x94; brace HSS8x8x1/2",
 "code": "ASCE7-22",
 "base_shear_kip": 742.1,
 "computed_T1_s": 1.553,
 "max_interstorey_drift": 0.00587,
 "modal_mass_mode1": 0.758,
 "analysis": "linear_static seismic ELF (DAM 0.8E) + modal",
 "status": "validated"
} -->

## TEMPLATE_CBF_09ST

OpenSeesPy steel building template TEMPLATE_CBF_09ST: chevron_braced_frame, 9 storeys, regular, 30 ft bays, base pinned. Members: col W14x211; beam W27x94; brace HSS8x8x1/2. Designed/analysed to ASCE7-22. Seismic weight 4400 kip, Cs=0.1687, base shear 742.1 kip; computed period T1=1.553 s (Ta=0.711); max interstorey drift 0.00587; mode-1 modal mass 0.758. Sanity checks: equilibrium=True, stable=True, period_vs_Ta=True, modal_mass_mode1=True, drift_ok=True. Status validated.

# CBF_09ST — CBF 9-storey building template

2D lateral frame, regular 30 ft bays, members W14x211/W27x94/HSS8x8x1/2.

ASCE 7 seismic ELF (DAM 0.8E): W=4400 kip, Cs=0.1687, V=742 kip; computed T1=1.55s (Ta=0.71s); max interstorey drift 0.0059 (1/170); mode-1 modal mass 0.76.

Sanity checks: {'equilibrium': True, 'stable': True, 'period_vs_Ta': True, 'modal_mass_mode1': True, 'drift_ok': True}. Status: validated.
Reproduce via generators/mf2d.py or cbf2d.py with these parameters.

