"""
Lección básica: Juego de adivinanza.
Objetivo:
    Permitir al usuario adivinar un número secreto con un número limitado de intentos.
"""

def main():
    """Ejecuta el juego de adivinar el número."""
    SECRET_NUMBER = 9
    guess_limit = 3
    guess_count = 0

    while guess_count < guess_limit:
        try:
            guess_number = int(input("Ingresa el número secreto: "))
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número entero.")
            continue

        guess_count += 1
        if guess_number == SECRET_NUMBER:
            print("\nAdivinaste, ¡Felicitaciones!")
            break
    else:
        print("\nLo lamento, has fallado, inténtalo nuevamente!!")

if __name__ == "__main__":
    main()