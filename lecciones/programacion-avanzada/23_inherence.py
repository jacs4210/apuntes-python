"""
Lección 23: Herencia en Programación Orientada a Objetos

Descripción:
Esta lección cubre el concepto de herencia en Python. Aprenderás a crear clases que heredan atributos y métodos de otras clases, a sobrescribir métodos y a extender funcionalidades.

Objetivos:
- Comprender qué es la herencia y para qué se usa
- Definir clases base y clases derivadas
- Heredar y sobrescribir métodos
- Usar super() para acceder a la clase base

Conceptos Clave:
- Herencia: Permite que una clase derive de otra
- Clase base (padre): Clase de la que se hereda
- Clase derivada (hija): Clase que hereda
- Sobrescritura: Redefinir métodos en la clase hija
- super(): Llama métodos de la clase base

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/tutorial/classes.html#inheritance
- Tutorial de herencia:
  https://realpython.com/python-inheritance/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

# =============================================================================
# EJEMPLO 1: Definir una clase base y clases derivadas
# =============================================================================


class Mammal:
    def speak(self):
        print("Some sound")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("Vroom")


cat1 = Cat()
cat1.be_annoying()  # Salida esperada: Vroom

dog1 = Dog()
dog1.speak()  # Salida esperada: Some sound

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Define una clase base Vehiculo y dos clases derivadas: Coche y Moto
# 2. Agrega métodos específicos a cada clase derivada
# 3. Crea objetos de cada clase y llama a sus métodos

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. La herencia permite reutilizar código y extender funcionalidades
2. Una clase derivada hereda todos los métodos y atributos de la base
3. Puedes sobrescribir métodos en la clase hija
4. super() permite llamar métodos de la clase base
5. Es útil para modelar jerarquías y relaciones "es-un"
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# class Vehiculo:
#     def arrancar(self):
#         print("Vehículo arrancado")
#
# class Coche(Vehiculo):
#     def tocar_bocina(self):
#         print("Beep beep!")
#
# coche = Coche()
# coche.arrancar()
# coche.tocar_bocina()
