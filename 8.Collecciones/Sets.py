# sets
# Un conjunto no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos

# Creando un conjunto vacio
example=set()
example2=set([1,2,3,4,5])

# Algunos metodos
""" 
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove'
, 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
 """
print(dir(example))

# Agregar elementos 
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorim")
# {False, 42, 3.14159, 'Thorim'}
print(example)

#Tamaño de una collecion
# 4
print(len(example))

#Eliminar elementos
example.remove(42)
print(len(example))

# Cuando el elemento no existe y uso REMOVE, me genera un error
# example.remove("No existe")

# Cuando el elemento no existe y uso DISCARD, no me genera ningun error
example.discard("No exite")

# Limpiar toda la lista dejandola vacia 
example.clear()

# OPERACIONES EN CONJUNTOS
pares={2,4,6,8,10}
impares={1,3,5,7,9}
primos={2,3,5,7,11}

# UNION
# No se puede unir con el operador '+'
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(impares.union(pares))
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(impares|pares)

# INTERSECCION
# {2}
print(pares.intersection(primos))
# {2}
print(impares & pares)

# DIFERENCIA
# Aqui si se puede reemplazar por el operador '-'
# {8, 10, 4, 6}
print(pares.difference(primos))
# {8, 10, 4, 6}
print(pares - primos)
