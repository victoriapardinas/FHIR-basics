from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference

def create_allergy_intolerance_resource(
    patient_id,
    substance_code,
    substance_display,
    criticality,
    category,
    manifestation_code,
    manifestation_display,
    severity,
    note
):
    """
    Crea un recurso FHIR de AllergyIntolerance asociado a un paciente.

    Args:
        patient_id (str): ID del paciente asociado a la alergia.
        substance_code (str): Código de la sustancia (RxNorm u otro sistema).
        substance_display (str): Descripción de la sustancia.
        criticality (str): Gravedad de la alergia ("low", "high", etc.).
        category (str): Categoría de la alergia (e.g., "medication").
        manifestation_code (str): Código de la manifestación (SNOMED u otro sistema).
        manifestation_display (str): Descripción de la manifestación.
        severity (str): Gravedad de la reacción ("mild", "moderate", "severe").
        note (str): Nota descriptiva sobre la alergia.

    Returns:
        AllergyIntolerance: Objeto FHIR representando la alergia.
    """
    allergy_intolerance = AllergyIntolerance(
        resourceType="AllergyIntolerance",
        patient=Reference(reference=f"Patient/{patient_id}"),  # Referencia al paciente
        substance=CodeableConcept(
            coding=[{
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": substance_code,
                "display": substance_display
            }]
        ),
        criticality=criticality,
        category=[category],  # Lista con una categoría
        reaction=[{
            "manifestation": [
                {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": manifestation_code,
                            "display": manifestation_display
                        }
                    ]
                }
            ],
            "severity": severity
        }],
        note=[{"text": note}]
    )
    return allergy_intolerance
    pass
    