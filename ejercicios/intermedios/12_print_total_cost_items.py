"""
Lección básica: Sumar costos.
Objetivo:
    Calcular el costo total de una lista de productos.
"""

def main():
    """Suma los precios y muestra el total."""
    products_cost = [10, 20, 30]
    total_cost = sum(products_cost)
    print(f"El costo total de los productos es: {total_cost}")

if __name__ == "__main__":
    main()