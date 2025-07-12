def emoji_converter(message):
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

# Inicio del programa
message = input(">")
output = emoji_converter(message)
print(output)