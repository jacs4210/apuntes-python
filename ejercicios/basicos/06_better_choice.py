"""
Lección básica: Comparar opciones.
Objetivo:
    Mostrar cuál de dos opciones tiene mejor costo por unidad.
"""

def main():
    """Compara dos tamaños de gaseosa y recomienda la mejor opción."""
    products_info = '''
Gaseosa 235ml tiene un costo de $24
Gaseosa 470ml tiene un costo de $42
'''
    print(products_info)
    input('¿Quieres saber cuál es la mejor opción? (Presiona Enter para continuar) ')

    gas_235ml = 24
    gas_470ml = 42

    costo_235 = gas_235ml / 235
    costo_470 = gas_470ml / 470

    print(f"Costo por ml de 235ml: ${costo_235:.4f}")
    print(f"Costo por ml de 470ml: ${costo_470:.4f}")

    if costo_235 < costo_470:
        mejor = "235 ml"
    elif costo_470 < costo_235:
        mejor = "470 ml"
    else:
        mejor = "Ambas son iguales en costo por ml"

    print(f"La mejor opción es: {mejor}")

if __name__ == "__main__":
    main()