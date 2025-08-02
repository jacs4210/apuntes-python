"""
Lección básica: Número a letras (teléfono).
Objetivo:
    Tomar un número de teléfono y convertir cada dígito a su representación en palabras.
"""

def main():
    """Convierte cada dígito ingresado en su palabra correspondiente."""
    numbers = {
        "0": "Cero",
        "1": "Uno",
        "2": "Dos",
        "3": "Tres",
        "4": "Cuatro",
        "5": "Cinco",
        "6": "Seis",
        "7": "Siete",
        "8": "Ocho",
        "9": "Nueve"
    }
    phone_in_letters = ""
    phone = input("Teléfono: ").strip()

    for digit in phone:
        if digit in numbers:
            phone_in_letters += numbers[digit] + " "
        else:
            phone_in_letters += "?" + " "  # carácter no reconocido

    print(f"Teléfono en palabras: {phone_in_letters.strip()}")

if __name__ == "__main__":
    main()