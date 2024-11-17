
import requests

# Buscar paciente por documento
def search_patient_by_document(document_number):
    url = f"http://hapi.fhir.org/baseR4/Patient?identifier={document_number}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        patients = response.json().get('entry', [])
        
        if patients:
            print(f"Paciente(s) encontrado(s) con el documento {document_number}:")
            for patient_entry in patients:
                patient = patient_entry['resource']
                print(f"ID: {patient['id']}")
                print(f"Nombre: {patient['name'][0]['given'][0]} {patient['name'][0]['family']}")
                print(f"Fecha de nacimiento: {patient['birthDate']}")
                print(f"Género: {patient['gender']}")
                print("-------------------------------")
        else:
            print(f"No se encontró ningún paciente con el documento {document_number}.")
    else:
        print(f"Error al buscar el paciente: {response.status_code}")
        print(response.json())
