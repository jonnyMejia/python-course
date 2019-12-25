# inicializando tupla
x=("rojo","verde","amarillo")
print(x)
# imprimiendo la tupla 
for e in x:
    print(e)

# Las tuplas son immutables, se pueden representar fechas, e incluso se puede anidar
y=("jonny","mejia",(5,"junio",2001))
print(y)

# Se aceden a sus elemetnos de la misma manera que en las listas
print(y[1])

# empaquetado y desempaquetado de tuplas
a="nombre"
b="apellido"
c=(1,"mes",2000)

# Empaquetado-Z consiste en asignar variables  a la tuple, estas no llevan el '()'
alumno=a,b,c

# ('nombre', 'apellido', (1, 'mes', 2000))
print(alumno)

# Desempaquetado-Z consiste en asignar variables  a la tuple, estas no llevan el '()'
m,n,p=alumno
print(n)

# Obtneer el tamaño de la lista 
print(len(alumno))

# Minimo elemento de la lista o tupla min(lista) y max(lista)

# Concatena n copias de la lista ('nombre', 'apellido', (1, 'mes', 2000), 'nombre', 'apellido', (1, 'mes', 
# 2000), 'nombre', 'apellido', (1, 'mes', 2000))
print(alumno*3)

# Concatena las listas o tuplas 
# ('rojo', 'verde', 'amarillo', 'jonny', 'mejia', (5, 'junio', 2001))   
print(x+y)

# Ordenar las listas

# SORTED->ordena la lista pero no la modifica.
num=[1,3,6,4,5,8,2]
copia_ordenada=sorted(num)
# [1, 2, 3, 4, 5, 6, 8]
print(copia_ordenada)
# [1, 3, 6, 4, 5, 8, 2]
print(num)

# SORT->ordena la lista y la modifica.
# [1, 2, 3, 4, 5, 6, 8]
print(num.sort())