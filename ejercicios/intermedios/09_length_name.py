"""
Lección básica: Validar nombre.
Objetivo:
    Verificar que el nombre ingresado tenga entre 3 y 50 caracteres.
"""

def main():
    """Pide el nombre y valida su longitud."""
    name = input("Ingrese su nombre: ").strip()

    if len(name) < 3:
        print("El nombre debe tener al menos 3 caracteres.")
    elif len(name) > 50:
        print("El nombre no puede tener más de 50 caracteres.")
    else:
        print(f"El nombre {name} es correcto")
        print(f"Bienvenido {name} a la validación de nombres")

if __name__ == "__main__":
    main()