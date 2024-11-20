
patient_id = "45179080"  # ID del paciente previamente creado
substance_code = "7635"  # Código para Aspirina
substance_display = "Aspirin"  # Nombre de la sustancia
criticality = "high"  # Nivel de gravedad
category = "medication"  # Categoría de la alergia (medicación)
manifestation_code = "56018004"  # Código de manifestación (Skin Rash)
manifestation_display = "Skin Rash"  # Descripción de la manifestación
severity = "severe"  # Severidad de la reacción
note = "El paciente tiene una reacción severa en la piel tras el consumo de aspirina."  # Nota descriptiva


allergy_dict = create_allergy_intolerance_resource(
    patient_id, substance_code, substance_display, criticality, category,
    manifestation_code, manifestation_display, severity, note
)

send_allergy_intolerance_to_fhir(allergy_dict)
