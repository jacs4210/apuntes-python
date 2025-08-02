"""
Lección básica: Imprimir la letra F.
Objetivo:
    Construir un patrón de texto que represente la letra 'F'.
"""

def print_f():
    """Dibuja la letra F usando 'x'."""
    # Barra horizontal superior
    print("xxxxx")
    # Dos filas de barra vertical
    for _ in range(2):
        print("x")
    # Barra horizontal del medio
    print("xxxxx")
    # Tres filas de barra vertical inferior
    for _ in range(3):
        print("x")

def main():
    """Punto de entrada para mostrar la letra F."""
    print_f()

if __name__ == "__main__":
    main()