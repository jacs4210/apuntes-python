"""
Lección 24: Módulos en Python

Descripción:
Esta lección cubre el concepto de módulos en Python. Aprenderás a crear, 
importar y reutilizar módulos para organizar y estructurar mejor tu código.

Objetivos:
- Comprender qué es un módulo y para qué se usa
- Crear y utilizar módulos propios
- Importar módulos estándar y de terceros
- Reutilizar código en diferentes archivos

Conceptos Clave:
- Módulo: Archivo .py que contiene variables, funciones o clases
- import: Palabra clave para importar módulos
- from ... import ...: Importar elementos específicos de un módulo
- Reutilización: Compartir código entre diferentes programas

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/tutorial/modules.html
- Tutorial de módulos:
  https://realpython.com/python-modules-packages/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

import math

# =============================================================================
# EJEMPLO 1: ¿Qué es un módulo?
# =============================================================================
# Un módulo es un archivo .py que puede contener variables, funciones y clases.
# Por ejemplo, utils.py puede tener funciones auxiliares y ser importado en otros archivos.

# =============================================================================
# EJEMPLO 2: Importar un módulo propio
# =============================================================================
# Supón que tienes un archivo utils.py con una función get_max
# import utils
# numbers = [1, 2, 3]
# print(utils.get_max(numbers))

# =============================================================================
# EJEMPLO 3: Importar módulos estándar
# =============================================================================
print(math.sqrt(16))  # Salida esperada: 4.0

# =============================================================================
# EJEMPLO 4: Importar elementos específicos
# =============================================================================
from math import pi, pow
print(pi)  # Salida esperada: 3.141592...
print(pow(2, 3))  # Salida esperada: 8.0

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Crea un módulo llamado operaciones.py con funciones suma y resta
# 2. Importa el módulo en otro archivo y usa las funciones
# 3. Usa un módulo estándar (random, datetime, etc.) en un ejemplo

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Un módulo es cualquier archivo .py
2. Puedes importar módulos propios, estándar o de terceros
3. import trae todo el módulo; from ... import ... trae elementos específicos
4. Los módulos ayudan a organizar y reutilizar código
5. Puedes usar alias con as (import math as m)
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# import random
# print(random.randint(1, 10))
#
# from datetime import datetime
# print(datetime.now())
