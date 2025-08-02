"""
Lección básica: Slicing de cadenas.
Objetivo:
    Mostrar cómo extraer una subcadena quitando el primer y último carácter.
"""

def main():
    """Imprime el resultado del slicing sobre una cadena de ejemplo."""
    name = "Jairo"
    resultado = name[1:-1]
    print(resultado)

if __name__ == "__main__":
    main()