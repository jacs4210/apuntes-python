"""
Lección básica: Datos de paciente.
Objetivo:
    Mostrar nombre, edad y si es nuevo o existente en un resumen simple.
"""

def main():
    """Define los datos del paciente y muestra el resumen."""
    patient_name = "John Smith"
    age = 20
    is_new_patient = True

    estado = "Nuevo paciente" if is_new_patient else "Paciente existente"
    print(f"Paciente: {patient_name}")
    print(f"Edad: {age}")
    print(f"Estado: {estado}")

if __name__ == "__main__":
    main()