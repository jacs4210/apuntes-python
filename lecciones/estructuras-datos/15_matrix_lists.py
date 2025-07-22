"""
Lección 15: Listas y Matrices (listas anidadas)

Descripción:
Esta lección cubre el uso de listas anidadas (matrices) en Python. Aprenderás a crear, acceder y manipular matrices, así como a recorrerlas para procesar sus elementos.

Objetivos:
- Comprender cómo crear y acceder a listas anidadas (matrices)
- Acceder a filas y elementos individuales
- Recorrer matrices con bucles anidados
- Aplicar operaciones básicas sobre matrices

Conceptos Clave:
- Lista anidada: Lista que contiene otras listas
- Matriz: Estructura de datos bidimensional
- Acceso por índices: matrix[fila][columna]
- Recorrido con bucles anidados

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
- Tutorial de matrices: https://realpython.com/python-matrix/

Autor: Jairo Cuartas
Fecha: 2025-07-21
"""

# =============================================================================
# EJEMPLO 1: Crear una matriz (lista de listas)
# =============================================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# =============================================================================
# EJEMPLO 2: Acceder a filas y elementos
# =============================================================================
# Imprime la segunda fila de la matriz
print(matrix[1])  # Salida esperada: [4, 5, 6]

# Imprime el primer elemento de la tercera fila de la matriz
print(matrix[2][0])  # Salida esperada: 7

# =============================================================================
# EJEMPLO 3: Recorrer todos los elementos de la matriz
# =============================================================================
for fila in matrix:
    for elemento in fila:
        print(elemento, end=' ')
    print()
# Salida esperada:
# 1 2 3
# 4 5 6
# 7 8 9

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Suma todos los elementos de la matriz
# 2. Imprime solo los elementos de la diagonal principal
# 3. Crea una matriz identidad de 3x3
# 4. Multiplica todos los elementos por 2 y muestra la nueva matriz

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Una matriz es una lista de listas (bidimensional)
2. El acceso es matrix[fila][columna], comenzando en 0
3. Puedes recorrer filas y columnas con bucles anidados
4. Las matrices pueden tener cualquier tamaño
5. Muy útil para representar tablas, tableros, imágenes, etc.
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# # Imprimir la diagonal principal
# for i in range(len(matrix)):
#     print(matrix[i][i])
#
# # Crear una matriz de ceros 3x3
# matriz_ceros = [[0 for _ in range(3)] for _ in range(3)]
# print(matriz_ceros)