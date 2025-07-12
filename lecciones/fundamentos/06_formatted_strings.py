"""
Lección 06: Formateo de Strings (String Formatting)

Descripción:
Esta lección introduce diferentes formas de formatear strings en Python.
Aprenderás sobre concatenación tradicional, f-strings (formatted strings),
y otras técnicas para crear texto dinámico con variables.

Objetivos:
- Comprender la concatenación tradicional de strings
- Aprender a usar f-strings (formatted strings)
- Entender las ventajas de cada método
- Crear texto dinámico con variables

Conceptos Clave:
- Concatenación: Unir strings con el operador +
- f-strings: Formateo moderno con f"texto {variable}"
- Variables en strings: Insertar valores dinámicos
- Legibilidad: Hacer el código más fácil de leer

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
- PEP 498: https://www.python.org/dev/peps/pep-0498/

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Variables básicas para formateo
# =============================================================================
nombre = 'Jairo'
apellido = 'Cuartas'
profesion = 'devops engineer'

# =============================================================================
# EJEMPLO 2: Concatenación tradicional (método antiguo)
# =============================================================================
# Usando concatenación normal con el operador +
mensaje_concatenacion = nombre + ' [' + apellido + '] is a ' + profesion
print("Concatenación tradicional:")
print(mensaje_concatenacion)
# Salida esperada: Jairo [Cuartas] is a devops engineer

# =============================================================================
# EJEMPLO 3: F-strings (método moderno y recomendado)
# =============================================================================
# Usando f-strings (formatted strings)
mensaje_fstring = f'{nombre} [{apellido}] is a {profesion}'
print("\nF-string (método moderno):")
print(mensaje_fstring)
# Salida esperada: Jairo [Cuartas] is a devops engineer

# =============================================================================
# EJEMPLO 4: Ventajas de f-strings
# =============================================================================
# F-strings son más legibles y menos propensos a errores
edad = 30
ciudad = 'Bogotá'

# Con concatenación (complejo)
mensaje_complejo = nombre + ' tiene ' + str(edad) + ' años y vive en ' + ciudad
print("\nConcatenación compleja:")
print(mensaje_complejo)

# Con f-strings (simple y claro)
mensaje_simple = f'{nombre} tiene {edad} años y vive en {ciudad}'
print("\nF-string simple:")
print(mensaje_simple)

# =============================================================================
# EJEMPLO 5: Expresiones en f-strings
# =============================================================================
precio = 25.50
cantidad = 3

# Puedes usar expresiones directamente en f-strings
total = f'El total es: ${precio * cantidad:.2f}'
print(f"\n{total}")

# También puedes usar métodos
nombre_mayusculas = f'Nombre en mayúsculas: {nombre.upper()}'
print(nombre_mayusculas)

# =============================================================================
# EJEMPLO 6: Comparación de métodos
# =============================================================================
print(f"\nComparación de métodos:")
print(f"1. Concatenación: '{nombre}' + ' ' + '{apellido}'")
print(f"2. F-string: f'{nombre} {apellido}'")
print(f"3. .format(): '{nombre} {apellido}'.format(nombre=nombre, apellido=apellido)")

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estos ejercicios:
# 1. Crear un mensaje que incluya tu nombre, edad y ciudad usando f-strings
# 2. Calcular el área de un rectángulo y mostrar el resultado formateado
# 3. Crear una tarjeta de presentación con tu información

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. F-strings son más legibles que la concatenación tradicional
2. F-strings permiten usar expresiones directamente
3. F-strings son más eficientes en términos de rendimiento
4. F-strings están disponibles desde Python 3.6+
5. La sintaxis es f"texto {variable} texto"
6. Puedes usar cualquier expresión válida de Python dentro de {}
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Más ejemplos con f-strings
# temperatura = 22.5
# humedad = 65
# 
# # Formateo con decimales
# clima = f"Temperatura: {temperatura:.1f}°C, Humedad: {humedad}%"
# print(f"\nInformación del clima: {clima}")
# 
# # F-strings con condiciones
# es_dia = True
# saludo = f"Buenos {'días' if es_dia else 'noches'}, {nombre}!"
# print(saludo)
# 
# # F-strings con listas
# colores = ['rojo', 'verde', 'azul']
# lista_colores = f"Colores disponibles: {', '.join(colores)}"
# print(lista_colores)

# =============================================================================
# MÉTODOS ALTERNATIVOS (para referencia)
# =============================================================================
# Nota: Aunque f-strings son los más recomendados, existen otros métodos:
# 1. .format() method
# 2. % operator (estilo C)
# 3. Concatenación con +
# Estos se verán en lecciones más avanzadas si es necesario