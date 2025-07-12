"""
Lección 03: Entrada de Datos del Usuario - Función input()

Descripción:
Esta lección introduce la función input(), que permite al programa recibir datos
directamente del usuario a través del teclado. Es fundamental para crear programas
interactivos que respondan a la entrada del usuario.

Objetivos:
- Comprender cómo usar la función input()
- Aprender a capturar datos del usuario
- Entender que input() siempre devuelve un string
- Crear programas interactivos básicos

Conceptos Clave:
- input(): Función para recibir datos del usuario
- Prompt: Mensaje que se muestra al usuario
- String: input() siempre devuelve texto
- Interactividad: El programa espera respuesta del usuario

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/library/functions.html#input
- Tutorial de entrada/salida: https://docs.python.org/3/tutorial/inputoutput.html

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Captura básica de datos del usuario
# =============================================================================
nombre = input("¿Cuál es tu nombre? ")
# El programa se pausa aquí y espera que el usuario escriba algo
# Cuando el usuario presiona Enter, el valor se guarda en 'nombre'

apellido = input("¿Cuál es tu primer apellido? ")
# Nuevamente, el programa espera la entrada del usuario

# =============================================================================
# EJEMPLO 2: Mostrar los datos capturados
# =============================================================================
print("Bienvenido " + nombre + " " + apellido)
# Salida esperada: Bienvenido [nombre] [apellido]
# Ejemplo: Si el usuario ingresa "Juan" y "Pérez"
# Salida: Bienvenido Juan Pérez

# =============================================================================
# EJEMPLO 3: Usando f-strings para mejor formato
# =============================================================================
print(f"¡Hola {nombre} {apellido}! Es un placer conocerte.")
# Salida esperada: ¡Hola [nombre] [apellido]! Es un placer conocerte.

# =============================================================================
# EJEMPLO 4: Verificando el tipo de dato
# =============================================================================
print(f"\nInformación sobre los datos ingresados:")
print(f"Nombre: '{nombre}' (tipo: {type(nombre)})")
print(f"Apellido: '{apellido}' (tipo: {type(apellido)})")
# Salida esperada:
# Información sobre los datos ingresados:
# Nombre: '[nombre]' (tipo: <class 'str'>)
# Apellido: '[apellido]' (tipo: <class 'str'>)

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estos programas:
# 1. Preguntar la edad y mostrar "Tienes X años"
# 2. Preguntar la ciudad y mostrar "Vives en X"
# 3. Preguntar nombre y edad, luego mostrar "Te llamas X y tienes Y años"

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. input() siempre devuelve un string, sin importar qué escriba el usuario
2. El programa se pausa hasta que el usuario presiona Enter
3. El prompt (mensaje) es opcional pero muy útil
4. Puedes usar variables para almacenar la entrada del usuario
5. input() es fundamental para programas interactivos
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Captura de diferentes tipos de información
# edad = input("¿Cuál es tu edad? ")
# ciudad = input("¿En qué ciudad vives? ")
# profesion = input("¿Cuál es tu profesión? ")

# # Mostrar toda la información recopilada
# print(f"\nResumen de tu información:")
# print(f"Nombre: {nombre} {apellido}")
# print(f"Edad: {edad} años")
# print(f"Ciudad: {ciudad}")
# print(f"Profesión: {profesion}")

# # Nota: Aunque el usuario ingrese números, input() los trata como texto
# print(f"Tipo de edad: {type(edad)}")  # Siempre será <class 'str'>