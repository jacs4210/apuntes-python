"""
Ejercicio 19: Obtener el valor máximo de una lista

Descripción:
Este ejercicio consiste en encontrar el valor máximo de una lista de números 
utilizando una función auxiliar definida en un módulo aparte (utils.py).

Objetivos:
- Practicar la importación y uso de módulos propios
- Implementar una función para encontrar el valor máximo en una lista
- Comprender la reutilización de código

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/tutorial/modules.html
- Funciones útiles:
  https://realpython.com/python-functions/

Autor: Jairo Cuartas
Fecha: 2025-07-26
"""

import utils

# from utils import get_max  # Importa solo la función get_max

# Lista de números de ejemplo
numbers = [1, 2, 3, 4, 5]

# Llama a la función get_max del módulo utils para obtener el valor máximo
encontrado = utils.get_max(numbers)

print(f"El valor máximo es: {encontrado}")  # Salida esperada: El valor máximo es: 5

# =============================================================================
# EJERCICIOS ADICIONALES
# =============================================================================
# 1. Modifica la lista para probar con otros valores y verifica el resultado
# 2. Usa la función get_max con una lista de números negativos
# 3. Implementa una función similar que devuelva el valor mínimo
