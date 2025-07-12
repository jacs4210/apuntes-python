"""
Lección 02: Variables y Tipos de Datos Básicos

Descripción:
Esta lección introduce el concepto de variables en Python. Las variables son contenedores
que almacenan datos en la memoria. Aprenderás sobre diferentes tipos de datos básicos
y cómo asignar valores a variables.

Objetivos:
- Comprender qué son las variables
- Conocer los tipos de datos básicos en Python
- Aprender a asignar valores a variables
- Entender la sobreescritura de variables

Conceptos Clave:
- Variable: Contenedor para almacenar datos
- Asignación: Proceso de guardar un valor en una variable
- Tipos de datos: int, float, str, bool
- Sobrescritura: Cambiar el valor de una variable existente

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/introduction.html#variables
- Tipos de datos: https://docs.python.org/3/library/stdtypes.html

Autor: Jairo Cuartas
Fecha: 2025-07-12
"""

# =============================================================================
# EJEMPLO 1: Variables numéricas (int - números enteros)
# =============================================================================
precio = 10
print(f"Precio inicial: {precio}")
# Salida esperada: Precio inicial: 10

# Es posible sobreescribir un valor usando la misma variable
precio = 15
print(f"Precio actualizado: {precio}")
# Salida esperada: Precio actualizado: 15

# =============================================================================
# EJEMPLO 2: Variables de punto flotante (float - números decimales)
# =============================================================================
porcentaje = 3.4
print(f"Porcentaje: {porcentaje}%")
# Salida esperada: Porcentaje: 3.4%

# =============================================================================
# EJEMPLO 3: Variables de texto (str - strings)
# =============================================================================
nombre = "Jairo Cuartas"
print(f"Nombre: {nombre}")
# Salida esperada: Nombre: Jairo Cuartas

# =============================================================================
# EJEMPLO 4: Variables booleanas (bool - valores lógicos)
# =============================================================================
existe = True
es_falso = False
print(f"¿Existe?: {existe}")
print(f"¿Es falso?: {es_falso}")
# Salida esperada: 
# ¿Existe?: True
# ¿Es falso?: False

# =============================================================================
# VERIFICACIÓN DE TIPOS DE DATOS
# =============================================================================
print(f"\nTipos de datos:")
print(f"precio ({precio}): {type(precio)}")
print(f"porcentaje ({porcentaje}): {type(porcentaje)}")
print(f"nombre ({nombre}): {type(nombre)}")
print(f"existe ({existe}): {type(existe)}")

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# Intenta crear estas variables:
# 1. Una variable 'edad' con tu edad
# 2. Una variable 'altura' con tu altura en metros
# 3. Una variable 'ciudad' con tu ciudad
# 4. Una variable 'estudiante' con True o False

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Las variables son contenedores que almacenan datos
2. Python infiere automáticamente el tipo de dato
3. Puedes cambiar el valor de una variable (sobrescribir)
4. Los nombres de variables deben ser descriptivos
5. Python es sensible a mayúsculas y minúsculas
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta estas líneas para experimentar:

# # Variables con nombres más descriptivos
# edad_usuario = 25
# temperatura_ambiente = 22.5
# nombre_completo = "María García"
# es_activo = True

# # Verificar tipos
# print(f"Tipo de edad_usuario: {type(edad_usuario)}")
# print(f"Tipo de temperatura_ambiente: {type(temperatura_ambiente)}")
# print(f"Tipo de nombre_completo: {type(nombre_completo)}")
# print(f"Tipo de es_activo: {type(es_activo)}")

