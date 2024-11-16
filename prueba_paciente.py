
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

# Crear el recurso FHIR de paciente con parámetros opcionales
def create_patient_resource(family_name=None, given_name=None, birth_date=None, gender=None, phone=None, document_number=None):
    patient = Patient()
    
    # Agregar el nombre del paciente si está disponible
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    # Agregar la fecha de nacimiento si está disponible
    if birth_date:
        patient.birthDate = birth_date

    # Agregar el género si está disponible
    if gender:
        patient.gender = gender

    # Agregar información de contacto si está disponible
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]
    
    # Agregar el identificador (número de documento) si está disponible
    if document_number:
        patient.identifier = [{
            "use": "official",  # Identificador oficial
            "system": "http://argentina.gob/dni",  # Sistema de emisión del documento
            "value": document_number  # Número de documento
        }]
    
    return patient

