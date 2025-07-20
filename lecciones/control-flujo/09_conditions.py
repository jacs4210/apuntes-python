"""
Lección 09: Estructuras Condicionales (if, elif, else)

Descripción:
Esta lección cubre el uso de las estructuras condicionales en Python. Aprenderás a tomar decisiones en tu código 
usando if, elif y else, y a evaluar condiciones booleanas para controlar el flujo del programa.

Objetivos:
- Comprender cómo funcionan las estructuras condicionales
- Usar if, elif y else para tomar decisiones
- Evaluar condiciones booleanas
- Escribir código que responda a diferentes escenarios

Conceptos Clave:
- if: ejecuta un bloque si la condición es verdadera
- elif: evalúa otra condición si la anterior es falsa
- else: ejecuta un bloque si todas las condiciones anteriores son falsas
- Booleanos: True o False

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#if-statements
- Operadores de comparación: https://docs.python.org/3/library/stdtypes.html#boolean-values

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Condiciones simples
# =============================================================================
is_hot = False
is_cold = False

if is_hot:
    print("Hace calor hoy")
    # Salida esperada si is_hot = True: Hace calor hoy
elif is_cold:
    print("Hace frío hoy")
    # Salida esperada si is_cold = True: Hace frío hoy
else:
    print("El clima está agradable hoy")
    # Salida esperada si ambos son False: El clima está agradable hoy

# =============================================================================
# EJEMPLO 2: Cambiando los valores
# =============================================================================
is_hot = True
is_cold = False

if is_hot:
    print("Hace calor hoy")
elif is_cold:
    print("Hace frío hoy")
else:
    print("El clima está agradable hoy")
# Salida esperada: Hace calor hoy

# =============================================================================
# EJEMPLO 3: Condiciones anidadas
# =============================================================================
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# Salida esperada: Eres mayor de edad

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Escribe un programa que pregunte la edad y diga si puedes votar (>=18)
# 2. Escribe un programa que pregunte la temperatura y diga si hace frío, calor o está agradable
# 3. Escribe un programa que pregunte si tienes hambre y responda "¡Hora de comer!" o "Sigue trabajando"

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Las condiciones se evalúan de arriba hacia abajo
2. Solo se ejecuta el primer bloque cuya condición sea verdadera
3. Puedes tener múltiples elif
4. else es opcional, pero útil para casos por defecto
5. Los booleanos pueden ser variables o resultados de comparaciones
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# temperatura = 25
# if temperatura > 30:
#     print("Hace mucho calor")
# elif temperatura < 15:
#     print("Hace mucho frío")
# else:
#     print("Temperatura agradable")

