"""
Lección básica: Pago inicial basado en crédito.
Objetivo:
    Calcular el pago inicial dependiendo si se tiene buen crédito o no.
"""

def main():
    """Determina el pago inicial a partir del precio y el crédito."""
    price_house = 1000000
    is_good_credit = True

    if is_good_credit:
        down_payment = price_house * 0.10
    else:
        down_payment = price_house * 0.20

    print(f"Pago inicial: ${down_payment:,.2f}")

if __name__ == "__main__":
    main()