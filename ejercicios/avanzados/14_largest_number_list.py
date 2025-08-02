"""
Lección básica: Número más grande en una lista.
Objetivo:
    Recorrer una lista y encontrar el número más grande sin usar funciones integradas.
"""

def main():
    """Encuentra e imprime el número más grande en una lista."""
    numbers = [15, 2, 1, 3, 20]
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(f"El número más grande es: {largest}")

if __name__ == "__main__":
    main()