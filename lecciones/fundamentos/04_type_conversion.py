"""
Lección 04: Conversión de Tipos de Datos (Type Conversion)

Descripción:
Esta lección introduce el concepto de conversión de tipos de datos en Python.
Aprenderás cómo convertir un tipo de dato a otro, especialmente importante
cuando trabajas con la función input() que siempre devuelve strings.

Objetivos:
- Comprender por qué necesitamos convertir tipos de datos
- Aprender las funciones de conversión principales
- Entender cuándo y cómo usar cada conversión
- Resolver problemas comunes con tipos de datos

Conceptos Clave:
- Conversión de tipos: Cambiar un tipo de dato a otro
- int(): Convertir a número entero
- float(): Convertir a número decimal
- str(): Convertir a texto
- input() siempre devuelve string

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/functions.html#int
- Tutorial de tipos: https://docs.python.org/3/tutorial/introduction.html#numbers

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Problema común con input() - siempre devuelve string
# =============================================================================
año_nacimiento = input("Ingresa tu año de nacimiento: ")
print(f"Tipo de dato ingresado: {type(año_nacimiento)}")
# Salida esperada: Tipo de dato ingresado: <class 'str'>
# Nota: Aunque ingreses un número, input() lo trata como texto

# =============================================================================
# EJEMPLO 2: Conversión de string a entero
# =============================================================================
# Convertir el string a entero para poder hacer cálculos
año_nacimiento_int = int(año_nacimiento)
print(f"Tipo después de conversión: {type(año_nacimiento_int)}")
# Salida esperada: Tipo después de conversión: <class 'int'>

# =============================================================================
# EJEMPLO 3: Cálculo con datos convertidos
# =============================================================================
edad = 2025 - año_nacimiento_int
print(f"Tu edad es: {edad}")
# Salida esperada: Tu edad es: [edad calculada]
# Ejemplo: Si naciste en 1990, mostrará: Tu edad es: 35

# =============================================================================
# EJEMPLO 4: Verificación de tipos en todo el proceso
# =============================================================================
print(f"\nResumen de tipos de datos:")
print(f"Entrada original: '{año_nacimiento}' (tipo: {type(año_nacimiento)})")
print(f"Después de int(): {año_nacimiento_int} (tipo: {type(año_nacimiento_int)})")
print(f"Resultado final: {edad} (tipo: {type(edad)})")

# =============================================================================
# EJEMPLO 5: Otras conversiones útiles
# =============================================================================
# Convertir a float (número decimal)
altura_texto = "1.75"
altura_float = float(altura_texto)
print(f"Altura como float: {altura_float} (tipo: {type(altura_float)})")

# Convertir número a string
numero = 42
numero_texto = str(numero)
print(f"Número como string: '{numero_texto}' (tipo: {type(numero_texto)})")

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estos programas:
# 1. Preguntar el peso en kg (como string) y convertirlo a float
# 2. Preguntar la temperatura en Celsius y convertirla a float
# 3. Calcular el área de un círculo (radio como input, convertir a float)

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. input() siempre devuelve string, sin importar qué escriba el usuario
2. int() convierte string a número entero
3. float() convierte string a número decimal
4. str() convierte cualquier dato a texto
5. Las conversiones pueden fallar si el formato no es correcto
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Captura y conversión de diferentes tipos de datos
# peso = input("Ingresa tu peso en kg: ")
# peso_float = float(peso)
# 
# temperatura = input("Ingresa la temperatura en Celsius: ")
# temperatura_float = float(temperatura)
# 
# # Cálculos con datos convertidos
# peso_libras = peso_float * 2.20462
# temperatura_fahrenheit = (temperatura_float * 9/5) + 32
# 
# print(f"Peso en libras: {peso_libras:.2f}")
# print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit:.1f}")

# =============================================================================
# MANEJO DE ERRORES (Concepto avanzado)
# =============================================================================
# Nota: Si el usuario ingresa texto cuando esperas números, el programa fallará
# Ejemplo: int("abc") causará un error
# Más adelante aprenderás a manejar estos errores con try/except