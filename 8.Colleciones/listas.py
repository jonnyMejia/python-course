# inicializando una lista
x=[2,4,4,"Hola",'Mundo']

# imprimiendo la lista [2, 4, 4, 'Hola', 'Mundo']
print(x)

# imprimiendo un elemento con el numero del indice -> Hola
print(x[3])

# cambiando el valor de una lista
# ['Inicio', 4, 4, 'Hola', 'Mundo']
x[0]="Inicio"
print(x)

# Eliminando un elemento 
# ['Inicio', 4, 4, 'Hola']
x.remove('Mundo')
print(x)

# Saber cuantas veces se repite un elemento 
# El numero 4 se repite 2 veces
print(x.count(4))

# Devolver el indice del elemento por argumento
print(x.index('Hola'))

# Recorriendo la lista con un for
""" 
Inicio
4
4
Hola """
for e in x:
    print(e)

# Extendiendo una lista con otra diferente con append
y=["y1","y1"]
#Append agrega una lista como un elemento haciendolo multidimensional
x.append(y)
# Extends agrega todos los valores de la lista y
x.extend(y)
# ['Inicio', 4, 4, 'Hola', ['y1', 'y1'], 'y1', 'y1']
print(x)

# Limpiando una lista
x.clear
print(x)
