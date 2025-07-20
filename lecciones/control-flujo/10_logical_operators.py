"""
Lección 10: Operadores Lógicos (and, or, not)

Descripción:
Esta lección cubre el uso de los operadores lógicos en Python. Aprenderás a combinar condiciones 
usando and, or y not para tomar decisiones más complejas en tu código.

Objetivos:
- Comprender cómo funcionan los operadores lógicos
- Usar and, or y not para combinar condiciones
- Escribir expresiones lógicas complejas
- Evaluar múltiples condiciones en una sola instrucción

Conceptos Clave:
- and: Verdadero solo si ambas condiciones son verdaderas
- or: Verdadero si al menos una condición es verdadera
- not: Invierte el valor lógico (True ↔ False)
- Expresiones lógicas: Combinación de condiciones booleanas

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- Tutorial de operadores lógicos: https://realpython.com/python-boolean/

Autor: Jairo Cuartas
Fecha: 2025-07-20
"""

# =============================================================================
# EJEMPLO 1: Operador AND
# =============================================================================
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eres elegible para un préstamo.")
    # Salida esperada: Eres elegible para un préstamo.

# =============================================================================
# EJEMPLO 2: Operador OR
# =============================================================================
if has_good_credit or has_criminal_record:
    print("Eres elegible para un préstamo, pero con condiciones.")
    # Salida esperada: Eres elegible para un préstamo, pero con condiciones.

# =============================================================================
# EJEMPLO 3: Operador NOT
# =============================================================================
if not has_criminal_record:
    print("No tienes antecedentes penales.")
    # Salida esperada: No tienes antecedentes penales.

# =============================================================================
# EJEMPLO 4: Combinando operadores
# =============================================================================
ingresos = 5000
edad = 25

if (has_good_credit and ingresos > 3000) or edad < 30:
    print("Cumples con los requisitos para aplicar.")
    # Salida esperada: Cumples con los requisitos para aplicar.

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Escribe un programa que pregunte si tienes licencia y si tienes seguro, y solo permita conducir si ambas son True
# 2. Escribe un programa que pregunte si tienes pasaporte o visa, y permita viajar si al menos una es True
# 3. Escribe un programa que niegue el acceso si la persona está en una lista negra (usa not)

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. and solo es True si ambas condiciones son True
2. or es True si al menos una condición es True
3. not invierte el valor lógico
4. Puedes combinar varios operadores en una sola expresión
5. El orden de evaluación sigue las reglas de precedencia lógica
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# tiene_licencia = True
# tiene_seguro = False
# if tiene_licencia and tiene_seguro:
#     print("Puedes conducir.")
# else:
#     print("No puedes conducir.")
