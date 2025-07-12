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
phone = input("Telefono: ")

for digit in phone:
    phone_in_letters += numbers[digit] + " "

print(phone_in_letters)