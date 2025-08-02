"""
Lección básica: Conversión de peso.
Objetivo:
    Preguntar el peso en libras y convertirlo a kilogramos.
"""

def main():
    """Pide el peso en libras y muestra su equivalente en kilogramos."""
    weight_pounds = input("Dime tu peso en libras: ").strip()
    try:
        weight_kg = float(weight_pounds) * 0.45359237
        print(f"Tienes un peso en kilogramos de: {weight_kg:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número, por ejemplo: 150.5")

if __name__ == "__main__":
    main()