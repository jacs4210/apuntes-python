# Añadir un elemento a una lista
lista = [1, 2, 3]
lista.append(5)
print(lista)

# Insertar un elemento en una posición especifica
lista.insert(1, 4)
print(lista)

# Limpiar una lista
lista.clear()
print(lista)

# Eliminar el ultimo elemento de una lista
lista = [1, 2, 3]
lista.pop()
print(lista)

# Obtener el indice de un elemento
lista = [1, 2, 3]
indice = lista.index(1)
print(indice)

# Contar la cantidad de ocurrecias de un elemento
lista = [1, 2, 3, 1]
cantidad = lista.count(1)
print(cantidad)

# Ordernar una lista
lista = [3, 1, 2]
lista.sort()
print(lista)

# Ordernar una lista de forma inversa
lista = [3, 1, 2]
lista.reverse()
print(lista)

# Copiar una lista
lista = [1, 2, 3]
lista_copia = lista.copy()
print(lista_copia)
