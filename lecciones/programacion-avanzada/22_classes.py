"""
Lección 22: Clases y Objetos (Programación Orientada a Objetos)

Descripción:
Esta lección cubre la creación y uso de clases y objetos en Python. Aprenderás a definir clases, crear instancias (objetos), usar el método __init__ y acceder a atributos y métodos.

Objetivos:
- Comprender qué es una clase y un objeto
- Definir clases con atributos y métodos
- Crear instancias de una clase
- Usar el método __init__ para inicializar objetos

Conceptos Clave:
- Clase: Plantilla para crear objetos
- Objeto: Instancia de una clase
- __init__: Método especial para inicializar objetos
- self: Referencia al objeto actual
- Atributo: Variable asociada a un objeto
- Método: Función asociada a una clase

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/classes.html
- Tutorial de POO: https://realpython.com/python3-object-oriented-programming/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

# =============================================================================
# EJEMPLO 1: Definir una clase y crear objetos
# =============================================================================


class Person:
    def __init__(self, name="", last_name=""):
        self.name = name
        self.last_name = last_name

    def get_name(self):
        print("get_name")


# Crear una instancia de la clase Person
person1 = Person()
person1.name = "Jairo"
person1.last_name = "Cuartas"
print(
    f"Hi, {person1.name} {person1.last_name}"
)  # Salida esperada: Hi, Jairo Cuartas

# Crear otra instancia con parámetros
person2 = Person("John", "Doe")
print(
    f"Hi, {person2.name} {person2.last_name}"
)  # Salida esperada: Hi, John Doe

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Define una clase Animal con atributos nombre y especie
# 2. Crea un método que imprima una presentación del animal
# 3. Crea varios objetos Animal y llama al método de presentación

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Una clase es una plantilla para crear objetos
2. El método __init__ se llama automáticamente al crear un objeto
3. self permite acceder a los atributos y métodos del objeto
4. Puedes crear múltiples instancias de una clase
5. Los métodos pueden usar self para modificar atributos
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
#
# class Animal:
#
#     def __init__(self, nombre, especie):
#         self.nombre = nombre
#         self.especie = especie
#
#     def presentar(self):
#         print(f"Soy {self.nombre} y soy un {self.especie}")
#
# perro = Animal("Max", "perro")
# gato = Animal("Luna", "gato")
# perro.presentar()
# gato.presentar()