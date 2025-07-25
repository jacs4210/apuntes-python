"""
Lección 20: Funciones en Python

Descripción:
Esta lección cubre la definición y uso de funciones en Python. Aprenderás a crear funciones con parámetros, a llamarlas y a entender la importancia de la reutilización de código.

Objetivos:
- Comprender cómo definir y llamar funciones
- Usar parámetros y argumentos
- Entender el alcance y la reutilización de funciones
- Manejar errores comunes al llamar funciones

Conceptos Clave:
- def: Palabra clave para definir funciones
- Parámetro: Variable en la definición de la función
- Argumento: Valor pasado a la función al llamarla
- Reutilización: Escribir código una vez y usarlo muchas veces

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Tutorial de funciones: https://realpython.com/defining-your-own-python-function/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

# =============================================================================
# EJEMPLO 1: Definir y llamar una función con parámetros
# =============================================================================
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")

# Llamada correcta
greet_user("John", "Doe")  # Salida esperada: Hi John Doe!

# =============================================================================
# EJEMPLO 2: Error común al llamar funciones
# =============================================================================
#greet_user()  # TypeError: greet_user() missing 2 required positional arguments: 'first_name' and 'last_name'

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Define una función que reciba un nombre y lo salude
# 2. Define una función que reciba dos números y retorne su suma
# 3. Llama a la función con diferentes argumentos y muestra los resultados

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Las funciones se definen con def y pueden tener uno o más parámetros
2. Los argumentos deben coincidir en número y orden con los parámetros
3. Las funciones ayudan a organizar y reutilizar el código
4. Puedes documentar funciones con docstrings
5. Si olvidas pasar argumentos requeridos, obtendrás un TypeError
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# def suma(a, b):
#     return a + b
# print(suma(3, 5))
#
# def saludar(nombre="Invitado"):
#     print(f"Hola {nombre}")
# saludar()
# saludar("Ana")