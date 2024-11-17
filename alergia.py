
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept

def create_allergy_intolerance_resource(patient_id, substance_code, substance_display, criticality="high", category="med", manifestacion="0", manifestacion_display="d",severity="severe", note=""):

    allergy_intolerance = AllergyIntolerance.construct(
        resourceType="AllergyIntolerance",

        patient=Reference({"reference": f"Patient/{patient_id}"}),  # Referencia al paciente
        substance=CodeableConcept.construct(
            coding=[{
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": substance_code,  # Código RxNorm para la sustancia
                "display": substance_display  # Nombre de la sustancia 
            }]
        ),
        criticality=criticality,  # Gravedad de la reacción alérgica
        category=category,  # Categoría de la alergia 
        reaction=[{
            
            "manifestation": [{
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": manifestacion,  # Código SNOMED 
                    "display": manifestacion_display
                }]
            }, {
                "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": manifestacion,  # Código SNOMED 
                    "display": manifestacion_display
                }]
            }],
            "severity": severity,  # Gravedad de la reacción alérgica
  
            
            "note": note  # Nota adicional sobre la reacción
        }],
        
    )

    return allergy_intolerance
    