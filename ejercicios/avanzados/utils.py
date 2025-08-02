"""
Módulo utils.py - Funciones auxiliares para ejercicios avanzados

Descripción:
Este módulo contiene funciones auxiliares para ejercicios de listas y números.
Incluye la función get_max para obtener el valor máximo de una lista de números.

Objetivos:
- Practicar la definición de funciones en módulos
- Reutilizar funciones en diferentes ejercicios

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/tutorial/modules.html
- Funciones útiles:
  https://realpython.com/python-functions/

Autor: Jairo Cuartas
Fecha: 2025-07-26
"""

def get_max(numbers):
    """
    Devuelve el valor máximo de una lista de números.
    Args:
        numbers (list): Lista de números
    Returns:
        int or float: Valor máximo encontrado
    """
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Ejemplo de uso:
# lista = [10, 5, 8, 20]
# print(get_max(lista))  # Salida esperada: 20