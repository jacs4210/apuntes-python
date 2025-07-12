products_info = '''
Gaseosa 235ml tiene un costo de $24
Gaseosa 470ml tiene un costo de $42
'''

print(products_info)

input('Quieres saber cual es la mejor opción? (Presiona Enter para continuar) ')

gas_235ml = 24
gas_470ml = 42

better_choice = gas_235ml * 2 < gas_470ml
if better_choice:
    better_choice = '''La mejor opción es la Gaseosa 235ml'''
else:
    better_choice = '''La mejor opción es la Gaseosa 470ml'''

print(better_choice)