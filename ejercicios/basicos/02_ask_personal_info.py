"""
Lección básica: Preguntar información personal.
Objetivo:
    Pedir nombre y color favorito y mostrar un mensaje con esa información.
"""

def main():
    """Solicita nombre y color favorito, luego imprime el resultado."""
    name = input("¿Cuál es tu nombre? ").strip()
    color = input("¿Cuál es tu color favorito? ").strip()
    print(f"El color favorito de {name} es {color}.")

if __name__ == "__main__":
    main()