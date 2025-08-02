"""
Ejercicio 20: Generar valores aleatorios con una clase Dado

Descripción:
Este ejercicio consiste en crear una clase Dice que simula el lanzamiento de dos dados, generando valores aleatorios entre 1 y 10.

Objetivos:
- Practicar la definición de clases y métodos
- Usar la biblioteca random para generar números aleatorios
- Comprender el retorno de tuplas desde métodos

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/library/random.html
- Tutorial de clases:
  https://realpython.com/python3-object-oriented-programming/

Autor: Jairo Cuartas
Fecha: 2025-07-26
"""

import random

class Dice:
    def roll(self):
        """
        Simula el lanzamiento de dos dados y retorna una tupla con los resultados.
        Returns:
            tuple: (valor_dado_1, valor_dado_2)
        """
        first_value = random.randint(1, 10)
        second_value = random.randint(1, 10)
        return (first_value, second_value)

# Crear una instancia de la clase Dice
dice = Dice()

# Lanzar los dados y mostrar el resultado
print(dice.roll())  # Salida esperada: (valor entre 1 y 10, valor entre 1 y 10)

# =============================================================================
# EJERCICIOS ADICIONALES
# =============================================================================
# 1. Modifica la clase para lanzar un dado de 6 caras
# 2. Lanza los dados 5 veces y muestra todos los resultados
# 3. Calcula la suma de los valores obtenidos en cada lanzamiento