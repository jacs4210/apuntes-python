"""
Lección 05: Manipulación de Strings (Cadenas de Texto)

Descripción:
Esta lección profundiza en el trabajo con strings en Python. Aprenderás diferentes
formas de crear strings, cómo acceder a caracteres individuales, y técnicas
básicas de manipulación de texto.

Objetivos:
- Comprender diferentes formas de crear strings
- Aprender a acceder a caracteres por posición (indexing)
- Entender el slicing (cortar strings)
- Manejar comillas simples y dobles correctamente

Conceptos Clave:
- String: Secuencia de caracteres
- Indexing: Acceder a caracteres por posición
- Slicing: Extraer partes de un string
- Comillas simples (') y dobles (")
- Strings multilínea

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/introduction.html#strings
- Métodos de strings: https://docs.python.org/3/library/stdtypes.html#string-methods

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Diferentes formas de crear strings
# =============================================================================
# Usando comillas dobles
mensaje1 = "Python's for beginners"
print(f"Mensaje 1: {mensaje1}")
# Salida esperada: Mensaje 1: Python's for beginners

# Usando comillas simples
mensaje2 = 'Python for "beginners"'
print(f"Mensaje 2: {mensaje2}")
# Salida esperada: Mensaje 2: Python for "beginners"

# =============================================================================
# EJEMPLO 2: Strings multilínea
# =============================================================================
email = '''
Hola Jairo,

Este es un mensaje del equipo de DevOps.

Gracias por tu apoyo.
'''
print("Email completo:")
print(email)
# Salida esperada:
# Hola Jairo,
#
# Este es un mensaje del equipo de DevOps.
#
# Gracias por tu apoyo.

# =============================================================================
# EJEMPLO 3: Indexing - Acceder a caracteres individuales
# =============================================================================
curso = 'Python for beginners'
print(f"String completo: '{curso}'")

# Acceder al primer carácter (índice 0)
primer_caracter = curso[0]
print(f"Primer carácter: '{primer_caracter}'")
# Salida esperada: Primer carácter: 'P'

# Acceder al último carácter (índice -1)
ultimo_caracter = curso[-1]
print(f"Último carácter: '{ultimo_caracter}'")
# Salida esperada: Último carácter: 's'

# =============================================================================
# EJEMPLO 4: Slicing - Extraer partes del string
# =============================================================================
# Extraer los primeros 4 caracteres (índices 0 a 3)
primeros_caracteres = curso[0:4]
print(f"Primeros 4 caracteres: '{primeros_caracteres}'")
# Salida esperada: Primeros 4 caracteres: 'Pyth'

# Forma abreviada para el inicio
primeros_caracteres_abreviado = curso[:4]
print(f"Primeros 4 caracteres (abreviado): '{primeros_caracteres_abreviado}'")
# Salida esperada: Primeros 4 caracteres (abreviado): 'Pyth'

# =============================================================================
# EJEMPLO 5: Más ejemplos de slicing
# =============================================================================
print(f"\nEjemplos de slicing:")
print(f"curso[0:6]: '{curso[0:6]}'")      # 'Python'
print(f"curso[7:10]: '{curso[7:10]}'")    # 'for'
print(f"curso[11:]: '{curso[11:]}'")      # 'beginners'
print(f"curso[-9:]: '{curso[-9:]}'")      # 'beginners'
print(f"curso[:-9]: '{curso[:-9]}'")      # 'Python for'

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estos ejercicios:
# 1. Extraer "Python" del string "Python Programming"
# 2. Obtener el último carácter de cualquier string
# 3. Extraer los primeros 3 caracteres de tu nombre

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Los índices en Python comienzan en 0 (no en 1)
2. Los índices negativos cuentan desde el final (-1 es el último)
3. Slicing usa la sintaxis [inicio:fin:paso]
4. Si omites inicio, comienza desde 0
5. Si omites fin, va hasta el final
6. Los strings son inmutables (no se pueden cambiar)
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Más ejemplos de slicing
# texto = "Hola Mundo Python"
# print(f"Texto original: '{texto}'")
# print(f"Primera palabra: '{texto[0:4]}'")
# print(f"Segunda palabra: '{texto[5:10]}'")
# print(f"Tercera palabra: '{texto[11:]}'")
# 
# # Slicing con paso (step)
# print(f"Cada segundo carácter: '{texto[::2]}'")
# print(f"Texto al revés: '{texto[::-1]}'")
# 
# # Longitud del string
# print(f"Longitud del texto: {len(texto)} caracteres")

# =============================================================================
# MANIPULACIÓN BÁSICA DE STRINGS
# =============================================================================
# Nota: Los strings son inmutables, pero puedes crear nuevos strings
# Ejemplo: curso.upper(), curso.lower(), curso.replace(), etc.
# Estos métodos se verán en lecciones posteriores