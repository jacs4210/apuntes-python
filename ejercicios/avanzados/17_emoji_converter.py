"""
Lección básica: Conversor de emojis.
Objetivo:
    Reemplazar atajos como ':)' por su emoji correspondiente en un mensaje.
"""

def emoji_converter(message):
    """Reemplaza secuencias por emojis en una cadena."""
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😄",
        ":P": "😛",
        ";)": "😉"
    }

    words = message.split(" ")
    converted_message = ""

    for word in words:
        converted_message += emojis.get(word, word) + " "

    return converted_message.strip()

def main():
    """Lee un mensaje del usuario y lo convierte usando emojis."""
    message = input("> ").strip()
    output = emoji_converter(message)
    print(output)

if __name__ == "__main__":
    main()