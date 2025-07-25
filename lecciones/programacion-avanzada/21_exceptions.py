"""
Lección 21: Manejo de Excepciones (exceptions)

Descripción:
Esta lección cubre el manejo de errores y excepciones en Python. Aprenderás a usar try, except y a capturar errores comunes para evitar que tu programa se detenga inesperadamente.

Objetivos:
- Comprender cómo funciona el manejo de excepciones
- Usar try y except para capturar errores
- Mostrar mensajes personalizados ante errores
- Escribir código más robusto y seguro

Conceptos Clave:
- try: Bloque donde puede ocurrir un error
- except: Bloque que se ejecuta si ocurre un error
- ValueError: Excepción común al convertir tipos
- Robustez: El programa no se detiene ante errores esperados

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/errors.html
- Tutorial de excepciones: https://realpython.com/python-exceptions/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

# =============================================================================
# EJEMPLO 1: Manejo básico de excepciones
# =============================================================================
try:
    age = int(input("Ingrese su edad: "))
    print(age)
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")
# Salida esperada:
# Si el usuario ingresa un número: muestra el número
# Si el usuario ingresa texto: muestra el mensaje de error

# =============================================================================
# EJEMPLO 2: Capturar múltiples excepciones
# =============================================================================
try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Debes ingresar un número entero.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Pide al usuario un número y muestra su inverso. Maneja el error si ingresa cero o texto.
# 2. Pide dos números y muestra la división. Captura errores de tipo y de división por cero.
# 3. Usa try/except para validar la entrada de un correo electrónico (usa input y verifica '@').

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. El bloque try contiene el código que puede fallar
2. except captura el error y permite manejarlo sin detener el programa
3. Puedes tener varios except para diferentes tipos de error
4. Es buena práctica mostrar mensajes claros al usuario
5. El manejo de excepciones hace tu código más robusto y profesional
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# try:
#     lista = [1, 2, 3]
#     print(lista[5])
# except IndexError:
#     print("Índice fuera de rango.")