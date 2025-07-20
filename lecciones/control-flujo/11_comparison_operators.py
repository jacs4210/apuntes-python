"""
Lección 11: Operadores de Comparación (==, !=, >, <, >=, <=)

Descripción:
Esta lección cubre el uso de los operadores de comparación en Python. Aprenderás a comparar valores y a 
tomar decisiones basadas en el resultado de esas comparaciones.

Objetivos:
- Comprender cómo funcionan los operadores de comparación
- Usar comparaciones en estructuras condicionales
- Escribir programas que respondan a diferentes valores

Conceptos Clave:
- == : Igualdad
- != : Diferente
- >  : Mayor que
- <  : Menor que
- >= : Mayor o igual que
- <= : Menor o igual que
- Comparaciones devuelven True o False

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/stdtypes.html#comparisons
- Tutorial de operadores: https://realpython.com/python-operators-expressions/

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Comparando temperatura
# =============================================================================
temperatura = int(input('Ingrese la temperatura actual: '))

if temperatura >= 25:
    print('Está haciendo calor')
    # Salida esperada si temperatura >= 25: Está haciendo calor
elif temperatura < 20:
    print('Está haciendo frío')
    # Salida esperada si temperatura < 20: Está haciendo frío
else:
    print('Está templado')
    # Salida esperada si 20 <= temperatura < 25: Está templado

# =============================================================================
# EJEMPLO 2: Otros operadores de comparación
# =============================================================================
edad = 18
if edad == 18:
    print('Tienes 18 años')
if edad != 21:
    print('No tienes 21 años')
if edad > 15:
    print('Eres mayor de 15 años')
if edad <= 18:
    print('Tienes 18 años o menos')

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Escribe un programa que pregunte la edad y diga si eres mayor de edad (>=18)
# 2. Escribe un programa que compare dos números y diga cuál es mayor, menor o si son iguales
# 3. Escribe un programa que pregunte la nota de un examen y diga si aprobaste (>=3.0)

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Los operadores de comparación devuelven True o False
2. Puedes usar comparaciones en if, elif y else
3. Puedes combinar comparaciones con operadores lógicos
4. Las comparaciones funcionan con números, strings y otros tipos
5. El resultado de una comparación puede guardarse en una variable
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# numero1 = int(input('Ingrese el primer número: '))
# numero2 = int(input('Ingrese el segundo número: '))
# if numero1 == numero2:
#     print('Son iguales')
# elif numero1 > numero2:
#     print('El primer número es mayor')
# else:
#     print('El segundo número es mayor')