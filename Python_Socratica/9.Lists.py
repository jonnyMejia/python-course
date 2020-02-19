# Listas
list=[1,2,3,"a","b"]

# Agrega u item al final de la lista
list.append("x")

# Extiende la lista agregandole todos los items del iterable
# [1, 2, 3, 'a', 'b', 'x', 2, 3, 4, 5]
list.extend([2,3,4,5])

# Inserta un item en una posicion dada
index=3
# [1, 2, 3, 'dato', 'a', 'b', 'x', 2, 3, 4, 5]
list.insert(index,"dato")

# Quita el primer item de la lista cuyo valor sea x
list.remove("x")

# Quita el item en la posicion dada de la lista, Si no se especifica se elimina el ultimo
index=5
list.pop(index)
list.pop()

#Quita todos los elementos de la lista
# list.clear()

# Devuelve el indice del item si esta en la lista, genera error sino lo esta
# 2do,3er indican el inicio y el final para limitar la busqueda
a=list.index("dato",3,5)

# Devuelve el numero de vecs que "x" aparece en la lista
list.count("x")

# Ordena  los items de la lista in situ
# list.sort(key=none,reverse=False)

# Invierte los elementos de la lista
list.reverse()

# Devuelve una copia superficial de la lista
list.copy()

# Muestra la lista desde el indice 1 hasta el final
print(list[1:])

# Muestra la lista desde el indice hasta el indice 8-1
print(list[3:8])

# Muestra desde el inicio hasta el indice 5-1
print(list[:5])

# Muestra una concatenacion
example =[1,2,3]
example2=["a","b","c"]
# [1, 2, 3, 'a', 'b', 'c']
print(example+example2)
