"""
Lección 19: Diccionarios (dictionaries)

Descripción:
Esta lección cubre el uso de diccionarios en Python. Aprenderás a crear, acceder, modificar y recorrer diccionarios, una estructura clave-valor muy útil para almacenar datos relacionados.

Objetivos:
- Comprender cómo crear y acceder a diccionarios
- Modificar valores y agregar nuevas claves
- Recorrer diccionarios con bucles
- Usar métodos útiles de diccionarios

Conceptos Clave:
- Diccionario: Colección de pares clave-valor
- Acceso por clave: diccionario["clave"]
- Métodos: keys(), values(), items(), get(), pop()
- Uso común: Almacenar información estructurada

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Tutorial de diccionarios: https://realpython.com/python-dicts/

Autor: Jairo Cuartas
Fecha: 2025-07-21
"""

# =============================================================================
# EJEMPLO 1: Crear y acceder a un diccionario
# =============================================================================
customer = {
    "name": "Jairo Cuartas",
    "age": 34
}

print(customer["name"])  # Salida esperada: Jairo Cuartas

# =============================================================================
# EJEMPLO 2: Modificar valores de un diccionario
# =============================================================================
customer["name"] = "Angelica Correa"
print(customer["name"])  # Salida esperada: Angelica Correa

# =============================================================================
# EJEMPLO 3: Agregar nuevas claves y valores
# =============================================================================
customer["email"] = "angelica@example.com"
print(customer)  # Salida esperada: {'name': 'Angelica Correa', 'age': 34, 'email': 'angelica@example.com'}

# =============================================================================
# EJEMPLO 4: Recorrer un diccionario
# =============================================================================
for key, value in customer.items():
    print(f"{key}: {value}")
# Salida esperada:
# name: Angelica Correa
# age: 34
# email: angelica@example.com

# =============================================================================
# EJEMPLO 5: Métodos útiles de diccionarios
# =============================================================================
print(customer.get("phone", "No disponible"))  # Salida esperada: No disponible
customer.pop("age")
print(customer)  # Salida esperada: {'name': 'Angelica Correa', 'email': 'angelica@example.com'}

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Crea un diccionario con información de un libro (título, autor, año)
# 2. Modifica el año del libro y agrega una clave 'género'
# 3. Recorre el diccionario e imprime cada clave y valor
# 4. Usa get() para acceder a una clave que no existe

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Los diccionarios almacenan pares clave-valor
2. Las claves deben ser únicas y de tipo inmutable (str, int, tuple)
3. Puedes agregar, modificar y eliminar claves y valores
4. get() permite acceder a claves sin error si no existen
5. items(), keys() y values() facilitan el recorrido
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# persona = {"nombre": "Ana", "edad": 28}
# persona["ciudad"] = "Bogotá"
# for clave in persona.keys():
#     print(clave)
# for valor in persona.values():
#     print(valor)