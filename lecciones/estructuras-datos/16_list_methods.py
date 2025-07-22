"""
Lección 16: Métodos de Listas

Descripción:
Esta lección cubre los métodos más comunes para manipular listas en Python. Aprenderás a agregar, eliminar, buscar, contar, ordenar y copiar elementos en listas.

Objetivos:
- Comprender cómo usar los métodos principales de listas
- Modificar listas agregando, eliminando y ordenando elementos
- Buscar y contar elementos en una lista
- Copiar listas y entender la diferencia entre copia y referencia

Conceptos Clave:
- append(): Agrega un elemento al final
- insert(): Inserta un elemento en una posición específica
- clear(): Elimina todos los elementos
- pop(): Elimina el último elemento
- index(): Devuelve el índice de un elemento
- count(): Cuenta las ocurrencias de un elemento
- sort(): Ordena la lista
- reverse(): Invierte el orden de la lista
- copy(): Crea una copia superficial de la lista

Recursos Adicionales:
- Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- Métodos de listas: https://realpython.com/python-lists-tuples/

Autor: Jairo Cuartas
Fecha: 2025-07-21
"""

# =============================================================================
# EJEMPLO 1: Añadir un elemento a una lista
# =============================================================================
lista = [1, 2, 3]
lista.append(5)
print(lista)  # Salida esperada: [1, 2, 3, 5]

# =============================================================================
# EJEMPLO 2: Insertar un elemento en una posición específica
# =============================================================================
lista.insert(1, 4)
print(lista)  # Salida esperada: [1, 4, 2, 3, 5]

# =============================================================================
# EJEMPLO 3: Limpiar una lista
# =============================================================================
lista.clear()
print(lista)  # Salida esperada: []

# =============================================================================
# EJEMPLO 4: Eliminar el último elemento de una lista
# =============================================================================
lista = [1, 2, 3]
lista.pop()
print(lista)  # Salida esperada: [1, 2]

# =============================================================================
# EJEMPLO 5: Obtener el índice de un elemento
# =============================================================================
lista = [1, 2, 3]
indice = lista.index(1)
print(indice)  # Salida esperada: 0

# =============================================================================
# EJEMPLO 6: Contar la cantidad de ocurrencias de un elemento
# =============================================================================
lista = [1, 2, 3, 1]
cantidad = lista.count(1)
print(cantidad)  # Salida esperada: 2

# =============================================================================
# EJEMPLO 7: Ordenar una lista
# =============================================================================
lista = [3, 1, 2]
lista.sort()
print(lista)  # Salida esperada: [1, 2, 3]

# =============================================================================
# EJEMPLO 8: Ordenar una lista de forma inversa
# =============================================================================
lista = [3, 1, 2]
lista.reverse()
print(lista)  # Salida esperada: [2, 1, 3]

# =============================================================================
# EJEMPLO 9: Copiar una lista
# =============================================================================
lista = [1, 2, 3]
lista_copia = lista.copy()
print(lista_copia)  # Salida esperada: [1, 2, 3]

# =============================================================================
# EJERCICIOS PRÁCTICOS
# =============================================================================
# 1. Crea una lista de nombres y ordénala alfabéticamente
# 2. Elimina todos los elementos de una lista usando clear()
# 3. Cuenta cuántas veces aparece un número en una lista
# 4. Inserta un elemento en la segunda posición de una lista
# 5. Copia una lista y modifica la copia, ¿qué sucede con la original?

# =============================================================================
# CONCEPTOS IMPORTANTES
# =============================================================================
"""
1. Los métodos modifican la lista original, excepto copy()
2. index() lanza un error si el elemento no existe
3. sort() y reverse() modifican la lista en el lugar
4. copy() crea una copia superficial, no profunda
5. Puedes combinar métodos para operaciones más complejas
"""

# =============================================================================
# VARIACIONES Y EXPERIMENTOS
# =============================================================================
# Descomenta para experimentar:
# lista = [5, 3, 8, 1]
# lista.sort(reverse=True)
# print(lista)  # Orden descendente
#
# lista = ['manzana', 'pera', 'uva']
# print(lista.index('pera'))
