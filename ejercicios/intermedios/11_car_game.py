command = ""
help = '''
start - Para arrancar el carro
stop - Para detener el carro
help - Para mostrar la ayuda del programa
quit - Para detener el programa
'''
is_car_run = False

while True:
    command = input("> ").lower()

    if command == "start":
        if not is_car_run:
            print('El carro inicia su recorrido...')
            is_car_run = True
        else:
            print('El carro ya está en un recorrido. Debes detenerlo primero!')
    elif command == "stop":
        if is_car_run:
            print('El carro se detiene')
            is_car_run = False
        else:
            print('Ya está detenido el carro, debes iniciarlo para volver a detenerlo')
    elif command == "help":
        print(help)
    elif command == "quit":
        break
    else:
        print('Me estas pidiendo lo que no sé. Te recuerdo como funciono')
        print(help)