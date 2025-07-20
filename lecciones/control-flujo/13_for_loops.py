"""
Lección 13: Bucles For (for loops)

Descripción:
Esta lección cubre el uso del bucle for en Python. Aprenderás a recorrer secuencias como strings, 
listas y rangos, y a controlar la iteración con diferentes parámetros.

Objetivos:
- Comprender cómo funciona el bucle for
- Recorrer strings, listas y rangos
- Usar range() con diferentes argumentos
- Escribir programas que repitan acciones sobre colecciones

Conceptos Clave:
- for: Repite un bloque para cada elemento de una secuencia
- range(): Genera una secuencia de números
- Iteración: Proceso de recorrer elementos uno a uno
- Paso (step): Controla el incremento en range()

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#for-statements
- Tutorial de bucles for: https://realpython.com/python-for-loop/

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Recorrer un string carácter por carácter
# =============================================================================
for char in 'Python':
    print(char)
# Salida esperada:
# P
# y
# t
# h
# o
# n

# =============================================================================
# EJEMPLO 2: Recorrer una lista de números
# =============================================================================
for number in [1, 2, 3, 4, 5]:
    print(number)
# Salida esperada:
# 1
# 2
# 3
# 4
# 5

# =============================================================================
# EJEMPLO 3: Recorrer una lista de nombres
# =============================================================================
for name in ["Jairo", "Angie", "Juan", "Pedro"]:
    print(name)
# Salida esperada:
# Jairo
# Angie
# Juan
# Pedro

# =============================================================================
# EJEMPLO 4: Usando range() para generar secuencias
# =============================================================================
for number in range(10):
    print(number)
# Salida esperada: 0 a 9

for number in range(1, 11):
    print(number)
# Salida esperada: 1 a 10

for number in range(1, 11, 2):
    print(number)
# Salida esperada: 1, 3, 5, 7, 9

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Imprime los caracteres de tu nombre usando un for
# 2. Imprime los números pares del 2 al 20 usando range()
# 3. Suma todos los números del 1 al 100 usando un for
# 4. Recorre una lista de frutas y muestra cada una en mayúsculas

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. El bucle for recorre cualquier secuencia (string, lista, range, etc.)
2. range(inicio, fin, paso) genera números desde inicio hasta fin-1
3. Puedes usar for para recorrer listas de cualquier tipo
4. El bloque dentro del for se ejecuta una vez por cada elemento
5. Puedes anidar bucles for para recorrer estructuras más complejas
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# for i in range(5, 0, -1):
#     print(i)
# print('Cuenta regresiva finalizada')
#
# lista = ['manzana', 'pera', 'uva']
# for fruta in lista:
#     print(fruta.upper())