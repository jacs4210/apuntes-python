try:
    age = int(input("Ingrese su edad: "))
    print(age)
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")