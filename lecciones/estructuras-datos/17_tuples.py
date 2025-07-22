"""
Lección 17: Tuplas (tuples)

Descripción:
Esta lección cubre el uso de tuplas en Python. Aprenderás a crear, acceder y utilizar tuplas, y a entender la diferencia entre tuplas y listas.

Objetivos:
- Comprender qué es una tupla y cómo se crea
- Acceder a elementos de una tupla
- Conocer las diferencias entre tuplas y listas
- Usar tuplas para datos inmutables

Conceptos Clave:
- Tupla: Secuencia inmutable de elementos
- Inmutabilidad: No se puede modificar después de crearla
- Acceso por índice: tupla[posición]
- Uso común: Coordenadas, datos constantes, retorno múltiple de funciones

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- Tutorial de tuplas: https://realpython.com/python-tuples/

Autor: Jairo Cuartas
Fecha: 2025-07-21
"""

# =============================================================================
# EJEMPLO 1: Crear una tupla
# =============================================================================
coordinates = (1, 2, 3)

# =============================================================================
# EJEMPLO 2: Acceder a elementos de una tupla
# =============================================================================
print(coordinates[0])  # Salida esperada: 1

# =============================================================================
# EJEMPLO 3: Recorrer una tupla con un for
# =============================================================================
for value in coordinates:
    print(value)
# Salida esperada:
# 1
# 2
# 3

# =============================================================================
# EJEMPLO 4: Intentar modificar una tupla (provoca error)
# =============================================================================
# coordinates[0] = 10  # Descomenta para ver el error: TypeError: 'tuple' object does not support item assignment

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Crea una tupla con los días de la semana y recórrela con un for
# 2. Intenta modificar un elemento de la tupla y observa el error
# 3. Usa una tupla para almacenar las coordenadas de un punto (x, y)

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Las tuplas se crean con paréntesis () y son inmutables
2. Puedes acceder a sus elementos por índice
3. No puedes agregar, eliminar ni modificar elementos
4. Son útiles para datos constantes o retornos múltiples
5. Ocupan menos memoria que las listas
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# tupla = (10, 20, 30)
# print(tupla[1])
# for i, valor in enumerate(tupla):
#     print(f'Índice {i}: {valor}')