"""
Lección 14: Bucles Anidados (nested loops)

Descripción:
Esta lección cubre el uso de bucles anidados en Python. Aprenderás a utilizar un bucle dentro 
de otro para recorrer estructuras más complejas, como matrices o para generar combinaciones de valores.

Objetivos:
- Comprender cómo funcionan los bucles anidados
- Usar for dentro de for para recorrer pares de valores
- Visualizar la ejecución de bucles anidados
- Aplicar bucles anidados en problemas prácticos

Conceptos Clave:
- Bucle anidado: Un bucle dentro de otro bucle
- Iteración múltiple: Recorrer varias dimensiones
- Combinaciones: Generar pares, tríos, etc.

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#nested-compound-statements
- Tutorial de bucles anidados: https://realpython.com/python-nested-loops/

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Bucles for anidados para pares de valores
# =============================================================================
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
# Salida esperada:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
# (3, 0)
# (3, 1)
# (3, 2)

# =============================================================================
# EJEMPLO 2: Imprimir una matriz de asteriscos
# =============================================================================
filas = 3
columnas = 5
for i in range(filas):
    for j in range(columnas):
        print('*', end='')
    print()  # Salto de línea al final de cada fila
# Salida esperada:
# *****
# *****
# *****

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Imprime la tabla de multiplicar del 1 al 5 usando bucles anidados
# 2. Dibuja un triángulo de asteriscos de altura 4
# 3. Recorre una matriz (lista de listas) y muestra cada elemento

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Un bucle anidado ejecuta su ciclo completo por cada iteración del bucle externo
2. El número total de iteraciones es el producto de los rangos
3. Puedes anidar for, while, o combinarlos
4. Muy útil para trabajar con matrices, tablas y combinaciones
5. Cuidado con la complejidad: demasiados anidados pueden hacer el código difícil de leer
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# for i in range(1, 4):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()
# # Salida esperada:
# # *
# # **
# # ***