## Patient
Creación del recurso paciente con algunos parámetros. 

## Base 
Lectura y escritura de recursos en el servidor público de HAPI FHIR. 

## Workflow
Desde acá se corre el código. 

## TPVI
En la carpeta TPVI se encontrara el repositorio de nuestro trabajo práctico de interoperabilidad
- *patient_with_id.py* corresponde al codigo que permite crear un recurso patient con un documento nacional de identidad.
- *prueba_paciente.py* es la validación del código anterior, donde insertamos la información correspondiente a un paciente ficiticio
- *buscar_por_doc.py* permite buscar pacientes unicamente por su numero de documento y devuelve el Nombre, ID, Fecha de Nacimiento, y Genero del paciente con ese documento
- *agregar_alergias.py* genera el recurso para AllergyIntolerance con distintos elementos que consideramos relevantes detalladas en el informe
- *ejemplo_alergia.py* es la validación de este ultimo código, donde se le adjudica una alergia al paciente que se genero con las anteriores funciones
- *obtener_alergia_pacientes.py* es una función creada para obtener las alergias que posee un paciente, en conjunto con sus elementos relevantes, utilizando unicamente el id del paciente
- *ejemplo_paciente_alergia.py* es la validación de obtener alergia con el id, con el paciente anteriormente creado
