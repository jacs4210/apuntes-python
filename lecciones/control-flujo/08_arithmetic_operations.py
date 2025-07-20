"""
Lección 08: Operaciones Aritméticas en Python

Descripción:
Esta lección cubre los operadores aritméticos básicos y avanzados en Python. Aprenderás a realizar sumas, restas, 
multiplicaciones, divisiones, módulo, exponenciación y más. También se muestra el uso de la biblioteca math para 
operaciones matemáticas avanzadas.

Objetivos:
- Comprender los operadores aritméticos básicos (+, -, *, /, %, **, //)
- Usar operadores de asignación aumentada (+=, -=, *=, /=)
- Aplicar funciones matemáticas avanzadas con la biblioteca math
- Entender la diferencia entre división normal y división entera

Conceptos Clave:
- Operadores aritméticos: símbolos para realizar operaciones matemáticas
- Operadores de asignación: combinan operación y asignación
- math: biblioteca estándar para operaciones matemáticas avanzadas

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
- Biblioteca math: https://docs.python.org/3/library/math.html

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

import math

# =============================================================================
# EJEMPLO 1: Suma
# =============================================================================
x = 10
x = x + 5
print("Suma:", x)  # Salida esperada: Suma: 15

# =============================================================================
# EJEMPLO 2: Resta
# =============================================================================
x = 10
x = x - 3
print("Resta:", x)  # Salida esperada: Resta: 7

# =============================================================================
# EJEMPLO 3: Multiplicación
# =============================================================================
x = 10
x = x * 2
print("Multiplicación:", x)  # Salida esperada: Multiplicación: 20

# =============================================================================
# EJEMPLO 4: División
# =============================================================================
x = 10
x = x / 4
print("División:", x)  # Salida esperada: División: 2.5

# =============================================================================
# EJEMPLO 5: Módulo (resto de la división)
# =============================================================================
x = 10
x = x % 3
print("Módulo:", x)  # Salida esperada: Módulo: 1

# =============================================================================
# EJEMPLO 6: Exponenciación
# =============================================================================
x = 10
x = x ** 2
print("Exponenciación:", x)  # Salida esperada: Exponenciación: 100

# =============================================================================
# EJEMPLO 7: División entera
# =============================================================================
x = 10
x = x // 3
print("División entera:", x)  # Salida esperada: División entera: 3

# =============================================================================
# EJEMPLO 8: Operadores de asignación aumentada
# =============================================================================
x = 10
x += 5
print("Asignación aumentada:", x)  # Salida esperada: Asignación aumentada: 15

x = 10
x -= 2
print("Asignación disminuida:", x)  # Salida esperada: Asignación disminuida: 8

x = 10
x *= 3
print("Asignación multiplicada:", x)  # Salida esperada: Asignación multiplicada: 30

# =============================================================================
# EJEMPLO 9: Usando la biblioteca math para operaciones avanzadas
# =============================================================================
x = 16
x = math.sqrt(x)
print("Raíz cuadrada:", x)  # Salida esperada: Raíz cuadrada: 4.0

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Calcula el área de un círculo de radio 5 (usa math.pi y math.pow)
# 2. Calcula el residuo de dividir 123 entre 7
# 3. Eleva 2 a la potencia de 8 usando el operador **
# 4. Calcula la raíz cúbica de 27 usando math.pow
# 5. Usa operadores de asignación para sumar 10 a una variable inicializada en 0

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. La división normal (/) siempre devuelve float
2. La división entera (//) devuelve solo la parte entera
3. El operador % devuelve el residuo de la división
4. math.sqrt(x) calcula la raíz cuadrada
5. math.pow(x, y) eleva x a la potencia y
6. Los operadores de asignación combinan operación y asignación
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# print("Potencia con math.pow:", math.pow(2, 8))
# print("Área de un círculo de radio 5:", math.pi * math.pow(5, 2))
# print("Raíz cúbica de 27:", math.pow(27, 1/3))