"""
Lección 07: Funciones y Métodos

Descripción:
Esta lección introduce la diferencia entre funciones y métodos en Python.
Aprenderás sobre funciones de propósito general como len() y print(),
y métodos específicos de strings como upper(), find(), replace(), etc.

Objetivos:
- Comprender la diferencia entre funciones y métodos
- Aprender funciones básicas de propósito general
- Conocer métodos útiles de strings
- Entender cuándo usar cada uno

Conceptos Clave:
- Función: Código reutilizable que realiza una tarea específica
- Método: Función que pertenece a un objeto específico
- len(): Función para obtener la longitud
- upper(), find(), replace(): Métodos de strings
- Operador 'in': Verificar si algo está contenido

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/functions.html
- Métodos de strings: https://docs.python.org/3/library/stdtypes.html#string-methods

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Variable de ejemplo
# =============================================================================
curso = "Curso de Python - Funciones y Métodos"
print(f"Texto de ejemplo: '{curso}'")

# =============================================================================
# EJEMPLO 2: Función len() - Obtener longitud
# =============================================================================
# len() es una función de propósito general
longitud = len(curso)
print(f"Longitud del texto: {longitud} caracteres")
# Salida esperada: Longitud del texto: 37 caracteres

# =============================================================================
# EJEMPLO 3: Método upper() - Convertir a mayúsculas
# =============================================================================
# upper() es un método de la clase str (string)
texto_mayusculas = curso.upper()
print(f"Texto en mayúsculas: '{texto_mayusculas}'")
# Salida esperada: Texto en mayúsculas: 'CURSO DE PYTHON - FUNCIONES Y MÉTODOS'

# =============================================================================
# EJEMPLO 4: Método find() - Buscar subcadena
# =============================================================================
# find() devuelve la posición donde encuentra la subcadena
posicion_python = curso.find("Python")
print(f"Posición de 'Python': {posicion_python}")
# Salida esperada: Posición de 'Python': 10

# Si no encuentra la subcadena, devuelve -1
posicion_java = curso.find("Java")
print(f"Posición de 'Java': {posicion_java}")
# Salida esperada: Posición de 'Java': -1

# =============================================================================
# EJEMPLO 5: Método replace() - Reemplazar texto
# =============================================================================
# replace() crea una nueva cadena con el reemplazo
curso_java = curso.replace("Python", "Java")
print(f"Reemplazando Python por Java: '{curso_java}'")
# Salida esperada: Reemplazando Python por Java: 'Curso de Java - Funciones y Métodos'

# El texto original no cambia (los strings son inmutables)
print(f"Texto original sin cambios: '{curso}'")

# =============================================================================
# EJEMPLO 6: Operador 'in' - Verificar contenido
# =============================================================================
# Verificar si una subcadena está contenida en el texto
contiene_python = 'Python' in curso
print(f"¿Contiene 'Python'?: {contiene_python}")
# Salida esperada: ¿Contiene 'Python'?: True

contiene_java = 'Java' in curso
print(f"¿Contiene 'Java'?: {contiene_java}")
# Salida esperada: ¿Contiene 'Java'?: False

# =============================================================================
# EJEMPLO 7: Más métodos útiles de strings
# =============================================================================
print(f"\nMás métodos de strings:")
print(f"lower(): '{curso.lower()}'")
print(f"title(): '{curso.title()}'")
print(f"strip(): '{curso.strip()}'")
print(f"split(): {curso.split()}")

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estos ejercicios:
# 1. Contar cuántas veces aparece la letra 'a' en tu nombre
# 2. Convertir tu nombre a mayúsculas y luego a minúsculas
# 3. Reemplazar espacios por guiones en una frase
# 4. Verificar si tu nombre contiene ciertas letras

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Las funciones son de propósito general (len(), print(), input())
2. Los métodos pertenecen a objetos específicos (curso.upper())
3. Los strings son inmutables (no se pueden cambiar directamente)
4. Los métodos de strings crean nuevas cadenas, no modifican la original
5. El operador 'in' devuelve True o False
6. find() devuelve la posición o -1 si no encuentra
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Experimentando con diferentes strings
# nombre = "María García López"
# 
# print(f"Nombre original: '{nombre}'")
# print(f"Longitud: {len(nombre)}")
# print(f"Mayúsculas: '{nombre.upper()}'")
# print(f"Minúsculas: '{nombre.lower()}'")
# print(f"Título: '{nombre.title()}'")
# print(f"¿Contiene 'García'?: {'García' in nombre}")
# print(f"Posición de 'García': {nombre.find('García')}")
# print(f"Reemplazar espacios: '{nombre.replace(' ', '_')}'")

# =============================================================================
# DIFERENCIA ENTRE FUNCIONES Y MÉTODOS
# =============================================================================
"""
FUNCIONES (de propósito general):
- len(texto) - Obtener longitud
- print(texto) - Mostrar en pantalla
- input(prompt) - Obtener entrada del usuario
- type(objeto) - Obtener tipo de dato

MÉTODOS (específicos de strings):
- texto.upper() - Convertir a mayúsculas
- texto.lower() - Convertir a minúsculas
- texto.find(subcadena) - Buscar posición
- texto.replace(viejo, nuevo) - Reemplazar
- texto.split() - Dividir en lista
- texto.strip() - Eliminar espacios
"""