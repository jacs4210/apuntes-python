"""
Lección 18: Desempaquetado de Secuencias (unpacking)

Descripción:
Esta lección cubre el desempaquetado de secuencias en Python. Aprenderás a asignar múltiples variables a partir de listas o tuplas de manera sencilla y clara.

Objetivos:
- Comprender cómo funciona el desempaquetado de secuencias
- Asignar varias variables en una sola línea
- Usar desempaquetado con listas y tuplas
- Aplicar desempaquetado en funciones y retornos múltiples

Conceptos Clave:
- Desempaquetado: Asignar elementos de una secuencia a variables
- Secuencia: Lista, tupla u otro iterable
- Orden: El número de variables debe coincidir con el número de elementos

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/unpacking.html
- Tutorial de desempaquetado: https://realpython.com/python-tuples/

Autor: Jairo Cuartas
Fecha: 2025-07-21
"""

# =============================================================================
# EJEMPLO 1: Desempaquetar una tupla
# =============================================================================
coordinates = (1, 2, 3)
x, y, z = coordinates

print(y)  # Salida esperada: 2

# =============================================================================
# EJEMPLO 2: Desempaquetar una lista
# =============================================================================
valores = [10, 20, 30]
a, b, c = valores
print(a, c)  # Salida esperada: 10 30

# =============================================================================
# EJEMPLO 3: Desempaquetado parcial con *resto
# =============================================================================
nums = [1, 2, 3, 4, 5]
primero, *resto = nums
print(primero)  # Salida esperada: 1
print(resto)    # Salida esperada: [2, 3, 4, 5]

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Desempaqueta una tupla con el nombre, edad y ciudad de una persona
# 2. Usa * para capturar todos los elementos excepto el primero
# 3. Desempaqueta el retorno de una función que devuelve tres valores

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. El número de variables debe coincidir con el número de elementos (excepto usando *)
2. Puedes desempaquetar listas, tuplas y otros iterables
3. El desempaquetado hace el código más limpio y legible
4. Puedes usar * para capturar el resto de los elementos
5. Muy útil en funciones que retornan múltiples valores
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# datos = ("Ana", 28, "Bogotá")
# nombre, edad, ciudad = datos
# print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
#
# lista = [1, 2, 3, 4, 5]
# primero, segundo, *otros = lista
# print(primero, segundo, otros)