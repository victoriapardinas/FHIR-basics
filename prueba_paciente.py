
from patient_with_id import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir

# Parámetros del paciente (usando los datos de Milhouse Martinez)
family_name = "Martinez"
given_name = "Milhouse"
birth_date = "1993-09-10"
gender = "male"
phone = "+1123456789"  # Número de teléfono de ejemplo
document_number = "35783587"  # Número de documento

# Crear el recurso de paciente con identificador
patient_with_id = create_patient_resource(family_name, given_name, birth_date, gender, phone, document_number)

patient_id = send_resource_to_hapi_fhir(patient_with_id, 'Patient')

# Si el paciente fue creado exitosamente, obtener el recurso del paciente
if patient_id:
    print(f"Paciente con ID {patient_id} creado exitosamente.")
    # Ahora leer el recurso de paciente usando el ID
    get_resource_from_hapi_fhir(patient_id, 'Patient')
else:
    print("Error al crear el paciente.")