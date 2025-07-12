SECRET_NUMBER = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_number = int(input('Ingresa el número secreto: '))
    guess_count += 1
    if guess_number == SECRET_NUMBER:
        print('\nAdivinaste, Felicitaciones!!')
        break
else:
    print('\nLo lamento, has fallado, intentalo nuevamente!!')