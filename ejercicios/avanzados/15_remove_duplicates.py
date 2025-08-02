"""
Lección básica: Quitar duplicados.
Objetivo:
    Eliminar valores repetidos de una lista sin usar estructuras complejas.
"""

def main():
    """Remueve duplicados de una lista y muestra el resultado."""
    numbers = [1, 2, 3, 3, 4, 5, 5, 6]
    numbers_no_duplicates = []

    for num in numbers:
        if num not in numbers_no_duplicates:
            numbers_no_duplicates.append(num)

    print(f"Lista original: {numbers}")
    print(f"Sin duplicados: {numbers_no_duplicates}")

if __name__ == "__main__":
    main()