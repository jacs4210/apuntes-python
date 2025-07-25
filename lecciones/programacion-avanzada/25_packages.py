"""
Lección 25: Paquetes en Python

Descripción:
Esta lección cubre el concepto de paquetes en Python. Aprenderás a 
organizar módulos en paquetes, importar submódulos y estructurar proyectos grandes de manera profesional.

Objetivos:
- Comprender qué es un paquete y para qué se usa
- Crear y utilizar paquetes propios
- Importar módulos y submódulos desde paquetes
- Estructurar proyectos grandes con paquetes

Conceptos Clave:
- Paquete: Carpeta con un archivo __init__.py y uno o más módulos
- Módulo: Archivo .py dentro de un paquete
- Importación: from paquete import modulo
- Subpaquete: Paquete dentro de otro paquete

Recursos Adicionales:
- Documentación oficial:
  https://docs.python.org/3/tutorial/modules.html#packages
- Tutorial de paquetes:
  https://realpython.com/python-modules-packages/

Autor: Jairo Cuartas
Fecha: 2025-07-24
"""

# =============================================================================
# EJEMPLO 1: ¿Qué es un paquete?
# =============================================================================
# Un paquete es una carpeta que contiene un archivo __init__.py y módulos .py
# Por ejemplo:
# mi_paquete/
#   __init__.py
#   modulo1.py
#   modulo2.py

# =============================================================================
# EJEMPLO 2: Importar un módulo de un paquete
# =============================================================================
# from mi_paquete import modulo1
# modulo1.mi_funcion()

# =============================================================================
# EJEMPLO 3: Importar un submódulo
# =============================================================================
# from mi_paquete.subpaquete import modulo3
# modulo3.otro_funcion()

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Crea un paquete llamado utilidades con un módulo operaciones.py
# 2. En operaciones.py, define funciones suma y resta
# 3. Importa y usa las funciones desde otro archivo

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Un paquete es una carpeta con __init__.py y módulos .py
2. Puedes tener subpaquetes para organizar mejor el código
3. La importación puede ser relativa o absoluta
4. Los paquetes permiten proyectos grandes y escalables
5. __init__.py puede estar vacío o inicializar el paquete
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# from utilidades import operaciones
# print(operaciones.suma(2, 3))