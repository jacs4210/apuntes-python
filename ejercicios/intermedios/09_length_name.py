name = input("Ingrese su nombre: ")

if len(name) < 3:
    print('El nomnbre de tener al menos 3 caracteres')
elif len(name) > 50:
    print('El nombre no puede tener mas de 50 caracteres')
else:
    print(f'El nombre {name} es correcto')
    print(f'Bienvenido {name} a la validación de nombres')