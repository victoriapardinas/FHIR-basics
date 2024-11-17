
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept

def create_allergy_intolerance_resource(patient_id, substance_code, substance_display, criticality="high", category="med", manifestacion="0", manifestacion_display="d",severity="severe", note=""):
    # Crear el recurso AllergyIntolerance con la estructura esperada
    allergy_intolerance = AllergyIntolerance.construct(
        resourceType="AllergyIntolerance",

        patient=Reference({"reference": f"Patient/{patient_id}"}),  # Referencia al paciente
        substance=CodeableConcept.construct(
            coding=[{
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": substance_code,  # Código RxNorm para la sustancia
                "display": substance_display  # Nombre de la sustancia (por ejemplo, "Aspirin")
            }]
        ),
        criticality=criticality,  # Gravedad de la reacción alérgica
        category=category,  # Categoría de la alergia (por ejemplo, medicamento)
        reaction=[{
            
            "manifestation": [{
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": manifestacion,  # Código SNOMED para cierre de garganta por ejemplo
                    "display": manifestacion_display
                }]
            }, {
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": manifestacion,  # Código SNOMED para dificultad para respirar
                    "display": manifestacion_display
                }]
            }],
            "severity": severity,  # Gravedad de la reacción alérgica
  
            
            "note": note  # Nota adicional sobre la reacción
        }],
        note=[{
            "text": note  # Historial de reacciones alérgicas del paciente
        }]
    )

    return allergy_intolerance
