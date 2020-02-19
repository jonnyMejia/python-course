# Tuplas
# Una tupla consiste en un numero de valores separados por comas
t=12345,54321,'hola1'
# (12345, 54321, 'hola1')
print(t)

# Las tuplas pueden anidarse
u=t,(1,2,3,4,5)
# ((12345, 54321, 'hola1'), (1, 2, 3, 4, 5)) 
print(u)

# Las tuplas son inmutables
# t[0]=232 -> Genera error

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
